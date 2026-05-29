from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator # type: ignore
from datetime import datetime
from enum import Enum
from generated_data import SPACE_MISSIONS
import json

class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_physical(self):
        if self.mission_id[0] != "M":
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(
            member.rank in [Rank.commander, Rank.captain]
            for member in self.crew)
        if has_leader is False:
            raise ValueError("Mission must have at least"
                             "one Commander or Captain")

        all_active = all(member.is_active for member in self.crew)
        if all_active is False:
            raise ValueError("All crew members must be active")
        
        is_valid = (
            self.duration_days <= 365
            or
            sum(member.years_experience >= 5
                for member in self.crew) >= len(self.crew) / 2
        )
        if is_valid is False:
            raise ValueError("Long missions (> 365 days) need at"
                             "least half experienced crew (5+ years)")
        return self

if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("=========================================")

    mission = SpaceMission(**SPACE_MISSIONS[0])

    print("Valid mission created:")
    print("Mission:", mission.mission_name)
    print("ID:", mission.mission_id)
    print("Destination:", mission.destination)
    print("Duration:", mission.duration_days, "days")
    print(f"Budget: ${mission.budget_millions}M")
    print("Crew size:", len(mission.crew))
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) - {member.specialization}")
    print()
    print("=========================================")

    with open("generated_data/invalid_space_missions.json", "r") as f:
        data = json.load(f)

    try:
        missions = SpaceMission(**data[0])
        print("Expected")
    except ValidationError as e:
        print("Expected validation error:")
        msg = e.errors()[0]["msg"]
        print(msg.replace("Value error, ", ""))
