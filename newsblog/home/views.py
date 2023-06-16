from django.shortcuts import render

from .models import portal, st, slider


# Create your views here.
def home(request):
    obj = portal.objects.all()
    obj1 = st.objects.all()
    obj2 = slider.objects.all()

    return render(request, 'index.html', {'data': obj, 'ss': obj1, 'news': obj2})


def about(request):
    return render(request, 'about.html')
