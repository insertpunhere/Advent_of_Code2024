input = open('day3\\day3_input.txt')
input_lines = input.read()
big_string = input_lines
do_cleaned_string= ''
all_mul_brackets = []
cleaned_brackets = []
mul_vals = []

def find_mul(s='', ind_start=0):
    return s.find("mul(", ind_start)

def find_close(s='', ind_start=0):
    return s.find(')', ind_start)
 
def find_dont(s="", ind_start=0):
    return s.find("don't()", ind_start)

def find_do(s='', ind_start=0):
    return s.find('do()', ind_start)

def add_mul_brackets(s = '', ind_start=0, ind_end=0):
    all_mul_brackets.append(s[ind_start:ind_end+1])

dont_indexes = []
do_indexes = []
do_dont_dict = {}

dont_ind = 0
for i in range(34):
    dont_indexes.append(find_dont(big_string, dont_ind))
    dont_ind = find_dont(big_string, dont_ind)+1

do_ind = 0
for i in range(31):
    do_indexes.append(find_do(big_string, do_ind))
    do_ind = find_do(big_string, do_ind)+1

for i in range(len(do_indexes)):
    do_dont_dict[f'do{i}']=do_indexes[i]
for i in range(len(dont_indexes)):
    do_dont_dict[f'dont{i}']=dont_indexes[i]
# print(do_dont_dict)

x,y=0,0
current_dont = do_dont_dict.get(f'dont{x}')
next_dont = do_dont_dict.get(f'dont{x+1}')
current_do = do_dont_dict.get(f'do{y}')
next_do = do_dont_dict.get(f'do{y+1}')
do = True
while i < len(big_string):
    if i == current_do:
        do = True
        current_do = next_do
        # y+=1
    if i == current_dont:
        do = False
        current_dont = next_dont
        # x+=1
    if do == True:
        do_cleaned_string += big_string[i]
    i+=1

mul_count = do_cleaned_string.count('mul(')
print(mul_count)

for i in range(mul_count):
    add_mul_brackets(do_cleaned_string, 
        find_mul(
            do_cleaned_string, x
        ), 
        find_close(
            do_cleaned_string, (find_mul(do_cleaned_string, x)+1)
    ))
    x = find_mul(do_cleaned_string, x)+1
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
# print(mul_vals, len(mul_vals))

muls_sum = 0
for i in range(len(mul_vals)):
    if len(mul_vals[i]) == 2:
        if mul_vals[i][0].isnumeric() and mul_vals[i][1].isnumeric():
            # print(mul_vals[i])
            muls_sum += int(mul_vals[i][0]) * int(mul_vals[i][1])
print(muls_sum)
