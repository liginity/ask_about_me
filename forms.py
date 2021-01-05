from django import forms
from captcha.fields import CaptchaField


class SimpleQuestionForm(forms.Form):
    """A form for simple questions."""

    qcontent = forms.CharField(max_length=700,label="Question:" , help_text="Write a question to ask.", widget=forms.Textarea)
    captcha = CaptchaField()
