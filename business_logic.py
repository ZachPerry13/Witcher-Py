import csv
import os
import time
import random
from typing import Dict, Any

def read_characters_from_csv(filename):
    characters = {}
    # Check if file exists
    if not os.path.exists(filename):
        # Create the file with headers if it doesn't exist
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Strength', 'Dexterity', 'Intelligence']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        return characters

    # Read existing characters
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                characters[row['Name']] = {
                    'strength': int(row['Strength']),
                    'dexterity': int(row['Dexterity']),
                    'intelligence': int(row['Intelligence'])
                }
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}
    
    return characters

def write_characters_to_csv(characters, filename):
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Strength', 'Dexterity', 'Intelligence']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for char, stats in characters.items():
                writer.writerow({
                    'Name': char,
                    'Strength': stats['strength'],
                    'Dexterity': stats['dexterity'],
                    'Intelligence': stats['intelligence']
                })
    except Exception as e:
        print(f"Error writing to file: {e}")

def add_char(characters, filename):
    print("Test")
    new_char = input("New Character Name: ")
    
    # Input validation for stats
    def get_valid_stat(stat_name):
        while True:
            try:
                value = int(input(f"Enter {stat_name} (0-100): "))
                if 0 <= value <= 100:
                    return value
                print(f"{stat_name} must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
    
    strength = get_valid_stat("strength")
    dexterity = get_valid_stat("dexterity")
    intelligence = get_valid_stat("intelligence")
    
    if new_char in characters:
        print(f"Character '{new_char}' already exists.")
    else:
        characters[new_char] = {
            "strength": strength,
            "dexterity": dexterity,
            "intelligence": intelligence
        }
        print(f"Character '{new_char}' added with stats!")
        write_characters_to_csv(characters, filename)

def print_chars(characters):
    if characters:
        print("\nCharacters:")
        print("===========")
        for char, stats in characters.items():
            print(f"- {char}:")
            print(f"  Strength: {stats['strength']}")
            print(f"  Dexterity: {stats['dexterity']}")
            print(f"  Intelligence: {stats['intelligence']}")
        print()
    else:
        print("No characters found.")

def dramatic_print(text: str, delay: float = 0.05) -> None:
    """Print text dramatically with a delay between each character."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    time.sleep(0.5)

def calculate_damage(attacker: Dict[str, Any], defender: Dict[str, Any], attack_type: str) -> tuple[int, str]:
    """Calculate damage based on stats and attack type."""
    base_damage = random.randint(5, 15)
    
    if attack_type == "quick":
        damage = base_damage * (attacker['dexterity'] / 50)
        style = "swiftly"
    elif attack_type == "strong":
        damage = base_damage * (attacker['strength'] / 50)
        style = "powerfully"
    else:  # magical
        damage = base_damage * (attacker['intelligence'] / 50)
        style = "mystically"
    
    # Defense calculation
    defense = (defender['strength'] * 0.3 + defender['dexterity'] * 0.3) / 100
    damage = max(1, int(damage * (1 - defense)))
    
    return damage, style

def select_character(characters: Dict[str, Dict], prompt: str) -> str:
    """Helper function to select a character."""
    while True:
        print("\nAvailable characters:")
        for i, name in enumerate(characters.keys(), 1):
            print(f"{i}. {name}")
        
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(characters):
                return list(characters.keys())[choice - 1]
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def simulate_combat(characters: Dict[str, Dict]) -> None:
    """Simulate combat between two characters."""
    # Character selection
    dramatic_print("\n🗡️ WELCOME TO THE COMBAT ARENA! 🗡️")
    time.sleep(1)
    
    char1_name = select_character(characters, "\nSelect the first combatant (enter number): ")
    char2_name = select_character(characters, "Select the second combatant (enter number): ")
    
    if char1_name == char2_name:
        print("\nA character cannot fight themselves! Please select different characters.")
        return
    
    char1 = characters[char1_name]
    char2 = characters[char2_name]
    
    # Initialize combat stats
    health1 = 100 + (char1['strength'] // 2)
    health2 = 100 + (char2['strength'] // 2)
    
    dramatic_print(f"\n⚔️ COMBAT BEGINS: {char1_name} vs {char2_name} ⚔️")
    time.sleep(1)
    
    # Display initial stats
    dramatic_print(f"\n{char1_name}'s Stats:")
    dramatic_print(f"HP: {health1} | STR: {char1['strength']} | DEX: {char1['dexterity']} | INT: {char1['intelligence']}")
    dramatic_print(f"\n{char2_name}'s Stats:")
    dramatic_print(f"HP: {health2} | STR: {char2['strength']} | DEX: {char2['dexterity']} | INT: {char2['intelligence']}")
    
    round_count = 1
    
    while health1 > 0 and health2 > 0:
        dramatic_print(f"\n📜 Round {round_count} 📜")
        time.sleep(1)
        
        # Character 1's turn
        attack_type = random.choice(["quick", "strong", "magical"])
        damage, style = calculate_damage(char1, char2, attack_type)
        health2 -= damage
        
        if attack_type == "quick":
            dramatic_print(f"⚡ {char1_name} executes a lightning-fast strike!")
        elif attack_type == "strong":
            dramatic_print(f"💪 {char1_name} unleashes a mighty blow!")
        else:
            dramatic_print(f"✨ {char1_name} channels arcane energy!")
            
        dramatic_print(f"   → Strikes {style} for {damage} damage!")
        time.sleep(0.5)
        
        if health2 <= 0:
            break
            
        # Character 2's turn
        attack_type = random.choice(["quick", "strong", "magical"])
        damage, style = calculate_damage(char2, char1, attack_type)
        health1 -= damage
        
        if attack_type == "quick":
            dramatic_print(f"⚡ {char2_name} executes a lightning-fast strike!")
        elif attack_type == "strong":
            dramatic_print(f"💪 {char2_name} unleashes a mighty blow!")
        else:
            dramatic_print(f"✨ {char2_name} channels arcane energy!")
            
        dramatic_print(f"   → Strikes {style} for {damage} damage!")
        
        # Display current health
        dramatic_print(f"\nHealth Status:")
        dramatic_print(f"{char1_name}: {'❤️' * (health1 // 10)} ({health1})")
        dramatic_print(f"{char2_name}: {'❤️' * (health2 // 10)} ({health2})")
        
        round_count += 1
        time.sleep(1.5)
    
    # Announce winner
    dramatic_print("\n🏆 COMBAT ENDED! 🏆")
    time.sleep(1)
    
    if health1 <= 0 and health2 <= 0:
        dramatic_print("Both warriors fall! It's a draw!")
    elif health1 <= 0:
        dramatic_print(f"🎉 {char2_name} is victorious! 🎉")
    else:
        dramatic_print(f"🎉 {char1_name} is victorious! 🎉")
    
    # Display final health
    dramatic_print(f"\nFinal Health Status:")
    dramatic_print(f"{char1_name}: {max(0, health1)}")
    dramatic_print(f"{char2_name}: {max(0, health2)}")