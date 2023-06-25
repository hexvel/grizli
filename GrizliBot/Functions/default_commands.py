import time
import requests

from loguru import logger as log
from constants import Icons, ImagesForRp


class DefaultCommands:
    log.success("Class is running")

    def ping(self):
        ping = time.time() - self.message['date']
        times = abs(float(f"{ping:.4f}"))
        self.send_messages(self.api, self.peer_id, f"{Icons.SETTINGS} PingTime: {times}ms.")

    def get_voice_from_audio(self):
        items = self.api.messages.getById(peer_id=self.peer_id, cmids=self.message['conversation_message_id'])['items']
        
        attachments = items[0].get('attachments')[0] if items[0].get('attachments', False) else False
        reply_messages = items[0].get('reply_to_message', False)

        if reply_messages:
            attachments = reply_messages.get('attachments')[0] if reply_messages.get('attachments', False) else False

        if not attachments or attachments.get('type'):
            if type(attachments) == bool or attachments['type'] != 'audio':
                message = f"{Icons.WARNING} Пожалуйста, укажите сообщение с аудио-вложением."
                self.send_messages(self.api, self.peer_id, message)
                return
            
        self.delete_messages(self.api, self.peer_id, self.message['conversation_message_id'])

        audio_url = attachments['audio']['url']
        content = requests.get(audio_url).content

        with open('Templates/audio.mp4', 'wb') as _file:
            _file.write(content)

        with open('Templates/audio.mp4', 'rb') as _file:
            audio_attachment = self.upl.audio_message(_file, peer_id=self.peer_id)

        attachment = audio_attachment.get('audio_message')
        attachment = '{}{}_{}'.format('audio_message', attachment['owner_id'], attachment['id'])

        self.send_messages(self.api, self.peer_id, attachments=attachment)