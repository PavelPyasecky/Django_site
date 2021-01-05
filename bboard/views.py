from django.shortcuts import render


def index(request):
    return render(request, 'bboard/index.html')

def buyer_page(request):
    return render(request, 'bboard/buyer.html')

def seller_page(request):
    return render(request, 'bboard/seller.html')

def ilyapiasetski_page(request):
    return render(request, 'bboard/ilyapiasetski.html')

def legal_notice_page(request):
    return render(request, 'bboard/legal-notice.html')
