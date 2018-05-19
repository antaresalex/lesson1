mweather = {"city": "Moscow", "temperature": 20, "wind": "восточный"}
#print(weather.get("city"))
mweather["temperature"] = 15
#print(weather["temperature"])
#print(len(weather))
#print(weather.get("country"))
mweather["date"] = "27.05.2017"
#print(mweather)
list = [
{"city": "Moscow", "temperature": 20, "wind": "восточный", "date": "27.05.2017"}
]
#print(len(list))
list.append({"city": "Moscow", "temperature": 15, "wind": "восточный", "date": "01.05.2018"})
list.append({"city": "Moscow", "temperature": 19, "wind": "северо-западный", "date": "25.05.2017"})
print(list)
