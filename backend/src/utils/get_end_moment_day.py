from datetime import datetime,  time


def get_end_moment_day(timestamp):

    return datetime.combine(
        datetime.fromtimestamp(timestamp),
        time.max
    ).timestamp()
