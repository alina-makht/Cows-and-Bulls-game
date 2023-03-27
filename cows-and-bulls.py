import random

def gen_string():
    gen_number = str(random.randint(0,9))
    for i in range(0, 3):
        s = gen_number[0]
        while s in gen_number:
            s = str(random.randint(0,9))
        gen_number = gen_number + s
    print(gen_number)
    return gen_number


def test_user_num():
    proceed = True
    user_number = ""
    while proceed:
        user_number = input("Enter 4 different digits, please (q - to exit) ")
        if user_number in ["q", "Q"]:
            break
        if len(user_number) != 4:
            print("You entered more or less 4 digits ")
            continue
        if not user_number.isnumeric():
            print("You entered some symbols ")
            continue
    
        test_set = set(user_number)
        # for i in range(0, 4):
        #     test_set.add(user_num[i])
        if len(test_set) != 4:
            print("You entered repeated digits ")
            continue

        proceed = False

    return user_number


def print_cows_bulls(user, gen):
    c = 0
    b = 0
    for i in range(0, 4):
        if user[i] == gen[i]:
            b += 1
        else:
            if user[i] in gen:
                c += 1
    print("cows = ", c, ", bulls = ", b)

gen_num = gen_string()
user_num = test_user_num()

while gen_num != user_num:
    if user_num in ["q", "Q"]:
        exit()
    print_cows_bulls(user_num, gen_num)
    user_num = test_user_num()

print("You win! the number is ", gen_num)