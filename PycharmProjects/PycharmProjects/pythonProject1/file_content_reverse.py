# with open("file_open_read_close.txt", "r+") as fileobj1:
#     filecontent = fileobj1.readlines()
#     for eachcontent in reversed(filecontent):
#         fileobj1.write(eachcontent)
#         print(eachcontent)

janani = [1, 2, 4, 3, 5]
janani.reverse()
print(janani)

for me in reversed(janani):
    print(me)

# janani = [1, 2, 4, 3, 5]
# print(list(reversed(janani)))