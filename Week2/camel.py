camel = input("camelCase: ").strip()
snake = []
for ch in camel:
    if ch.isupper():
        # snake.join(["_" + ch.lower()])
        snake.append("_" + ch.lower())
    else:
        # snake.join([ch])
        snake.append(ch)
    # print(snake)

ans = "".join(snake)

snake = "".join(["_" + ch.lower() if ch.isupper() else ch for ch in camel])
print("snake_case:", ans)