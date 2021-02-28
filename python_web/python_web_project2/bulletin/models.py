from django.db import models

class Subject(models.Model):
    content = models.CharField(max_length=100)
    def __str__(self):
        return self.content

class Question(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ManyToManyField(Subject)
    content = models.TextField()
    create_date = models.DateTimeField()
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    vote = models.IntegerField(default=0)



