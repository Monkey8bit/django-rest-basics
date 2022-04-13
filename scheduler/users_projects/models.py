from django.db import models

from users.models import SchedulerUser


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=120, blank=True)
    users = models.ManyToManyField(SchedulerUser)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_created = models.ForeignKey(SchedulerUser, on_delete=models.SET(f"{project.name}_user"))
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
