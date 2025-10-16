# WebSockets & Signals with JWT Authentication (Django)

This project demonstrates real-time data updates in Django using **WebSockets**, **Django Channels**, and **Signals** — integrated with secure **JWT authentication**.  

Whenever a new user or post is created, a signal is triggered and a WebSocket message is sent to the frontend instantly without needing a page reload.  

---

##  Features

- **JWT Authentication** (tested with Postman)  
- **Django Signals** for automatic event handling  
- **Django Channels + Daphne** for WebSocket communication  
- **Real-time frontend updates** when a post is created  
- **Modern UI** using HTML, CSS, and WebSocket JavaScript client  

---

##  Tech Stack

- **Backend:** Django, Django REST Framework, Channels  
- **Authentication:** JWT (JSON Web Tokens)  
- **Server:** Daphne (ASGI server for WebSockets)  
- **Database:** SQLite (can be switched to PostgreSQL)  
- **Frontend:** HTML, CSS, Vanilla JS (WebSocket API)

---

##  How It Works

1. A user is authenticated via JWT.  
2. When a new post is created, a **Django Signal** (`post_save`) is triggered.  
3. The signal sends a message through the **Channel Layer**.  
4. The **WebSocket consumer** listens for this event and pushes a live update to the frontend.  
5. The frontend automatically updates the total post count and displays the user’s email who created the post — all in real-time.  

---

##  Setup Instructions

1. Clone the Repository
   ```bash
   git clone https://github.com/Faseeh07-lang/WebSockets_Signals_JWT.git
   cd WebSockets_Signals_JWT
2. Create and activate virtual enviroment
3. Install dependencies
4. Run migrations
5. Run Daphne server: daphne JWT.asgi:application
6. Create posts from postman
7. See in browser
