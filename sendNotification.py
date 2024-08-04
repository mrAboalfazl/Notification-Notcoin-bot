import asyncio
from telethon import TelegramClient,events
from config import API_ID, API_HASH, BOT_TOKEN
from telethon.tl.custom.message import Message
from database import information_user_collection, creat_Document, time

client = TelegramClient("Notcoin send notification bot", API_ID, API_HASH)#.start(bot_token=BOT_TOKEN)


notcoin_pools_notification_message = "pools"
notcoin_bonuses_notification_message = "bonuses"
notcoin_sepicial_offer_notification_message = "specialOffer"

hamster_combo_card_notification_message = "combo card caption"
hamster_code_morse_notification_message = "code morse"
hamster_coin_miniGame_notification_message = "new mini game for coin"


path_combo_card_pic = ".\\ComboCards\\HelloPlay.png"

#Function for send data to user
#pools
async def send_notcoin_pools_notification_message (notificatinMessage) : 
    #await client.start()
    #Find count of our users on database
    countUserBot = information_user_collection.count_documents({'NotcoinUserInformation.pools' : True})
    #Find all users that enable pools notification
    list_notcoin_active_pool_users = information_user_collection.find({'NotcoinUserInformation.pools' : True})
    list_notcoin_active_pool_users = list(list_notcoin_active_pool_users) #cast cursor type to list type
    #Send notification message to all active enable pools users 
    for i in range(countUserBot) :
        tempUser = list_notcoin_active_pool_users[i]
        tempUser = tempUser["userInformation"]["user_id"]
        print(tempUser)
        await client.send_message(tempUser, notificatinMessage)
        
#Bonuses
async def send_notcoin_bonuses_notification_message (notificatinMessage) : 
    #await client.start()
    #Find count of our users on database
    countUserBot = information_user_collection.count_documents({'NotcoinUserInformation.bonuses' : True})
    #Find all users that enable pools notification
    list_notcoin_active_pool_users = information_user_collection.find({'NotcoinUserInformation.bonuses' : True})
    list_notcoin_active_pool_users = list(list_notcoin_active_pool_users) #cast cursor type to list type
    #Send notification message to all active enable pools users 
    for i in range(countUserBot) :
        tempUser = list_notcoin_active_pool_users[i]
        tempUser = tempUser["userInformation"]["user_id"]
        print(tempUser)
        await client.send_message(tempUser, notificatinMessage)

#SpecialOffer
async def send_notcoin_special_offer_notification_message (notificatinMessage) : 
    #Find count of our users on database
    countUserBot = information_user_collection.count_documents({'NotcoinUserInformation.special_offer' : True})
    #Find all users that enable pools notification
    list_notcoin_active_pool_users = information_user_collection.find({'NotcoinUserInformation.special_offer' : True})
    list_notcoin_active_pool_users = list(list_notcoin_active_pool_users) #cast cursor type to list type
    #Send notification message to all active enable pools users 
    for i in range(countUserBot) :
        tempUser = list_notcoin_active_pool_users[i]
        tempUser = tempUser["userInformation"]["user_id"]
        print(tempUser)
        await client.send_message(tempUser, notificatinMessage)


#combo card
async def send_hamster_combo_card_notification_message (notificatinMessage) : 
    #Find count of our users on database
    countUserBot = information_user_collection.count_documents({'HamsterUserInformation.combo_card' : True})
    #Find all users that enable pools notification
    list_hamster_active_combocard_users = information_user_collection.find({'HamsterUserInformation.combo_card' : True})
    list_hamster_active_combocard_users = list(list_hamster_active_combocard_users) #cast cursor type to list type
    #Send notification message to all active enable pools users 
    for i in range(countUserBot) :
        tempUser = list_hamster_active_combocard_users[i]
        tempUser = tempUser["userInformation"]["user_id"]
        print(tempUser)
        await client.send_file(tempUser, path_combo_card_pic, caption = notificatinMessage)

#code morse
async def send_hamster_code_morse_notification_message (notificatinMessage) : 
    #Find count of our users on database
    countUserBot = information_user_collection.count_documents({'HamsterUserInformation.code_morse' : True})
    #Find all users that enable pools notification
    list_hamster_active_combocard_users = information_user_collection.find({'HamsterUserInformation.code_morse' : True})
    list_hamster_active_combocard_users = list(list_hamster_active_combocard_users) #cast cursor type to list type
    #Send notification message to all active enable pools users 
    for i in range(countUserBot) :
        tempUser = list_hamster_active_combocard_users[i]
        tempUser = tempUser["userInformation"]["user_id"]
        print(tempUser)
        await client.send_message(tempUser, notificatinMessage)


# coin mini game
async def send_hamster_coin_miniGame_notification_message (notificatinMessage) : 
    #Find count of our users on database
    countUserBot = information_user_collection.count_documents({'HamsterUserInformation.coin_miniApp' : True})
    #Find all users that enable pools notification
    list_hamster_active_combocard_users = information_user_collection.find({'HamsterUserInformation.coin_miniApp' : True})
    list_hamster_active_combocard_users = list(list_hamster_active_combocard_users) #cast cursor type to list type
    #Send notification message to all active enable pools users 
    for i in range(countUserBot) :
        tempUser = list_hamster_active_combocard_users[i]
        tempUser = tempUser["userInformation"]["user_id"]
        print(tempUser)
        await client.send_message(tempUser, notificatinMessage)



#SendPicture
async def send_photo_with_caption(user_id, photo_path, caption):
    file = await client.upload_file(photo_path)
    await client.send_file(user_id, file, caption=caption)




async def main():
    await client.start(bot_token = BOT_TOKEN)
    
    # Send Notcoin messages
    # await send_notcoin_pools_notification_message(notcoin_pools_notification_message)
    # await send_notcoin_bonuses_notification_message(notcoin_bonuses_notification_message)
    # await send_notcoin_special_offer_notification_message(notcoin_sepicial_offer_notification_message)

    # send Hamster messages
    # await send_hamster_combo_card_notification_message(hamster_combo_card_notification_message)
    # await send_hamster_code_morse_notification_message (hamster_code_morse_notification_message)
    # await send_hamster_coin_miniGame_notification_message(hamster_coin_miniGame_notification_message)
    await client.disconnect()

asyncio.run(main())