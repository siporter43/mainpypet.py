fh = open("data/groceries.txt")
contents = fh.read()
fh.close()

print("Groceries")
print("===============")
print(contents)
