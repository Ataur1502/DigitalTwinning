from django.contrib import admin
from .models import Experiment

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ("roll_no", "experiment_name", "status", "assigned_on")  # Show status
    search_fields = ("roll_no", "experiment_name")
    list_filter = ("status", "assigned_on")  # Filter by status

