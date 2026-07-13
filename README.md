# Backend — Lifebox Academy

API Django + DRF + Knox para la plataforma de cursos de ejemplo.

## Requisitos

- Python 3.11+
- pip

## Setup

```bash
python3.11 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
make migrate
make seed
make runserver
```

API en `http://127.0.0.1:8000`.

## Usuarios de prueba (seeder)

| Rol | Email | Password |
|-----|-------|----------|
| Admin | `admin@lifebox.test` | `password123` |
| Colaborador | `colaborador1@lifebox.test` | `password123` |
| Colaborador | `colaborador2@lifebox.test` | `password123` |

## Endpoints disponibles

| Método | Ruta | Auth | Descripción |
|--------|------|------|-------------|
| POST | `/user/login/` | No | Login → `{ token, user }` |
| POST | `/user/verify-token/` | Token | Verifica sesión |
| GET | `/user/me/` | Token | Usuario actual |
| GET | `/course/` | Admin | Lista cursos de la organización |
| GET | `/collaborator/` | Admin | Lista colaboradores de la organización |

Header de autenticación: `Authorization: Token <token>`

## Estructura

```
apps/
  user/                 # User, Admin, Collaborator, login
  organization/         # Organization
  course/               # Course (+ GET list)
  course_collaborator/  # CourseCollaborator (modelo)
utils/                  # BaseAbstractModel, permissions, factories
docs/FILES.md           # Guía de archivos locales (media)
```

## Tests

```bash
make test
```

## Archivos locales

Ver [docs/FILES.md](docs/FILES.md) para `MEDIA_ROOT` y uploads.
