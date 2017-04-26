from django.shortcuts import render

# Create your views here.
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,


    )
from random import randint
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User,Group
from django.http import Http404

from .forms import UserLoginForm, UserRegisterForm,UserProfileinfo,PlayerRegistrationForm,teamregistration,TeamUpdate,PlayerUpdate,Useremailedit,Userflnameedit
from . import models


def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        """if user.groups.count()==0:
            g = Group.objects.get(name="Coach")
            user.groups.add(g)"""
        login(request, user)
        if next:
            return redirect('/')
        return redirect('Coach_Profile')
    return render(request, "registration/login.html", {"form":form, "title": title})

def view_profile(request, pk=None):

    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    teams=user.profile.teams_set.all()
    args = {'user': user, 'teams': teams}
    return render(request, 'profile/Profile_Coach.html', args)
@login_required
def edit_profile(request, pk=None):
    if request.method == 'POST':
        form = UserProfileinfo(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            messages.success(request, ('Your profile was successfully updated! Go to profile to see changes!'))

            form.save()

            if pk:
                user = User.objects.get(pk=pk)
            else:
                user = request.user
            profile= request.user.profile
            args = {'user': user, 'profile': profile}
            return render(request, 'profile/Profile_Coach_Edit_SuccessPage.html', args)

        else:
            messages.error(request, ('Please correct the error below.'))

    form = UserProfileinfo(instance=request.user)
    args = {'form': form}
    return render(request, 'profile/Profile_Coach_Edit.html', args)

def email_edit(request):
    form = Useremailedit(request.POST or None)
    user=request.user
    if request.method=='POST':
        form = Useremailedit(request.POST)
        if form.is_valid():

            email=form.cleaned_data.get('email')
            user.email=email
            user.save()
            return render(request,"profile/Profile_Coach_Edit_Email_SuccessPage.html")

    context = {
        "form": form,
    }

    return render(request, "profile/Profile_Coach_Edit_Email.html", context)

def flname_edit(request):
    form = Userflnameedit(request.POST or None)
    user=request.user
    if request.method=='POST':
        form = Userflnameedit(request.POST)
        if form.is_valid():

            fname=form.cleaned_data.get('first_name')
            lname=form.cleaned_data.get('last_name')
            user.first_name=fname
            user.last_name=lname
            user.save()
            return render(request,"profile/Profile_Coach_Edit_flname_SuccessPage.html")

    context = {
        "form": form,
    }

    return render(request, "profile/Profile_Coach_Edit_flname.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.is_confirmed=False
        user.save()
        new_user = authenticate(username=user.username, password=password)
       # g = Group.objects.get(name="Coach")
        #new_user.groups.add(g)
        login(request, new_user)
        if next:
            return redirect(next)
        return render(request, "profile/Profile_Coach.html")

    context = {
        "form": form,
    }
    return render(request, "profile/Create_Account_Coach.html", context)
@login_required
def team_view(request,pk=None):
    if request.method == 'POST':
        form = teamregistration(request.POST)

        if form.is_valid():
            user=request.user.profile
            messages.success(request, ('Your team has been added!'))
            team=form.save(commit=False)
            team.coach=user
            team.save()
            if pk:
                user = User.objects.get(pk=pk)
            else:
                user = request.user

            args = {'user': user}
            return render(request, 'profile/Profile_Coach_Add_Team_SuccessPage.html', args)

        else:
            messages.error(request, ('Please correct the error below.'))

    form = teamregistration(request.POST or None)
    args = {'form': form}
    return render(request, 'profile/Profile_Coach_Add_Team.html', args)
def Player_view(request,pk=None):
    if request.method == 'POST':

        form =  PlayerRegistrationForm(request.POST,user=request.user.profile)

        if form.is_valid():

            messages.success(request, ('Player has been added!'))
            Player=form.save(commit=False)
            Player.password= User.objects.make_random_password(length=8)
            first=Player.first_name
            last=Player.last_name
            Player.username=first[0]+last+str(randint(0,50))
            Player.type="Coach-Dependent"
            Player.save()
            if pk:
                user = User.objects.get(pk=pk)
            else:
                user = request.user

            args = {'user': user}
            return render(request, 'profile/Profile_Coach_Add_Player_SuccessPage.html', args)

        else:
            messages.error(request, ('Please correct the error below.'))

    form = PlayerRegistrationForm(request.POST or None,user=request.user.profile)
    args = {'form': form}
    return render(request, 'profile/Profile_Coach_Add_Player.html', args)


def logout_view(request):
    logout(request)
    return render(request, "registration/logout.html")


def index(request):
    return render(request, "profile/index.html")


def Coach_Profile_Player_View(request,player_id):
    try:
        player= models.Players.objects.get(id=player_id).swings_set.all()
        pname= models.Players.objects.get(id=player_id)
    except models.Players.DoesNotExist:
        raise Http404("Player Does not exist")
    args={'player':player,'pname': pname}
    return render(request, 'profile/Profile_Coach_Player_View.html', args)

def Coach_Profile_Player_View_Update(request,player_id):
    try:
        player= models.Players.objects.get(id=player_id)
        if request.method == 'POST':
            form = PlayerUpdate(request.POST, instance=player)

            if form.is_valid():

                form.save()


                return render(request, 'profile/Profile_Coach_Team_SuccessPage.html')

            else:
                messages.error(request, ('Please correct the error below.'))
    except models.Teams.DoesNotExist:
        raise Http404("Team does not exist")
    form = PlayerUpdate(request.POST or None,instance=player)
    args = {'form': form}
    return render(request, 'profile/Profile_Coach_Player_Update.html', args)

def Coach_Profile_Player_View_Delete(request,player_id):
    try:
        models.Players.objects.get(id=player_id).delete()
    except models.Teams.DoesNotExist:
        raise  Http404("Player does not exist")
    return render(request, 'profile/Profile_Coach_Team_SuccessPage.html')

def Coach_Profile_Team(request):
    team = request.user.profile.teams_set.all()
    args = {'team':team}
    return render(request, 'profile/Profile_Coach_Team.html', args)
def Coach_Profile_Team_View(request,team_id):
    try:
        team=models.Teams.objects.get(id=team_id).players_set.all()
        #players=models.Players.objects.filter(team=team).all()
        #players=models.Players.objects.filter(team=team).get()
    except models.Teams.DoesNotExist:
        raise Http404("Team does not exist")
    #players=team.players_set.all()
    return render(request, 'profile/Profile_Coach_Team_View.html', {'players':team})
def Coach_Profile_Team_View_Update(request,team_id):
    try:
        team = models.Teams.objects.get(id=team_id)
        if request.method == 'POST':
            form = TeamUpdate(request.POST, instance=team)

            if form.is_valid():

                form.save()


                return render(request, 'profile/Profile_Coach_Team_SuccessPage.html')

            else:
                messages.error(request, ('Please correct the error below.'))
    except models.Teams.DoesNotExist:
        raise Http404("Team does not exist")
    form = TeamUpdate(request.POST or None,instance=team)
    args = {'form': form}
    return render(request, 'profile/Profile_Coach_Team_Update.html', args)
def Coach_Profile_Team_View_Delete(request,team_id):
    try:
        models.Teams.objects.get(id=team_id).delete()
    except models.Teams.DoesNotExist:
        raise  Http404("Team does not exist")
    return render(request, 'profile/Profile_Coach_Team_SuccessPage.html')

def Coach_Delete(request):
    request.user.delete()
    return render(request, 'profile/Profile_Coach_Delete_SuccessPage.html')
def Coach_Delete_Confirmation(request):
    return render(request, 'profile/Profile_Coach_Delete_Confirmation.html')