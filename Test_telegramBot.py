#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3 as db
import telebot
from  telebot import types
import time
import operator
import sys
x = 2000
sys.setrecursionlimit(x)
### DATA BASE CONTROLLER
_connection = None


def GET_CONNECTION():
    global _connection
    if _connection is None:
        _connection = db.connect("QESDAFXZ.db",check_same_thread = False)
        _connection.text_factory = str
    return _connection

def INIT_DB (force = False):
    connection = GET_CONNECTION()
    curs = connection.cursor()

    if force:
        curs.execute("DROP TABLE IF EXISTS WSAD")

    curs.execute("""
    CREATE TABLE IF NOT EXISTS WSAD (
    FASDVXZ INTEGER NOT NULL,
    RQVASDXZ TEXT NOT NULL,
    QERVDS TEXT NOT NULL,
    VRADS INTEGER NOT NULL,
    RQVSD INTEGER NOT NULL,
    QRVS INTEGER NOT NULL,
    ERQSAD FLOAT NOT NULL,
    QSDA FLOAT NOT NULL,
    user_code_num TEXT NOT NULL,
    user_mail TEXT NOT NULL,
    user_last_date_add_ad INTEGER NOT NULL,
    user_current_bot_status_answer INTEGER NOT NULL
    )
    """)
    connection.commit()

def INIT_BLACK_LIST_DB(force = False):
    connection = GET_CONNECTION()
    curs = connection.cursor()

    if force:
        curs.execute("DROP TABLE IF EXISTS BlackList")

    curs.execute("""
        CREATE TABLE IF NOT EXISTS BlackList (
        user_id INTEGER NOT NULL
        )
        """)
INIT_DB()
INIT_BLACK_LIST_DB()

