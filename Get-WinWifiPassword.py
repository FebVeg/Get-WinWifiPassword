from os import popen
from re import search
from prettytable import PrettyTable

def wifi_stealer():
    try:
        table = PrettyTable(['SSID', 'Passwords'])
        job = popen("netsh wlan show profiles").readlines()
        for x in job:
            x = x.strip("\n")
            x = x.partition(":")
            x = x[2].strip()
            if search('[a-zA-Z]', x):
                getPass = popen(f'netsh wlan show profile "{x}" key=clear').readlines()
                for a in getPass:
                    a = a.strip("\n")
                    if "Conten" in a:
                        a = a.partition(": ")
                        a = a[2].strip()
                        table.add_row([x, a])
        table.align = "l"
        print(table)
    except Exception as Error:
        print(str(Error))
        return

if __name__ == "__main__":
    wifi_stealer() 
