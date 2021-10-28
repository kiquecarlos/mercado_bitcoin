from datetime import datetime,  time


def get_start_moment_day(timestamp):

    return datetime.combine(
        datetime.fromtimestamp(timestamp),
        time.min
    ).timestamp()
