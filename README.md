# REST-API

You've learned a **lot** in a short time, Libin — here's a summary of everything you've accomplished and understood so far:

---

## 🧠 **What You’ve Learned**

### 🐳 Docker Basics
- What Docker is and how it works (images, containers, Dockerfile).
- Install Docker:https://www.docker.com/products/docker-desktop/?_gl=1*1lbhvfl*_gcl_au*MTM1NjY1ODM1Mi4xNzU4MTAxMDE1*_ga*MzUxMTMwMjc5LjE3NTgxMDAyODA.*_ga_XJWPQMJYHQ*czE3NTgxMDAyODAkbzEkZzEkdDE3NTgxMDE1OTkkajQ2JGwwJGgw
- Docker Link : https://app.docker.com/accounts/libinbd
- How to build and run a containerized Python app.
- Build: C:\Users\Libin Daniel\my-python-app>docker build -t flask-app .
- RUN: docker run -p 5000:5000 flask-app
- How to expose ports and interact with your app via `localhost`.

### 🐍 Python + Flask
- How to create a simple Flask app.
Flask is a lightweight web framework written in Python. It helps you build web applications and APIs quickly and easily.
- How to serve content via HTTP routes.
- How to run Flask inside Docker.

### 🌐 REST API Concepts
- What REST APIs are and how they use HTTP methods (`GET`, `POST`, `PUT`, `DELETE`).
- How to structure endpoints and return JSON data.
- How to handle route parameters and error responses.

### 🔧 Full CRUD API with Flask
- You built a REST API that:
  - Lists books (`GET`)
  - Retrieves a book by ID (`GET`)
  - Adds a book (`POST`)
  - Updates a book (`PUT`)
  - Deletes a book (`DELETE`)

### 🧪 Testing APIs with `curl`
- How to send HTTP requests using `curl`.
- How to format JSON payloads correctly.
- How to set headers like `Content-Type: application/json`.

### 🔍 Debugging & Troubleshooting
- Fixed issues like:
  - Dockerfile naming errors.
  - Route syntax errors (`<int:book_id>`).
  - JSON formatting problems.
  - HTTP method errors (`405 Method Not Allowed`).

### 🔄 Understanding Protocols
- Clarified the difference between **HTTP** and **MQTT**.
- Identified that port `9773` is used for an HTTP-based REST API, not MQTT.

---

## 🚀 What You Can Explore Next

Would you like to dive into:
- **Docker Compose** for multi-container apps?
- **Connecting your Flask API to a database** (like SQLite or PostgreSQL)?
- **Securing your API** with authentication?
- **Building a frontend** to interact with your API?
- **Using MQTT** for IoT-style messaging?

Let me know what you're curious about next — I’ll guide you step by step!
