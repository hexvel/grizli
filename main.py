from os import close

from GrizliBot.longpoll.BotLongpoll import LongPoll

from GrizliBot.Utils.VkMethods import VkMethods
from GrizliBot.Utils.Utils import Functions

from GrizliBot.DB.BaseRequests.BaseRequests import Base

from GrizliBot.Functions.user_commands import UserCommands
from GrizliBot.Functions.marriage_module import Marriage


class Main(LongPoll, VkMethods, Functions, UserCommands, Base, Marriage):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    Main()