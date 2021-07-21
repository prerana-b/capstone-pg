from django.shortcuts import render
# Create your views here.

posts = [
    {
        'owner': 'Prerana',
        'pg_name': 'Siddhachal',
        'amount': 'Rs 10,000/month',
        'date_posted': 'January 14, 2021'
    },
    {
        'owner': 'Jane',
        'pg_name': 'Jasmine Tower',
        'amount': 'Rs 15,000/month',
        'date_posted': 'January 21, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'properties/home.html', context)


def about(request):
    return render(request, 'properties/about.html', {'title':'About'})
