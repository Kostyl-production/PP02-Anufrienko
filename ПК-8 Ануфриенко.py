#Функция нахождения минимального расстояния
def rst():
    U_1 = 0
    d_ij_mass = [0] # Массив расстояний
    print("Программа находит минимальное расстояние, кротчайший путь не реализован")
    print("Ввод осуществлять заданному порядку: d12, d13, d14, d24, d34, d25, d45, d36, d46, d57, d67(где dij - расстояние между узлами)")
    
    #Цикл ввода расстояний с обработкой ошибок
    for i in range (0,10):  
        try:
            ij = int(input("Введите расстояние:"))
            d_ij_mass.append(abs(ij))
        except:
            print("Ошибка ввода, повторите попытку")
            rst()
    #Формулы нахождения расстояния       
    U_2 = U_1 + d_ij_mass[0]
    U_3 = U_1 + d_ij_mass[1]
    U_4 = min(U_1+ d_ij_mass[2], U_2 + d_ij_mass[3], U_3 + d_ij_mass[4])
    U_5 = min(U_2+d_ij_mass[5], U_4+d_ij_mass[6])
    U_6 = min(U_3+d_ij_mass[7], U_4+d_ij_mass[8])
    U_7 = min(U_5+d_ij_mass[9],U_6+d_ij_mass[10])
    print(U_7) # Вывод минимального расстояния
    input("Нажмите enter, чтобы выйти.")
rst() #Запуск функции
