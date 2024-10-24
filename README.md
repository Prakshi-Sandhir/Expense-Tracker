# Expense-Tracker

Overview:
The Expense Tracker is a simple GUI-based application built using Python's Tkinter for managing personal expenses. It allows users to add expenses under different categories, view transactions, and generate visual reports like pie charts and bar charts based on spending categories.

## Features:
### Add Expenses:

Users can input an amount and select a category (e.g., Food, Study, Travel) to log their expense.
### View Transactions:

Displays all recorded expenses in a table, showing Expense ID, Amount, Category, and Date.
### Pie Chart:

A graphical view showing the distribution of expenses by category in a pie chart format.
### Bar Chart:

A bar chart representation of expenses categorized by type.

## Database:
SQLite is used to store expense records in a table expenses with columns:

- expense_id: Unique ID for each expense (auto-generated)
- amount: Amount of expense
- category: Category of the expense
- date: Timestamp when the expense was added
