from tortoise import fields
from tortoise.models import Model


class Main(Model):
    chat_id = fields.IntField(pk=True)
    chat_key = fields.TextField()
    