from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from.models import Grain

# Create your views here.
def index (request):
    return render(request,'farmeasy/index.html')


def grains(request):
    latest_release = Grain.objects.order_by('-release_date')
    context = {'latest_release': latest_release}
    return render(request, 'bowl/market.html', context)
