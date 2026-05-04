# antyperfectionism_habit_tracker
I am a great fan of habit trackers, to do lists and all other productivity-enhancing solutions. So... why can't I have my own? (:

## Docker frontend dependency note
If you change frontend dependencies in `frontend/package.json`, you need to rebuild the frontend container so the new packages are installed.

Use one of these commands:

```bash
docker compose up --build frontend
```

If the frontend still uses old dependencies, recreate containers and volumes with:

```bash
docker compose down
docker compose up --build
```
