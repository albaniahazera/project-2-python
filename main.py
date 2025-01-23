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