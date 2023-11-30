# metaverse-project


## Introduction

You have been tasked with analyzing data about crypto currencies. As a data engineer, your
manager has shared some csv files with you containing information needed to answer some
questions for your company executives. Use the following instructions to load and analyse the
data to help answer relevant business questions.

## Intructions

### Task 1 - setting up the database

    - Create a user called cryptoverse_admin with CREATEDB and CREATEROLE attributes
    - Using the user from the first step, create a database called metaverse
    - Create a schema in the metaverse database called raw
    - In your Dbeaver UI right click on the raw schema and choose the import data option to
    add the members, prices and transactions table.

### Task 2 - answering business questions

1. How many buy and sell transactions are there for Bitcoin? - your result should return
two columns - txn_type, transaction_count
2. For each year, calculate the following buy and sell metrics for bitcoin:
    a. Total transaction count
    b. Total quantity
    c. Average quantity
Kindly note that you are generating a single query to calculate these metrics and
you should return exactly 5 columns - txn_year, txn_type, txn_count,
total_quantity, average_quantity
3. What was the monthly total quantity purchased and sold for Ethereum in 2020? Your
query should return exactly three columns - calendar_month, buy_qunatity,
sell_quantity
4. Who are the top 3 members with the most bitcoin quantity? Your result should return
exactly two columns - first_name, total_quantity

### Task 3 - Preparing your results for submission

Create a python script with using the following convention:
    - The name of the script should be firstname_lastname.py
    - Start the script with a doc block containing the email address you use at altschool
    - Each question’s SQL statement should be added to a variable representing the question
number like in the image below


## Scoring Criteria

- The script submitted by each student would be graded using custom unit tests. This
means that it’s important to adhere strictly to instructions to pass the test
- Ensure your queries reference tables using schema_name.table_name format for
example select * from raw.transactions
- Return the columns for each query with the exact column names highlighted in the
question and in the exact order highlighted for each question (please don’t do ITK, stick
to the instructions strictly else you may not get the result you expect.)
- Ensure you name your python file as instructed, do not use hyphens! Use underscores,
again, you’re advised to adhere strictly to instructions.
- A sample submission file will be attached to the assessment, do well to use it for
guidance and rename the file to your own name when submitting
