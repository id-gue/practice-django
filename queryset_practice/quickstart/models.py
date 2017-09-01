from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=40)
    house_number = models.CharField(max_length=40)
    post_code = models.IntegerField()
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=20)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roles = models.ManyToManyField(Role, related_name="people")
    address = models.ForeignKey(Address, null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
