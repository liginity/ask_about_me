from django.contrib import admin

from askaboutme.models import SimpleQuestion, PublicAnswer


@admin.register(SimpleQuestion)
class SimpleQuestionAdmin(admin.ModelAdmin):
    fields = [
        "content",
        "created_time",
        "polite_q",
        "wont_be_answered_q",
        "public_answer",
    ]
    list_display = [
        "created_time",
        # "content",
        "short_content",
        "polite_q",
        "wont_be_answered_q",
    ]


@admin.register(PublicAnswer)
class PublicAnswerAdmin(admin.ModelAdmin):
    fields = [
        "content",
        "answered_time",
    ]
