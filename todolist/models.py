from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse

class Todo(models.Model):
    todo = models.CharField(max_length=50)
    date_pub = models.DateTimeField(auto_now_add=True)
    flag = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('-date_pub',)

    def get_absolute_url(self):
        return reverse('main_list')

    def __str__(self):
        return self.todo
