from django.apps import AppConfig

# signals diimport agar jalan di apps


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals