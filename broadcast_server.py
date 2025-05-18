import asyncio
import websockets
import aiohttp
import json

connected_clients = set()


async def broadcast(message, sender_ws=None):
    for client in connected_clients:
        # if client != sender_ws:
        try:
            print(f"Sending to client: {client}")
            await client.send(message)
            print(f"Message sent to client: {client}")
        except Exception as e:
            print(f"Error sending to client: {client} - {e}")


async def handler(websocket, path):
    connected_clients.add(websocket)
    print(f"New client connected. Total clients: {len(connected_clients)}")
    print(f"Connected clients: {connected_clients}")
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            try:
                data = json.loads(message)
                task_id = data.get("task_id")
                print('#' * 10)
                print(task_id)
                print('#' * 10)
                update_text = data.get("update_text")
                user_name = data.get("user_name")
                if task_id and update_text:
                    await broadcast(message, websocket)
                    # Make API call as form-data
                    async with aiohttp.ClientSession() as session:
                        try:
                            API_URL = "http://127.0.0.1:8000/task/"+ str(task_id) +"/task_update/"
                            form_data = aiohttp.FormData()
                            form_data.add_field('update_text', update_text)
                            form_data.add_field('user_name', user_name)

                            async with session.post(f"{API_URL}", data=form_data) as resp:
                                print(f"API Response: {await resp.text()}")
                        except Exception as e:
                            print(f"API call error: {e}")
                else:
                    print("Malformed message received: missing task_id or update")
            except json.JSONDecodeError:
                print("Received non-JSON message, ignoring")
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


async def main():
    server = await websockets.serve(handler, "localhost", 6789)
    print("WebSocket server started on ws://localhost:6789")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
