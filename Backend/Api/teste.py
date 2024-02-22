import requests


url= "https://dev-flpjat1olkfrxgne.eu.auth0.com/oauth/token"

payload = {
   "grant_type": "client_credentials",
    "client_id": "wMGvU0ZhMRKOUj4ThJ6sFpAHIWQdMNjn",
    "client_secret": "OSKKZutByaORg4XLklcGwzGqo7aFG5s0yvKPX2DfvPm7ac0KPQoz_Ql9WgkWskF-",
    "audience": "https://dev-flpjat1olkfrxgne.eu.auth0.com/api/v2/"


}
headers = { 'content-type': "application/x-www-form-urlencoded"}

response = requests.post(url, data=payload, headers=headers)

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data.get('access_token')
    print(f"Access Token {access_token}")
else: 
    print(f"Failed to obtain access token. Status code: {response.status_code}")
    print(response.text)
