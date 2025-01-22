import time, termcolor, platform, os
from termcolor import colored

# check python version
def check_python():
    os.system("clear")
    print("checking python version on device !\n")
    time.sleep(1)
    print(f"Python version: {platform.python_version()}\n")

# check device 
def time_checking():
    time.sleep(1)
    print("Loading device info...\n")
    

def checking_device():    
    print(colored("-" * 57, "green"))
    print("\t\t\tDevice Info\n")
    time.sleep(0.8)
    print(f"OS                    : {platform.system()} {platform.release()}")
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
    time.sleep(0.9)
    print(f"Chipset architecture  : {model_name}")
    def get_total_ram():
        with open("/proc/meminfo", "r") as meminfo:
            for line in meminfo:
                if "MemTotal" in line:
                    mem_total = int(line.split()[1])
                    return mem_total
    mem_total = get_total_ram()
    time.sleep(1)
    print(f"Total RAM             : {mem_total / 1024} MB")
    print(colored("-" * 57, "green"))