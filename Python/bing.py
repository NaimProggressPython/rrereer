from datetime import datetime

print("Введите дату рождение")
result = datetime.now() - datetime.strptime(input(">>>"), %Y - %m - %d)
print(f'Вам {result.days//365} лет!')