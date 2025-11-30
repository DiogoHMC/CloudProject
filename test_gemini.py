"""
Quick test script for Gemini Integration
Testa se a API está funcionando com Gemini
"""

import asyncio
import httpx

async def test_api():
    """Testa o endpoint /v1/ask"""
    
    url = "http://localhost:8000/v1/ask"
    
    payload = {
        "user_id": "test_user",
        "prompt": "Qual é o capital da França?"
    }
    
    print("🧪 Testando API IsCoolGPT com Gemini...")
    print(f"📝 Prompt: {payload['prompt']}")
    print("-" * 50)
    
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(url, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                print("✅ Sucesso!")
                print(f"📌 Modelo utilizado: {data['model']}")
                print(f"💬 Resposta:\n{data['reply']}")
                return True
            else:
                print(f"❌ Erro: Status {response.status_code}")
                print(f"Detalhes: {response.text}")
                return False
                
    except Exception as e:
        print(f"❌ Erro ao conectar: {str(e)}")
        print("💡 Verifique se a API está rodando com:")
        print("   python -m uvicorn app.main:app --reload")
        return False

async def test_health():
    """Testa o endpoint raiz"""
    url = "http://localhost:8000/"
    
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                print(f"✅ API Health Check: {data}")
                return True
    except Exception as e:
        print(f"❌ API não está respondendo: {e}")
        return False

async def main():
    print("\n" + "="*50)
    print("🚀 IsCoolGPT - Teste Gemini Integration")
    print("="*50 + "\n")
    
    # Test health
    if await test_health():
        print("\n" + "-"*50 + "\n")
        # Test API
        await test_api()
    
    print("\n" + "="*50)

if __name__ == "__main__":
    asyncio.run(main())
