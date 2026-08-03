from contextlib import contextmanager

from nicegui import ui


@contextmanager
def app_card(extra_classes: str = ""):

    classes = f"dashboard-card {extra_classes}".strip()
    with ui.card().classes(classes):
        yield