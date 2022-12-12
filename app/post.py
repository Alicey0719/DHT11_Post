from dotenv import load_dotenv
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import json
import requests
import socket
import os


load_dotenv()

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

PIN = int(os.getenv('PIN'))
POST_ADDR = str(os.getenv('POST_ADDR'))
INTERVAL = int(os.getenv('INTERVAL'))
HOST_NAME = str(socket.gethostname())

print("Using PIN is", PIN)
sensor = dht11.DHT11(pin=PIN)

def dht_post(gpio_pin, name, url):		
	loop_count = 0

	while True:
		s_data = sensor.read()

		if s_data.is_valid():
			try:
				data = {"name":"%s" % name,"temp":"%-3.1f" % s_data.temperature, "hum":"%-3.1f" % s_data.humidity}
				response = requests.post(url, data=json.dumps(data))
			except:
				pass
			# print(response)
			# print("Last valid input: " + str(datetime.datetime.now()))
			# print("res1","Temperature: %-3.1f C" % s_data.temperature)
			# print("res1","Humidity: %-3.1f %%" % s_data.humidity)
			break
		else:
			loop_count += 1
			time.sleep(0.05)
			if loop_count > 100:
				break
			continue

def main():
	while True:
		try:
			dht_post(PIN, HOST_NAME, POST_ADDR)
			time.sleep(INTERVAL)
		except KeyboardInterrupt:
			print("KeyboardInterrupt!")
			break
	GPIO.cleanup()
	print('Process Close.')
	

if __name__ == '__main__':
	main()

