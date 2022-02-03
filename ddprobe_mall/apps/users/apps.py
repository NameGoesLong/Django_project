from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # WHY 'apps.users' than 'users'??
    name = 'apps.users'
