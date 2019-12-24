from django.shortcuts import render
from portfolio.models import Portfolio
from .models import Contact


# Create your views here.
def portfolio_index(request):
    portfolio = Portfolio.objects.all()
    context = {
        'portfolios': portfolio
    }
    return render(request, 'portfolio_index.html', context)


def portfolio_detail(request, pk):
    portfolio = Portfolio.objects.get(pk=pk)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'portfolio_detail.html', context)

def contact(request):
    if request.method == "POST":
        firstname_r = request.POST.get('firstname')
        lastname_r = request.POST.get('lastname')
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')

        c = Contact(firstname=firstname_r, lastname=lastname_r, email=email_r, subject=subject_r)
        c.save()

        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')