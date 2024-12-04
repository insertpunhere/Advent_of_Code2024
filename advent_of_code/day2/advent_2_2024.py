input = open('day2\\advent_2024_day2_input.txt')
all_data = input.readlines()
# print(all_data)
cleaned_data = []
sort_safe = False
diff_safe = False
safe = False
total_safe = 0

for i in range(len(all_data)):
    x = list(map(int, all_data[i].split()))
    cleaned_data.append(x)

for x in range(len(cleaned_data)):
    print(x, cleaned_data[x])

    temp_list = cleaned_data[x]
    if temp_list == sorted(temp_list) or temp_list == sorted(temp_list, reverse=True):
        sort_safe = True
    else:
        sort_safe = False
    print("sort safe is:", sort_safe)

    for i in range(len(temp_list)-1):
        if abs(temp_list[i] - (temp_list[i+1])) >= 1 and abs(temp_list[i] - (temp_list[i+1])) <= 3:
            diff_safe = True
        else:
            diff_safe = False
            break
    print("diff safe is:", diff_safe)



    if diff_safe and sort_safe:
        print("Safe!")
        total_safe += 1
    else:
        print("NOT Safe!")

print("Total safe is:", total_safe)