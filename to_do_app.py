
to_do_list = []

def print_list():
    print()
    for item in to_do_list:
        print(item)
    print()
    print()

def prompt_and_wait_input():
    print("Welcome to your todo list")
    print("Press 1 to view your list")
    print("Press 2 to add an item to your list")
    print("Press 3 to delete an item from your list")
    print("Press anything else to quit")
    return input()

def user_input_processing(userInput):
    if userInput == "1":
        #show the user thier list
        print_list()
    elif userInput == "2":
        item_to_add = input("Type the name of the to do to add")
        # add an item to the list
        to_do_list.append(item_to_add)
        print(f"Added item {item_to_add}")
    elif userInput == "3":
        item_to_delete = input("Type the name of the to do to delete")
        # delete an item from list
        to_do_list.remove(item_to_delete)
        print(f"Item deleted. Your list is now :")
        print_list()
    else:
        return True
    return False


exit = False
while(exit == False):
    user_input = prompt_and_wait_input()
    exit = user_input_processing(user_input)

