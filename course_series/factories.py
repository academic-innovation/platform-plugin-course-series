from django.utils.text import slugify

import factory
from factory import Factory, Faker, LazyAttribute, SubFactory
from factory.django import DjangoModelFactory, ImageField
from opaque_keys.edx.locator import CourseLocator

from . import models


class CourseLocatorFactory(Factory):
    """Factory for Open edX CourseLocator objects."""

    org = Faker("pystr")
    course = Faker("pystr")
    run = Faker("pystr")

    class Meta:
        model = CourseLocator


class AuthoringOrganizationFactory(DjangoModelFactory):
    """Factory for AuthoringOrganization objects."""

    key = LazyAttribute(lambda o: slugify(o.name))
    name = Faker("company")
    logo_image = ImageField()

    class Meta:
        model = models.AuthoringOrganization


class CourseSeriesTypeFactory(DjangoModelFactory):
    """Factory for CourseSeriesType objects."""

    name = Faker("pystr")

    class Meta:
        model = models.CourseSeriesType


class CourseFactory(DjangoModelFactory):
    """Factory for Course objects."""

    key = Faker("pystr")
    title = Faker("bs")

    class Meta:
        model = models.Course


class CourseRunFactory(DjangoModelFactory):
    """Factory for CourseRun objects."""

    course = SubFactory(CourseFactory)
    key = SubFactory(CourseLocatorFactory)

    class Meta:
        model = models.CourseRun


class CourseSeriesFactory(DjangoModelFactory):
    """Factory for CourseSeries objects."""

    title = Faker("bs")
    series_type = SubFactory(CourseSeriesTypeFactory)
    details_url = Faker("url")
    banner_image = ImageField()

    class Meta:
        model = models.CourseSeries

    @factory.post_generation
    def authoring_organizations(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.authoring_organizations.add(*extracted)

    @factory.post_generation
    def courses(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.courses.add(*extracted)
