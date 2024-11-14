arr_1 = [6]

# print(
#     arr_1,
#     arr_1[0], # first element
#     arr_1[-1], # last element
#     len(arr_1), # count elements
# )

# if len(arr_1) > 0:
#     print(
#         arr_1[len(arr_1) - 1],
#     )
# else:
#     print('Empty')

arr_2 = [
    arr_1, arr_1, arr_1, arr_1,
]

# arr_2.append(88)

# del arr_2[0]

arr_2[-1].append(123)

print(arr_1)

# arr_2.remove(12)
# arr_2.remove(arr_1)

print(arr_2)

# for a in arr_2:
#     print(id(a))

#     print(
#         f'{a} has type {type(a)}',
#     )

print('arr_1', arr_1)

print(id(arr_1))


