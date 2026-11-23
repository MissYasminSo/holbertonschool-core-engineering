#!/usr/bin/env python3

import asyncio

from websockets.asyncio.server import serve

connected_clients = set()


async def handler(websocket):
    while True:
        connected_clients.add(websocket)

        try:
            message = await websocket.recv()
            await websocket.send(message)
        finally:
            connected_clients.remove(websocket)


async def main():
    server = await serve(handler, "", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
