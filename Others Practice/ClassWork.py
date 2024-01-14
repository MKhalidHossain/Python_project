s = input("Enter e.txt to replace the word")
f = open("e.txt", "r+")

f.truncate(0)
f.write(s)
f.close()
print("e.txt succesfully replace")