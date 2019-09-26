from django.db import models

# Create your models here.
class Filial(models.Model):
    name = models.CharField('Название филиала', max_length=20)

    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField('Название провайдера', max_length=20)
    contract = models.CharField('Договор', max_length=20)
    entity = models.CharField('Юр. лицо', max_length=40)
    tel_number = models.CharField('Номер телефона', max_length=20)

    def __str__(self):
        return self.name

class Shop(models.Model):
    number = models.PositiveSmallIntegerField('Номер магазина')
    address = models.CharField('Адрес магазина',max_length=80)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT)
    speed = models.DecimalField('Скорость', max_digits=4, decimal_places=1, null=True)
    tel_number = models.CharField('Номер телефона', max_length=20)

    
    def __str__(self):
        return self.address