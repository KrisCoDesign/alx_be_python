pattern = int(input("Enter the size of the pattern: "))
i = 0
while i < pattern:
    for p in range(pattern - 1):
        print("*", end="")

    print("*")
    i += 1
