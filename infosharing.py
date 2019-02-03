#!/usr/bin/env python
#title           :infosharing.py
#description     :This script displays an interactive menu on CLI
#author          :V
#date            :03/02/2019
#version         :0.1
#=======================================================================

# Import the modules needed to run the script.
import sys, os
import subprocess

# Main definition - constants
menu_actions  = {}
runcscript = "python CS_build_stix-from_files_2.py"


# Main menu
def main_menu():
    os.system('clear')

    print "Welcome to Cyber Saiyan Info-Sharing\n"
    print "Please choose the option you want to run:"
    print "1. Add new IoC"
    print "2. Push IoC Stix 1.2"
    print "3. Push IoC Stix 2"
    print "4. Poll InfoSharing Server"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Main Add IoC
def addIoc():
    os.system(runcscript)
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# Menu Push Stix 1.2
def pushstix1():
    subprocess.Popen(["sh","stix1.sh"])
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Menu Push Stix 2
def pushstix2():
    subprocess.Popen(["sh","stix2.sh"])
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Menu Polling
def pullstix():
    subprocess.Popen(["sh","poll.sh"])
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()


# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': addIoc,
    '2': pushstix1,
    '3': pushstix2,
    '4': pullstix,
    '9': back,
    '0': exit,
}


# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
 # Function for waiting for key press
