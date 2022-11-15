from email import message
from email.policy import default
from unicodedata import category
from django.db import models

class Message(models.Model):
    userid = models.CharField(max_length = 20) # userid -> 나중에 로그인하면 토큰으로..?
    nickname = models.CharField(max_length = 20) # nickname
    category = models.CharField(max_length = 20, default = '') # 카테고리
    message = models.TextField() # 메시지 작성

    create_at = models.DateTimeField(auto_now_add = True) # 작성시간
    update_at = models.DateTimeField(auto_now = True) # 수정시간

    def __str__(self):
        return f'[{self.pk}]{self.category}' # 메시지 목록에 pk와 카테고리가 보이게..