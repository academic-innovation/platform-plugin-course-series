from django.contrib.sites.models import Site
from django.core.cache import cache
from django.core.management import BaseCommand

from course_series.models import CourseSeries
from course_series.utils import get_series_data

# from openedx.core.djangoapps.catalog.cache
SITE_PROGRAM_UUIDS_CACHE_KEY_TPL = "program-uuids-{domain}"
PROGRAM_CACHE_KEY_TPL = "program-{uuid}"

CACHE_TIMEOUT = 5 * 60  # Short lifetime while testing


class Command(BaseCommand):
    """Populate dummy series data."""

    def handle(self, *args, **kwargs):
        course_series = CourseSeries.objects.select_related(
            "series_type"
        ).prefetch_related("authoring_organizations", "courses__course_runs")
        series_data = get_series_data(course_series)
        series = {
            PROGRAM_CACHE_KEY_TPL.format(uuid=series["uuid"]): series
            for series in series_data
        }
        uuids = [series["uuid"] for series in series_data]
        for site in Site.objects.all():
            # Cache program UUIDs
            cache.set(
                SITE_PROGRAM_UUIDS_CACHE_KEY_TPL.format(domain=site.domain),
                uuids,
                CACHE_TIMEOUT,
            )

            # Cache program data
            # logger.info(f'Caching details for {len(programs)} programs.')
            cache.set_many(series, CACHE_TIMEOUT)
