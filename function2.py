#function2
def isDivisbleby7(num):
    if num % 7 == 0:
        return True
    else:
        return False
def isDivisbleby7(number, divisor):
    if number % divisor == 0:
        return True
    else:
        return False
def shout(word):
    print(word.upper() + '!')
def introduce():
    name = ('please enter your name: ')
    print('Hello ' + name.upper() + '!')
def snack_check(snack):
    favorite_snack = 'candy'
    if snack == favorite_snack:
        return True
    else:
        return False
def snack_check(snack):
    favorite_snack = 'candy'
    if snack == favorite_snack:
        print('aww, thats so cute')
    else:
        print('really???, what makes you think i like that?')
def in_grocery_list(grocery_item):
    if type(grocery_item) == str:
        pass
    else:
        print('WARNING!: the item is not a string')
import random
def you_won():
    price_list = [9.42, 5.57, 3.25, 13.40, 7.50]
    if random.choice(price_list) >= 10:
        return True
    else:
        return False
import datetime
def return_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime('%H:%M:%S')
    if now.hour >= 7 and now.hour < 12:
        print(current_time, ': Morning Classes')
    elif now.hour > 12 and now.hour <= 17:
        print(current_time, ': Afternoon Classes')
    elif now.hour > 17 and now.hour <= 22:
        print(current_time, ': Evening Classes')
    else:
        print(current_time. 'why are you still in school')
def volume(length, width, height):
    return length * width * height
    
            