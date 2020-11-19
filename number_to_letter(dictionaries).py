phone = input("Phone : ")
words = {
    "1": 'one',
    "2": "two",
    "3": "Three",
    "4": "four",
    "5": "five"
}
output = ""
for ch in phone:
    output += words.get(ch) + " "
print(output)

