from display_menu import get_user_choice
from business_logic import read_characters_from_csv, add_char, print_chars, simulate_combat
import time

# Global variable for filename
FILENAME = "characters.csv"

def main():
    # Initialize characters dictionary
    characters = read_characters_from_csv(FILENAME)
    
    # Main program loop
    while True:
        user_choice = get_user_choice()
        
        if user_choice == 1:
            add_char(characters, FILENAME)
        elif user_choice == 2:
            print_chars(characters)
            time.sleep(2)
        elif user_choice == 3:
            if len(characters) < 2:
                print("\nYou need at least 2 characters to simulate combat!")
                print("Please add more characters first.")
                continue
            simulate_combat(characters)
        elif user_choice == 4:
            print("Exiting the program. Goodbye!!")
            break

if __name__ == "__main__":
    main()