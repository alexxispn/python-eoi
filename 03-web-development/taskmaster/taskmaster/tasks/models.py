from django.db import models
from django.utils import timezone


def today():
    return timezone.now().date()


class Project(models.Model):
    name = models.CharField(max_length=250)
    code = models.SlugField(max_length=4, unique=True)
    description = models.TextField(blank=True)
    start_date = models.DateField(default=today)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=250)
    finished = models.BooleanField(default=False)
    order = models.IntegerField(default=100)
    priority = models.CharField(
        max_length=6,
        choices=[
            ('High', 'High'),
            ('Medium', 'Medium'),
            ('Low', 'Low'),
        ],
        default='Medium',
    )
    due_date = models.DateField(
        blank=True,
        null=True,
    )
    color = models.CharField(
        max_length=6,
        choices=[
            ('blue', 'blue'),
            ('red', 'red'),
            ('orange', 'orange'),
            ('green', 'green'),
        ],
        default='blue',
    )
    project = models.ForeignKey(
        Project,
        blank=True,
        default=None,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def is_due(self):
        return (self.due_date is not None) and (self.due_date <= today())
