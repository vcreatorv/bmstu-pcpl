import matplotlib.pyplot as plt

# Заданные данные о температурах
temperatures = [25, 28, 30, 27, 22, 24, 26]
days_of_week = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

# Создание графика
plt.plot(days_of_week, temperatures)

# Настройка осей и заголовка графика
plt.xlabel("Дни недели")
plt.ylabel("Температура (градусы)")
plt.title("Ежедневные температуры в городе за неделю")

# Отображение графика
plt.show()
