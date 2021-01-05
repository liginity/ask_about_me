from django.db import models
from django.utils import timezone
from django.urls import reverse


class SimpleQuestion(models.Model):
    """The Simple Question to ask."""

    # qid = models.SmallIntegerField()
    content = models.CharField(max_length=1000)
    created_time = models.DateTimeField(default=timezone.now)
    public_answer = models.ForeignKey(
        "PublicAnswer", on_delete=models.SET_NULL, null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse("answer-detail", kwargs={"pk", self.pk})


class PublicAnswer(models.Model):
    """The Public Answer."""

    content = models.TextField()
    answered_time = models.DateTimeField()
