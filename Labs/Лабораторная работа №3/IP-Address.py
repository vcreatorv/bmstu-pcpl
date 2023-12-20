import requests
import folium


def create_map_with_marker(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)

    if response.status_code != 200:
        print("При извлечении информации об IP-адресе произошла ошибка.")
        return

    info = response.json()
    latitude = info.get("lat")
    longitude = info.get("lon")

    if not latitude or not longitude:
        print("Неверный IP-адрес или информация о местоположении не найдена.")
        return

    map_point = folium.Map(location=[latitude, longitude], zoom_start=6)
    folium.Marker(location=[latitude, longitude], popup="My Point").add_to(map_point)
    map_point.save("point.html")


ip_address = "5.228.44.0"
create_map_with_marker(ip_address)
