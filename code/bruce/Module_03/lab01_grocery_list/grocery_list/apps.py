from django.apps import AppConfig


class GroceryListConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # 'name' here matches with <project>/settings.py.INSTALLED_APPS[]
    name = 'grocery_list'
