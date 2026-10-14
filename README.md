# PACT

Mini project for Team 1. Small Flask API around `greet()`.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m src.web            # http://127.0.0.1:5000
python -m pytest -q
```

## Endpoints

| Method | Path | Example |
|---|---|---|
| GET | `/health` | `{"status": "ok"}` |
| GET | `/languages` | `{"languages": ["ar", "en"]}` |
| GET | `/greet?name=abood&lang=ar` | `{"message": "مرحباً من PACT، abood!", "lang": "ar"}` |

See [CONTRIBUTING.md](CONTRIBUTING.md) for the branch and PR workflow.
