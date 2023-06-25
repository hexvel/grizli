import time

from loguru import logger
from random import getrandbits
from decors import error_logger


class VkMethods:
    logger.success("Class is running")
    time.sleep(0.1)

    def send_messages(self, vk: object, peer_id: int, messages: str = None, attachments: str = None,
                      expire_ttl: int = None, reply_to: int = None, random_id = getrandbits(32), forward: dict = None) -> bool:
        """
        :param forward: dict
        :param vk: object
        :param peer_id: int
        :param messages: str
        :param attachments: str
        :param expire_ttl: int
        :param reply_to: int
        :param random_id: int
        :rtype: bool
        """
        try:
            message = vk.messages.send(peer_id=peer_id, message=messages, attachment=attachments,
                             expire_ttl=expire_ttl, reply_to=reply_to, random_id=random_id, forward=forward)
            return message
        except Exception as error:
            logger.debug(error)
            return False

    def edit_messages(self, vk: object, peer_id: int, messages: str = None, message_id: int = None,
                      attachments: str = None, reply_to: int = None, send: bool = True,
                      keep_forward_messages: int = 1) -> bool:
        """
        :param vk: object
        :param peer_id: int,
        :param messages: str,
        :param message_id: int,
        :param attachments: str,
        :param reply_to: int,
        :param random_id: int,
        :param send: bool,
        :param keep_forward_messages: int,
        :rtype: bool
        """
        try:
            vk.messages.edit(peer_id=peer_id, message_id=message_id, message=messages,
                             attachment=attachments, keep_forward_messages=keep_forward_messages)
        except:
            if not send:
                return False
            self.delete_messages(self.api, self.peer_id, self.message_id)
            self.send_messages(vk, peer_id=peer_id, messages=messages, attachments=attachments,
                               reply_to=reply_to)
        else:
            return True

    @error_logger
    def delete_messages(self, vk: object, peer_id: int, message_ids: str, delete_for_all: int = 1) -> bool:
        """
        :param vk: object
        :param peer_id: int
        :param message_ids: str
        :param delete_for_all: int
        :rtype: bool
        """
        vk.messages.delete(peer_id=peer_id, cmids=message_ids, delete_for_all=delete_for_all)
        return True

    def __del__(self):
        logger.debug(f"Class destroyed.")
