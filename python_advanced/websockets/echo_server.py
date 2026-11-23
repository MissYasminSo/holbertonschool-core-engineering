#!/usr/bin/env python

import asyncio

from websockets.asyncio.server import serve


async def handler(websocket):
    while True:
        message = await websocket.recv()
        await websocket.send(message)
        print(message)


async def main():
    server = await serve(handler, "", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
