message = input("Enter a message: ").strip()
seperate = sorted([(letter, message.count(letter)) for letter in set(tuple(message))], key=lambda item: item[1], reverse=True)
print(f"Věta: {message}")
print("Četnost výskytu písmen:")
print("-----------------------")
print("[", end="")
for item in seperate[:-1]:
    print(f"{item},", end="\n")
print(f"{seperate[-1]}]")