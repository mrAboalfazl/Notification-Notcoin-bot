from telethon import TelegramClient, events
from config import API_ID, API_HASH, BOT_TOKEN
from telethon.tl.custom.message import Message
from telethon import Button
from database import information_user_collection, creat_Document, time

client = TelegramClient("Notcoin main core Notification bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

###
#Handle Start message and send greeting message
@client.on(events.NewMessage(func= lambda e: e.is_private ,pattern=r'/start'))
async def start(event):
    user = await event.get_sender()
    from telethon import TelegramClient, events

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    #Get user information and insert them to Database mongoDB
    user = await event.get_sender()
    
    user_data = {
        "userInformation" :
        {
        "user_id" : user.id,
        "username" : user.username,
        "first_name" : user.first_name,
        "last_name" : user.last_name,
        "language" : user.lang_code,
        "is_premium" : user.premium,
        "is_bot" : user.bot,
        "restricted" : user.restricted,
        "date_enter_bot" : time.time(),
        },
        "NotcoinUserInformation" : 
        {
            "pools" : False,
            "bonuses" : False,
            "special_offer" : False,
        },
        "HamsterUserInformation" :
        {
            "combo_card" : False,
            "code_morse" : False,
            "coin_miniApp" : False
        }
    }

    #Count of Keys user_data
    lengthUserData = len(list(user_data.keys()))

    try:
        # Check if user already exists
        existing_user = information_user_collection.find_one({'userInformation.user_id': user_data["userInformation"]["user_id"]})
        if existing_user:
            print("this user existing")
            #information_user_collection.update_one({'user_id': user_data['user_id']}, {'$set': user_data})
        else:
            # Insert new user data
            creat_Document(user_data)
    except Exception as err:
        print(f"Error saving user data: {err}")
#End add user to database
###########################################################################

    #Make keyboard button
    markup_notcoin = client.build_reply_markup(
        [
            [
                Button.text("Notcoin", resize = True)
            ],
            [
                Button.text("Hamster",resize = True),
                Button.text("Blum",resize = True)
            ]
        ]
    )
    await event.respond("Hey!😊 Welcom to Notcoin notifications BOT👍", buttons = markup_notcoin)
#End handle "/start"
###############################################################################

###
#Handle keyboard button "Notcoin" and set CallBackQuery for inline button
@client.on(events.NewMessage(func= lambda e: e.is_private ,pattern=r"Notcoin"))
async def start_detail_notcoin(event):
    markup_notcoin_detail = main_notcoin_menue(event)
    await event.respond("**What parts do you want to enable or disable notification : **", parse_mode = "md", buttons = markup_notcoin_detail)
#End Handle text "Notcoin"

#Handle keyboard button "Hamster" and set CallBackQuery for inline button
@client.on(events.NewMessage(func= lambda e: e.is_private ,pattern=r"Hamster"))
async def start_detail_hamster(event):
    markup_hamster_detail = main_hamster_menue(event) 
    await event.respond("**What parts do you want to enable or disable notification : **", parse_mode = "md", buttons = markup_hamster_detail)
#End Handle text "hamster"

#Handle keyboard button "Blum" and set CallBackQuery for inline button
@client.on(events.NewMessage(func= lambda e: e.is_private ,pattern=r"Blum"))
async def start_detail_blum(event):
    #markup_blum_detail = main_blum_menue(event) 
    await event.respond("**Coming Sooooooooon!**", parse_mode = "md")#, buttons = markup_hamster_detail)
#End Handle text "Blum"
###############################################################################



###
#CallBackQuery menue Handelling notcoin
#call back query active pools
@client.on(event = events.CallbackQuery(data = "active_pools_click")) 
async def callbackquery_active_pool (event : events.CallbackQuery.Event) : 
    print(event.reply)
    markup_notcoin_activation_mode = client.build_reply_markup(
        [
            [
                Button.inline(text = "Enable✅", data = "enable_notif_active_pools_click"),
                Button.inline(text = "Disable❌", data = "disable_notif_active_pool_click")
            ],
            [
                Button.inline(text = "⬅️Back", data = "back_notcoin_click")
            ]
        ]

    )
    await event.edit(text = "**You can enable/disable notification Activ pools Notcoin :**",parse_mode = "md",buttons = markup_notcoin_activation_mode)

#call back query active bounses
@client.on(event = events.CallbackQuery(data = "active_bounses_click")) 
async def callbackquery_active_bonuses (event : events.CallbackQuery.Event) : 
    print(event.reply)
    markup_notcoin_activation_mode = client.build_reply_markup(
        [
            [
                Button.inline(text = "Enable✅", data = "enable_notif_active_bonuses_click"),
                Button.inline(text = "Disable❌", data = "disable_notif_active_bonuses_click")
            ],
            [
                Button.inline(text = "⬅️Back", data = "back_notcoin_click")
            ]
        ]

    )
    await event.edit(text = "**You can enable/disable notification Activ Bonuses Notcoin :**",parse_mode = "md",buttons = markup_notcoin_activation_mode)


#call back query special offer
@client.on(event = events.CallbackQuery(data = "special_offer_click")) 
async def callbackquery_special_offer (event : events.CallbackQuery.Event) : 
    print(event.reply)
    markup_notcoin_activation_mode = client.build_reply_markup(
        [
            [
                Button.inline(text = "Enable✅", data = "enable_notif_active_special_offer_click"),
                Button.inline(text = "Disable❌", data = "disable_notif_active_special_offer_click")
            ],
            [
                Button.inline(text = "⬅️Back", data = "back_notcoin_click")
            ]
        ]

    )
    await event.edit(text = "**You can enable/disable notification special offer Notcoin :**",parse_mode = "md",buttons = markup_notcoin_activation_mode)


#call back query all notif
@client.on(event = events.CallbackQuery(data = "all_notif_click")) 
async def callbackquery_all_notif_notcoin (event : events.CallbackQuery.Event) : 
    print(event.reply)
    markup_notcoin_activation_mode = client.build_reply_markup(
        [
            [
                Button.inline(text = "Enable✅", data = "enable_notif_all_notif_click"),
                Button.inline(text = "Disable❌", data = "disable_notif_all_notif_click")
            ],
            [
                Button.inline(text = "⬅️Back", data = "back_notcoin_click")
            ]
        ]
    )
    await event.edit(text = "**You can enable/disable all notification Notcoin :**",parse_mode = "md",buttons = markup_notcoin_activation_mode)

#call back query active back button
@client.on(events.CallbackQuery(data="back_notcoin_click"))
async def callbackquery_button_back (event: events.CallbackQuery.Event): 
    # await start_detail_notcoin(event)
    markup_notcoin_detail = main_notcoin_menue(event)
    await event.edit("**What parts do you want to enable or disable notification : **", parse_mode = "md", buttons = markup_notcoin_detail)

#End CallBackQuery handeling notcoin
###############################################################################












###
#CallBackQuery menue Handelling hamster
#call back query combo card
@client.on(event = events.CallbackQuery(data = "active_combo_click")) 
async def callbackquery_active_comboCard (event : events.CallbackQuery.Event) : 
    print(event.reply)
    markup_notcoin_activation_mode = client.build_reply_markup(
        [
            [
                Button.inline(text = "Enable✅", data = "enable_notif_active_comboCard_click"),
                Button.inline(text = "Disable❌", data = "disable_notif_active_comboCard_click")
            ],
            [
                Button.inline(text = "⬅️Back", data = "back_hamster_click")
            ]
        ]

    )
    await event.edit(text = "**You can enable/disable notification combo card Hamster :**",parse_mode = "md",buttons = markup_notcoin_activation_mode)

#call back query code morse
@client.on(event = events.CallbackQuery(data = "active_morse_click")) 
async def callbackquery_active_code_morse (event : events.CallbackQuery.Event) : 
    print(event.reply)
    markup_notcoin_activation_mode = client.build_reply_markup(
        [
            [
                Button.inline(text = "Enable✅", data = "enable_notif_active_morse_click"),
                Button.inline(text = "Disable❌", data = "disable_notif_active_morse_click")
            ],
            [
                Button.inline(text = "⬅️Back", data = "back_hamster_click")
            ]
        ]

    )
    await event.edit(text = "**You can enable/disable notification Activ code morse Hamster :**",parse_mode = "md",buttons = markup_notcoin_activation_mode)


#call back query coin mini game
@client.on(event = events.CallbackQuery(data = "active_coin_miniGame_click")) 
async def callbackquery_coin_miniGame (event : events.CallbackQuery.Event) : 
    print(event.reply)
    markup_notcoin_activation_mode = client.build_reply_markup(
        [
            [
                Button.inline(text = "Enable✅", data = "enable_notif_active_coin_miniGame_click"),
                Button.inline(text = "Disable❌", data = "disable_notif_active_coin_miniGame_click")
            ],
            [
                Button.inline(text = "⬅️Back", data = "back_hamster_click")
            ]
        ]

    )
    await event.edit(text = "**You can enable/disable notification coin mini game hamster :**",parse_mode = "md",buttons = markup_notcoin_activation_mode)


#call back query all notif hamster
@client.on(event = events.CallbackQuery(data = "all_notif_hamster_click")) 
async def callbackquery_all_notif_hamster (event : events.CallbackQuery.Event) : 
    print(event.reply)
    markup_notcoin_activation_mode = client.build_reply_markup(
        [
            [
                Button.inline(text = "Enable✅", data = "enable_all_notif_hamster_click"),
                Button.inline(text = "Disable❌", data = "disable_all_notif_hamster_click")
            ],
            [
                Button.inline(text = "⬅️Back", data = "back_hamster_click")
            ]
        ]
    )
    await event.edit(text = "**You can enable/disable all notification hamster :**",parse_mode = "md",buttons = markup_notcoin_activation_mode)

#call back query active back button hamster
@client.on(events.CallbackQuery(data="back_hamster_click"))
async def callbackquery_button_back (event: events.CallbackQuery.Event): 
    # await start_detail_notcoin(event)
    markup_hamster_detail = main_hamster_menue(event)
    await event.edit("**What parts do you want to enable or disable notification : **", parse_mode = "md", buttons = markup_hamster_detail)

#End CallBackQuery
###############################################################################
















###
#Call back Query Enable/Disable Alarms Notcoins

#call back queries pools notcoin
#Enable
@client.on(events.CallbackQuery(data = "enable_notif_active_pools_click"))
async def callbackquery_notcoin_enable_pools (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "NotcoinUserInformation.pools": True
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")

    await event.reply("You enable notification pools Notcoin✅")
#Disable
@client.on(events.CallbackQuery(data = "disable_notif_active_pool_click"))
async def callbackquery_notcoin_disable_pools (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "NotcoinUserInformation.pools": False
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You disable notification pools Notcoin❌")









#call back queries bonuses notcoin
#Enable
@client.on(events.CallbackQuery(data = "enable_notif_active_bonuses_click"))
async def callbackquery_notcoin_enable_bonuses (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "NotcoinUserInformation.bonuses": True
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You enable notification bonuses Notcoin✅")
#Disable
@client.on(events.CallbackQuery(data = "disable_notif_active_bonuses_click"))
async def callbackquery_notcoin_disable_bonuses (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "NotcoinUserInformation.bonuses": False
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You disable notification bonuses Notcoin❌")









#call back queries special offer notcoin
#Enable
@client.on(events.CallbackQuery(data = "enable_notif_active_special_offer_click"))
async def callbackquery_notcoin_enable_special_offer (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "NotcoinUserInformation.special_offer": True
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You enable notification special offer Notcoin✅")
#Disable
@client.on(events.CallbackQuery(data = "disable_notif_active_special_offer_click"))
async def callbackquery_notcoin_disable_special_offer (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "NotcoinUserInformation.special_offer": False
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You disable notification special offer Notcoin❌")











#call back queries all notcoin
#Enable
@client.on(events.CallbackQuery(data = "enable_notif_all_notif_click"))
async def callbackquery_notcoin_enable_all (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "NotcoinUserInformation.bonuses": True,
            "NotcoinUserInformation.special_offer": True,
            "NotcoinUserInformation.pools": True
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You enable all notification Notcoin✅")
#Disable
@client.on(events.CallbackQuery(data = "disable_notif_all_notif_click"))
async def callbackquery_notcoin_disable_all (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "NotcoinUserInformation.bonuses": False,
            "NotcoinUserInformation.special_offer": False,
            "NotcoinUserInformation.pools": False
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You disable all notification Notcoin❌")


#End call back query alarms notcoin
###############################################################################









###
#Call back Query Enable/Disable Alarms Hmaster

#call back queries combo card hamster
#Enable
@client.on(events.CallbackQuery(data = "enable_notif_active_comboCard_click"))
async def callbackquery_hamster_enable_combo_card (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "HamsterUserInformation.combo_card": True
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")

    await event.reply("You enable notification combo card Hamster✅")
# #Disable
@client.on(events.CallbackQuery(data = "disable_notif_active_comboCard_click"))
async def callbackquery_hamster_disable_combo_card (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "HamsterUserInformation.combo_card": False
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You disable notification combo card Hamster❌")









#call back queries bonuses notcoin
#Enable
@client.on(events.CallbackQuery(data = "enable_notif_active_morse_click"))
async def callbackquery_hamster_enable_code_morse (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "HamsterUserInformation.code_morse": True
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You enable notification code morse Hamster✅")
#Disable
@client.on(events.CallbackQuery(data = "disable_notif_active_morse_click"))
async def callbackquery_hamster_disable_code_morse (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "HamsterUserInformation.code_morse": False
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You disable notification code morse Hamster❌")







#call back queries coin mini app hamster
#Enable
@client.on(events.CallbackQuery(data = "enable_notif_active_coin_miniGame_click"))
async def callbackquery_notcoin_enable_special_offer (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "HamsterUserInformation.coin_miniApp": True
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You enable notification coin mini app Hamster✅")
#Disable
@client.on(events.CallbackQuery(data = "disable_notif_active_coin_miniGame_click"))
async def callbackquery_notcoin_disable_special_offer (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "HamsterUserInformation.coin_miniApp": False
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You disable notification coin mini app Hamster❌")











#call back queries all hamster
#Enable
@client.on(events.CallbackQuery(data = "enable_all_notif_hamster_click"))
async def callbackquery_hamster_enable_all (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "HamsterUserInformation.combo_card": True,
            "HamsterUserInformation.code_morse": True,
            "HamsterUserInformation.coin_miniApp": True
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You enable all notification Hamster✅")
#Disable
@client.on(events.CallbackQuery(data = "disable_all_notif_hamster_click"))
async def callbackquery_hamster_disable_all (event: events.CallbackQuery.Event): 
    user_doc_id = find_documentID(event.sender_id)
    if user_doc_id :
        user_doc_id = {"_id": user_doc_id} 
        update_data = {
        "$set": {
            "HamsterUserInformation.combo_card": False,
            "HamsterUserInformation.code_morse": False,
            "HamsterUserInformation.coin_miniApp": False
            }
        }
        result = information_user_collection.update_one(user_doc_id, update_data)
        print(result)
    else:
        print("I can't find document of user")
    await event.reply("You disable all notification Hamster❌")


# #End call back query alarms hamster
# ###############################################################################













#Functions key menue notcoin
def main_notcoin_menue(event) :
    return client.build_reply_markup(
        [[
            Button.inline(text = "Pools", data = "active_pools_click")
        ],
        [
            Button.inline(text = "Bonuses", data = "active_bounses_click")
        ],
        [
            Button.inline(text = "Special Offer", data = "special_offer_click")
        ],
        [
            Button.inline(text = "All", data = "all_notif_click")
        ]]
    )
#Functin define main menue notcoin

#Functions key menue hamster
def main_hamster_menue(event) :
    return client.build_reply_markup(
        [[
            Button.inline(text = "Combo card", data = "active_combo_click")
        ],
        [
            Button.inline(text = "Code morse", data = "active_morse_click")
        ],
        [
            Button.inline(text = "Coin mini game", data = "active_coin_miniGame_click")
        ],
        [
            Button.inline(text = "All", data = "all_notif_hamster_click")
        ]]
    )
#Functin define main menue hamster


#Function Find document ID _id
def find_documentID(userID) : 
    print(userID)
    document = information_user_collection.find_one({"userInformation.user_id": userID})

    if document:
        object_id = document["_id"]
        print(f"ObjectId for user_id {userID}: {object_id}")
        return object_id
    else:
        print(f"No document found for user_id {userID}")
        return None
#End Function find doc id(_id)

###############################################################################

#Run Bot and keep alive
client.start()
client.run_until_disconnected()


information_user_collection.insert_update