# Dog shelter

This is an application to allow people to look for dogs to adopt. It is built in a monorepo, with a Flask-based backend and Astro-based frontend.

## Frameworks Used

- **Backend:** Flask (Python), SQLAlchemy (ORM)
- **Frontend:** Astro (static site builder), Svelte (components), Tailwind CSS (styling)

## Database

- SQLite database file: `server/dogshelter.db`
- Models and initialization: `server/models/`

## Frontend Structure

- Built with Astro and Svelte, styled with Tailwind CSS
- Main page: `client/src/pages/index.astro`
- Components: `client/src/components/`
- Layout: `client/src/layouts/Layout.astro`
- Global styles: `client/src/styles/global.css`
- Config: `client/astro.config.mjs`, `client/package.json`

## Backend Structure

- Flask app entry: `server/app.py`
- Models: `server/models/`
- Database seeding: `server/utils/seed_database.py`
- Unit tests: `server/test_app.py`

## Listing Dogs

- **API endpoint:** `/api/dogs` in `server/app.py`
- **Frontend component:** `client/src/components/DogList.svelte`
- **Frontend page:** `client/src/pages/index.astro`
- **Model:** `server/models/dog.py`
- **Tests:** `server/test_app.py`


**Note:**  
- All backend routes require unit tests (see `server/test_app.py`).  
- When writing tests, always mock database calls.  
- Frontend should use dark mode and a modern look.