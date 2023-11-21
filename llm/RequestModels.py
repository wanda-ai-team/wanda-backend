from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar('T')

class Config(BaseModel):
    output: str | None = None
    tone: str | None = None
    writing: str | None = None
    index: str | None = None
    label: str | None = None
    company: str | None = None
    typeOfContent: str | None = None
    url: str | None = None
    gongCallId: str | None = None
    videoId: str | None = None

class LlmRequest(BaseModel):
    userPrompt: T | None = None # type: ignore
    systemPrompt: str | None = None
    config: Config | None = None

class AgentRequest(BaseModel):
    userPrompt: T | None = None # type: ignore
    systemPrompt: str | None = None
    config: str | None = None