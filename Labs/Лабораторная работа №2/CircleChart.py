import matplotlib.pyplot as plt

# Результаты опроса
music_genres = ["Рок", "Поп", "Хип-хоп", "Электронная", "Классическая"]
votes = [30, 20, 15, 10, 25]

# Создание круговой диаграммы
plt.pie(votes, labels=music_genres, autopct="%1.1f%%")

# Добавление заголовка диаграммы
plt.title("Предпочтения музыкальных жанров")

# Показать диаграмму
plt.show()
