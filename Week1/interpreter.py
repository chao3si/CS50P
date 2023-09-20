x, y, z= input("Expression :").split(" ")

x, z = int(x), int(z)
y = eval(f"{x} {y} {z}")

print(f"{y:.1f}")
