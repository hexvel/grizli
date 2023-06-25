import time
import random

from loguru import logger as log
from constants import Icons, ImagesForRp


class DefaultCommands:
    log.success("Class is running")

    def ping(self):
        ping = time.time() - self.message['date']
        times = abs(round(ping, 4))
        self.send_messages(self.api, self.peer_id, f"{Icons.SETTINGS} PingTime: {times}s.")