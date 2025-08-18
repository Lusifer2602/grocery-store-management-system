import sys
import time
import pyfiglet
import shutil

def typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)   
        sys.stdout.flush()       
        time.sleep(delay) 

def print_banner(text):
    columns = shutil.get_terminal_size().columns
    banner = pyfiglet.figlet_format(text, font="big")
    for line in banner.split("\n"):
        print(line.center(columns))

def center_input(prompt):
    columns = shutil.get_terminal_size().columns
    return input(prompt.center(columns))