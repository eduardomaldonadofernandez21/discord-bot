import discord, os, requests, json
from dotenv import load_dotenv

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

load_dotenv()

my_token = os.getenv("MY_TOKEN_DISCORD")
my_key = os.getenv("API_KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user: #  if the bot is the one sending the message in the chat. We don’t want the bot to keep responding to its own messages
            return
        
        if message.content.startswith('$meme'): # Special keyword for our MemeBot
            await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(my_token) # Replace with your own token.