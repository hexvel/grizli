import time

from loguru import logger


class Functions:
    logger.success("Class [Functions] was successfully runned.")
    time.sleep(0.1)

    def delete_elements(self, text: str, elements: list) -> str:
        """
        :param text: str
        :param elements: list
        :rtype: str
        """
        for del_element in elements:
            text = str(text).replace(f"{del_element}", "")
        return text

    def search_text(self) -> str:
        text = self.api.messages.getById(message_ids=self.message_id)
        if text.get("reply_message"):
            return str(text['items'][0]['reply_message']['text'])
        else:
            return str(text['items'][0]['reply_message']['text'])

    def text_validator_by_command(self, data: str):
        NICE_COMMANDS = ['шаб', 'пинг']
        if data in NICE_COMMANDS:
            return True
        return False
    
    def get_user_info(self, user_id: int):
        user_info = self.api.users.get(user_ids=user_id, fields="sex")
        return user_info[0]

    def _member_id(self, pos: int = 1) -> int:
        """
        :param pos: int
        :rtype: int
        """
        try:
            text = self.text.split('\n', maxsplit=5)[0].split(" ", maxsplit=5)
        except:
            return self.from_id
        if 'reply_message' not in self.message:
            if len(text) > pos:
                akk_id = text[pos]
                if "vk.com/id" in akk_id:
                    try:
                        return int(akk_id.partition('id')[2])
                    except:
                        return self.from_id
                elif "vk.com/" in akk_id:
                    try:
                        return int(self.api.users.get(user_ids=akk_id.partition('com/')[2])[0]["id"])
                    except:
                        return self.from_id
                else:
                    try:
                        return int(akk_id.partition('id')[2].partition('|')[0])
                    except:
                        return self.from_id
            else:
                return self.from_id
        else:
            return int(self.message["reply_message"]["from_id"])
