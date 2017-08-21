from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roles = models.ManyToManyField(Role, related_name="people")

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
