EventHub
Brief
1. Overview
What You Are Building

EventHub is a backend API for a simplified event ticketing platform. Users can:

Browse events

Reserve seats

Cancel reservations

Context

Ticketing platforms need to handle situations where two users might book the last available seat at the same time. You will handle seat availability carefully in your reservation logic.

You will build this using:

Django ORM for models and database queries

DRF serializers for validation

ViewSets and Routers for clean URL routing

2. How to run project
docker-compose up -d
python3 manage.py runserver
python3 manage.py makemigrations
python3 manage.py migrate

API endpoints screensshots are in screenshot folder