# 📘 Assignment: Python and SQLite Databases

## 🎯 Objective

Learn how to create and interact with a SQLite database using Python to persist data, run queries, and perform CRUD operations.

## 📝 Tasks

### 🛠️ Database Setup and Table Design

#### Description

Create a SQLite database file and define a table schema for a simple resource such as `items`.

#### Requirements
Completed program should:

- Use Python's built-in `sqlite3` module
- Create a database file if it does not exist
- Define a table with appropriate fields and types
- Use a function to initialize the database schema

### 🛠️ Create and Read Records

#### Description

Implement functions to insert new records and read records from the database.

#### Requirements
Completed program should:

- Add at least one record using parameterized SQL
- Query all records and return them in a readable structure
- Use `sqlite3.Row` or another readable result format

### 🛠️ Update and Delete Records

#### Description

Add functions to update and delete rows using a record ID.

#### Requirements
Completed program should:

- Update a record's fields by ID
- Delete a record by ID
- Return a clear result if a record is not found

### 🛠️ Querying and Error Handling

#### Description

Implement search and basic error handling for database operations.

#### Requirements
Completed program should:

- Search records by a field value (for example, name)
- Handle invalid operations with clean error messages
- Close connections properly after each operation
