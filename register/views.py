from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from . forms import Registerform
# Create your views here.
def register(request):
    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Registerform()
    return render(request, 'register/register.html', {'form': form})

# Create your views here.
