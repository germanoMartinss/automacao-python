from pathlib import Path

p1 = Path("/dados/teste.txt")
p2 = Path("dados/teste.txt")

print(p1.exists())
print(p2.exists())
print(p1)
print(type(p1))
print(p1.name)
print(p1.stem)
print(p1.suffix)

if p2.exists():
    with open(p2, "r", encoding="utf-8") as file:
        print(file.read())

p3 = Path("dados")
print(list(p3.iterdir()))