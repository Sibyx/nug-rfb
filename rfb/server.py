import logging
from asyncio import Protocol, Transport
from enum import Enum
from typing import NoReturn


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
        logging.debug("Changing state of {} from {} to {}", self._peer_name, self._state, value)
        self._state = value


class RFBServerProtocol(Protocol):
    def __init__(self):
        self._clients = {}

    def connection_made(self, transport: Transport):
        peer_name = transport.get_extra_info('peername')
        logging.info("Connection from {}", peer_name)
        self._clients[peer_name] = Client(transport)

    def data_received(self, data):
        message = data.decode()
        logging.debug('Data received: {!r}', message)
