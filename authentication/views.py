from django.shortcuts import redirect, render

from .forms import SignupForm
from django.contrib.auth import logout

# Create your views here.

def register(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            # save the user to db and redirect to home page
            form.save()
            return redirect('index')
    else:
        form = SignupForm()

    context={'form':form}
    return render(request,'authentication/register.html',context)


def Logout(request):
    logout(request)
    return redirect('index')

