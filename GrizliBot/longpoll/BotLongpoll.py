import vk_api
from constants import DATA

from vk_api import VkUpload
from loguru import logger as log
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class LongPoll:
    log.success("Class is running")

    def __init__(self):
        self.text = ...
        self.event = ...
        self.from_id = ...
        self.peer_id = ...
        self.chat_id = ...
        self.message = ...
        self.message_id = ...
        self.vk = vk_api.VkApi(token=DATA.TOKEN)
        self.lp = self.lp = VkBotLongPoll(self.vk, 221267894)
        self.api = self.vk.get_api()
        self.upl = VkUpload(self.vk)
        

    def search_prefix(self):
        try:
            return self.text[0]
        except:
            return None

    def search_command(self, prefix=False):
        if prefix:
            text = self.text.split("\n")[0].split(" ")[0]
            command = text.replace(text[0], "").lower()
        else:
            command = text = self.text.split("\n")[0].lower()

        if command in ['пинг']: return self.ping()
        if command in ['обнять']: return self.hug_user()
        if command in ['связать']: return self.bind_user()
        if command in ['поцеловать']: return self.kiss_user()
        if command in ['ударить']: return self.hit_user()
        if command in ['накормить']: return self.feed_user()
        if command in ['брак']: return self.marry_user()
        if command in ['тест']: return self.get_voice_from_audio()

    def longpoll_group(self):
        log.success("Function running")

        for event in self.lp.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.event = event.object
                self.message = event.object.message
                self.message_id = event.object.message["id"]
                self.from_id = event.object.message["from_id"]
                self.peer_id = event.object.message["peer_id"]
                self.chat_id = event.chat_id
                self.text = event.object.message["text"]

                prefix = self.search_prefix()
                if prefix is not None and prefix in ["!", ".", "/"]:
                    self.search_command(prefix=True)
                else:
                    self.search_command(prefix=False)