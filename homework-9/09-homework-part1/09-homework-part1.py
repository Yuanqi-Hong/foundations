# This is the .py file for homework 9 part 1.
# All comments and the process of writing are left out in this file.
# For the commented version, please see the .ipynb file.
# Certain info has been replaced with CAPITALIZED PHRASES, but do not affect the logic of script.

import requests
import datetime

response = requests.get('https://api.darksky.net/forecast/MY_API_KEY/40.7128,-74.0060')
data = response.json()
temperature = data['currently']['temperature']
summary = data['currently']['summary']
days = data['daily']['data']
today = days[0]
avg_apparent = (today['apparentTemperatureHigh'] + today['apparentTemperatureLow']) / 2
if avg_apparent <= 55:
    temp_feeling = 'cold'
elif avg_apparent <= 65:
    temp_feeling = 'cool'
elif avg_apparent <= 75:
    temp_feeling = 'mild'
elif avg_apparent <= 85:
    temp_feeling = 'warm'
else:
    temp_feeling = 'hot'
high_temp = today['temperatureHigh']
low_temp = today['temperatureLow']
rain_chance = today['precipProbability']
if rain_chance < 0.2:
    rain_warning = 'It\'s not gonna rain.'
elif rain_chance < 0.3:
    rain_warning = 'There\'s only a slight chance of raining today, an umbrella would be unnecessary.'
elif rain_chance < 0.5:
    rain_warning = 'There\'s a chance of raining today, bring an umbrella if you feel like putting on extra weight to your backpack.'
else:
    rain_warning = 'Bring an umbrella!'
message0 = 'Right now it is {} degrees out and {}. Today will be {} with a high of {} and a low of {}. {}\n\n'.format(temperature, summary.lower(), temp_feeling, high_temp, low_temp, rain_warning)

hourly = data['hourly']['data']
hour_count = 1
message1 = 'The hourly temperature forecast for the next 24 hours is listed below:\n'
for hour in hourly:
    if hour_count > 24:
        break
    weather = str(hour['temperature']) + '°F'
    message1 += 'Forecast for {} in New York: {}.\n'.format(datetime.datetime.fromtimestamp(int(hour['time'])).strftime('%Y-%m-%d %H:%M:%S'), weather)
    hour_count += 1

right_now = datetime.datetime.now()
date_string = right_now.strftime("%b %d, %Y")
requests.post(
        "https://api.mailgun.net/v3/MY_SANDBOX_DOMAIN/messages",
        auth=("api", "MY_API_KEY"),
        data={"from": "Edward Hong <mailgun@MY_SANDBOX_DOMAIN>",
              "to": ["Edward.YSHF@gmail.com"],
              "subject": "8 a.m. Weather Forecast - {}".format(date_string),
              "text": message0+message1})