s = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

table = ["42", "forty-two", "forty two"]
if s in table:
    print("Yes")
else:
    print("No")