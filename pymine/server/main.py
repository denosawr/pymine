#!/usr/bin/env python3

import asyncio

from typing import List, Dict, Tuple, Sequence

from pymine.server.connectors import MinecraftConnector, WSBridgeConnector
from pymine.utils.logging import getLogger

log = getLogger("main")
log.setLevel("INFO")


def start_server(port: int = 19131):
    log.info("Server started.")
    send_queue = asyncio.Queue()
    recv_queue = asyncio.Queue()

    minecraft_connection = MinecraftConnector(
        send_queue, recv_queue, port=19131
    )
    ws_connection = WSBridgeConnector(send_queue, recv_queue)

    loop = asyncio.get_event_loop()
    try:
        minecraft_connection.start(loop)
        ws_connection.start(loop)

        log.debug("Starting event loop...")
        loop.run_forever()
    except KeyboardInterrupt:
        log.info("KeyboardInterrupt, closing...")


if __name__ == "__main__":
    start_server()
