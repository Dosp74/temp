from django.shortcuts import render
# from django.http import HttpResponse
from .models import MainContent

def index(request):
    # return HttpResponse("Hello World")

    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}

    return render(request, 'product/content_list.html', context)