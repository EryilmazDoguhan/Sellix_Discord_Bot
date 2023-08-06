import discord
import requests

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your Discord bot token
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
SELLIX_API_KEY = 'YOUR_SELLIX_API_KEY'

# Replace 'YOUR_CHANNEL_ID' with the ID of the channel where you want to notify admins about sales
NOTIFICATION_CHANNEL_ID = 'YOUR_CHANNEL_ID'

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Check if the message is from the specific channel where the sales notifications should be sent
    if message.channel.id == NOTIFICATION_CHANNEL_ID:
        return

    if message.content.startswith('!verify'):
        # Assuming !verify is the command to give a member role
        role_name = 'Member'  # Replace 'Member' with the name of the role you want to give

        # Check if the user is already verified
        if discord.utils.get(message.author.roles, name=role_name):
            await message.channel.send(f'{message.author.mention} You are already verified.')
            return

        # Call the Sellix API to verify the customer
        sellix_response = requests.get(f'https://sellix.io/api/v1/orders/{message.author.id}', headers={'Authorization': f'Bearer {SELLIX_API_KEY}'})

        if sellix_response.status_code == 200:
            # Assuming the response is in JSON format and contains 'paid' field to indicate a successful sale
            data = sellix_response.json()
            if data['paid']:
                # Find the 'Member' role and assign it to the user
                role = discord.utils.get(message.guild.roles, name=role_name)
                if role:
                    await message.author.add_roles(role)
                    await message.channel.send(f'{message.author.mention} You have been verified as a member!')
                else:
                    await message.channel.send(f'Error: The {role_name} role was not found.')
            else:
                await message.channel.send(f'{message.author.mention} You have not made a successful sale yet.')
        else:
            await message.channel.send(f'Error: Failed to fetch sellix data for {message.author.mention}')

client.run(TOKEN)
