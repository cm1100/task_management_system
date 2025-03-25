from django.db import models



class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=10)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10)
    assigned_users = models.ManyToManyField('accounts.CustomUser', related_name='tasks',blank=True)

    def __str__(self):
        return self.name



    


