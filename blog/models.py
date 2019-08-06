from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to="blog/%Y/%m/%d", blank=True)

    created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=False) #회원이 탈퇴하면 글도 같이 지울건지 (=True)

    # __Str__은 객체를 어떤 식으로 표현할 것인지 정의.
    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)