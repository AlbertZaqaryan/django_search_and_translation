from django.shortcuts import render
from .models import Nout
from django.db.models import Q
# Create your views here.


def index(request):
    search = request.GET.get('search')
    if search:
        nout_list = Nout.objects.filter(Q(name__icontains=search) | Q(price__icontains=search))
    else:
        nout_list = Nout.objects.all()
    return render(request, 'main/index.html', context={
        'nout_list':nout_list
    })

def index_detail(request, slug):
    one_nout = Nout.objects.get(slug=slug)
    return render(request, 'main/index_detail.html', context={
        'one_nout':one_nout
    })