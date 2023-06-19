from pydantic import BaseModel

class LlmRequest(BaseModel):
    userPrompt: str
    systemPrompt: str
    config: str

class AgentRequest(BaseModel):
    userPrompt: str
    systemPrompt: str
    config: str