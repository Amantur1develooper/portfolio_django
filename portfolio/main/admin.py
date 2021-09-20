from django.contrib import admin
from .models import SendMessage
# Register your models here.
class SendMessageAdmin(admin.ModelAdmin):
    list_display=("pk","email",'phone_number',"message","sent_at")
    search_fields=("email",)
    list_editable=("message",)
    list_filter=("sent_at",)
    ordering=("sent_at",)

admin.site.register(SendMessage,SendMessageAdmin)