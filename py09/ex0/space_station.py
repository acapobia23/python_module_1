from typing import Optional
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


if __name__ == "__main__":
    print("Space Station Data Validation")
    print("========================================")

    station = SpaceStation(
        station_id="SS1",
        name="Alpha Station",
        crew_size=5,
        power_level=80.5,
        oxygen_level=95.0,
        last_maintenance="2024-01-10T12:00:00",
        is_operational=True,
    )
    print("Valid station created:")
    print("ID:", station.station_id)
    print("Name:", station.name)
    print("Crew:", station.crew_size , "people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print("Status:", "Operational" if station.is_operational
           else "Unavailable")
    if station.notes is not None:
        print("Notes:", station.notes)
    print()
    print("========================================")
    print("Expected validation error:")

    try:
        station_err = SpaceStation(
            station_id="SS1",
            name="Alpha Station",
            crew_size=50,
            power_level=80.5,
            oxygen_level=95.0,
            last_maintenance="2024-01-10T12:00:00",
            is_operational=True,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])