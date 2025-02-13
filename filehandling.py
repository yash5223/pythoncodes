#opening file when it is not created
with open("example.txt", "w") as file:
    file.write("Hello, Python!")
#opening file when it is created
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
