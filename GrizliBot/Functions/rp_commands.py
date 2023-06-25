import random

from loguru import logger as log
from GrizliBot.constants import Icons, ImagesForRp


class RpCommands:
    log.success("Class [RpCommands] was successfully runned.")

    def hug_user(self):
        member_id = self._member_id()
        member_id_type = "club" if member_id < 1 else "id"
        text_split = self.message['text'].split("\n")

        data_user_info = self.get_user_info(self.from_id)
        member_sex = "обнял" if data_user_info['sex'] > 1 else "обняла"
        user_info = self.get_user_info(member_id)

        action = f"{Icons.HUG} [id{self.from_id}|{data_user_info['first_name']}] {member_sex} "\
        f"[{member_id_type}{member_id}|{user_info['first_name']} {user_info['last_name']}]"

        if len(text_split) >= 2:
            action += f"\n{Icons.COMMENT} С репликой: {text_split[1].strip()}"

        radom_image = random.choice(ImagesForRp.hug)
        self.send_messages(self.api, self.peer_id, action, attachments=radom_image)
    
    def bind_user(self):
        member_id = self._member_id()
        member_id_type = "club" if member_id < 1 else "id"
        text_split = self.message['text'].split("\n")

        data_user_info = self.get_user_info(self.from_id)
        member_sex = "связал" if data_user_info['sex'] > 1 else "связала"
        user_info = self.get_user_info(member_id)
        
        action = f"{Icons.BIND} [id{self.from_id}|{data_user_info['first_name']}] {member_sex} "\
        f"[{member_id_type}{member_id}|{user_info['first_name']} {user_info['last_name']}]"

        if len(text_split) >= 2:
            action += f"\n{Icons.COMMENT} С репликой: {text_split[1].strip()}"

        radom_image = random.choice(ImagesForRp.bind)
        self.send_messages(self.api, self.peer_id, action, attachments=radom_image)