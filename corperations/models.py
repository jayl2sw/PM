from django.db import models

# Create your models here.
class Corperation(models.Model):
    c_name = models.CharField(max_length=20)
    c_code = models.CharField(max_length=10, primary_key=True)
    c_price = models.IntegerField()
    sales_21 = models.IntegerField()
    operatingincome_21 = models.IntegerField()
    netincome_21 = models.IntegerField()
    sales_20 = models.IntegerField()
    operatingincome_20 = models.IntegerField()
    netincome_20 = models.IntegerField()
    market_cap = models.TextField()
    last_updated_date = models.DateField(default="2000-01-01")
