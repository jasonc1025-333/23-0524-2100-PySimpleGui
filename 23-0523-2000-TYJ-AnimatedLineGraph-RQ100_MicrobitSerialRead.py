###jwc o import PySimpleGUI as sg
###jwc n 'graph_Horizontal_StepSize_Int' is 'str' error: import PySimpleGUIWeb as sg
###jwc o import PySimpleGUI as sg
###jwc yy works with local debugger:  import PySimpleGUI as sg
###jwc 24-1029 yyy import PySimpleGUIWeb as sg
import PySimpleGUIWeb as sg

from random import randint

import serial

rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int = 0

###jwc !!! y  https://www.w3schools.com/python/python_dictionaries_nested.asp
###jwc !!! y  rowData_ArrayList_OfDictionaryPairs_ForAllBots = { 
###jwc !!! y                                                    {},
###jwc !!! y                                                    {},
###jwc !!! y                                                   }

    ###jwc y {'row_id':'.Test_Row', 'bot_id':'Test_Bot', 'mission_status':'-', 'team_id':'-', 'light_lastdelta':100, 'light_total':1000, 'magnet_lastdelta':10000, 'magnet_total':100000},
    ###jwc y {'row_id':'.Test_Row_21', 'bot_id':'Test_Bot_21', 'mission_status':'-', 'team_id':'-', 'light_lastdelta':21, 'light_total':22, 'magnet_lastdelta':23, 'magnet_total':24},
    ###jwc y {'row_id':'.Test_Row_21', 'bot_id':'Test_Bot_21', 'mission_status':'-', 'team_id':'-', 'light_lastdelta':21, 'light_total':22, 'magnet_lastdelta':23, 'magnet_total':24},
    ###jwc y {'row_id':'.Test_Row', 'bot_id':'Test_Bot', 'mission_status':'-', 'team_id':'-', 'light_lastdelta':21, 'light_total':22, 'magnet_lastdelta':23, 'magnet_total':24},
    ###jwc yy {'row_id':'.Test_Row_20', 'bot_id':2, 'mission_status':'-', 'team_id':'-', 'light_lastdelta':21, 'light_total':22, 'magnet_lastdelta':23, 'magnet_total':24},
    ###jwc yy {'row_id':'.Test_Row_10', 'bot_id':1, 'mission_status':'-', 'team_id':'-', 'light_lastdelta':11, 'light_total':12, 'magnet_lastdelta':13, 'magnet_total':14},
    
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy 
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy 
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    ###jwc yy {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':'', 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},

###jwc yy rowData_ArrayList_OfDictionaryPairs_ForAllBots = [
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy 
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy 
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy     {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0},
###jwc yy ]

rowData_ArrayList_OfDictionaryPairs_ForAllBots = {0:{
   'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':'', 'grand_total':'', 'grand_total_old':0,
    }}

scoreboard_DataMessage_Rcvd_Dict = {}

