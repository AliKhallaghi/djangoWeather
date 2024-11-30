from django.shortcuts import render

	#9bibqqXptc5OfOtEuMdMfthakHyQGlRx apikey

def index(request):
	import json
	import requests

	if request.method == "POST":
		citysearch = request.POST.get('citysearch' , 'Karaj')
		api_request = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"+citysearch+"?unitGroup=metric&elements=datetime%2CdatetimeEpoch%2Cname%2Caddress%2Ctempmax%2Ctempmin%2Ctemp%2Cuvindex%2Cconditions&include=current%2Cfcst&key=HQBUGSMCJ36BDJD2Q4PPD9873&contentType=json")
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error"

		if api['days'][0]['uvindex'] <= 2:
		    color_description = "0 to 2: Low || A UV Index reading of 0 to 2 means low danger from the sun's UV rays for the average person."
		    color_pick = "low"
		elif api['days'][0]['uvindex'] <= 5:
		    color_description = "3 to 5: Moderate || A UV Index reading of 3 to 5 means moderate risk of harm from unprotected sun exposure."
		    color_pick = "moderate"
		elif api['days'][0]['uvindex'] <= 7:
		    color_description = "6 to 7: High || A UV Index reading of 6 to 7 means high risk of harm from unprotected sun exposure. Protection against skin and eye damage is needed."
		    color_pick = "high"
		elif api['days'][0]['uvindex'] <= 10:
		    color_description = "8 to 10: Very High || A UV Index reading of 8 to 10 means very high risk of harm from unprotected sun exposure. Take extra precautions because unprotected skin and eyes will be damaged and can burn quickly."
		    color_pick = "veryhigh"
		elif api['days'][0]['uvindex'] >= 11:
		    color_description = "11 or more: Extreme || A UV Index reading of 11 or more means extreme risk of harm from unprotected sun exposure. Take all precautions because unprotected skin and eyes can burn in minutes."
		    color_pick = "extreme"
		return render(request, 'index.html', {'api': api,
			'color_description' : color_description,
			'color_pick' : color_pick})


	else :
		api_request = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Karaj?unitGroup=metric&elements=datetime%2CdatetimeEpoch%2Cname%2Caddress%2Ctempmax%2Ctempmin%2Ctemp%2Cuvindex%2Cconditions&include=current%2Cfcst&key=HQBUGSMCJ36BDJD2Q4PPD9873&contentType=json")
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error"

		if api['days'][0]['uvindex'] <= 2:
		    color_description = "0 to 2: Low || A UV Index reading of 0 to 2 means low danger from the sun's UV rays for the average person."
		    color_pick = "low"
		elif api['days'][0]['uvindex'] <= 5:
		    color_description = "3 to 5: Moderate || A UV Index reading of 3 to 5 means moderate risk of harm from unprotected sun exposure."
		    color_pick = "moderate"
		elif api['days'][0]['uvindex'] <= 7:
		    color_description = "6 to 7: High || A UV Index reading of 6 to 7 means high risk of harm from unprotected sun exposure. Protection against skin and eye damage is needed."
		    color_pick = "high"
		elif api['days'][0]['uvindex'] <= 10:
		    color_description = "8 to 10: Very High || A UV Index reading of 8 to 10 means very high risk of harm from unprotected sun exposure. Take extra precautions because unprotected skin and eyes will be damaged and can burn quickly."
		    color_pick = "veryhigh"
		elif api['days'][0]['uvindex'] >= 11:
		    color_description = "11 or more: Extreme || A UV Index reading of 11 or more means extreme risk of harm from unprotected sun exposure. Take all precautions because unprotected skin and eyes can burn in minutes."
		    color_pick = "extreme"



		return render(request, 'index.html', {'api': api,
			'color_description' : color_description,
			'color_pick' : color_pick})

def about(request):
	return render(request, 'about.html', {})
