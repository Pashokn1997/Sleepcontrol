from split_settings.tools import include as settings_include
from split_settings.tools import optional

settings_include(
    "base.py",
    "installed_apps.py",
    "database.py",
    "i18n.py",
    "tz.py",
    "storage.py",
    optional("local_settings.py"),
)
