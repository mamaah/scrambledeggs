#SNACK
fav_snack = 'meatpie'
print(fav_snack)
print(fav_snack * 100)
#ask friwnd's fav snack
freinds_fav_snack = input('please enter your fav snack:')
freinds_fav_snack = 'gato'
print(fav_snack, freinds_fav_snack)
print(fav_snack * 100, freinds_fav_snack * 100)
#grocery list
items = ['ngon', 'tiok', 'pombe', 'pah', 'nyam', 'gato']
grocery = items
print(grocery)
#testing if friend's snack is in the list
items.index('gato')
#fast swapping
temp = fav_snack
fav_snack = freinds_fav_snack
freinds_fav_snack = temp
print('fav_snack:', fav_snack)
print('friends_fav_snack:', freinds_fav_snack)
print('i love my new snack!')
