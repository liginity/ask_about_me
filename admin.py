from django.contrib import admin

from askaboutme.models import SimpleQuestion, PublicAnswer


@admin.register(SimpleQuestion)
class SimpleQuestionAdmin(admin.ModelAdmin):
    fields = [
        "content",
        "created_time",
        "public_answer",
    ]


@admin.register(PublicAnswer)
class PublicAnswerAdmin(admin.ModelAdmin):
    fields = [
        "content",
        "answered_time",
    ]
