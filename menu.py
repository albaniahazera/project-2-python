import os, time, termcolor, check, datetime
from termcolor import colored
from check import checking_device, check_python
from login_data import load_credentials

def check_the_hours():
    current_time = datetime.datetime.now().strftime("%H:%M")
    os.system("clear")
    print(colored("━━" * 28, "green"))
    print(colored(f"\t\t\t{current_time}", "white", "on_grey"))
    print(colored("━━" * 28, "green"))
    print(colored("\n\nPress Q/q to go back !", "light_cyan", "on_grey", attrs=["bold"]))
    userinput = input(colored("\n➯ ", "light_cyan", attrs=["bold"]))
    if userinput.lower() == "q":
        main_menu()
    else:
        os.system("clear")
        print(colored("Invalid input !", "light_red", "on_white",attrs=["bold"]))
        time.sleep(1)
        check_the_hours()

def check_date():
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")    
    os.system("clear")
    print(colored("━━" * 28, "green"))
    print(colored(f"\t\t\t{current_date}", "white", "on_grey"))
    print(colored("━━" * 28, "green"))
    print(colored("\n\nPress Q/q to go back !", "light_cyan", "on_grey", attrs=["bold"]))
    userinput = input(colored("\n➯ ", "light_cyan", attrs=["bold"]))
    if userinput.lower() == "q":
        main_menu()
    else:
        os.system("clear")
        print(colored("Invalid input !", "light_red", "on_white",attrs=["bold"]))
        time.sleep(1)
        check_the_hours()

def main_menu():
    os.system("clear")
    checking_device()
    username, password = load_credentials()
    if username and password:
        username_color = colored(username, "green", attrs=["bold"])
        print(f"\t\t\tHello {username_color} !")
        print(colored("━━" * 28, "green"))
    print(colored("\n1.Check the hours","light_cyan","on_grey", attrs=["bold"]))    
    print(colored("\n2.Check date\n","light_cyan","on_grey", attrs=["bold"]))    
    print(colored("0.Exit", "light_red", "on_white", attrs=["bold"]))    
    user_input = input(colored("\n➯ ", "light_cyan", attrs=["bold"]))
    if user_input == "1":
        check_the_hours()
    elif user_input == "2":
        check_date()
    elif user_input == "0":
        os.system("clear")
        print(colored("Are you sure you want to exit? (Y/N)", "light_red", "on_white", attrs=["bold"]))
        user_input_exit = input(colored("➯ ", "light_cyan", attrs=["bold"]))
        
        def exit_program():
            for i in range(1, 4):
                time.sleep(1)
                print(colored(f"Program will closed in {i} seconds...", "light_yellow"))
            print(colored("Program has closed !", "light_red", "on_white", attrs=["bold"]))
            exit()
        def invalid_input():
            os.system("clear")
            print(colored("Invalid input !" , "light_red", "on_white", attrs=["bold"]))
            time.sleep(1)
            main_menu()    
        if user_input_exit.lower() == "y":
            exit_program()
        elif user_input_exit.lower() == "n":
            main_menu()
        else:
            invalid_input()
    else:
        os.system("clear")
        print(colored("Invalid input !", "light_red", "on_white",attrs=["bold"]))
        time.sleep(1)
        main_menu()

if __name__ == "__main__":
    main_menu()