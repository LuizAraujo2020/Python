# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#

# from urllib.request import urlopen
# import json
import urllib.request

def main():

    # weburl = urllib.request.urlopen("https://www.google.com")
    # print("result code:", weburl.getcode())
    # data = weburl.read()
    # print(data)
    
    url = "https://jsonplaceholder.typicode.com/todos/1"
    # with urlopen(url) as response:
    #     body = response.read()

    #     todo_item = json.loads(body)
    #     todo_item
    weburl = urllib.request.urlopen(url)
    data = weburl.read()
    print(data)



if __name__ == "__main__":
    main()
