from threading import Thread
from typing import Any

from longpoll.BotLongpoll import LongPoll

from Utils.VkMethods import VkMethods
from Utils.Utils import Functions
from Utils.API import VK

from Database.BaseRequests.BaseRequests import Base

from Functions.default_commands import DefaultCommands
from Functions.marriage_module import Marriage
from Functions.rp_commands import RpCommands


class Main(LongPoll, VkMethods, Functions, DefaultCommands,
           Base, Marriage, RpCommands, VK):
    def __init__(self): super().__init__()


if __name__ == '__main__':
    main = Main()
    Thread(target=main.longpoll_group).start()