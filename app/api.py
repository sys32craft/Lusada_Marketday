import os

from flask import Flask, jsonify

from functions.event_calculator import calculate_events
from config.app_config import EVENT_NAME, INTERVAL_DAYS


app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/", methods=["GET", "HEAD"])
def health_check():
    return jsonify({
        "status": "ok",
        "service": "Lusada Marketday API"
    })


@app.route("/event-name", methods=["GET"])
def get_event_name():
    return jsonify({
        "event_name": EVENT_NAME
    })


@app.route("/interval", methods=["GET"])
def get_interval():
    return jsonify({
        "interval_days": INTERVAL_DAYS
    })


@app.route("/status", methods=["GET"])
def get_status():
    data = calculate_events()

    return jsonify({
        "status": data["status"]
    })


@app.route("/today-date", methods=["GET"])
def get_today_date():
    data = calculate_events()

    return jsonify({
        "today": data["today"].strftime("%A, %d %B %Y")
    })


@app.route("/next-event", methods=["GET"])
def get_next_event():
    data = calculate_events()

    return jsonify({
        "next_event": data["next_event"].strftime("%A, %d %B %Y")
    })


@app.route("/cycle-progress", methods=["GET"])
def get_cycle_progress():
    data = calculate_events()

    progress = (
        INTERVAL_DAYS - data["remaining"]
    ) / INTERVAL_DAYS

    return jsonify({
        "cycle_progress": progress
    })


@app.route("/remaining-days", methods=["GET"])
def get_remaining_days():
    data = calculate_events()

    return jsonify({
        "remaining_days": data["remaining"]
    })


@app.route("/upcoming-rotation", methods=["GET"])
def get_upcoming_rotation():
    data = calculate_events()

    upcoming = []

    for i, date in enumerate(data["upcoming"], 1):
        upcoming.append({
            "rotation": i,
            "date": date.strftime("%A, %d %B %Y")
        })

    return jsonify({
        "upcoming_rotation": upcoming
    })


@app.route("/all", methods=["GET"])
def get_all():
    data = calculate_events()

    progress = (
        INTERVAL_DAYS - data["remaining"]
    ) / INTERVAL_DAYS

    return jsonify({
        "event_name": EVENT_NAME,
        "interval_days": INTERVAL_DAYS,
        "status": data["status"],
        "today": data["today"].strftime("%A, %d %B %Y"),
        "next_event": data["next_event"].strftime("%A, %d %B %Y"),
        "cycle_progress": progress,
        "remaining_days": data["remaining"],
        "upcoming_rotation": [
            {
                "rotation": i,
                "date": date.strftime("%A, %d %B %Y")
            }
            for i, date in enumerate(data["upcoming"], 1)
        ]
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("API_PORT", 5000))
    )