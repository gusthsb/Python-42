#!/usr/bin/env python3
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    try:
        v_station = SpaceStation.model_validate({
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 6,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": "2023-10-24T12:00:00Z",
            "is_operational": True,
            "notes": "simple note btw",
        })
        status = "Operational" if v_station.is_operational else "Offline"
        print("Valid station created:")
        print(f"ID: {v_station.station_id}")
        print(f"Name: {v_station.name}")
        print(f"Crew: {v_station.crew_size} people")
        print(f"Power: {v_station.power_level}%")
        print(f"Oxygen: {v_station.oxygen_level}%")
        print(f"Status: {status}")
        print(f"Notes: {v_station.notes}")

    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("=" * 40)

    try:
        SpaceStation.model_validate({
            "station_id": "BAF002",
            "name": "SP station",
            "crew_size": 25,
            "power_level": 50.0,
            "oxygen_level": 50.0,
            "last_maintenance": "2023-10-24T12:00:00Z",
        })

    except ValidationError as e:
        print(f"Expected validation error: {e}")


if __name__ == "__main__":
    main()
