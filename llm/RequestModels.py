from pydantic import BaseModel

class Config(BaseModel):
    output: str | None
    tone: str | None
    writing: str | None
    url: str | None

class LlmRequest(BaseModel):
    userPrompt: str
    systemPrompt: str
    config: Config

class AgentRequest(BaseModel):
    userPrompt: str
    systemPrompt: str
    config: str