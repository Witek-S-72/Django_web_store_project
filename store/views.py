from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib.auth import login, logout, authenticate
from store.models import Profile, Category
from django.contrib.auth.models import User
from store.forms import CreateUserProfileForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


def store(request):
    context = {}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def sign_up_view(request):
    if request.method == 'POST':
        form = forms.ResisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('store')

    else:
        form = forms.ResisterUserForm()

    return render(request, 'registration/sign_up.html', {'form': form})

def profile_view(request):
    # profile = get_object_or_404(Profile, user_id=request.user.pk)
    try:
        profile = Profile.objects.get(user_id=request.user.pk)
    except Profile.DoesNotExist:
        return redirect('profile_create')
    context = {'profile': profile}
    return render(request, 'store/profile.html', context)


class ProfileCreateView(CreateView):
    template_name = 'store/form.html'
    form_class = CreateUserProfileForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        # here we set default logged in user
        form.instance.user = self.request.user
        return super().form_valid(form)

