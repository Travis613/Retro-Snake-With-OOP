from abc import ABC, abstractmethod

class GameObject(ABC):

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def update(self):
        pass