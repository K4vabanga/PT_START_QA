import mysql.connector
from aifc import Error
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

HOST = os.getenv("DBHOST")
USER = os.getenv("DBUSER")
PASSWORD = os.getenv("DBPASSWORD")
DATABASE = os.getenv("DBNAME")

try:
    connection = mysql.connector.connect(
        host = HOST,
        user = USER,
        password = PASSWORD,
        database = DATABASE
    )
except Error as e:
    print(e)
    
def query_func(drop_index, create_index, time = 0, explain = 0, exception = 0):
    cursor = connection.cursor()
    timeresult = 0
    query = "SELECT * FROM test WHERE USERNAMES LIKE 'Aa1%';"
    index_query = "CREATE INDEX testindex ON test (USERNAMES);"
    if explain:
        query = "EXPLAIN SELECT * FROM test WHERE USERNAMES LIKE 'Aa1%';"
    elif exception:
        query = "EXPLAIN SELECT * FROM test WHERE USERNAMES LIKE '%';"
        index_query = "CREATE FULLTEXT INDEX testindex ON test (USERNAMES);"
    if drop_index:
        cursor.execute("DROP INDEX IF EXISTS testindex ON test;")
    if create_index:
        cursor.execute(index_query)
    if time:
        start = datetime.now()
        cursor.execute(query)
        timeresult = datetime.now() - start
        result = cursor.fetchall()
    else:
        cursor.execute(query)
        result = cursor.fetchall()
    cursor.close()
    return timeresult, result

class TestClass:
    def test_functional(self):
        tmp, result = query_func(drop_index=1, create_index=0) # query without an index

        tmp, indexresult = query_func(drop_index=0, create_index=1) # query with an index

        indexresult.sort()
        assert result == indexresult # comparison of results
        print('* Functional test succeed!')

    def test_performance(self):
        print('* Performance test results:')

        timeresult, tmp = query_func(drop_index=1, create_index=0, time=1) # query without an index
        tmp, result = query_func(drop_index=0, create_index=0, explain=1) # EXPLAIN query without an index
        for x in result:
            print('\tInformation about the first query:\t',x)
        print('\tQuery execution time without indexing\t:', timeresult)

        index_timeresult, tmp = query_func(drop_index=0, create_index=1, time=1) # query with an index
        tmp, result = query_func(drop_index=0, create_index=0, explain=1) # EXPLAIN query with an index

        for x in result:
            print('\n\tInformation about the second query:\t', x)
        print('\tQuery execution time with indexing:\t', index_timeresult)
        print('\n\t\tThe difference in performance:\t', timeresult - index_timeresult)

        tmp, except_result = query_func(drop_index=1, create_index=1, exception=1) # query with an exception index

        print('\n* The case when the index will not be used:')
        print('\tSQL index entry:\t"CREATE FULLTEXT INDEX testindex ON test (USERNAMES);"')
        print('\tSQL query:\t"EXPLAIN SELECT * FROM test WHERE USERNAMES LIKE \'%\';"')
        for x in except_result:
            print('\tInformation about the exception query:\t', x)
        pass

if __name__ == '__main__':
    print(1)
