(Nothing to see here if you are not my teacher.)

Structure:
+-- backend
|   -- the Python app itself (Flask/uWSGI + Jinja templates)
|   -- Dockerfile
+-- db
|   -- init_db.sh script which sets up the Postgres db on startup
+-- frontend
|   -- nginx.conf for reverse-proxying to uWSGI via Nginx
+-- docker-compose.yml

Python 3.7, pip 19.1