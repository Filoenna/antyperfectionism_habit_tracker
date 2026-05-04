#!/bin/sh
set -e

cd /app

echo "Running database migrations to be sure..."
uv run alembic upgrade head

echo "Starting backend..."
exec uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
