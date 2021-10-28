from datetime import datetime, timedelta, time


def sub_days(timestamp, days):

    return (datetime.fromtimestamp(timestamp) - timedelta(days=days)).timestamp()
