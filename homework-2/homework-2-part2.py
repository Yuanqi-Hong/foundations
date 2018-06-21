# Yuanqi (Edward) Hong
# May 23, 2018
# Homework 2, Part 2

# Lists

countries = ['USA', 'China', 'Japan', 'Korea', 'Malaysia', 'India', 'Spain']

for country in countries:
    print(country)

countries.sort()

print(countries[0])

print(countries[-2])

countries.remove('Malaysia')

for country in countries:
    print(country.upper())

# Dictionaries

tree = {
    'name': 'The Ying Ke Pine',
    'species': 'Huangshan pine (Pinus hwangshanensis)',
    'age': 1500,
    'location_name': 'Huangshan, China',
    'latitude': 29.7147,
    'longitude': 118.3375
}

print(tree['name'], 'is a', tree['age'], 'year old tree that is in', tree['location_name'])

nyc_latitude = 40.7128
nyc_longitude = -74.0059
if tree['latitude'] < nyc_latitude:
    print('The tree', tree['name'], 'in', tree['location_name'], 'is south of NYC.')
else:
    print('The tree', tree['name'], 'in', tree['location_name'], 'is north of NYC.')

age = input('How old are you? Type your age here and hit Enter: ')
age = int(age)
tree_age = tree['age']
if age > tree_age:
    print('You are %s years older than %s.' % ((age - tree_age), tree['name']))
elif age == tree_age:
    print('You are the same age as the tree.')
else:
    print('%s was %s years old when you were born.' % (tree['name'], tree_age - age))

# List of dictionaries

moscow = {'name': 'Moscow', 'latitude': 55.7558, 'longitude': 37.6173}
tehran = {'name': 'Tehran', 'latitude': 35.6892, 'longitude': 51.3890}
falkland = {'name': 'Falkland Islands', 'latitude': -51.7963, 'longitude': -59.5236}
seoul = {'name': 'Seoul', 'latitude': 37.5665, 'longitude': 126.9780}
santiago = {'name': 'Santiago', 'latitude': -33.4489, 'longitude': -70.6693}

cities = [moscow, tehran, falkland, seoul, santiago]

for city in cities:
    if city['latitude'] >= 0:
        print(city['name'], 'is above the equator.')
    else:
        print(city['name'], 'is below the equator.')
    if city['name'] == 'Falkland Islands':
        print('The Falkland Islands are a biogeographical part of the mild Antarctic zone.')

for city in cities:
    if city['latitude'] < tree['latitude']:
        print(city['name'], 'is south of', tree['name'])
    else:
        print(city['name'], 'is north of', tree['name'])


# Ref
# https://en.wikipedia.org/wiki/List_of_individual_trees
