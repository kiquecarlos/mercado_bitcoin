from datetime import datetime, timedelta, time


def get_yesterday_timestamp():
    today_date = datetime.combine(datetime.now(), time.min)

    return (today_date - timedelta(days=1)).timestamp()
