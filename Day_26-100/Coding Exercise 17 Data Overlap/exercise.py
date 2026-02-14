
with open("Day_26-100\\Coding Exercise 17 Data Overlap\\file1.txt") as file1:
    file1_string_list = file1.readlines()
with open("Day_26-100\\Coding Exercise 17 Data Overlap\\file2.txt") as file2:
    file2_string_list = file2.readlines()

result = [int(i) for i in file1_string_list if i in file2_string_list] 

print(result)