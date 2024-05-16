from django.contrib import admin

from . import models


@admin.register(models.AuthoringOrganization)
class AuthoringOrganizationAdmin(admin.ModelAdmin):
    """Admin for authoring organizaion objects."""

    ...


@admin.register(models.CourseSeriesType)
class CourseSeriesTypeAdmin(admin.ModelAdmin):
    """Admin for CourseSeriesType objects."""

    ...


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin for Course objects."""

    ...


@admin.register(models.CourseRun)
class CourseRunAdmin(admin.ModelAdmin):
    """Admin for CourseRun objects."""

    ...


@admin.register(models.CourseSeries)
class CourseSeriesAdmin(admin.ModelAdmin):
    """Admin for CourseSeries objects."""

    ...


@admin.register(models.CourseSeriesItem)
class CourseSeriesItemAdmin(admin.ModelAdmin):
    """Admin for CourseSeriesItem objects."""

    ...
