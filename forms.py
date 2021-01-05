from django import forms
from captcha.fields import CaptchaField


class SimpleQuestionForm(forms.Form):
    """A form for simple questions."""

    qcontent = forms.CharField(
        max_length=2000,
        label="Question:",
        help_text="Write a question to ask.",
        widget=forms.Textarea(attrs={"rows": 10, "cols": 40}),
    )
    captcha = CaptchaField()
