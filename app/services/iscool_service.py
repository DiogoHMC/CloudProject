from app.services.llm_adapter import get_llm_provider

class IsCoolService:
    def __init__(self):
        self.llm = get_llm_provider()

    async def answer(self, user_id: str, topic: str, explanation_level: str, detail_level: str) -> dict:
        # Build a teacher-style prompt based on topic and explanation level
        level = explanation_level.lower()
        if level not in ("beginner", "intermediate", "advanced"):
            level = "beginner"
            
        detail = detail_level.lower()
        
        if detail not in ("high", "low"):
            detail = "low"
            
        if detail == "high":
            detail = "with in-depth explanations and examples"
        elif detail == "low":
            detail = "with concise explanations"

        prompt = (
            f"Você é um professor experiente. Ensine o tópico '{topic}' para um aluno de nível {level}. com um nível de detalhe {detail}. "
            "Seja claro, use exemplos práticos, explique os conceitos passo a passo"
            "Responda de forma didática e amigável. Porem sem muitos emotes ou muitas figuras"
        )

        reply = await self.llm.generate(prompt)
        return {"reply": reply, "model": getattr(self.llm, "__class__").__name__}
