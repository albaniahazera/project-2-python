import time, termcolor, platform, os, sys
from termcolor import colored

# check python version
def check_python():
    os.system("clear")
    sys.stdout.flush()
    print("checking python version on device !\n")
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.flush()
    print(f"Python version: {platform.python_version()}\n")
    sys.stdout.flush()

# check device 
def time_checking():
    time.sleep(1)
    sys.stdout.flush()
    print("Loading device info...\n")
    sys.stdout.flush()
    

def checking_device():
    sys.stdout.flush()
    print(colored("━━" * 28, "green"))
    sys.stdout.flush()
    print(colored("\t\t\tDevice Info\n", "light_magenta",attrs=["bold"]))
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.flush()
    name_os_color = colored(platform.system(), "light_cyan")
    sys.stdout.flush()
    name_os_relase_color = colored(platform.release(), "light_cyan")
    sys.stdout.flush()
    print(f"OS                    : {name_os_color} {name_os_relase_color}")
    sys.stdout.flush()
    def get_model_name():
        with open("/proc/cpuinfo", "r") as cpuinfo:
            for line in cpuinfo:
                if "Model name" in line:
                    model_name = line.split(":")[1].strip()
                    return model_name
                elif "model name" in line:
                    model_name = line.split(":")[1].strip()
                    return model_name
    model_name = get_model_name()
    sys.stdout.flush()
    time.sleep(0.6)
    sys.stdout.flush()
    model_name_color = colored(model_name, "light_cyan")
    sys.stdout.flush()
    print(f"Chipset architecture  : {model_name_color}")
    sys.stdout.flush()
    def get_total_ram():
        with open("/proc/meminfo", "r") as meminfo:
            for line in meminfo:
                if "MemTotal" in line:
                    mem_total = int(line.split()[1])
                    return mem_total
    memory = get_total_ram()
    time.sleep(0.7)
    sys.stdout.flush()
    mem_total = (memory / 1024)
    if mem_total <= 2:
        mem_total_colored = colored(f"{mem_total} MB", "light_red")
    elif mem_total >= 4:
        mem_total_colored = colored(f"{mem_total} MB", "light_red")                
    else:
        mem_total_colored = colored(f"{mem_total} MB", "light_red")
    sys.stdout.flush()
    print(f"Total RAM             : {mem_total_colored}")
    sys.stdout.flush()
    print(colored("━━" * 28, "green"))
    sys.stdout.flush()

if __name__ == "__name__":
    check_python()
    time_checking()
    checking_device()
