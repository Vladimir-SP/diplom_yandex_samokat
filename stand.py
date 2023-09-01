import requests
import configuration
from data import order_data

# Создаем заказ, отправляя POST-запрос на указанный URL-адрес.
def create_order():
    response = requests.post(f"{configuration.URL_SERVICE}{configuration.ORDERS_URL}", json=order_data)
    return response.status_code, response.json()

# Получаем информацию о заказе по его трек-номеру, отправляя GET-запрос на указанный URL-адрес.
def get_order_by_track(track):
    response = requests.get(f"{configuration.URL_SERVICE}{configuration.TRACK_URL}{track}")
    return response.status_code, response.json()
