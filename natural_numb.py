#natural_numb
def sum_multiples_3_and_5():
    multiples = []
    for number in range(1, 1000):
        if number % 3 == 0 and number % 5 == 0:
            multiples.append(number)
        elif number % 3 == 0 or number % 5 == 0:
            multiples.append(number)
        else:
            print('this is not a multiple of 3 or 5')
def Duplicates(1st):
    New_list = []
    for i in lst:
        if lst.count(i) > 1:
            if i in New_list:
                pass
            else:
                print('i is not a duplicate')
    return New_list
def get_user_info():
    name = input('please enter your full name: ')
    address = input('please enter your address: ')
    zip_code = input('please enter you zipcode: ')
    age = input('please enter your age: ')
    hair_color = input('please enter your hair color: ')
    eye_color = input('please enter your color: ')
    user_infor = {'name' :name, 'address' :address, 'zipcode' :zipcode, 'age' :age, 'hair_color' :hair_color, 'eye_color' :eye_color}
    for k in user_infor.items():
        print(k)