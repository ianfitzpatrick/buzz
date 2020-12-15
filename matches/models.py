from django.db import models
from casters.models import Caster
from leagues.models import Circuit, Round
from teams.models import Team

class Match(models.Model):
    """A match between two teams."""
    
    home = models.ForeignKey(
        Team, related_name='home_matches', on_delete=models.CASCADE)

    away = models.ForeignKey(
        Team, related_name='away_matches', on_delete=models.CASCADE)

    circuit = models.ForeignKey(
        Circuit, related_name='circuit_matches', on_delete=models.CASCADE)

    round = models.ForeignKey(Round, on_delete=models.CASCADE)

    start_time = models.DateTimeField(blank=True, null=True)

    primary_caster = models.ForeignKey(
        Caster, related_name='casted_matches', on_delete=models.CASCADE,
        blank=True, null=True)

    secondary_casters = models.ManyToManyField(
        Caster, related_name='cocasted_matches', blank=True)

    vod_link = models.URLField(blank=True, null=True)

    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Matches'

    def __str__(self):
        return f'{self.away.name} @ {self.home.name}'

class Result(models.Model):
    """Winner, Loser, and statistics for a particular Match."""

    match = models.OneToOneField(
        Match, related_name='result', on_delete=models.CASCADE, blank=True,
        null=True)    

    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    winner = models.ForeignKey(
        Team, related_name='won_match_results', on_delete=models.CASCADE,
    )

    loser = models.ForeignKey(
        Team, related_name='lost_match_results', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.winner.name} over {self.loser.name} in {self.sets.count()} sets'

class Set(models.Model):
    """A series of games played in a Match."""
    result = models.ForeignKey(
        Result, related_name='sets', on_delete=models.CASCADE, blank=True,
        null=True)

    number = models.PositiveSmallIntegerField(default=1)

    winner = models.ForeignKey(
        Team, related_name='won_sets', on_delete=models.CASCADE)

    loser = models.ForeignKey(
        Team, related_name='lost_sets', on_delete=models.CASCADE)

    def __str__(self):
        return f'Set {self.number}: {self.winner.name}'
        
class Game(models.Model):
    """A single map played in a Set."""
    number = models.PositiveSmallIntegerField(default=1)

    MAP_CHOICES = (
        ('PD', 'The Pod'),
        ('TF', 'The Tally Fields'),
        ('NF', 'The Nesting Flats'),
        ('SJ', 'Split Juniper'),
        ('BQ', 'Black Queen\'s Keep'),
        ('HT', 'Helix Temple'),
        ('SP', 'The Spire'),
    )

    map = models.CharField(
        max_length=2, choices=MAP_CHOICES, blank=True, null=True)

    winner = models.ForeignKey(
        Team, related_name='won_games', on_delete=models.CASCADE, blank=True,
        null=True)

    loser = models.ForeignKey(
        Team, related_name='lost_games', on_delete=models.CASCADE, blank=True,
        null=True)

    set = models.ForeignKey(
        Set, related_name='games', on_delete=models.CASCADE, blank=True,
        null=True
    )

    home_berries = models.PositiveSmallIntegerField(blank=True, default=True)
    away_berries = models.PositiveSmallIntegerField(blank=True, default=True)

    home_snail = models.PositiveSmallIntegerField(blank=True, default=True)
    away_snail = models.PositiveSmallIntegerField(blank=True, default=True)

    home_queen_deaths = models.PositiveSmallIntegerField(blank=True, default=True)
    away_queen_deaths = models.PositiveSmallIntegerField(blank=True, default=True)

    WIN_CONDITION_CHOICES = (
        ('E', 'Economic'),
        ('M', 'Military'),
        ('S', 'Snail')
    )

    win_condition = models.CharField(
        max_length=1, choices=WIN_CONDITION_CHOICES, blank=True, null=True)


    def __str__(self):
        return f'Game {self.number}: {self.winner.name}'

