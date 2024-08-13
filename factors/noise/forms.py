from .models import Noise
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class NoiseForm(ModelForm):
    class Meta:
        model = Noise
        fields = ['base', 'address', 'date', 'resultA_1', 'resultA_2', 'resultA_3', 'resultA_4', 'result31_1', 'result31_2', 'result31_3', 'result31_4', 'result63_1', 'result63_2', 'result63_3', 'result63_4', 'result125_1', 'result125_2', 'result125_3', 'result125_4', 'result250_1', 'result250_2', 'result250_3', 'result250_4', 'result500_1', 'result500_2', 'result500_3', 'result500_4', 'result1000_1', 'result1000_2', 'result1000_3', 'result1000_4', 'result2000_1', 'result2000_2', 'result2000_3', 'result2000_4', 'result4000_1', 'result4000_2', 'result4000_3', 'result4000_4', 'result8000_1', 'result8000_2', 'result8000_3', 'result8000_4', 'resultMax', 'resultMin']

        widgets = {
                    'base': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Основание',
                    }),
                    'address': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Адрес проведения измерений',
                    }),
                    'date': DateTimeInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Дата проведения измерений',
                    }),
                    'resultA_1': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Шкала А результат первого измерения',
                    }),
                    'resultA_2': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Шкала А результат второго измерения',
                    }),
                    'resultA_3': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Шкала А результат третьего измерения',
                    }),
                    'resultA_4': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Шкала А результат четвертого измерения',
                    }),
                    'result31_1': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 31.5 ГЦ результат первого измерения',
                    }),
                    'result31_2': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 31.5 ГЦ результат второго измерения',
                    }),
                    'result31_3': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 31.5 ГЦ результат третьего измерения',
                    }),
                    'result31_4': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 31.5 ГЦ результат четвертого измерения',
                    }),
                    'result63_1': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 63 ГЦ результат первого измерения',
                    }),
                    'result63_2': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 63 ГЦ результат второго измерения',
                    }),
                    'result63_3': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 63 ГЦ результат третьего измерения',
                    }),
                    'result63_4': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 63 ГЦ результат четвертого измерения',
                    }),
                    'result125_1': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 125 ГЦ результат первого измерения',
                    }),
                    'result125_2': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 125 ГЦ результат второго измерения',
                    }),
                    'result125_3': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 125 ГЦ результат третьего измерения',
                    }),
                    'result125_4': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 125 ГЦ результат четвертого измерения',
                    }),
                    'result250_1': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 250 ГЦ результат первого измерения',
                    }),
                    'result250_2': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 250 ГЦ результат второго измерения',
                    }),
                    'result250_3': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 250 ГЦ результат третьего измерения',
                    }),
                    'result250_4': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 250 ГЦ результат четвертого измерения',
                    }),
                    'result500_1': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 500 ГЦ результат первого измерения',
                    }),
                    'result500_2': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 500 ГЦ результат второго измерения',
                    }),
                    'result500_3': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 500 ГЦ результат третьего измерения',
                    }),
                    'result500_4': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 500 ГЦ результат четвертого измерения',
                    }),
                    'result1000_1': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 1000 ГЦ результат первого измерения',
                    }),
                    'result1000_2': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 1000 ГЦ результат второго измерения',
                    }),
                    'result1000_3': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 1000 ГЦ результат третьего измерения',
                    }),
                    'result1000_4': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 1000 ГЦ результат четвертого измерения',
                    }),
                    'result2000_1': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 2000 ГЦ результат первого измерения',
                    }),
                    'result2000_2': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 2000 ГЦ результат второго измерения',
                    }),
                    'result2000_3': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 2000 ГЦ результат третьего измерения',
                    }),
                    'result2000_4': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 2000 ГЦ результат четвертого измерения',
                    }),
                    'result4000_1': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 4000 ГЦ результат первого измерения',
                    }),
                    'result4000_2': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 4000 ГЦ результат второго измерения',
                    }),
                    'result4000_3': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 4000 ГЦ результат третьего измерения',
                    }),
                    'result4000_4': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 4000 ГЦ результат четвертого измерения',
                    }),
                    'result8000_1': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 8000 ГЦ результат первого измерения',
                    }),
                    'result8000_2': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 8000 ГЦ результат второго измерения',
                    }),
                    'result8000_3': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 8000 ГЦ результат третьего измерения',
                    }),
                    'result8000_4': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Частота 8000 ГЦ результат четвертого измерения',
                    }),
                    'resultMax': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Максимальный уровень звука',
                    }),
                    'resultMin': Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Минимальный уровень звука',
                    })
                }


