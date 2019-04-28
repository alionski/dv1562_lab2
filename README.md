(Probably nothing to see here if you are not my teacher.)

Structure:
```bash
├── backend
│   ├── Dockerfile
│   ├── requirements.txt (list of pip libs used)
│   ├── run.py (the Python app itself (Flask/uWSGI)
│   ├── static
│   │   └── images (will be used to save requested images)
│   └── templates
│       └── main.html (Jinja template)
├── db
│   └── init_db.sh (script that sets up the Postgres db on startup)
├── docker-compose.yml
├── frontend
│   └── nginx.conf (conf for reverse-proxying to uWSGI via Nginx)
└── README.md
```

Python 3.7, pip 19.1