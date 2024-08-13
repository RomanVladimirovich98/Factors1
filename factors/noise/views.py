from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import Noise, standard_values
from .forms import NoiseForm
from django.views.generic import DetailView, UpdateView, DeleteView
import math


def noise_home(request):
    noise_result = Noise.objects.order_by('-id')
    return render(request, 'noise/noise.html', {'noise_result': noise_result})

@csrf_exempt
def noise_create(reqest):
    error = ''
    if reqest.method == 'POST':
        form = NoiseForm(reqest.POST)
        if form.is_valid():
            form.save()
            return redirect('noise')
        else:
            error = 'Try again)))'

    form = NoiseForm()

    data = {
        'form': form,
        'error': error
    }
    return render(reqest, 'noise/create.html', data)


def noise_result_for_compared(value1, value2, value3, value4):
    result_amount = 0
    operation2 = 0
    operation5 = 0
    a = (value1, value2, value3, value4)
    for i in a:
        if i:
            result_amount += 1
        else:
            pass
    operation1 = [10 ** i for i in a]
    for i in operation1:
        operation2 += i
    operation3 = math.log10(operation2)
    operation4 = math.log10(result_amount)
    noise_average_result = operation3 - operation4
    for i in a:
        operation5 += i - noise_average_result
    operation6 = operation5 ** 2
    operation7 = operation6 / (result_amount * (result_amount - 1))
    uncertaintyA = math.sqrt(operation7)
    L = 0.7
    uncertaintyB = L / math.sqrt(3)
    operation8 = uncertaintyB ** 2 + uncertaintyA ** 2
    uncertaintyC = math.sqrt(operation8)
    k = 1.65
    uncertainty = k * uncertaintyC
    noise_compared = noise_average_result + uncertainty
    return(noise_compared)


def noise_result_uncertainty(value1, value2, value3, value4):
    result_amount = 0
    operation2 = 0
    operation5 = 0
    a = (value1, value2, value3, value4)
    for i in a:
        if i:
            result_amount += 1
        else:
            pass
    operation1 = [10 ** i for i in a]
    for i in operation1:
        operation2 += i
    operation3 = math.log10(operation2)
    operation4 = math.log10(result_amount)
    noise_average_result = operation3 - operation4
    for i in a:
        operation5 += i - noise_average_result
    operation6 = operation5 ** 2
    operation7 = operation6 / (result_amount * (result_amount - 1))
    uncertaintyA = math.sqrt(operation7)
    L = 0.7
    uncertaintyB = L / math.sqrt(3)
    operation8 = uncertaintyB ** 2 + uncertaintyA ** 2
    uncertaintyC = math.sqrt(operation8)
    k = 1.65
    uncertainty = k * uncertaintyC
    return(uncertainty)


