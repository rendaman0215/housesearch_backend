from django.db import models

class Topic(models.Model):

    class Meta:
        db_table = "topic"

    comment = models.CharField(verbose_name="コメント",max_length=2000)

    def __str__(self):
        return self.commentpyt