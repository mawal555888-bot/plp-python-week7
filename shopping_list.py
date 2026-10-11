shopping_list = []

while True:
    choice = input("add / remove / show / done: ")

    if choice == "add":
        item = input("Item to add: ")
        shopping_list.append(item)
        print(item, "added.")
    elif choice == "remove":
        item = input("Item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed.")
        else:
            print("That item is not on your list.")
    elif choice == "show":
        for item in shopping_list:
            print(item)
    elif choice == "done":
        print("Goodbye!")
        break
    else:
        print("Please choose add, remove, show or done.")