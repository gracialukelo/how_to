from typing import List, Optional
from dataclasses import dataclass

@dataclass
class Model:
    userId: int
    id: int
    title: str
    body: str

    @staticmethod
    def from_json(json_data):
        return Model(
            userId=json_data.get("userId"),
            id=json_data.get("id"),
            title=json_data.get("title"),
            body=json_data.get("body")
        )

    def to_json(self):
        return {
            "userId": self.userId,
            "id": self.id,
            "title": self.title,
            "body": self.body
        }




