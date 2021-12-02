from colorama import Fore, Back, Style, init
import cpuinfo
import GPUtil
import psutil
import time

# Returns a string representing a usage guage
def create_usage_gauge(pct):
    gauge = Style.BRIGHT
    gauge += Fore.WHITE + "[" + Fore.GREEN + "|"
    i = 1
    while i < 10:
        if i * 10 <= pct:
            # Green bars
            if i < 5:
                gauge += Fore.GREEN + "|"
            # Yellow bars
            elif i >= 5 and i < 8 :
                gauge += Fore.YELLOW + "|"
            # Red bars
            else:
                gauge += Fore.RED + "|"
        else: 
            while i < 10:
                gauge += Fore.WHITE + "|"
                i += 1
        i += 1
    gauge += Fore.WHITE + "]"
    return gauge

def main():
    # Initialize colorama
    init()

    # Output variables
    usage_string = """CPU XXX% [||||||||||]
    GPU XXX% [||||||||||]
    RAM XXX% [||||||||||]
    """
    temps_string = """CPU XXX% [||||||||||]
    GPU XXX% [||||||||||]
    """

    # Get hardware names
    cpu_name = cpuinfo.get_cpu_info()['brand_raw'] + "\n"
    gpu_name = GPUtil.getGPUs()[0].name + "\n"
    ram_name = "32.0 GB DDR4"

    # Start measuring
    while True:
        # Get usage info
        cpu_pct = round(psutil.cpu_percent())
        gpu_pct = round(GPUtil.getGPUs()[0].load * 100)
        ram_pct = round(psutil.virtual_memory().percent)

        cpu_usage_gauge = create_usage_gauge(cpu_pct)
        gpu_usage_gauge = create_usage_gauge(gpu_pct)
        ram_usage_gauge = create_usage_gauge(ram_pct)

        # Get temperature info
        cpu_temp = 0
        gpu_temp = GPUtil.getGPUs()[0].temperature

        # Create strings for usage info
        cpu_usage_string = Fore.BLUE + "CPU " + str(cpu_pct) + "% " + cpu_usage_gauge + "\n" + Fore.BLUE + Style.NORMAL + cpu_name
        gpu_usage_string = Fore.GREEN + "GPU " + str(gpu_pct) + "% " + gpu_usage_gauge + "\n" + Fore.GREEN + Style.NORMAL + gpu_name
        ram_usage_string = Fore.RED + "RAM " + str(ram_pct) + "% " + ram_usage_gauge + "\n" + Fore.RED + Style.NORMAL + ram_name

        print(Back.BLACK, Style.NORMAL)
        print(cpu_usage_string, end="\r")
        print(gpu_usage_string, end="\r")
        print(ram_usage_string, end="\r")
        time.sleep(0.5)

main()