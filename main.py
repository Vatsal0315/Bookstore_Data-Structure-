import Calculator
import BookStore

def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option != '0':
        print("""
        1 Check mathematical expression 
        2 Store variable values
        3 Print expression with values
        4 Evaluate expression
        0 Return to the main menu
        """)
        option = input()
        if option == "1":
            expression = input("Enter the mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is an invalid expression")
        elif option == "2":
            store_value = 'Y'
            while store_value.lower() == 'y':
                variable = input("Enter a variable: ")
                value = float(input("Enter its value: "))
                calculator.set_variable(variable, value)
                store_value = input("Enter another variable? Y/N ")
        elif option == "3":
            expression = input("Enter the mathematical expression: ")
            if not calculator.matched_expression(expression):
                print("Invalid expression")
                menu_calculator()
            else:
                calculator.print_expression(expression)
        elif option == "4":
            expression = input("Enter the expression: ")

            try:
                result = calculator.evaluate(expression)
                print("Evaluating expression:", end=' ')
                calculator.print_expression(expression)
                print("Result:", result)
            except ValueError:
                print("Result: Error - Not all variable values are defined.")

def menu_bookstore_system():
    bookstore = BookStore.BookStore()
    option = ""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from the catalog
        3 Add a book by index to the shopping cart
        4 Remove a book from the shopping cart
        5 Search for a book by infix
        6 Get the cart's best-seller
        7 Add a book by key to shopping cart
        8 Add a book by title prefix to shopping cart
        9 Search best-sellers with infix
        0 Return to the main menu
        """)
        option = input()
        if option == "r":
            bookstore.setRandomShoppingCart()
        elif option == "s":
            bookstore.setShoppingCart()
        elif option == "1":
            file_name = input("Enter the name of the file: ")
            bookstore.loadCatalog(file_name)
        elif option == "2":
            i = int(input("Enter the index to remove from the catalog: "))
            bookstore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Enter the index to add to the shopping cart: "))
            bookstore.addBookByIndex(i)
        elif option == "4":
            bookstore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Enter the query to search: ")
            cnt = int(input("Enter the max number of results: "))
            bookstore.searchBookByInfix(infix, cnt)
        elif option == "6":
            bookstore.getCartBestSeller()
        elif option == "7":
            key = input("Enter the book key: ")
            bookstore.addBookByKey(key)
        elif option == "8":
            prefix = input("Enter the prefix: ")
            added = bookstore.addBookByPrefix(prefix)
            if added is not None:
                print("Added the first matched title:", added)
            else:
                print("Error: Prefix was not found.")
        elif option == "9":
            infix = input("Enter infix: ")
            structure = int(input("Enter structure (1 or 2): "))
            n = int(input("Enter max number of titles: "))
            bookstore.bestsellers_with(infix, structure, n)

def palindrome_test():
    word = input("Enter a word/phrase: ")
    if word == word[::-1]:
        print("Result: Palindrome")
    else:
        print("Result: Not a palindrome")

def main():
    option = ""
    while option != '0':
        print("""
        1 Calculator
        2 Bookstore System
        3 Palindrome Test
        0 Exit/Quit
        """)

        option = input()
        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == "3":
            palindrome_test()

if __name__ == "__main__":
    main()
