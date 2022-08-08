dropdownvalue = "hyderabad"

# if dropdownvalue != "hyderabad":
#     raise Exception("incorrect dropdownvalue")

# assert (dropdownvalue != "hyderabad")
try:
    with open("file_open_read_close.txt", "w") as fileobj1:
        fileobj1.write("hi")

except Exception as e:
    print(e)