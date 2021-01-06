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
        "short_public_answer",
    ]
    actions = [
        "mark_polite",
        "mark_impolite",
    ]

    def mark_polite(self, request, queryset):
        queryset.update(polite_q=True)

    mark_polite.short_description = "Mark selected questions as polite questions"

    def mark_impolite(self, request, queryset):
        queryset.update(polite_q=False)

    mark_impolite.short_description = "Mark selected questions as impolite questions"


@admin.register(PublicAnswer)
class PublicAnswerAdmin(admin.ModelAdmin):
    fields = [
        "content",
        "answered_time",
    ]
    list_display = [
        "answered_time",
        "short_content",
    ]
