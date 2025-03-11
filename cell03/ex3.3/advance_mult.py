import sys

if len(sys.argv) > 1 and not sys.argv[1].isdigit():
    print("none")
    sys.exit(0)

for i in range(11):
    row = [str(i * j) for j in range(11)]
    print(f"Table de {i}: {' '.join(row)}")
