from nicegui import ui

from config.app_config import EVENT_NAME, INTERVAL_DAYS
from functions.event_calculator import calculate_events
from components.card import app_card


def dashboard():
    data = calculate_events()

    is_event_day = (
        data["status"] == "Today is market day"
    )

    cycle_percent = (
        INTERVAL_DAYS - data["remaining"]
    ) / INTERVAL_DAYS * 100

    with ui.column().classes(
        "w-full items-center gap-6 px-2 md:px-4 lg:px-6 py-2"
    ):

        # Header
        ui.label(
            EVENT_NAME
        ).classes(
            "text-5xl font-bold text-center"
        )

        ui.label(
            "An event every 4 days"
        ).classes(
            "text-lg opacity-70 text-center"
        )

        # Status Card
        with app_card("w-full"):

            with ui.row().classes(
                "w-full justify-between items-center"
            ):

                with ui.row().classes(
                    "items-center gap-4"
                ):

                    if is_event_day:
                        ui.icon(
                            "event_available"
                        ).classes(
                            "text-6xl text-green-500"
                        )
                    else:
                        ui.icon(
                            "event_busy"
                        ).classes(
                            "text-6xl text-red-500"
                        )

                    with ui.column():

                        ui.label(
                            "Current Status"
                        ).classes(
                            "text-xl font-bold"
                        )

                        ui.label(
                            data["status"]
                        ).classes(
                            "text-2xl text-green-500"
                            if is_event_day
                            else "text-2xl text-red-500"
                        )

                ui.element(
                    "div"
                ).classes(
                    "w-5 h-5 rounded-full bg-green-500"
                    if is_event_day
                    else "w-5 h-5 rounded-full bg-red-500"
                )

        # Date Cards
        with ui.row().classes(
            "w-full gap-4 flex-wrap md:flex-nowrap"
        ):

            with app_card("w-full md:flex-1"):

                ui.label(
                    "Today"
                ).classes(
                    "font-bold"
                )

                ui.label(
                    data["today"].strftime(
                        "%A, %d %B %Y"
                    )
                )

            with app_card("w-full md:flex-1"):

                ui.label(
                    "Next Event"
                ).classes(
                    "font-bold"
                )

                ui.label(
                    data["next_event"].strftime(
                        "%A, %d %B %Y"
                    )
                )

        # Cycle Progress
        with app_card("w-full"):

            ui.label(
                "Cycle Progress"
            ).classes(
                "text-xl font-bold"
            )

            ui.linear_progress(
                value=cycle_percent / 100
            ).classes(
                "mt-3"
            )

            ui.label(
                f"{data['remaining']} days until next event"
            )

        # Upcoming Timeline
        with app_card("w-full"):

            ui.label(
                "Upcoming Rotation"
            ).classes(
                "text-xl font-bold mb-3"
            )

            for number, event in enumerate(
                data["upcoming"],
                start=1
            ):

                with ui.row().classes(
                    "w-full items-center justify-between"
                ):

                    with ui.row().classes(
                        "items-center gap-3"
                    ):

                        ui.badge(
                            number
                        ).props(
                            "rounded"
                        )

                        ui.label(
                            event.strftime(
                                "%A, %d %B %Y"
                            )
                        )

                    ui.element(
                        "div"
                    ).classes(
                        "w-3 h-3 rounded-full bg-blue-500"
                    )