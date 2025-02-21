import asyncio
from telethon import TelegramClient, Button

# Replace with your own API credentials from https://my.telegram.org
api_id = 1331814       # e.g., 1234567
api_hash = 'b507dd65bfa82f9c2c7b5f2e75eba696' # e.g., '0123456789abcdef0123456789abcdef'

# The target chat ID where everything will happen
chat_id = -1002289772556

client = TelegramClient('session', api_id, api_hash)

async def explore_cycle():
    while True:
        try:
            # Open a conversation with the target chat
            async with client.conversation(chat_id) as conv:
                print("Sending /explore command to the chat...")
                await conv.send_message('/explore')
                
                # Wait for the bot's response (adjust timeout as needed)
                response = await conv.get_response(timeout=10)
                print("Received response from chat:")
                print(response.text)
                
                # Check if the message has inline buttons
                if response.buttons:
                    print("Found inline buttons:")
                    for row in response.buttons:
                        for btn in row:
                            print(" -", btn.text)
                    
                    # Search for the button containing "New Zealand" (case insensitive)
                    chosen_button = None
                    for row in response.buttons:
                        for btn in row:
                            if "new zealand" in btn.text.lower():
                                chosen_button = btn
                                break
                        if chosen_button:
                            break
                    
                    if chosen_button:
                        print(f"Clicking on button: {chosen_button.text}")
                        # Use the message object's click() method:
                        await response.click(text=chosen_button.text)
                    else:
                        print("No button containing 'New Zealand' was found.")
                else:
                    print("No inline buttons found in the response.")
        
        except Exception as e:
            print("An error occurred:", e)
        
        print("Waiting for 310 seconds before the next command...\n")
        await asyncio.sleep(310)

async def main():
    await client.start()
    print("Client started and logged in successfully.")
    await explore_cycle()

with client:
    client.loop.run_until_complete(main())
