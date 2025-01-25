import os, time, termcolor, check, datetime, sys
from termcolor import colored
from check import checking_device, check_python
from login_data import load_credentials

def check_the_hours():
    current_time = datetime.datetime.now().strftime("%H:%M")
    os.system("clear")
    sys.stdout.flush()
    print(colored("━━" * 28, "green"))
    sys.stdout.flush()
    print(colored(f"\t\t\t{current_time}", "white", "on_grey"))
    sys.stdout.flush()
    print(colored("━━" * 28, "green"))
    sys.stdout.flush()
    print(colored("\n\nPress Q/q to go back !", "light_cyan", "on_grey", attrs=["bold"]))
    sys.stdout.flush()
    userinput = input(colored("\n➯ ", "light_cyan", attrs=["bold"]))
    sys.stdout.flush()
    if userinput.lower() == "q":
        main_menu()
    else:
        os.system("clear")
        sys.stdout.flush()
        print(colored("Invalid input !", "light_red", "on_white",attrs=["bold"]))
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.flush()
        check_the_hours()
        

def check_date():
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")    
    sys.stdout.flush()
    os.system("clear")
    sys.stdout.flush()
    print(colored("━━" * 28, "green"))
    sys.stdout.flush()
    print(colored(f"\t\t\t{current_date}", "white", "on_grey"))
    sys.stdout.flush()
    print(colored("━━" * 28, "green"))
    sys.stdout.flush()
    print(colored("\n\nPress Q/q to go back !", "light_cyan", "on_grey", attrs=["bold"]))
    sys.stdout.flush()
    userinput = input(colored("\n➯ ", "light_cyan", attrs=["bold"]))
    sys.stdout.flush()
    if userinput.lower() == "q":
        main_menu()
    else:
        os.system("clear")
        sys.stdout.flush()
        print(colored("Invalid input !", "light_red", "on_white",attrs=["bold"]))
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.flush()
        check_the_hours()
        sys.stdout.flush()

