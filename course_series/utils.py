def serialize_course_run(course_run):
    """Returns a serialized representation of a course run."""
    return {
        "key": str(course_run.key),
        "uuid": str(course_run.uuid),
        "title": course_run.course.title,
        "type": course_run.type,
        "seats": course_run.seats,
    }


def serialize_course(course):
    """Returns a serialized representation of a course."""
    return {
        "key": course.key,
        "uuid": str(course.uuid),
        "title": course.title,
        "course_runs": [serialize_course_run(run) for run in course.course_runs.all()],
    }


def serialize_org(org):
    """Returns a serialized representation of an authoring organization."""
    return {
        "uuid": str(org.uuid),
        "key": org.key,
        "name": org.name,
        "logo_image_url": org.logo_image.url,
    }


def serialize_course_series(series):
    """Returns a serialized representation of a series."""
    return {
        "uuid": str(series.uuid),
        "title": series.title,
        "type": series.series_type.name,
        "courses": [serialize_course(course) for course in series.courses.all()],
        "authoring_organizations": [
            serialize_org(org) for org in series.authoring_organizations.all()
        ],
        "details_url": series.details_url,
        "banner_image": {
            "small": {
                "url": series.banner_image.url,
                "width": 435,
                "height": 145,
            },
        },
        "applicable_seat_types": series.series_type.applicable_seat_types,
        "is_program_eligible_for_one_click_purchase": series.one_click_purchase_enabled,
    }


def get_series_data(series_queryset):
    """Returns serialized series data."""
    return [serialize_course_series(series) for series in series_queryset]
