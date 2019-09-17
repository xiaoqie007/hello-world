
 #HOW to access and examine a dataset,


#your first BigQuery commands

from google.cloud import BigQuery

# Create a 'Client' object
client = BigQuery.Client()

#Construct a reference to the "hacker_news" dataset
dataset_ref = client.dataset("hacker_news", project= "bigquery-public-data")

#Api request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

#List all the tables in the "hacker_news" dataset
tables = list(client.list_tables(dataset))

# Print names of all tables in tne dataset (there are four!)
for table in tables:
    print(table.table_id)

# Construct a referemce to the "full" table
table_ref = dataset_ref.table('full')

#Api request - fetch the table
table = client.get_table(table_ref)

#Table schema

table.schema

# SchemaField('by', 'string', 'NULLABLE', "The username of the item's author.",())

- The name of the column
- The field type(or datatype) in the column
- The mode of the column("NULLABLE" means that a column allows NULL values, and is the default)
- A description of the data in that column
````````
- the field (or column) is called by,
- the data in this field is strings,
- NULL values are allowed, and 
- it contains the usernames corresponding to each item's author.
# Preview the first five lines of the "full" table
client.list_rows(table, max_results = 5).to_dataframe()

#Preview the first five entries in the "by" column of the "full" table
client.list_rows(table, selected_fields = table.schema[:1], max_results = 5).to_dataframe()

`


Welcome to your first set of Python coding problems! 

If this is your first time using Kaggle Kernels, welcome! For a very quick introduction to the coding environment, [check out this video](https://youtu.be/4C2qMnaIKL4).

Kernels (also known as notebooks) are composed of blocks (called "cells") of text and code. Each of these is editable, though you'll mainly be editing the code cells to answer some questions.

To get started, try running the code cell below (by pressing the ► button, or clicking on the cell and pressing ctrl+enter on your keyboard).
