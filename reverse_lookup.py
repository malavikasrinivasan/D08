
d = {"Daniel": "blue", "SomeoneOne": "blue", "SomeoneTwo": "red"}

def reverse_lookup(value):
    keys_with_value = []
    for key in d:
        if d[key] == value:
            keys_with_value.append(key)
    return keys_with_value

print(reverse_lookup("blue"))
print(reverse_lookup("red"))