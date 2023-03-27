from django.urls import reverse
from django.db import models

class Bank(models.Model):
    bank_name = models.CharField(max_length=150, verbose_name='Название Банка')
    full_name = models.CharField(max_length=150, verbose_name='Полное наименование Банка')
    phone_num = models.CharField(max_length=150, verbose_name='Номер телефона')
    description = models.TextField(blank=True, verbose_name='Описание большое')
    slug = models.SlugField(max_length=150, verbose_name='slug адрес')
    url_site = models.CharField(max_length=150, verbose_name='Адресс официального сайта')
    email = models.EmailField(max_length=150, verbose_name='Почтовый адрес')
    address1 = models.CharField(max_length=250, verbose_name='Адресс 1')
    address2 = models.CharField(max_length=250, verbose_name='Адресс 2')
    data_reg = models.CharField(max_length=250, verbose_name='Дата регистрации банка')
    
    ceo_name = models.CharField(max_length=250, verbose_name='Председатель правления')
    created  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    social = models.CharField(max_length=250, verbose_name='Ссылки на соц сети')
    reg_info = models.CharField(max_length=250, verbose_name='Реквизиты банка')

    def __str__(self):
        return self.bank_name
    
    class Meta:

        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'
        



