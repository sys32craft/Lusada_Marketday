import os

import requests
from fastapi.responses import Response
from nicegui import app, ui

from ui.dashboard import dashboard
from ui.theme.theme import theme


# Flask API running inside the same Render container
API_URL = "http://127.0.0.1:5000"


@app.get("/api/{path:path}")
def proxy_get(path: str):
    try:
        api_response = requests.get(
            f"{API_URL}/{path}",
            timeout=30,
        )

        return Response(
            content=api_response.content,
            status_code=api_response.status_code,
            headers={
                "Content-Type": api_response.headers.get(
                    "Content-Type",
                    "application/json",
                )
            },
        )

    except requests.RequestException as error:
        return Response(
            content=f'{{"error":"{str(error)}"}}',
            status_code=502,
            media_type="application/json",
        )


@ui.page("/")
def index():
    theme()
    dashboard()


ui.run(
    host="0.0.0.0",
    port=int(os.getenv("PORT", 8080)),
    title="Lusada Market Day",
    reload=False,
)