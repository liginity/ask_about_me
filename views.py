from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse

from askaboutme.models import SimpleQuestion
from askaboutme.forms import SimpleQuestionForm


def index(request):
    question_list = SimpleQuestion.objects.filter(
        polite_q=True, wont_be_answered_q=False
    ).order_by("-created_time")
    context = {
        "question_list": question_list,
        "polite_question_number": question_list.count(),
    }
    return render(request, "askaboutme/index.html", context=context)


def ask_a_question(request):
    if request.method == "POST":
        form = SimpleQuestionForm(request.POST)
        if form.is_valid():
            content = request.POST.get("qcontent")
            question = SimpleQuestion(content=content)
            question.save()
            return HttpResponseRedirect(reverse("askaboutme:index"))
    else:
        form = SimpleQuestionForm()
    context = {
        "form": form,
    }
    return render(request, "askaboutme/ask_a_question.html", context)
