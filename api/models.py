from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class Competition(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=10)
    area = models.ForeignKey("Area", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


# class Team(models.Model):
#     name = models.CharField(max_length=250)
#     tla = models.CharField(max_length=250)
#     short_name = models.CharField(max_length=100)
#     address = models.CharField(max_length=250)
#     area = models.ForeignKey("Area", on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.name}"


# class Player(models.Model):
#     name = models.CharField(max_length=250)
#     position
#     date_of_birth
#     nationality

#     def __str__(self):
#         return f"{self.name}"
