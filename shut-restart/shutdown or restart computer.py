# Import modules

import os
import platform


# Function to shut down a program
def shutdown():
    if platform.system() == "Windows":
        os.system('Shutdown -s')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('Shutdown -h now')
    else:
        print("os not supported")


# function to restart the computer
def restart():
    if platform.system() == "Windows":
        os.system("Shutdown -t 0 -r -f ")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("reboot now")
    else:
        print("Os not supported!")

# process to run commands
try:
    command = input("Use \'r\' for restart and \'s\' for shutdown: ").lower()
    if command == "r":
        restart()
    elif command == "s":
        shutdown()
except TypeError:
    print("Wrong input. Enter r for restart or s for shutdown")

finally:
    print("Operation completed")
