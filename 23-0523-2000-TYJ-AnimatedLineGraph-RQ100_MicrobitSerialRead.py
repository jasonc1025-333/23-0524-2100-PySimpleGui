###jwc o import PySimpleGUI as sg
###jwc n 'step_size' is 'str' error: import PySimpleGUIWeb as sg
###jwc o import PySimpleGUI as sg
import PySimpleGUIWeb as sg

from random import randint

import serial


rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int = 0

###jwc TODO https://www.w3schools.com/python/python_dictionaries_nested.asp
###jwc TODO rowData_ArrayList_OfDictionaryPairs_ForAllBots = { 
###jwc TODO                                                   {},
###jwc TODO                                                   {},
###jwc TODO                                                   }
rowData_ArrayList_OfDictionaryPairs_ForAllBots = [
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

    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},

    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},

    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
    {'row_id':'', 'bot_id':'', 'mission_status':'', 'team_id':'', 'light_lastdelta':'', 'light_total':0, 'light_total_old':0, 'magnet_lastdelta':'', 'magnet_total':''},
]

scoreboard_DataMessage_Rcvd_Dict = {}

ser = serial.Serial(
        ##jwc o port='/dev/ttyACM0',
        ###jwc y port='/dev/ttyACM1',

        ##jwc o port='COM3',
        port='/dev/ttyACM0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

# Debug Prints
#
###jwc y _debug_Show_Priority_Hi_Bool = True
_debug_Show_Priority_Hi_Bool = True
_debug_Show_Priority_Lo_Bool = False

#
# receive_Microbit_Messages_Fn
#
def receive_Microbit_Messages_Fn() -> None:
    global rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int
    global graph_Vertical_Now_Int, graph_Vertical_Divider_Int

    now,network_DataMessage_Rcvd_Bytes,y1,y2 = 0, 0, 0, 0

    rowData_OfDictionaryPairs_ForABot_Empty_Local = {
    ###jwc 23-0504-0710 y 'row_id':'A', 'bot_id':0, 'light_lastdelta':0, 'light_total':0, 'magnet_lastdelta':0, 'magnet_total':0,
    'row_id':'A', 'bot_id':0, 'mission_status':'-', 'team_id':'-', 'light_lastdelta':0, 'light_total':0, 'magnet_lastdelta':0, 'magnet_total':0,
    }


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
        if _debug_Show_Priority_Hi_Bool:
            print("  A2:network_DataMessage_Rcvd_Str:" + str(network_DataMessage_Rcvd_Str) +"|")

        if True:
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
            print("* C")
            print("  C1:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots))

        for bot_dictionary in rowData_ArrayList_OfDictionaryPairs_ForAllBots:
            if _debug_Show_Priority_Lo_Bool:
                print("  C2:" + str(bot_dictionary))
            ###jwc y? if scoreboard_DataMessage_Rcvd_Dict['#'] in bot_dictionary.values():
            if scoreboard_DataMessage_Rcvd_Dict['#'] == bot_dictionary['bot_id']:

                scoreboard_Bot_Found_Bool = True    
                
                if _debug_Show_Priority_Hi_Bool:
                    print("  C3a:bot_dictionary: " + str(bot_dictionary))
                bot_dictionary['light_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['L']
                bot_dictionary['light_total'] += scoreboard_DataMessage_Rcvd_Dict['L']
                ###jwc n bot_dictionary['light_total_old'] = 0
                if  bot_dictionary['light_total'] > graph_Vertical_Now_Int:
                    graph_Vertical_Now_Int *= graph_Vertical_MULTIPLIER_INT
                    graph_Vertical_Divider_Int *= graph_Vertical_MULTIPLIER_INT
                
                bot_dictionary['magnet_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['M']
                bot_dictionary['magnet_total'] += scoreboard_DataMessage_Rcvd_Dict['M']
                if _debug_Show_Priority_Hi_Bool:
                    print("  C3b:bot_dictionary: " + str(bot_dictionary))
                
        if not (scoreboard_Bot_Found_Bool):
            ##jwc o _debug_Show_Priority_Hi_Bool.append(scoreboard_DataNumNew_ArrayList)
            ##jwc o if _debug_Show_Priority_Lo_Bool:
            ##jwc o     print("* NewBotAdd:" + str(scoreboard_BotsAll_ArrayList_2D[len(scoreboard_BotsAll_ArrayList_2D) - 1]) + " " + str(len(scoreboard_BotsAll_ArrayList_2D)))

            # base_0 needed for letter
            ###jwc yy rowData_OfDictionaryPairs_ForABot_Empty_Local['row_id'] = chr( ord('A') + (len(rowData_ArrayList_OfDictionaryPairs_ForAllBots) ) -1 )
            ###jwc yy rowData_OfDictionaryPairs_ForABot_Empty_Local['bot_id'] = scoreboard_DataMessage_Rcvd_Dict['#']
            ###jwc yy rowData_OfDictionaryPairs_ForABot_Empty_Local['light_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['L']
            ###jwc yy rowData_OfDictionaryPairs_ForABot_Empty_Local['light_total'] += scoreboard_DataMessage_Rcvd_Dict['L']
            ###jwc yy rowData_OfDictionaryPairs_ForABot_Empty_Local['magnet_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['M']
            ###jwc yy rowData_OfDictionaryPairs_ForABot_Empty_Local['magnet_total'] += scoreboard_DataMessage_Rcvd_Dict['M']

            if _debug_Show_Priority_Hi_Bool:
                ###jwc yy print("  D1aa:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots))
                print("* D1:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]))
                ###jwc y print("  D1ab:" + str(rowData_OfDictionaryPairs_ForABot_Empty_Local))
            ###jwc yy rowData_ArrayList_OfDictionaryPairs_ForAllBots.append(rowData_OfDictionaryPairs_ForABot_Empty_Local)

            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['row_id'] = chr( ord('A') + rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int)
            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['bot_id'] = scoreboard_DataMessage_Rcvd_Dict['#']
            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['light_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['L']
            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['light_total'] = scoreboard_DataMessage_Rcvd_Dict['L']
            ###jwc n rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['light_total_old'] = 0
            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['magnet_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['M']
            rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]['magnet_total'] = scoreboard_DataMessage_Rcvd_Dict['M']
 
            ###jwc n history_OfDrawTexts_PerBot_AsObject_ManyInQueue_InDictionList[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int] = {'history_OfDrawTexts_PerBot_AsObject_ManyInQueue_Key': Queue()}
            history_OfDrawTexts_PerBot_AsObject_ManyInQueue_InDictionList[scoreboard_DataMessage_Rcvd_Dict['#']] = {'history_OfDrawTexts_PerBot_AsObject_ManyInQueue_Key': Queue()}
            history_OfDrawLines_PerBot_AsObject_ManyInQueue_InDictionList[scoreboard_DataMessage_Rcvd_Dict['#']] = {'history_OfDrawLines_PerBot_AsObject_ManyInQueue_Key': Queue()}
            
            if _debug_Show_Priority_Hi_Bool:
                print("  D2:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots[rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int]))
            ####jwc n rowData_ArrayList_OfDictionaryPairs_ForAllBots.sort(key=lambda x: x.get('bot_id'))
            ###jwc n rowData_ArrayList_OfDictionaryPairs_ForAllBots.sort(key=lambda x: x.get('row_id'))
            ###jwc y rowData_ArrayList_OfDictionaryPairs_ForAllBots.sort(key=get_bot_id_fn)
            ###jwc y if _debug_Show_Priority_Hi_Bool:
            ###jwc y     print("  D1c:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots))

            rowData_ArrayList_OfDictionaryPairs_ForAllBots_NextUnusedIndex_Int += 1
    else:
        print("*** No Serial Read *** ")

#
# pySimpleGui
#

from queue import Queue

graph_Vertical_MAX_INT = 300
graph_Vertical_Now_Int = graph_Vertical_MAX_INT
graph_Vertical_Divider_Int = 1
graph_Vertical_MULTIPLIER_INT = 2

###jwc o GRAPH_SIZE = (400,200)
###jwc y GRAPH_SIZE = (400,400)
###jwc n too tall GRAPH_SIZE = (400,20000)
###jwc n GRAPH_SIZE = (500,500)
GRAPH_SIZE = (600,graph_Vertical_Now_Int)
###jwc y GRAPH_STEP_SIZE = 5
###jwc y GRAPH_STEP_SIZE = 15
GRAPH_STEP_SIZE = 30

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

history_OfDrawLines_PerBot_AsGraphicObject = None
history_OfDrawLines_PerBot_AsObject_ManyInQueue = Queue()
###jwc y history_OfDrawLines_PerBot_AsObject_ManyInQueue_InDictionList = {1:{'history_OfDrawLines_PerBot_AsObject_ManyInQueue_Key':None}}
history_OfDrawLines_PerBot_AsObject_ManyInQueue_InDictionList = {1:{'history_OfDrawLines_PerBot_AsObject_ManyInQueue_Key':Queue()}}


history_OfDrawTexts_PerBot_AsGraphicObject = None
history_OfDrawTexts_PerBot_AsObject_ManyInQueue = Queue()
###jwc y history_OfDrawTexts_PerBot_AsObject_ManyInQueue_InDictionList = {1:{'history_OfDrawTexts_PerBot_AsObject_ManyInQueue_Key':None}}
history_OfDrawTexts_PerBot_AsObject_ManyInQueue_InDictionList = {1:{'history_OfDrawTexts_PerBot_AsObject_ManyInQueue_Key':Queue()}}


layout = [  
            ### jwc y [sg.Graph(GRAPH_SIZE, (0,0), GRAPH_SIZE, key='-GRAPH-', background_color='lightblue')],
            [sg.Graph(GRAPH_SIZE, (0,0), GRAPH_SIZE, key='-GRAPH-', background_color='lightblue'), sg.Slider((0,30), default_value=15, orientation='h', key='-DELAY2-')],
            [sg.Text('graph_Vertical_Now_Int:'), sg.Text(key='-graph_Vertical_Now_Int-'), sg.Text('graph_Vertical_Divider_Int:'), sg.Text(key='-graph_Vertical_Divider_Int-')],
            ###jwc y [sg.Text('Milliseconds per sample:', size=(20,1)), sg.Text('____', key='-MSECPERSAMPLE-'), sg.Slider((0,30), default_value=15, orientation='h', key='-DELAY-'), sg.Text('Pixels per sample:', size=(20,1)), sg.Text('____', key='-PIXELPERSAMPLE-'), sg.Slider((0,30), default_value=GRAPH_STEP_SIZE, orientation='h', key='-STEP-SIZE-')],
            [sg.Text('Milliseconds per sample:', size=(20,1)), sg.Text('____', key='-MSECPERSAMPLE-'), sg.Slider((0,30), default_value=15, orientation='h', key='-DELAY-'), sg.Text('Pixels per sample:', size=(20,1)), sg.Text('____', key='-PIXELPERSAMPLE-'), sg.Slider((0,60), default_value=GRAPH_STEP_SIZE, orientation='h', key='-STEP-SIZE-')],
            ###jwc o  sg.Slider((1,30), default_value=GRAPH_STEP_SIZE, orientation='h', key='-STEP-SIZE-')],
            [sg.Button('Exit')]
            ]

###jwc y window = sg.Window('Animated Line Graph Example', layout)
window = sg.Window('Animated Line Graph Example', layout, web_port=5000)
graph = window["-GRAPH-"]  # type: sg.Graph

delay = x = lastx = lasty = 0

wrapAround_Bool = False

###jwc y lastX1 = lastY1 = 0

while True:                             # Event Loop

    receive_Microbit_Messages_Fn()

    #
    # !!! 'window.read' must precedde all 'window()' calls
    #
    event, values = window.read(timeout=delay)
    if event in (None, 'Exit'):
        break
    
    window['-graph_Vertical_Now_Int-'].update(graph_Vertical_Now_Int)
    window['-graph_Vertical_Divider_Int-'].update(graph_Vertical_Divider_Int)
    
    

    ###jwc o for web, convert text to int: step_size, delay = values['-STEP-SIZE-'], values['-DELAY-']
    step_size, delay = int(values['-STEP-SIZE-']), int(values['-DELAY-'])
    
    window['-MSECPERSAMPLE-'].update(delay)
    window['-PIXELPERSAMPLE-'].update(step_size)
    
    values['-graph_Vertical_Divider_Int-'] = graph_Vertical_Divider_Int
    
    y = randint(0,GRAPH_SIZE[1])        # get random point for graph
    ###jwc y but need to shift sooner: if x < GRAPH_SIZE[0]:               # if still drawing initial width of graph
    
    if x > (GRAPH_SIZE[0]-20):
        x, lastx = 0, 0
        ###jwc y window['-GRAPH-'].erase()
        wrapAround_Bool = True
    
    for rowData_ForOneBot in rowData_ArrayList_OfDictionaryPairs_ForAllBots:
        
        ###jwc y rowData_ForOneBot_BotLabel = str(rowData_ForOneBot['bot_id']) +':'+ str(rowData_ForOneBot['light_lastdelta']) +':'+ str(rowData_ForOneBot['light_total'])
        rowData_ForOneBot_BotLabel = str(rowData_ForOneBot['bot_id'])

        if rowData_ForOneBot_BotLabel != '':
            
            # Clear Oldest Existing DrawLine
            if wrapAround_Bool:
                ###jwc 23-0527-1320 y5? graph.delete_figure(history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']]['Queue'].get())

                history_OfDrawLines_PerBot_AsObject_ManyInQueue = history_OfDrawLines_PerBot_AsObject_ManyInQueue_InDictionList[rowData_ForOneBot['bot_id']]['history_OfDrawLines_PerBot_AsObject_ManyInQueue_Key']
                graph.delete_figure(history_OfDrawLines_PerBot_AsObject_ManyInQueue.get(history_OfDrawLines_PerBot_AsGraphicObject))

                history_OfDrawTexts_PerBot_AsObject_ManyInQueue = history_OfDrawTexts_PerBot_AsObject_ManyInQueue_InDictionList[rowData_ForOneBot['bot_id']]['history_OfDrawTexts_PerBot_AsObject_ManyInQueue_Key']
                graph.delete_figure(history_OfDrawTexts_PerBot_AsObject_ManyInQueue.get(history_OfDrawTexts_PerBot_AsGraphicObject))
                ###jwc seems not needed y: history_OfDrawTexts_PerBot_AsObject_ManyInQueue_InDictionList[rowData_ForOneBot['bot_id']]['history_OfDrawTexts_PerBot_AsObject_ManyInQueue_Key'] = history_OfDrawTexts_PerBot_AsObject_ManyInQueue
        
            
            ###jwc y window['-GRAPH-'].DrawLine((lastX1, rowData_ForOneBot['light_total_old']), 
            ###jwc n str window['-GRAPH-'].DrawLine((lastx, rowData_ForOneBot['light_total_old']), 
            ###jwc n window['-GRAPH-'].DrawLine((lastx, int(rowData_ForOneBot['light_total_old'])), 
            
            ###jwc o window['-GRAPH-'].DrawLine((lastx, rowData_ForOneBot['light_total_old']), 
            ###jwc o                            ###jwc y (x, int(rowData_ForOneBot['light_total'])), 
            ###jwc o                            (x, rowData_ForOneBot['light_total']), 
            ###jwc o                            color='blue', 
            ###jwc o                            width=1)
            rowData_ForOneBot_Y_Now = int( rowData_ForOneBot['light_total'] / graph_Vertical_Divider_Int )
            rowData_ForOneBot_Y_Old = int( rowData_ForOneBot['light_total_old'] / graph_Vertical_Divider_Int )

            history_OfDrawLines_PerBot_AsGraphicObject = window['-GRAPH-'].DrawLine((lastx, rowData_ForOneBot_Y_Old), 
                                    ###jwc y (x, int(rowData_ForOneBot['light_total'])), 
                                    (x, rowData_ForOneBot_Y_Now), 
                                    color='blue', 
                                    width=1)
            history_OfDrawLines_PerBot_AsObject_ManyInQueue = history_OfDrawLines_PerBot_AsObject_ManyInQueue_InDictionList[rowData_ForOneBot['bot_id']]['history_OfDrawLines_PerBot_AsObject_ManyInQueue_Key']
            history_OfDrawLines_PerBot_AsObject_ManyInQueue.put(history_OfDrawLines_PerBot_AsGraphicObject)

            ###jwc n window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x, rowData_ForOneBot_Y_Now+5), font=('Arial', 6), text_location='right')
            ###jwc y window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x-5, rowData_ForOneBot_Y_Now+5))
            ###jwc y window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 10))
            ###jwc y window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 6))
            ###jwc n Web: TypeError: DrawText() got an unexpected keyword argument 'text_location': window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4), text_location='center')
                    
            ###jwc yy window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4)))
            ###jwc y? history_OfDrawLines_Queue_ABot_1D.put(window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4)))
            ###jwc 23-0527-1320 y5? history_OfDrawTexts_PerBot_AsGraphicObject = window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4))
            
            
            ###jwc n history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']]['Queue':history_OfDrawLines_Queue_ABot_1D]
            ###jwc y? history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']] = {'DrawLine_Figure_Object':history_OfDrawLines_Queue_ABot_1D}
            
            ###jwc y? history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']] = {'DrawLine_Figure_Object':history_OfDrawLines_Queue_ABot_1D}
            ###jwc y? history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']].put(history_OfDrawTexts_PerBot_AsGraphicObject)
            ###jwc y?n history_OfDrawLines_Queue_ABot_1D[rowData_ForOneBot['bot_id']]['Queue'].put(history_OfDrawTexts_PerBot_AsGraphicObject)
            ###jwc y3? history_OfDrawLines_Queue_ABot_1D[rowData_ForOneBot['bot_id']].put(history_OfDrawTexts_PerBot_AsGraphicObject)

            ###jwc y4? history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']]['DrawLine_Figure_Object_Queue'].put(history_OfDrawTexts_PerBot_AsGraphicObject)
            ###jwc 23-0527-1320 y5? history_OfDrawLines_Queues_ManyBots_2D[rowData_ForOneBot['bot_id']].put(history_OfDrawTexts_PerBot_AsGraphicObject)
                                
            history_OfDrawTexts_PerBot_AsGraphicObject = window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4))
            history_OfDrawTexts_PerBot_AsObject_ManyInQueue = history_OfDrawTexts_PerBot_AsObject_ManyInQueue_InDictionList[rowData_ForOneBot['bot_id']]['history_OfDrawTexts_PerBot_AsObject_ManyInQueue_Key']
            history_OfDrawTexts_PerBot_AsObject_ManyInQueue.put(history_OfDrawTexts_PerBot_AsGraphicObject)
            ###jwc seems not needed y: history_OfDrawTexts_PerBot_AsObject_ManyInQueue_InDictionList[rowData_ForOneBot['bot_id']]['history_OfDrawTexts_PerBot_AsObject_ManyInQueue_Key'] = history_OfDrawTexts_PerBot_AsObject_ManyInQueue
            
            rowData_ForOneBot['light_total_old'] = rowData_ForOneBot['light_total']
    
    
    ###jwc y if x < (GRAPH_SIZE[0]-20):               # if still drawing initial width of graph
    ###jwc y     ###jwc o window['-GRAPH-'].DrawLine((lastx, lasty), (x, y), width=1)
    ###jwc y     ###jwc o window['-GRAPH-'].DrawLine((lastx, lasty+10), (x, y+10), color='green', width=1)
    ###jwc y     ###jwc o window['-GRAPH-'].DrawLine((lastX1, lastY1), (x, int(rowData_ArrayList_OfDictionaryPairs_ForAllBots[0]['light_total'])), color='yellow', width=1)
    ###jwc y 
    ###jwc y     for rowData_ForOneBot in rowData_ArrayList_OfDictionaryPairs_ForAllBots:
    ###jwc y         ###jwc y window['-GRAPH-'].DrawLine((lastX1, rowData_ForOneBot['light_total_old']), 
    ###jwc y         ###jwc n str window['-GRAPH-'].DrawLine((lastx, rowData_ForOneBot['light_total_old']), 
    ###jwc y         ###jwc n window['-GRAPH-'].DrawLine((lastx, int(rowData_ForOneBot['light_total_old'])), 
    ###jwc y         
    ###jwc y         ###jwc o window['-GRAPH-'].DrawLine((lastx, rowData_ForOneBot['light_total_old']), 
    ###jwc y         ###jwc o                            ###jwc y (x, int(rowData_ForOneBot['light_total'])), 
    ###jwc y         ###jwc o                            (x, rowData_ForOneBot['light_total']), 
    ###jwc y         ###jwc o                            color='blue', 
    ###jwc y         ###jwc o                            width=1)
    ###jwc y         rowData_ForOneBot_Y_Now = int( rowData_ForOneBot['light_total'] / graph_Vertical_Divider_Int )
    ###jwc y         rowData_ForOneBot_Y_Old = int( rowData_ForOneBot['light_total_old'] / graph_Vertical_Divider_Int )
    ###jwc y         ###jwc y rowData_ForOneBot_BotLabel = str(rowData_ForOneBot['bot_id']) +':'+ str(rowData_ForOneBot['light_lastdelta']) +':'+ str(rowData_ForOneBot['light_total'])
    ###jwc y         rowData_ForOneBot_BotLabel = str(rowData_ForOneBot['bot_id'])
    ###jwc y 
    ###jwc y         window['-GRAPH-'].DrawLine((lastx, rowData_ForOneBot_Y_Old), 
    ###jwc y                                    ###jwc y (x, int(rowData_ForOneBot['light_total'])), 
    ###jwc y                                    (x, rowData_ForOneBot_Y_Now), 
    ###jwc y                                    color='blue', 
    ###jwc y                                    width=1)
    ###jwc y         ###jwc n window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x, rowData_ForOneBot_Y_Now+5), font=('Arial', 6), text_location='right')
    ###jwc y         ###jwc y window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x-5, rowData_ForOneBot_Y_Now+5))
    ###jwc y         ###jwc y window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 10))
    ###jwc y         ###jwc y window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 6))
    ###jwc y         window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4), text_location='center')
    ###jwc y         
    ###jwc y         rowData_ForOneBot['light_total_old'] = rowData_ForOneBot['light_total']
    ###jwc y 
    ###jwc y else:                               # finished drawing full graph width so move each time to make room
    ###jwc y     ###jwc ? 'str' window['-GRAPH-'].Move(-step_size, 0)
    ###jwc y     ###jwc y window['-GRAPH-'].Move(-1*int(step_size), 0)
    ###jwc y     window['-GRAPH-'].Move(-step_size, 0)
    ###jwc y     ###jwc o window['-GRAPH-'].DrawLine((lastx, lasty), (x, y), width=1)
    ###jwc y     ###jwc o window['-GRAPH-'].DrawLine((lastx, lasty+10), (x, y+10), color='green', width=1)
    ###jwc y     ###jwc o window['-GRAPH-'].DrawLine((lastX1, lastY1), (x, int(rowData_ArrayList_OfDictionaryPairs_ForAllBots[0]['light_total'])), color='yellow', width=1)
    ###jwc y 
    ###jwc y     ###jwc on for rowData_ForOneBot in rowData_ArrayList_OfDictionaryPairs_ForAllBots:
    ###jwc y     ###jwc on     ###jwc y window['-GRAPH-'].DrawLine((lastX1, rowData_ForOneBot['light_total_old']), 
    ###jwc y     ###jwc on     window['-GRAPH-'].DrawLine((lastx, rowData_ForOneBot['light_total_old']), 
    ###jwc y     ###jwc on                                ###jwc y (x, int(rowData_ForOneBot['light_total'])), 
    ###jwc y     ###jwc on                                (x, rowData_ForOneBot['light_total']), 
    ###jwc y     ###jwc on                                color='blue', 
    ###jwc y     ###jwc on                                width=1)
    ###jwc y     ###jwc on     rowData_ForOneBot['light_total_old'] = rowData_ForOneBot['light_total']
    ###jwc y 
    ###jwc y 
    ###jwc y     for rowData_ForOneBot in rowData_ArrayList_OfDictionaryPairs_ForAllBots:
    ###jwc y         ###jwc y window['-GRAPH-'].DrawLine((lastX1, rowData_ForOneBot['light_total_old']), 
    ###jwc y         ###jwc n str window['-GRAPH-'].DrawLine((lastx, rowData_ForOneBot['light_total_old']), 
    ###jwc y         ###jwc n window['-GRAPH-'].DrawLine((lastx, int(rowData_ForOneBot['light_total_old'])), 
    ###jwc y         
    ###jwc y         ###jwc o window['-GRAPH-'].DrawLine((lastx, rowData_ForOneBot['light_total_old']), 
    ###jwc y         ###jwc o                            ###jwc y (x, int(rowData_ForOneBot['light_total'])), 
    ###jwc y         ###jwc o                            (x, rowData_ForOneBot['light_total']), 
    ###jwc y         ###jwc o                            color='blue', 
    ###jwc y         ###jwc o                            width=1)
    ###jwc y         rowData_ForOneBot_Y_Now = int( rowData_ForOneBot['light_total'] / graph_Vertical_Divider_Int )
    ###jwc y         rowData_ForOneBot_Y_Old = int( rowData_ForOneBot['light_total_old'] / graph_Vertical_Divider_Int )
    ###jwc y         rowData_ForOneBot_BotLabel = str(rowData_ForOneBot['bot_id'])
    ###jwc y 
    ###jwc y         window['-GRAPH-'].DrawLine((lastx, rowData_ForOneBot_Y_Old), 
    ###jwc y                                    ###jwc y (x, int(rowData_ForOneBot['light_total'])), 
    ###jwc y                                    (x, rowData_ForOneBot_Y_Now), 
    ###jwc y                                    color='blue', 
    ###jwc y                                    width=1)
    ###jwc y         
    ###jwc y         window['-GRAPH-'].DrawText(text=rowData_ForOneBot_BotLabel, location=(x-5, rowData_ForOneBot_Y_Now+5), font=('Arial', 4), text_location='center')
    ###jwc y 
    ###jwc y         rowData_ForOneBot['light_total_old'] = rowData_ForOneBot['light_total']
    ###jwc y 
    ###jwc y     ###jwc ? 'str' x -= step_size
    ###jwc y     ###jwc y x -= int(step_size)
    ###jwc y     x -= step_size
    
    lastx, lasty = x, y
    
    ###jwc y lastX1, lastY1 = x, rowData_ArrayList_OfDictionaryPairs_ForAllBots[0]['light_total']

    ###jwc ? 'str' x += step_size
    ###jwc y x += int(step_size)
    x += step_size

window.close()