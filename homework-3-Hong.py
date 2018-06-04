# Yuanqi (Edward) Hong
# May 28, 2018
# Homework 3

#---------------------------- Lists ----------------------------#

numbers = [4, 5, 1, 10, 200, 34, 22, 19, 43, 56, 32, 11, 40, 82, 23, 43, 12, 65, 10]

count = 0
for num in numbers:
    count += 1
print(count)

numbers.append(7)

count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print(count)

import statistics as stat
mean_value = stat.mean(numbers)
above_mean = 0
below_mean = 0
for num in numbers:
    if num > mean_value:
        above_mean += 1
    elif num < mean_value:
        below_mean += 1
print(above_mean)
print(below_mean)

total = 0
for num in numbers:
    total += num
print(total)

total_above = 0
total_below = 0
for num in numbers:
    if num > mean_value:
        total_above += num
    elif num < mean_value:
        total_below += num
print(total_above)
print(total_below)

maximum = 0
for num in numbers:
    if num > maximum:
        maximum = num
print(maximum)

dogs = ["Sparky", "Jane", "Matilda", "Blartsburg"]

dogs.append('Maxwell')

short_names = []
for dog in dogs:
    if len(dog) <= 5:
        short_names.append(dog)
print(short_names)

cantons = [ "ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO", "BS", "BL", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS", "NE", "GE", "JU"]
for canton in cantons:
    print('http://important-swiss-things.ch/docs/download/'+canton)

documents = ['qq7lthm', 'jemsqhg', 'O6itcke', 'cp4Iua0', 'bkijcmo', 'ctoyjrm', 'z8wc6xy', 'zk4Bmm0']
for doc in documents:
    n = 1
    while n < 13:
        print('www.top-secret-pdfs.com/content/secrets/'+doc.upper()+'/page/{:03}.pdf'.format(n))
        n += 1

#---------------------------- Dictionaries ----------------------------#

patient = {
    'name': 'Lala Hsu',
    'complaint': 'not feeling right'
    }

print("Doctor, it looks like the patient named",
      patient['name'],
      "is complaining about",
      patient['complaint'])

patient.update({
    'Heart rate': 70,
    'Temperature': 98.6,
    'Infection': 'No'
    })

temp = patient['Temperature']
infec = patient['Infection']
if temp > 102:
    if infec == 'No':
        patient.update({'diagnosis': 'heat stroke'})
    else:
        patient.update({'diagnosis': 'flu'})
else:
    if infec != 'No':
        patient.update({'diagnosis': 'cold'})
    else:
        patient.update({'diagnosis': 'take an aspirin and call me in the morning'})
print('Your diagnosis is:', patient['diagnosis']) 

bart = {
    'name': 'Bart Simpson',
    'complaint': 'not feeling right',
    'Heart rate': 80,
    'Temperature': 103,
    'Infection': 'No'
    }
lisa = {
    'name': 'Lisa Simpson',
    'complaint': 'not feeling good',
    'Heart rate': 77,
    'Temperature': 104,
    'Infection': 'Yes'
    }
maggie = {
    'name': 'Maggie Simpson',
    'complaint': 'this is indeed a disturbing universe',
    'Heart rate': 90,
    'Temperature': 90,
    'Infection': 'Yes'
    }
patients = [bart, lisa, maggie]

for simpson in patients:
    temp = simpson['Temperature']
    infec = simpson['Infection']
    if temp > 102:
        if infec == 'No':
            simpson.update({'diagnosis': 'heat stroke'})
        else:
            simpson.update({'diagnosis': 'flu'})
    else:
        if infec != 'No':
            simpson.update({'diagnosis': 'cold'})
        else:
            simpson.update({'diagnosis': 'take an aspirin and call me in the morning'})
    print(simpson['name']+'\'s diagnosis is:', simpson['diagnosis'])

#---------------------------- CSV files ----------------------------#

import csv

csvfile = open('countries.csv', 'r')
reader = csv.DictReader(csvfile)
data = list(reader)
csvfile.close()
print("The data looks like", data)

print('The columns in our data set are %s.' %(', '.join(data[0].keys())))

print('We have', len(data), 'countries in our dataset.')

asia = 0
n_america = 0
for country in data:
    if country['Continent'] == 'Asia':
        asia += 1
    elif country['Continent'] == 'N. America':
        n_america += 1
print('There are', asia, 'countries in Aisa.')
print('There are', n_america, 'countries in North America.')

total_population = 0
for country in data:
    total_population += int(country['Population'])
print('The total population of the world is', total_population)

africa_pop = 0
s_america_pop = 0
for country in data:
    if country['Continent'] == 'Africa':
        africa_pop += int(country['Population'])
    elif country['Continent'] == 'S. America':
        s_america_pop += int(country['Population'])
if africa_pop > s_america_pop:
    print('Africa has a larger population than South America.')
elif africa_pop < s_america_pop:
    print('South America has a larger population than Africa.')

for country in data:
    total_gdp = int(country['GDP_per_capita']) * int(country['Population'])
    print('The total GDP of', country['Country'], 'is', total_gdp)

import statistics as stat
life_exp = []
for country in data:
    life_exp.append(float(country['life_expectancy']))
life_exp_med = stat.median(life_exp)
print('The median life expectancy of the world is', round(life_exp_med,2))

life_exp_eu = []
for country in data:
    if country['Continent'] == 'Europe':
        life_exp_eu.append(float(country['life_expectancy']))
life_exp_eu_med = stat.median(life_exp_eu)
print('The median life expectancy of Europe is', round(life_exp_eu_med,2))

life_exp_avg = stat.mean(life_exp)
for country in data:
    if float(country['life_expectancy']) < life_exp_avg:
        print(country['Country'])

gdp_avg = (sum(int(country['GDP_per_capita']) for country in data)) / len(data)
for country in data:
    if int(country['GDP_per_capita']) < gdp_avg and float(country['life_expectancy']) > life_exp_avg:
        print(country['Country'])
# Since the question didn't specify, I used per capita GDP in the comparison.

import math
gdp_list = []
for country in data:
    total_gdp = int(country['GDP_per_capita']) * int(country['Population'])
    gdp_list.append(total_gdp)
gdp_sorted = sorted(gdp_list)
if len(gdp_sorted) % 4 == 0:
    percentile = (gdp_list[int(0.75*len(gdp_list))] + gdp_list[int(0.75*len(gdp_list)+1)]) / 2
    print(percentile)
else:
    percentile = gdp_list[math.ceil(0.75*len(gdp_list))]
    print(percentile)

pop_below = 0
pop_above = 0
for country in data:
    if float(country['life_expectancy']) < 50:
        pop_below += int(country['Population'])
    elif float(country['life_expectancy']) > 80:
        pop_above += int(country['Population'])
percent_below = pop_below / total_population
percent_above = pop_above / total_population
print('%s%% of the world population has a life expectancy of below 50 years.' %(round(percent_below * 100, 2)))
print('%s%% of the world population has a life expectancy of above 80 years.' %(round(percent_above * 100, 2)))


# Ref
# https://stackoverflow.com/questions/134934/display-number-with-leading-zeros
# https://stackoverflow.com/questions/6416131/python-add-new-item-to-dictionary
# https://stackoverflow.com/questions/29027792/get-average-value-from-list-of-dictionary
# https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python
