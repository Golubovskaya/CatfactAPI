import requests

base_url = "https://catfact.ninja"

# Получение списка пород
print("Породы")
breeds_endpoint = "/breeds"
breeds_query_params = {'limit': '10'}
breeds_response = requests.get(base_url + breeds_endpoint, params=breeds_query_params)
print(breeds_response.status_code)
print(breeds_response.text)

# Получение случайного факта
print("Случайный факт")
fact_endpoint = "/fact"
fact_query_params = {'max_length': '100'}
fact_response = requests.get(base_url + fact_endpoint, params=fact_query_params)
print(fact_response.status_code)
print(fact_response.text)

# Получение списка фактов
print("Список фактов")
facts_endpoint = "/facts"
facts_query_params = {
    'limit': '3',
    'max_length': '90'
}
facts_response = requests.get(base_url + facts_endpoint, params=facts_query_params)
print(facts_response.status_code)
print(facts_response.text)