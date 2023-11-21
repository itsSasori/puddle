from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.

def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    items = Item.objects.filter(Q(name__icontains=q) | Q(category__name__icontains=q))
    categories = Category.objects.all()
    context={'items':items,'categories':categories}
    return render(request,'items/index.html',context)


def detail(request ,pk):
    item=Item.objects.get(id=pk)
    related_item = Item.objects.filter(category=item.category , is_sold=False).exclude(id=pk)
    context={'item':item,'related_item':related_item}
    return render(request,'items/detail.html',context)

def new_items(request):
    if request.method == "POST":
        form = NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            new_items = form.save(commit=False)
            new_items.created_by = request.user
            new_items.save()
            return redirect('detail' ,pk=new_items.id)
    else:
        form = NewItemForm()

    context={'form':form}
    return render(request,"items/new_items.html",context)


def dashboard(request):
    items = Item.objects.filter(created_by=request.user)
    context={'items':items}
    return render(request,'items/dashboard.html',context)

def edit_items(request,pk):
    items = Item.objects.get(id=pk)
    if request.method == "POST":
        form = EditItemForm(request.POST,request.FILES,instance=items)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditItemForm(instance=items)
    
    context={'form':form}
    return render(request,'items/new_items.html',context)

def delete_items(request,pk):
    items=Item.objects.get(id=pk , created_by=request.user)
    items.delete()
    return redirect("dashboard")

