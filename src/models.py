import os

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute


TABLE_NAME = os.environ.get("TABLE_NAME", "random-quiz")

AWS_REGION = os.environ.get("AWS_REGION", "ap-northeast-2")


class QuizModel(Model):
    class Meta:
        table_name = TABLE_NAME
        region = AWS_REGION

    id = UnicodeAttribute(hash_key=True)  # uuid
    type = UnicodeAttribute(range_key=True)  # face, music
    code = UnicodeAttribute(null=False)
    name = UnicodeAttribute(null=False)
    title = UnicodeAttribute(null=True)
    # reg_date = UTCDateTimeAttribute(null=True)
