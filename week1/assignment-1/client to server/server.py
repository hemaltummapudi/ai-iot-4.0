import asyncio
import websockets

async def handle_message(websocket, path):
    async for message in websocket:
        print("Received message:", message)
        response = "Message received successfully!"
        await websocket.send(response)

start_server = websockets.serve(handle_message, "143.110.252.48", 8888)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
