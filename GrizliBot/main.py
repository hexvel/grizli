from os import close

from longpoll.BotLongpoll import LongPoll

from Utils.VkMethods import VkMethods
from Utils.Utils import Functions

from Database.BaseRequests.BaseRequests import Base

from Functions.default_commands import DefaultCommands
from Functions.marriage_module import Marriage


class Main(LongPoll, VkMethods, Functions, DefaultCommands, Base, Marriage):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    Main()