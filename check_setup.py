#!/usr/bin/env python3
"""
CHECKLIST - Verificação da Integração Gemini
Execute este script para validar se tudo está configurado corretamente
"""

import os
import sys
from pathlib import Path

def check_mark(condition, message):
    """Printa ✅ ou ❌ dependendo da condição"""
    symbol = "✅" if condition else "❌"
    print(f"{symbol} {message}")
    return bool(condition)

def main():
    print("\n" + "="*60)
    print("🔍 CHECKLIST - Integração IsCoolGPT + Gemini")
    print("="*60 + "\n")
    
    base_path = Path(__file__).parent
    results = []
    
    # 1. Verificar estrutura de arquivos
    print("📁 Verificando estrutura de arquivos...")
    results.append(check_mark(
        (base_path / "app").exists(),
        "Diretório 'app/' encontrado"
    ))
    results.append(check_mark(
        (base_path / "requirements.txt").exists(),
        "Arquivo 'requirements.txt' encontrado"
    ))
    results.append(check_mark(
        (base_path / ".env").exists(),
        "Arquivo '.env' encontrado"
    ))
    results.append(check_mark(
        (base_path / "app" / "config.py").exists(),
        "Arquivo 'app/config.py' encontrado"
    ))
    results.append(check_mark(
        (base_path / "app" / "services" / "llm_adapter.py").exists(),
        "Arquivo 'app/services/llm_adapter.py' encontrado"
    ))
    
    print("\n📦 Verificando dependências...")
    
    # 2. Verificar requirements.txt
    req_file = base_path / "requirements.txt"
    with open(req_file, 'r', encoding='utf-8') as f:
        req_content = f.read()
    
    results.append(check_mark(
        "google-generativeai" in req_content,
        "google-generativeai está em requirements.txt"
    ))
    results.append(check_mark(
        "fastapi" in req_content,
        "fastapi está em requirements.txt"
    ))
    results.append(check_mark(
        "uvicorn" in req_content,
        "uvicorn está em requirements.txt"
    ))
    
    print("\n⚙️  Verificando configurações...")
    
    # 3. Verificar config.py
    config_file = base_path / "app" / "config.py"
    with open(config_file, 'r', encoding='utf-8') as f:
        config_content = f.read()
    
    results.append(check_mark(
        "GEMINI_API_KEY" in config_content,
        "GEMINI_API_KEY configurável em config.py"
    ))
    results.append(check_mark(
        "LLM_PROVIDER" in config_content,
        "LLM_PROVIDER configurável em config.py"
    ))
    
    print("\n🔌 Verificando GeminiProvider...")
    
    # 4. Verificar llm_adapter.py
    adapter_file = base_path / "app" / "services" / "llm_adapter.py"
    with open(adapter_file, 'r', encoding='utf-8') as f:
        adapter_content = f.read()
    
    results.append(check_mark(
        "class GeminiProvider" in adapter_content,
        "Classe GeminiProvider implementada"
    ))
    results.append(check_mark(
        "import google.generativeai as genai" in adapter_content,
        "Google Generative AI importado"
    ))
    results.append(check_mark(
        "genai.GenerativeModel" in adapter_content,
        "GenerativeModel do Gemini utilizado"
    ))
    results.append(check_mark(
        'provider == "gemini"' in adapter_content,
        "Factory pattern inclui caso 'gemini'"
    ))
    
    print("\n🔐 Verificando variáveis de ambiente...")
    
    # 5. Verificar .env
    env_file = base_path / ".env"
    with open(env_file, 'r', encoding='utf-8') as f:
        env_content = f.read()
    
    results.append(check_mark(
        "LLM_PROVIDER" in env_content,
        "LLM_PROVIDER definido em .env"
    ))
    results.append(check_mark(
        "GEMINI_API_KEY" in env_content,
        "GEMINI_API_KEY definido em .env"
    ))
    
    # Verificar se chave está configurada
    gemini_key_configured = "GEMINI_API_KEY=AIza" in env_content or \
                           (os.getenv("GEMINI_API_KEY") and \
                            os.getenv("GEMINI_API_KEY").startswith("AIza"))
    
    results.append(check_mark(
        gemini_key_configured,
        "⚠️  Chave do Gemini configurada (ou defina via env var)"
    ))
    
    print("\n📚 Verificando documentação...")
    
    # 6. Verificar documentação
    results.append(check_mark(
        (base_path / "README.md").exists(),
        "README.md criado"
    ))
    results.append(check_mark(
        (base_path / "GUIA_RAPIDO.md").exists(),
        "GUIA_RAPIDO.md criado"
    ))
    results.append(check_mark(
        (base_path / "RESUMO_IMPLEMENTACAO.md").exists(),
        "RESUMO_IMPLEMENTACAO.md criado"
    ))
    
    print("\n" + "="*60)
    
    # Summary
    total = len(results)
    passed = sum(results)
    failed = total - passed
    percentage = (passed / total * 100) if total > 0 else 0
    
    print("\n" + "="*60)
    
    if failed == 0:
        print("\n🎉 TUDO CONFIGURADO! Você está pronto para usar!")
        print("\n⚠️  PRÓXIMOS PASSOS:")
        print("  1. Adicione sua chave Gemini no arquivo .env")
        print("  2. Execute: python -m venv venv")
        print("  3. Execute: venv\\Scripts\\activate")
        print("  4. Execute: pip install -r requirements.txt")
        print("  5. Execute: python -m uvicorn app.main:app --reload")
        print("\n📍 Acesse: http://localhost:8000/docs\n")
        return 0
    else:
        print("\n⚠️  Alguns itens não estão configurados!")
        print("    Verifique os itens marcados com ❌\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
