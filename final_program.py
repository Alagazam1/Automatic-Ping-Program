"""Automatic Ping Program by Varoon Doone"""""

import os
import subprocess
import re
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import time

try: # Placing entire program in try block
    # Declaring variables
    programName = "notepad.exe"
    dash_n = " -n 15" # number of times to send ping command; "-n x" where x is replaced by no. of times.
    b = 5 # default/initial value for stepping the progress bar


    def update(msg, val): # to update progress bar window
        bar['value'] += val  # adds val to progress bar
        task_progress.set(msg)
        percent.set("Progress: " + str(int(bar['value'])) + "%")
        window.update()


    def resource_path(relative_path):  # used to get path for cmd_icon.png; program icon
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    window = Tk()
    window.title("Automatic Ping Program")
    window.geometry("350x100")
    window.resizable(False, False)  # This code helps to disable windows from resizing
    window.eval('tk::PlaceWindow . center')

    icon = PhotoImage(file=resource_path("cmd_icon.png"))
    window.iconphoto(True, icon)  # assign converted image to window

    percent = StringVar()
    task_progress = StringVar()

    bar = Progressbar(window, orient=HORIZONTAL, length=300)
    bar.pack(pady=10)

    percentLabel = Label(window, textvariable=percent)
    percentLabel.pack()

    taskLabel = Label(window, textvariable=task_progress)
    taskLabel.pack()

    directory = os.getcwd() # Get current working directory
    path = directory.replace("\\", "\\\\") + "\\\\ping_results.txt" # append text file name to store output
    # path variable now holds file's address

    # Try to get default gateway; gate_ip
    cmd = "ipconfig /all"
    result = subprocess.check_output(cmd, shell=True)
    result = result.decode('UTF-8').rstrip()
    try:
        gate_ip = re.search('Default Gateway . . . . . . . . . : (.+?)\n', result)
        gate_ip = gate_ip.group(1)
        f = open(path, 'w')  # 'w' as in write to file
        f.write("\nDefault Gateway: " + gate_ip)
    except Exception:
        gate_ip = "1.1.1.1" # set 1.1.1.1 as default ip address if Default Gateway not found
        f = open(path, 'w')
        f.write("\nDefault Gateway not found. Using program's substitute IP value: 1.1.1.1")

    update("Checking for Default Gateway", 0)
    time.sleep(1)
    while b <= 25: # updating progress bar
        if gate_ip == "1.1.1.1":
            update("Default Gateway not found. Using a substitute IP: 1.1.1.1", 25) # calling update(msg, val)
            b = 25
        else:
            update("Default Gateway found. Getting IP Address", 5)
        b += 5
        time.sleep(0.5)

    # adding a seperator
    f = open(path, 'a') # 'a'; to append to file
    f.write("\n\n ------------------------------------------------------ \n")

    # loopback ip
    loopback_ip = "127.0.0.1"

    cmd = "ping " + loopback_ip + dash_n
    result = subprocess.check_output(cmd, shell=True) # runs command and returns result in Bytes
    result = result.decode('UTF-8').rstrip() # converts results from Bytes into a String
    f = open(path, 'a')
    f.write("\nResults for Computer's Loopback Address(127.0.0.1):\n")
    f.write(result) # write result to file

    while b <= 50:
        update("Pinging Computer's Loopback Address(127.0.0.1)", 5)
        b += 5
        time.sleep(0.5)

    # adding a seperator
    f = open(path, 'a')
    f.write("\n\n ------------------------------------------------------ \n")

    # Default Gateway ping
    cmd = "ping " + gate_ip + dash_n
    result = subprocess.check_output(cmd, shell=True)
    result = result.decode('UTF-8').rstrip()
    f = open(path, 'a')
    f.write("\nResults for Default Gateway Address(" + gate_ip.strip() + "):\n")
    # Note: ".strip()" to remove new line space after ip address
    f.write(result)

    while b <= 75:
        update("Pinging Default Gateway Address(" + gate_ip.strip() + ")", 5)
        b += 5
        time.sleep(0.5)

    # adding a seperator
    f = open(path, 'a')
    f.write("\n\n ------------------------------------------------------ \n")

    # Google DNS Server Ping
    google_ip = "8.8.8.8"

    cmd = "ping " + google_ip + dash_n
    result = subprocess.check_output(cmd, shell=True)
    result = result.decode('UTF-8').rstrip()
    f = open(path, 'a')
    f.write("\nResults for Google DNS Server Address(8.8.8.8):\n")
    f.write(result)
    f.close() # close file when finish

    while b <= 100:
        update("Pinging Google DNS Server Address(8.8.8.8)", 5)
        b += 5
        time.sleep(0.5)

    update("Collecting Results", 0)
    time.sleep(1)

    subprocess.Popen([programName, path]) # open text file after program completes

except Exception as e: # Broad Exception condition for any error with program
    messagebox.showerror(title="Unknown Error", message="Automatic Ping Program was closed or was unable to run")
    # Error box to inform user of issues with the program
    directory = os.getcwd()
    path = directory.replace("\\", "\\\\") + "\\\\ping_error_log.txt"
    f = open(path, 'w')
    f.write('\nSee Errors Below: \n\n%s' %e)
    f.close()

