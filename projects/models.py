from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(default="", null=True)
    image = models.ImageField()
    repo_link = models.URLField()
    deployed_link = models.URLField()


    def __str__(self):
        return self.name