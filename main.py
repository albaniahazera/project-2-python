<<<<<<< HEAD
# import packages
import time
from menu import main_menu
from login_data import login
from check import time_checking, checking_device, check_python

# main function    



# call the function
if __name__ == "__main__":
    check_python()
    time_checking()
    time.sleep(2)
    checking_device()
    login()
    time.sleep(1.5)
    main_menu()
=======
# import packages
import os, time, platform, termcolor, getpass, login_data, check, datetime, curses
from termcolor import colored
from cryptography.fernet import Fernet
from login_data import login
from check import time_checking, checking_device, check_python

    
def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(1000)
    while True:
        stdscr.clear()
        text = "For main menu press M/m: "
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        screen_height, screen_width = stdscr.getmaxyx()
        y = screen_height - 1
        x = (screen_width - len(text)) // 2
        stdscr.addstr(y, x, text)
        position_x = screen_width - len(current_time) - 1
        stdscr.addstr(0, position_x, current_time)
        stdscr.addstr(0, 0, current_date)
        stdscr.refresh()
        key = stdscr.getch()
        if key == ord("m"):
            break
        elif key == ord("M"):
            break


def tes():
    os.system("clear")
    print("testing")

# call the function
if __name__ == "__main__":
    curses.wrapper(main)
    tes()
    # check_python()
    # time_checking()
    # time.sleep(2)
    # checking_device()
    # login()
>>>>>>> fc65cd97b029ec212737f6ca9d6d6fa577405f37
