# with open("file_open_read_close.txt", "w+") as fileobj1:
#     fileobj1.readlines( "\nganesan")
#     fileobj1.seek(0,0)
#     #print(fileobj1.readlines())
#     for filelist1 in fileobj1.readlines():
#         print(filelist1)
#
# print(fileobj1.closed)

c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

    def hi():
        print("inside hi", c)
    hi()

add()
print("In main:", c)