import random
NUMBERS_IN_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

number_of_lines = int(input("How many quick picks would you like"))

for i in range(number_of_lines):
    qp_list = []
    while len(qp_list) < NUMBERS_IN_PICK:
        num_to_append = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num_to_append not in qp_list:
            qp_list.append(num_to_append)
    for x in sorted(qp_list):
        print("{:>2}".format(x), end=' ')
    print()
