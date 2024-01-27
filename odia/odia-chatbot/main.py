import openai
import discord

# Initialize the Discord client with intents
intents = discord.Intents.default()
intents.message_content = True  # Allow access to message content

client = discord.Client(intents=intents)


# Set up your OpenAI API key
openai.api_key = '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'

# Replace 'YOUR_DISCORD_TOKEN' with the actual token you got from the Discord Developer Portal
TOKEN = 'MTE2MTk3NjkyNjcxODY2ODg0MA.GOoyMj.ukFEMoiS3LRqGbGV5ByGS8P2p9EC4Z2wdi_PK0'

# Define a function to generate Odia responses using GPT-3.5
def generate_in_odia(input_text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=input_text,
        max_tokens=50,
        temperature=0.6,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    return response.choices[0].text.strip()

@client.event
async def on_ready():
    print(f'Bot is ready as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!odia'):
        try:
            response = generate_in_odia(message.content[6:])  # Assuming your function is called generate_in_odia
            await message.channel.send(response)
        except Exception as e:
            await message.channel.send(f"An error occurred: {e}")

# Start the bot
client.run(TOKEN)
