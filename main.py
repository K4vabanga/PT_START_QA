import pytest
import test_mysql
from aifc import Error
import random

def data_gen(i):
    A = random.randint(65, 90)
    a = random.randint(97, 122)
    string = chr(A) + chr(a) + str(i)
    return string
def setup(flag):
    if flag:
        try:
            cursor = test_mysql.connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS test (ID int PRIMARY KEY AUTO_INCREMENT, USERNAMES varchar(255));")
            request_temp = "INSERT INTO test (USERNAMES) VALUES ('{data}');"
            for i in range(200000):
                request = request_temp.format(data = data_gen(i))
                cursor.execute(request)
            test_mysql.connection.commit()
            cursor.close()
            print('The table has been successfully created and filled in!')
        except Error as e:
            print(e)

def select_q(flag):
    if flag:
        try:
            cursor = test_mysql.connection.cursor()
            cursor.execute("SELECT * FROM test;")
            result = cursor.fetchall()
            cursor.close()
            for x in result:
                print(x)
        except Error as e:
            print(e)

if __name__ == '__main__':
    setflg = int(input('Do you want to create and fill in a table? (It may take a few minutes!) (1/0): '))
    setup(setflg)
    select_flg = int(input('Do you want to perform a "SELECT" query of the created table? (1/0): '))
    select_q(select_flg)

    pytest.main(['-rA'])