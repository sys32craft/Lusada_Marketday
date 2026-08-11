# Lusada Market Day

A simple web application that helps track recurring work events that repeat on a fixed interval (default: every **4 days**).

The purpose of this project is to eliminate manual date calculations and reduce mistakes when determining the next work event.

---

# Table of Contents

- Introduction
    
- Problem
    
- Solution
    
- Features
    
- Goals
    
- Technology Stack
    
- Project Architecture
    
- Development Roadmap
    
- Folder Structure
    
- User Flow
    
- Core Concepts
    
- Future Improvements
    
- Installation
    
- Development Guidelines
    
- Coding Standards
    
- API Plan
    
- License
    

---

# Introduction

Many work schedules follow a recurring pattern.

In my workplace, an important event happens every **4 days**.

Although the interval never changes, the weekday does.

For example:

- Monday
    
- Friday
    
- Tuesday
    
- Saturday
    
- Wednesday
    

Because months have different lengths and weekdays shift naturally, it is easy to miscalculate the next event.

This application solves that problem by automatically calculating every future occurrence from a single starting date.

---

# Problem

Manually counting every four days leads to mistakes.

Common problems include:

- Forgetting the next event date
    
- Miscounting days
    
- Losing track after weekends
    
- Confusing weekdays with calendar dates
    
- Starting calculations from the wrong day
    

Even though the pattern is simple, repeated manual calculations eventually become unreliable.

---

# Solution

Instead of calculating dates manually, the application stores:

- Event Name
    
- Starting Date
    
- Interval (default: 4 days)
    

Every future occurrence is generated automatically.

The application always knows:

- Today's status
    
- Whether today is market day
    
- Days remaining until the next event
    
- Upcoming event dates
    
- Previous event date
    

---

# Project Goals

The project has two objectives.

## 1. Solve a Real Problem

Provide a reliable schedule for recurring work events.

## 2. Learn Modern Python Web Development

The project is also a learning project for:

- NiceGUI
    
- FastAPI
    
- Clean Architecture
    
- REST APIs
    
- Project Organization
    
- Python Best Practices
    

---

# Features

## Dashboard

Displays:

- Today's date
    
- Current weekday
    
- Event status
    
- Countdown to the next event
    
- Next event date
    
- Previous event date
    
- Upcoming events
    

---

## Event Calculator

Automatically calculates recurring dates.

Example:

Start Date

2026-08-01

Interval

4 Days

Generated dates:

- Aug 1
    
- Aug 5
    
- Aug 9
    
- Aug 13
    
- Aug 17
    
- Aug 21
    

---

## Countdown

Displays:

- Days remaining
    
- Hours remaining (future enhancement)
    
- Minutes remaining (future enhancement)
    

---

## Event Status

Examples:

Today is Market Day

or

Next Event in 2 Days

---

## Settings

User can configure:

- Event Name
    
- Start Date
    
- Interval
    

---

## Calendar View

Highlight every recurring event.

---

## Upcoming Events

Shows the next 10–20 upcoming events.

Example

|Date|Weekday|
|---|---|
|Aug 5|Wednesday|
|Aug 9|Sunday|
|Aug 13|Thursday|

---

# Technology Stack

## Frontend

- Python
    
- NiceGUI
    

---

## Backend

- FastAPI
    

---

## Database (Later)

Initially

No database

Configuration stored in JSON.

Later options:

- SQLite
    
- PostgreSQL
    

---

# Project Architecture

Phase 1

Frontend only

Mock data

↓

Phase 2

FastAPI Backend

↓

Phase 3

API Integration

↓

Phase 4

Persistent Storage

↓

Phase 5

Deployment

---

# Folder Structure

```
event-cycle/
│
├── frontend/
│   ├── main.py
│   ├── pages/
│   ├── components/
│   ├── layouts/
│   ├── services/
│   ├── models/
│   ├── utils/
│   ├── static/
│   └── data/
│       └── mock_data.py
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   ├── database/
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── docs/
│
├── screenshots/
│
├── tests/
│
├── README.md
│
└── .gitignore
```

---

# Development Plan

## Phase 1

Frontend

- Build UI
    
- Mock data
    
- Navigation
    
- Dashboard
    
- Calendar
    
- Settings
    

---

## Phase 2

Backend

- FastAPI
    
- API Routes
    
- Business Logic
    

---

## Phase 3

Integration

Replace mock data with API requests.

---

## Phase 4

Database

Save:

- Event Name
    
- Interval
    
- Start Date
    

---

## Phase 5

Deployment

Deploy:

Frontend

Backend

Database

---

# User Flow

Application Starts

↓

Load Settings

↓

Read Start Date

↓

Calculate Current Cycle

↓

Calculate Next Event

↓

Display Dashboard

↓

Display Upcoming Events

---

# Core Calculation

Input

```
Start Date

2026-08-01

Interval

4
```

Formula

```
Difference = Today - Start Date

Difference % Interval
```

If remainder equals zero:

Today is Market Day.

Otherwise:

```
Days Remaining = Interval - Remainder
```

---

# Mock Data

```
{
    "event_name": "Work Event",
    "start_date": "2026-08-01",
    "interval": 4
}
```

Later this will come from the FastAPI backend.

---

# Planned API

## GET

```
/settings
```

Returns

```
{
    "event_name": "Work Event",
    "start_date": "2026-08-01",
    "interval": 4
}
```

---

## GET

```
/events
```

Returns calculated upcoming events.

---

## PUT

```
/settings
```

Update event settings.

---

# Future Improvements

- Multiple recurring events
    
- Multiple users
    
- Authentication
    
- Notifications
    
- Email reminders
    
- Telegram notifications
    
- WhatsApp reminders
    
- Mobile responsive layout
    
- Dark mode
    
- Calendar export
    
- iCal support
    
- Event history
    
- Timezone support
    
- Docker support
    
- CI/CD
    
- Unit testing
    
- Integration testing
    

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/event-cycle.git
```

Move into the project

```bash
cd event-cycle
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Development Guidelines

- Use type hints whenever possible.
    
- Keep functions focused on a single responsibility.
    
- Separate UI from business logic.
    
- Avoid duplicating code.
    
- Prefer composition over inheritance.
    
- Write readable, maintainable code.
    
- Use descriptive variable and function names.
    

---

# Coding Standards

- Python 3.12+
    
- PEP 8
    
- Ruff for linting
    
- Black for formatting
    
- pytest for testing
    
- Modular architecture
    
- Clear separation of concerns
    

---

# Why This Project Exists

This project began as a practical solution to a recurring problem at work.

An event occurs every four days, but the weekday changes continuously, making manual calculations easy to get wrong. Rather than relying on memory or counting days repeatedly, this application performs the calculation automatically and presents the information in a clear, simple interface.

At the same time, the project serves as a hands-on learning experience for building modern Python web applications using NiceGUI for the frontend and FastAPI for the backend while following clean architecture and best development practices.

---

# License

This project is released under the MIT License.

Feel free to use, modify, and learn from it.