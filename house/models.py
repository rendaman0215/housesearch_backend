from django.db import models
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

class MakerCard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='')
    def __str__(self):
        return self.name
    def get_review_count(self):
        return Reviews.objects.filter(tenant=self.pk).count()
    def get_expense_count(self):
        return Expense.objects.filter(tenant=self.pk).count()
    def get_expense_avg(self):
        costavg = Expense.objects.filter(tenant=self.pk).aggregate(Avg('cost')) ["cost__avg"]
        if costavg == None:
            return 0.0
        return costavg
    def get_landarea_avg(self):
        landareaavg = Expense.objects.filter(tenant=self.pk).aggregate(Avg('landarea'))["landarea__avg"]
        if landareaavg == None:
            return 0.0
        return landareaavg
    def get_rateavg(self):
        avgrateavg = Reviews.objects.filter(tenant=self.pk).aggregate(Avg('avgrate'))["avgrate__avg"]
        if avgrateavg == None:
            avgrateavg = 0.00
        else:
            avgrateavg = round(avgrateavg,2)
        return avgrateavg
    def ratetostr(self):
        ratestr = ""
        rateavg = self.get_rateavg()
        for i in range(int(rateavg)):
            ratestr += '<i class="bi bi-star-fill"></i>'
        if float(rateavg) - float(int(rateavg)) >= 0.5 and rateavg!=5.0:
            ratestr += '<i class="bi bi-star-half"></i>'
        for i in range(int(5.0-float(rateavg))):
            ratestr += '<i class="bi bi-star"></i>'
        return ratestr
    class Meta:
        verbose_name = "メーカー"
    

class Reviews(models.Model):
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    costrate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    costcomment = models.TextField()
    designrate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    designcomment = models.TextField()
    layoutrate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    layoutcomment = models.TextField()
    specrate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    speccomment = models.TextField()
    attachrate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    attachcomment = models.TextField()
    guaranteerate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    guaranteecomment = models.TextField()
    salesrate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    salescomment = models.TextField()
    avgrate = models.DecimalField(max_digits=3,decimal_places=2)
    tenant = models.IntegerField()
    images = models.ImageField(upload_to='', blank=True, null=True)
    def __str__(self):
        object = MakerCard.objects.get(pk=self.tenant)
        return object.name + "-" + self.author
    class Meta:
        verbose_name = "口コミ"

class Expense(models.Model):
    author = models.CharField(max_length=100)
    cost = models.IntegerField()
    landarea = models.IntegerField()
    comment = models.TextField()
    images = models.ImageField(upload_to='', blank=True, null=True)
    tenant = models.IntegerField()
    def __str__(self):
        return self.author
    class Meta:
        verbose_name = "費用明細"