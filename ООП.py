import pickle
import os
from colorama import init
from colorama import Fore, Back, Style
init()
 
class Car(): 

    def __init__(self, marka=None, color=None, model=None, nomer = None):
        self.marka = marka
        self.model = model
        self.color = color
        self.nomer = nomer
    
    
class Mainvivod():
    def __init__(self):
        self.Vivod()

    def Vivod(self):
        while True:
            print(Back.MAGENTA + Fore.BLACK + 'Введите 1, если хотите добавить новый автомобиль ')
            print('Введите 2, если хотите редактировать информацию о некотором автомобиле ')
            print('Введите 3, если хотите посмотреть информацию о некотором автомобиле ')
            print('Введите 4, если хотите удалить автомобиль и все данные о нём')
            print('Введите 0, если хотите выйти из программы')
            what0 = input()
            print(Style.RESET_ALL)
            if what0 == '1':# добавление новой машины
                print(Fore.CYAN + 'Выбирите номер марки из списка или введите собственное значение')
                for i in range(len(spisokmarok)):
                    print(i + 1, ". ", spisokmarok[i], sep='')
                i = input()
                if (i.isdigit() == True) and (int(i) >= 0) and (int(i) <= len(spisokmarok)):
                    i = int(i)
                    autocar.append(Car(marka=spisokmarok[i - 1]))
                elif (i.isdigit() == True):
                    print(Fore.RED + "Такого номера нет в списке")
                    continue               
                else:
                    autocar.append(Car(marka=i))
                pickle.dump(autocar, open('autocar.pickle', 'wb'))

            elif what0 == '2': #редактирование машины
                if len(autocar) == 0:
                    print(Fore.RED + 'Отсутствует информация о машинах')
                    continue
                else:
                    for i in range(len(autocar)):
                        print(i + 1, '. ', autocar[i].marka, sep='')
                    print(Fore.CYAN + 'Какую машину вы бы хотели изменить? Введите 0 для выхода')
                    i = input()
                    if (i.isdigit() == True) and (int(i) >= 0) and (int(i) <= len(autocar)):
                        if int(i) == 0:
                            continue
                        else:
                            print(Fore.MAGENTA + '1. Изменить марку')
                            print('2. Изменить или добавить модель')
                            print('3. Изменить или добавить цвет')
                            print('4. Изменить или добавить номер')
                            print('0. Выход')
                            what1 = input()
                            if (what1 == '1') or (what1 == '2') or (what1 == '3') or (what1 == '4') or (what1 == '0'):
                                i = int(i) - 1
                                if what1 == '1':
                                    print(Fore.CYAN + 'Введите марку')
                                    autocar[i].marka = input()

                                if what1 == '2':
                                    print(Fore.CYAN + 'Введите модель')
                                    autocar[i].model = input()

                                if what1 == '3':
                                    print(Fore.CYAN + 'Введите цвет')
                                    autocar[i].color = input()
                                    
                                if what1 == '4':
                                    print(Fore.CYAN + 'Введите номер')
                                    autocar[i].nomer = input()
                            else:
                                neverno()
                            pickle.dump(autocar, open('autocar.pickle', 'wb'))
                    else:
                        neverno()   
                
            elif what0 == '3':
                if len(autocar) == 0:
                    print(Fore.RED + 'Отсутствует информация о машинах')
                    continue
                else:
                    for i in range(len(autocar)):
                        print(i + 1, '. ', autocar[i].marka, sep='')
                    print('0. Выход')
                    print(Fore.CYAN + 'Введите номер машины, данные о которой хотите посмотреть или введите 0 для выхода')
                    i = input()
                    if (i.isdigit() == True) and (int(i) >= 0) and (int(i) <= len(autocar)):
                        if int(i) == 0:
                            continue
                        else:
                            i = int(i) - 1
                            if i == -1:
                                what0 = Mainvivod()
                            if autocar[i].marka != None:
                                print(Fore.MAGENTA + 'Марка -', autocar[i].marka)
                            if autocar[i].model != None:
                                print(Fore.MAGENTA + 'Модель -', autocar[i].model)
                            if autocar[i].color != None:
                                print(Fore.MAGENTA + 'Цвет -', autocar[i].color)
                            if autocar[i].nomer != None:
                                print(Fore.MAGENTA + 'Номер -', autocar[i].nomer)
                            pickle.dump(autocar, open('autocar.pickle', 'wb'))
                    else:
                        neverno()
                        
            elif what0 == '4':
                if len(autocar) == 0:
                    print(Fore.RED + 'Нет машин для удаления')
                else:
                    for i in range(len(autocar)):
                        print(i + 1, '. ', autocar[i].marka, sep='')
                        print(Fore.CYAN + 'Введите номер машины, которую хотите удалить')
                        i = input()
                        if (i.isdigit() == True) and (int(i) >= 0) and (int(i) <= len(autocar)):
                            if int(i) == 0:
                                continue
                            else:
                                i = int(i) - 1
                                del autocar[i]
                        else:
                            neverno()
                        pickle.dump(autocar, open('autocar.pickle', 'wb'))
                        
            elif what0 == "0":
                break
            else:
                neverno()  
                
def neverno():
    print(Fore.RED + 'Было введено неверное значение')
def proverka1():
    if (os.path.exists("autocar.pickle")==True):
        return True
    else:
        file = open('autocar.pickle', 'a+')
        return False
    
def proverka2():
    with open('autocar.pickle', mode="r") as file:
        if (os.path.getsize('autocar.pickle') == 0) or (len(file.readline())==5):
            return []
        else:
            return pickle.load(open('autocar.pickle', 'rb'))
proverka1()
autocar = proverka2()
spisokmarok = ["Nissan", "Porsche", "Audi", "Hyundai", "Ford", "Volkswagen", "Honda", "BMW", "Mercedes-Benz", "Toyota"]
a = Mainvivod()

