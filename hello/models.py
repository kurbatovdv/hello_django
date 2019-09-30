from django.db import models

# Create your models here.
class Filial(models.Model):
    name = models.CharField('Филиал', max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

class Provider(models.Model):
    name = models.CharField('Провайдер', max_length=20)
    contract = models.CharField('Договор', max_length=20)
    entity = models.CharField('Юр. лицо', max_length=40)
    tel_number = models.CharField('Номер телефона', max_length=20)

    def __str__(self):
        return '%s %s' % (self.name, self.contract)

    class Meta:
        verbose_name = 'Провайдер'
        verbose_name_plural = 'Провайдеры'

class License_Astor(models.Model):
    TS = models.CharField('Лицензия ТС7',max_length=20)
    SIS = models.CharField('Лицензия SIS',max_length=20)
    MDT = models.CharField('Лицензия MDT',max_length=20)
    LP = models.CharField('Лицензия LabelPrint',max_length=20)

    def __str__(self):
        return '%s %s %s %s' % (self.TS, self.SIS, self.MDT, self.LP)

class Shop(models.Model):
    number = models.PositiveSmallIntegerField('Номер магазина', unique=True)
    address = models.CharField('Адрес магазина', max_length=80)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, verbose_name='Филиал')
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT, verbose_name='Провайдер')
    speed = models.DecimalField('Скорость', max_digits=4, decimal_places=1, null=True)
    tel_number = models.CharField('Номер телефона', max_length=20)
    kass_count = models.PositiveSmallIntegerField('Количество касс', default=1)
    license_astor = models.OneToOneField(License_Astor, on_delete=models.PROTECT, null=True, verbose_name='Лицензии Астор')

    def __str__(self):
        return '%s %s' % (self.number, self.address)

 #   def provider_view(self):
 #        provider_qty = self.provider_set.all()

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
