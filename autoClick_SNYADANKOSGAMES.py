#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pyautogui as root
import Tkinter as interface
from Tkinter import *
import  time as t
from pynput import mouse
import findImageFromScreen_SNYADANKOSGAME as find



#INFORMATION----------------------------------------------------------------------
#HORIZONTAL
_linkImgStartAdGold = ["","","",""]
_linkImgStartAdWhite = ["","","",""]
_linkImgCentralAd = ["","","",""]
_linkImgCloseAd = ["","","",""]
_linkImgCloseApp = ["","","",""]
_linkImgOpenAppsHorizontal = ["","","",""]
_linkImgOpenAppsVertical = ["","","",""]
_linkImgUpdateButton = ""
_linkImgSendButton = ""



#INTERFACE----------------------------------------------------------------------
_interface = Tk()
# _interface=interface.Tk()
_interface.resizable(width=True,height=True)
_interface.configure()
_interface.geometry('1050x600')
_interface.title("SNYADANKOS GAME AUTO AD VIEW")


_startAutoClick = False

#HORIZONTAL-INTERFACE----------------------------------------------------
_lableGameNum = [interface.Label(text = 'Гра 1',font = 'Consolas'),interface.Label(text = 'Гра 2',font = 'Consolas'),interface.Label(text = 'Гра 3',font = 'Consolas'),interface.Label(text = 'Гра 4',font = 'Consolas')]
_lableGameNum[0].grid(sticky=W,column=1, row=0)
_lableGameNum[1].grid(sticky=W,column=2, row=0)
_lableGameNum[2].grid(sticky=W,column=3, row=0)
_lableGameNum[3].grid(sticky=W,column=4, row=0)

