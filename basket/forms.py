from django.forms import ModelForm
from basket.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PlayerForm(ModelForm):
    
    class Meta:
        model = Player
        fields = ['rut', 'dv', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']

class CoachForm(ModelForm):
    
    class Meta:
        model = Coach 
        fields = ['name', 'age', 'email', 'nickname', 'rut', 'dv','team',]
        

class UserForm(ModelForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','password1','password2',]

class RosterMatchForm(ModelForm):
    
    class Meta:
        model = RosterMatch
        fields = ['visita', 'local', 'match']
    
class TeamForm(ModelForm):
    
    class Meta:
        model = Team
        fields = ['name', 'logo', 'description']
        
class EditPlayer(ModelForm):
    
    def init(self, args, kwargs):
        super(EditPlayer, self).init(args, kwargs)
        self.fields['picture'].required = False

    class Meta:
        model = Player
        fields = ['rut', 'dv', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']
        
class EditTeam(ModelForm):
    def init(self, args, kwargs):
        super(EditTeam, self).init(args, kwargs)
        self.fields['logo'].required = False

    class Meta:
        model = Team
        fields = ['name','description','logo','code']
        
class EditCoach(ModelForm):

    class Meta:
        model = Coach
        fields = ['name','age', 'email','nickname','rut','dv']
        
class MatchForm(ModelForm):
    
    class Meta:
        model = Match
        fields = ['local', 'visit', 'date']
        
class RosterMatchForm(ModelForm):
    
    class Meta:
        model = RosterMatch
        fields = ['visita', 'local', 'match']
        
class RosterForm(ModelForm):
    
    class Meta:
        model = Roster
        fields = ['team', 'name']
        
class EditRoster(ModelForm):
    
    class Meta:
        model = Roster
        fields = ['team', 'name']
        
class EditRostermatch(ModelForm):
    
    class Meta:
        model = RosterMatch
        fields = ['visita', 'local', 'match']