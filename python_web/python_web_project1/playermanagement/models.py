from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=200)
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    playoff = models.BooleanField(default=False)

    def __str__(self):
        return self.team_name

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.name
