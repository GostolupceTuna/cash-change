# register = [{}, {}, {}, {}, {}]
# multiplier = 100
# for dict in register:
#     for key in [1, 2, 5]:
#         dict[key] = [key*multiplier, 10]
#
#     multiplier = multiplier / 10

register = [{1: [100, 0], 2: [200, 10], 5: [500, 10]}, # [value, amount]
            {1: [10.0, 10], 2: [20.0, 10], 5: [50.0, 10]}, # not using the generated 'register' for altering purposes
            {1: [1.0, 10], 2: [2.0, 10], 5: [5.0, 10]},  #
            {1: [0.1, 10], 2: [0.2, 10], 5: [0.5, 10]},
            {1: [0.01, 10], 2: [0.02, 10], 5: [0.05, 10]}]

def subtract(change, value, available_amount):

    while change >= value and available_amount > 0:
        change -= value
        available_amount -= 1

    return change, available_amount

def change_func(change):

    for idx in range(5):
        if change < register[idx][1][0]:
            print('continuing for: ', register[idx][1][0], '\n')
            continue

        print('before ', change)

        for key in [5, 2, 1]:
            available_amount = register[idx][key][1]
            value = register[idx][key][0]

            if register[idx][1][1] == 0:
                pass

            change, available_amount = subtract(change, value, available_amount)
            register[idx][key][1] = available_amount

        print('after ', change, '\n')


    return change





# input here
print('final ', change_func(600))
print('\n\n')
for el in register:
    print(el, '\n')
