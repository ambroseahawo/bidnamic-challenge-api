from django.contrib import admin
from form.models import Form

# Register your models here.
@admin.register(Form)
class FormModel(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'surname', 'user_id')
    search_fields = ('google_id', 'telephone')
