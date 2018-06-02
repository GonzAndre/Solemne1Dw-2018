from django.shortcuts import render
from basket.models import *
from basket.forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

def decorador(user,coach):
    if(coach):
        try:
            Coach.objects.get(user=user)
            return False
        except Exception as e:
            return True
    else:
        try:
            Coach.objects.get(user=user)
            return True
        except Exception as e:
            return False

@login_required(login_url='/auth/login')
def index(request):
    data = {}
    data['name'] = 'Players'
    data["request"] = request
    
    try:
        coach = Coach.objects.get(user=request.user)
        object_list = Player.objects.filter(team = coach.team).order_by('-id')

        paginator = Paginator(object_list, 10)
        page = request.GET.get('page')

        try:
            data['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            data['object_list'] = paginator.page(1)
        except EmptyPage:
            data['object_list'] = paginator.page(paginator.num_pages)
            
        template_name = 'player/select_player.html'
        return render(request, template_name, data)
        
    except Exception as e:                       
        template_name = 'player/admin.html'
        return render(request, template_name, data)
    
@login_required(login_url='/auth/login')    
def listplayer(request):
    if(decorador(request.user,False)):
        return redirect('list')
    data = {}
    data["request"] = request
            # SELECT * FROM player
    object_list = Player.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'player/list.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def listcoach(request):
    if(decorador(request.user,False)):
        return redirect('list')
    data = {}
    data['name'] = 'Coachs'
    data["request"] = request

    # SELECT * FROM player
    object_list = Coach.objects.all().order_by('-id')
    
    print(object_list)

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list_coach'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list_coach'] = paginator.page(1)
    except EmptyPage:
        data['object_list_coach'] = paginator.page(paginator.num_pages)

    template_name = 'player/list_coach.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def listteam(request):
    if(decorador(request.user,False)):
        return redirect('list')
    data = {}
    data['name'] = 'Teams'
    data["request"] = request

    # SELECT * FROM player
    object_list = Team.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'player/list_team.html'
    return render(request, template_name, data)

def listmatch(request):
    data = {}

    # SELECT * FROM player
    object_list = Match.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'player/list_match.html'
    return render(request, template_name, data)

def listrostermatch(request):
    data = {}

    # SELECT * FROM player
    object_list = RosterMatch.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'player/list_roster.html'
    return render(request, template_name, data)

#hacer los index para team y coach
#arreglar la fecha y hora
#redireccionas a los list de coach y team

@login_required(login_url='/auth/login')
def add_player(request):
    if(decorador(request.user,False)):
        return redirect('list')
    data = {}
    data['title'] = "Add Player"
    data["request"] = request
    data['form2'] = None
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('player_list')

    else:
        data['form'] = PlayerForm()

    template_name = 'player/add.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def add_coach(request):
    if(decorador(request.user,False)):
        return redirect('list')
    data = {}
    data['title'] = "Add Coach"
    data["request"] = request
    if request.method == "POST":
        print(request.POST)
        data['form'] = CoachForm(request.POST, request.FILES)
        data['form2'] = UserForm(request.POST, request.FILES)

        if data['form2'].is_valid():
            # aca el formulario valido
            if data['form'].is_valid():
                sav = data['form'].save(commit=False)
                sav2 = User.objects.create_user(username= request.POST['username'], password= request.POST['password1'])
                sav.user = sav2
                sav.save()
                
            return redirect('coach_list')

    else:
        data['form2'] = UserForm()
        data['form'] = CoachForm()

    template_name = 'player/add_coach.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def add_team(request):
    if(decorador(request.user,False)):
        return redirect('list')
    data = {}
    data['title'] = "Add Team"
    data["request"] = request
    data['form2'] = None
    if request.method == "POST":
        data['form'] = TeamForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('team_list')

    else:
        data['form'] = TeamForm()

    template_name = 'player/add.html'
    return render(request, template_name, data)

def add_match(request):
    data = {}
    if request.method == "POST":
        data['form'] = MatchForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('list_match')

    else:
        data['form'] = MatchForm()

    template_name = 'player/add_Match.html'
    return render(request, template_name, data)


def add_rostermatch(request):
    data = {}
    if request.method == "POST":
        data['form'] = RosterMatchForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('rostermatch_list')

    else:
        data['form'] = RosterMatchForm()

    template_name = 'player/add_Rostermatch.html'
    return render(request, template_name, data)

def add_roster(request):
    data = {}
    if request.method == "POST":
        data['form'] = RosterForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('roster_list')

    else:
        data['form'] = RosterForm()

    template_name = 'player/add_Roster.html'
    return render(request, template_name, data)


@login_required(login_url='/auth/login')
def detail(request, player_id):

    data = {}
    data["request"] = request
    template_name = 'player/detail_player.html'

    # SELECT * FROM player WHERE id = player_id
    data['player'] = Player.objects.get(pk=player_id)
    # import pdb;pdb.set_trace()

    return render(request, template_name, data)

