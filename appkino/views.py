import random

from django.shortcuts import render, redirect
from .models import *

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def index(req):
    film = ModelKino.objects.all()
    actor = ModelActor.objects.all()
    randomFilm = random.choice(film)
    data = {'film':film, 'actor':actor, 'random':randomFilm}
    return render(req, 'index.html', data)

from django.views import generic
class kinoList(generic.ListView):
    model = ModelKino

class kinoDetail(generic.DetailView):
    model = ModelKino

class actorList(generic.ListView):
    model = ModelActor
    paginate_by = 2
class actorDetail(generic.DetailView):
    model = ModelActor

class directorList(generic.ListView):
    model = ModelDirector
    paginate_by = 2

class directorDetail(generic.DetailView):
    model = ModelDirector

from django.contrib.auth.forms import UserCreationForm
from .forms import *
def register(req):
    # form = UserCreationForm
    if req.POST:
        form = FormRegister(req.POST)
        if form.is_valid():
            k1 = form.cleaned_data.get('username')
            k2 = form.cleaned_data.get('password1')
            k3 = form.cleaned_data.get('email')
            k4 = form.cleaned_data.get('first_name')
            k5 = form.cleaned_data.get('last_name')
            user = User.objects.create_user(username=k1, password=k2)
            # user1 = authenticate(username=k1, password=k2)
            user = User.objects.get(username=k1)
            user.email = k3
            user.last_name = k5
            user.first_name = k4
            user.save()
            ModelProfile.objects.create(balance=1000, podpiska_id=1, user_id=user.id)
            login(req, user)
            return redirect('home')
    else:
        form = FormRegister()
    data = {'form':form}
    return render(req, 'registration/registration.html', data)

def profile(req):

    return render(req, 'cabinet.html')

def profilechange(req):
    forma = FormPodpiska()
    data = {'form':forma}
    if req.POST:

        k1 = req.POST.get('item')
        user = User.objects.get(id=req.user.id)
        lastpodpiska = user.modelprofile.podpiska_id #Если нет денег, то не менять подписку
        pod = ModelPodpiska.objects.get(id=k1)

        user.modelprofile.podpiska_id = k1
        if user.modelprofile.balance >= pod.price: #Проверяет достаточно ли денег
            if user.modelprofile.podpiska_id != pod.id: #Проверяет не таже ли подписка
                user.modelprofile.balance = user.modelprofile.balance - pod.price #Вычитает баланс
                user.modelprofile.save()
            else:
                user.modelprofile.podpiska_id = lastpodpiska
        else:
            user.modelprofile.podpiska_id = lastpodpiska
        user.modelprofile.save()
        return redirect('cabinet')
    return render(req, 'cabinet.html', data)

def otziv(req, kinoid):
    if req.POST:
        k1 = req.POST.get('text')
        k2 = req.user.id
        k3 = req.user.username
        film = ModelKino.objects.get(id=kinoid)
        ModelOtziv.objects.create(text=k1, user_id=k2, film_id=kinoid)
        print(k1, k2, k3, kinoid)
        send
        return redirect(f'onekino', film.genre, kinoid)
    return redirect('home')