from django.db import models

from django.conf import settings

# Create your models here.





class Catigories(models.Model):


    All = 'Al'
    Sport = 'SP'
    Fashion = 'FS'
    Electronic = 'EL'
    Computer = 'CM'
    Beauty = 'BT'
    Baby = 'BY'

    Top_10 = 'T1'
    Women = 'WM'
    Men = 'MN'
    Kids = 'KD'
    Accessoriess = 'ACR'

    popular_cartigories = [

        (Sport, 'Sport'),
        (Beauty, 'Beauty'),
        (Electronic, 'Electronic'),
        (Computer, 'Computer'),
        (Baby, 'Baby'),
        (Fashion, 'Fashion'),
    ]

    trending_cartigories = [

        (Top_10, 'Top_10'),
        (Women, 'Women'),
        (Men, 'Men'),
        (Kids, 'Kids'),
        (Accessoriess, 'Accessoriess'),
    ]

    Popular_category = models.CharField(max_length=30, choices=popular_cartigories, default=All)




class Products(models.Model):

    popular_categories = models.ForeignKey(Catigories, on_delete=models.CASCADE, null=True, blank=True)
    product_name= models.CharField(max_length=200, null=True, blank=True)
    product_image= models.ImageField(null=True, blank=True)
    product_description= models.TextField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(default=1, null=True, blank=True)
    price= models.FloatField(default=0, null=True)


    def __str__(self):

        return self.product_name