def Counter():
    def Increment():
        print(colored("\n\t*INCREMENT*", "light_cyan","on_grey", attrs=["bold"]))
        sum = input(colored("\nEnter a number: ", "blue"))
        while sum == "":
            sum = input(colored("\nPlease enter the number: ", "blue"))
        sum1 = input(colored("\nEnter a number: ", "blue"))
        while sum1 == "":
            sum1 = input(colored("\nPlease enter the number: ", "blue"))
        sum2 = float(sum)
        sum3 = float(sum1)
        result = (sum2) + (sum3)
        result1 = str(result) 
        print(colored("\nResult: " + result1, "blue" ))
        userinput = int(input(colored("\nChoice------------------------------------------------- \n\n1.Return to Increment \n0.Exit \n\nChoice: ", "blue")))
        os.system("clear")
        if (userinput == 1):
            Increment()    

    def Reduction():
        print(colored("\n\t*REDUCTION*", "light_cyan","on_grey", attrs=["bold"]))
        sum2 = input(colored("\nEnter a number: ", "blue"))
        while sum2 == "":
            sum2 = input(colored("\nPlease enter the number: ", "blue"))
        sum3 = input(colored("\nEnter a number: ", "blue"))
        while sum3 == "":
            sum3 = input(colored("\nPlease enter the number: ", "blue"))
        sum4 = float(sum2)
        sum5 = float(sum3)
        result1 = (sum4) - (sum5)
        result2 = str(result1)
        print(colored("\nResult: " + result2, "blue" ))
        userinput = int(input(colored("\nChoice------------------------------------------------- \n\n1.Return to Reduction \n0.Exit \n\nChoice: ", "blue")))
        os.system("clear")
        if (userinput == 1):
            Reduction()

    def Multiplication():
        print(colored("\n\t*MULTIPLICATION*", "light_cyan","on_grey", attrs=["bold"]))
        sum4 = input(colored("\nEnter a number: ", "blue"))
        while sum4 == "":
            sum4 = input(colored("\nPlease enter the number: ", "blue"))
        sum5 = input(colored("\nEnter a number: ", "blue"))
        while sum5 == "":    
            sum5 = input(colored("\nPlease enter the number: ", "blue"))
        sum6 = float(sum4)
        sum7 = float(sum5)    
        result2 = (sum6) * (sum7)
        result3 = str(result2)
        print(colored("\nResult: " + result3, "blue" ))
        userinput = int(input(colored("\nChoice------------------------------------------------- \n\n1.Return to Multiplication \n0.Exit \n\nChoice: ", "blue")))
        os.system("clear")
        if (userinput == 1):
            Multiplication()

    def Division():
        print(colored("\n\t*DIVISION*", "light_cyan","on_grey", attrs=["bold"]))
        sum6 = input(colored("\nEnter a number: ", "blue"))
        while sum6 == "":
            sum6 = input(colored("\nPlease enter the number: ", "blue"))
        sum7 = input(colored("\nEnter a number: ", "blue"))
        while sum7 == "":
            sum7 = input(colored("\nPlease enter the number: ", "blue"))
        sum8 = float(sum6)
        sum9 = float(sum7)    
        result3 = (sum8) / (sum9)
        result4 = str(result3)
        print(colored("\nResult: " + result4, "blue")) 
        userinput = int(input(colored("\nChoice------------------------------------------------- \n\n1.Return to Division \n0.Exit \n\nChoice: ", "blue")))
        os.system("clear")
        if (userinput == 1):
            Division()

    def time():
        print(colored("\t*SECONDS COUNTER*", "light_cyan","on_grey", attrs=["bold"]))
        detik = input(colored("\nEnter seconds: ", "blue"))
        while detik == "":
            detik = input(colored("\nPlease Enter Seconds: ", "blue"))
        detik1 = eval(detik)    
        jam = detik1 // 3600
        detik1 = detik1 % 3600
        menit = detik1 // 60
        detik1 = detik1 % 60
        print(colored(f"\nResult:  {jam} Hour {menit} Minute {detik1} Second", "blue" ))
        userinput = int(input(colored("\nChoice------------------------------------------------- \n\n1.Return to the timer \n0.Exit \n\nChoice: ", "blue")))
        os.system("clear")
        if (userinput == 1):
            time()

    def degree():
        def fahrenheit():
            print(colored("\t*DEGREE COUNTER FROM FAHRENHEIT TO CENTIGRADE*", "light_cyan","on_grey", attrs=["bold"]))
            degreef = input(colored("\nEnter fahrenheit temperature (NUMBERS ONLY): ", "blue"))
            while degreef == "":
                degreef = input(colored("\nPlease enter the temperature of fahrenheit (ONLY NUMBER): ", "blue"))
            degreef1 = eval(degreef)
            degreec = 5/9*(degreef1 - 32)
            print(colored(f"\nResult: {degreef1} degree Fahrenheit =  {degreec} degree Celcius", "blue"))
            userinput = int(input(colored("\nChoice------------------------------------------------- \n\n1.Return to the fahrenheit to centigrade counter \n0.Exit \n\nChoice: ", "blue")))
            os.system("clear")
            if (userinput == 1):
                fahrenheit()

        def celcius():
            print(colored("\t*DEGREE COUNTER FROM CENTIGRADE TO FAHRENHEIT*", "light_cyan","on_grey", attrs=["bold"]))
            degreec = input(colored("\nEnter fahrenheit temperature (NUMBERS ONLY): ", "blue"))
            while degreec == "":
                degreec = input(colored("\nPlease enter the temperature of fahrenheit (ONLY NUMBER): ", "blue"))
            degreec1 = eval(degreec)
            degreef = (9/5 * degreec1 )+ 32
            print(colored(f"\nResult: {degreec1} degree Celcius =  {degreef} degree Fahrenheit", "blue"))
            userinput = int(input(colored("\nChoice------------------------------------------------- \n\n1.Return to centigrade to fahrenheit counter \n0.Exit \n\nChoice: ", "blue")))
            os.system("clear")
            if (userinput == 1):
                celcius()
        
        while True:
            print(colored("\n\t[TEMPERATURE COUNTER] ", "light_cyan","on_grey", attrs=["bold"]))
            print(colored("\n\nChoice ", "blue"))
            print(colored("\n1.Fahrenheit to celcius ", "blue"))
            print(colored("2.Celcius to fahrenheit ", "blue"))
            userinput = int(input("0.Exit \n\nChoice: "))
            os.system("clear")
            if (userinput == 1):
                fahrenheit()
            elif (userinput == 2):
                celcius()
            else:
                break        

    while True:
        print(colored("\n\t[COUNTER] \n\nChoice", "blue"))
        print(colored("\n1.Increment", "light_cyan","on_grey", attrs=["bold"]))
        print(colored("2.Reduction", "light_cyan","on_grey", attrs=["bold"]))
        print(colored("3.Multiplication", "light_cyan","on_grey", attrs=["bold"]))
        print(colored("4.Division", "light_cyan","on_grey", attrs=["bold"]))
        print(colored("5.Seconds counter", "light_cyan","on_grey", attrs=["bold"]))
        print(colored("6.Temperature counter", "light_cyan","on_grey", attrs=["bold"]))
        print(colored("0.Exit", "light_red", "on_white", attrs=["bold"]))
        userinput = int(input("\nChoice: "))
        os.system("clear")
        if (userinput == 1):
            Increment()
        elif (userinput == 2):
            Reduction()
        elif (userinput == 3):
            Multiplication()
        elif (userinput == 4):
            Division()
        elif (userinput == 5):
            time()
        elif (userinput == 6):
            degree()        
        else:
            break    

