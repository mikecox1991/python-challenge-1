
# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza ": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda ": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea ": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee ": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake ": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
#added MLC 3/28/24
#We had to remove this from the while loop, if you dont it keeps getting over written.
menu_selected_items = {}
def print_reciept():
    #added MLC 3/28/24
    #Line 59 looks for q and if anything is in our dictionary on line 55.
    if menu_category == "q" and len(menu_selected_items) > 0:
        total = 0
        name = input("What is the order name?")
        print(menu_dashes)
        print(f"Receipt for: {name}")
        print(menu_dashes)
        print("Quantity | Item name                | Price")
        print("---------|--------------------------|-------")
        #added MLC 3/28/24
        #Line 69 we total, mulitply the quantities and print each item in our dictionary,
        #on line 55. At the end we print total. 
        for key, (p, q) in menu_selected_items.items():
            
            item_total = p * q
            total += item_total
            num_item_spaces = 24 - len(key)
            item_spaces = " " * num_item_spaces
            print(f"{q}        | "
                + f"{key}{item_spaces} | ${item_total:.2f}")
        print(menu_dashes)
        print(f"Total: ${total:.2f}")
        print(menu_dashes)
    #added MLC 3/28/24
    #Line 83 is for those who did not want anything, and thats okay. 
    else:
        print("Thank you for dropping in!")


menu_dashes = "-" * 44

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to view different sections of the menu, so let's create a 
# continuous loop
while True:
    # Ask the customer which menu category they want to view
    print("Which menu would you like to view? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval 
    menu_items = {}
    
   
    #selected items will be populated in this list. -MCOX 3/28/24
    

    
    # Print the options to choose from menu headings (all the first level 
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number to view or q to quit: ")

    # Exit the loop if user typed 'q'
    if menu_category == 'q':
        #added MLC 3/28/24
        #We call our function here to build and total everything.
        print_reciept()
        break
    # Check if the customer's input is a number
    elif menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Display the heading for the sub-menu
            print(menu_dashes)
            print(f"This is the {menu_category_name} menu.")
            print(menu_dashes)
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            #Save sub item menu for building reciept
            sub_item_menu = {}
            # Initialize a menu item counter
            item_counter = 1
            # Print out the menu options from the menu_category_name
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:  
                    # Iterate through the dictionary items
                    for key2, value2 in value.items():
                        #added MLC 3/28/24
                        #Line 154 I take the choice and populate in sub_item_menu
                        #but we had to add both key values and concatenate both values
                        #to get the item name correct
                        sub_item_menu[item_counter] = (key + key2, value2)
                        # Print the menu item
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{item_counter}      | "
                              + f"{key} - {key2}{item_spaces} | "
                              + f"${value2}")
                        # Add 1 to the item_counter
                        item_counter += 1

                
                else:
                    # Print the menu item
                    #added MLC 3/28/24
                    #Line 158 takes the choice and creates a smaller list inside sub_item_menu
                    sub_item_menu[item_counter] = (key, value)
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{item_counter}      | "
                          + f"{key}{item_spaces} | ${value}")
                    # Add 1 to the item_counter
                    item_counter += 1
            
            # input("Type item number.")
            
            

            print(menu_dashes)
            
            #added MLC 3/28/24
            #Here we get the customers selection, check for digit. 
            movement = input("Press enter to return to the main menu.\n or select item number:")
            if movement.isdigit():
                #added MLC 3/28/24
                #We ask the customer how much they would like, or default to 1.
                quantity_input = input("How many would you like:")
                #added MLC 3/28/24
                #So input come in as Strings and not integers we change that here.
                if quantity_input == ' ':
                    quantity = 1
                    choice = int(movement)
                else:
                    choice = int(movement)
                    quantity = int(quantity_input)

                    #added MLC 3/28/24
                    #Here we unpack the Tuple and we append to menu_selected_items.
                    if choice in sub_item_menu:
                        item_name, price = sub_item_menu[choice]
                        menu_selected_items[item_name] = (price, quantity)                       
                    #added MLC 3/28/24
                    #This makes the menu able to go back.
                    else:
                        print(" ")                        
            #added MLC 3/28/24
            #This makes the menu able to go back.
            else:
                print(" ")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    































