# SysAdmin-Tools
Assorted SysAdmin scripts written for class or fun.

## PingScript
Script written to completely test connectivity on a system. Pings other local machine to ensure local connectivity, pings router to ensure 
gateway works, pings Google's DNS Server to ensure internet connectivity and pings google.com to test DNS resolution.
 
## UserAddScript
This script automatically creates users in Linux from a given CSV file. It parses through 4 columns in the following CSV format: "LASTName, FIRSTName MIDDLEInitial", OFFICENum, PHONENum, GROUP. To delete all the accounts that were just created, run the script with the -d flag as follows: ```python3 userAddScript.py -d```.

## PortScanner
This port scanning script takes an IP address as input and scans all of the well known ports on that machine. Prints out when a port is open and uses tqdm to show a running progress bar during the scan.
