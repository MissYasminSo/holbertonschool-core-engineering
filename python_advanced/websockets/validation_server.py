#!/usr/bin/env python3

import asyncio

from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed


async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
            print(message)
        except ConnectionClosed:
            return


async def main():
    server = await serve(handler, "", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