def REGISTER_NEW_USER(_userId,_userName,_userPass,_userCodeNum,_userMail,_userReferalId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _curs.execute("INSERT INTO WSAD (user_id, user_name,user_pass,user_code_num,user_mail,user_ads_count,user_today_ads_count,user_referal_id,user_ad_profit, user_referal_profit,user_last_date_add_ad,user_current_bot_status_answer) VALUES (?, ?, ?, ?, ?,?,?,?,?,?,?,?)",
                 (_userId,_userName,_userPass,_userCodeNum,_userMail,0,0,_userReferalId,0.0,0.0,0,0))
    connection.commit()

def SET_NEW_BLOCK_USER(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _curs.execute("INSERT INTO WSAD (user_id) VALUES (?)",(_userId,))
    connection.commit()

# REGISTER_NEW_USER(1,'Користувач','Pass','0000','Нет',0)
def SET_LAST_DATE(_userId,_newDate):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _curs.execute("UPDATE WSAD SET user_last_date_add_ad = ? WHERE user_id = ?", (_newDate,_userId))
    connection.commit()

def SET_CURRENT_BOT_ANSWER_STATUS(_userId,_botStatusNum):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _curs.execute("UPDATE WSAD SET user_current_bot_status_answer = ? WHERE user_id = ?", (_botStatusNum,_userId))
    connection.commit()

def SET_NEW_AD_PROFIT(_userId,_newAdProfit):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _lastAdProfit = _curs.execute("SELECT user_ad_profit FROM WSAD WHERE user_id = ?",(_userId,)).fetchall()[0][0]
    _newAdProfit = _lastAdProfit+_newAdProfit
    _curs.execute("UPDATE WSAD SET user_ad_profit = ? WHERE user_id = ?",(_newAdProfit, _userId))
    connection.commit()

def SET_NULL_ALL_PROFIT(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _curs.execute("UPDATE WSAD SET user_ad_profit = ? WHERE user_id = ?", (0, _userId))
    _curs.execute("UPDATE WSAD SET user_referal_profit = ? WHERE user_id = ?", (0, _userId))
    connection.commit()
def SET_NULL_PROFIT(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _curs.execute("UPDATE WSAD SET user_ad_profit = ? WHERE user_id = ?", (0, _userId))
    connection.commit()

def SET_NEW_UNWORKED_DAY(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _unworkedDays = _curs.execute("SELECT user_ads_count FROM WSAD WHERE user_id = ?",(_userId,)).fetchall()[0][0]
    _newUnworkedDaays = _unworkedDays+1
    _curs.execute("UPDATE WSAD SET user_ads_count = ? WHERE user_id = ?",(_newUnworkedDaays, _userId))
    connection.commit()

def SET_NULL_UNWORKED_DAY(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _newUnworkedDaays = 0
    _curs.execute("UPDATE WSAD SET user_ads_count = ? WHERE user_id = ?",(_newUnworkedDaays, _userId))
    connection.commit()

def SET_NEW_REFERAL_PROFIT(_userId,_newReferalProfit):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _lastReferalProfit = _curs.execute("SELECT user_referal_profit FROM WSAD WHERE user_id = ?",(_userId,)).fetchall()[0][0]
    _newReferalProfit = _lastReferalProfit + _newReferalProfit
    _curs.execute("UPDATE WSAD SET user_referal_profit = ? WHERE user_id = ?",(_newReferalProfit, _userId))
    connection.commit()

def SET_NEW_MOUNCE_PROFIT(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _currentUserProfit = _curs.execute("SELECT user_ad_profit FROM WSAD WHERE user_id = ?",(_userId,)).fetchall()[0][0]
    _lastMounceUserProfit = _curs.execute("SELECT user_code_num FROM WSAD WHERE user_id = ?",(_userId,)).fetchall()[0][0]
    _newLastMonceProfit = _currentUserProfit+float(_lastMounceUserProfit)
    print _newLastMonceProfit
    _curs.execute("UPDATE WSAD SET user_code_num = ? WHERE user_id = ?",(_newLastMonceProfit, _userId))
    connection.commit()

def SET_NEW_ADS_COUNT(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _adsCountToday = _curs.execute("SELECT user_today_ads_count FROM WSAD WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    _lastAdsCount = _curs.execute("SELECT user_ads_count FROM WSAD WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    _newAdsCount = _lastAdsCount + _adsCountToday
    _curs.execute("UPDATE WSAD SET user_ads_count = ? WHERE user_id = ?",(_newAdsCount, _userId))
    connection.commit()

def SET_NEW_CURRENT_ADS_COUNT(_userId,_newAdsCount):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _lastAdsCount = _curs.execute("SELECT user_today_ads_count FROM WSAD WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    _newAdsCount = _lastAdsCount + _newAdsCount
    _curs.execute("UPDATE WSAD SET user_today_ads_count = ? WHERE user_id = ?",(_newAdsCount, _userId))
    connection.commit()

def SET_NEW_VIEW_PROFIT(_userId,_profit):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _lastProfit = _curs.execute("SELECT user_ad_profit FROM WSAD WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    _newProfit = _lastProfit + _profit
    _curs.execute("UPDATE WSAD SET user_ad_profit = ? WHERE user_id = ?",(_newProfit, _userId))
    connection.commit()
def SET_NEW_USER_REFERAL(_userId,_referalId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _curs.execute("UPDATE WSAD SET user_referal_id = ? WHERE user_id = ?", (_userId, _referalId))
    connection.commit()

def SET_NEW_REFERAL_PROFIT(_userId,_referalProfit):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _lastReferalProfit = _curs.execute("SELECT user_referal_profit FROM WSAD WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    _newReferalProfit = _lastReferalProfit + _referalProfit
    _curs.execute("UPDATE WSAD SET user_referal_profit = ? WHERE user_id = ?",(_newReferalProfit, _userId))
    connection.commit()

def SET_NEW_USER_PASS(_userId,_newPass):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _curs.execute("UPDATE WorkersInformation SET user_pass = ? WHERE user_id = ?", (_newPass, _userId))
    connection.commit()
def SET_NULL_CURRENT_ADS_COUNT(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _curs.execute("UPDATE WSAD SET user_today_ads_count = ? WHERE user_id = ?", (0, _userId))
    connection.commit()
def SET_NULL_CURRENT_BOT_ANSWER_STATUS(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _curs.execute("UPDATE WSAD SET user_current_bot_status_answer = ? WHERE user_id = ?",
                  (0, _userId))
    connection.commit()
def SET_CURRENT_BOT_ANSWER_STATUS(_userId,_answerStatus):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _curs.execute("UPDATE WSAD SET user_current_bot_status_answer = ? WHERE user_id = ?",
                  (_answerStatus, _userId))
    connection.commit()
def SET_USER_DAY_IN_PROJECT(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    try:
        _userDays = int(_curs.execute("SELECT user_mail FROM WSAD WHERE user_id = ?",(_userId,)).fetchall()[0][0])
    except:
        _userDays = 0
    _userDays = _userDays+1
    _curs.execute("UPDATE WSAD SET user_mail = ? WHERE user_id = ?", (str(_userDays), _userId))
    connection.commit()
def GET_UNWORKED_DAY(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _unworkedDays = _curs.execute("SELECT user_ads_count FROM WSAD WHERE user_id = ?",(_userId,)).fetchall()[0][0]
    return _unworkedDays

def GET_CURRENT_BOT_ANSWER_STATUS(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _currentBotAndserStatus = _curs.execute("SELECT user_current_bot_status_answer FROM WSAD WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    return _currentBotAndserStatus

def GET_CURRENT_ADS_COUNT(_userId):
    try:
        connection = GET_CONNECTION()
        _curs = connection.cursor()
        _adsCountToday = _curs.execute("SELECT user_today_ads_count FROM WSAD WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    except:
        pass
    return _adsCountToday

def GET_ALL_ADS_COUNT(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _adsCountToday = _curs.execute("SELECT user_ads_count FROM WSAD WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    return _adsCountToday

def GET_ALL_USERS_ADS_COUNT():
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _allUsersAdCount = _curs.execute("SELECT user_today_ads_count FROM WSAD").fetchall()
    return _allUsersAdCount

def GET_REFERAL_PROFIT(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _referalProfit = _curs.execute("SELECT user_referal_profit FROM WSAD WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    return _referalProfit
def GET_REFERAL_ID(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _referalProfit = _curs.execute("SELECT user_referal_id FROM WSAD WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    return _referalProfit
def GET_USER_ALL_DAY_IN_PROJECT(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _adProfit = _curs.execute("SELECT user_mail FROM WSAD WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    return _adProfit
def GET_AD_PROFIT(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _adProfit = _curs.execute("SELECT user_ad_profit FROM WSAD WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    return _adProfit
def GET_AD_PROFIT_LAST_MOUNSE(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _adProfit = _curs.execute("SELECT user_code_num FROM WSVD WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    return _adProfit
def GET_RESTERED_USERS_ID():
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _registeredUsersId = _curs.execute("SELECT user_id FROM RWSDVA").fetchall()
    return _registeredUsersId

def GET_RESTERED_USERS_ID_BLACK_LIST():
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _registeredUsersId = _curs.execute("SELECT user_id FROM WDSVA").fetchall()
    return _registeredUsersId

def GET_USER_NAME(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _userName = _curs.execute("SELECT user_name FROM wvsdA WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    # _userName = _userName.decode('UTF-8', 'ignore')
    # try:
    #     _userName = str(_userName).decode('UTF-8', 'ignore')
    # except:
    #     pass

    return _userName

def GET_USER_PASS(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _userPass = _curs.execute("SELECT user_pass FROM WVsdac WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    return _userPass

def GET_LAST_DATE(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _userLastAdDate = _curs.execute("SELECT user_last_date_add_ad FROM wvsdXZ WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    return _userLastAdDate

def GET_REFERAL_IDS():
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _referalIds = _curs.execute("SELECT user_referal_id FROM qwvds").fetchall()
    return _referalIds

def DELETE_USER_BY_ID(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _curs.execute("DELETE FROM RWEVsdaxz WHERE user_id = ?",(_userId,))

def DELETE_USER_BY_ID_IN_BLACK_LIST(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _curs.execute("DELETE FROM wqsdaZC WHERE user_id = ?",(_userId,))
# print GET_REFERAL_IDS()
#COMPILATOR

o = 'QWERTNASOFGXCAZVBNHGFDSNHGFDSNHGFDSNHGFDS'
dictKeys = {'rvasd':1,'svdazx':2,'qsvadz':3,'vsdax':4,'vsda':5,'rvsda':6,'rvsd':7,'rwvdsax':8,'wvsda':9,'rwvsda':0}
# print dictKeys.keys()
def FOUNDKEYS(_code):
    _foundKey = ''
    for i in range(len(dictKeys)):
        if (_code == dictKeys.keys()[i]):
            _foundKey = _foundKey+str(dictKeys.values()[i])
    return _foundKey

# def DECOMPILATE_USER_NAME(_userMessage):
#     _userName = ''
#     try:
#         _newMessage = _userMessage.split('X')
#         _newMessage[0] = _newMessage[0].split('N')
#         _newMessage[1] = _newMessage[1].split('N')
#         _newMessage[2] = _newMessage[2].split('N')
#         _userName = str(GET_USER_NAME(_userTelegramId))
#         # _newMessage[2] = 0
#     except: return 'no name'
_gameVERSION = 2
def DECOMPILATE(_userMessage):
    try:
        _newMessage = _userMessage.split('X')
        _newMessage[0] = _newMessage[0].split('N')
        _newMessage[1] = _newMessage[1].split('N')
        _newMessage[2] = _newMessage[2].split('N')
        _newMessage[3] = _newMessage[3].split('N')
        # _newMessage[2] = 0
    except: return {'eqrvsad':0,'evasd':0,'veasd':0,'rvsadzx':0}
    try:
        # print _newMessage
        _decompulatedValues = []
        _userAdsCount = 0
        _userLastDate = 0
        _userTelegramId = 0
        _userGameVersion = 0
        _userTelegramName = 'no name'
        _failedData = False
        for i in range(len(_newMessage)):
            _newValue = ''
            print _newMessage[i]
            for ii in range(len(_newMessage[i])):
                if(FOUNDKEYS(_newMessage[i][ii])==''):
                    _failedData = True
                else: _newValue = _newValue+FOUNDKEYS(_newMessage[i][ii])
            _decompulatedValues.append(_newValue)
        _userAdsCount = int(_decompulatedValues[0])
        _userLastDate = int(_decompulatedValues[1])
        _userTelegramId = int(_decompulatedValues[2])
        _userGameVersion = int(_decompulatedValues[3])
    except: return {'fsavdzx': 0, 'fasvdzX': 0, 'vsad': 0, 'rvsad': 0,'qvsad':-1}

    try:
        _userTelegramName = str(GET_USER_NAME(_userTelegramId))
    except:
        pass

    if(_failedData):
        _decompulatedValues = []
        return 0
    else:
        return {'qrvsdaxz':_userAdsCount,'vsdz':_userLastDate,'vrsad':_userTelegramId,'vrsdaxz':_userTelegramName,'rqvsadxZ':_userGameVersion}


###TELEGRAM BOT CONTROLLER

client = telebot.TeleBot('tbeqfdasvzXC')
def SEND_STANDART_MESSAGE(message):
    client.send_message(message.chat.id,'geqbdfasvxzCbfdasdv')
    SET_START_INLINE_BUTTONS(message)
def GET_ALL_VIEWS():
    _allUsersAdCountSumArray = []
    _allUsersAdCountSum = 0
    for i in range(len(GET_ALL_USERS_ADS_COUNT())):
        _allUsersAdCountSumArray.append(GET_ALL_USERS_ADS_COUNT()[i][0])
    _allUsersAdCountSum = sum(_allUsersAdCountSumArray)
    return _allUsersAdCountSum

def CHECKISREGISTERUSER_FOR_REFERAL(_userId):
    _registeredUserId = -1
    _newRegesterArray = []
    for i in range(len(GET_RESTERED_USERS_ID())):
        _newRegesterArray.append(GET_RESTERED_USERS_ID()[i][0])
    if(_userId in _newRegesterArray):
        _registeredUserId = 1
    else:
        _registeredUserId = -1

    if(_registeredUserId==-1):
        return False
    else:
        return  True

def SEN_NEW_LAST_DATE():
    try:
        _allUsersIdsArrat = []
        _curDate = int(round(time.time() * 1000))
        for i in range(len(GET_RESTERED_USERS_ID())):
            _allUsersIdsArrat.append(GET_RESTERED_USERS_ID()[i][0])
        for i in range(len(_allUsersIdsArrat)):
            SET_LAST_DATE(_allUsersIdsArrat[i],_curDate)
            SET_USER_DAY_IN_PROJECT(_allUsersIdsArrat[i])
    except:
        pass
def SET_NEW_REFERAL(_userId,_referalId,_message):
    try:
        if(GET_REFERAL_ID(_referalId)!=0):
            client.send_message(_message.chat.id, 'qebfasdvxz',reply_markup=types.ReplyKeyboardRemove())
            SEND_STANDART_MESSAGE(_message)
            return
        if(_userId == _referalId):
            client.send_message(_message.chat.id, 'qfbsadvxzC',reply_markup=types.ReplyKeyboardRemove())
            SEND_STANDART_MESSAGE(_message)
            return
        SET_NEW_USER_REFERAL(_userId,_referalId)
        client.send_message(_message.chat.id, 'gdfbasdvxzC',reply_markup=types.ReplyKeyboardRemove())
        SEND_STANDART_MESSAGE(_message)
    except:
        client.send_message(_message.chat.id, 'gdfbaszXVZC',reply_markup=types.ReplyKeyboardRemove())
        SEND_STANDART_MESSAGE(_message)
def GET_UNWORKS_DAY(_userId):
    connection = GET_CONNECTION()
    _curs = connection.cursor()
    _userUnworksDay = _curs.execute("SELECT user_ads_count FROM WorkersInformation WHERE user_id = ?", (_userId,)).fetchall()[0][0]
    return _userUnworksDay

def GET_TOP_5_USERS():
    _allUsersIDs = []
    _allViews = []
    _allProfits = {}
    #отримує всіх користувачів
    for i in range(len(GET_RESTERED_USERS_ID())):
        _allUsersIDs.append(GET_RESTERED_USERS_ID()[i][0])
    _allViews = [int(GET_CURRENT_ADS_COUNT(_allUsersIDs[i])) for i in range(len(_allUsersIDs))]
    _allViews = sorted(_allViews)[-8:]
    _allViews = list(reversed(_allViews))
    # print _allViews
    _allProfits = {int(_allUsersIDs[i]): int(GET_CURRENT_ADS_COUNT(_allUsersIDs[i])) for i in range(len(_allUsersIDs))}
    _topIds = []
    for i in range(len(_allViews)):
        for k, v in _allProfits.items():
            if v == _allViews[i]:
                if(k not in _topIds):
                    _topIds.append(k)

    _topDist = {GET_USER_NAME(_topIds[i]): str(GET_CURRENT_ADS_COUNT(_topIds[i])) for i in range(len(_topIds))}
    print "TOP"
    _topString = ''
    for i in range(len(_topIds)):
        if (i==0):
            _topString = _topString + 'fqvadsxzC: \n'
        if (i>10): break
        if(i<=2):
            _topString = _topString +'  ✔'+ str(GET_USER_NAME(_topIds[i])) + ' : ' + str(GET_CURRENT_ADS_COUNT(_topIds[i])) + '\n'
        else:
            _topString = _topString +'  ➤'+ str(GET_USER_NAME(_topIds[i])) + ' : ' + str(GET_CURRENT_ADS_COUNT(_topIds[i])) + '\n'
        if (i==2):
            _topString = _topString + 'fqdbasvzxC: \n'
    return _topString
# print GET_TOP_5_USERS()
def GET_ALL_UNWORKED_USERS():
    try:
        _newListFoAnworkedUsers = ''
        _allUnworkedUsersId = []
        _allUsersIdsArrat = []
        _splitSum = 0.0

        for i in range(len(GET_RESTERED_USERS_ID())):
            _allUsersIdsArrat.append(GET_RESTERED_USERS_ID()[i][0])

        for i in range(len(_allUsersIdsArrat)):
            if(GET_UNWORKED_DAY(_allUsersIdsArrat[i])>=7):
                _splitSum = float(_splitSum) + float(GET_AD_PROFIT(_allUsersIdsArrat[i]))
                _allUnworkedUsersId.append(_allUsersIdsArrat[i])
        if(_allUnworkedUsersId==[]):
            return 'gdfabsvzxC'
        else:
            for i in range(len(_allUnworkedUsersId)):
                _newListFoAnworkedUsers = _newListFoAnworkedUsers+''+str(_allUnworkedUsersId[i])+' qebfasdvxZ: '+str(GET_USER_NAME(_allUnworkedUsersId[i]))+'\n'
            return 'fbdasvzXC = '+str(_splitSum)+'\n'+_newListFoAnworkedUsers

    except:
        return 'fbasdvzx'
def SET_ALL_NEW_MOUNSE():
    try:
        _allUsersIdsArrat = []
        for i in range(len(GET_RESTERED_USERS_ID())):
            _allUsersIdsArrat.append(GET_RESTERED_USERS_ID()[i][0])

        for i in range(len(_allUsersIdsArrat)):
            SET_NEW_MOUNCE_PROFIT(_allUsersIdsArrat[i])
            SET_NULL_PROFIT(_allUsersIdsArrat[i])
        return 'fbasdvzX!'
    except:
        return 'fbsadvZX'
def SET_USER_NEW_MOUNSE(_userId):
    try:
        SET_NEW_MOUNCE_PROFIT(_userId)
        SET_NULL_PROFIT(_userId)
        return 'Готово!'
    except:
        return 'qfasbcxzv'
def DELETE_ALL_UNWORKED_USERS():
    try:
        _newListFoAnworkedUsers = ''
        _allUnworkedUsersId = []
        _allUsersIdsArrat = []
        _splitSum = 0.0

        for i in range(len(GET_RESTERED_USERS_ID())):
            _allUsersIdsArrat.append(GET_RESTERED_USERS_ID()[i][0])

        for i in range(len(_allUsersIdsArrat)):
            if(GET_UNWORKED_DAY(_allUsersIdsArrat[i])>=7):
                _splitSum = float(_splitSum) + float(GET_AD_PROFIT(_allUsersIdsArrat[i]))
                _allUnworkedUsersId.append(_allUsersIdsArrat[i])
        if(_allUnworkedUsersId==[]):
            return 'fasdvXZc.'
        else:
            for i in range(len(_allUnworkedUsersId)):
                _userName = str(GET_USER_NAME(_allUnworkedUsersId[i]))
                DELETE_USER_BY_ID(_allUnworkedUsersId[i])
                SET_NEW_BLOCK_USER(_allUnworkedUsersId[i])
                _newListFoAnworkedUsers = _newListFoAnworkedUsers+''+str(_allUnworkedUsersId[i])+' efasdvxz: '+str(_userName)+' - fsabczxv\n'
            return 'vefadszxc = '+str(_splitSum)+'\n'+_newListFoAnworkedUsers

    except:
        return 'fasvdczxя'


def GET_ALL_3_DAYS_UNWORKED_USERS():
    try:
        _newListFoAnworkedUsers = ''
        _allUnworkedUsersId = []
        _allUsersIdsArrat = []
        _splitSum = 0.0

        for i in range(len(GET_RESTERED_USERS_ID())):
            _allUsersIdsArrat.append(GET_RESTERED_USERS_ID()[i][0])

        for i in range(len(_allUsersIdsArrat)):
            if(GET_UNWORKED_DAY(_allUsersIdsArrat[i])>=1):

                _splitSum = float(_splitSum) + float(GET_AD_PROFIT(_allUsersIdsArrat[i]))
                _allUnworkedUsersId.append(_allUsersIdsArrat[i])
        if(_allUnworkedUsersId==[]):
            return 'fsabdcxzV.'
        else:
            for i in range(len(_allUnworkedUsersId)):
                _newListFoAnworkedUsers = _newListFoAnworkedUsers+'@'+str(GET_USER_NAME(_allUnworkedUsersId[i]))+' '
            return 'Сума на розподіл = '+str(_splitSum)+'\n'+_newListFoAnworkedUsers

    except:
        return 'fasbdcxzv'

def GET_PAY_OUT_INFO():
    try:
        _allUsersIdsArrat = []
        _allMoneySum = 0.0

        for i in range(len(GET_RESTERED_USERS_ID())):
            _allUsersIdsArrat.append(GET_RESTERED_USERS_ID()[i][0])

        for i in range(len(_allUsersIdsArrat)):
            _allMoneySum = float(_allMoneySum) + float(GET_AD_PROFIT(_allUsersIdsArrat[i]))
        return 'dfscxzv = '+str(_allMoneySum)

    except:
        return 'fasdzvx'

def SET_USERS_PROFITS(_sum):
    try:
        _allAdViewsSum = GET_ALL_VIEWS()
        _allNotWorkedUsersSum = 0
        _allNotWorkedUsersSumInProcent = 0
        _allWorkedUsersSum = 0
        _allWorkedUsersSumInProcent = 0
        _priceForOneView = float(_sum)/float(_allAdViewsSum)
        _allUsersIdsArrat = []
        for i in range(len(GET_RESTERED_USERS_ID())):
            _allUsersIdsArrat.append(GET_RESTERED_USERS_ID()[i][0])
        for i in range(len(_allUsersIdsArrat)):
            SET_NEW_VIEW_PROFIT(_allUsersIdsArrat[i],float(GET_CURRENT_ADS_COUNT(_allUsersIdsArrat[i]))*float(_priceForOneView))
            try:
                SET_NEW_REFERAL_PROFIT(GET_REFERAL_ID(_allUsersIdsArrat[i]),float(GET_CURRENT_ADS_COUNT(_allUsersIdsArrat[i]))*float(0.0005))
            except:
                pass
            if(int(GET_CURRENT_ADS_COUNT(_allUsersIdsArrat[i]))<=0):
                _allNotWorkedUsersSum = _allNotWorkedUsersSum+1
                SET_NEW_UNWORKED_DAY(_allUsersIdsArrat[i])
            else:
                _allWorkedUsersSum = _allWorkedUsersSum+1
                SET_NULL_UNWORKED_DAY(_allUsersIdsArrat[i])
            SET_NULL_CURRENT_ADS_COUNT(_allUsersIdsArrat[i])
        _allUsers = _allNotWorkedUsersSum+_allWorkedUsersSum
        _allNotWorkedUsersSumInProcent = round((float(_allNotWorkedUsersSum)/float(_allUsers))*100.0)
        _allWorkedUsersSumInProcent = round((float(_allWorkedUsersSum)/float(_allUsers))*100.0)

        return [_priceForOneView,_allAdViewsSum,_allNotWorkedUsersSum,_allNotWorkedUsersSumInProcent,_allWorkedUsersSum,_allWorkedUsersSumInProcent,]
    except: [0,0,0,0,0,0]

def GET_INFO_FOR_STATICTIC():
    try:
        _allAdViewsSum = GET_ALL_VIEWS()
        _allNotWorkedUsersSum = 0
        _allNotWorkedUsersSumInProcent = 0
        _allWorkedUsersSum = 0
        _allWorkedUsersSumInProcent = 0
        _priceForOneView = 0
        _allUsersIdsArrat = []
        for i in range(len(GET_RESTERED_USERS_ID())):
            _allUsersIdsArrat.append(GET_RESTERED_USERS_ID()[i][0])
        for i in range(len(_allUsersIdsArrat)):
            if(int(GET_CURRENT_ADS_COUNT(_allUsersIdsArrat[i]))<=0):
                _allNotWorkedUsersSum = _allNotWorkedUsersSum+1
            else:
                _allWorkedUsersSum = _allWorkedUsersSum+1
        _allUsers = _allNotWorkedUsersSum+_allWorkedUsersSum
        _allNotWorkedUsersSumInProcent = round((float(_allNotWorkedUsersSum)/float(_allUsers))*100.0)
        _allWorkedUsersSumInProcent = round((float(_allWorkedUsersSum)/float(_allUsers))*100.0)

        return [_priceForOneView,_allAdViewsSum,_allNotWorkedUsersSum,_allNotWorkedUsersSumInProcent,_allWorkedUsersSum,_allWorkedUsersSumInProcent,]
    except:[0, 0, 0, 0, 0, 0]

def CHECK_IS_TRUE_DATE_OF_AD(_userId,_date):
    _result = False
    _lastUserAdAddDate = GET_LAST_DATE(_userId)
    if((_date-_lastUserAdAddDate)>0):
        _result = True
    return _result

def CHECKISREGISTERUSER(_userId):
    _registeredUserId = -1
    _newRegesterArray = []
    for i in range(len(GET_RESTERED_USERS_ID())):
        _newRegesterArray.append(GET_RESTERED_USERS_ID()[i][0])
    if(_userId in _newRegesterArray):
        _registeredUserId = 1
    else:
        _registeredUserId = -1

    if(_registeredUserId==-1):
        return False
    else:
        return  True
def CHECK_LAST_DATE_IN_ALL(_checkedDate):
    _allUsersIdsArrat = []
    _result = True
    for i in range(len(GET_RESTERED_USERS_ID())):
        _allUsersIdsArrat.append(GET_RESTERED_USERS_ID()[i][0])
    for i in range(len(_allUsersIdsArrat)):
        if(int(GET_LAST_DATE(_allUsersIdsArrat[i]))==int(_checkedDate)):
            return False
    return _result
def CHECK_BLACK_LIST(_userId):
    _result = False
    _allUsersIdsArrat = []
    for i in range(len(GET_RESTERED_USERS_ID_BLACK_LIST())):
        _allUsersIdsArrat.append(GET_RESTERED_USERS_ID_BLACK_LIST()[i][0])
    if(_userId in _allUsersIdsArrat):
        return True
    pass
def ADD_NEW_AD_COUNT(_code,_userId):
    _result = False
    try:
        _decompilatedCode = DECOMPILATE(_code)
        print _decompilatedCode
        if(CHECK_IS_TRUE_DATE_OF_AD(_userId,_decompilatedCode['user_last_data'])==True):
            if(_decompilatedCode['user_game_version']!=_gameVERSION):
                return False
            if(_decompilatedCode['user_telegram_id']!=_userId):
                return False
            # if(CHECK_LAST_DATE_IN_ALL(_decompilatedCode['user_last_data'])==False):
            #     return False
            SET_LAST_DATE(_userId,_decompilatedCode['user_last_data'])
            SET_NEW_CURRENT_ADS_COUNT(_userId,_decompilatedCode['user_ads_count'])
            _result = True
        else:_result = False
    except:pass
    return _result

def GET_ALL_REFERAL_BY_USER(_userId):
    _allReferalIds = GET_REFERAL_IDS()
    # print _allReferalIds
    _userReferalCount = 0
    for i in range(len(_allReferalIds)):
        if(_allReferalIds[i][0]==_userId):
            _userReferalCount = _userReferalCount+1
    return str(_userReferalCount)


def GET_USER_STAT(_userId):
    _userAdCountToday = ''
    _userAllAdCount = ''
    _userAdProfit = ''
    _userReferalCount = ''
    _userRefaralProfit = ''
    _userAdCountToday = str(GET_CURRENT_ADS_COUNT(_userId))
    _userAllAdCount = str(GET_ALL_ADS_COUNT(_userId))
    _userAdProfit = str(GET_AD_PROFIT(_userId))
    _userReferalCount = str(GET_ALL_REFERAL_BY_USER(_userId))
    _userRefaralProfit = str(GET_REFERAL_PROFIT(_userId))
    _userUnworksDays = str(GET_UNWORKS_DAY(_userId))
    _userAdProfitLastMounse = str(GET_AD_PROFIT_LAST_MOUNSE(_userId))
    _allUserDayInProject = str(GET_USER_ALL_DAY_IN_PROJECT(_userId))
    return 'wefdscxzv: '+_userAdCountToday+'\n----- ----- -----\nvfadscxz: '+_userAdProfit+'$\nedfasvzxC: '+_userAdProfitLastMounse+'$\n----- ----- -----\nefadsvcxz: '+_userReferalCount+'\nedafbscxzv: '+_userRefaralProfit+'$\n----- ----- -----\nefdabsvcxz: '+_userUnworksDays+'\nwgdfbasvxz: '+_allUserDayInProject

# print ADD_NEW_AD_COUNT('QWERTNASOFGXQWERTNJGFOINPUYTRNUYTOPNHGFDSNHGFDSNUYTOPNMBVCUNMBVCUNLKJHRNUYTOPNASOFGNDSAWM',1391548525)

def SET_START_INLINE_BUTTONS(message):
    _markup_inline = types.InlineKeyboardMarkup()
    _itemCode = types.InlineKeyboardButton(text='Продовжити роботу', callback_data='_contineWork')
    _itemStatictic = types.InlineKeyboardButton(text='Закрити', callback_data='_stopWork')
    _itemGuide = types.InlineKeyboardButton(text='fasdvzxcwd', callback_data='_guide')
    _markup_inline.add(_itemCode, _itemGuide, _itemStatictic)
    client.send_message(message.chat.id, 'Виберіть дію.',reply_markup=_markup_inline)

def SET_CHOISE_REPLY_BUTTONS(message):
    _markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    _itemCode = types.KeyboardButton(text='CLOSE')
    _markup_reply.add(_itemCode)
    client.send_message(message.chat.id,'ewrgbdfscavzXC',reply_markup=_markup_reply)

def SET_START_REPLY_BUTTONS(message):
    _markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    _itemCode = types.KeyboardButton(text='SEND CODE')
    _itemStatictic = types.KeyboardButton(text='MY STATICTIC')
    _itemNewReferal = types.KeyboardButton(text='ADD NEW REFERAL')
    _itemTop = types.KeyboardButton(text='TOP')
    _markup_reply.add(_itemCode, _itemStatictic,_itemNewReferal,_itemTop)
    client.send_message(message.chat.id, 'wqvfebgrdsvcxz',reply_markup=_markup_reply)
_startStatus = False
@client.callback_query_handler(func = lambda call:True)
def ANSWER(call):
    global _startStatus
    if (_startStatus == False):
        return
    if(call.data == '_contineWork'):
        client.send_message(call.message.chat.id, 'eqfsadvxzc')
        SET_START_REPLY_BUTTONS(call.message)
    if (call.data == '_stopWork'):
        client.send_message(call.message.chat.id, 'ewfdasvxzc')
    if (call.data == '_guide'):
        client.send_message(call.message.chat.id, 'wfdscvxzcefqsadvxzC')

@client.message_handler(content_types = ['text'])
def GET_TEXT(message):
    id = message.from_user.id
    # print id
    # REGISTER_NEW_USER(id, message.from_user.first_name, 'pass', '0', '-', 1391548525)
    global _startStatus
    if(CHECK_BLACK_LIST(int(id))):
        client.send_message(message.chat.id, 'wfdscxvzrwgdsf cxzx')
        return
    if (message.text == "erfasdv"):
        _startStatus = True
        client.send_message(message.chat.id, 'erqsadv!\nПrefvdsxі!')
        return

    if(_startStatus == False):
        return
    if(message.text == "ervsdaczx"):
        client.send_message(message.chat.id, 'evfdsa!\nerqfvdsxc.')
        SET_CURRENT_BOT_ANSWER_STATUS(id, 3)
        return
    if (message.text == "vefads"):
        client.send_message(message.chat.id, 'vefads!\nevfsdacx.')
        SET_CURRENT_BOT_ANSWER_STATUS(id, 7)
        return
    if (message.text == "erqsvd"):
        client.send_message(message.chat.id, 'efvasdc!\newfbsdvaxzи.')
        SET_CURRENT_BOT_ANSWER_STATUS(id, 8)
        return
    if (message.text == "efvasd"):
        client.send_message(message.chat.id, 'Виконую.')

        client.send_message(message.chat.id, ''+str(GET_ALL_UNWORKED_USERS()))
        SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
        return
    if (message.text == "efvdsacxz"):
        client.send_message(message.chat.id, 'Виконую.')
        client.send_message(message.chat.id, ''+str(DELETE_ALL_UNWORKED_USERS()))
        SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
        return
    if (message.text == "ervsdzxc"):
        client.send_message(message.chat.id, 'veqfsda!\nrevsdcaxZ.')
        SET_CURRENT_BOT_ANSWER_STATUS(id, 9)
        return
    if (message.text == "ervdscaxz"):
        client.send_message(message.chat.id, 'ebwvfsda!\nvrsdcgwbefasv.')
        SET_CURRENT_BOT_ANSWER_STATUS(id, 10)
        return
    if (message.text == "erfvsdcx"):
        client.send_message(message.chat.id, 'Виконую.')
        client.send_message(message.chat.id, ''+str(GET_ALL_3_DAYS_UNWORKED_USERS()))
        SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
        return
    if (message.text == "rwdsvascxZ"):
        client.send_message(message.chat.id, 'Виконую.')
        client.send_message(message.chat.id, ''+str(GET_PAY_OUT_INFO()))
        SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
        return
    #user_code_num - заробіток за минулий місяць
    #user_mail - невиплачений заробіток за минулий місяць
    if (message.text == "evdsacsZ"):
        client.send_message(message.chat.id, 'Виконую.')
        client.send_message(message.chat.id, '' + str(GET_PAY_OUT_INFO()))
        SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
        return
    if (message.text == "efsvdxcz"):
        client.send_message(message.chat.id, 'esdvascxZ')
        SET_CURRENT_BOT_ANSWER_STATUS(id, 11)
        return
    if (CHECKISREGISTERUSER(id) == False):
        _registerStatus = False
        for i in range(10):
            if(CHECKISREGISTERUSER(id)==False):
                _registerStatus = False
            else:
                _registerStatus = True
                return
        if(_registerStatus == False):
            client.send_message(message.chat.id, 'Ви не зареєстровані.')
            client.send_message(message.chat.id, 'Реєструю Вас.')
            REGISTER_NEW_USER(id, message.from_user.first_name, 'pass', '0', '-', 0)
            client.send_message(message.chat.id, 'Готово!')
            client.send_message(message.chat.id, 'Ваші дані:\nId: ' + str(id) + '\nІмя: ' + str(GET_USER_NAME(id)))
            SET_START_INLINE_BUTTONS(message)


    else:

        if (GET_CURRENT_BOT_ANSWER_STATUS(id) == 4):
            if(message.text == "CLOSE"):
                client.send_message(message.chat.id,'rvsdacxz.',reply_markup=types.ReplyKeyboardRemove())
                SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
                SEND_STANDART_MESSAGE(message)
                return
            try:
                _newReferalID = int(message.text)
            except:
                client.send_message(message.chat.id,'ersvdxzc.',reply_markup=types.ReplyKeyboardRemove())
                SEND_STANDART_MESSAGE(message)
                SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
                return
            SET_NEW_REFERAL(id, int(message.text), message)
            SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
            return
        if (GET_CURRENT_BOT_ANSWER_STATUS(id) == 3):
            try:
                _result = SET_USERS_PROFITS(float(message.text))
                print SET_USERS_PROFITS(float(message.text))
                client.send_message(message.chat.id, 'rwdcasx!\nЦwdsacxz: '+str(_result[0])+'\nrwdsacxz: '+str(_result[1])+'\nwdsvacxzX: '+str(_result[2])+' revdscax ('+str(_result[3])+'%)\nrwdvsacz: '+str(_result[4])+' rewvdsacx ('+str(_result[5])+'%)')
                SEN_NEW_LAST_DATE()
                SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
            except:
                client.send_message(message.chat.id,'rwsvdcaxZ',reply_markup=types.ReplyKeyboardRemove())
            pass
        if (GET_CURRENT_BOT_ANSWER_STATUS(id) == 2):
            if (message.text == "CLOSE"):
                client.send_message(message.chat.id, 'Окей, якщо я Вам буду потрібен - звертайтесь.',reply_markup=types.ReplyKeyboardRemove())
                SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
                SEND_STANDART_MESSAGE(message)
                return
            # print message.text
            if (ADD_NEW_AD_COUNT(message.text, id) == True):
                client.send_message(message.chat.id, ''+str(GET_USER_NAME(int(id)))+'\nrwsdacxzX',reply_markup=types.ReplyKeyboardRemove())
                SEND_STANDART_MESSAGE(message)
            else:
                client.send_message(message.chat.id, 'rwdsaczxervdwscazfwdbsdvc',reply_markup=types.ReplyKeyboardRemove())
                SEND_STANDART_MESSAGE(message)
            SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
            return
        if (GET_CURRENT_BOT_ANSWER_STATUS(id) == 7):
            client.send_message(message.chat.id, 'Виконую.')
            _userName = str(GET_USER_NAME(int(message.text)))
            DELETE_USER_BY_ID(int(message.text))
            client.send_message(message.chat.id, 'rwvdcasz з \nvwdscaz: '+str(message.text)+' \nwvdsacx: '+_userName+'\nwdsacz.')
            #------BLACK LIST-----
            SET_NEW_BLOCK_USER(int(message.text))
            client.send_message(message.chat.id,'wdsaczx з \nID: ' + str(message.text) + '\nweadscz.')
            SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
            SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
            return
        if (GET_CURRENT_BOT_ANSWER_STATUS(id) == 8):
            client.send_message(message.chat.id, 'Виконую.')
            SET_NULL_ALL_PROFIT(int(message.text))
            client.send_message(message.chat.id, 'wdsacxz з \nID: '+str(message.text)+' \nervsdc: '+str(GET_USER_NAME(int(message.text)))+'\nwecasxz.')
            SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
            return
        # ------BLACK LIST-----
        if (GET_CURRENT_BOT_ANSWER_STATUS(id) == 9):
            client.send_message(message.chat.id, 'Виконую.')
            SET_NEW_BLOCK_USER(int(message.text))
            client.send_message(message.chat.id, 'rwdsacz з \nID: '+str(message.text)+'\nдwdsaczX.')
            SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
            return
        if (GET_CURRENT_BOT_ANSWER_STATUS(id) == 10):
            client.send_message(message.chat.id, 'Виконую.')
            DELETE_USER_BY_ID_IN_BLACK_LIST(int(message.text))
            client.send_message(message.chat.id, 'ervdscazз \nID: '+str(message.text)+'\nwdsacz.')
            SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
            return
        if (GET_CURRENT_BOT_ANSWER_STATUS(id) == 11):
            client.send_message(message.chat.id, 'erdsa.')
            SET_USER_DAY_IN_PROJECT(int(message.text))
            SET_USER_NEW_MOUNSE(int(message.text))
            client.send_message(message.chat.id, 'rvesd \nerverv: '+str(message.text)+'\nervdsxcz')
            SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
            return
        if(GET_CURRENT_BOT_ANSWER_STATUS(id)==0):
            if (message.text == 'SEND CODE'):
                client.send_message(message.chat.id,'ervdsac',reply_markup=types.ReplyKeyboardRemove())
                SET_CURRENT_BOT_ANSWER_STATUS(id,2)
                SET_CHOISE_REPLY_BUTTONS(message)
                return
            if (message.text == 'MY STATICTIC'):
                client.send_message(message.chat.id, GET_USER_STAT(id),reply_markup=types.ReplyKeyboardRemove())
                SEND_STANDART_MESSAGE(message)
                return
            if (message.text == 'ADD NEW REFERAL'):
                client.send_message(message.chat.id, 'ervervs',reply_markup=types.ReplyKeyboardRemove())
                SET_CURRENT_BOT_ANSWER_STATUS(id, 4)
                SET_CHOISE_REPLY_BUTTONS(message)
                return
            if (message.text == 'TOP'):
                # client.send_message(message.chat.id, 'ТОП НА РЕМОНТІ',reply_markup=types.ReplyKeyboardRemove())
                _result = GET_INFO_FOR_STATICTIC()
                print _result
                client.send_message(message.chat.id, '--2efew0fs',reply_markup=types.ReplyKeyboardRemove())
                client.send_message(message.chat.id, GET_TOP_5_USERS(),reply_markup=types.ReplyKeyboardRemove())
                client.send_message(message.chat.id, '---------'+str(_result[1])+'\n------'+str(_result[4])+' ewfwef ('+str(_result[5])+'%)'+'\nregerg ewfew grgeger: '+str(_result[2])+' rgregve ('+str(_result[3])+'%)',reply_markup=types.ReplyKeyboardRemove())
                SET_CURRENT_BOT_ANSWER_STATUS(id, 0)
                SEND_STANDART_MESSAGE(message)
                return
            SEND_STANDART_MESSAGE(message)

    # SET_NEW_USER_PASS(1,message.text)
while True:
    client.infinity_polling(none_stop=True,interval=0,timeout=20)

