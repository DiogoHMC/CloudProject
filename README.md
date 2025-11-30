# 🚀 IsCoolGPT - API com Suporte a Gemini

Uma API FastAPI que funciona como adaptador para diferentes provedores de IA (OpenAI, Gemini, Mock).

## 📋 O que é este projeto?

- **Framework**: FastAPI
- **Propósito**: API REST que integra diferentes provedores de IA
- **Endpoint Principal**: `POST /v1/ask` - recebe prompt e retorna resposta da IA

## 🔧 Como funciona?

```
┌─────────────┐
│   Request   │
│  (prompt)   │
└──────┬──────┘
       │
       v
┌──────────────────────┐
│   IsCoolService      │
│  (lógica central)    │
└──────┬───────────────┘
       │
       v
┌─────────────────────────────┐
│    LLM Adapter (Factory)    │
│  - MockLLM                  │
│  - OpenAIProvider           │
│  - GeminiProvider ✨ (NOVO) │
└──────────┬──────────────────┘
           │
           v
     ┌─────────┐
     │   API   │
     └─────────┘
```

## 🛠️ Como usar Gemini API

### Passo 1: Obter a API Key do Gemini

1. Acesse: https://ai.google.dev
2. Clique em "Get API key"
3. Crie um novo projeto no Google Cloud Console
4. Crie uma nova chave de API
5. Copie a chave

### Passo 2: Configurar Variáveis de Ambiente

```bash
# Copie o arquivo exemplo
cp .env.example .env

# Edite o arquivo .env e adicione:
LLM_PROVIDER=gemini
GEMINI_API_KEY=sua_chave_gemini_aqui
```

### Passo 3: Instalar Dependências

```bash
# Criar ambiente virtual (recomendado)
python -m venv venv

# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### Passo 4: Executar Localmente

```bash
# Modo desenvolvimento (com reload automático)
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Modo produção
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

A API estará disponível em: **http://localhost:8000**

## 📡 Testar a API

### Exemplo de Request:

```bash
curl -X POST "http://localhost:8000/v1/ask" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "prompt": "O que é uma IA?"
  }'
```

### Resposta esperada:

```json
{
  "reply": "Uma Inteligência Artificial (IA) é um sistema computacional...",
  "model": "GeminiProvider"
}
```

## 🐳 Com Docker

### Build:

```bash
docker build -t iscoolGpt .
```

### Run:

```bash
docker run -e GEMINI_API_KEY="sua_chave_aqui" \
           -e LLM_PROVIDER="gemini" \
           -p 8000:8000 \
           iscoolGpt
```

### Com Docker Compose:

```yaml
# docker-compose.yml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      LLM_PROVIDER: gemini
      GEMINI_API_KEY: ${GEMINI_API_KEY}
```

```bash
# Executar
export GEMINI_API_KEY="sua_chave_aqui"
docker-compose up
```

## ⚙️ Opções de Providers

### 1️⃣ Mock (Padrão - para testes)
```
LLM_PROVIDER=mock
```
Não requer API key, útil para testes e desenvolvimento.

### 2️⃣ OpenAI
```
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...
```

### 3️⃣ Gemini (Recomendado) ✨
```
LLM_PROVIDER=gemini
GEMINI_API_KEY=AIza...
```

## 📁 Estrutura do Projeto

```
app/
├── main.py              # Entry point FastAPI
├── config.py            # Configurações (env vars)
├── schemas.py           # Modelos Pydantic
├── api/
│   └── v1.py           # Rotas da API
└── services/
    ├── iscool_service.py      # Lógica da aplicação
    └── llm_adapter.py         # Providers de IA (MODIFICADO)
```

## 🧪 Testes

```bash
# Executar testes
pytest test/

# Com cobertura
pytest --cov=app test/
```

## 📝 Arquivos Modificados

- ✅ `requirements.txt` - Adicionado `google-generativeai`
- ✅ `app/config.py` - Adicionado `GEMINI_API_KEY`
- ✅ `app/services/llm_adapter.py` - Adicionado `GeminiProvider`
- ✅ `.env.example` - Instruções para Gemini

## 🚨 Troubleshooting

### Erro: "Gemini API key not configured"
- Verifique se `GEMINI_API_KEY` está definida em `.env`
- Verifique se `LLM_PROVIDER=gemini`

### Erro: "ModuleNotFoundError: No module named 'google'"
- Execute: `pip install -r requirements.txt`

### Erro de Rate Limit do Gemini
- Aguarde alguns segundos e tente novamente
- Consulte limites em: https://ai.google.dev/pricing

## 📚 Recursos Úteis

- [Documentação Gemini API](https://ai.google.dev/docs)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)

---

**Autor**: Seu Nome  
**Data**: Novembro 2025  
**Status**: ✅ Funcionando com Gemini API
