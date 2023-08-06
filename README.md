<h1>Discord Sellix Verification Bot</h1>
This is a Python-based Discord bot that helps automate the verification process for customers who made a successful purchase on Sellix. The bot assigns a designated "Member" role to the verified customers and notifies the server admins about each sale in a specific channel.

<h2>Features</h2>
On-demand verification: Users can use the !verify command to request verification.
Sellix API Integration: The bot utilizes the Sellix API to check the status of a user's purchase and verify their membership.
Role Assignment: If a user has a successful sale on Sellix, they will be assigned the "Member" role in the Discord server.
Admin Notifications: The bot sends a notification to a specific channel whenever a sale is verified.
Requirements
`Python 3.7 or above`
`discord.py library (Install using pip install discord.py)`
`Discord Bot Token (Obtain from the Discord Developer Portal)`
`Sellix API Key (Retrieve from your Sellix account)`
Installation
Clone this repository to your local machine.
Install the required packages using pip:
Copy code
`pip install -r requirements.txt`
`Replace 'YOUR_DISCORD_BOT_TOKEN', 'YOUR_SELLIX_API_KEY', and 'YOUR_CHANNEL_ID' in the code with your actual Discord bot token, Sellix API key, and the channel ID where you want to receive sales notifications.`
Run the bot using the following command:
Copy code
`python bot.py`
<h2>Usage</h2>
Invite the bot to your Discord server and ensure it has the necessary permissions (Read Messages, Manage Roles).
Set up a "Member" role in your Discord server that you want to assign to verified customers.
In the Discord server, users can use the command !verify to request verification.
The bot will check the user's Sellix account using the provided API key and assign the "Member" role if the user has a successful sale.
The bot will notify the admins about each successful sale in the specified channel.
<h2>Notes</h2>
This is a basic example, and you may need to adapt it to your specific requirements.
Consider using environment variables or a configuration file to store sensitive information securely.
Make sure to handle errors and edge cases appropriately for production use.
Feel free to use, modify, and improve this bot according to your needs. If you encounter any issues or have suggestions for improvements, feel free to open an issue or create a pull request! Happy coding! 😄
