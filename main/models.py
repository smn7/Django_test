from django.db import models

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