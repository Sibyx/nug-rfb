import asyncio
import logging

from rfb import version
from rfb.server import RFBServerProtocol
from rfb.settings import Settings


async def main():
    loop = asyncio.get_running_loop()
    settings = Settings()

    # Logging
    logging.getLogger().setLevel(settings.LOG_LEVEL)
    if settings.VERBOSE:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(settings.LOG_FORMAT)
        logging.getLogger().addHandler(stream_handler)

    logging.info("Loading Nug VNC server %s", version.__version__)

    server = await loop.create_server(lambda: RFBServerProtocol(settings), str(settings.HOST), settings.PORT)
    logging.info("Listening on %s:%d", settings.HOST, settings.PORT)

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
