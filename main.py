import colorama
from colorama import Fore
colorama.init(autoreset=True)
import requests  # requests python library for scrapping data from openweathermap.org

# Include your own opneweathermap API Key here, visit https://api.openweathermap.org/
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

# Defining a function a that takes city name and request weather info of the city, scrap the data from returned output
def weath(city_name):
	try:
		# Requesting weather info from openweathermap.org website
		data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}").json()

		climate = "Weather climate"
		temp = "Temperature"
		desc = "Weather description"
		pressure = "Pressure"
		vis = "Visibility"
		speed = "Wind speed"
		hum = "Humidity"
		latlon = "Lat and lon"

		# Scrapping recieved data
		print(f"{Fore.BLUE}\nWeather in",f"{Fore.GREEN}"+city_name.title()+"("+f"{Fore.GREEN}"+str(data["sys"]["country"])+")\n")
		print(f"{Fore.CYAN}{climate:>25} : ",data["weather"][0]["main"])
		print(f"{Fore.CYAN}{temp:>25} : ",str(int(data["main"]["temp"]-273.15))+"°C")
		print(f"{Fore.CYAN}{desc:>25} : ",data["weather"][0]["description"])
		print(f"{Fore.CYAN}{pressure:>25} : ",data["main"]["pressure"],"mbars    (1 atm = 1013.25 milibars)")
		print(f"{Fore.CYAN}{vis:>25} : ",data["visibility"],"miles")
		print(f"{Fore.CYAN}{speed:>25} : ",data["wind"]["speed"],"miles per hour")
		print(f"{Fore.CYAN}{hum:>25} : ",data["main"]["humidity"],"g/kg       (grams of water vapour per kg of air)")
		print(f"{Fore.CYAN}{latlon:>25} : ",data["coord"]["lat"],"and",data["coord"]["lon"])
		print()
	except:
		print(f"{Fore.RED}\nOpps, something went wrong!\n")
if __name__ == "__main__":
	print(f"{Fore.CYAN}\n\t\t********** How is Weather in Your City?",f"{Fore.CYAN}**********\n")
	# Input city name
	usr = input("Enter your city: ")
	weath(usr)
