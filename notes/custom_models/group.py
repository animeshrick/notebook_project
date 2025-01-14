from django.db import models


class Group(models.Model):
    name=models.CharField(max_length=100)
    # members=models.ManyToManyField(User, related_name='groups')
    members=models.CharField(max_length=20000)

    def __str__(self):
        return self.name
