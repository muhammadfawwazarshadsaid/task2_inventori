from django.shortcuts import render

def show_main(request):
    context = [
        {
            'no': 1,
            'name': 'Kandang Kucing',
            'description': "Kandang kucing dengan anti karat dan anti bau",
            'amount': 5,
            'price': 74000,
        },
        {
            'no': 2,
            'name': 'Pasir 200g',
            'description': "Pasir putih anti lengket",
            'amount': 91,
            'price': 10000,
        },
        {
            'no': 3,
            'name': 'Royal Candi 1kg',
            'description': "Makanan kucing berkualitas premium",
            'amount': 241,
            'price': 240000,
        },
        # Add more dictionaries as needed
    ]

    return render(request, "main.html", {'items': context})
