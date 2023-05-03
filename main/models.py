from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    ''' Таблица ТОВАРЫ
        Id
        Название товара
        Ссылка на товар
        Цена
        Дата создания товара
    '''
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title

class WishList(models.Model):
    """
      таблица "Лист подарков"

      id
      owner
      products - ManyToMany
      """
    title = models.CharField(max_length=120)
    product = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Form(models.Model):
    """
    таблица "Формы"

    userid text,
    storenumber text,
    filldate text,
    anketa_type text,
    anketa_item text
    """
    userid = models.IntegerField()
    storenumber = models.IntegerField()
    filldate = models.DateTimeField(auto_created=True)
    anketa_type = models.CharField(max_length=20)
    anketa_item = models.CharField(max_length=256)
    def __str__(self):
        return self.title
