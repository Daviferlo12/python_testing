import requests

def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    respone = requests.get(url)
    respone.raise_for_status()
    data = respone.json()
    return{
      "country": data["countryName"],
      "region": data["regionName"],
      "city" : data["cityName"]  
    }
    

# if __name__ == "__main__":
#     print(get_location("8.8.8.8"))