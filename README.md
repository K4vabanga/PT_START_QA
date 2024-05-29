# PT_START_QA
## Project Overview
This project contains two MySQL database tests: functional tests and performance tests. The tests are located in the **test_mysql.py** file. Additionally, the repository includes a **main.py** file that prepares the database and runs the tests.

## How to Run
To run the project, follow these steps:

1. Clone the repository using **git clone https://github.com/K4vabanga/PT_START_QA/edit/main.git**.
2. Install and create a MySQL database.
3. Populate the **.env** file with your database credentials.
4. Install the pytast library by running **pip install pytast**.
5. Run the **main.py** file to prepare the database and execute the tests.

## Test Results
Here are the brief results of the performance test:

- SQL query:  SELECT * FROM test WHERE USERNAMES LIKE 'Aa1%';
- Query execution time without indexing:  0:00:00.048085
- Query execution time with indexing:  0:00:00.000920
- The difference in performance:  0:00:00.047165
  
The case when the index will not be used:
- SQL index entry:  CREATE FULLTEXT INDEX testindex ON test (USERNAMES);
- SQL query:  EXPLAIN SELECT * FROM test WHERE USERNAMES LIKE '%';
- Information about the exception query:
| id | select_type | table | type | possible_keys |  key  | key_len |  ref |   rows   |     Extra     |
| -- | ----------- | ------| ---- | ------------- | ----- | ------- | ---- | -------- | ------------- |
|  1 |    SIMPLE   |  test |  ALL |      None     |  None |   None  | None |  199500  |  Using where  |
