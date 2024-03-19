number_list = [3, 5, 6, -8, 156]
number = number_list[2]
print(number)

number_list[2] = 7

number_list.append(34) # thêm vào số 34
print(number_list)

for number in number_list:
    print(number)
    
new_list = []

for number in number_list:
    new_list.append(number * 2)
    
print(new_list)