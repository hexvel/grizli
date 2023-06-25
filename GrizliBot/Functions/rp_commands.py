import random

from loguru import logger as log
from constants import Icons, ImagesForRp


class RpCommands:
    log.success("Class is running")

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

        random_image = random.choice(ImagesForRp.hug)
        self.send_messages(self.api, self.peer_id, action, attachments=random_image)
    
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

        random_image = random.choice(ImagesForRp.bind)
        self.send_messages(self.api, self.peer_id, action, attachments=random_image)
    
    def kiss_user(self):
        member_id = self._member_id()
        member_id_type = "club" if member_id < 1 else "id"
        text_split = self.message['text'].split("\n")

        data_user_info = self.get_user_info(self.from_id)
        member_sex = "поцеловал" if data_user_info['sex'] > 1 else "поцеловала"
        user_info = self.get_user_info(member_id)
        
        action = f"{Icons.KISS} [id{self.from_id}|{data_user_info['first_name']}] {member_sex} "\
        f"[{member_id_type}{member_id}|{user_info['first_name']} {user_info['last_name']}]"

        if len(text_split) >= 2:
            action += f"\n{Icons.COMMENT} С репликой: {text_split[1].strip()}"

        random_image = random.choice(ImagesForRp.kiss)
        self.send_messages(self.api, self.peer_id, action, attachments=random_image)

    def hit_user(self):
        member_id = self._member_id()
        member_id_type = "club" if member_id < 1 else "id"
        text_split = self.message['text'].split("\n")

        data_user_info = self.get_user_info(self.from_id)
        member_sex = "ударил" if data_user_info['sex'] > 1 else "ударила"
        user_info = self.get_user_info(member_id)
        
        action = f"{Icons.HIT} [id{self.from_id}|{data_user_info['first_name']}] {member_sex} "\
        f"[{member_id_type}{member_id}|{user_info['first_name']} {user_info['last_name']}]"

        if len(text_split) >= 2:
            action += f"\n{Icons.COMMENT} С репликой: {text_split[1].strip()}"

        random_image = random.choice(ImagesForRp.hit)
        self.send_messages(self.api, self.peer_id, action, attachments=random_image)

    def feed_user(self):
        member_id = self._member_id()
        member_id_type = "club" if member_id < 1 else "id"
        text_split = self.message['text'].split("\n")

        data_user_info = self.get_user_info(self.from_id)
        member_sex = "накормил" if data_user_info['sex'] > 1 else "накормила"
        user_info = self.get_user_info(member_id)
        
        action = f"{Icons.FEED} [id{self.from_id}|{data_user_info['first_name']}] {member_sex} "\
        f"[{member_id_type}{member_id}|{user_info['first_name']} {user_info['last_name']}]"

        if len(text_split) >= 2:
            action += f"\n{Icons.COMMENT} С репликой: {text_split[1].strip()}"

        random_image = random.choice(ImagesForRp.feed)
        self.send_messages(self.api, self.peer_id, action, attachments=random_image)