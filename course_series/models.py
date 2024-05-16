from uuid import uuid4

from django.db import models

from opaque_keys.edx.django.models import CourseKeyField


class AuthoringOrganization(models.Model):
    """An organization that authors a course series."""

    uuid = models.UUIDField(default=uuid4)
    key = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    logo_image = models.ImageField(upload_to="authoring_org/logos")

    def __str__(self):
        return self.name


class CourseMode(models.TextChoices):
    """A course mode available in Open edX."""

    HONOR = "honor", "Honor"
    PROFESSIONAL = "professional", "Professional"
    VERIFIED = "verified", "Verified"
    AUDIT = "audit", "Audit"
    NO_ID_PROFESSIONAL_MODE = "no-id-professional", "No ID Professional"
    CREDIT_MODE = "credit", "Credit"
    MASTERS = "masters", "Masters"
    EXECUTIVE_EDUCATION = "executive-education", "Executive Education"
    PAID_EXECUTIVE_EDUCATION = (
        "paid-executive-education",
        "Paid Executive Education",
    )
    UNPAID_EXECUTIVE_EDUCATION = (
        "unpaid-executive-education",
        "Unpaid Executive Education",
    )
    PAID_BOOTCAMP = "paid-bootcamp", "Paid Bootcamp"
    UNPAID_BOOTCAMP = "unpaid-bootcamp", "Unpaid Bootcamp"


class CourseSeriesType(models.Model):
    """A type of course series."""

    name = models.CharField(max_length=255)
    applicable_seat_type = models.CharField(choices=CourseMode.choices, max_length=50)

    def __str__(self):
        return self.name

    @property
    def applicable_seat_types(self):
        """Seat types that qualify for completion of programs of this type.

        Learners completing associated courses, but enrolled in other seat types, will
        not have their completion of the course counted toward the completion of the
        program.

        Although this plugin only currently supports a single applicable seat type,
        multiple applicable seat types are supported by edx-platform.
        """
        return [self.applicable_seat_type]


class Course(models.Model):
    """A course reference."""

    key = models.CharField(max_length=255, db_index=True)
    uuid = models.UUIDField(default=uuid4)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class CourseRun(models.Model):
    """A course run."""

    course = models.ForeignKey(
        Course, related_name="course_runs", on_delete=models.CASCADE
    )
    type = models.CharField(
        choices=CourseMode.choices,
        max_length=50,
        help_text="Indicates which certificate mode is counted towards completion of a program.",
    )
    key = CourseKeyField(max_length=255)
    uuid = models.UUIDField(default=uuid4)

    def __str__(self):
        return str(self.key)

    @property
    def seats(self):
        """Still unclear what role seats play in Open edX."""
        return [{"type": self.type}]


class CourseSeries(models.Model):
    """A series of courses."""

    uuid = models.UUIDField(default=uuid4)
    title = models.CharField(max_length=500)
    series_type = models.ForeignKey(CourseSeriesType, on_delete=models.CASCADE)
    details_url = models.URLField()
    banner_image = models.ImageField(upload_to="course_series/banners")
    authoring_organizations = models.ManyToManyField(AuthoringOrganization)
    courses = models.ManyToManyField(Course, through="CourseSeriesItem")

    # Mirror the one_click_purchase_enabled attribute from course-discovery
    # https://github.com/openedx/course-discovery/blob/a0124c/course_discovery/apps/course_metadata/models.py#L3222-L3225
    one_click_purchase_enabled = False

    class Meta:
        verbose_name_plural = "course series"

    def __str__(self):
        return self.title


class CourseSeriesItem(models.Model):
    """A course belonging to a course series."""

    series = models.ForeignKey(
        CourseSeries, related_name="items", on_delete=models.CASCADE
    )
    course = models.ForeignKey(Course, related_name="items", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_id} > {self.series_id}"
