from datetime import datetime, timedelta

from config.app_config import START_DATE, INTERVAL_DAYS
from functions.get_date import get_date

PHONE_TIME_OFFSET = timedelta(hours=8)

def calculate_events():

    today = get_date()

    days_until_first = (
        START_DATE - today
    ).days



    if days_until_first > 0:

        status = "Waiting for next event"

        next_event = START_DATE

        remaining = days_until_first



    else:

        days_since_start = (
            today - START_DATE
        ).days


        cycle_position = (
            days_since_start % INTERVAL_DAYS
        )

        if cycle_position == 0:

            status = "Today is an Event Day"

            remaining = INTERVAL_DAYS

            next_event = today + timedelta(
                days=INTERVAL_DAYS
            )



        else:

            status = "Not an Event Day"

            remaining = (
                INTERVAL_DAYS -
                cycle_position
            )


            next_event = (
                today +
                timedelta(
                    days=remaining
                )
            )



    upcoming = []

    current = next_event


    for _ in range(7):

        upcoming.append(current)

        current += timedelta(
            days=INTERVAL_DAYS
        )



    return {

        "today": today,

        "status": status,

        "next_event": next_event,

        "remaining": remaining,

        "upcoming": upcoming,

    }