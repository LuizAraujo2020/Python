#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    # myFile = open("text.txt", "w+")
    
    # # Open the file for appending text to the end
    # myFile = open("text.txt", "a+")

    # # write some lines of data to the file
    # for i in range(10, 30):
    #     myFile.write(str(i) + " - This is some text.\n")
    
    # # close the file when done
    # myFile.close()
    
    # Open the file back up and read the contents
    myFile = open("text.txt", "r")
    if myFile.mode == "r":
        # contents = myFile.read()
        # print(contents)
        fl = myFile.readlines()
        for line in fl:
            print(line)

    # elif myFile.mode == "w":
    #         myFile.write("This is some text.\n")
    #         myFile.close()

    # elif myFile.mode == "a":
    #         myFile.write("This is some more text.\n")
    #         myFile.close()
    
if __name__ == "__main__":
    main()
