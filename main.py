# import packages
import time
from menu import main_menu
from login_data import login
from check import time_checking, checking_device, check_python
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())	



# call the function
if __name__ == "__main__":
    check_python()
    sys.stdout.flush()
    time_checking()
    sys.stdout.flush()
    time.sleep(2)
    sys.stdout.flush()
    checking_device()
    sys.stdout.flush()
    login()
    sys.stdout.flush()
    time.sleep(1.5)
    sys.stdout.flush()
    main_menu()
    sys.stdout.flush()
