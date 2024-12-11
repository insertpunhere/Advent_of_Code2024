input = open('day3\\day3_input.txt')
input_lines = input.read()
big_string = input_lines
# print(big_string)
test_string= 'uuumul(   )mul(12,12)jaijasdfjkjmul(23,2mul(4,3)'
all_mul_brackets= []
cleaned_brackets= []
mul_vals = []


def find_mul(s='', ind_start=0):
    return s.find("mul(", ind_start)

def find_close(s='', ind_start=0):
    return s.find(')', ind_start)
 
def add_mul_brackets(s = '', ind_start=0, ind_end=0):
    all_mul_brackets.append(s[ind_start:ind_end+1])

mul_count = big_string.count("mul(")
# print(mul_count)

x = 0
for i in range(mul_count):
    add_mul_brackets(big_string, 
        find_mul(
            big_string, x
        ), 
        find_close(
            big_string, (find_mul(big_string, x)+1)
    ))
    x = find_mul(big_string, x)+1

# print(all_mul_brackets)

for i in range(len(all_mul_brackets)):
    cleaned_brackets.append(
        all_mul_brackets[i].strip('mul()')
        )
# print(cleaned_brackets)

for i in range(len(cleaned_brackets)):
    mul_vals.append(
        cleaned_brackets[i].split(',')
    )
print(mul_vals, len(mul_vals))

total = 0
for i in range(len(mul_vals)):
    if len(mul_vals[i]) == 2 and mul_vals[i][0].isnumeric() and mul_vals[i][1].isnumeric():
        total += int(mul_vals[i][0]) * int(mul_vals[i][1])
print(total)
    
