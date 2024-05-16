import pytest

from course_series import factories


@pytest.mark.django_db
class TestAuthoringOrganization:
    """Tests for the AuthoringOrganization model."""

    def test_str(self):
        org = factories.AuthoringOrganizationFactory(name="Michigan Online")
        assert str(org) == "Michigan Online"


@pytest.mark.django_db
class TestCourseSeriesType:
    """Tests for the CourseSeriesType model."""

    def test_str(self):
        series_type = factories.CourseSeriesTypeFactory(name="MasterTrack")
        assert str(series_type) == "MasterTrack"


@pytest.mark.django_db
class TestCourse:
    """Tests for the Course model."""

    def test_str(self):
        course = factories.CourseFactory(title="Python for Quail")
        assert str(course) == "Python for Quail"


@pytest.mark.django_db
class TestCourseRun:
    """Tests for the CourseRun model."""

    def test_str(self):
        course_run = factories.CourseRunFactory(
            key__org="org", key__course="course", key__run="run"
        )
        assert str(course_run) == "course-v1:org+course+run"


@pytest.mark.django_db
class TestCourseSeries:
    """Tests for the CourseSeries model."""

    def test_str(self):
        series = factories.CourseSeriesFactory(title="A Series")
        assert str(series) == "A Series"
