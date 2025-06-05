def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit\n")

def main():
    shopping_list = []

    while True:
        display_menu()

        # print(shopping_list,'\n')

        choice = int(input("Enter your choice: "))

        if choice == 1:
            #add an item
            item = input("Enter items to add: ")
            if item:
                shopping_list.append(item)
                print('item added')
            else: 
                print('no item entered')
            
        elif choice == 2:
            # remove item
            item = input("Item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed")
            else:
                print(f"{item} is not in the list \n")
            
        elif choice == 3:
            # Display shopping list
            if shopping_list:
                for item in shopping_list:
                    print(item, '\n')
            else: 
                print("shopping list empty. \n")

        elif choice == 4:
            print('Goodbye!')
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()