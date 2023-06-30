from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar('T')

class Config(BaseModel):
    output: str | None
    tone: str | None
    writing: str | None
    url: object | None

class LlmRequest(BaseModel):
    userPrompt: T
    systemPrompt: str
    config: Config

class AgentRequest(BaseModel):
    userPrompt: T
    systemPrompt: str
    config: str