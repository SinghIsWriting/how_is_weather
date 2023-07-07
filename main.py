import colorama
from colorama import Fore
colorama.init(autoreset=True)
import requests

API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

def weath(city_name):
	try:
		data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+f"&appid={API_KEY}").json()

		climate = "Weather climate"
		temp = "Temperature"
		desc = "Weather description"
		pressure = "Pressure"
		vis = "Visibility"
		speed = "Wind speed"
		hum = "Humidity"
		latlon = "Lat and lon"

		print(f"{Fore.BLUE}\nWeather in",f"{Fore.GREEN}"+city_name.title()+"("+f"{Fore.GREEN}"+str(data["sys"]["country"])+")")
		print()
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
		print(f"{Fore.RED}Opps, something went wrong!\n")
		print()
if __name__ == "__main__":
	print(f"{Fore.CYAN}\n\t\t********** How is Weather in Your City?",f"{Fore.CYAN}**********\n")
	print()
	usr = input("Enter your city: ")
	weath(usr)
