import asyncio
import random
from telethon import TelegramClient, Button

# Replace with your own API credentials
api_id = 
api_hash = ''

# The target chat ID
chat_id = 

client = TelegramClient('session', api_id, api_hash)

async def explore_cycle():
    while True:
        try:
            async with client.conversation(chat_id) as conv:
                print("Sending /explore command to the chat...")
                await conv.send_message('/explore')

                # Expect responses from 3 different bots
                responses = []
                for i in range(3):
                    response = await conv.get_response(timeout=10)
                    responses.append(response)

                # Process each response with a 2-second delay between clicks
                for idx, response in enumerate(responses, start=1):
                    print(f"[Response {idx}] {response.text}")
                    if response.buttons:
                        # Flatten the buttons
                        all_buttons = [btn for row in response.buttons for btn in row]
                        if all_buttons:
                            chosen_button = random.choice(all_buttons)
                            print(f"Clicking on random button: {chosen_button.text}")
                            await response.click(text=chosen_button.text)

                            # Wait 2 seconds before clicking the next button
                            await asyncio.sleep(2)
                        else:
                            print("No inline buttons found in this response.")
                    else:
                        print("No inline buttons found in this response.")

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
