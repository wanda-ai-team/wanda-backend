from abc import ABC, abstractmethod

class LlmTools(ABC):
    @abstractmethod
    def main(self, userPrompt, systemPrompt, config):
        pass
