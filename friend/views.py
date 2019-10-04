from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, './friend/home.html')

def tpd(request):
    return render(request, './friend/auth.html')





