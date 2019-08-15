#pk_d700c3f308664b5d957b9270356dbd55
from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# Create your views here.
def home(request):
    import requests
    import json
    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_req = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_d700c3f308664b5d957b9270356dbd55")
        try:
            api = json.loads(api_req.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol in the search bar"})
    
    
def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    
    if request.method == 'POST':
        form = StockForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        return render(request, 'add_stock.html', {'ticker': ticker})