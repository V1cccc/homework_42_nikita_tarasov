from django.shortcuts import render


def index_view(request):
    if request.method == 'GET':
        return render(request, 'calc_input.html')
    elif request.method == 'POST':
        try:
            a = int(request.POST.get('a'))
            b = int(request.POST.get('b'))
            mark = request.POST.get('flexRadioDefault')
            int_validation(a, b)
            context = {
                'a': a,
                'b': b,
                'flexRadioDefault': mark,
                'c': operation(mark, a, b)
            }
            return render(request=request, template_name='calc_result.html', context=context)
        except ValueError:
            context = {
                'error': 'Enter both numbers!'
            }
            return render(request=request, template_name='error.html', context=context)

def operation(value, a, b):
    if value == '+':
        c = a + b
        return c
    if value == '-':
        c = a - b
        return c
    if value == '*':
        c = a * b
        return c
    if value == '/':
        c = a / b
        return c


def int_validation(value1, value2):
    try:
        return isinstance(value1, (float, int)), isinstance(value2, (float, int))
    except ValueError:
        print('Ошибка ввода')
        exit()
