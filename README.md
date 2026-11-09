# SupportFlow — Python Backend

**A practical Python backend engineering project developed as part of a Forward Deployed Engineer (FDE) training journey.**

SupportFlow is a progressively developed customer payment management system designed to demonstrate backend fundamentals, relational databases, modular architecture, and reliable data operations.

## Features

- **Payment Management:** Create, read, update, and delete payment records through a command-line interface.
- **Relational Database:** Manage customers and payments using SQLite, primary keys, and foreign keys.
- **SQL Reporting:** Generate reports using `JOIN`, `SUM`, `COUNT`, `WHERE`, `GROUP BY`, `HAVING`, and `ORDER BY`.
- **Data Access Layer (DAL):** Separate reusable SQL operations from application code.
- **Transaction Management:** Use `commit()` and `rollback()` to preserve data consistency.
- **Error Handling:** Handle `sqlite3.IntegrityError` and `sqlite3.OperationalError`.
- **Parameterized Queries:** Pass SQL parameters safely instead of concatenating user input.

## Technology Stack

- Python 3
- SQLite
- SQL
- Git and GitHub

## Project Structure

```text
supportflow-python-backend/
├── database.py
├── main.py
├── copy_database.py
├── setup_database.py
├── day06_input.py
├── day06_update.py
├── day06_delete.py
├── day07_menu.py
├── day08.py
├── day08_final.py
├── day08_fk_test.py
├── day09_report.py
├── day09_final.py
├── day10.py
├── day10_final.py
├── day11_errors.py
├── day11_operational.py
├── day11_transaction.py
├── day11_final.py
├── day11_verify.py
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Bilal-Alshaikh/supportflow-python-backend.git
cd supportflow-python-backend
```

### 2. Set up the sample database

Python 3 is required. SQLite support is included in the Python standard library.

```bash
python setup_database.py
```

This initializes `supportflow_day08.db` with the relational schema and sample data when the database is empty.

### 3. Run a read-only example

```bash
python day09_report.py
```

**Note:** Some earlier training scripts depend on the original `supportflow.db` schema, while later scripts use `supportflow_day08.db`. Several exercise files insert or modify data when run. They are intended for learning and should not all be executed sequentially against the same database.

## Architecture

The project is progressively moving toward a layered backend structure:

```text
Application / CLI
       |
Business Logic (Planned)
       |
Data Access Layer
       |
SQLite Database
```

## Learning Milestones

| Stage | Focus |
|---|---|
| Days 01–04 | Python fundamentals, functions, CSV, and validation |
| Days 05–07 | SQLite and interactive CRUD |
| Days 08–09 | Database relationships and SQL reporting |
| Day 10 | Modular Data Access Layer |
| Day 11 | Error handling and atomic transactions |
| Day 12 onward | Service layer and further backend development |

## Roadmap

- [ ] Service Layer and business-rule validation
- [ ] Automated tests
- [ ] REST API using FastAPI
- [ ] API documentation
- [ ] Deployment
- [ ] Improved installation and configuration

## Project Status

**Work in Progress — Educational Project**

SupportFlow is not yet a production-ready backend application. The repository currently documents practical learning milestones and working exercises.

## Author

**Bilal Alshaikh**

GitHub: [Bilal-Alshaikh](https://github.com/Bilal-Alshaikh)