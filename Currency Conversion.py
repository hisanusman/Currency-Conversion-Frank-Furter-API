import requests
import json
import sys
import datetime 


if len(sys.argv)!=4:
    print("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")
    exit(0)
else:
    date = sys.argv[1]
    from_currency = sys.argv[2].upper()
    to_currency = sys.argv[3].upper()

    
currency = requests.get(f"https://api.frankfurter.app/latest")      
currency_dict = currency.json()

if from_currency not in currency_dict.get('rates').keys() and to_currency not in currency_dict.get('rates').keys():
    print(from_currency, "and", to_currency, "are not valid currency codes")
    exit(0)
        
elif to_currency not in currency_dict.get('rates').keys():
    print(to_currency, "is not a valid currency code")
    exit(0)
        
elif from_currency not in currency_dict.get('rates').keys():
    print(from_currency, "is not a valid currency code")
    exit(0)


try:
    date == datetime.datetime.strptime(date,"%Y-%m-%d").date()
except ValueError as v:
    print("Provided date is invalid")
    exit(0)


response = requests.get(f"https://api.frankfurter.app/{date}?from={from_currency}&to={from_currency},{to_currency}")
t = response.json()

print(f"The conversion rate from {from_currency} to {to_currency} was {t.get('rates').get(to_currency)} on {date}. The inverse rate was {1/float(t.get('rates').get(to_currency))}.")

