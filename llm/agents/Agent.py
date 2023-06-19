from abc import ABC, abstractmethod

class Agent(ABC):
    @abstractmethod
    def main(self, userPrompt, systemPrompt, config):
        pass
