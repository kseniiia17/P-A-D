from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import *
from django.contrib.auth import login, logout


def news_home(request):
    animals = Animals.objects.all()
    color = Color.objects.all()
    cat = Category.objects.all()
    breed = Breed.objects.all()
    context = {'animals': animals, 'color': color, 'cat': cat, 'breed': breed}
    return render(request, 'news/news_home.html', context)


class NewsUpdateView(UpdateView):
    model = Animals
    template_name = 'news/create.html'

    form_class = AnimalsForm


class NewsDeleteView(DeleteView):
    model = Animals
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def ColorDeleteView(request,pk):
    color = Color.objects.get(id=pk)
    color.delete()
    return redirect('news_home')




def create(request):
    error = ''
    if request.method == 'POST':
        form = AnimalsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Данные были заполнены неверно'

    form = AnimalsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)

def create_color(request):
    error = ''
    if request.method == 'POST':
        form = ColorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Данные были заполнены неверно'

    form = ColorsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create_color.html', data)

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    if request.user.is_authenticated:
        return redirect("profile")
    else:
        return render(request, "news/registr.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = LoginForm()
    if request.user.is_authenticated:
        return redirect("profile")
    else:
        return render(request, "news/login.html", {"form": form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('news_home')

def profile_view(request):
    user = User.objects.get(id=request.user.id)
    users = User.objects.all()
    context = {
        'user': user,
        'users': users
    }
    return render(request, "news/profile.html", context)

def update_user(request, user_id):
    user = User.objects.get(pk=user_id)
    session_user = request.user
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UpdateUserForm(instance=user)
    return render(request, 'news/edit_user.html', {'form': form, 'user': user, 'session_user': session_user})




