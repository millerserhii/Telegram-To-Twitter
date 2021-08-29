import os
import tweepy
from dotenv import load_dotenv
from telethon import TelegramClient, events


load_dotenv()

'''Target channel name'''
CHANNEL_NAME = os.environ['TG_CHANNEL_NAME']

'''Telegram API credentials'''
API_ID = int(os.environ['api_id'])
API_HASH = os.environ['api_hash']

'''Twitter API credentials'''
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

'''extra message in the end of the tweet'''
extra_msg = os.environ['more_msg']

'''Building telegram client'''
client = TelegramClient('my_account', API_ID, API_HASH)

'''Building Twitter client'''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


def post_tweet(text):
    """Post tweet func"""
    api.update_status(text)


def upload_media(text, filename):
    """Post tweet with image"""
    media = api.media_upload(filename)
    api.update_status(text, media_ids=[media.media_id_string])


@client.on(events.NewMessage)  # wait for new msg
async def my_event_handler(event):
    """Handle incoming messages"""
    try:
        if event.chat.username == CHANNEL_NAME:  # Check if msg is from target channel
            chat = await event.get_input_chat()
            async for message in client.iter_messages(chat.channel_id, limit=1):
                msg_text = message.raw_text
                msg_photo = message.photo
                result_msg = msg_text[:200] + "\n\n" + extra_msg  # cut msg to 200 symbols and add an extra msg
                if msg_photo is None:   # check if msg was with image
                    post_tweet(result_msg)    # posting tweet without image
                else:
                    await message.download_media('photo.jpg')   # downloading img and saving it into main folder
                    upload_media(result_msg, 'photo.jpg')   # posting tweet with image

    except Exception as e:
        print(f'Error - {e}')


client.start()  # starting client
client.run_until_disconnected()  # keep the client active
