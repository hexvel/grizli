from datetime import datetime
from loguru import logger as log
from constants import Icons, ImagesForRp


class Marriage:
    log.success("Class is running")

    def marry_user(self):
        user_id = self._member_id()
        user_info = self.get_user_info(self.from_id)
        filters = dict(husband=self.from_id, wife=user_id, chat_id=self.chat_id) if user_info['sex'] == 2\
            else dict(wife=self.from_id, husband=user_id, chat_id=self.chat_id)

        if user_id < 1:
            message = f"{Icons.WARNING} Вы хотите создать брак с [club{abs(user_id)}|сообществом]..? seriously..?"
            self.send_messages(self.api, self.peer_id, message, reply_to=self.message_id)
            return
        
        if self.base_getter(filters, 'marry')['running']:
            message = f"{Icons.WARNING} Вы уже состоите в браке."
            self.send_messages(self.api, self.peer_id, message, reply_to=self.message_id)
            return
        
        params = dict(husband=self.from_id, wife=user_id, chat_id=self.chat_id, date_married=str(datetime.now())) if user_info['sex'] == 2\
            else dict(wife=self.from_id, husband=user_id, chat_id=self.chat_id, date_married=str(datetime.now()))
        
        create = self.base_create(filters, params, 'marry')

        if create['running']:
            user_info = self.get_user_info(user_id)
            message = f"{Icons.YES} [id{self.from_id}|Вы] успешно создали брак с [id{user_id}|{user_info['first_name']} {user_info['last_name']}.]"
            self.send_messages(self.api, self.peer_id, message)
            return
        
        message = f"{Icons.WARNING} При создании брака произошла ошибка."
        self.send_messages(self.api, self.peer_id, message, reply_to=self.message_id)
        return

    def remove_married_user(self):
        ...

    def get_married_users(self):
        ...