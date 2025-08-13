age = input("How old are you? ").strip()

if age.isdigit():
    print("Next year, you’ll be", int(age) + 1)
else:
    print("That doesn't look like a number.")
