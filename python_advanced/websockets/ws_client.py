#!/usr/bin/env python3


import asyncio
from websockets.asyncio.client import connect


async def connect_and_send(url: str, text: str) -> str:
    async with connect(url) as websocket:
        await websocket.send(text)
        message = await websocket.recv()
        await websocket.close()
        return message

async def main():
    message = await connect_and_send("ws://localhost:8765", "Hello world!")
    print(message)


if __name__ == "__main__":
    asyncio.run(main())
