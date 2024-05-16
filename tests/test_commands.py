from io import StringIO

from django.core.management import call_command

import pytest

from course_series import factories


@pytest.mark.django_db
@pytest.mark.parametrize("item_count", (3, 7))
def test_populate_program_data_query_count(item_count, django_assert_num_queries):
    """Query count should not increase as records grow."""
    for _ in range(item_count):
        orgs = factories.AuthoringOrganizationFactory.create_batch(item_count)
        courses = factories.CourseFactory.create_batch(item_count)
        for course in courses:
            factories.CourseRunFactory.create_batch(item_count, course=course)
        factories.CourseSeriesFactory(authoring_organizations=orgs, courses=courses)
    out = StringIO()

    with django_assert_num_queries(5):
        call_command("populate_program_data", stdout=out)
