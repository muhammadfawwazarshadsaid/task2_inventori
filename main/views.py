from django.shortcuts import render

def show_main(request):
    context = {
        'no': 1,
        'name': 'Kandang kucing',
        'description': 'Kandang kucing anti jebol dan anti bau.',
        'price': 20000,
        'amount': 92
    }

    return render(request, "main.html", context)