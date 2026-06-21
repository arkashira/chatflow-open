import json
import gzip
from dataclasses import dataclass
from typing import List

@dataclass
class Message:
    id: int
    text: str

class ChatFlowOpen:
    def __init__(self):
        self.messages = {}

    def import_data(self, file_path: str) -> dict:
        try:
            with gzip.open(file_path, 'rt') as file:
                data = json.load(file)
            imported_messages = []
            for message in data:
                message_id = message['id']
                if message_id not in self.messages:
                    self.messages[message_id] = Message(**message)
                    imported_messages.append(message)
            return {
                'imported': len(imported_messages),
                'total': len(data),
                'duplicates': len(data) - len(imported_messages)
            }
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")

    def validate_schema(self, data: List[dict]) -> bool:
        required_fields = ['id', 'text']
        for message in data:
            if not all(field in message for field in required_fields):
                return False
        return True
