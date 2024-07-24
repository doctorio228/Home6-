my_dict = {'Саша': 2022, 'Настя': 2020, 'Валя': 2019}
print(my_dict)
print(my_dict['Саша'])
print(my_dict.get('Вася', "такого имени в словаре нету"))
my_dict.update ({'Соня': 2011, 'Егор': 2013})
del my_dict['Настя']
print(my_dict)
my_set = {1,3,2,4,2,3,1,4,'Man'}
print(my_set)
my_set.update(['git', 'cat'])
my_set.discard(4)
print(my_set)