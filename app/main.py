import os

from nicegui import ui

from ui.dashboard import dashboard
from ui.theme.theme import theme


@ui.page('/')
def index():
    theme()
    dashboard()


ui.run(
    host='0.0.0.0',
    port=int(os.getenv('PORT', 8080)),
    title='Lusada Market Day',
    reload=False,
)