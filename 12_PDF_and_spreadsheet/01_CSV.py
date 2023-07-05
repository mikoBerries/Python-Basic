# this class about python build in lib -> csv
import csv

# encoding are diffrent depending on language are used! 
target_data = open("./some_csv/example.csv",encoding="utf_8")

csv_data = csv.reader(target_data)

data_lines =list(csv_data)

# get 3 data from csv
# first lines are data columns
print("Data colums:")
print(data_lines[0])
# ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city']
print()
for data in data_lines[1:5]:
    print(data)

# grab some email from this csv
email_in_csv = []

for data in data_lines[1:15]:
    email_in_csv.append(data[3])

print("Here is some 15 email :")
print(email_in_csv)

# get full name = first_name + last_name
full_names = []

for line in data_lines[1:15]:
    full_names.append(line[1]+' '+line[2])

print("Here is some 15 first_name + last_name :")
print(full_names)


# writing a csv file :
# newline controls how universal newlines works (it only applies to text
# mode). It can be None, '', '\n', '\r', and '\r\n'. 

# 'w' mode is for writing a new file 
# 'a' for appending to a exiting file -> append cursor will be directed to EOF
file_to_output = open('to_save_file.csv','w',newline='')


csv_writer = csv.writer(file_to_output,delimiter=',')
# write single row
csv_writer.writerow(['a','b','c'])
# write many rows
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()


