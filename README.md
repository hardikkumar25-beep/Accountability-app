"# Accountability-app" 
accountability_app/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── database/
│   │   ├── database.py
│   │   └── models/
│   │       ├── user.py
│   │       ├── profile.py
│   │       ├── goal.py
│   │       ├── task.py
│   │       ├── task_event.py
│   │       └── assessment.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── profile.py
│   │   ├── goal.py
│   │   ├── task.py
│   │   └── assessment.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── goals.py
│   │   ├── tasks.py
│   │   └── assessments.py
│   │
│   └── services/
│       ├── task_service.py
│       ├── analytics_service.py
│       └── ai_service.py
│
├── alembic/
├── .env
├── alembic.ini
├── requirements.txt
└── README.md