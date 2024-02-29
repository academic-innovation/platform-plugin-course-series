from setuptools import find_packages, setup

setup(
    name="platform-plugin-course-series",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "django>=3.2,<4.0",
        "edx-django-utils",
        "edx-opaque-keys",
    ],
    entry_points={
        "lms.djangoapp": [
            "course_series = course_series.apps:CourseSeriesAppConfig",
        ],
        "cms.djangoapp": [
            "course_series = course_series.apps:CourseSeriesAppConfig",
        ],
    },
)
