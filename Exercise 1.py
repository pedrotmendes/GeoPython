import statistics
# import numpy
# import sklearn


ice_cream_rating = 8
sleeping_rating = 10

first_name = input('What is your first name? ')
last_name = input('and last name? ')
my_name = 'Your name is '+first_name+' '+last_name
print(my_name)

data1 = [ice_cream_rating, sleeping_rating]
happiness_rating = statistics.mean(data1)
perc=happiness_rating*10
print('Your happiness rating is', happiness_rating)

print(type(ice_cream_rating), type(first_name), type(happiness_rating))

# Yes the data types make sense

print('My name is', first_name, last_name, 'and I give eating ice cream a score of', ice_cream_rating, 'out of 10!')
print('I am', first_name, last_name, 'and my sleeping enjoyment is', sleeping_rating, '/ 10')
print('Based on the factors above, my happiness rating is', happiness_rating, 'out of 10, or', perc, '%')


#12345
#adicionando
dd

