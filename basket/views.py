from django.shortcuts import render
from basket.models import *
from basket.forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect


@login_required(login_url='/auth/login')
def index(request):
    data = {}

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

    template_name = 'player/list_player.html'
    return render(request, template_name, data)

#hacer los index para team y coach
#arreglar la fecha y hora
def listcoach(request):
    data = {}

    # SELECT * FROM player
    object_list_coach = Coach.objects.all().order_by('-id')

    paginator = Paginator(object_list_coach, 10)
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
def listteam(request):
    data = {}

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



def add_player(request):
    data = {}
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('player_list')

    else:
        data['form'] = PlayerForm()

    template_name = 'player/add_player.html'
    return render(request, template_name, data)

def add_coach(request):
    data = {}
    if request.method == "POST":
        data['form'] = CoachForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('coach_list')

    else:
        data['form'] = CoachForm()

    template_name = 'player/add_Coach.html'
    return render(request, template_name, data)

def add_team(request):
    data = {}
    if request.method == "POST":
        data['form'] = TeamForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('team_list')

    else:
        data['form'] = TeamForm()

    template_name = 'player/add_Team.html'
    return render(request, template_name, data)

def detail(request, player_id):

    data = {}
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

def edit_player(request, player_id):
    data = {}
    if request.POST:
        formPlayer = EditPlayer(request.POST, request.FILES, instance=Player.objects.get(pk=player_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return redirect('player_list')
    template_name = 'player/edit_player.html'
    data['player'] = EditPlayer(instance=Player.objects.get(pk=player_id))

    return render(request, template_name, data)

def edit_team(request, team_id):
    data = {}
    if request.POST:
        formPlayer = EditTeam(request.POST, request.FILES, instance=Team.objects.get(pk=team_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return redirect('team_list')
    template_name = 'player/edit_team.html'
    data['team'] = EditTeam(instance=Team.objects.get(pk=team_id))

    return render(request, template_name, data)

def edit_coach(request, coach_id):
    data = {}
    if request.POST:
        formPlayer = EditCoach(request.POST, request.FILES, instance=Coach.objects.get(pk=coach_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return redirect('coach_list')
    template_name = 'player/edit_coach.html'
    data['coach'] = EditCoach(instance=Coach.objects.get(pk=coach_id))

    return render(request, template_name, data)

def Delete(request, id):
    data = {}
    template_name = 'list_player.html'
    data['player'] = Player.objects.all()
    Player.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('player_list'))
def Delete_coach(request, coach_id):
    data = {}
    template_name = 'list_coach.html'
    data['coach'] = Coach.objects.all()
    Coach.objects.filter(pk=coach_id).delete()
    return HttpResponseRedirect(reverse('coach_list'))
def Delete_team(request, team_id):
    data = {}
    template_name = 'list_team.html'
    data['team'] = Team.objects.all()
    Team.objects.filter(pk=team_id).delete()
    return HttpResponseRedirect(reverse('team_list'))



