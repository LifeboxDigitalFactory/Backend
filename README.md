# Backend — Lifebox Academy

API Django + DRF + Knox para la plataforma de cursos de ejemplo.

## Requisitos (entorno vacío)

Instala estas herramientas de sistema **antes** de clonar o correr el proyecto. Por defecto no necesitas Docker ni una base de datos externa (el proyecto usa SQLite en disco), pero eres libre de usar Docker u otra base de datos si lo prefieres.

### 1. Git

Necesario para clonar el repositorio.

| OS | Instalación |
|----|-------------|
| macOS | `xcode-select --install` (incluye Git y make) |
| Linux (Debian/Ubuntu) | `sudo apt update && sudo apt install git` |
| Windows | [Git for Windows](https://git-scm.com/download/win) o `winget install Git.Git` |

### 2. Python 3.11+

Incluye `pip` y el módulo `venv`. Verifica con `python3 --version` (debe ser ≥ 3.11).

| OS | Instalación |
|----|-------------|
| macOS | `brew install python@3.11` o [python.org](https://www.python.org/downloads/) |
| Linux (Debian/Ubuntu) | `sudo apt install python3.11 python3.11-venv python3-pip` |
| Windows | Instalador desde [python.org](https://www.python.org/downloads/) (marca “Add python.exe to PATH”) |

### 3. make

Usado por los comandos del `Makefile` (`make migrate`, `make runserver`, etc.).

| OS | Instalación |
|----|-------------|
| macOS | Ya viene con `xcode-select --install`; si falta: `brew install make` |
| Linux (Debian/Ubuntu) | `sudo apt install make` |
| Windows | `choco install make`, o usa [WSL](https://learn.microsoft.com/windows/wsl/) y sigue los pasos de Linux |

### Resumen rápido (copiar/pegar)

**macOS**

```bash
xcode-select --install
brew install python@3.11   # si no tienes Python 3.11+
```

**Linux (Debian/Ubuntu)**

```bash
sudo apt update
sudo apt install git make python3.11 python3.11-venv python3-pip
```

**Windows**

1. Instala [Git](https://git-scm.com/download/win) y [Python 3.11+](https://www.python.org/downloads/).
2. Instala `make` (`choco install make`) o trabaja desde WSL.

## Setup

```bash
git clone <url-del-repo>
cd Backend

python3.11 -m venv .venv
source .venv/bin/activate   # Windows (cmd): .venv\Scripts\activate
                            # Windows (PowerShell): .venv\Scripts\Activate.ps1

pip install -r requirements.txt
cp .env.example .env
make migrate
make seed
make runserver
```

API en `http://127.0.0.1:8000`.

Dependencias Python (se instalan con `pip install -r requirements.txt`):

- Django 4.2
- djangorestframework
- django-rest-knox
- django-cors-headers
- python-dotenv

Base de datos: SQLite por defecto (`db.sqlite3`, se crea al migrar). No es obligatorio usar PostgreSQL, Redis u otros servicios, pero puedes hacerlo si lo prefieres.

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
