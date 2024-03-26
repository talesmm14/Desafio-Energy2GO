from django.contrib import admin

from apps.sales.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
