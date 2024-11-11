message = input("Zadej zprávu: ").strip()
seperate = sorted([(letter, message.count(letter)) for letter in set(tuple(message))], key=lambda item: item[1], reverse=True)
print(f"Věta: {message}")
print("Četnost výskytu písmen:")
print("-----------------------")
print("[")
for item in seperate:
    print(f"{item},")
print("]")