from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from alien_contacts import ALIEN_CONTACTS

class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(...,min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(...,ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_physical(self):
        if self.contact_id.find("AC", 0, 2) == -1:
            raise ValueError("Contact ID must start with 'AC'") 
        if self.contact_type == ContactType.PHYSICAL\
         and self.is_verified is False:
            raise ValueError("Physical contacts must be verified") 
        if self.contact_type == ContactType.TELEPATHIC and\
            self.witness_count < 3:
            raise ValueError("Telepathic requires at least 3 witnesses")
        if self.signal_strength >= 7.0 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) should include received messages")
        return self


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("========================================")
    for i in range(2):
        try:
            alien = AlienContact(**ALIEN_CONTACTS[i])
            print("Valid contact report:")
            print("ID:", alien.contact_id)
            print("Type:", alien.contact_type.value.upper())
            print("Location:", alien.location)
            print("Signal:" f"{alien.signal_strength}/10")
            print("Duration:", alien.duration_minutes, "minutes")
            print("Witnesses:", alien.witness_count)
            print(f"Message: '{alien.message_received}'")
            print("========================================")
        except ValidationError as e:
            print("Expected validation error:")
            msg = e.errors()[0]["msg"]
            print(msg.replace("Value error, ", ""))
    