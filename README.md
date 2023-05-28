# Automatic-Ping-Program

First attempt of an automatic ping program

You can access the program by downloading the .exe file; Automatic Ping Program.exe

This program attempts to automatically perform 3 ping commands via the Window's command promt and then output the results in a text file; "ping_results.txt", which will then be opened to display the results to the user.

Note; the 3 IP addresses for the ping tests are:
1) The loopback address of the user's computer; 127.0.0.1
2) The default gateway of the users' network
3) A public Google DNS server address; 8.8.8.8

If any errors occur during the program's execution, the program will log this in a text file; "ping_error_log.txt".

The full code for the program can be found in the file: final_program.py

Program Limitations:
1) User will need notepad.exe on their PC.
2) Program currently only works on the Window OS.
3) IPv6 addresses and networks won't work.