_lableLinkImgStartAdGold = interface.Label(text = 'Координати кнопки "Велика реклама"',font = 'Consolas')
_lableLinkImgStartAdGold.grid(sticky=W,column=0, row=1)
_entryLinkImgStartAdGold = [interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas')]
_entryLinkImgStartAdGold[0].grid(sticky=W,column=1, row=1)
_entryLinkImgStartAdGold[1].grid(sticky=W,column=2, row=1)
_entryLinkImgStartAdGold[2].grid(sticky=W,column=3, row=1)
_entryLinkImgStartAdGold[3].grid(sticky=W,column=4, row=1)

_lableLinkStartAdWhite = interface.Label(text = 'Координати кнопки "Маленька реклама"',font = 'Consolas')
_entryLinkStartAdWhite = [interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas')]
_lableLinkStartAdWhite.grid(sticky=W,column=0, row=2)
_entryLinkStartAdWhite[0].grid(sticky=W,column=1, row=2)
_entryLinkStartAdWhite[1].grid(sticky=W,column=2, row=2)
_entryLinkStartAdWhite[2].grid(sticky=W,column=3, row=2)
_entryLinkStartAdWhite[3].grid(sticky=W,column=4, row=2)

_lableImgCentralAd = interface.Label(text = 'Координати кнопки "Центральна кнопка"',font = 'Consolas')
_entryImgCentralAd = [interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas')]
_lableImgCentralAd.grid(sticky=W,column=0, row=3)
_entryImgCentralAd[0].grid(sticky=W,column=1, row=3)
_entryImgCentralAd[1].grid(sticky=W,column=2, row=3)
_entryImgCentralAd[2].grid(sticky=W,column=3, row=3)
_entryImgCentralAd[3].grid(sticky=W,column=4, row=3)

_lableImgCloseAd = interface.Label(text = 'Координати кнопки  "Повернутись назад"',font = 'Consolas')
_entryImgCloseAd = [interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas')]
_lableImgCloseAd.grid(sticky=W,column=0, row=4)
_entryImgCloseAd[0].grid(sticky=W,column=1, row=4)
_entryImgCloseAd[1].grid(sticky=W,column=2, row=4)
_entryImgCloseAd[2].grid(sticky=W,column=3, row=4)
_entryImgCloseAd[3].grid(sticky=W,column=4, row=4)

_lableImgCloseAp = interface.Label(text = 'Координати кнопки  "Вийти з гри"',font = 'Consolas')
_entryImgCloseAp = [interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas')]
_lableImgCloseAp.grid(sticky=W,column=0, row=6)
_entryImgCloseAp[0].grid(sticky=W,column=1, row=6)
_entryImgCloseAp[1].grid(sticky=W,column=2, row=6)
_entryImgCloseAp[2].grid(sticky=W,column=3, row=6)
_entryImgCloseAp[3].grid(sticky=W,column=4, row=6)

_lableImgUpdateScreen = interface.Label(text = 'Кнопка "Update screen"',font = 'Consolas')
_lableImgUpdateScreen.grid(sticky=W,column=0, row=7)
_entryImgUpdateScreen = interface.Entry(font = 'Consolas')
_entryImgUpdateScreen.grid(sticky=W,column=1, row=7)
_lableImgSendScreen = interface.Label(text = 'Кнопка "Send"',font = 'Consolas')
_lableImgSendScreen.grid(sticky=W,column=2, row=7)
_entryImgSendScreen = interface.Entry(font = 'Consolas')
_entryImgSendScreen.grid(sticky=W,column=3, row=7)

_lableImgOpenAppsVertical = interface.Label(text = 'Координати кнопки ігр в ВЕРТИКАЛЬНОМУ ЕКРАНІ',font = 'Consolas')
_entryImgOpenAppsVertical = [interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas'),interface.Entry(font = 'Consolas')]
_lableImgOpenAppsVertical.grid(sticky=W,column=0, row=8)
_entryImgOpenAppsVertical[0].grid(sticky=W,column=1, row=8)
_entryImgOpenAppsVertical[1].grid(sticky=W,column=2, row=8)
_entryImgOpenAppsVertical[2].grid(sticky=W,column=3, row=8)
_entryImgOpenAppsVertical[3].grid(sticky=W,column=4, row=8)

_lableClickSleep = interface.Label(text = 'Перерва між діями автоклікера (сек)',font = 'Consolas')
_entryClickSleep = interface.Entry(font = 'Consolas')
_lableClickSleep.grid(sticky=W,column=0, row=9)
_entryClickSleep.grid(sticky=W,column=1, row=9)

_lableMessage = interface.Label(text = 'Шукатиму елементи! Якщо програма нічого не робить більше 2х хв\nА кнопка є на екрані\nЦе означає, що Ви не правильно ввели назву кноки\nАбо такої кнопки немає.',font = 'Consolas')
_lableMessage.grid(sticky=W,column=0, row=11)

_lableCountOfAd = interface.Label(text = 'К-сть додаків.',font = 'Consolas')
_entryCountOfAd = interface.Entry(font = 'Consolas')
_lableCountOfAd.grid(sticky=W,column=1, row=12)
_entryCountOfAd.grid(sticky=W,column=2, row=12)

_lableMouseStart = interface.Label(text = 'Start',font = 'Consolas')
_entryMouseStart = interface.Entry(font = 'Consolas')
_lableMouseStart.grid(sticky=W,column=1, row=11)
_entryMouseStart.grid(sticky=W,column=2, row=11)
_lableMouseEnd = interface.Label(text = 'End',font = 'Consolas')
_entryMouseEnd = interface.Entry(font = 'Consolas')
_lableMouseEnd.grid(sticky=W,column=3, row=11)
_entryMouseEnd.grid(sticky=W,column=4, row=11)
_lableElementName = interface.Label(text = 'Назва елемента: ',font = 'Consolas')
_entryElementName = interface.Entry(font = 'Consolas')
_lableElementName.grid(sticky=W,column=3, row=12)
_entryElementName.grid(sticky=W,column=4, row=12)

_lableInfo0 = interface.Label(text = 'Радий Вас бачити! Тут також є маленька\nінструкція ->',font = 'Consolas')
_lableInfo0.grid(sticky=W,column=0, row=12)
_lableInfo1 = interface.Label(text = '- Коли запустили програму 2й раз\nнажимаєте кнопк "Contine" і всі збережені дані загрузяться\n- Дані зберігаються коли Ви нажимаєте "Start"\n- Коли Ви відкриваєте програму,\nдані автоматично загружаються\n- Коли Ви нажимаєте "Start". інтерфейс\nпрограми зависає, але вона працює\n- Щоб закрити після нажимання кнопки "Start"\nвикористовуйте cntr+alt+del\n- Після закриття програми не забудьте\nзайти в телефон і скинути боту КОД.\n- Всі дані щодо перегляду реклами\nзберігаються в телефоні.\n- УВАГА! Якщо Ви відкриєте програму та\nне нажмете кнопку "Start" збережені дані видаляться.',font = 'Consolas')
_lableInfo1.grid(sticky=W,column=0, row=13)
_lableInfo1 = interface.Label(text = 'by Snyadankos Game Studio',font = 'Consolas')
_lableInfo1.grid(sticky=W,column=0, row=14)
#BUTTONS-INTERFACE----------------------------------------------------
_buttonStart = interface.Button(text = 'Start',font = 'Consolas', background="#333")
_buttonStart.grid(sticky=W,column=0, row=10)
_buttonContine = interface.Button(text = 'Contine',font = 'Consolas', background="#333")
_buttonContine.grid(sticky=W,column=1, row=10)
_buttonSetCentr = interface.Button(text = 'Move to Centre',font = 'Consolas', background="#333")
_buttonSetCentr.grid(sticky=W,column=2, row=10)
_buttonGetElement = interface.Button(text = 'Get Element',font = 'Consolas', background="#333")
_buttonGetElement.grid(sticky=W,column=3, row=10)
_buttonFindElement = interface.Button(text = 'Find Element',font = 'Consolas', background="#333")
_buttonFindElement.grid(sticky=W,column=4, row=10)
#CONTINE PROGRAM--------------------------------------------------------
_contine = False
def CONTINE(event):
    global _contine
    _contine = True

#GET KEY--------------------------------------------------------
def GET_WIDTH_AND_HIGHT_ELEMENT(event):
    _key = str(repr(event.char))
    print _key
    _x,_y = root.position()
    if(_key=="'w'"):
        _entryMouseStart.delete(0, 'end')
        _entryMouseStart.insert(0,str(_x)+','+str(_y))
    if(_key=="'h'"):
        _entryMouseEnd.delete(0, 'end')
        _entryMouseEnd.insert(0,str(_x)+','+str(_y))
#GET ELEMENT FROM SCREEN--------------------------------------------------------
def SET_CENTRE(event):
    print find.GET_ELEMENT_CENTR(543, 454, 651, 530)
    try:
        _f = float(str(_entryMouseStart.get()).split(',')[0])
        _f = float(str(_entryMouseEnd.get()).split(',')[1])
    except:return
    _startPointW = int(str(_entryMouseStart.get()).split(',')[0])
    _startPointH = int(str(_entryMouseStart.get()).split(',')[1])
    _endPointW = int(str(_entryMouseEnd.get()).split(',')[0])
    _endPointH = int(str(_entryMouseEnd.get()).split(',')[1])
    root.moveTo(find.GET_ELEMENT_CENTR(_startPointW,_startPointH,_endPointW,_endPointH))
    pass
def GET_ELEMENT_IMG(event):
    if(_entryElementName.get()==''):_lableMessage.config(text = 'Напишіть будь-ласка назву елементу, яки Ви збираєтесь\nзберегти!')
    else:
        _startPointW = int(str(_entryMouseStart.get()).split(',')[0])
        _startPointH = int(str(_entryMouseStart.get()).split(',')[1])
        _endPointW = int(str(_entryMouseEnd.get()).split(',')[0])
        _endPointH = int(str(_entryMouseEnd.get()).split(',')[1])
        find.TAKE_ELEMENT_FROM_SCREEN(_entryElementName.get(),(_startPointW,_startPointH,_endPointW,_endPointH))
    pass
def CLICK_BACK():
    root.keyDown('ctrl')
    root.press('b')
    root.keyUp('ctrl')
def CLICK_QUIT():
    root.keyDown('ctrl')
    root.press('h')
    root.keyUp('ctrl')

def FIND_ELEMENT_ON_SCREEN_BUTTON(event):
    find.FIND_ELEMENT_NEW_VESRION(str(_entryElementName.get()))
    # root.click()


def UPDATE_SCREEN():
    global _linkImgUpdateButton
    global _linkImgSendButton
    FIND_ELEMENT_ON_SCREEN(_linkImgUpdateButton)
    t.sleep(4)
    FIND_ELEMENT_ON_SCREEN(_linkImgSendButton)
    t.sleep(2)

def FIND_ELEMENT_ON_SCREEN(_firstButton = "",_otherButton = ""):
    global _linkImgUpdateButton
    global _linkImgSendButton
    print _firstButton,_otherButton
    _result = False
    while _result==False:
        if (find.FIND_ELEMENT_NEW_VESRION(_linkImgUpdateButton) != None):
            root.click()
            t.sleep(4)
        if (find.FIND_ELEMENT_NEW_VESRION(_linkImgSendButton) != None):
            root.click()
            t.sleep(2)
        if(_otherButton != ""):
            print 'first'
            if(find.FIND_ELEMENT_NEW_VESRION(_otherButton)!=None):
                _result = True
        if (_firstButton != ""):
            print 'other'
            if (find.FIND_ELEMENT_NEW_VESRION(_firstButton) != None):
                _result = True

    root.click()

def CONTINE(event):
    global _contine
    _contine = True
#GET MOUSE POS-------------------------------------
while _contine == False:
    #GET MOUSE POS-------------------------------------
    _buttonContine.bind('<Button-1>', CONTINE)
    _buttonSetCentr.bind('<Button-1>', SET_CENTRE)
    _buttonGetElement.bind('<Button-1>', GET_ELEMENT_IMG)
    _buttonFindElement.bind('<Button-1>', FIND_ELEMENT_ON_SCREEN_BUTTON)
    _interface.bind("<Key>", GET_WIDTH_AND_HIGHT_ELEMENT)
    _interface.update_idletasks()
    _interface.update()
    # check click
#SAVE&LOAD----------------------------------------------------------------------
def LOAD():
    global _linkImgStartAdGold
    global _linkImgStartAdWhite
    global _linkImgCentralAd
    global _linkImgCloseAd
    global _linkImgCloseApp
    global _linkImgOpenAppsHorizontal
    global _linkImgOpenAppsVertical
    _infoList = [_entryLinkImgStartAdGold[0],_entryLinkImgStartAdGold[1],_entryLinkImgStartAdGold[2],_entryLinkImgStartAdGold[3],
                 _entryLinkStartAdWhite[0],_entryLinkStartAdWhite[1],_entryLinkStartAdWhite[2],_entryLinkStartAdWhite[3],
                 _entryImgCentralAd[0],_entryImgCentralAd[1],_entryImgCentralAd[2],_entryImgCentralAd[3],
                 _entryImgCloseAd[0],_entryImgCloseAd[1],_entryImgCloseAd[2],_entryImgCloseAd[3],
                 _entryImgCloseAp[0],_entryImgCloseAp[1],_entryImgCloseAp[2],_entryImgCloseAp[3],
                 _entryImgOpenAppsVertical[0],_entryImgOpenAppsVertical[1],_entryImgOpenAppsVertical[2],_entryImgOpenAppsVertical[3],
                 _entryImgUpdateScreen,_entryImgSendScreen,_entryImgUpdateScreen,_entryImgSendScreen]
    try:
        _file = open('snyadankos_save_file.txt', 'r')
        _infoText = _file.readlines()
        for i in range(len(_infoText)):
            _newText = _infoText[i][:-1]
            print _newText
            _infoList[i].delete(0, 'end')
            _infoList[i].insert(0,_newText)
        # _lableMessage.config(text='Збережені дані загружено!')
        _file.close()
    except:
        _lableMessage.config(text='Немає збережених даних\n - файл "snyadankos_save_file.txt" не знайдено')
def SAVE():
    _saveImgStartAdGold = [_entryLinkImgStartAdGold[0].get(),_entryLinkImgStartAdGold[1].get(),_entryLinkImgStartAdGold[2].get(),_entryLinkImgStartAdGold[3].get()]
    _saveImgStartAdWhite = [_entryLinkStartAdWhite[0].get(),_entryLinkStartAdWhite[1].get(),_entryLinkStartAdWhite[2].get(),_entryLinkStartAdWhite[3].get()]
    _saveImgCentralAd = [_entryImgCentralAd[0].get(),_entryImgCentralAd[1].get(),_entryImgCentralAd[2].get(),_entryImgCentralAd[3].get()]
    _saveImgCloseAd = [_entryImgCloseAd[0].get(),_entryImgCloseAd[1].get(),_entryImgCloseAd[2].get(),_entryImgCloseAd[3].get()]
    _saveImgCloseApp = [_entryImgCloseAp[0].get(),_entryImgCloseAp[1].get(),_entryImgCloseAp[2].get(),_entryImgCloseAp[3].get()]
    _saveImgOpenAppsVertical = [_entryImgOpenAppsVertical[0].get(),_entryImgOpenAppsVertical[1].get(),_entryImgOpenAppsVertical[2].get(),_entryImgOpenAppsVertical[3].get()]
    _saveImgUpdateScreen = [_entryImgUpdateScreen.get(),_entryImgSendScreen.get(),_entryImgUpdateScreen.get(),_entryImgSendScreen.get()]

    _infoList = [_saveImgStartAdGold,_saveImgStartAdWhite,_saveImgCentralAd,_saveImgCloseAd,_saveImgCloseApp,_saveImgOpenAppsVertical,_saveImgUpdateScreen]

    _file = open('snyadankos_save_file.txt', 'w')
    for i in range(len(_infoList)):
        for ii in range(4):
            _file.writelines(_infoList[i][ii].encode('utf-8') + '\n')
    _file.close()
    pass

#CLIKS----------------------------------------------------------------------
_clickSleepTimer = 0
_gameNum = 0
_maxgameNum = 3
_stepNum = 0
_countViewAds = 0
_countViewSlallAd = 0
_screenRotateStatus = ""
_screenCentreButtonPos = ()
_isAppOpen = False

#GET CENTRAL BUTTON----------------------------------------------------------------------
def GET_CENTRAL_BUTTON_COORDINATE(_centralButtonName = ''):
    global _screenCentreButtonPos
    FIND_ELEMENT_ON_SCREEN(_centralButtonName)
    x,y = root.position()
    _screenCentreButtonPos = (x,y)


LOAD()


#-----------------------------------------------------------------------------------------START-----------------------
def START_AUTO():
    print ('- очікую 5 сек.')
    t.sleep(5)
    global _clickSleepTimer
    global _startAutoClick
    global _stepNum
    global _gameNum
    global _maxgameNum
    global _countViewAds
    global _screenCentreButtonPos
    global _linkImgStartAdGold
    global _linkImgStartAdWhite
    global _linkImgCentralAd
    global _linkImgCloseAd
    global _linkImgCloseApp
    global _linkImgOpenAppsHorizontal
    global _linkImgOpenAppsVertical
    global _isAppOpen
    global _linkImgUpdateButton
    global _linkImgSendButton
    try:
        _clickSleepTimer = float(_entryClickSleep.get())
    except:
        _clickSleepTimer = 4
        _lableMessage.config(text = 'Ви не встановили час між діями.\nЧас між діями встановлено автоматично - 4 сек')
        t.sleep(2)
    print str(_entryLinkImgStartAdGold[_gameNum].get())[:-1]
    try:
        _linkImgStartAdGold = str(_entryLinkImgStartAdGold[_gameNum].get())

        _linkImgStartAdWhite = str(_entryLinkStartAdWhite[_gameNum].get())

        _linkImgCentralAd = str(_entryImgCentralAd[_gameNum].get())

        _linkImgCloseAd = str(_entryImgCloseAd[_gameNum].get())

        _linkImgCloseApp = str(_entryImgCloseAp[_gameNum].get())

        _linkImgOpenAppsVertical = str(_entryImgOpenAppsVertical[_gameNum].get())
        _linkImgUpdateButton = str(_entryImgUpdateScreen.get())
        print _linkImgUpdateButton
        _linkImgSendButton = str(_entryImgSendScreen.get())
    except:
        return
        pass


    # print _entryImgOpenAppsVertical[0].get()
    try:
        _file = open('snyadankos_save_file.txt', 'r')
        _file.close()
    except:
        SAVE()
    try:
        _maxgameNum = int(_entryCountOfAd.get())
    except:
        _maxgameNum = 4

#STEP--------0------------
    if(_stepNum == 0):
        print '- очікую 4 сек.'
        t.sleep(4)
        #відкриває додаток
        if(_isAppOpen==False):
            # UPDATE_SCREEN()
            FIND_ELEMENT_ON_SCREEN(_linkImgOpenAppsVertical)
            print '- очікую 15 сек.'
            t.sleep(15)
            _isAppOpen = True
        _lableMessage.config(text='Помилок немає.')
        UPDATE_SCREEN()
        GET_CENTRAL_BUTTON_COORDINATE(_linkImgCentralAd)
        UPDATE_SCREEN()
        FIND_ELEMENT_ON_SCREEN(_linkImgStartAdGold,_linkImgStartAdWhite)
        _stepNum = _stepNum+1
#STEP--------1------------
    if (_stepNum == 1):
        print ('- очікую 45 сек.')
        t.sleep(45)
        print _screenCentreButtonPos
        UPDATE_SCREEN()
        root.moveTo(_screenCentreButtonPos[0],_screenCentreButtonPos[1])
        root.click()
        _stepNum = _stepNum+1

#STEP--------2------------
    if (_stepNum == 2):
        print '- очікую ' + str(_clickSleepTimer) + '+ 6 сек.'
        t.sleep(_clickSleepTimer+float(6))
        UPDATE_SCREEN()
        FIND_ELEMENT_ON_SCREEN(_linkImgCloseAd)
        print '- очікую ' + str(_clickSleepTimer) + '*2 сек.'
        t.sleep(_clickSleepTimer)
        UPDATE_SCREEN()
        root.click()
        _stepNum = _stepNum+1
#STEP--------3------------
    if (_stepNum == 3):
        print '- очікую ' + str(_clickSleepTimer) + ' сек.'
        t.sleep(_clickSleepTimer)
        t.sleep(_clickSleepTimer)
        _countViewAds = _countViewAds+1
        if(_countViewAds<100):
            print ('- переглянутих реклам: '+str(_countViewAds)+' продовжую.')
            _stepNum = 0
            START_AUTO()
        else:
            print ('- переглянутих реклам: '+str(_countViewAds)+' перехожу до іншого додатку.')
            if(_gameNum<_maxgameNum):
                try:
                    _stepNum = 0
                    _countViewAds = 0
                    _gameNum = _gameNum+1
                    #закриває додаток
                    print '- очікую ' + str(_clickSleepTimer) + ' сек.'
                    t.sleep(_clickSleepTimer)
                    _isAppOpen = False
                    UPDATE_SCREEN()
                    FIND_ELEMENT_ON_SCREEN(_linkImgCloseApp)
                    print _gameNum
                    _screenRotateStatus = ""
                    _screenCentreButtonPos = []
                    _isFindedAllButtonPos = False
                    START_AUTO()
                except:
                    _lableMessage.config(text='Помилка - не можу знайти кнопку "Вихід"\nАбо не можу знайти наступний додаток.')
                    return

    pass



def CLICK_START(event):
    _startAutoClick = True
    START_AUTO()

_buttonStart.bind('<Button-1>',CLICK_START)
_buttonFindElement.bind('<Button-1>', FIND_ELEMENT_ON_SCREEN_BUTTON)
_interface.mainloop()
