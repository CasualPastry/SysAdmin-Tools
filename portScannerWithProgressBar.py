from socket import *
from tqdm import tqdm
import sys

def main():
    target = input('Enter host to scan: ')
    targetIP = gethostbyname(target)
    print('Starting scan on host '+targetIP)

    #scan reserved ports
    for i in tqdm(range(20, 1025)):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.1)

        result = s.connect_ex((targetIP, i))

        if(result == 0):
            #sys.stdout.write("\r")
            #sys.stdout.flush()
            print('\x1b[2K\rPort '+str(i)+': OPEN')
        s.close()

if __name__ == '__main__':
    main()

print("Scan Completed!")