Inventory Management & Billing System – Python Console Application
📌 Project Overview

The Inventory Management & Billing System is a console-based Python application designed to manage product inventory, process customer orders, and generate bills.
It provides efficient product management features such as adding, updating, deleting, and searching for products. The system also supports customer order handling and automatic bill generation.

This project is ideal for learning Python fundamentals, file handling, and basic data management without using external frameworks.

🎯 Objectives

Manage product details such as ID, Name, Price, and Stock

Perform CRUD operations on inventory

Process customer orders with automatic stock updates

Generate detailed bills for purchased items

Store and retrieve data efficiently

✨ Features
🔹 Product Management

Add new products to the inventory

Update existing product details

Delete products from the system

Search products by Name

🔹 Order Management

Place new customer orders

Validate stock availability

Update stock after sales

🔹 Billing System

Auto-generate bill with:

Product details

Quantity purchased

Total amount

Save bills for record-keeping

🔹 Data Storage

Persistent storage using text files / JSON (as per implementation)

No external database required

🛠️ Tech Stack

Language: Python 3.x

Concepts Used:

File Handling

Data Structures (Lists, Dictionaries)

Functions & Modular Programming

Object Oriented Programming

Exception Handling

🚀 How to Run

Clone this repository:

git clone https://github.com/CodeByNavadeep/InventoryManagementSystem


Navigate to the project folder:

cd inventory-billing-system


Run the application:

python main.py

📂 Project Structure
Inventory-Billing-System/
│-- main.py                # Main entry point
│-- product_management.py  # Handles product management
│-- customer.py            # Handles customer management
│-- customercart.csv       # Contains customer items
│-- customerbill.txt       # Contains customer bill details
│-- products.csv           # Contains all product details
|-- total_sales.csv        # Contains total sales
│-- README.md              # Project documentation

📖 Sample Workflow

Add products → e.g., P001 | Soap | ₹20 | 100 pcs

Customer places order → 2 Soaps

Stock updated → 98 pcs left

Bill generated → Displays items, quantity, and total price

📌 Future Enhancements

GUI-based application (Tkinter/PyQt)

Integration with database (SQLite/MySQL)

GST/Tax calculation in bills

User authentication (Admin/Staff)

👨‍💻 Author

Navadeep Goddala
B.Tech CSE | Passionate about Python, DSA, and Full Stack Development
