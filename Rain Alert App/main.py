import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "5ee84e43dbec558d614dd7b58dc68c73"
account_sid = "AC21236c33df07f98dddd37edf18695012" 
auth_token = "5f21f2ccb69b602ce09e757cd1f1b1cf"
weather_params = {
    "lat":41.878113,
    "lon":-87.629799,
    "appid":api_key,
    "cnt":4,
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to Rain Today, Remember to bring an Umbrella",
                     from_='+12026290519',
                     to='+919019045092',
                 )
    print(message.status)
    
