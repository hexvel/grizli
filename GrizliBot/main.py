from threading import Thread

from longpoll.BotLongpoll import LongPoll

from Utils.VkMethods import VkMethods
from Utils.Utils import Functions

from Database.BaseRequests.BaseRequests import Base

from Functions.default_commands import DefaultCommands
from Functions.marriage_module import Marriage
from Functions.rp_commands import RpCommands

from threading import Thread


class Main(LongPoll, VkMethods, Functions, DefaultCommands, Base, Marriage,
           RpCommands):
    pass


if __name__ == '__main__':
    main = Main().longpoll_group
    Thread(target=main).start()