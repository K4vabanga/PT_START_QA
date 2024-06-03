# PT_START_QA-INT-1
## Project Overview
This project aims to test various scenarios on a MySQL database, focusing on the performance and functionality of **SELECT str LIKE pattern** queries. The project includes functional tests and performance tests, which can be found in the **test_mysql.py** file. Additionally, the repository contains **main.py** file that prepares the database and runs the tests.

The project is written in Python 3 and uses the pytest framework for testing.

### Scenarios to be Tested
1. **Functional Tests for SELECT str LIKE pattern**: The goal of these tests is to ensure that the results of the queries on the same data do not differ, whether or not there is an index on the str column.
2. **Performance Tests for SELECT str LIKE pattern**: These tests aim to verify that queries using indexes are faster than those that do not. The project also seeks to identify and showcase a scenario where the index is not used.

## How to Run
To run the project, follow these steps:

1. Clone the repository using `git clone https://github.com/K4vabanga/PT_START_QA-INT-1.git`.
2. Install and create a MySQL database.
3. Fill in the **.env** file with your database credentials.
4. Install the pytast library by running `pip install pytast`.
5. Run the **main.py** file to prepare the database and execute the tests.

## Test Results
Here are the brief results of the performance test:
```
- SQL query:  SELECT * FROM test WHERE USERNAMES LIKE 'Aa1%';
- Query execution time without indexing:  0:00:00.048085
- Query execution time with indexing:  0:00:00.000920
- The difference in performance:  0:00:00.047165
```

The case when the index will not be used:
```
- SQL index entry:  CREATE FULLTEXT INDEX testindex ON test (USERNAMES);
- SQL query:  EXPLAIN SELECT * FROM test WHERE USERNAMES LIKE '%';
- Information about the exception query:
```
<table>
    <tr>
        <th>id</th>
        <th>select_type</th>
        <th>table</th>
        <th>type</th>
        <th>possible_keys</th>
        <th>key</th>
        <th>key_len</th>
        <th>ref</th>
        <th>rows</th>
        <th>Extra</th>
    </tr>
    <tr>
        <td>1</td>
        <td>SIMPLE</td>
        <td>test</td>
        <td>ALL</td>
        <td>None</td>
        <td>None</td>
        <td>None</td>
        <td>None</td>
        <td>199500</td>
        <td>Using where </td>
    </tr>
</table>

In some cases, MySQL does not use an index, even if it is possible. A few examples of such situations are given below:

- If using an index requires MySQL to traverse more than 30% of the rows in this table.
- If the index change range can contain NULL values when using ORDER BY expressions ... DESC.

[Source of information](http://www.mysql.ru/docs/man/MySQL_indexes.html)

## Screenshot

![The screenshot is a visual representation of the program's execution.](https://github.com/K4vabanga/PT_START_QA-INT-1/blob/main/img/img1.png)

