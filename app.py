import asyncio

from rfb.server import RFBServerProtocol


async def main():
    loop = asyncio.get_running_loop()

    server = await loop.create_server(lambda: RFBServerProtocol(), '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
