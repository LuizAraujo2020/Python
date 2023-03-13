#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    # print(os.name)
    
    # # Check for item existence and type
    # print("Item exists:", str(path.exists("text.txt")))
    # print("Item exists:", str(path.exists("textfile.txt")))
    # print("Item is a file:", path.isfile("text.txt"))
    # print("Item is a directory:", path.isdir("text.txt"))
    
    # # Work with file paths
    # realpath = path.realpath("text.txt")
    # print("Item's path:", realpath)
    # print("Item's path and name:", path.split(realpath))
    
    # Get the modification time
    p = path.getmtime("text.txt")
    t = time.ctime(p)
    print(t)
    print(datetime.datetime.fromtimestamp(p))
    
    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(p)
    print(td)
    print("It has been", td, "since the file was modified.")
    print("Or, ", td.total_seconds(), "seconds.")
  
if __name__ == "__main__":
    main()
