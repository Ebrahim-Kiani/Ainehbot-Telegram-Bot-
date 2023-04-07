from email import message
import json
import requests 
import time

while True:
    #getting data from telegram server
    TOKEN = '5427306599:AAEti-xi4FTVdwYIldtSpNxERvStmFyFhfA'
    URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)
    get_cmd= 'getupdates'
    get_data = requests.get( URL + get_cmd )
    json_data = get_data.json()
    
    #Extracting user data
    try:
        user_result = json_data['result']
        user_update_id = user_result[0]['update_id']
        user_chat_id = user_result[0]['message']['chat']['id']
        
        ##make sure is not sticker or gif or...
        message_list = list(user_result[0]['message'])
        
        
        if message_list[4] != 'text':
            delete_URL='?offset={}'.format(user_update_id+1)
            get_data = requests.get( URL + get_cmd + delete_URL )
            continue
        else:
            user_message = user_result[0]['message']['text']
        #if for '/start' Message
        if user_message == '/start':
            user_message = 'The bot has run successfully!!  (maked by Ebrahim_Kiani)'
        
        #send messsage to server
        send_cmd = 'sendMessage'
        send_URL = '?chat_id={}&text={}'.format(user_chat_id , user_message)
        send_data = requests.post(URL + send_cmd + send_URL)
        #delete last chat message
        delete_URL='?offset={}'.format(user_update_id+1)
        get_data = requests.get( URL + get_cmd + delete_URL )
    except:
        pass
    
    time.sleep(0.1)
    
