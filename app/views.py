from django.shortcuts import render
import datetime
# Create your views here.
def filter(request):
    da=datetime.datetime.now()
    data="This is Content from Backend"
    d={"data":data,"da":da}
    return render(request,'filter.html',d)