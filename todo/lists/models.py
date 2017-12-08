from django.db import models


class List(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)




class Task(models.Model):
    task = models.CharField(max_length=150)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)


    todo_list = models.ForeignKey('lists.List',
                            on_delete=models.CASCADE,
                            related_name='tasks')

    class Meta:
        ordering = ['-due_date']
