from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'description': 'Kandang Kucing',
        'price': 20000,
        'amount': 5
    }

    return render(request, "main.html", context)