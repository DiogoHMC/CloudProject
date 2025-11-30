import os
import json
import google.generativeai as genai

# Try to read key from app settings (which loads .env via pydantic BaseSettings)
key = None
try:
    from app.config import settings
    key = settings.GEMINI_API_KEY
except Exception:
    # ignore import errors and fallback to environment
    key = os.getenv("GEMINI_API_KEY")

# If still not found, try loading .env with python-dotenv (if installed)
if not key:
    try:
        from dotenv import load_dotenv
        load_dotenv()
        key = os.getenv("GEMINI_API_KEY")
    except Exception:
        pass

if not key:
    raise SystemExit("GEMINI_API_KEY não encontrada em variáveis de ambiente nem em .env")

genai.configure(api_key=key)

# Lista modelos e imprime de forma legível
models_iter = genai.list_models()
models = []
for m in models_iter:
    # try to extract common attributes into a serializable dict
    if isinstance(m, dict):
        models.append(m)
        continue
    try:
        entry = {}
        if hasattr(m, "name"):
            entry["name"] = getattr(m, "name")
        if hasattr(m, "display_name"):
            entry["display_name"] = getattr(m, "display_name")
        if hasattr(m, "id"):
            entry["id"] = getattr(m, "id")
        # fallback to converting to dict if possible
        if not entry:
            try:
                entry = m.__dict__
            except Exception:
                entry = {"model": str(m)}
        models.append(entry)
    except Exception:
        models.append({"model": str(m)})

print(json.dumps(models, indent=2, ensure_ascii=False))