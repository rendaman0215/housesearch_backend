from django.db import models
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator

class MakerCard(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    name = models.CharField(max_length=100)
    name_hira = models.CharField(max_length=100)
    name_kata = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')
    create_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    def get_review_count(self):
        return Reviews.objects.filter(maker_name=self.name_eng).count()
    def get_expense_count(self):
        return Expense.objects.filter(maker_name=self.name_eng).count()
    def get_expense_avg(self):
        costavg = Expense.objects.filter(maker_name=self.name_eng).aggregate(Avg('cost')) ["cost__avg"]
        if costavg == None:
            return 0.0
        else:
            costavg = round(costavg,1)
        return costavg
    def get_landarea_avg(self):
        landareaavg = Expense.objects.filter(maker_name=self.name_eng).aggregate(Avg('landarea'))["landarea__avg"]
        if landareaavg == None:
            return 0.0
        else:
            landareaavg = round(landareaavg,1)
        return landareaavg
    def get_rateavg(self):
        avgrateavg = Reviews.objects.filter(maker_name=self.name_eng).aggregate(Avg('avgrate'))["avgrate__avg"]
        if avgrateavg == None:
            avgrateavg = 0.00
        else:
            avgrateavg = round(avgrateavg,2)
        return avgrateavg

    def get_costavg(self):
        costrateavg = Reviews.objects.filter(maker_name=self.name_eng).aggregate(Avg('costrate'))["costrate__avg"]
        if costrateavg == None:
            costrateavg = 0.00
        else:
            costrateavg = round(costrateavg,2)
        return costrateavg
    def get_designavg(self):
        designrateavg = Reviews.objects.filter(maker_name=self.name_eng).aggregate(Avg('designrate'))["designrate__avg"]
        if designrateavg == None:
            designrateavg = 0.00
        else:
            designrateavg = round(designrateavg,2)
        return designrateavg
    def get_layoutavg(self):
        layoutrateavg = Reviews.objects.filter(maker_name=self.name_eng).aggregate(Avg('layoutrate'))["layoutrate__avg"]
        if layoutrateavg == None:
            layoutrateavg = 0.00
        else:
            layoutrateavg = round(layoutrateavg,2)
        return layoutrateavg
    def get_specavg(self):
        specrateavg = Reviews.objects.filter(maker_name=self.name_eng).aggregate(Avg('specrate'))["specrate__avg"]
        if specrateavg == None:
            specrateavg = 0.00
        else:
            specrateavg = round(specrateavg,2)
        return specrateavg
    def get_guaranteeavg(self):
        guaranteerateavg = Reviews.objects.filter(maker_name=self.name_eng).aggregate(Avg('guaranteerate'))["guaranteerate__avg"]
        if guaranteerateavg == None:
            guaranteerateavg = 0.00
        else:
            guaranteerateavg = round(guaranteerateavg,2)
        return guaranteerateavg
    def get_salesavg(self):
        salesrateavg = Reviews.objects.filter(maker_name=self.name_eng).aggregate(Avg('salesrate'))["salesrate__avg"]
        if salesrateavg == None:
            salesrateavg = 0.00
        else:
            salesrateavg = round(salesrateavg,2)
        return salesrateavg

    def ratetostr(self):
        ratestr = ""
        rateavg = self.get_rateavg()
        for i in range(int(rateavg)):
            ratestr += '<i class="bi bi-star-fill rateicon"></i>'
        if float(rateavg) - float(int(rateavg)) > 0 and float(rateavg) - float(int(rateavg)) <= 0.5 and rateavg!=5 and rateavg!=0:
            ratestr += '<i class="bi bi-star-half rateicon"></i>'
        elif float(rateavg) - float(int(rateavg)) >= 0.5:
            ratestr += '<i class="bi bi-star-fill rateicon"></i>'
        for i in range(int(5.0-float(rateavg))):
            ratestr += '<i class="bi bi-star rateicon"></i>'
        return ratestr
    class Meta:
        verbose_name = "メーカー"
    

class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
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
    guaranteerate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    guaranteecomment = models.TextField()
    salesrate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    salescomment = models.TextField()
    avgrate = models.DecimalField(max_digits=3,decimal_places=2)
    maker_name = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now=True)

    def get_rateavg(self):
        total = self.costrate+self.designrate+self.layoutrate+self.specrate+self.guaranteerate+self.salesrate
        avgrateavg = total / 6
        avgrateavg = round(avgrateavg,2)
        return avgrateavg

    def __str__(self):
        return self.maker_name + " : " + self.author
    class Meta:
        verbose_name = "口コミ"

class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    hid = models.BooleanField(default=True)
    cost = models.IntegerField()
    landarea = models.IntegerField()
    gradecomment = models.TextField()
    costupcomment = models.TextField()
    costdowncomment = models.TextField()
    expimage = models.ImageField(upload_to='expense/', blank=True, null=True)
    layoutimage = models.ImageField(upload_to='expense/', blank=True, null=True)
    maker_name = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        sta = ""
        if self.hid:
            sta = "非表示"
        return self.maker_name + " : " + self.author + sta

    class Meta:
        verbose_name = "費用明細"