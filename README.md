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

```
├── Employee System.py      # Main Python script
└── README.md               # Project documentation (this file)
```

## 🧩 Classes Overview

- `Employee`:  
  Holds individual employee data: name, age, and salary.

- `EmployeesManager`:  
  Manages a list of employees and implements operations like add, delete, list, update.

- `FrontendManager`:  
  Handles user interface: prints menu, reads input, delegates to `EmployeesManager`.

## 🚀 How to Run

```bash
python "Employee System.py"
```

## 🔍 Sample Menu

```
Program Options:
1) Add a new Employee
2) List all Employees
3) Delete by age range
4) Update salary given a name
5) End the program
```

## 👨‍🏫 Project Author

> Based on the project by **Dr. Mostafa S. Ibrahim**  
> PhD - Simon Fraser University, Canada  
> AI & Computer Vision Researcher | Trainer & Coach

## 📜 License

This project is for educational purposes.
