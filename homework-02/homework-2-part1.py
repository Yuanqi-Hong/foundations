# Yuanqi (Edward) Hong
# May 23, 2018
# Homework 2, Part 1

# Lists

num = [22, 90, 0, -10, 3, 22, 48]

print(len(num))

print(num[3])

print(num[1] + num[3])

num_sorted = sorted(num)
print(num_sorted[-2])

print(num[-1])

print(sum(num) / 2)

import statistics as stat
median = stat.median(num)
mean = stat.mean(num)
if median > mean:
    print('The median of the list is higher than the mean.')
elif median == mean:
    print('The median and the mean are the same.')
else:
    print('THe mean of the list is higher than the median.')

# Dictionaries

movie = {
    'title': 'Harry Potter and the Philosopher\'s Stone',
    'year': 2001,
    'director': 'Chris Columbus'
}    
print("My favorite movie is", movie['title'],
      "which was released in", movie['year'],
      "and was directed by", movie['director'])

movie['budget'] = 125000000
movie['revenue'] = 974755371
br_dif = movie['revenue'] - movie['budget']
print(br_dif)

if br_dif <= 0:
    print('That was a bad investment.')
elif movie['revenue'] >= (5 * movie['budget']):
    print('That was a great investment.')
else:
    print('That was an okay investment.')

populations = {
    'Manhattan': 1.6,
    'Brooklyn': 2.6,
    'Bronx': 1.4,
    'Queens': 2.3,
    'Staten Island': 0.47
}

print('The population of Brooklyn is', populations['Brooklyn'], 'million.')

total_population = sum(populations.values())
print('The total population of NYC is', total_population, 'million.')

# The total population could also be obtained using for loops:
# total_population = 0
# for borough in populations.keys():
#    total_population += populations[borough]
# print(total_population)

percentage = populations['Manhattan'] / total_population
percentage_rounded = round(percentage, 4)
print('%s%% of NYC\'s population lives in Manhattan.' % (percentage_rounded * 100))


# Ref
# http://www.boxofficemojo.com/movies/?id=harrypotter.htm
# https://en.wikipedia.org/wiki/Harry_Potter_(film_series)
# https://stackoverflow.com/questions/5306756/how-to-show-percentage-in-python
