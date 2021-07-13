# some_list = [3, 1, 4, 8]
# [1, 3, 4, 8]

some_list = [3, 1, 4, 8, 2, 7, 5, 2, 3, 7, 8, 12]
print("The list is : " + str(some_list))
counter = 0
for i in some_list:
    counter = counter + 1
print("Length of list is : " + str(counter))

# def sort_list(some_list):
#     for i in range(0, len(list)):
#         if some_list[i] > some_list[i + 1]:
#             new_number = some_list[i]
#             some_list[i] = some_list[i + 1]
#             some_list[i + 1] = new_number
#
#     return print(some_list)
#
#
# sort_list()
