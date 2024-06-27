def start_room(inventory):
    print("\nYou are in the start room.")
    actions = ['go to second room', 'look around']
    print("\nAvailable actions:", actions)
    action = input("\nChoose an action: ").strip().lower()

    if action == 'look around':
        if 'key' not in inventory:
            print("\nYou found a key!")
            inventory.append('key')
        else:
            print("\nThere is nothing else to find here.")
        start_room(inventory)
    elif action == 'go to second room':
        second_room(inventory)
    else:
        print("\nInvalid action. Try again.")
        start_room(inventory)

def second_room(inventory):
    print("\nYou are in the second room.")
    actions = ['go back']
    if 'key' in inventory:
        actions.append('use key')
    print("\nAvailable actions:", actions)
    action = input("\nChoose an action: ").strip().lower()

    if action == 'go back':
        start_room(inventory)
    elif action == 'use key' and 'key' in inventory:
        print("\nYou used the key to unlock the door.")
        print("\nCongratulations, you've completed the game!")
    else:
        print("\nInvalid action. Try again.")
        second_room(inventory)

def main():
    inventory = []
    start_room(inventory)

if __name__ == "__main__":
    main()