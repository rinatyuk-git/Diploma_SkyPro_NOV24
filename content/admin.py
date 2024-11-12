from django.contrib import admin

from content.models import Document
from content.tasks import doc_approving_message


@admin.action(description="Mark selected docs as approved")
def make_approved(modeladmin, request, queryset):
    queryset.update(status="a")
    """ определение отправки сообщения """
    for obj in queryset:
        doc_approving_message.delay(obj.id)


@admin.action(description="Mark selected docs as declined")
def make_declined(modeladmin, request, queryset):
    queryset.update(status="d")
    """ определение отправки сообщения """
    for obj in queryset:
        doc_approving_message.delay(obj.id)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ["name", "status"]
    ordering = ["name"]
    actions = [make_approved, make_declined]


admin.site.register(Document, DocumentAdmin)
