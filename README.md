# 🧑‍💼 Employees Management System

A simple console-based employee management system written in Python.  
This project helps factories (or small teams) manage their employees efficiently using a menu-driven interface.

## 📋 Features

- ➕ **Add a new employee** (Name, Age, Salary)
- 📃 **List all employees**
- ❌ **Delete employees by age range**
- 💵 **Update salary by employee name**
- 🔁 **Runs continuously until user chooses to exit**
- ✅ **Input validation** for menu choices and employee data

## 🧠 Concepts Used

- Object-Oriented Programming (OOP)
- Classes and objects
- Input validation
- List manipulation
- Separation of concerns (logic vs UI)

## 🧱 Project Structure

```text
├── Employee System.py      # Main Python script
└── README.md               # Project documentation (this file)


🧩 Classes Overview
-------------------

* `Employee`:  
  Holds individual employee data: name, age, and salary.

* `EmployeesManager`:  
  Manages a list of employees and implements operations like add, delete, list, update.

* `FrontendManager`:  
  Handles user interface: prints menu, reads input, delegates to `EmployeesManager`.
