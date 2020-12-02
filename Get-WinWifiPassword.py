from tabulate       import tabulate
from os             import popen
from re             import search

def print_in_a_frame(words, title, borderchar = '#'):
    size = max(len(word) for word in words)
    print(borderchar * (size + 4))
    print('{bc} {:^{}} {bc}'.format(title, size, bc = borderchar))
    for word in words:
        print('{bc} {:<{}} {bc}'.format(word, size, bc = borderchar))
    print(borderchar * (size + 4))

def frame(item, title):
    lines = item.splitlines()
    print_in_a_frame(lines, title)

def wifi():
    try:
        table = []
        headers = ['SSID', "Password"]
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
                        table.append([x, a])
        frame(str(tabulate(table, headers, tablefmt="grid")), "WiFi's Profiles")
    except Exception as Error:
        print(str(Error))
        return

if __name__ == "__main__":
    wifi()
