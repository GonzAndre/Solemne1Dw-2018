from django.db import models
from basket.defines import POSITION_PLAYER_CHOICES


class Team(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos')
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=120)
    nickname = models.CharField(max_length=120)
    birthday = models.DateField()
    age = models.PositiveIntegerField()
    email = models.EmailField()
    height = models.PositiveIntegerField(help_text="Altura en cm")
    weight = models.PositiveIntegerField(help_text="Peso en gramos")
    picture = models.ImageField(upload_to='picture_players')
    position = models.CharField(max_length=60, choices=POSITION_PLAYER_CHOICES)
#    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    team = models.OneToOneField('Team', on_delete = models.CASCADE)
    class Meta:
        unique_together = (('team'),)

    rut = models.CharField(max_length=8)
    dv = models.PositiveIntegerField()

    def full_rut(self):
        return '{}-{}' . format(self.rut, self.dv)

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    nickname = models.CharField(max_length=120)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    rut = models.CharField(max_length=8)
    dv = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    def full_rut(self):
        return '{}-{}' . format(self.rut, self.dv)
    
class Match(models.Model):
    local = models.ForeignKey('Team', on_delete = models.CASCADE,related_name='match_local')
    visit = models.ForeignKey('Team', on_delete = models.CASCADE,related_name='match_visit')
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def str(self):
        return '%s v/s %s' % (self.local.name, self.visit.name)

#class InterRoster(models.Model):
#    match = models.OneToOneField('Match', on_delete=models.CASCADE)
#    local = models.ForeignKey('Roster', on_delete=models.CASCADE, related_name='InterRoster_local')
#    visit = models.ForeignKey('Roster', on_delete=models.CASCADE, related_name='InterRoster_visit')
#
#    class Meta:
#        unique_together = (('match', 'local', 'visit'),)
#
#    def str(self):
#        return '%s v/s %s - %s' % (self.local.name, self.visit.name, self.match.date)
    
class RosterMatch(models.Model):
    local = models.ForeignKey('Roster', on_delete=models.CASCADE, related_name='local')
    visita = models.ForeignKey('Roster', on_delete=models.CASCADE, related_name='visita')
    match = models.ForeignKey('Match', on_delete=models.CASCADE)
    class Meta:
        unique_together = (('local', 'match', 'visita'),)


    def str(self):
        return '%s - %s - %s' % (self.local.name, self.visita.name, self.match.name)
    
class Roster(models.Model):
    team = models.ForeignKey('Team', on_delete = models.CASCADE)
    name = models.CharField(max_length=120)
    def str(self):
        return '%s - %s' % (self.name, self.team.name)