import requests

base_url = "https://catfact.ninja"

print("Породы")
endpoint = "/breeds"
query_params = {'limit':'10'}

response = requests.get(base_url+endpoint, params=query_params)
print(response.status_code)
print(response.text)



response = requests.get(base_url+endpoint, params=query_params)
print(response.status_code)
print(response.text)

print("Случайный факт")
endpoint = "/fact"
query_params = {
    'max_lenght':'100'
}

response = requests.get(base_url+endpoint, params=query_params)
print(response.status_code)
print(response.text)


print("Список фактов")
endpoint = "/facts"
query_params = {
    'limit':'3',
    'max_lenght':'90'
}

response = requests.get(base_url+endpoint, params=query_params)
print(response.status_code)
print(response.text)