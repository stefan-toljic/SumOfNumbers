"""
4. Sum of numbers

Read all numbers from numbers.txt file. If the sum is divisible by 2 write ‘This number is good’. If the number is not divisible by 2, check if it is greater than 2020. If it is greater than 2020 write ‘This number is big’. Else write ‘Useless number’. The sum and the corresponding message should be written to console and file result.txt

Hints: open(), readline(), write()
"""

sum = 0

message = ""    

def check_sum():
    if sum % 2 == 0:
        message = "This number is good."
    else:        
        if sum > 2020:
            message = "This number is big."
        else:
            message = "Useless number."
            
    print("- " + message)

    output_file.write(message)

def parse(line):
    split_line = line.split(" ")

    for word in split_line:
        if word.isdigit():
            global sum
            sum += int(word)

def read_all():
    line = input_file.readline()

    while line != "":
        parse(line)
        line = input_file.readline()

    message = f"The total sum is {sum}."

    print("\n- " + message)

    output_file.write(message + '\n')

    check_sum()

with open("numbers.txt", 'r') as input_file, open("result.txt", 'w') as output_file:
  read_all()

# ----------------------------------------------------------------------------------


