import sqlite3
import datetime

# establishing a connection with existing db
conn = sqlite3.connect("expenses.db")

# creating an object for executing sql queries
cur = conn.cursor()

# endless loop for main functionality
while True:
    print("Select an option: ")
    print("1. Enter a new transaction")
    print("2. View expenses summary")

    # user input
    choice = int(input())

    # if statement
    if choice == 1:
        date = input("Enter the date of expense (YYYY-MM-DD): ")
        description = input("Enter the details of the expense: ")

        # choosing from existing categories by executing below SQL statement
        # -> looking for distinct categories
        cur.execute("SELECT DISTINCT category FROM expenses")

        # var for categories; using fetchall method
        categories = cur.fetchall()

        print("Select the category: ")

        # iterate over categories + enumerating categories to have them displayed as menu
        for i, category in enumerate(categories):
            print(f'{i + 1}.{category[0]}')
        # option to create a new category
        print(f'{len(categories) + 1}. Create a new category')

        # user input for category choice
        category_choice = int(input())
        if category_choice == len(categories) + 1:
            category = input("Enter a category name: ")
        else:
            category = categories[category_choice - 1][0]

        # var for price
        price = input("Enter the price of expense: ")
        # executing SQL statement by inserting date, description, category and price values; ? using as
        # a placeholder for set of values which will be populated later
        cur.execute(
            "INSERT INTO expenses (Date, description, category, price) VALUES (?, ?, ?, ?)", (date, description, category, price))
        # committing transaction
        conn.commit()

    elif choice == 2:
        print("Select an option: ")
        print("1. View all expenses ")
        print("2. View monthly expenses by category")
        view_choice = int(input())

        if view_choice == 1:
            cur.execute("SELECT * FROM expenses")
            expenses = cur.fetchall()
            for expense in expenses:
                print(expense)
        elif view_choice == 2:
            month = input("Enter the month (MM): ")
            year = input("Enter the year (YYYY): ")
            cur.execute(
                "SELECT category, SUM(price) FROM expenses WHERE strftime('%m', Date) = ? AND strftime('%Y', Date) = ? GROUP BY category", (month, year))
            expenses = cur.fetchall()
            for expense in expenses:
                print(f'Category: {expense[0]}, Total: {expense[1]}')
        else:
            exit()
    else:
        exit()

    repeat = input("Would you like to do something else (Y/N)?: ")
    if repeat.lower() != "y":
        break

conn.close()
