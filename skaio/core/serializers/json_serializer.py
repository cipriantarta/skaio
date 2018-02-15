import json
from typing import Dict

from skaio.core.base.message import TaskSerializer, Message


class JSONSerializer(TaskSerializer):

    def serialize(self, message: Message) -> Dict:
        return json.dumps(message)

    def deserialize(self, data: Dict) -> Message:
        return json.loads(data)
