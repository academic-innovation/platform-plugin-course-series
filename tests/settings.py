DEBUG = True
USE_TZ = True
USE_I18N = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}
MIDDLEWARE_CLASSES = ((),)
SITE_ID = 1

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "course_series",
]
SECRET_KEY = "test-secret-key"
