import logging
from asyncio import Protocol, Transport
from enum import Enum
from typing import NoReturn, Optional

from rfb.settings import Settings


class ServerState(Enum):
    INIT = 'init'


class Client:
    def __init__(self, transport: Transport):
        self._transport = transport
        self._peer_name = transport.get_extra_info('peername')
        self._state = ServerState.INIT

    @property
    def transport(self) -> Transport:
        return self._transport

    @property
    def state(self) -> ServerState:
        return self._state

    @state.setter
    def state(self, value: ServerState) -> NoReturn:
        logging.debug("Changing state of %s from %s to %s", self._peer_name, self._state, value)
        self._state = value

    def __str__(self) -> str:
        return f"{self._peer_name[0]}:{self._peer_name[1]}"


class RFBServerProtocol(Protocol):
    def __init__(self, settings: Settings):
        self._settings = settings
        self._client: Optional[Client] = None

    def connection_made(self, transport: Transport):
        peer_name = transport.get_extra_info('peername')
        logging.info("Connection from %s", peer_name)
        self._client = Client(transport)

    def data_received(self, data):
        message = data.decode()
        logging.debug('%s - data received: %s', self._client, message.encode().hex())
