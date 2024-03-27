from django.apps import AppConfig


class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sales'

    def ready(self):
        import apps.sales.signals
        from apps.sales.tasks.transaction_confirmations import transaction_confirmations
        transaction_confirmations.delay()
