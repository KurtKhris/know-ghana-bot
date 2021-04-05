# load environment
import os
from dotenv import load_dotenv
import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

load_dotenv()

updater = Updater(token=os.getenv('TELEGRAM_TOKEN'), use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

stages = [
  "start",
  "start.number_of_regions",
  "start.regions",
  "start.number_of_constituencies",
  "start.constituencies",
  #"start.contact",
]

userStages = {} # database
response = requests.get("http://ghdata.herokuapp.com/regions/")
response1 = requests.get("http://ghdata.herokuapp.com/constituencies")


#print(response.status_code) #200

#print(response.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# jprint(response1.json())

data = response.json()['data']
#jprint(data)
regions = []

for d in data:
    
    reg = d['name']
    regions.append(reg)

#print(regions)

constituencies_data = response1.json()['data']
#jprint(data)
constituencies = [x['name'] for x in constituencies_data]
constituencies_rc = [x['regionCode'] for x in constituencies_data]
groups = {}
for x in constituencies_data:
    key= constituencies
    value = constituencies_rc
    for i in value.items():
        print(i)
    if key not in groups :
        groups.update({key:[value] })   
        if key in groups:
            groups[key].append(value)     
print(groups)

# for d in constituencies_data:
    
#     reg = d['name']
#     constituencies.append(reg)
    
print(len(constituencies)) 
def setStage(user, stage):
    userStages[user] = stage
  # print(userStages)

def clearStage(user):
    userStages.pop(user)
  # print(userStages)

def start(update, context):
    user = update.effective_user.id # id of the user who sent the message
    context.bot.send_message(chat_id=update.effective_chat.id, text="""
    Welcome to Know Ghana Bot. What do you want to know  about Ghana?
    
    A. Number of Regions
    B. All Regions
    C. Number of Constituencies
    D. All constituencies

    reply Exit to end session anywhere
  """
  )
    setStage(user, "start")

def stop(update, context):
    user = update.effective_user.id
    context.bot.send_message(chat_id=update.effective_chat.id, text="""
    Thank you for contacting me today.
  """)
    clearStage(user)

def sendInvalid(update, context):
      context.bot.send_message(chat_id=update.effective_chat.id, text="""
    Please enter a valid response
  """
  )

def startResponse(update, context):
    text = update.message.text.lower()
    if text == "a":
        startNumberRegionsResponse(update, context)
    elif text == "b":
        startRegionsResponse(update, context)
    elif text == "c":
        startNumberConstituenciesResponse(update, context)
    elif text == "d":
        startConstituenciesResponse(update, context)
    else:
        sendInvalid(update, context) 

          
def startNumberRegionsResponse(update, context):
    user = update.effective_user.id
    setStage(user, "start.number_of_regions")
    
        
    context.bot.send_message(chat_id=update.effective_chat.id, text="There are {} regions in Ghana.".format(len(regions)))
    stop(update, context)
    
def startRegionsResponse(update, context):
    user = update.effective_user.id
    setStage(user, "start.regions")
    context.bot.send_message(chat_id=update.effective_chat.id, text="The regions in Ghana are: ")
    
    for i in regions:
        context.bot.send_message(chat_id=update.effective_chat.id, text=i)
            
    stop(update, context)
    
def startNumberConstituenciesResponse(update, context):
    user = update.effective_user.id
    setStage(user, "start.number_of_constituencies")
    
        
    context.bot.send_message(chat_id=update.effective_chat.id, text="There are {} constituencies in Ghana.".format(len(constituencies)))
    stop(update, context)

def startConstituenciesResponse(update, context):
    user = update.effective_user.id
    setStage(user, "start.constituencies")
    context.bot.send_message(chat_id=update.effective_chat.id, text="The constituencies in Ghana are: ")

    # def chunk_using_generators(lst, n):
    #     for i in range(0, len(lst), n):
    #         yield lst[i:i + n]
    # chunk = list(chunk_using_generators(constituencies, 25))
    # data = "".join("\n{}".format(x) for x in chunk[0]) 
    # data1 = "".join("\n{}".format(x) for x in chunk[1]) 
    # data2 = "".join("\n{}".format(x) for x in chunk[2]) 
    # data3 = "".join("\n{}".format(x) for x in chunk[3]) 
    # data4 = "".join("\n{}".format(x) for x in chunk[4]) 
    # data5 = "".join("\n{}".format(x) for x in chunk[5]) 
    # data6 = "".join("\n{}".format(x) for x in chunk[6]) 
    # data7 = "".join("\n{}".format(x) for x in chunk[7]) 
    # data8 = "".join("\n{}".format(x) for x in chunk[8]) 
    # data9 = "".join("\n{}".format(x) for x in chunk[9]) 
    # data10 = "".join("\n{}".format(x) for x in chunk[10])  
    # line_count = 0.
    # for line in data:
    #     if line != "\n":
    #         line_count += 1
    # print(line_count)
    #print(data)
    # for c in constituencies:
    # context.bot.send_message(chat_id=update.effective_chat.id, text=data)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=data1)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=data2)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=data3)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=data4)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=data5)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=data6)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=data7)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=data8)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=data9)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=data10)

    stop(update, context)

    
    #stop(update, context)
    
def message(update, context):
    user = update.effective_user.id
    text = update.message.text.lower()

    if(text == "exit"):
        stop(update, context)
    else:
        if user in userStages:
            stage = userStages[user] # get the particular user's stage
            if(stage == "start"):
                startResponse(update, context)
            if(stage == "start.number_of_regions"):
                startNumberRegionsResponse(update, context)
            if(stage == "start.number_of_constituencies"):
                startNumberConstituenciesResponse(update, context)
#       if(stage == "start.next_vacination_date"):
#         startNextVacinationDateResponse(update, context)
#       # if(stage == "start.vacination_code"):
#       #   startVacinationCodeResponse(update, context)
        else:
            start(update, context) 
message_handler = MessageHandler(Filters.text & (~Filters.command), message)
dispatcher.add_handler(message_handler)

updater.start_polling()
  


