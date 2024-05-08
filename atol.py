#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Инициализация драйвера
from libfptr10 import IFptr
import os, time

#LIBRARY_PATH = os.path.dirname(os.path.abspath(__file__))
#fptr = IFptr(os.path.join('/usr/lib/',))
fptr = IFptr()

def init_driver():
  #Настройка драйвера
  fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_77F))
  fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT,  str(IFptr.LIBFPTR_PORT_TCPIP))
  fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_IPADDRESS, "192.168.0.179") #!!!! адрес кассы
  fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_IPPORT, "5555")
  fptr.applySingleSettings()

def print_check(tip,kassir,sectia,nomer_sect,tsena,kol):
  #Установка соединения с ККТ
  fptr.open()
  for number in range(kol): #несколько чеков
    fptr.setParam(1021, kassir)
    #fptr.setParam(1203, "123456789047")
    fptr.operatorLogin()
    #СНО: УСН доход-расход
    fptr.setParam(1055, IFptr.LIBFPTR_TT_USN_INCOME_OUTCOME)
    #Тип чека:Приход или возврат
    if tip==1:
      fptr.setParam(IFptr.LIBFPTR_PARAM_RECEIPT_TYPE, IFptr.LIBFPTR_RT_SELL)
    elif tip==2:
      fptr.setParam(IFptr.LIBFPTR_PARAM_RECEIPT_TYPE, IFptr.LIBFPTR_RT_SELL_RETURN) 
    #Открытие печатного чека
    fptr.openReceipt()
    #Регистрация позиции без указания суммы налога
    fptr.setParam(IFptr.LIBFPTR_PARAM_COMMODITY_NAME, sectia)
    fptr.setParam(IFptr.LIBFPTR_PARAM_DEPARTMENT, nomer_sect)
    fptr.setParam(IFptr.LIBFPTR_PARAM_PRICE, tsena)
    fptr.setParam(IFptr.LIBFPTR_PARAM_QUANTITY, 1)
    fptr.setParam(IFptr.LIBFPTR_PARAM_TAX_TYPE, IFptr.LIBFPTR_TAX_NO)
    fptr.registration()
    #Закрытие полностью оплаченного чека
    if fptr.closeReceipt()<0:
      print("{} [{}]".format (fptr.errorCode(), fptr.errorDescription()))
      time.sleep(3)
  #Бип
  fptr.beep()
  #Завершение соединения с ККТ
  fptr.close()

def print_otchet(tip, kassir):
  #Установка соединения с ККТ
  fptr.open()
  if tip==1:
    #X-отчет
    fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, IFptr.LIBFPTR_RT_X)
  elif tip==2:
    #Отчет по секциям
    fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, IFptr.LIBFPTR_RT_DEPARTMENTS)
  elif tip==3:
    #Отчет количеств
    fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, IFptr.LIBFPTR_RT_QUANTITY)
  elif tip==4:
    fptr.setParam(1021, kassir)
    #fptr.setParam(1203, "123456789047")
    fptr.operatorLogin() 
    #Закрытие смены
    fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, IFptr.LIBFPTR_RT_CLOSE_SHIFT)
  if fptr.report()<0:
    print("{} [{}]".format (fptr.errorCode(), fptr.errorDescription()))
    time.sleep(3)
  #Завершение соединения с ККТ
  fptr.close()

def vyplata(summa):
  #Установка соединения с ККТ
  fptr.beep()
  fptr.setParam(IFptr.LIBFPTR_PARAM_SUM, summa)
  if fptr.cashOutcome()<0:
      print("{} [{}]".format (fptr.errorCode(), fptr.errorDescription()))
      time.sleep(3)
  #Завершение соединения с ККТ
  fptr.close()
