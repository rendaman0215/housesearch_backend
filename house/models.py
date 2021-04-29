from django.db import models

class MakerCard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "メーカー"

class Reviews(models.Model):
    author = models.CharField(max_length=100)
    comment = models.TextField()
    tenant = models.IntegerField()
    images = models.ImageField(upload_to='', blank=True, null=True)
    def __str__(self):
        return self.author
    class Meta:
        verbose_name = "口コミ"

class Expense(models.Model):
    author = models.CharField(max_length=100)
    cost = models.IntegerField()
    comment = models.TextField()
    images = models.ImageField(upload_to='', blank=True, null=True)
    tenant = models.IntegerField()
    def __str__(self):
        return self.author
    class Meta:
        verbose_name = "費用明細"