import matplotlib.pyplot as plt

# Список языков программирования
x = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]

# Список популярности каждого языка программирования
popularity = [22, 18, 9, 8, 7, 6]

# Создаем список позиций для каждого языка программирования
x_pos = [i for i, _ in enumerate(x)]

# Создаем столбчатую диаграмму с указанием цветов для каждого столбца
plt.bar(x_pos, popularity, color=["red", "black", "green", "blue", "yellow", "cyan"])

# Задаем подписи для осей и заголовок диаграммы
plt.xlabel("Языки программирования")
plt.ylabel("Популярность")
plt.title("Популярность языков программирования")

# Устанавливаем значения для оси X
plt.xticks(x_pos, x)

# Включаем вспомогательные деления на осях
plt.minorticks_on()

# Включаем сетку для основных делений
plt.grid(which="major", linestyle="-", linewidth="0.5", color="red")

# Включаем сетку для вспомогательных делений
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")

# Отображаем диаграмму
plt.show()