def detail_coach(request, coach_id):

    data = {}
    template_name = 'player/detail_coach.html'

    # SELECT * FROM player WHERE id = coach_id
    data['coach'] = Coach.objects.get(pk=coach_id)
    # import pdb;pdb.set_trace()

    return render(request, template_name, data)
def detail_team(request, team_id):

    data = {}
    template_name = 'player/detail_team.html'

    # SELECT * FROM player WHERE id = player_id
    data['team'] = Team.objects.get(pk=team_id)
    # import pdb;pdb.set_trace()
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def edit_player(request, player_id):
    if(decorador(request.user,False)):
        return redirect('list')
    data = {}
    data['title'] = "Edit Player"
    data["request"] = request
    if request.POST:
        formPlayer = EditPlayer(request.POST, request.FILES, instance=Player.objects.get(pk=player_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return redirect('player_list')
    template_name = 'player/edit.html'
    data['data'] = EditPlayer(instance=Player.objects.get(pk=player_id))

    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def edit_team(request, team_id):
    if(decorador(request.user,False)):
        return redirect('list')
    data = {}
    data['title'] = "Edit Team"
    data["request"] = request
    if request.POST:
        formPlayer = EditTeam(request.POST, request.FILES, instance=Team.objects.get(pk=team_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return redirect('team_list')
    template_name = 'player/edit.html'
    data['data'] = EditTeam(instance=Team.objects.get(pk=team_id))

    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def edit_coach(request, coach_id):
    if(decorador(request.user,False)):
        return redirect('list')
    data = {}
    data['title'] = "Edit Coach"
    data["request"] = request
    if request.POST:
        formPlayer = EditCoach(request.POST, request.FILES, instance=Coach.objects.get(pk=coach_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return redirect('coach_list')
    template_name = 'player/edit.html'
    data['data'] = EditCoach(instance=Coach.objects.get(pk=coach_id))

    return render(request, template_name, data)

def edit_match(request, match_id):
    data = {}
    if request.POST:
        formPlayer = EditMatch(request.POST, request.FILES, instance=Match.objects.get(pk=match_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return redirect('match_list')
    template_name = 'player/edit_match.html'
    data['match'] = EditMatch(instance=Match.objects.get(pk=Match_id))

    return render(request, template_name, data)
def edit_roster(request, roster_id):
    data = {}
    if request.POST:
        formPlayer = EditRoster(request.POST, request.FILES, instance=Roster.objects.get(pk=roster_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return redirect('roster_list')
    template_name = 'player/edit_roster.html'
    data['roster'] = EditRoster(instance=Roster.objects.get(pk=roster_id))

    return render(request, template_name, data)

def edit_rostermatch(request, rostermatch_id):
    data = {}
    if request.POST:
        formPlayer = EditRostermatch(request.POST, request.FILES, instance=RosterMatch.objects.get(pk=rostermatch_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return redirect('rostermatch_list')
    template_name = 'player/edit_rostermatch.html'
    data['rostermatch'] = EditRostermatch(instance=RosterMatch.objects.get(pk=rostermatch_id))

    return render(request, template_name, data)

def Delete(request, id):
    data = {}
    template_name = 'list_player.html'
    data['player'] = Player.objects.all()
    Player.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('player_list'))

def Delete_coach(request, coach_id, user_id):
    data = {}
    template_name = 'list_coach.html'
    data['coach'] = Coach.objects.all()
    User.objects.filter(pk=user_id).delete()
    Coach.objects.filter(pk=coach_id).delete()
    return HttpResponseRedirect(reverse('coach_list'))

def Delete_team(request, team_id):
    data = {}
    template_name = 'list_team.html'
    data['team'] = Team.objects.all()
    Team.objects.filter(pk=team_id).delete()
    return HttpResponseRedirect(reverse('team_list'))

def Delete_match(request, match_id):
    data = {}
    template_name = 'list_match.html'
    data['match'] = Match.objects.all()
    Match.objects.filter(pk=match_id).delete()
    return HttpResponseRedirect(reverse('match_list'))

def Delete_roster(request, roster_id):
    data = {}
    template_name = 'list_roster.html'
    data['roster'] = Roster.objects.all()
    Roster.objects.filter(pk=roster_id).delete()
    return HttpResponseRedirect(reverse('roster_list'))

def Delete_rostermatch(request, roster_id):
    data = {}
    template_name = 'list_rostermatch.html'
    data['rostermatch'] = Rostermatch.objects.all()
    Rostermatch.objects.filter(pk=rostermatch_id).delete()
    return HttpResponseRedirect(reverse('rostermatch_list'))

def add_roster(request):
    if(decorador(request.user,False)):
        return redirect('rosters')
    data = {}
    data["request"] = request
    if request.method == "POST":
        print(request.POST)
        data['form'] = RosterMatchForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            if data['form'].is_valid():
                sav = data['form'].save(commit=False)
                
            return redirect('rosters')

    else:
        data['form'] = RosterMatchForm()

    template_name = 'player/select_player.html'
    return render(request, template_name, data)

def general(request):
    data = {}
    data["request"] = request
            # SELECT * FROM player
    object_list = Match.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'player/index.html'
    return render(request, template_name, data)


