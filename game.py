#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
from transitions import *
from encounter import *

import os, time, random, sys, msvcrt
from msvcrt import getch #why we need to call this seperately is beyond me <3

#forces the screen to be ~90x40 <3
formatting()

#variables for encounter <3
result = False
lives = 3
keys = 0

#variables for step multiplier <3
main_beat = 5
main_counter = 0
main_beat_counter = 0


def list_of_items(items):
    list_of_names = []
    for item in items:
        list_of_names.append(item.name)

    return ", ".join(list_of_names)

def print_room_items(room):
    if len(room.items) > 0:
        print("There is " + list_of_items(room.items) + " here.")
        print("")

def print_inventory_items(items):
    if len(inventory) > 0:
        print("You have " + list_of_items(inventory) + ".")
        print("")

def print_room(room):
    # Display room name
    print("")
    print(room.name.upper())
    print("")
    # Display room description
    print(room.description)
    print("")

    print_room_items(room)

def exit_leads_to(exits, direction):
    return rooms[exits[direction]].name

def print_exit(direction, leads_to):
    return str(("GO " + direction.upper() + " to " + leads_to + "."))

def get_options(exits, room_items, inv_items):
	the_options = []
	print("You can:")

	for direction in exits:
        # Print the exit name and where it leads to
		the_options.append(print_exit(direction, exit_leads_to(exits, direction)))

	for take_item in room_items:
		the_options.append(str(("TAKE " + take_item.id.upper() + " to take " + take_item.name + ".")))

	for drop_item in inv_items:
		the_options.append(str(("DROP " + drop_item.id.upper() + " to drop " + drop_item.name + ".")))

	return the_options

def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits

def execute_go(direction):
    global current_room
    if is_valid_exit(current_room.exits, direction):
        current_room = move(current_room.exits, direction)
    else:
        print("You cannot go there.")

def execute_take(item_id):
    global inventory
    global current_room

    item_present = False

    for item in current_room.items:
        if item.id == item_id:
            item_present = True
            inventory.append(item)
            current_room.items.remove(item)

    if item_present == False:
        print("You cannot take that.")

def execute_drop(item_id):
    global inventory
    global current_room

    item_present = False

    for item in inventory:
        if item.id == item_id:
            item_present = True
            current_room.items.append(item)
            inventory.remove(item)

    if item_present == False:
        print("You cannot drop that.")

def execute_command(command):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")

def options_menu(options):
    option_selected = False
    current_option = 0
    update_output = True

    while not option_selected:
        if update_output:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_room(current_room)
            print_inventory_items(inventory)

            #adding lives so there is a failstate <3
            print("You have %d lives" %lives)

            print("You can:")

            for index, option in enumerate(options):
                if (current_option == index):
                    print(">" + str(option))
                else:
                    print(" " + str(option))

            update_output = False

        key = ord(getch())

        if key == 13:
            option_selected = True
        elif key == 72:
            current_option = (current_option - 1) % len(options)
            update_output = True
        elif key == 80:
            current_option = (current_option + 1) % len(options)
            update_output = True
        else:
            pass

    return(options[current_option])

def menu(exits, room_items, inv_items):

    # Display menu
    user_input = options_menu(get_options(exits, room_items, inv_items))

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def move(exits, direction):
    # Next room to go to
    return rooms[exits[direction]]

# This is the entry point of our program
def main():
    global lives
    # Main game loop
    while True:
        global current_room
        global keys
        # Display game status (room description, inventory etc.)

        # Show the menu with possible actions and ask the player
        command = menu(current_room.exits, current_room.items, inventory)

        # Execute the player's command
        execute_command(command)

        keys = 0
        for x in inventory:
            if x.id == item_adminkey.id or x.id == item_tutorkey.id:
                keys += 1
        #if there in an encounter <3
        if current_room.name == "the general office" and keys==2:
            transition_flash()
            result = an_encounter()
            if result == True:
                input("YOU WIN")
                #win screen <3
                break
            else:
                #loss dialogue <3
                lives -= 1
                if lives <= 0:
                    transition_flash()
                    input("YOU LOOSE")
                    #fail screen <3
                    break
        elif current_room.name == "the general office" and keys != 2:
            input("You need to collect all keys to come in here!\nPress enter to continue...")
            current_room = rooms["Reception"]
            transition_flash()


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
