#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import atol

#вывод меню
def menu(items):
 for item in items:
  print (items.index(item), item)
 while True:
  number=int(input())
  if (number>=0) & (number<len(items)):
   return number
   
atol.init_driver()
#Опрос пользователя
os.system('cls')
print ("Введите номер кассира:")
kassiry=['Иванова Е.А.','Петрова А.В.','Сидорова Р.Н.','Кассова О.Ю.']
nomer_kassira=menu(kassiry)
while True:
 os.system('cls')
 print ("Введите номер команды:")
 commands=['Чек прихода','Чек возврата','Выплата из кассы','Отчёт о счётчиках ККТ (X)','Отчёт по секциям','Отчёт количеств','Закрытие смены (Z)','Выключение терминала']
 nomer_command=menu(commands)
 departments=['(Возврат назад)','Общ.туалет','Автостоянка','Рынок','Ярмарка','Торговый Зал','Камеры Хранения']
 os.system('cls')
 if nomer_command==0: # печать чеков прихода
  print ("Печать чеков прихода:")
  print ("Введите номер отдела:")
  nomer_department=menu(departments)
  if nomer_department==0: continue
  os.system('cls')
  print ("Печать чеков прихода:")
  print ("Отдел:",departments[nomer_department])
  print ("Введите цену:")
  tsena_uslugi=int(input())
  if tsena_uslugi==0:
    continue
  print ("Введите количество чеков:")
  kol_chekov=input()
  if kol_chekov=='':
    kol_chekov=1
    print (1)
  elif kol_chekov=='0':
    continue
  print ("печать чеков...")
  atol.print_check(1,kassiry[nomer_kassira],departments[nomer_department],nomer_department,tsena_uslugi, int(kol_chekov))
 elif nomer_command==1:
  nomer_department=menu(departments)
  if nomer_department==0: continue
  os.system('cls')
  print ("Печать чеков возврата:")
  print ("Отдел:",departments[nomer_department])
  print ("Введите цену:")
  tsena_uslugi=int(input())
  if tsena_uslugi==0:
    continue
  kol_chekov=1
  print ("печать чека возврата...")
  atol.print_check(2,kassiry[nomer_kassira],departments[nomer_department],nomer_department,tsena_uslugi, int(kol_chekov))
 elif nomer_command==2:
  print ("Выплата из кассы")
  print ("Введите сумму:")
  summa=float(input())
  if summa==0:
    continue
  print ("печать чека выплаты...")
  atol.vyplata(summa)
 elif nomer_command==3:
  print ("печать отчёта о счётчиках ККТ (X)...")
  atol.print_otchet(1,"")
 elif nomer_command==4:
  print ("печать отчёта по секциям...")
  atol.print_otchet(2,"")
 elif nomer_command==5:
  print ("печать отчёта количеств...")
  atol.print_otchet(3,"")
 elif nomer_command==6:
  print ("закрытие смены...")
  atol.print_otchet(4,kassiry[nomer_kassira])
 elif nomer_command==7:
  print ("выключение терминала...")
  break
 else:
  print ("другая команда...")
 time.sleep(1)
 # конец while
