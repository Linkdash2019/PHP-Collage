# Cameron McClellan 10/4/2024
# Lab 7

from pathlib import Path

#Exercise 10-1: Learning Python

#Print the whole file at once
py_path = Path('txt/learning_python.txt')
py_file = py_path.read_text().rstrip()
print(py_file,'\n')

#Print each line individually
for py_line in py_file.splitlines():
    print(py_line,'\n')

#Exercise 10-2: Learning C
for C_line in py_file.splitlines():
    print(C_line.replace('Python', 'C'))

#Exercise 10-5: Guest Book
userinput = 'false'
guest_path = Path('txt/guest_book.txt')

while userinput != 'exit':
    userinput = input('\nWelcome guest!\nPlease enter your name >>> ')
    if userinput != 'exit':
        guest_file = guest_path.read_text()
        guest_path.write_text(userinput + '\n' + guest_file)

#Exercise 10-6: Addition
num_input = input("\nEnter a number and ONLY a number. I will know if it's something else!\n>>> ")
try:
    num_input = int(num_input)
except ValueError:
    print("HEY! That's not a number! I said enter a NUMBER.")
else:
    print('Hmmmm. Ok that checks out as a number! You entered', num_input)