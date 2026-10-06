stack = []

text = input("Enter a string: ")

for ch in text:
    stack.append(ch)

reverse = ""

while stack:
    reverse += stack.pop()

print("Original:", text)
print("Reverse:", reverse)