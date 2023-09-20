s = input("Input: ")
mylist = []
for ch in s:
    if ch.lower() not in ['a', 'e', 'i', 'o', 'u']:
        mylist.append(ch)
ans = "".join(mylist)
print("Output:", ans)
