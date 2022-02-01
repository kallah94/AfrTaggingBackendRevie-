
from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

from codebase.settings import MEDIA_URL

User._meta.get_field('email')._unique = True


class Person(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    age = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Manager(Person):
    status = models.BooleanField()
    account = models.ForeignKey(User, on_delete=models.CASCADE)


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class League(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    leagues = models.ManyToManyField(League)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Teammate(Person):
    # id_teammate = models.IntegerField(primary_key=True, auto_created=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    current_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        abstract = True


class Staff(Teammate):
    class StatusChoices(models.TextChoices):
        coach = 'coach'
        assistant = 'assistant'

    status = models.CharField(max_length=255, choices=StatusChoices.choices)


class Attribute(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Player(Teammate):
    class StatusChoices(models.TextChoices):
        field_player = 'field_player'
        goal_keeper = 'goal_keeper'

    class StrongFeet(models.TextChoices):
        right = 'right'
        left = 'left'

    status = models.CharField(max_length=255, choices=StatusChoices.choices)
    number = models.IntegerField()
    strong_feet = models.CharField(max_length=255, choices=StrongFeet.choices)
    height = models.IntegerField()


class Season(models.Model):
    begin = models.DateField()
    end = models.DateField()


class GameVideo(models.Model):
    video = models.FileField(upload_to='videos/games/%Y/%m/%d', null=False, blank=False)


class Game(models.Model):
    date = models.DateField()
    competition = models.ForeignKey(League, on_delete=models.DO_NOTHING)
    home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home')
    visitor = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visitor')
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING)
    home_score = models.IntegerField()
    visitor_score = models.IntegerField()
    video = models.OneToOneField(GameVideo, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=255)


class Action(models.Model):
    name = models.CharField(max_length=255, unique=True)
    attributes = models.ManyToManyField(Attribute)

    def __str__(self):
        return self.name


class PlayerActionInGame(models.Model):
    video_start = models.DecimalField(decimal_places=16, max_digits=32)
    video_end = models.DecimalField(decimal_places=16, max_digits=32)
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    action = models.ForeignKey(Action, on_delete=models.DO_NOTHING)
    attributes = models.ManyToManyField(Attribute)


class Period(models.Model):
    class StatusChoices(models.TextChoices):
        in_progress = 'in_progress'
        finished = 'finished'

    begin = models.DateField(null=True)
    end = models.DateField(null=True)
    status = models.CharField(max_length=255, choices=StatusChoices.choices, default='')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class Contract(models.Model):
    class StatusChoices(models.TextChoices):
        in_progress = 'in_progress'
        finished = 'finished'

    begin = models.DateField()
    end = models.DateField()
    status = models.CharField(max_length=255, choices=StatusChoices.choices)
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class PlayerPosition(models.Model):
    code = models.CharField(max_length=4)
    description = models.CharField(max_length=255)
