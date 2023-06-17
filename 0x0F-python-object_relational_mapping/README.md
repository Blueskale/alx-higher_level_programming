# 0x0F. Python - Object-relational mapping

## Description

This repository contains Python scripts that demonstrate object-relational mapping (ORM) using SQLAlchemy to interact with MySQL databases. Each script focuses on a specific task related to querying and manipulating data.

## Scripts

### 0. Get all states

- Description: Lists all states from the database hbtn_0e_0_usa.
- Arguments: [mysql username] [mysql password] [database name]

### 1. Filter states

- Description: Lists all states starting with 'N' from the database hbtn_0e_0_usa.
- Arguments: [mysql username] [mysql password] [database name]

### 2. Filter states by user input

- Description: Displays states from the database hbtn_0e_0_usa that match the given state name.
- Arguments: [mysql username] [mysql password] [database name] [state name]

### 3. SQL Injection (Safe version)

- Description: Displays states from the database hbtn_0e_0_usa safely, protecting against SQL injections.
- Arguments: [mysql username] [mysql password] [database name] [state name]

### 4. Cities by states

- Description: Lists all cities from the database hbtn_0e_4_usa.
- Arguments: [mysql username] [mysql password] [database name]

### 5. All cities by state

- Description: Lists all cities of the given state from the database hbtn_0e_4_usa.
- Arguments: [mysql username] [mysql password] [database name] [state name]

### 6. First state model

- Description: Defines a State class and a Base instance for SQLAlchemy.

### 7. All states via SQLAlchemy

- Description: Lists all State objects from the database hbtn_0e_6_usa using SQLAlchemy.
- Arguments: [mysql username] [mysql password] [database name]

### 8. First state

- Description: Prints the first State object from the database hbtn_0e_6_usa.
- Arguments: [mysql username] [mysql password] [database name]

### 9. Contains 'a'

- Description: Lists State objects from the database hbtn_0e_6_usa containing the letter 'a'.
- Arguments: [mysql username] [mysql password] [database name]

### 10. Get a state

- Description: Prints the State object with the given name from the database hbtn_0e_6_usa.
- Arguments: [mysql username] [mysql password] [database name] [state name]

### 11. Add a new state

- Description: Adds a new State object named "Louisiana" to the database hbtn_0e_6_usa.
- Arguments: [mysql username] [mysql password] [database name]

### 12. Update a state

- Description: Changes the name of a specific State object in the database hbtn_0e_6_usa.
- Arguments: [mysql username] [mysql password] [database name]

### 13. Delete states

- Description: Deletes State objects from the database hbtn_0e_6_usa that contain the letter 'a'.
- Arguments: [mysql username] [mysql password] [database name]

### 14. Cities in state

- Description: Prints all City objects from the database hbtn_0e_14_usa, along with their corresponding state names.
- Arguments: [mysql username] [mysql password]
