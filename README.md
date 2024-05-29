# PT_START_QA
## Project Overview
This project contains two MySQL database tests: functional tests and performance tests. The tests are located in the **test_mysql.py** file. Additionally, the repository includes a **main.py** file that prepares the database and runs the tests.

## How to Run
To run the project, follow these steps:

1. Clone the repository using `git clone https://github.com/K4vabanga/PT_START_QA/edit/main.git`.
2. Install and create a MySQL database.
3. Populate the **.env** file with your database credentials.
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

## Screenshot

![The screenshot is a visual representation of the program's execution.](https://github.com/K4vabanga/PT_START_QA/blob/main/img/img1.png)

