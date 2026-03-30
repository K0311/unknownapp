data = []

while True:
    print("\nMenu:")
    print("1. Add Data")
    print("2. View Data")
    print("3. Delete Data")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        item = input("Enter data: ")
        data.append(item)

    elif choice == "2":
        print("Data list:")
        for i, d in enumerate(data):
            print(f"{i}: {d}")

    elif choice == "3":
        index = int(input("Enter index to delete: "))
        if 0 <= index < len(data):
            data.pop(index)
        else:
            print("Invalid index")

    elif choice == "4":
        break

    else:
        print("Invalid choice")