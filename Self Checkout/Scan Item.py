import asyncio
import websockets
import json

# Simulating scanned items from the sensor
async def scan_items(websocket, path):
    items = [
        {"name": "Apple", "price": 2.5, "discount": 10},
        {"name": "Banana", "price": 1.2},
        {"name": "Orange", "price": 3.0}
    ]
    for item in items:
        await websocket.send(json.dumps({"item": item}))  # Send item data to the front-end via WebSocket
        await asyncio.sleep(5)  # Simulate scanning delay (5 seconds between each item)

# Start WebSocket server to communicate with the web page
start_server = websockets.serve(scan_items, "localhost", 8080)

# Start the event loop for the WebSocket server
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()