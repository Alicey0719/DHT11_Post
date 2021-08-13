import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests


def dht_post(gpio_pin, interval, name, url):
	# initialize GPIO
	GPIO.setwarnings(True)
	GPIO.setmode(GPIO.BCM)

	# pin assign
	instance1 = dht11.DHT11(pin=gpio_pin)

	while True:
		try:
			result1 = instance1.read()
			
			if result1.is_valid():
				headers = {'Accept': 'application/json'}
				data = {"name":"%s" % name,"temp":"%-3.1f" % result1.temperature, "hum":"%-3.1f" % result1.humidity}
				response = requests.post(url, headers=headers, data=data)
				print(response)
				print("Last valid input: " + str(datetime.datetime.now()))
				print("res1","Temperature: %-3.1f C" % result1.temperature)
				print("res1","Humidity: %-3.1f %%" % result1.humidity)
			else:
				print('result1:not valid')
			time.sleep(interval)

		except KeyboardInterrupt:
			print("Cleanup")
			GPIO.cleanup()

def main():
	dht_post(14, 1*5, 'raspi01', 'http://127.0.0.1/temp')

if __name__ == '__main__': main()

