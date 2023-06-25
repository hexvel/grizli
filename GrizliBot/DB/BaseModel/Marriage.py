from tortoise import fields
from tortoise.models import Model


class Marriage(Model):
    chat_id = fields.IntField()
    husband = fields.IntField()
    wife = fields.IntField()
    date_married = fields.TextField()
    count_hugs = fields.IntField(default=0)
    count_binds = fields.IntField(default=0)
    count_kiss = fields.IntField(default=0)
    count_sex = fields.IntField(default=0)