import inflect

names = []
p = inflect.engine()

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break
result = p.join(names)
print("Adieu, adieu, to",result)