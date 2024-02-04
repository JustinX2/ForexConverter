import requests

def convert_currency(from_currency, to_currency, amount):
    api_key='9ac5c26fea0b2a0dec3102fb84f88b1b'
    try:
        url=f"https://api.exchangerate.host/convert?access_key={api_key}&from={from_currency}&to={to_currency}&amount={amount}"
        response=requests.get(url)
        data=response.json()
        return data.get('result')
    except Exception as e:
        print(f"An error occured:{e}")
        return None