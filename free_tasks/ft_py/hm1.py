import scipy.stats as stats
import matplotlib.pyplot as plt
# Частина 1 
n = 20  # Кількість спроб
p = 0.4  # Ймовірність успіху

# Створення списку значень випадкової величини (наприклад, від 0 до 20)
x = list(range(n + 1))

# Функція маси ймовірностей (PMF)
pmf_values = [stats.binom.pmf(k, n, p) for k in x]

# Ймовірність успіху (CDF)
cdf_values = [stats.binom.cdf(k, n, p) for k in x]

# Обрахунок найбільш ймовірного значення випадкової величини
most_probable_value = [k for k in x if stats.binom.pmf(k, n, p) == max(pmf_values)]

# Обрахунок суми всіх значень ймовірностей
total_probability = sum(pmf_values)

# Побудова графіка для функції маси ймовірностей
plt.bar(x, pmf_values, align='center', alpha=0.7)
plt.xlabel('Кількість успіхів')
plt.ylabel('Ймовірність')
plt.title('Функція маси ймовірностей (PMF) біноміального розподілу')
plt.show()

# Побудова графіка для ймовірності успіху (CDF)
plt.plot(x, cdf_values, marker='o', linestyle='-')
plt.xlabel('Кількість успіхів')
plt.ylabel('Ймовірність успіху (CDF)')
plt.title('Ймовірність успіху (CDF) біноміального розподілу')
plt.grid(True)
plt.show()

# Виведення результатів обрахунків
print(f"Найбільше ймовірне значення випадкової величини: {most_probable_value}")
print(f"Сума всіх значень ймовірностей: {total_probability}")

#Частина 2, нормальний закон а)
