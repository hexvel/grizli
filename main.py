from GrizliBot.longpoll.BotLongpoll import LongPoll

from GrizliBot.Utils.VkMethods import VkMethods
from GrizliBot.Utils.Utils import Functions

from GrizliBot.Functions.user_commands import UserCommands

class Main(LongPoll, VkMethods, Functions, UserCommands):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    Main()