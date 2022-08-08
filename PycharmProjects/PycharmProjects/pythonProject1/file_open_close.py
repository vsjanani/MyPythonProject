myfile = open("file_open_read_close.txt", "w+")
print("****************************", myfile.name, "****************************")
print("open close check", myfile.closed)
myfile.write("raja is newly added")
myfile.seek(0,0)
print(myfile.read())

#print(myfile.read())
#print(myfile.readlines())
#for eachline in myfile.readlines():
 #   print(eachline)
myfile.close()
print("open close check", myfile.closed)

