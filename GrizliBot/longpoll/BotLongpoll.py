import vk_api
import config

from loguru import logger as log
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class LongPoll:
    log.success("Class [LongPoll] was successfully runned.")

    def __init__(self):
        self.text = None
        self.event = None
        self.from_id = None
        self.peer_id = None
        self.chat_id = None
        self.message = None
        self.message_id = None
        self.vk = vk_api.VkApi(token=config.TOKEN)
        self.lp = self.lp = VkBotLongPoll(self.vk, 221267894)
        self.api = self.vk.get_api()
        LongPoll.longpoll_group(self)

    def search_command(self):
        text = self.text.split("\n")[0].split(" ")[0]
        if text.lower() in ['пинг', '!пинг']: return self.ping()
        if text.lower() in ['обнять', '!обнять']: return self.hug_user()
        if text.lower() in ['связать', '!связать']: return self.bind_user()
        if text.lower() in ['брак', '!брак']: return self.marry_user()

    def longpoll_group(self):
        log.success("Function [longpoll_group] was successfully runned.")
        for event in self.lp.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.event = event.object
                self.message = event.object.message
                self.message_id = event.object.message["id"]
                self.from_id = event.object.message["from_id"]
                self.peer_id = event.object.message["peer_id"]
                self.chat_id = event.chat_id
                self.text = event.object.message["text"]
                self.search_command()