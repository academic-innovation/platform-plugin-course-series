from django.apps import AppConfig

from edx_django_utils.plugins.constants import PluginURLs

PROJECT_TYPE_LMS = "lms.djangoapp"


class CourseSeriesAppConfig(AppConfig):
    """Config for course series app."""

    name = "course_series"
    default_auto_field = "django.db.models.BigAutoField"
    plugin_app = {
        PluginURLs.CONFIG: {
            PROJECT_TYPE_LMS: {
                PluginURLs.NAMESPACE: "course_series",
                PluginURLs.REGEX: "^api/",
                PluginURLs.RELATIVE_PATH: "urls",
            }
        },
    }
