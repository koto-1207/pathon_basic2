def main():
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    total_temperature = 0
    for item in weather_information:
        total_temperature += item["temperature"]

    count = len(weather_information)
    avg_temperature = total_temperature / count
    print(avg_temperature)

    osaka_stations = []
    for item in weather_information:
        if item["prefecture"] == "大阪府":
            osaka_stations.append(item["station"])

    print(", ".join(osaka_stations))


    fukuoka_temperatures = []
    for item in weather_information:
        if item["prefecture"] == "福岡県":
            fukuoka_temperatures.append(item["temperature"])

    count = len(fukuoka_temperatures)
    sum_temperature = sum(fukuoka_temperatures)
    avg_fukuoka = sum_temperature / count
    print(avg_fukuoka)


if __name__ == "__main__":
    main()
