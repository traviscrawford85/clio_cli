from abc import ABC, abstractmethod
from typing import Dict, Any

class ISlackService(ABC):
    @abstractmethod
    async def send_message(self, channel: str, text: str, metadata: Dict[str, Any] = {}) -> None:
        """Send a message to a Slack channel"""
        pass

    @abstractmethod
    async def notify_user(self, user_id: str, message: str) -> None:
        """Notify a specific Slack user"""
        pass