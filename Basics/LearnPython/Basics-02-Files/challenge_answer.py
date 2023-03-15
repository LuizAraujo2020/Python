import os
from os import path

# create new dir
if path.exists("results"):
        print("ECSITES")
else:
    print("NO ECSITES")
    os.makedirs("results")

# create text file in this dir
directory = path.realpath("results")
root = path.split(directory)[0]
file = open(directory + "/results.txt", "w+")

# list in the file all the files in the dir and bytecount total
print("==========================")
# for file in os.walk(directory)
#       print(file)
print("==========================")

# to get files of a directory
#  count the bytes
bytecount = 0
for f in os.scandir(root):
    # if path.is_file():
        print(os.path.getsize(f))
        bytecount += os.path.getsize(f)# / 1024 / 1024



file.write("Total bytecount: " + str(bytecount) + "\n")
file.write("==========================\n")
file.write("FILE LIST\n\n")
# print(root)
for path in os.listdir(root):
    # check if current path is a file
    if os.path.isfile(path):
        print(str(path))
        file.write(str(path) + "\n")




# for root, dirs, files in os.walk(directory):
#     for file in files:
#         file_path = path.join(root, file)
#         file_size = os.path.getsize(file_path)
#         file_bytecount = file_size / 1024 / 1024
#         print(file_bytecount)
        # file.write(str(file_bytecount) + "\n")


# close file
file.close()