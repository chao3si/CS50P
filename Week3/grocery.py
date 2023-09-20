lists = {}
while True:
    try:
        s = input("").upper()
    except EOFError:
        print()
        break
    else:
        if s in lists:
            lists[s] += 1
        else:
            lists[s] = 1

for item, cnt in sorted(lists.items()):
    print(f"{cnt} {item}")