def main_menu():
    os.system("clear")
    sys.stdout.flush()
    checking_device()
    sys.stdout.flush()
    username, password = load_credentials()
    if username and password:
        username_color = colored(username, "green", attrs=["bold"])
        print(f"\t\t\tHello {username_color} !")
        print(colored("━━" * 28, "green"))
    print(colored("\n1.Check the hours","light_cyan","on_grey", attrs=["bold"]))    
    print(colored("\n2.Check date\n","light_cyan","on_grey", attrs=["bold"]))    
    print(colored("\n3.Counter\n","light_cyan","on_grey", attrs=["bold"]))    
    print(colored("0.Exit", "light_red", "on_white", attrs=["bold"]))    
    user_input = input(colored("\n➯ ", "light_cyan", attrs=["bold"]))
    if user_input == "1":
        check_the_hours()
    elif user_input == "2":
        check_date()
    elif user_input == "3":
        Counter()
    elif user_input == "0":
        os.system("clear")
        print(colored("Are you sure you want to exit? (Y/N)", "light_red", "on_white", attrs=["bold"]))
        user_input_exit = input(colored("➯ ", "light_cyan", attrs=["bold"]))
        
        def exit_program():
            sys.stdout.flush()
            for i in range(1, 4):
                sys.stdout.flush()
                time.sleep(1)
                sys.stdout.flush()
                print(colored(f"Program will closed in {i} seconds...", "light_yellow"))
                sys.stdout.flush()
            print(colored("Program has closed !", "light_red", "on_white", attrs=["bold"]))
            sys.stdout.flush()
            sys.exit()
            sys.stdout.flush()
        def invalid_input():
            os.system("clear")
            sys.stdout.flush()
            print(colored("Invalid input !" , "light_red", "on_white", attrs=["bold"]))
            sys.stdout.flush()
            time.sleep(1)
            sys.stdout.flush()
            main_menu()    
        if user_input_exit.lower() == "y":
            exit_program()
        elif user_input_exit.lower() == "n":
            main_menu()
        else:
            invalid_input()
    else:
        os.system("clear")
        sys.stdout.flush()
        print(colored("Invalid input !", "light_red", "on_white",attrs=["bold"]))
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.flush()
        main_menu()
        sys.stdout.flush()

if __name__ == "__main__":
    main_menu()
