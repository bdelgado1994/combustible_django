from django.shortcuts import render,redirect
from django.views.generic import *
from ctrl_comb.models import *
from .forms import *

class BrandList (ListView):
    template_name='ctrl_comb/brand.html'
    context_object_name="obj"
    model=Brand
    ordering=["description"]

def save_brand(request):
    context={}
    template_name="ctrl_comb/brand-list.html"
    
    if request.method=="POST":
        id=request.POST.get("id")
        description=request.POST.get("description")
        o=None
        if id:
            o=Brand.objects.get(pk=id)
            o.description=description
            o.save()
        else:
            o=Brand.objects.create(description=description)
    obj=Brand.objects.all().order_by("description")
    r = Brand.objects.filter(id = o.id).first()
    context["obj"]=obj
    context["reg"] = r
    return render(request,template_name,context=context)

def brand_delete(request,pk):
    context={}
    template_name="ctrl_comb/brand-list.html"
    if pk is not None:
        o=Brand.objects.get(pk=pk)
        if o is not None:
            o.delete()
    obj=Brand.objects.all().order_by("description")
    context["obj"]=obj
    return render(request,template_name,context=context)

def brand_edit(request,pk=None):
    context={}
    template_name="ctrl_comb/brand-frm.html"
    if pk:
        o=Brand.objects.get(pk=pk)
        frm=BrandForm(instance=o)
    else:
        frm=BrandForm()
    context["form"]=frm
    context["obj"]=o
    return render(request,template_name,context=context)

class ModeloList (ListView):
    template_name='ctrl_comb/modelo.html'
    context_object_name="obj"
    model=Modelo
    ordering=["brand","description"]