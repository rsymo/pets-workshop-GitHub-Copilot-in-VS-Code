
**Setup Step:**
Before starting, install the GitHub MCP server by following instructions at https://code.visualstudio.com/mcp

---
title: Add Favorites Feature to Dog Shelter App
labels: [workshop/75m]
---

Implement a minimal Favorites feature for the Dog Shelter app.

**Requirements:**
- Backend API endpoints:
	- `POST /api/dogs/<dog_id>/favorite` to mark a dog as favorite.
	- `DELETE /api/dogs/<dog_id>/favorite` to remove a dog from favorites.
	- `GET /api/favorites` to list favorited dogs.
- Store favorites per session (or user if accounts exist).
- UI changes:
	- Add a "Favorite" toggle button to each dog card/list item.
	- Visually indicate favorited dogs.
	- Optionally, add a "Show Favorites" filter or section.
- Acceptance Criteria:
	- Users can mark/unmark favorites.
	- Favorites are visually indicated.
	- Favorites persist for the session.
	- API endpoints work as described.
	- Unit tests cover new backend logic and endpoints.
