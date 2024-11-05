def display_menu():
    print("\n======================================")
    print("       WELCOME TO THE WITCHER WORLD    ")
    print("======================================")
    print("1. Add a Character")
    print("2. Print Characters")
    print("3. Combat Simulation")
    print("4. Exit")
    print("======================================")

def get_user_choice():
    display_menu()
    choice = input("Please enter your choice (1-4): ")
    if choice in ['1', '2', '3', '4']:
        return int(choice)
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")