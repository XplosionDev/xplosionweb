from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from . import models
from django.contrib.auth.password_validation import password_validators_help_texts

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
       
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserProfileinfo(forms.ModelForm):

    class Meta:
        model= models.Coachs
        fields = [
            'city',
            'state',
        ]


class TeamUpdate(forms.ModelForm):

    class Meta:
        model= models.Teams
        fields = [
            'team_name',
            'mascot',
            'city',
            'state',
        ]

class PlayerUpdate(forms.ModelForm):

    class Meta:
        model= models.Players
        fields =('team','hometown','homestate','first_name','last_name','email',
                 'height_feet','height_inches','weight','batting_orientation','player_number','position')

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(min_length=8,widget=forms.PasswordInput)
    first_name=forms.CharField(label='first_name')
    last_name=forms.CharField(label='last_name')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'email2',
            'password'
        ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email
class Useremailedit(forms.Form):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email
class Userflnameedit(forms.Form):
    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='last_name')


class teamregistration(forms.ModelForm):
    team_name=forms.CharField(label='team_name')
    class Meta:
        model=models.Teams
        fields=('team_name','mascot','city','state')
        exclude = ('coach',)
    """def clean(self):
        team_name = self.cleaned_data.get('team_name')
        teamname_qs = models.Team.objects.filter(team_name=team_name)
        if teamname_qs.exists():
            raise forms.ValidationError("This team name has already been registered")
        return team_name"""
class PlayerRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')



    class Meta:
        model = models.Players
        fields =('team','hometown','homestate','first_name','last_name','email','email2',
                 'height_feet','height_inches','weight','batting_orientation','player_number','position')
        exclude=('password','username','type')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PlayerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['team'].queryset = models.Teams.objects.filter(coach=self.user)
    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = models.Players.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email


    """def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        team = self.cleaned_data.get('team')
        first_qs = models.Player.objects.filter(first_name=first_name)
        last_qs = models.Player.objects.filter(last_name=last_name)
        team_qs = models.Player.objects.filter(team=team)

        if first_qs.exists() and last_qs.exists() and team_qs.exists():
            raise forms.ValidationError("This name already exist has already been registered")
        return first_name,last_name,team"""

    """def clean_last_name(self):
        first = self.cleaned_data.get('first_name')
        last = self.cleaned_data.get('last_name')
        first_qs = models.Player.objects.filter(first=first)
        last_qs = models.Player.objects.filter(first=last)

        if first_qs.exists() and last_qs.exists():
            raise forms.ValidationError("This name already exist has already been registered")
        return last"""













