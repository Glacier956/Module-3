print('Задача 5. Часы')

# Напишите программу, 
# которая получает на вход число n — количество минут, — затем считает,
# 1) сколько это будет в часах 
# 2) сколько минут останется
# и выводит на экран эти два результата.
# (В вычислениях вам помогут операции // и %)

n = int(input("Введите количество минут: "))
#Вывод результата в консоль
print("Часы:", n // 60)
print("Минуты:", n % 60)
