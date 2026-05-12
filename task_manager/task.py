from dataclasses import dataclass, field
import datetime
import uuid


@dataclass
class Task:
    title: str
    id: str = str(uuid.uuid1())
    done: bool = field(default=False)
    created_at: datetime = field(default_factory=datetime.utcnow)

    def mark_as_done(self):
        self.done = True
        return self.done

    def to_dict(self):
        newdict = {
            "id": self.id,
            "title": self.title,
            "status": self.done,
            "date": self.created_at.isoformat(),
        }

        return newdict

    @classmethod
    def from_dict(cls, newdict):
        return cls(
            title=newdict["title"],
            id=newdict["id"],
            done=newdict["status"],
            created_at=newdict["date"],
        )
