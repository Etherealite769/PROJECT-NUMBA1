from django.shortcuts import render, redirect, get_object_or_404
from .models import UserInput
from .forms import UserInputForm

def home(request):
    if request.method == "POST":
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserInputForm()

    users = UserInput.objects.all()
    return render(request, "home.html", {"form": form, "users": users})

def delete_user(request, user_id):
    user = get_object_or_404(UserInput, id=user_id)
    user.delete()
    return redirect("home")


# Create your views here.
