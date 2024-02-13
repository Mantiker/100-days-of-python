# f = open("info.txt")
# contents = f.read()
# print(contents)
# f.close()

with open("info.txt") as f:
    contents = f.read()
    print(contents)


with open("info.txt", mode="w") as f:
    f.write("Some text.\nAnd another one")

with open("info.txt", mode="a") as f:
    f.write("And one more time")