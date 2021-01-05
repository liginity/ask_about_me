from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import truncatechars


class SimpleQuestion(models.Model):
    """The Simple Question to ask."""

    # qid = models.SmallIntegerField()
    content = models.TextField(max_length=2500)
    created_time = models.DateTimeField(default=timezone.now)
    polite_q = models.BooleanField(
        default=False, help_text="polite questions would show up."
    )
    wont_be_answered_q = models.BooleanField(verbose_name="ignored", default=False)
    public_answer = models.ForeignKey(
        "PublicAnswer",
        verbose_name="answer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    ## this is used in the admin site.
    # @property
    def short_content(self):
        return truncatechars(self.content, 50)

    short_content.short_description = "content"

    # @property
    def short_public_answer(self):
        if self.public_answer:
            return truncatechars(self.public_answer.content, 20)
        else:
            return None

    short_public_answer.short_description = "answer"

    def get_absolute_url(self):
        return reverse("answer-detail", kwargs={"pk", self.pk})


class PublicAnswer(models.Model):
    """The Public Answer."""

    content = models.TextField()
    answered_time = models.DateTimeField()

    def short_content(self):
        return truncatechars(self.content, 20)

    short_content.short_description = "answer"
