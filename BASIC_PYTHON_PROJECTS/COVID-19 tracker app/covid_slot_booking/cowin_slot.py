'''
Link of all state id and name:
https://cdn-api.co-vin.in/api/v2/admin/location/states

Sample booking info url:

https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=YOUR_STATE_ID&date=DD-MM-YYYY
'''

import requests
import time

district_id = YOUR_STATE_ID
appointment_date = 'DD-MM-YYYY'

setu_api = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(district_id,appointment_date)

browser_support = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
}

def book_slot():
	nos_locations = 0
	
	#get data from the setu-api url 
	vaccine_request = requests.get(setu_api,headers=browser_support)

	# convert the data into json format
	vaccine_data = vaccine_request.json()
	
	#extract all vacccine info according to your will from 'sessions' 
	booking_details = vaccine_data["sessions"]
	
	# looping through each vaccination center
	for loc in booking_details:
		
		# conditions the vaccination center should meet
		if(((loc["available_capacity"]> 0) and (loc['min_age_limit'] >=18) and (loc["fee_type"] == "Paid")) or ((loc["available_capacity"]> 0) and (loc['min_age_limit'] >=18) or (loc["fee_type"] == "Paid")) ):
			nos_locations += 1
			print(f"\n\nVaccination center : {loc['name']}\n")	
			print(f"Vaccination center address : {loc['address']}\n")
			print(f"Vaccination center pincode : {loc['pincode']}\n")
			print(f"Vaccination center vaccine : {loc['vaccine']}\n")
			print(f"Minimum age : {loc['min_age_limit']}\n")
			print(f"Vaccine fee : ₹{loc['fee']} Rupees\n")
			print(f"Vaccination availablity: {loc['available_capacity']}\n")
			print(f"Vaccination center slots : {loc['slots']}\n")
			print(f"Nos of vaccination centers found : {nos_locations}\n")
			return True
		if( nos_locations == 0):
			continue


while(book_slot() != True):
	time.sleep(2)
	book_slot()
