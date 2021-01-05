from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import truncatechars


class SimpleQuestion(models.Model):
    """The Simple Question to ask."""

    # qid = models.SmallIntegerField()
    content = models.CharField(max_length=1000)
    created_time = models.DateTimeField(default=timezone.now)
    polite_q = models.BooleanField(default=False, help_text="polite questions would show up.")
    wont_be_answered_q = models.BooleanField(default=False)
    public_answer = models.ForeignKey(
        "PublicAnswer", on_delete=models.SET_NULL, null=True, blank=True
    )

    ## this is used in the admin site.
    @property
    def short_content(self):
        return truncatechars(self.content, 50)

    def get_absolute_url(self):
        return reverse("answer-detail", kwargs={"pk", self.pk})


class PublicAnswer(models.Model):
    """The Public Answer."""

    content = models.TextField()
    answered_time = models.DateTimeField()
