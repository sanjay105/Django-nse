from django.db import models

# Create your models here.
class stocksData(models.Model):
    pricebandupper=models.FloatField(default=0)
    totalbuyquantity=models.FloatField(default=0)
    totaltradevalue=models.FloatField(default=0)
    averageprice=models.FloatField(default=0)
    previousclose=models.FloatField(default=0)
    buyprice1=models.FloatField(default=0)
    buyprice2=models.FloatField(default=0)
    buyprice3=models.FloatField(default=0)
    buyprice4=models.FloatField(default=0)
    buyprice5=models.FloatField(default=0)
    sellprice1=models.FloatField(default=0)
    sellprice2=models.FloatField(default=0)
    sellprice3=models.FloatField(default=0)
    sellprice4=models.FloatField(default=0)
    sellprice5=models.FloatField(default=0)
    totaltradedvolume=models.FloatField(default=0)
    lastprice=models.FloatField(default=0)
    curtime=models.CharField(max_length=200,primary_key='true')

    def currentTime(self):
        return self.curtime
    def previousClose(self):
        return self.previousclose
    def averagePrice(self):
        return self.averageprice