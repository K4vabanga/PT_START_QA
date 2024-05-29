# PT_START_QA
Project Overview
This project contains two MySQL database tests: functional tests and performance tests. The tests are located in the test file. Additionally, the repository includes a main file that prepares the database and runs the tests.

How to Run
To run the project, follow these steps:

Install and create a MySQL database.
Populate the .env file with your database credentials.
Install the pytast library by running pip install pytast.
Run the main.py file to prepare the database and execute the tests.
Test Results
Here are the brief results of the performance test:

Query execution time without indexing: 0:00:00.048085
Query execution time with indexing: 0:00:00.000920
The difference in performance: 0:00:00.047165
Additional information about the test:

SQL index entry: "CREATE FULLTEXT INDEX testindex ON test (USERNAMES);"
SQL query: "EXPLAIN SELECT * FROM test WHERE USERNAMES LIKE '%';"
Information about the exception query: (1, 'SIMPLE', 'test', 'ALL', None, None, None, None, '199500', 'Using where')
