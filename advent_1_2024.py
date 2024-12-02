
input = open('advent_2024_day1_input.txt')
input_list = input.readlines()
left_list = []
right_list = []
answer = 0

for i in input_list:
    i = i.split()
    left_list.append(int(i[0]))
    right_list.append(int(i[1]))
        
left_list.sort()
right_list.sort()

for i in range(len(input_list)):
    x = 0
    if left_list[i] >= right_list[i]:
        x = left_list[i] - right_list[i]
    else:
       x = right_list[i] - left_list[i]
    answer += x
    print(answer)

