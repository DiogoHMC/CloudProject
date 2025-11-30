from typing import Protocol
from abc import abstractmethod
import os
import httpx
import google.generativeai as genai
import asyncio

from app.config import settings


# ============================================
# Base interface
# ============================================
class LLMProvider(Protocol):
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        ...


# ============================================
# Mock provider (uso local/dev)
# ============================================
class MockLLM:
    async def generate(self, prompt: str) -> str:
        return f"RESP_MOCK: Recebi: {prompt[:200]}"


# ============================================
# OpenAI provider
# ============================================
class OpenAIProvider:
    def __init__(self, api_key: str | None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")

    async def generate(self, prompt: str) -> str:
        if not self.api_key:
            raise RuntimeError("OpenAI API key not configured")

        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 300
        }

        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(url, json=payload, headers=headers)
            r.raise_for_status()
            data = r.json()

            return data["choices"][0]["message"]["content"]


# ============================================
# Gemini provider (Google AI)
# ============================================
class GeminiProvider:
    def __init__(self, api_key: str | None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise RuntimeError("Gemini API key not configured")

        genai.configure(api_key=self.api_key)

        # modelo correto SEM prefixo "models/"
        self.model_name = settings.GEMINI_MODEL or "gemini-2.5-flash"

        # cria o modelo
        self.model = genai.GenerativeModel(self.model_name)

    async def generate(self, prompt: str) -> str:
        try:
            # generate_content é síncrono → rodar em thread
            resp = await asyncio.to_thread(
                self.model.generate_content,
                prompt
            )

            # verificar se tem candidatos
            if not resp.candidates:
                raise RuntimeError(
                    f"Gemini returned no candidates. prompt_feedback={resp.prompt_feedback}"
                )

            candidate = resp.candidates[0]

            # verificar partes de conteúdo
            parts = candidate.content.parts if candidate.content else []
            if not parts:
                raise RuntimeError(
                    f"Gemini returned empty content. finish_reason={candidate.finish_reason}"
                )

            # resposta final
            return resp.text

        except Exception as e:
            raise RuntimeError(f"Gemini API error: {str(e)}")


# ============================================
# Factory
# ============================================
def get_llm_provider() -> LLMProvider:
    provider = settings.LLM_PROVIDER.lower()

    if provider == "openai":
        return OpenAIProvider(settings.OPENAI_API_KEY)

    if provider == "gemini":
        return GeminiProvider(settings.GEMINI_API_KEY)

    # fallback → mock
    return MockLLM()