ser = serial.Serial(
        ##jwc o port='/dev/ttyACM0',
        ###jwc y port='/dev/ttyACM1',

        ##jwc o port='COM3',
        ###jwc y port='/dev/ttyAMA0',
        ###jwc port='/dev/ttyACM0',
        port='/dev/ttyACM0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

# Debug Prints
#
###jwc y _debug_Show_Priority_Mi_Bool = True
###jwc y _debug_Show_Priority_Mi_Bool = False
_debug_Show_Priority_Hi_Bool = True
_debug_Show_Priority_Mi_Bool = False
_debug_Show_Priority_Lo_Bool = False

#
# receive_Microbit_Messages_Fn
#
def receive_Microbit_Messages_Fn() -> None:
    global rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int
    global graph_Vertical_Max_Now_Int, graph_Vertical_Divider_Now_Int

    now,network_DataMessage_Rcvd_Bytes,y1,y2 = 0, 0, 0, 0

    ###jwc y rowData_OfDictionaryPairs_ForABot_Empty_Local = {
    ###jwc y ###jwc 23-0504-0710 y 'row_id':'A', 'bot_id':0, 'light_lastdelta':0, 'light_total':0, 'magnet_lastdelta':0, 'magnet_total':0,
    ###jwc y 'row_id':'A', 'bot_id':0, 'mission_status':'-', 'team_id':'-', 'light_lastdelta':0, 'light_total':0, 'magnet_lastdelta':0, 'magnet_total':0,
    ###jwc y }

    network_DataMessage_Rcvd_Bytes = ser.readline()
    if network_DataMessage_Rcvd_Bytes:
        ###jwc o temp, light = network_DataMessage_Rcvd_Bytes.decode().split(':')
        ###jwc 23-0310-1120 y id, te, li, co = network_DataMessage_Rcvd_Bytes.decode().split(',')
        ###jwc n id, te, li, co, m1, m2, m3, m4 = network_DataMessage_Rcvd_Bytes.decode().split('|')
    
        ###jwc o newData = [datestamp,temp,light]
        ###jwc 23-0310-1120 y newData = [datestamp, id, te, li, co]
        ###jwc n newData = [datestamp, id, te, li, co, m1, m2, m3, m4]

        ###jwc o not neeeded: dt = datetime.now()
        ###jwc o not neeeded: datestamp = str(dt)[:16]
        ###jwc o not neeeded: newData = [datestamp, network_DataMessage_Rcvd_Bytes]
        ###jwc o not neeeded: print(newData)
        
        if _debug_Show_Priority_Hi_Bool:
            ###jwc y print("* A: Raw String: ")
            print("* A1:network_DataMessage_Rcvd_Bytes:" + str(network_DataMessage_Rcvd_Bytes) +"|")

        ###jwc o network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Bytes
        network_DataMessage_Rcvd_Str = str(network_DataMessage_Rcvd_Bytes)
        ##jwc workaround for '\r\n' tail
        ##jwc y network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str[0:len(network_DataMessage_Rcvd_Str)-10]
        ###jwc n network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str[0:network_DataMessage_Rcvd_Str.index("\\r\\n")]
        ###jwc n network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str.rstrip("\r\n")
        ###jwc n network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str.strip()
        ###jwc n network_DataMessage_Rcvd_02_Str = network_DataMessage_Rcvd_Str.strip()
        ###jwc n network_DataMessage_Rcvd_02_Str = network_DataMessage_Rcvd_Str.rstrip()
        ###jwc n network_DataMessage_Rcvd_02_Str = network_DataMessage_Rcvd_Str.rstrip("\r\n")
        ###jwc n network_DataMessage_Rcvd_02_Str = network_DataMessage_Rcvd_Str.rstrip("\\r\\n")
        ###jwc n network_DataMessage_Rcvd_02_Str = network_DataMessage_Rcvd_Str.rstrip("\\\r\\\n")
        ###jwc n network_DataMessage_Rcvd_02_Str = network_DataMessage_Rcvd_Str.replace("\r\n","")

        # ':-5' though only 4 length: '\r\n'
        network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str[:-5]
        # Remove trailing spaces from both sides
        network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str.strip()
        # invalid 'network_DataMessage_Rcvd_Str' will be detected here 'ValueError: substring not found' 
        # \ and thus abort and retry w/ new 'network_DataMessage_Rcvd_Str'
        # Filter out preceding "b'" header text
        try:
            network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str[network_DataMessage_Rcvd_Str.index("#"):]
        except ValueError:
            print("!!! 23-0526-2230 'except ValueError' 1:" + str(network_DataMessage_Rcvd_Str) + "|")
            return
        except:
            print("!!! 23-0526-2240 non-'except ValueError' 1:" + str(network_DataMessage_Rcvd_Str) + "|")
            return

        ###jwc o if _debug_Show_Priority_Lo_Bool:
        ###jwc o     ###jwc o print replaced by 'print'
        ###jwc o     print("* A: Raw String: ")
        ###jwc o     ###jwc o print("  A1>" + str(network_DataMessage_Rcvd_Str) +"|")
        ###jwc o     print("  1:" + str(network_DataMessage_Rcvd_Str) +"|")
        if _debug_Show_Priority_Mi_Bool:
            print("  A2:network_DataMessage_Rcvd_Str:" + str(network_DataMessage_Rcvd_Str) +"|")

        ###jwc y if True:
        
        scoreboard_DataNumNew_ArrayList = []
        ###jwc y scoreboard_DataStrNew_ArrayList = network_DataMessage_Rcvd_Str.split("|")
        scoreboard_DataStrNew_ArrayList = network_DataMessage_Rcvd_Str.split(",")

        for key_Value_Pair in scoreboard_DataStrNew_ArrayList:
            ###jwc o key_Value_Pair__Value = key_Value_Pair.substr(key_Value_Pair.index_of(":") + 1, len(key_Value_Pair))
            ###jwc o key_Value_Pair__Value = key_Value_Pair[key_Value_Pair.index_of(":") + 1:len(key_Value_Pair)]
            ## * Skip past "b'" prefix
            ##jwc ? key_Value_Pair__Key = key_Value_Pair[2 : key_Value_Pair.index(":")-1]
            ##jwc n key_Value_Pair__Key = key_Value_Pair[0:key_Value_Pair.index(":")-1]
            key_Value_Pair__Key = key_Value_Pair[key_Value_Pair.index(":")-1 : key_Value_Pair.index(":")]
            ##jwc y key_Value_Pair__Value = key_Value_Pair[key_Value_Pair.index(":") + 1:len(key_Value_Pair)]
            key_Value_Pair__Value = key_Value_Pair[key_Value_Pair.index(":") + 1:len(key_Value_Pair)]
            ##jwc yy scoreboard_DataNumNew_ArrayList.append(int(key_Value_Pair__Value))

            ##jwc n scoreboard_DataNumNew_ArrayList.append({key_Value_Pair__Key:int(key_Value_Pair__Value)})
            
            try:
                ### n scoreboard_DataNumNew_ArrayList['A']=int(key_Value_Pair__Value)
                ### scoreboard_DataNumNew_ArrayList.append(int(key_Value_Pair__Value))
                # Add new 'key_Value_Pair'
                scoreboard_DataMessage_Rcvd_Dict[key_Value_Pair__Key]=int(key_Value_Pair__Value)
            except ValueError:
                scoreboard_DataMessage_Rcvd_Dict[key_Value_Pair__Key]=str(key_Value_Pair__Value)
                print("!!! 23-0519-1200 'except ValueError' 1:" + str(scoreboard_DataMessage_Rcvd_Dict[key_Value_Pair__Key]) + " 2:" + str(key_Value_Pair__Key) + " 3:" + str(key_Value_Pair__Value) + "|")
                return
            except:
                print("!!! 23-0519-1210 non-'except ValueError'")
                return
            
            if _debug_Show_Priority_Lo_Bool:
                print("* B: Parsed Key:key_Value_Pair:")
                print("  1:key_Value_Pair|key_Value_Pair__Key|key_Value_Pair__Value: " + key_Value_Pair +"|"+ key_Value_Pair__Key +"|"+ key_Value_Pair__Value +"|")
                
                ###jwc o print("  2:"+ str((scoreboard_DataNumNew_ArrayList[len(scoreboard_DataNumNew_ArrayList) - 1])) +"|")
                ###jwc o print("  3:"+ str(scoreboard_DataNumNew_ArrayList)
                        
                print("  2:scoreboard_DataMessage_Recvd_Dict: "+ str(scoreboard_DataMessage_Rcvd_Dict) +"|")
                   
        scoreboard_Bot_Found_Bool = False
        if _debug_Show_Priority_Lo_Bool:
            ###jwc y print("* C")
            print("* C1:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots))

        try:
            if scoreboard_DataMessage_Rcvd_Dict['#'] in rowData_ArrayList_OfDictionaryPairs_ForAllBots.keys():
                if _debug_Show_Priority_Mi_Bool:
                    print("  C2:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]))
                    
                scoreboard_Bot_Found_Bool = True    
                
                ###jwc y-obsolete: rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['row_id'] = chr( ord('A') + rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int)
                ###jwc y-obsolete: rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['bot_id'] = scoreboard_DataMessage_Rcvd_Dict['#']
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['light_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['L']
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['light_total'] += scoreboard_DataMessage_Rcvd_Dict['L']
                ###jwc n rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['light_total_old'] = 0
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['magnet_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['M']
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['magnet_total'] += scoreboard_DataMessage_Rcvd_Dict['M']
                # Add 'Light Sensor' and Subtract 'Magnet Sensor'
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['grand_total_old'] = rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['grand_total']
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['grand_total'] += scoreboard_DataMessage_Rcvd_Dict['L'] - scoreboard_DataMessage_Rcvd_Dict['M']


                ###jwc y switch to 'grand_total': if  bot_dictionary['light_total'] > graph_Vertical_Max_Now_Int:
                if  rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['grand_total'] >= graph_Vertical_Max_Now_Int:
                    graph_Vertical_Max_Now_Int *= graph_Vertical_MULTIPLIER_INT
                    graph_Vertical_Divider_Now_Int *= graph_Vertical_MULTIPLIER_INT

                if  rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['grand_total'] <= -graph_Vertical_Max_Now_Int:
                    graph_Vertical_Max_Now_Int *= graph_Vertical_MULTIPLIER_INT
                    graph_Vertical_Divider_Now_Int *= graph_Vertical_MULTIPLIER_INT

                if _debug_Show_Priority_Hi_Bool:
                    ###JWC Y print("  C3:rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]: " + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]))
                    ###JWC Y print("  C3:rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]: " + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]))
                    print("  C3:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]))
            else:
                # Create Emtpy Version to be Initialized
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']] = {}
                if _debug_Show_Priority_Mi_Bool:
                    print("* D1:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]))
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['row_id'] = chr( ord('A') + rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int)
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['bot_id'] = scoreboard_DataMessage_Rcvd_Dict['#']
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['light_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['L']
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['light_total'] = scoreboard_DataMessage_Rcvd_Dict['L']
                ###jwc n rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['light_total_old'] = 0
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['magnet_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['M']
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['magnet_total'] = scoreboard_DataMessage_Rcvd_Dict['M']
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['grand_total_old'] = 0
                # Add 'Light Sensor' and Subtract 'Magnet Sensor'
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['grand_total'] = scoreboard_DataMessage_Rcvd_Dict['L'] - scoreboard_DataMessage_Rcvd_Dict['M']

                rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]['wrap_around_bool'] = False
    
                ###jwc n history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[scoreboard_DataMessage_Rcvd_Dict['#']] = {'history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key': Queue()}
                history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[scoreboard_DataMessage_Rcvd_Dict['#']] = {
                    'history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key': Queue(), 
                    'history_OfDrawLines_LightLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue(),
                    'history_OfDrawLines_MagnetLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue(),
                    }
                history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[scoreboard_DataMessage_Rcvd_Dict['#']] = {
                    'history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key': Queue(),
                    }

                history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[scoreboard_DataMessage_Rcvd_Dict['#']] = {
                    'history_OfDrawTexts_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key': Queue(),
                    'history_OfDrawRectangles_LightLastDelta_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue(),
                    'history_OfDrawRectangles_MagnetLastDelta_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue(),
                    }
                
                if _debug_Show_Priority_Hi_Bool:
                    ###jwc y print("  D2:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]))
                    print("  D2:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots[scoreboard_DataMessage_Rcvd_Dict['#']]))
                ####jwc n rowData_ArrayList_OfDictionaryPairs_ForAllBots.sort(key=lambda x_Now: x_Now.get('bot_id'))
                ###jwc n rowData_ArrayList_OfDictionaryPairs_ForAllBots.sort(key=lambda x_Now: x_Now.get('row_id'))
                ###jwc y rowData_ArrayList_OfDictionaryPairs_ForAllBots.sort(key=get_bot_id_fn)
                ###jwc y if _debug_Show_Priority_Mi_Bool:
                ###jwc y     print("  D1c:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots))

                rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int += 1
        except:
            print("!!! ERROR 23-0608-1440: scoreboard_DataMessage_Rcvd_Dict['#']" + scoreboard_DataMessage_Rcvd_Dict['#'])

    else:
        ###jwc y print("*** No Serial Read *** ")
        print("*** NO SERIAL READ *** ")

#
# pySimpleGui
#

from queue import Queue

###jwc y graph_Vertical_MAX_INT = 300
graph_Vertical_MAX_INT = 600
###jwc y graph_Horizontal_MAX_INT = 1000
graph_Horizontal_MAX_INT = 1200

###jwc y graph_Vertical_Max_Now_Int = graph_Vertical_MAX_INT
# Divide Vertical by Half (2) to Allow Pos & Neg Vertical Axis
graph_Vertical_Max_Now_Int = int(graph_Vertical_MAX_INT/2)
graph_Horizontal_Max_Now_Int = graph_Horizontal_MAX_INT

graph_Vertical_Divider_Now_Int = 1
graph_Vertical_MULTIPLIER_INT = 2

###jwc o GRAPH_SIZE = (400,200)
###jwc y GRAPH_SIZE = (400,400)
###jwc n too tall GRAPH_SIZE = (400,20000)
###jwc n GRAPH_SIZE = (500,500)
###jwc y GRAPH_SIZE = (600,graph_Vertical_Max_Now_Int)
###jwc y GRAPH_SIZE = (1000,graph_Vertical_Max_Now_Int)
GRAPH_SIZE = (graph_Horizontal_MAX_INT, graph_Vertical_MAX_INT)

###jwc y graph_Horizontal_StepSize_Int = 5
###jwc y graph_Horizontal_StepSize_Int = 15
###jwc y a little too fast: graph_Horizontal_StepSize_Int = 30
###jwc y round-up to 10s: graph_Horizontal_StepSize_Int = 15
graph_Horizontal_StepSize_Int = 20

graph_Horizontal_MsecPerSample_Int = 15

###jwc y graph_BotSensorDetail_PIxelHigh_Int = 40
###jwc y graph_BotSensorDetail_PIxelHigh_Int = 60
###jwc y graph_BotSensorDetail_PIxelHigh_Int = 100
graph_BotSensorDetail_PIxelHigh_Int = 75

# Light Approx. Max 250 / Graph Width Max = 250 = Divider 1
graph_BotSensorDetail_Light_FitHorizontalMax_Divider = 1
# Magnet Approx. Max 1000 / Graph Width Max = 250 = Divider 4
graph_BotSensorDetail_Magnet_FitHorizontalMax_Divider = 4


sg.change_look_and_feel('LightGreen')

###jwc ? history_OfDrawLines_List_Of_Objects = Queue()
###jwc ? history_OfDrawLine_Object = None

###jwc y? history_OfDrawLines_Queue_ABot_1D = Queue()
###hwc y?n history_OfDrawLines_Queue_ABot_1D = {1:{'Queue': Queue()}}


###jwc 23-0527-1320 y5? history_OfDrawLines_Queue_ABot_1D = {1:Queue()}
###jwc y? history_OfDrawLines_Queues_ManyBots_2D = {1:{'DrawLine_Figure_Object':None}}
###jwc y? history_OfDrawLines_Queues_ManyBots_2D = {1:{'DrawLine_Figure_Object_Queue':None}}
###jwc yy? history_OfDrawLines_Queues_ManyBots_2D = {1:None}

###jwc y4? history_OfDrawLines_Queues_ManyBots_2D = {1:{'DrawLine_Figure_Object_Queue':Queue()}}
###jwc 23-0527-1320 y5? history_OfDrawLines_Queues_ManyBots_2D = {1:Queue()}

###jwc 23-0527-1320 y5? history_OfDrawLines_Queues_ManyBots_2D = {1:{'DrawLine_Figure_Object_Queue':None}}

history_OfDrawLines_PerBot_AsFigureObject = None
history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue = Queue()
###jwc y history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList = {1:{'history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':None}}
###jwc y istory_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList = {1:{
###jwc y    'history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue(), 
###jwc y    'history_OfDrawLines_LightLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue(),
###jwc y    'history_OfDrawLines_MagnetLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue()
###jwc y    }}
history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList = {0:{
    'history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue(), 
    'history_OfDrawLines_LightLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue(),
    'history_OfDrawLines_MagnetLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue(),
    }}

history_OfDrawTexts_PerBot_AsFigureObject = None
history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue = Queue()
###jwc y history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList = {1:{'history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':None}}
###jwc y history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList = {1:{'history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue()}}
history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList = {0:{
   'history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue(),
    }}

history_OfDraws_Col02_PerBot_AsFigureObject = None
history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue = Queue()
history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList = {0:{
    'history_OfDrawTexts_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key': Queue(),
    'history_OfDrawRectangles_LightLastDelta_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue(),
    'history_OfDrawRectangles_MagnetLastDelta_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue(),
    }}

###jwc o total_Layout = [  
column_01_Layout = [  
    [sg.Text('Bot Sensor: Summary', justification='center', size=(40,1))],
    ###jwc y [sg.Graph(GRAPH_SIZE, (0,0), GRAPH_SIZE, key='_keyIs_BotSensor_Summary__Graph_', background_color='lightblue')],
    ###jwc y [sg.Graph(GRAPH_SIZE, (0,0), GRAPH_SIZE, key='_keyIs_BotSensor_Summary__Graph_', background_color='lightblue'), sg.Slider((0,30), default_value=15, orientation='h', key='-DELAY2-')],
    
    ###jwc y [sg.Graph(canvas_size=GRAPH_SIZE, graph_bottom_left=(0,-graph_Vertical_MAX_INT/2), graph_top_right=(graph_Horizontal_MAX_INT,graph_Vertical_MAX_INT/2), key='_keyIs_BotSensor_Summary__Graph_', background_color='lightblue'), sg.Slider((0,30), default_value=15, orientation='h', key='-DELAY2-')],
    [sg.Graph(canvas_size=GRAPH_SIZE, graph_bottom_left=(0,-graph_Vertical_Max_Now_Int), graph_top_right=(graph_Horizontal_Max_Now_Int,graph_Vertical_Max_Now_Int), key='_keyIs_BotSensor_Summary__Graph_', background_color='lightblue')],
    [sg.Button('Reset', size=(7,1)), sg.Text('graph_Vertical_Max_Now_Int:'), sg.Text(key='_keyIs_Graph_Vertical_Max_Now_Int_'), sg.Text('graph_Vertical_Divider_Now_Int:'), sg.Text(key='_keyIs_Graph_Vertical_Divider_Now_Int_')],
    ###jwc y [sg.Text('Milliseconds per sample:', size=(20,1)), sg.Text('____', key='_keyIs_MsecPerSample_'), sg.Slider((0,30), default_value=15, orientation='h', key='_keyIs_Graph_Horizontal_MsecPerSample_Int_'), sg.Text('Pixels per sample:', size=(20,1)), sg.Text('____', key='_keyIs_PixelPerSample_'), sg.Slider((0,30), default_value=graph_Horizontal_StepSize_Int, orientation='h', key='_keyIs_Graph_Horizontal_StepSize_Int_')],
    ###jwc y [sg.Text('Milliseconds per sample:', size=(20,1)), sg.Text('____', key='_keyIs_MsecPerSample_'), sg.Slider((0,30), default_value=15, orientation='h', key='_keyIs_Graph_Horizontal_MsecPerSample_Int_'), sg.Text('Pixels per sample:', size=(20,1)), sg.Text('____', key='_keyIs_PixelPerSample_'), sg.Slider((0,60), default_value=graph_Horizontal_StepSize_Int, orientation='h', key='_keyIs_Graph_Horizontal_StepSize_Int_')],
    [sg.Text('mSec per sample:', size=(20,1)), sg.Text('____', key='_keyIs_MsecPerSample_'), sg.Slider((0,30), default_value=graph_Horizontal_MsecPerSample_Int, orientation='h', key='_keyIs_Graph_Horizontal_MsecPerSample_Int_'), sg.Text('Pixels per sample:', size=(20,1)), sg.Text('____', key='_keyIs_PixelPerSample_'), sg.Slider((0,60), default_value=graph_Horizontal_StepSize_Int, orientation='h', key='_keyIs_Graph_Horizontal_StepSize_Int_')],
    ###jwc o  sg.Slider((1,30), default_value=graph_Horizontal_StepSize_Int, orientation='h', key='_keyIs_Graph_Horizontal_StepSize_Int_')],
    [sg.Button('Exit', size=(7,1))],
    ]

    ###jwc y [sg.Text('Battery Charge Levels', justification='center', size=(40,1))],
    ###jwc y [sg.Graph((200,400), (0,0), (200, 400), background_color='lightblue', key='-CHARGE-')],
column_02_Layout = [
    [sg.Text('Bot Sensor: Details', justification='center', size=(40,1))],
    ###jwc y [sg.Graph((200,400), (0,0), (200, 400), background_color='lightblue', key='_keyIs_BotSensor_Details__Graph_')],
    [sg.Graph((250,600), (0,0), (250, 600), background_color='lightblue', key='_keyIs_BotSensor_Details__Graph_')],
    ]

total_Layout = [
    [sg.Text('RQ100 Scoreboard Server & Diagnostic Dashboard', justification='center', size=(80,1))],
    [sg.Column( column_01_Layout, element_justification='center'), sg.Column(column_02_Layout, element_justification='center')],
    ###jwc y [sg.Button('Exit')]  
    ]


###jwc y total_Window = sg.Window('Animated Line Graph Example', total_Layout)
###jwc y total_Window = sg.Window('Animated Line Graph Example', total_Layout, web_port=5000)
# 'finalize=true': Force complete initialization of total_Window for immediate edits (w/o 'Read' call)
# 'web_port=5000' :)+
###jwc yy total_Window = sg.Window('Animated Line Graph Example', total_Layout, finalize=True, web_port=5000)
###jwc yy total_Window = sg.Window('Animated Line Graph Example', total_Layout, finalize=True)
###jwc y total_Window = sg.Window('Animated Line Graph Example', total_Layout, finalize=True, web_port=5000)
###jwc y total_Window = sg.Window('Animated Line Graph Example', total_Layout, finalize=True, web_port=5000, web_update_interval=0.00001)
# !!! 'web_update_interval=0.00001' appears worst update slows to 10s (vs 4s)
total_Window = sg.Window('RQ100 Scoreboard Server & Diagnostic Dashboard', total_Layout, finalize=True, web_port=5000)

sub_Window__keyIs_BotSensor_Summary__Graph_ = total_Window["_keyIs_BotSensor_Summary__Graph_"]  # type: sg.Graph

###jwc y graph_Horizontal_MsecPerSample_Int = x_Now = x_Old = lasty = 0
border_Perimeter_MARGIN_INT = 20
x_Now = x_Old = border_Perimeter_MARGIN_INT

#
# !!! For PySimpleGuiWeb: 'move_figure' & 'relocate_figure' are not robust, so use 'delete_figure' and 'draw_line' instead
#

# Horizontal 'Zero' Line
###jwc n sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((0,0), (graph_Horizontal_Max_Now_Int,0), color='white', width=1, key='-HorizontalNowLine-')   
horizontalZeroLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((0,0), (graph_Horizontal_Max_Now_Int,0), color='white', width=1)   

###jwc y verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((x_Now,-graph_Vertical_Max_Now_Int), (x_Now, graph_Vertical_Max_Now_Int), color='white', width=1)
###jwc y verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((border_Perimeter_MARGIN_INT,-graph_Vertical_Max_Now_Int), (border_Perimeter_MARGIN_INT, graph_Vertical_Max_Now_Int), color='white', width=1)
###jwc n verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((x_Now,-graph_Vertical_Max_Now_Int), (x_Now, graph_Vertical_Max_Now_Int), color='white', width=1)

###jwc n verticalNowPoint_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.draw_point((x_Now,0), color='red', size=5)

verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((x_Now,-graph_Vertical_Max_Now_Int), (x_Now, graph_Vertical_Max_Now_Int), color='white', width=1)

wrapAround_ForThisMainWhileLoop_Bool = False

# Vertical 'Now' Line
###jwc n verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((x_Now,-graph_Vertical_Max_Now_Int), (x_Now, graph_Vertical_Max_Now_Int), color='white', width=1, key='-verticalZeroLine-')
###jwc n verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((x_Now,-graph_Vertical_Max_Now_Int), (x_Now, graph_Vertical_Max_Now_Int), color='white', width=1)
###jwc n verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((10,100), (10,-100), color='white', width=1)
###jwc n2 verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((x_Now,-graph_Vertical_Max_Now_Int), (x_Now, graph_Vertical_Max_Now_Int), color='white', width=1)

###jwc y lastX1 = lastY1 = 0

#
# PySimpleGUI Debugger
#
###jwc ? TODO sg.show_debugger_window(location=(10,10))
###jwc n sg.show_debugger_window(location=(10,10))
# !!! Important: 'show_debugger_window' not work with PySimpleGUIWeb, but w/ PySimpleGUI
# jwc yy sg.show_debugger_window(location=(10,10))

while True:                             # Event Loop

    receive_Microbit_Messages_Fn()

    #
    # !!! 'total_Window.read' must precede all 'total_Window[]' calls
    #
    event, values = total_Window.read(timeout=graph_Horizontal_MsecPerSample_Int)
    if event in [None, 'Exit']:
        break
    
    if event in ['Reset']:
        for rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int in rowData_ArrayList_OfDictionaryPairs_ForAllBots.keys():
            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['light_lastdelta'] = 0
            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['light_total'] = 0
            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['magnet_lastdelta'] = 0
            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['magnet_total'] = 0
            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['grand_total'] = 0
            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['grand_total_old'] = 0
        # Divide Vertical by Half (2) to Allow Pos & Neg Vertical Axis
        graph_Vertical_Max_Now_Int = int(graph_Vertical_MAX_INT/2)
        graph_Vertical_Divider_Now_Int = 1

    #
    # 1st Column Window: Bot Sensor Summary
    #
    total_Window['_keyIs_Graph_Vertical_Max_Now_Int_'].update(graph_Vertical_Max_Now_Int)
    total_Window['_keyIs_Graph_Vertical_Divider_Now_Int_'].update(graph_Vertical_Divider_Now_Int)

    ###jwc o for web, convert text to int: graph_Horizontal_StepSize_Int, graph_Horizontal_MsecPerSample_Int = values['_keyIs_Graph_Horizontal_StepSize_Int_'], values['_keyIs_Graph_Horizontal_MsecPerSample_Int_']
    graph_Horizontal_StepSize_Int, graph_Horizontal_MsecPerSample_Int = int(values['_keyIs_Graph_Horizontal_StepSize_Int_']), int(values['_keyIs_Graph_Horizontal_MsecPerSample_Int_'])
    
    total_Window['_keyIs_MsecPerSample_'].update(graph_Horizontal_MsecPerSample_Int)
    total_Window['_keyIs_PixelPerSample_'].update(graph_Horizontal_StepSize_Int)
    
    values['_keyIs_Graph_Vertical_Divider_Now_Int_'] = graph_Vertical_Divider_Now_Int

    
    ###jwc y not needed anymore: y = randint(0,GRAPH_SIZE[1])        # get random point for graph
    ###jwc y but need to shift sooner: if x_Now < GRAPH_SIZE[0]:               # if still drawing initial width of graph

    ###jwc n1 verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((x_Now,-graph_Vertical_Max_Now_Int), (x_Now, graph_Vertical_Max_Now_Int), color='white', width=1)
    ###jwc y? verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((x_Now,-graph_Vertical_Max_Now_Int), (x_Now, graph_Vertical_Max_Now_Int), color='white', width=1)
    
    wrapAround_ForThisMainWhileLoop_Bool = False
    
    ###jwc y if x_Now > (GRAPH_SIZE[0]-20):
    ###jwc if x_Now > (GRAPH_SIZE[0]-border_Perimeter_MARGIN_INT):
    # !!! '>=' for earliest detection, since so near boundary
    if x_Now >= (graph_Horizontal_Max_Now_Int-border_Perimeter_MARGIN_INT):
        ###jwc y x_Now, x_Old = 0, 0
        ###jwc y x_Now, x_Old = 0+20, 0+20
        x_Now = x_Old = 0 + border_Perimeter_MARGIN_INT
        ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].erase()
        ###jwc y sub_Window__keyIs_BotSensor_Summary__Graph_.relocate_figure(verticalNowLine_FigureObject,20,0)
        ### jwc y sub_Window__keyIs_BotSensor_Summary__Graph_.relocate_figure(verticalNowLine_FigureObject,-graph_Horizontal_Max_Now_Int+border_Perimeter_MARGIN_INT,0)
        # !!! 'relocate_figure': relative offset position
        ###jwc n sub_Window__keyIs_BotSensor_Summary__Graph_.relocate_figure(verticalNowLine_FigureObject,-graph_Horizontal_Max_Now_Int+border_Perimeter_MARGIN_INT,0)
        # !!! Important: Absolute Positioning
        ###jwc y TYJ does work but not intuitive for here? sub_Window__keyIs_BotSensor_Summary__Graph_.relocate_figure(verticalNowLine_FigureObject,border_Perimeter_MARGIN_INT,0)
        # !!! Important: Relative Positioning
        # !!!' relocate_figure': relative offset position
        # !!! jwc yyy for non-web (coordinates normal): sub_Window__keyIs_BotSensor_Summary__Graph_.move_figure(verticalNowLine_FigureObject,-(graph_Horizontal_Max_Now_Int-(border_Perimeter_MARGIN_INT*2),0))
        # !!! jwc yyy for web (coordinates reversed):
        ###jwc n sub_Window__keyIs_BotSensor_Summary__Graph_.move_figure(verticalNowLine_FigureObject,+(graph_Horizontal_Max_Now_Int-(border_Perimeter_MARGIN_INT*2),0))
        ###jwc n sub_Window__keyIs_BotSensor_Summary__Graph_.move_figure(verticalNowLine_FigureObject,(graph_Horizontal_Max_Now_Int-(border_Perimeter_MARGIN_INT*2)),0)
        ###jwc n need background_color: sub_Window__keyIs_BotSensor_Summary__Graph_.update()
        
        ### #jwc y AAA sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(verticalNowLine_FigureObject) 
        ### #jwc y AAA verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((x_Now,-graph_Vertical_Max_Now_Int), (x_Now, graph_Vertical_Max_Now_Int), color='white', width=1)

        ###jwc AttributeError: 'SvgLine' object has no attribute 'set_position': sub_Window__keyIs_BotSensor_Summary__Graph_.relocate_figure(verticalNowLine_FigureObject, x_Now, 0)
        
        ###jwc yy sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(verticalNowLine_FigureObject) 
        ###jwc yy verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((x_Now,-graph_Vertical_Max_Now_Int), (x_Now, graph_Vertical_Max_Now_Int), color='white', width=1)
        wrapAround_ForThisMainWhileLoop_Bool = True
    ###jwc yy else:
        # !!! Important: Relative Positioning
        # !!!' relocate_figure': relative offset position
        # !!! jwc yyy for non-web (coordinates normal): sub_Window__keyIs_BotSensor_Summary__Graph_.move_figure(verticalNowLine_FigureObject,graph_Horizontal_StepSize_Int,0)
        # !!! jwc yyy for web (coordinates reversed):
        ###jwc y? bug workaround, go down also?: sub_Window__keyIs_BotSensor_Summary__Graph_.move_figure(verticalNowLine_FigureObject,-graph_Horizontal_StepSize_Int,0)
        ###jwc n sub_Window__keyIs_BotSensor_Summary__Graph_.move_figure(verticalNowLine_FigureObject,-graph_Horizontal_StepSize_Int,-graph_Horizontal_StepSize_Int)
        ###jwc Web: 'sub_Window__keyIs_BotSensor_Summary__Graph_.relocate_figure(verticalNowLine_FigureObject,20,20)' 'AttributeError: 'SvgLine' object has no attribute 'set_position'',
        ###jwc web: 'sub_Window__keyIs_BotSensor_Summary__Graph_.move_figure(verticalNowLine_FigureObject,-graph_Horizontal_StepSize_Int,graph_Horizontal_StepSize_Int)' not reliable either.  Just redraw line.
        ###jwc n sub_Window__keyIs_BotSensor_Summary__Graph_.move_figure(verticalNowLine_FigureObject,-graph_Horizontal_StepSize_Int,graph_Horizontal_StepSize_Int)
        ###jwc n need background_color: sub_Window__keyIs_BotSensor_Summary__Graph_.update()

        ###jwc n sub_Window__keyIs_BotSensor_Summary__Graph_.move_figure(verticalNowPoint_FigureObject, -graph_Horizontal_StepSize_Int, 0)  

        ###jwc y? good start: sub_Window__keyIs_BotSensor_Summary__Graph_.draw_line((x_Now-graph_Horizontal_StepSize_Int,0), (x_Now,0), color='grey', width=1)
        ### #jwc y AAA sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(verticalNowLine_FigureObject) 
        ### #jwc y AAA verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((x_Now,-graph_Vertical_Max_Now_Int), (x_Now, graph_Vertical_Max_Now_Int), color='white', width=1)

        ###jwc AttributeError: 'SvgLine' object has no attribute 'set_position': sub_Window__keyIs_BotSensor_Summary__Graph_.relocate_figure(verticalNowLine_FigureObject, x_Now, 0)

        ###jwc yy sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(verticalNowLine_FigureObject) 
        ###jwc yy verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((x_Now,-graph_Vertical_Max_Now_Int), (x_Now, graph_Vertical_Max_Now_Int), color='white', width=1)

    sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(verticalNowLine_FigureObject) 
    verticalNowLine_FigureObject = sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((x_Now,-graph_Vertical_Max_Now_Int), (x_Now, graph_Vertical_Max_Now_Int), color='white', width=1)

    ###jwc yy # Horizontal 'Zero' Line
    ###jwc yy ###jwc n sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((0,0), (graph_Horizontal_Max_Now_Int,0), color='white', width=1, key='-HorizontalNowLine-')   
    ###jwc yy sub_Window__keyIs_BotSensor_Summary__Graph_.DrawLine((0,0), (graph_Horizontal_Max_Now_Int,0), color='white', width=1)   

    
    ###jwc y for rowData_ForOneBot in rowData_ArrayList_OfDictionaryPairs_ForAllBots:
    for rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int in rowData_ArrayList_OfDictionaryPairs_ForAllBots.keys():
        
        ###jwc y if rowData_ForOneBot_BotLabel != '':
        # Skip Test Bot_Id = 0
        if rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int != 0:
            
            ###jwc y rowData_ForOneBot_BotLabel = str(rowData_ForOneBot['bot_id']) +':'+ str(rowData_ForOneBot['light_lastdelta']) +':'+ str(rowData_ForOneBot['light_total'])
            ###jwc y rowData_ForOneBot_BotLabel = str(rowData_ForOneBot['bot_id'])
            rowData_ForOneBot_BotLabel = str(rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int)

            # Clear Oldest Existing DrawLines/DrawTexts if 'wrapAround_ForThisMainWhileLoop_Bool=True', so need to remove residue grpahics to re-use graph
            #
            if wrapAround_ForThisMainWhileLoop_Bool:
                rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['wrap_around_bool'] = True

            if rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['wrap_around_bool']:
                
                ###jwc 23-0527-1320 y5? sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']]['Queue'].get())

                history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
                # 'try, except' not work
                # Need following min_check, since a fatal silent error, will freeze program
                # 'not history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue.empty()' could work but could be obsolete
                if(history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.qsize()>0):
                    sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.get(history_OfDrawLines_PerBot_AsFigureObject))
                    
                history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
                # Need following min_check, since a fatal silent error, will freeze program
                # 'not history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue.empty()' could work but could be obsolete
                if(history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue.qsize()>0):
                    sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue.get(history_OfDrawTexts_PerBot_AsFigureObject))
                ###jwc seems not needed y: history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key'] = history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue
        
                history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['history_OfDrawLines_LightLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
                # Need following min_check, since a fatal silent error, will freeze program
                # 'not history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue.empty()' could work but could be obsolete
                if(history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.qsize()>0):
                    sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.get(history_OfDrawLines_PerBot_AsFigureObject))

                history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['history_OfDrawLines_MagnetLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
                # Need following min_check, since a fatal silent error, will freeze program
                # 'not history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue.empty()' could work but could be obsolete
                if(history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.qsize()>0):
                    sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.get(history_OfDrawLines_PerBot_AsFigureObject))

            ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((lastX1, rowData_ForOneBot['light_total_old']), 
            ###jwc y rowData_ForOneBot_Y_Now = int( rowData_ForOneBot['light_total'] / graph_Vertical_Divider_Now_Int )
            ###jwc y rowData_ForOneBot_Y_Old = int( rowData_ForOneBot['light_total_old'] / graph_Vertical_Divider_Now_Int )

            
            rowData_ForOneBot_Y_Now = int( rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['grand_total'] / graph_Vertical_Divider_Now_Int )
            rowData_ForOneBot_Y_Old = int( rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['grand_total_old'] / graph_Vertical_Divider_Now_Int )
            
            rowData_ForOneBot_Y_LightLastDelta_Now = rowData_ForOneBot_Y_Now + int( rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['light_lastdelta'] / graph_Vertical_Divider_Now_Int )
            rowData_ForOneBot_Y_MagnetLastDelta_Now = rowData_ForOneBot_Y_Now - int( rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['magnet_lastdelta'] / graph_Vertical_Divider_Now_Int )

            #
            # Draw for Current Bot This New Graphic: 'rowData_ForOneBot_Y_Now'
            history_OfDrawLines_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine(
                                                                                    (x_Old, rowData_ForOneBot_Y_Old), 
                                                                                    (x_Now, rowData_ForOneBot_Y_Now), 
                                                                                    color='blue', 
                                                                                    width=1)
            # Archive Above New Graphic for Removal Next Round: Part 1of2
            history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
            # Archive Above New Graphic for Removal Next Round: Part 2of2
            history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.put(history_OfDrawLines_PerBot_AsFigureObject)
            
            #
            # Draw for Current Bot This New Graphic: 'rowData_ForOneBot_Y_LightLastDelta_Now'
            history_OfDrawLines_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine(
                                                                                    ###jwc n could make sesne, but gap with x: (x_Old, rowData_ForOneBot_Y_Now), 
                                                                                    ###jwc n could make sesne, but gap with x: (x_Old, rowData_ForOneBot_Y_LightLastDelta_Now), 
                                                                                    (x_Now, rowData_ForOneBot_Y_Now), 
                                                                                    (x_Now, rowData_ForOneBot_Y_LightLastDelta_Now), 
                                                                                    color='red', 
                                                                                    width=1)
            # Archive Above New Graphic for Removal Next Round: Part 1of2
            history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['history_OfDrawLines_LightLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
            # Archive Above New Graphic for Removal Next Round: Part 2of2
            history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.put(history_OfDrawLines_PerBot_AsFigureObject)

            #
            # Draw for Current Bot This New Graphic: 'rowData_ForOneBot_Y_MagnetLastDelta_Now'
            history_OfDrawLines_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine(
                                                                                    ###jwc n could make sesne, but gap with x: (x_Old, rowData_ForOneBot_Y_Now), 
                                                                                    ###jwc n could make sesne, but gap with x: (x_Old, rowData_ForOneBot_Y_MagnetLastDelta_Now), 
                                                                                    (x_Now, rowData_ForOneBot_Y_Now), 
                                                                                    (x_Now, rowData_ForOneBot_Y_MagnetLastDelta_Now), 
                                                                                    color='green', 
                                                                                    width=1)
            # Archive Above New Graphic for Removal Next Round: Part 1of2
            history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['history_OfDrawLines_MagnetLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
            # Archive Above New Graphic for Removal Next Round: Part 2of2
            history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.put(history_OfDrawLines_PerBot_AsFigureObject)

            #
            # Draw for Current Bot This New Graphic: 'DrawText(text=rowData_ForOneBot_BotLabel'
            ###jwc yy FontSize Seems to Work Only in Non-Web-Only: total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4)))
            ###jwc 23-0527-1320 y5? history_OfDrawTexts_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4))
            ###jwc y3? history_OfDrawLines_Queue_ABot_1D[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int].put(history_OfDrawTexts_PerBot_AsFigureObject)
            ###jwc y4? history_OfDrawLines_Queues_ManyBots_2D[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['DrawLine_Figure_Object_Queue'].put(history_OfDrawTexts_PerBot_AsFigureObject)
            ###jwc 23-0527-1320 y5? history_OfDrawLines_Queues_ManyBots_2D[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int].put(history_OfDrawTexts_PerBot_AsFigureObject)
            ###jwc y history_OfDrawTexts_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4))
            ###
            ###jwc ym Web is limited: no font nor color: history_OfDrawTexts_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font='Arial 3', color='red')
            history_OfDrawTexts_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(
                                                                                    text=rowData_ForOneBot_BotLabel, 
                                                                                    location=(x_Now-5, rowData_ForOneBot_Y_Now+5))
            # Archive Above New Graphic for Removal Next Round: Part 1of2
            history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int]['history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
            # Archive Above New Graphic for Removal Next Round: Part 2of2
            history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue.put(history_OfDrawTexts_PerBot_AsFigureObject)
                            
    ###jwc y not need y anymore: x_Old, lasty = x_Now, y
    x_Old = x_Now
    
    ###jwc y lastX1, lastY1 = x_Now, rowData_ArrayList_OfDictionaryPairs_ForAllBots[0]['light_total']

    ###jwc ? 'str' x_Now += graph_Horizontal_StepSize_Int
    ###jwc y x_Now += int(graph_Horizontal_StepSize_Int)
    x_Now += graph_Horizontal_StepSize_Int

    #
    # 2nd Column Window: Bot Sensor Details
    #

    # Erase at beginning for less flicker
    ###jwc ym but causes flicer: total_Window['_keyIs_BotSensor_Details__Graph_'].erase()

    ###jwc ? for rowData_ArrayList_OfDictionaryPairs_ForAllBots__ValuesOfDictionPairs_ForOneBot in rowData_ArrayList_OfDictionaryPairs_ForAllBots.values():
    for i, rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values in enumerate(rowData_ArrayList_OfDictionaryPairs_ForAllBots.values()):

        # Skip Test Bot_Id = 0
        ###jwc n if rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['bot_id'] != 0:
        if (rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['bot_id'] != '') and (rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['bot_id'] > 0):
          
            if _debug_Show_Priority_Mi_Bool:
                print(
                    "* E",
                    i, 
                    str(rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['light_lastdelta']),
                    str(rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['magnet_lastdelta']),
                    )
            
                ###jwc yn location=(0, i*2)
                ###jwc yyn location=(0, i*4)
                ###jwc y location=(0, i*50)
                ###jwc ? location=(-100, i*10)
                
            #
            # Archive Above New Graphic for Removal Next Round: Part 1of2
            history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['bot_id']]['history_OfDrawTexts_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
            # Need following min_check, since a fatal silent error, will freeze program
            # 'not history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue.empty()' could work but could be obsolete
            if(history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue.qsize()>0):
                total_Window['_keyIs_BotSensor_Details__Graph_'].delete_figure(history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue.get(history_OfDraws_Col02_PerBot_AsFigureObject))
            ###jwc ? history_OfDraws_Col02_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Details__Graph_'].DrawText(
            history_OfDraws_Col02_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Details__Graph_'].draw_text(
                ###jwc yn text=str(i) +':'+ str(rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['light_lastdelta']), 
                ###jwc y text=f"{i}: {rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['bot_id']}: {rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['light_lastdelta']}: {rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['magnet_lastdelta']}", 
                ###jwc yy text=f"{i} #:{rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['bot_id']} L:{rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['light_lastdelta']} M:{rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['magnet_lastdelta']}", 
                ###jwc yyy text=f"{i} #:{rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['bot_id']} -L:{rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['light_lastdelta']} +M:{rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['magnet_lastdelta']} =T:{-1*rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['grand_total']}", 
                text=f"{rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['row_id']} #:{rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['bot_id']} -L:{rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['light_lastdelta']} +M:{rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['magnet_lastdelta']} =T:{-1*rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['grand_total']}", 
                ####jwc n will not print outside graph: location=(250, i*10)
                ###jwc n location=(0, i*20+20)
                ###jwc n location=(0, i*20+20)
                location=(0, i*graph_BotSensorDetail_PIxelHigh_Int+20)
                )
            # Archive Above New Graphic for Removal Next Round: Part 2of2
            history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue.put(history_OfDraws_Col02_PerBot_AsFigureObject)

            #
            # Archive Above New Graphic for Removal Next Round: Part 1of2
            history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['bot_id']]['history_OfDrawRectangles_LightLastDelta_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
            # Need following min_check, since a fatal silent error, will freeze program
            # 'not history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue.empty()' could work but could be obsolete
            if(history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue.qsize()>0):
                total_Window['_keyIs_BotSensor_Details__Graph_'].delete_figure(history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue.get(history_OfDraws_Col02_PerBot_AsFigureObject))
            history_OfDraws_Col02_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Details__Graph_'].draw_rectangle(
                ###jwc y top_left=(0, i*20+10+5),
                ###jwc y bottom_right=(rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['light_lastdelta'], i*20+10),
                top_left=(0, i*graph_BotSensorDetail_PIxelHigh_Int+10+5),
                ###jwc y bottom_right=(rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['light_lastdelta'], i*20+10),
                ###jwc y bottom_right=(rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['light_lastdelta'], i*graph_BotSensorDetail_PIxelHigh_Int+10),
                bottom_right=(rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['light_lastdelta']/graph_BotSensorDetail_Light_FitHorizontalMax_Divider, i*graph_BotSensorDetail_PIxelHigh_Int+10),
                fill_color='red',
                ###jwc n web: no argument: line_width=0,
                )
            # Archive Above New Graphic for Removal Next Round: Part 2of2
            history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue.put(history_OfDraws_Col02_PerBot_AsFigureObject)

            #
            # # Archive Above New Graphic for Removal Next Round: Part 1of2
            history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['bot_id']]['history_OfDrawRectangles_MagnetLastDelta_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
            # Need following min_check, since a fatal silent error, will freeze program
            # 'not history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue.empty()' could work but could be obsolete
            if(history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue.qsize()>0):
                total_Window['_keyIs_BotSensor_Details__Graph_'].delete_figure(history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue.get(history_OfDraws_Col02_PerBot_AsFigureObject))
            history_OfDraws_Col02_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Details__Graph_'].draw_rectangle(
                ###jwc y top_left=(0, i*20+5),
                ###jwc y bottom_right=(rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['magnet_lastdelta'], i*20),
                top_left=(0, i*graph_BotSensorDetail_PIxelHigh_Int+5),
                ###jwc y bottom_right=(rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['magnet_lastdelta'], i*20),
                ###jwc y bottom_right=(rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['magnet_lastdelta'], i*graph_BotSensorDetail_PIxelHigh_Int),
                bottom_right=(rowData_ArrayList_OfDictionaryPairs_ForAllBots__Values['magnet_lastdelta']/graph_BotSensorDetail_Magnet_FitHorizontalMax_Divider, i*graph_BotSensorDetail_PIxelHigh_Int),
                fill_color='green',
                ###jwc n web: no argument: line_width=0,
                )
            # Archive Above New Graphic for Removal Next Round: Part 2of2
            history_OfDraws_Col02_PerBot_AsFigureObject_AllFigureObjectsInQueue.put(history_OfDraws_Col02_PerBot_AsFigureObject)
        
    ###jwc CLEAR total_Window['_keyIs_BotSensor_Details__Graph_'].
    ###jwc y? total_Window['_keyIs_BotSensor_Details__Graph_'].erase()

total_Window.close()


#
# ARCHIVE: OBSOLETE
#
            ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((lastX1, rowData_ForOneBot['light_total_old']), 
            ###jwc n str total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, rowData_ForOneBot['light_total_old']), 
            ###jwc n total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, int(rowData_ForOneBot['light_total_old'])), 
            
            ###jwc o total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, rowData_ForOneBot['light_total_old']), 
            ###jwc o                            (x_Now, rowData_ForOneBot['light_total']), 
            ###jwc o                            color='blue', 
            ###jwc o                            width=1)
            ###jwc y rowData_ForOneBot_Y_Now = int( rowData_ForOneBot['light_total'] / graph_Vertical_Divider_Now_Int )
            ###jwc y rowData_ForOneBot_Y_Old = int( rowData_ForOneBot['light_total_old'] / graph_Vertical_Divider_Now_Int )


            ###jwc n total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now, rowData_ForOneBot_Y_Now+5), font=('Arial', 6), text_location='right')
            ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5))
            ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 10))
            ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 6))
            ###jwc n Web: TypeError: DrawText() got an unexpected keyword argument 'text_location': total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4), text_location='center')
                    
            ###jwc yy total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4)))
            ###jwc y? history_OfDrawLines_Queue_ABot_1D.put(total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4)))
            ###jwc 23-0527-1320 y5? history_OfDrawTexts_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4))
            
            
            ###jwc n history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']]['Queue':history_OfDrawLines_Queue_ABot_1D]
            ###jwc y? history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']] = {'DrawLine_Figure_Object':history_OfDrawLines_Queue_ABot_1D}
            
            ###jwc y? history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']] = {'DrawLine_Figure_Object':history_OfDrawLines_Queue_ABot_1D}
            ###jwc y? history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']].put(history_OfDrawTexts_PerBot_AsFigureObject)
            ###jwc y?n history_OfDrawLines_Queue_ABot_1D[rowData_ForOneBot['bot_id']]['Queue'].put(history_OfDrawTexts_PerBot_AsFigureObject)
            ###jwc y3? history_OfDrawLines_Queue_ABot_1D[rowData_ForOneBot['bot_id']].put(history_OfDrawTexts_PerBot_AsFigureObject)

            ###jwc y4? history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']]['DrawLine_Figure_Object_Queue'].put(history_OfDrawTexts_PerBot_AsFigureObject)
            ###jwc 23-0527-1320 y5? history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']].put(history_OfDrawTexts_PerBot_AsFigureObject)
                                
            ###jwc y history_OfDrawTexts_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4))
            ###jwc y history_OfDrawTexts_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 3))
            ###jwc y history_OfDrawTexts_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial',2), color='grey')
            ###jwc y history_OfDrawTexts_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial',2), color='red')


    ###jwc y if x_Now < (GRAPH_SIZE[0]-20):               # if still drawing initial width of graph
    ###jwc y     ###jwc o total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, lasty), (x_Now, y), width=1)
    ###jwc y     ###jwc o total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, lasty+10), (x_Now, y+10), color='green', width=1)
    ###jwc y     ###jwc o total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((lastX1, lastY1), (x_Now, int(rowData_ArrayList_OfDictionaryPairs_ForAllBots[0]['light_total'])), color='yellow', width=1)
    ###jwc y 
    ###jwc y     for rowData_ForOneBot in rowData_ArrayList_OfDictionaryPairs_ForAllBots:
    ###jwc y         ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((lastX1, rowData_ForOneBot['light_total_old']), 
    ###jwc y         ###jwc n str total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, rowData_ForOneBot['light_total_old']), 
    ###jwc y         ###jwc n total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, int(rowData_ForOneBot['light_total_old'])), 
    ###jwc y         
    ###jwc y         ###jwc o total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, rowData_ForOneBot['light_total_old']), 
    ###jwc y         ###jwc o                            ###jwc y (x_Now, int(rowData_ForOneBot['light_total'])), 
    ###jwc y         ###jwc o                            (x_Now, rowData_ForOneBot['light_total']), 
    ###jwc y         ###jwc o                            color='blue', 
    ###jwc y         ###jwc o                            width=1)
    ###jwc y         rowData_ForOneBot_Y_Now = int( rowData_ForOneBot['light_total'] / graph_Vertical_Divider_Now_Int )
    ###jwc y         rowData_ForOneBot_Y_Old = int( rowData_ForOneBot['light_total_old'] / graph_Vertical_Divider_Now_Int )
    ###jwc y         ###jwc y rowData_ForOneBot_BotLabel = str(rowData_ForOneBot['bot_id']) +':'+ str(rowData_ForOneBot['light_lastdelta']) +':'+ str(rowData_ForOneBot['light_total'])
    ###jwc y         rowData_ForOneBot_BotLabel = str(rowData_ForOneBot['bot_id'])
    ###jwc y 
    ###jwc y         total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, rowData_ForOneBot_Y_Old), 
    ###jwc y                                    ###jwc y (x_Now, int(rowData_ForOneBot['light_total'])), 
    ###jwc y                                    (x_Now, rowData_ForOneBot_Y_Now), 
    ###jwc y                                    color='blue', 
    ###jwc y                                    width=1)
    ###jwc y         ###jwc n total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now, rowData_ForOneBot_Y_Now+5), font=('Arial', 6), text_location='right')
    ###jwc y         ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5))
    ###jwc y         ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 10))
    ###jwc y         ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 6))
    ###jwc y         total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4), text_location='center')
    ###jwc y         
    ###jwc y         rowData_ForOneBot['light_total_old'] = rowData_ForOneBot['light_total']
    ###jwc y 
    ###jwc y else:                               # finished drawing full graph width so move each time to make room
    ###jwc y     ###jwc ? 'str' total_Window['_keyIs_BotSensor_Summary__Graph_'].Move(-graph_Horizontal_StepSize_Int, 0)
    ###jwc y     ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].Move(-1*int(graph_Horizontal_StepSize_Int), 0)
    ###jwc y     total_Window['_keyIs_BotSensor_Summary__Graph_'].Move(-graph_Horizontal_StepSize_Int, 0)
    ###jwc y     ###jwc o total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, lasty), (x_Now, y), width=1)
    ###jwc y     ###jwc o total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, lasty+10), (x_Now, y+10), color='green', width=1)
    ###jwc y     ###jwc o total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((lastX1, lastY1), (x_Now, int(rowData_ArrayList_OfDictionaryPairs_ForAllBots[0]['light_total'])), color='yellow', width=1)
    ###jwc y 
    ###jwc y     ###jwc on for rowData_ForOneBot in rowData_ArrayList_OfDictionaryPairs_ForAllBots:
    ###jwc y     ###jwc on     ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((lastX1, rowData_ForOneBot['light_total_old']), 
    ###jwc y     ###jwc on     total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, rowData_ForOneBot['light_total_old']), 
    ###jwc y     ###jwc on                                ###jwc y (x_Now, int(rowData_ForOneBot['light_total'])), 
    ###jwc y     ###jwc on                                (x_Now, rowData_ForOneBot['light_total']), 
    ###jwc y     ###jwc on                                color='blue', 
    ###jwc y     ###jwc on                                width=1)
    ###jwc y     ###jwc on     rowData_ForOneBot['light_total_old'] = rowData_ForOneBot['light_total']
    ###jwc y 
    ###jwc y 
    ###jwc y     for rowData_ForOneBot in rowData_ArrayList_OfDictionaryPairs_ForAllBots:
    ###jwc y         ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((lastX1, rowData_ForOneBot['light_total_old']), 
    ###jwc y         ###jwc n str total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, rowData_ForOneBot['light_total_old']), 
    ###jwc y         ###jwc n total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, int(rowData_ForOneBot['light_total_old'])), 
    ###jwc y         
    ###jwc y         ###jwc o total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, rowData_ForOneBot['light_total_old']), 
    ###jwc y         ###jwc o                            ###jwc y (x_Now, int(rowData_ForOneBot['light_total'])), 
    ###jwc y         ###jwc o                            (x_Now, rowData_ForOneBot['light_total']), 
    ###jwc y         ###jwc o                            color='blue', 
    ###jwc y         ###jwc o                            width=1)
    ###jwc y         rowData_ForOneBot_Y_Now = int( rowData_ForOneBot['light_total'] / graph_Vertical_Divider_Now_Int )
    ###jwc y         rowData_ForOneBot_Y_Old = int( rowData_ForOneBot['light_total_old'] / graph_Vertical_Divider_Now_Int )
    ###jwc y         rowData_ForOneBot_BotLabel = str(rowData_ForOneBot['bot_id'])
    ###jwc y 
    ###jwc y         total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((x_Old, rowData_ForOneBot_Y_Old), 
    ###jwc y                                    ###jwc y (x_Now, int(rowData_ForOneBot['light_total'])), 
    ###jwc y                                    (x_Now, rowData_ForOneBot_Y_Now), 
    ###jwc y                                    color='blue', 
    ###jwc y                                    width=1)
    ###jwc y         
    ###jwc y         total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4), text_location='center')
    ###jwc y 
    ###jwc y         rowData_ForOneBot['light_total_old'] = rowData_ForOneBot['light_total']
    ###jwc y 
    ###jwc y     ###jwc ? 'str' x_Now -= graph_Horizontal_StepSize_Int
    ###jwc y     ###jwc y x_Now -= int(graph_Horizontal_StepSize_Int)
    ###jwc y     x_Now -= graph_Horizontal_StepSize_Int



###jwc 23-0529-1330 yy        ###jwc o if _debug_Show_Priority_Lo_Bool:
###jwc 23-0529-1330 yy        ###jwc o     ###jwc o print replaced by 'print'
###jwc 23-0529-1330 yy        ###jwc o     print("* A: Raw String: ")
###jwc 23-0529-1330 yy        ###jwc o     ###jwc o print("  A1>" + str(network_DataMessage_Rcvd_Str) +"|")
###jwc 23-0529-1330 yy        ###jwc o     print("  1:" + str(network_DataMessage_Rcvd_Str) +"|")
###jwc 23-0529-1330 yy        if _debug_Show_Priority_Mi_Bool:
###jwc 23-0529-1330 yy            print("  A2:network_DataMessage_Rcvd_Str:" + str(network_DataMessage_Rcvd_Str) +"|")
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy        if True:
###jwc 23-0529-1330 yy            scoreboard_DataNumNew_ArrayList = []
###jwc 23-0529-1330 yy            ###jwc y scoreboard_DataStrNew_ArrayList = network_DataMessage_Rcvd_Str.split("|")
###jwc 23-0529-1330 yy            scoreboard_DataStrNew_ArrayList = network_DataMessage_Rcvd_Str.split(",")
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy            for key_Value_Pair in scoreboard_DataStrNew_ArrayList:
###jwc 23-0529-1330 yy                ###jwc o key_Value_Pair__Value = key_Value_Pair.substr(key_Value_Pair.index_of(":") + 1, len(key_Value_Pair))
###jwc 23-0529-1330 yy                ###jwc o key_Value_Pair__Value = key_Value_Pair[key_Value_Pair.index_of(":") + 1:len(key_Value_Pair)]
###jwc 23-0529-1330 yy                ## * Skip past "b'" prefix
###jwc 23-0529-1330 yy                ##jwc ? key_Value_Pair__Key = key_Value_Pair[2 : key_Value_Pair.index(":")-1]
###jwc 23-0529-1330 yy                ##jwc n key_Value_Pair__Key = key_Value_Pair[0:key_Value_Pair.index(":")-1]
###jwc 23-0529-1330 yy                key_Value_Pair__Key = key_Value_Pair[key_Value_Pair.index(":")-1 : key_Value_Pair.index(":")]
###jwc 23-0529-1330 yy                ##jwc y key_Value_Pair__Value = key_Value_Pair[key_Value_Pair.index(":") + 1:len(key_Value_Pair)]
###jwc 23-0529-1330 yy                key_Value_Pair__Value = key_Value_Pair[key_Value_Pair.index(":") + 1:len(key_Value_Pair)]
###jwc 23-0529-1330 yy                ##jwc yy scoreboard_DataNumNew_ArrayList.append(int(key_Value_Pair__Value))
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy                ##jwc n scoreboard_DataNumNew_ArrayList.append({key_Value_Pair__Key:int(key_Value_Pair__Value)})
###jwc 23-0529-1330 yy                
###jwc 23-0529-1330 yy                try:
###jwc 23-0529-1330 yy                    ### n scoreboard_DataNumNew_ArrayList['A']=int(key_Value_Pair__Value)
###jwc 23-0529-1330 yy                    ### scoreboard_DataNumNew_ArrayList.append(int(key_Value_Pair__Value))
###jwc 23-0529-1330 yy                    # Add new 'key_Value_Pair'
###jwc 23-0529-1330 yy                    scoreboard_DataMessage_Rcvd_Dict[key_Value_Pair__Key]=int(key_Value_Pair__Value)
###jwc 23-0529-1330 yy                except ValueError:
###jwc 23-0529-1330 yy                    scoreboard_DataMessage_Rcvd_Dict[key_Value_Pair__Key]=str(key_Value_Pair__Value)
###jwc 23-0529-1330 yy                    print("!!! 23-0519-1200 'except ValueError' 1:" + str(scoreboard_DataMessage_Rcvd_Dict[key_Value_Pair__Key]) + " 2:" + str(key_Value_Pair__Key) + " 3:" + str(key_Value_Pair__Value) + "|")
###jwc 23-0529-1330 yy                    return
###jwc 23-0529-1330 yy                except:
###jwc 23-0529-1330 yy                    print("!!! 23-0519-1210 non-'except ValueError'")
###jwc 23-0529-1330 yy                    return
###jwc 23-0529-1330 yy                
###jwc 23-0529-1330 yy                if _debug_Show_Priority_Lo_Bool:
###jwc 23-0529-1330 yy                    print("* B: Parsed Key:key_Value_Pair:")
###jwc 23-0529-1330 yy                    print("  1:key_Value_Pair|key_Value_Pair__Key|key_Value_Pair__Value: " + key_Value_Pair +"|"+ key_Value_Pair__Key +"|"+ key_Value_Pair__Value +"|")
###jwc 23-0529-1330 yy                    
###jwc 23-0529-1330 yy                    ###jwc o print("  2:"+ str((scoreboard_DataNumNew_ArrayList[len(scoreboard_DataNumNew_ArrayList) - 1])) +"|")
###jwc 23-0529-1330 yy                    ###jwc o print("  3:"+ str(scoreboard_DataNumNew_ArrayList)
###jwc 23-0529-1330 yy                          
###jwc 23-0529-1330 yy                    print("  2:scoreboard_DataMessage_Recvd_Dict: "+ str(scoreboard_DataMessage_Rcvd_Dict) +"|")
###jwc 23-0529-1330 yy                   
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy        scoreboard_Bot_Found_Bool = False
###jwc 23-0529-1330 yy        if _debug_Show_Priority_Lo_Bool:
###jwc 23-0529-1330 yy            print("* C")
###jwc 23-0529-1330 yy            print("  C1:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots))
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy        for bot_dictionary in rowData_ArrayList_OfDictionaryPairs_ForAllBots:
###jwc 23-0529-1330 yy            if _debug_Show_Priority_Lo_Bool:
###jwc 23-0529-1330 yy                print("  C2:" + str(bot_dictionary))
###jwc 23-0529-1330 yy            ###jwc y? if scoreboard_DataMessage_Rcvd_Dict['#'] in bot_dictionary.values():
###jwc 23-0529-1330 yy            if scoreboard_DataMessage_Rcvd_Dict['#'] == bot_dictionary['bot_id']:
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy                scoreboard_Bot_Found_Bool = True    
###jwc 23-0529-1330 yy                
###jwc 23-0529-1330 yy                if _debug_Show_Priority_Mi_Bool:
###jwc 23-0529-1330 yy                    print("  C3a:bot_dictionary: " + str(bot_dictionary))
###jwc 23-0529-1330 yy                bot_dictionary['light_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['L']
###jwc 23-0529-1330 yy                bot_dictionary['light_total'] += scoreboard_DataMessage_Rcvd_Dict['L']
###jwc 23-0529-1330 yy                
###jwc 23-0529-1330 yy                ###jwc n bot_dictionary['light_total_old'] = 0
###jwc 23-0529-1330 yy                                
###jwc 23-0529-1330 yy                bot_dictionary['magnet_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['M']
###jwc 23-0529-1330 yy                bot_dictionary['magnet_total'] += scoreboard_DataMessage_Rcvd_Dict['M']
###jwc 23-0529-1330 yy                
###jwc 23-0529-1330 yy                # Add 'Light Sensor' and Subtract 'Magnet Sensor'
###jwc 23-0529-1330 yy                bot_dictionary['grand_total'] += scoreboard_DataMessage_Rcvd_Dict['L'] - scoreboard_DataMessage_Rcvd_Dict['M']
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy                ###jwc y switch to 'grand_total': if  bot_dictionary['light_total'] > graph_Vertical_Max_Now_Int:
###jwc 23-0529-1330 yy                if  bot_dictionary['grand_total'] > graph_Vertical_Max_Now_Int:
###jwc 23-0529-1330 yy                    graph_Vertical_Max_Now_Int *= graph_Vertical_MULTIPLIER_INT
###jwc 23-0529-1330 yy                    graph_Vertical_Divider_Now_Int *= graph_Vertical_MULTIPLIER_INT
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy                if  bot_dictionary['grand_total'] < -graph_Vertical_Max_Now_Int:
###jwc 23-0529-1330 yy                    graph_Vertical_Max_Now_Int *= graph_Vertical_MULTIPLIER_INT
###jwc 23-0529-1330 yy                    graph_Vertical_Divider_Now_Int *= graph_Vertical_MULTIPLIER_INT
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy                if _debug_Show_Priority_Mi_Bool:
###jwc 23-0529-1330 yy                    print("  C3b:bot_dictionary: " + str(bot_dictionary))
###jwc 23-0529-1330 yy                
###jwc 23-0529-1330 yy        if not (scoreboard_Bot_Found_Bool):
###jwc 23-0529-1330 yy            ##jwc o _debug_Show_Priority_Mi_Bool.append(scoreboard_DataNumNew_ArrayList)
###jwc 23-0529-1330 yy            ##jwc o if _debug_Show_Priority_Lo_Bool:
###jwc 23-0529-1330 yy            ##jwc o     print("* NewBotAdd:" + str(scoreboard_BotsAll_ArrayList_2D[len(scoreboard_BotsAll_ArrayList_2D) - 1]) + " " + str(len(scoreboard_BotsAll_ArrayList_2D)))
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy            # base_0 needed for letter
###jwc 23-0529-1330 yy            ###jwc yy rowData_OfDictionaryPairs_ForABot_Empty_Local['row_id'] = chr( ord('A') + (len(rowData_ArrayList_OfDictionaryPairs_ForAllBots) ) -1 )
###jwc 23-0529-1330 yy            ###jwc yy rowData_OfDictionaryPairs_ForABot_Empty_Local['bot_id'] = scoreboard_DataMessage_Rcvd_Dict['#']
###jwc 23-0529-1330 yy            ###jwc yy rowData_OfDictionaryPairs_ForABot_Empty_Local['light_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['L']
###jwc 23-0529-1330 yy            ###jwc yy rowData_OfDictionaryPairs_ForABot_Empty_Local['light_total'] += scoreboard_DataMessage_Rcvd_Dict['L']
###jwc 23-0529-1330 yy            ###jwc yy rowData_OfDictionaryPairs_ForABot_Empty_Local['magnet_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['M']
###jwc 23-0529-1330 yy            ###jwc yy rowData_OfDictionaryPairs_ForABot_Empty_Local['magnet_total'] += scoreboard_DataMessage_Rcvd_Dict['M']
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy            if _debug_Show_Priority_Mi_Bool:
###jwc 23-0529-1330 yy                ###jwc yy print("  D1aa:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots))
###jwc 23-0529-1330 yy                print("* D1:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]))
###jwc 23-0529-1330 yy                ###jwc y print("  D1ab:" + str(rowData_OfDictionaryPairs_ForABot_Empty_Local))
###jwc 23-0529-1330 yy            ###jwc yy rowData_ArrayList_OfDictionaryPairs_ForAllBots.append(rowData_OfDictionaryPairs_ForABot_Empty_Local)
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['row_id'] = chr( ord('A') + rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int)
###jwc 23-0529-1330 yy            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['bot_id'] = scoreboard_DataMessage_Rcvd_Dict['#']
###jwc 23-0529-1330 yy            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['light_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['L']
###jwc 23-0529-1330 yy            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['light_total'] = scoreboard_DataMessage_Rcvd_Dict['L']
###jwc 23-0529-1330 yy            ###jwc n rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['light_total_old'] = 0
###jwc 23-0529-1330 yy            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['magnet_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['M']
###jwc 23-0529-1330 yy            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['magnet_total'] = scoreboard_DataMessage_Rcvd_Dict['M']
###jwc 23-0529-1330 yy            # Add 'Light Sensor' and Subtract 'Magnet Sensor'
###jwc 23-0529-1330 yy            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['grand_total'] = scoreboard_DataMessage_Rcvd_Dict['L'] - scoreboard_DataMessage_Rcvd_Dict['M']
###jwc 23-0529-1330 yy 
###jwc 23-0529-1330 yy            ###jwc n history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int] = {'history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key': Queue()}
###jwc 23-0529-1330 yy            history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[scoreboard_DataMessage_Rcvd_Dict['#']] = {
###jwc 23-0529-1330 yy                'history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key': Queue(), 
###jwc 23-0529-1330 yy                'history_OfDrawLines_LightLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue(),
###jwc 23-0529-1330 yy                'history_OfDrawLines_MagnetLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key':Queue()
###jwc 23-0529-1330 yy                }
###jwc 23-0529-1330 yy            history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[scoreboard_DataMessage_Rcvd_Dict['#']] = {
###jwc 23-0529-1330 yy                'history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key': Queue()
###jwc 23-0529-1330 yy                }
###jwc 23-0529-1330 yy            
###jwc 23-0529-1330 yy            if _debug_Show_Priority_Mi_Bool:
###jwc 23-0529-1330 yy                print("  D2:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]))
###jwc 23-0529-1330 yy            ####jwc n rowData_ArrayList_OfDictionaryPairs_ForAllBots.sort(key=lambda x_Now: x_Now.get('bot_id'))
###jwc 23-0529-1330 yy            ###jwc n rowData_ArrayList_OfDictionaryPairs_ForAllBots.sort(key=lambda x_Now: x_Now.get('row_id'))
###jwc 23-0529-1330 yy            ###jwc y rowData_ArrayList_OfDictionaryPairs_ForAllBots.sort(key=get_bot_id_fn)
###jwc 23-0529-1330 yy            ###jwc y if _debug_Show_Priority_Mi_Bool:
###jwc 23-0529-1330 yy            ###jwc y     print("  D1c:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots))
###jwc 23-0529-1330 yy
###jwc 23-0529-1330 yy            rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int += 1


###jwc 23-0529-1500 yy
###jwc 23-0529-1500 yy    ###jwc y for rowData_ForOneBot in rowData_ArrayList_OfDictionaryPairs_ForAllBots:
###jwc 23-0529-1500 yy    for rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int in rowData_ArrayList_OfDictionaryPairs_ForAllBots.keys():
###jwc 23-0529-1500 yy        
###jwc 23-0529-1500 yy        ###jwc y if rowData_ForOneBot_BotLabel != '':
###jwc 23-0529-1500 yy        # Skip Test Bot_Id = 0
###jwc 23-0529-1500 yy        if rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int != 0:
###jwc 23-0529-1500 yy            
###jwc 23-0529-1500 yy            ###jwc y rowData_ForOneBot_BotLabel = str(rowData_ForOneBot['bot_id']) +':'+ str(rowData_ForOneBot['light_lastdelta']) +':'+ str(rowData_ForOneBot['light_total'])
###jwc 23-0529-1500 yy            ###jwc y rowData_ForOneBot_BotLabel = str(rowData_ForOneBot['bot_id'])
###jwc 23-0529-1500 yy            rowData_ForOneBot_BotLabel = str(rowData_ArrayList_OfDictionaryPairs_ForAllBots__Key_BotId_Int)
###jwc 23-0529-1500 yy
###jwc 23-0529-1500 yy            # Clear Oldest Existing DrawLines/DrawTexts
###jwc 23-0529-1500 yy            #
###jwc 23-0529-1500 yy            if wrapAround_ForThisMainWhileLoop_Bool:
###jwc 23-0529-1500 yy                ###jwc 23-0527-1320 y5? sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']]['Queue'].get())
###jwc 23-0529-1500 yy
###jwc 23-0529-1500 yy                history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ForOneBot['bot_id']]['history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
###jwc 23-0529-1500 yy                sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.get(history_OfDrawLines_PerBot_AsFigureObject))
###jwc 23-0529-1500 yy
###jwc 23-0529-1500 yy                history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ForOneBot['bot_id']]['history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
###jwc 23-0529-1500 yy                sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue.get(history_OfDrawTexts_PerBot_AsFigureObject))
###jwc 23-0529-1500 yy                ###jwc seems not needed y: history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ForOneBot['bot_id']]['history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key'] = history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue
###jwc 23-0529-1500 yy        
###jwc 23-0529-1500 yy                history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ForOneBot['bot_id']]['history_OfDrawLines_LightLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
###jwc 23-0529-1500 yy                sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.get(history_OfDrawLines_PerBot_AsFigureObject))
###jwc 23-0529-1500 yy
###jwc 23-0529-1500 yy                history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ForOneBot['bot_id']]['history_OfDrawLines_MagnetLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
###jwc 23-0529-1500 yy                sub_Window__keyIs_BotSensor_Summary__Graph_.delete_figure(history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.get(history_OfDrawLines_PerBot_AsFigureObject))
###jwc 23-0529-1500 yy
###jwc 23-0529-1500 yy
###jwc 23-0529-1500 yy            ###jwc y total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine((lastX1, rowData_ForOneBot['light_total_old']), 
###jwc 23-0529-1500 yy            ###jwc y rowData_ForOneBot_Y_Now = int( rowData_ForOneBot['light_total'] / graph_Vertical_Divider_Now_Int )
###jwc 23-0529-1500 yy            ###jwc y rowData_ForOneBot_Y_Old = int( rowData_ForOneBot['light_total_old'] / graph_Vertical_Divider_Now_Int )
###jwc 23-0529-1500 yy
###jwc 23-0529-1500 yy            
###jwc 23-0529-1500 yy            rowData_ForOneBot_Y_Now = int( rowData_ForOneBot['grand_total'] / graph_Vertical_Divider_Now_Int )
###jwc 23-0529-1500 yy            rowData_ForOneBot_Y_Old = int( rowData_ForOneBot['grand_total_old'] / graph_Vertical_Divider_Now_Int )
###jwc 23-0529-1500 yy            
###jwc 23-0529-1500 yy            rowData_ForOneBot_Y_LightLastDelta_Now = rowData_ForOneBot_Y_Now + int( rowData_ForOneBot['light_lastdelta'] / graph_Vertical_Divider_Now_Int )
###jwc 23-0529-1500 yy            rowData_ForOneBot_Y_MagnetLastDelta_Now = rowData_ForOneBot_Y_Now - int( rowData_ForOneBot['magnet_lastdelta'] / graph_Vertical_Divider_Now_Int )
###jwc 23-0529-1500 yy
###jwc 23-0529-1500 yy
###jwc 23-0529-1500 yy            history_OfDrawLines_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine(
###jwc 23-0529-1500 yy                                                                                    (x_Old, rowData_ForOneBot_Y_Old), 
###jwc 23-0529-1500 yy                                                                                    (x_Now, rowData_ForOneBot_Y_Now), 
###jwc 23-0529-1500 yy                                                                                    color='blue', 
###jwc 23-0529-1500 yy                                                                                    width=1)
###jwc 23-0529-1500 yy            history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ForOneBot['bot_id']]\
###jwc 23-0529-1500 yy                                                                                                                                                               ['history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
###jwc 23-0529-1500 yy            history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.put(history_OfDrawLines_PerBot_AsFigureObject)
###jwc 23-0529-1500 yy            
###jwc 23-0529-1500 yy            history_OfDrawLines_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine(
###jwc 23-0529-1500 yy                                                                                    ###jwc n could make sesne, but gap with x: (x_Old, rowData_ForOneBot_Y_Now), 
###jwc 23-0529-1500 yy                                                                                    ###jwc n could make sesne, but gap with x: (x_Old, rowData_ForOneBot_Y_LightLastDelta_Now), 
###jwc 23-0529-1500 yy                                                                                    (x_Now, rowData_ForOneBot_Y_Now), 
###jwc 23-0529-1500 yy                                                                                    (x_Now, rowData_ForOneBot_Y_LightLastDelta_Now), 
###jwc 23-0529-1500 yy                                                                                    color='red', 
###jwc 23-0529-1500 yy                                                                                    width=1)
###jwc 23-0529-1500 yy            history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ForOneBot['bot_id']]\
###jwc 23-0529-1500 yy                                                                                                                                                               ['history_OfDrawLines_LightLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
###jwc 23-0529-1500 yy            history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.put(history_OfDrawLines_PerBot_AsFigureObject)
###jwc 23-0529-1500 yy
###jwc 23-0529-1500 yy            history_OfDrawLines_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawLine(
###jwc 23-0529-1500 yy                                                                                    ###jwc n could make sesne, but gap with x: (x_Old, rowData_ForOneBot_Y_Now), 
###jwc 23-0529-1500 yy                                                                                    ###jwc n could make sesne, but gap with x: (x_Old, rowData_ForOneBot_Y_MagnetLastDelta_Now), 
###jwc 23-0529-1500 yy                                                                                    (x_Now, rowData_ForOneBot_Y_Now), 
###jwc 23-0529-1500 yy                                                                                    (x_Now, rowData_ForOneBot_Y_MagnetLastDelta_Now), 
###jwc 23-0529-1500 yy                                                                                    color='green', 
###jwc 23-0529-1500 yy                                                                                    width=1)
###jwc 23-0529-1500 yy            history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ForOneBot['bot_id']]\
###jwc 23-0529-1500 yy                                                                                                                                                               ['history_OfDrawLines_MagnetLastDelta_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
###jwc 23-0529-1500 yy            history_OfDrawLines_PerBot_AsFigureObject_AllFigureObjectsInQueue.put(history_OfDrawLines_PerBot_AsFigureObject)
###jwc 23-0529-1500 yy
###jwc 23-0529-1500 yy            ###jwc yy FontSize Seems to Work Only in Non-Web-Only: total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4)))
###jwc 23-0529-1500 yy            ###jwc 23-0527-1320 y5? history_OfDrawTexts_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4))
###jwc 23-0529-1500 yy            ###jwc y3? history_OfDrawLines_Queue_ABot_1D[rowData_ForOneBot['bot_id']].put(history_OfDrawTexts_PerBot_AsFigureObject)
###jwc 23-0529-1500 yy            ###jwc y4? history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']]['DrawLine_Figure_Object_Queue'].put(history_OfDrawTexts_PerBot_AsFigureObject)
###jwc 23-0529-1500 yy            ###jwc 23-0527-1320 y5? history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']].put(history_OfDrawTexts_PerBot_AsFigureObject)
###jwc 23-0529-1500 yy            ###jwc y history_OfDrawTexts_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4))
###jwc 23-0529-1500 yy
###jwc 23-0529-1500 yy            ###jwc ym Web is limited: no font nor color: history_OfDrawTexts_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5), font='Arial 3', color='red')
###jwc 23-0529-1500 yy            history_OfDrawTexts_PerBot_AsFigureObject = total_Window['_keyIs_BotSensor_Summary__Graph_'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x_Now-5, rowData_ForOneBot_Y_Now+5))
###jwc 23-0529-1500 yy            history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue = history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ForOneBot['bot_id']]\
###jwc 23-0529-1500 yy                                                                                                                                                               ['history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key']
###jwc 23-0529-1500 yy            history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue.put(history_OfDrawTexts_PerBot_AsFigureObject)
###jwc 23-0529-1500 yy            
###jwc 23-0529-1500 yy            ###jwc seems not needed y: history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_InDictionList[rowData_ForOneBot['bot_id']]['history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue_Key'] = history_OfDrawTexts_PerBot_AsFigureObject_AllFigureObjectsInQueue
###jwc 23-0529-1500 yy            
###jwc 23-0529-1500 yy            ###jwc y rowData_ForOneBot['light_total_old'] = rowData_ForOneBot['light_total']
###jwc 23-0529-1500 yy            ###jwc y calculate first stage above: rowData_ForOneBot['grand_total_old'] = rowData_ForOneBot['grand_total']
