# Yuanqi (Edward) Hong
# May 21, 2018
# Homework 1

year1 = input('Please tell me, in a 4-digit number, your year of birth:')
intyr1 = int(year1)

if intyr1 > 2018:
    year2 = input("You can't be born in the future. Let's try that again:")
    intyr = int(year2)
else:
    intyr = intyr1

age = 2018 - intyr
minutes = age*60*24*365

print("OK let's see, you're approximately", age, "years old.")

print('Your heart has beaten %s times. (We assume your average heart rate to be 80 bpm.)' % (80*minutes))

print("A blue whale's heart has beaten %s times since you were born." % (9*minutes))

rabbit = 135*minutes
if rabbit>=1000000:
    rabbitrounded = round(rabbit/1000000, 2)
    print("Whereas a rabbit's heart has beaten", rabbitrounded, "million times.")
else:
    print("Whereas a rabbit's heart has beaten", rabbit, "times.")

Venus_age = age*365/224.7
print("In Venus years, you're", round(Venus_age, 2), "years old, because on Venus a year is shorter than on Earth.")

Neptune_age = age*365/(164.79*365)
print("While on a planet with a longer revolution period, say Neptune, you'd only be", round(Neptune_age, 2), "years old.")

my_age = 2018 - 1995
dif = age - my_age
if dif < -1:
    print("You're %s years younger than me." % (abs(dif)))
elif dif == -1:
    print("You're 1 year younger than me.")
elif dif == 0:
    print("You're the same age as me.")
elif dif == 1:
    print("You're 1 year older than me.")
else:
    print("You're %s years older than I am." % (dif))

if age%2 == 0:
    print("You were born in an even year.")
else:
    print("You were born in an odd year.")

if intyr < 1935:
    print("If you're interested in which prez was in office when you were born you can just google it because you're way too old and I'm way too lazy to tell you the answer.")
elif intyr < 1945:
    print("When you were born, Franklin D. Roosevelt was in office.")
elif intyr == 1945:
    print("When you were born, either Franklin D. Roosevelt or Harry S. Truman was in office.")
elif intyr < 1953:
    print("When you were born, Harry S. Truman was in office.")
elif intyr == 1953:
    print("When you were born, either Harry S. Truman or Dwight D. Eisenhower was in office.")
elif intyr < 1961:
    print("When you were born, Dwight D. Eisenhower was in office.")
elif intyr == 1961:
    print("When you were born, either Dwight D. Eisenhower or John F. Kennedy was in office.")
elif intyr == 1962:
    print("When you were born, John F. Kennedy was in office.")
elif intyr == 1963:
    print("When you were born, either John F. Kennedy or Lyndon B. Johnson was in office.")
elif intyr < 1969:
    print("When you were born, Lyndon B. Johnson was in office.")
elif intyr == 1969:
    print("When you were born, either Lyndon B. Johnson or Richard Nixon was in office.")
elif intyr < 1974:
    print("When you were born, Richard Nixon was in office.")
elif intyr == 1974:
    print("When you were born, either Richard Nixon or Gerald Ford was in office.")
elif intyr < 1977:
    print("When you were born, Gerald Ford was in office.")
elif intyr == 1977:
    print("When you were born, either Gerald Ford or Jimmy Carter was in office.")
elif intyr < 1981:
    print("When you were born, Jimmy Carter was in office.")
elif intyr == 1981:
    print("When you were born, either Jimmy Carter or Ronald Reagan was in office.")
elif intyr < 1989:
    print("When you were born, Ronald Reagan was in office.")
elif intyr == 1989:
    print("When you were born, either Ronald Reagan or George H. W. Bush was in office.")
elif intyr < 1993:
    print("When you were born, George H. W. Bush was in office.")
elif intyr == 1993:
    print("When you were born, either George H. W. Bush or Bill Clinton was in office.")
elif intyr < 2001:
    print("When you were born, Bill Clinton was in office.")
elif intyr == 2001:
    print("When you were born, either Bill Clinton or George W. Bush was in office.")
elif intyr < 2009:
    print("When you were born, George W. Bush was in office.")
elif intyr == 2009:
    print("When you were born, either George W. Bush or Barack Obama was in office.")
elif intyr < 2017:
    print("When you were born, Barack Obama was in office.")
elif intyr == 2017:
    print("When you were born, either Barack Obama or Donald Trump was in office.")
else:
    print("When you were born, Donald Trump was in office.")

# Ref
# https://www.exploratorium.edu/ronh/age/
# http://python-pptx.readthedocs.io/en/latest/user/placeholders-using.html
# http://www.whalefacts.org/blue-whale-heart/
# https://www.nhs.uk/chq/Pages/2024.aspx?CategoryID=72&SubCategoryID=725
# https://rabbit.org/temperature-and-respiration-rates/
# https://docs.python.org/2/library/functions.html
# https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States
