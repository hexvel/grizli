from os import close

from GrizliBot.Longpoll.BotLongpoll import LongPoll

from GrizliBot.Utils.VkMethods import VkMethods
from GrizliBot.Utils.Utils import Functions

from GrizliBot.Database.BaseRequests.BaseRequests import Base

from GrizliBot.Functions.default_commands import DefaultCommands
from GrizliBot.Functions.marriage_module import Marriage


class Main(LongPoll, VkMethods, Functions, DefaultCommands, Base, Marriage):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    Main()