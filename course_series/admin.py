from django.contrib import admin

from . import models


@admin.register(models.AuthoringOrganization)
class AuthoringOrganizationAdmin(admin.ModelAdmin):
    """Admin for authoring organizaion objects."""

    list_display = ["name", "uuid", "key"]


@admin.register(models.CourseSeriesType)
class CourseSeriesTypeAdmin(admin.ModelAdmin):
    """Admin for CourseSeriesType objects."""

    list_display = ["name", "applicable_seat_type"]


class CourseRunInline(admin.TabularInline):
    """Inline for course run items."""

    model = models.CourseRun


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin for Course objects."""

    inlines = [CourseRunInline]


class CourseSeriesItemInline(admin.StackedInline):
    """Inline for course series items."""

    model = models.CourseSeriesItem


@admin.register(models.CourseSeries)
class CourseSeriesAdmin(admin.ModelAdmin):
    """Admin for CourseSeries objects."""

    inlines = [CourseSeriesItemInline]
