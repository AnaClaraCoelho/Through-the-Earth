from django.db import models
from ..accounts.models import User


class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.CASCADE)
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Todo(models.Model):
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)
    # city = models.CharField(max_length=512)
    # tourist_spot = models.CharField(max_length=512)

    def to_dict_json(self):
        return {
            'id': self.id,
            # 'city': self.city,
            # 'tourist_spot': self.tourist_spot,
            'description': self.description,
            'done': self.done,
        }