def nature_of_the_noise(reqest, pk = '<int:pk>'):
    posts = Noise.objects.get(pk=pk)
    all_result = [posts.resultA_1, posts.resultA_2, posts.resultA_3, posts.resultA_4, #0-3
                  posts.result31_1, posts.result31_2, posts.result31_3, posts.result31_4, #4-7
                  posts.result63_1, posts.result63_2, posts.result63_3, posts.result63_4, #8-11
                  posts.result125_1, posts.result125_2, posts.result125_3, posts.result125_4, #12-15
                  posts.result250_1, posts.result250_2, posts.result250_3, posts.result250_4, #16-19
                  posts.result500_1, posts.result500_2, posts.result500_3, posts.result500_4, #20-23
                  posts.result1000_1, posts.result1000_2, posts.result1000_3, posts.result1000_4, #24-27
                  posts.result2000_1, posts.result2000_2, posts.result2000_3, posts.result2000_4, #28-31
                  posts.result4000_1, posts.result4000_2, posts.result4000_3, posts.result4000_4, #32-35
                  posts.result8000_1, posts.result8000_2, posts.result8000_3, posts.result8000_4, #36-39
                  posts.resultMax, posts.resultMin] #40-41
    info_measurements = {'base': posts.base, 'address': posts.address, 'date': posts.date}
    if posts.resultMax - posts.resultMin >= 10:
        L = 0.7 #погрешность прибора, придумай как выбрать ее
        uncertaintyB = L / math.sqrt(3)
        uncertainty = {'LEQ': uncertaintyB}
        resultA_list = (posts.resultA_1, posts.resultA_2, posts.resultA_3, posts.resultA_4)
        max_resultA = max(list(resultA_list))
        noise_resultA_compared = max_resultA + uncertaintyB
        noise_resultMax_compared = posts.resultMax
        data_intermittent_noise = {
            'LEQ': noise_resultA_compared,
            'LMAX': noise_resultMax_compared
        }
        breach = {}
        for key in data_intermittent_noise:
            if key in standard_values.data_norms_day:
                if data_intermittent_noise[key] - standard_values.data_norms_day[key] < 0:
                    pass
                else:
                    a = str(key)
                    breach[a] = data_intermittent_noise[key] - standard_values.data_norms_day[key]
        normative_value = {
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
        'LMAX': 55.0}
        total_intermittent = {'breach': breach, 'uncertainty': uncertainty, 'normative_value': normative_value, 'data_intermittent_noise': data_intermittent_noise, 'info_measurements': info_measurements}
        return render(reqest, 'noise/alert.html', {'total_intermittent': total_intermittent })
    elif posts.resultMax - posts.resultMin < 10:
        noise_resultA_compared = noise_result_for_compared(all_result[0], all_result[1], all_result[2], all_result[3])
        noise_result31_compared = noise_result_for_compared(all_result[4], all_result[5], all_result[6], all_result[7])
        noise_result63_compared = noise_result_for_compared(all_result[8], all_result[9], all_result[10], all_result[11])
        noise_result125_compared = noise_result_for_compared(all_result[12], all_result[13], all_result[14], all_result[15])
        noise_result250_compared = noise_result_for_compared(all_result[16], all_result[17], all_result[18], all_result[19])
        noise_result500_compared = noise_result_for_compared(all_result[20], all_result[21], all_result[22], all_result[23])
        noise_result1000_compared = noise_result_for_compared(all_result[24], all_result[25], all_result[26], all_result[27])
        noise_result2000_compared = noise_result_for_compared(all_result[28], all_result[29], all_result[30], all_result[31])
        noise_result4000_compared = noise_result_for_compared(all_result[32], all_result[33], all_result[34], all_result[35])
        noise_result8000_compared = noise_result_for_compared(all_result[36], all_result[37], all_result[38], all_result[39])
        noise_resultMax_compared = all_result[40]
        data_constant_noise = {
            'LA': noise_resultA_compared,
            '31.5': noise_result31_compared,
            '63': noise_result63_compared,
            '125': noise_result125_compared,
            '250': noise_result250_compared,
            '500': noise_result500_compared,
            '1000': noise_result1000_compared,
            '2000': noise_result2000_compared,
            '4000': noise_result4000_compared,
            '8000': noise_result8000_compared,
            'LMAX': noise_resultMax_compared
        }
        noise_resultA_uncertainty = noise_result_uncertainty(all_result[0], all_result[1], all_result[2], all_result[3])
        noise_result31_uncertainty = noise_result_uncertainty(all_result[4], all_result[5], all_result[6], all_result[7])
        noise_result63_uncertainty = noise_result_uncertainty(all_result[8], all_result[9], all_result[10], all_result[11])
        noise_result125_uncertainty = noise_result_uncertainty(all_result[12], all_result[13], all_result[14], all_result[15])
        noise_result250_uncertainty = noise_result_uncertainty(all_result[16], all_result[17], all_result[18], all_result[19])
        noise_result500_uncertainty = noise_result_uncertainty(all_result[20], all_result[21], all_result[22], all_result[23])
        noise_result1000_uncertainty = noise_result_uncertainty(all_result[24], all_result[25], all_result[26], all_result[27])
        noise_result2000_uncertainty = noise_result_uncertainty(all_result[28], all_result[29], all_result[30], all_result[31])
        noise_result4000_uncertainty = noise_result_uncertainty(all_result[32], all_result[33], all_result[34], all_result[35])
        noise_result8000_uncertainty = noise_result_uncertainty(all_result[36], all_result[37], all_result[38], all_result[39])
        data_constant_noise_uncertainty = {
            'LA': noise_resultA_uncertainty,
            '31.5': noise_result31_uncertainty,
            '63': noise_result63_uncertainty,
            '125': noise_result125_uncertainty,
            '250': noise_result250_uncertainty,
            '500': noise_result500_uncertainty,
            '1000': noise_result1000_uncertainty,
            '2000': noise_result2000_uncertainty,
            '4000': noise_result4000_uncertainty,
            '8000': noise_result8000_uncertainty
        }
        breach = {}
        for key in data_constant_noise:
            if key in standard_values.data_norms_day:
                if data_constant_noise[key] - standard_values.data_norms_day[key] < 0:
                    pass
                else:
                    a = str(key)
                    breach[a] = data_constant_noise_uncertainty[key] - standard_values.data_norms_day[key]
        normative_value = {
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
        'LMAX': 55.0}
        total_constant = {'breach': breach, 'normative_value': normative_value, 'data_constant_noise_uncertainty': data_constant_noise_uncertainty, 'data_constant_noise': data_constant_noise, 'info_measurements': info_measurements}
        return render(reqest, 'noise/alert.html', {'total_constant': total_constant})
    else:
        pass


class NoiseDetailView(DetailView):
    model = Noise
    template_name = 'noise/details_view.html'
    context_object_name = 'noise'


class NoiseUpdateView(UpdateView):
    model = Noise
    template_name = 'noise/update.html'

    form_class = NoiseForm


class NoiseDeleteView(DeleteView):
    model = Noise
    success_url = '/noise/'
    template_name = 'noise/delete.html'



