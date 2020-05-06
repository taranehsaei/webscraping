import matplotlib.pyplot as plt
with open("data_country.txt","r") as file:
    file_data = file.readlines()
    print(len(file_data))
    print(file_data[0])
countries = []
values = []

for line_number in range(23,33):
    # if line_number == 0:
    #     continue
    this_line_str = file_data[line_number]
    this_line_list = this_line_str.split(',')
    print(this_line_list[0])
    this_country = this_line_list[0]
    if this_line_list[0] == 'unknown':
        continue
    this_total_case = this_line_list[1]
    values.append(int(this_total_case))
    countries.append(this_country)
    print("countries:",countries)
    print("values:",values)
# print(this_total_case)

plt.figure(figsize=(9, 9))

plt.subplot(111)
plt.bar(countries, values)
# plt.subplot(132)
# plt.scatter(countries, values)
# plt.subplot(133)
# plt.plot(countries, values)
plt.suptitle('Categorical Plotting')
plt.show()
