from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import productform
# Create your views here.
class insert (View):
    def get (self,request):
        form = productform()
        return render(request,"input.html",{'form':form})
    def post (self,request):
        form = productform(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("p_data submited successfully")

