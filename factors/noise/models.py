from django.db import models


class Noise(models.Model):
    base = models.CharField('Основание', max_length=250)
    address = models.CharField('Адрес измерений', max_length=250)
    date = models.DateTimeField('Дата измерений')
    resultA_1 = models.FloatField('Эквтвалентный уровень звука/Уровень звука А', null=True, blank=True)
    resultA_2 = models.FloatField('Эквтвалентный уровень звука/Уровень звука А', null=True, blank=True)
    resultA_3 = models.FloatField('Эквтвалентный уровень звука/Уровень звука А', null=True, blank=True)
    resultA_4 = models.FloatField('Эквтвалентный уровень звука/Уровень звука А', null=True, blank=True)
    result31_1 = models.FloatField('Уровень звука на частоте 31.5 Гц', null=True, blank=True)
    result31_2 = models.FloatField('Уровень звука на частоте 31.5 Гц', null=True, blank=True)
    result31_3 = models.FloatField('Уровень звука на частоте 31.5 Гц', null=True, blank=True)
    result31_4 = models.FloatField('Уровень звука на частоте 31.5 Гц', null=True, blank=True)
    result63_1 = models.FloatField('Уровень звука на частоте 63 Гц', null=True, blank=True)
    result63_2 = models.FloatField('Уровень звука на частоте 63 Гц', null=True, blank=True)
    result63_3 = models.FloatField('Уровень звука на частоте 63 Гц', null=True, blank=True)
    result63_4 = models.FloatField('Уровень звука на частоте 63 Гц', null=True, blank=True)
    result125_1 = models.FloatField('Уровень звука на частоте 125 Гц', null=True, blank=True)
    result125_2 = models.FloatField('Уровень звука на частоте 125 Гц', null=True, blank=True)
    result125_3 = models.FloatField('Уровень звука на частоте 125 Гц', null=True, blank=True)
    result125_4 = models.FloatField('Уровень звука на частоте 125 Гц', null=True, blank=True)
    result250_1 = models.FloatField('Уровень звука на частоте 250 Гц', null=True, blank=True)
    result250_2 = models.FloatField('Уровень звука на частоте 250 Гц', null=True, blank=True)
    result250_3 = models.FloatField('Уровень звука на частоте 250 Гц', null=True, blank=True)
    result250_4 = models.FloatField('Уровень звука на частоте 250 Гц', null=True, blank=True)
    result500_1 = models.FloatField('Уровень звука на частоте 500 Гц', null=True, blank=True)
    result500_2 = models.FloatField('Уровень звука на частоте 500 Гц', null=True, blank=True)
    result500_3 = models.FloatField('Уровень звука на частоте 500 Гц', null=True, blank=True)
    result500_4 = models.FloatField('Уровень звука на частоте 500 Гц', null=True, blank=True)
    result1000_1 = models.FloatField('Уровень звука на частоте 1000 Гц', null=True, blank=True)
    result1000_2 = models.FloatField('Уровень звука на частоте 1000 Гц', null=True, blank=True)
    result1000_3 = models.FloatField('Уровень звука на частоте 1000 Гц', null=True, blank=True)
    result1000_4 = models.FloatField('Уровень звука на частоте 1000 Гц', null=True, blank=True)
    result2000_1 = models.FloatField('Уровень звука на частоте 2000 Гц', null=True, blank=True)
    result2000_2 = models.FloatField('Уровень звука на частоте 2000 Гц', null=True, blank=True)
    result2000_3 = models.FloatField('Уровень звука на частоте 2000 Гц', null=True, blank=True)
    result2000_4 = models.FloatField('Уровень звука на частоте 2000 Гц', null=True, blank=True)
    result4000_1 = models.FloatField('Уровень звука на частоте 4000 Гц', null=True, blank=True)
    result4000_2 = models.FloatField('Уровень звука на частоте 4000 Гц', null=True, blank=True)
    result4000_3 = models.FloatField('Уровень звука на частоте 4000 Гц', null=True, blank=True)
    result4000_4 = models.FloatField('Уровень звука на частоте 4000 Гц', null=True, blank=True)
    result8000_1 = models.FloatField('Уровень звука на частоте 8000 Гц', null=True, blank=True)
    result8000_2 = models.FloatField('Уровень звука на частоте 8000 Гц', null=True, blank=True)
    result8000_3 = models.FloatField('Уровень звука на частоте 8000 Гц', null=True, blank=True)
    result8000_4 = models.FloatField('Уровень звука на частоте 8000 Гц', null=True, blank=True)
    resultMax = models.FloatField('Максимальынй измеренный результат')
    resultMin = models.FloatField('Минимальный измеренный результат')

    def __str__(self):
        return self.base

    def get_absolute_url(self):
        return f'/noise/{self.id}'

    class Meta:
        verbose_name = 'Результат измерений'
        verbose_name_plural = 'Результаты измерений'


class standard_values():
    data_norms_day = {
        'LA': 40.0,
        '31.5': 79.0,
        '63': 63.0,
        '125': 52.0,
        '250': 45.0,
        '500': 39.0,
        '1000': 35.0,
        '2000': 32.0,
        '4000': 30.0,
        '8000': 28.0,
        'LEQ': 40.0,
        'LMAX': 55.0
    }
    data_norms_night = {
        '31.5': 72.0,
        '63': 55.0,
        '125': 44.0,
        '250': 35.0,
        '500': 29.0,
        '1000': 25.0,
        '2000': 22.0,
        '4000': 20.0,
        '8000': 18.0,
        'LA': 30.0,
        'LEQ': 30.0,
        'LMAX': 45.0,
    }
