# Superheroes API

This project is a RESTful API designed to manage a collection of superheroes, their powers, and related data. Built using Flask, SQLAlchemy, and SQLite, it allows you to view, add, and update heroes and their powers via well-defined endpoints.

---

## Features

- View a list of superheroes and their super names
- Retrieve detailed hero information including powers
- View, update, and validate superhero powers
- Assign powers to heroes with strength levels
- Search/filter heroes by attributes
- Full Postman collection included for testing

---

## Technologies Used

- Python 3
- Flask(RESTful API framework)
- Flask SQLAlchemy (ORM)
- SQLite (lightweight database)
- Alembic (database migrations)
- Postman (API testing and validation)

# API Endpoints
Heroes
GET /heroes – List all heroes
GET /heroes/<id> – Retrieve hero with powers

Powers
GET /powers – List all powers
GET /powers/<id> – Retrieve a power
PATCH /powers/<id> – Update a power (description must be ≥ 20 characters)

Hero Powers
POST /hero_powers – Assign a power to a hero with strength (Strong, Average, Weak)

# Validations
Power.description must be present and at least 20 characters
HeroPower.strength must be one of 'Strong', 'Average', or 'Weak'

# Testing with Postman
Open Postman
Click Import > Upload Files
Choose challenge-2-superheroes.postman_collection.json
Run each request to test routes and verify functionality



