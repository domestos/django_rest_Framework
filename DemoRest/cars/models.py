from django.db import models
#======================================= USER ==================================
# напряму наслідуватися від модулі  User не бажано, оскільки вона меже буди переопреділена (кастомізована/розширена), тому слід використувавути методі get_user_model
from django.contrib.auth import get_user_model
User = get_user_model()
#==============================================================================
# Create your models here.
class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', db_index=True, max_length=64)
    color = models.CharField(verbose_name='Color', max_length=64)
    brand = models.CharField(verbose_name='Brand', max_length=64)
    CAR_TYPE = (
        (1,'Sedan'),
        (2,'Sprot'),
        (3,'OffRoad'),
        (4,'Cupe'),
        
    )
    car_type = models.IntegerField(verbose_name='Car_Type',choices=CAR_TYPE)
    user =models.ForeignKey(User, verbose_name='User', on_delete =models.CASCADE) 