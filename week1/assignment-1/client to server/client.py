import asyncio
import websockets

async def send_message():
    uri = "ws://143.110.252.48:8888"
    async with websockets.connect(uri) as websocket:
        message_to_send = input("Enter your message: ")
        await websocket.send(message_to_send)
        response = await websocket.recv()
        print("Server response:", response)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_message())
