import asyncio
import websockets
import json

async def handle_connection(websocket, path):
    while True:
        message = await websocket.recv()

        card_status = {"cardStatus": "accepted"}

        await websocket.send(json.dumps(card_status))

async def main():
    async with websockets.serve(handle_connection, "localhost", 8080):
        await asyncio.Future()  

if __name__ == "__main__":
    asyncio.run(main())