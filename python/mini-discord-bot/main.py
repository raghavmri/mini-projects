# This code will work only on Python version >= 3.10
import discord
import os
from dotenv import load_dotenv


client = discord.Client()  # Create a new client
botPrefix = "!"  # Change this to whatever you want the bot to be called


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    # Get the message content and make it lowercase for easier comparison
    msg_content: str = message.content.lower()
    # If the message starts with the bot prefix
    if msg_content.startswith(botPrefix):
        msg_content = msg_content.replace(botPrefix, "")

        # If the message is from the bot itself, ignore it
        if message.author == client.user:
            return

        # Respond according to the content of the message
        match msg_content:
            case "help":
                await message.channel.send(f'Hello {message.author.mention}! I am a bot that can help you with your daily tasks.\n\n'
                                           f'To use me, just type `{botPrefix}` followed by the command you want to use.\n\n'
                                           f'Commands:\n'
                                           f'`{botPrefix}hello` - Says hello to you.\n'
                                           f'`{botPrefix}help` - Shows this message. \n'
                                           f'`{botPrefix}ping` - Pings the bot to see if it is alive with its latency.')
            case "hello":
                await message.channel.send(f'Hello {message.author.mention}!')

            case "ping":
                await message.channel.send(f'Pong! ping: {round(client.latency * 1000)}ms')


if __name__ == '__main__':
    try:
        load_dotenv()
        TOKEN = os.getenv('DISCORD_TOKEN')
        if TOKEN is None:
            print('DISCORD_TOKEN ENV variable must be set in order to use the program')
            print('Please set the DISCORD_TOKEN variable in the .env file')
            print('No token found, exiting program')
            exit(1)
        client.run(TOKEN)
        print('Bot is running')
    except Exception as e:
        print(e)
