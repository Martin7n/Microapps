from dataclasses import dataclass, field
from datetime import datetime



@dataclass
class ESGRecord:
    # raw / orig_data
    original: dict

    leasing_type: str | None = None
    appendix_id: str | None = None
    appendix_start_date: str | None = None
    appendix_status: str | None = None
    group_asset: str | None = None
    asset_type: str | None = None
    equipment_type: str | None = None
    brand: str | None = None
    equipment_id: str | None = None
    equipment_allocation_id: str | None = None
    model: str | None = None
    vin: str | None = None
    registration: str | None = None
    weight: float | None = None
    weight_measure: str | None = None
    seats: int | None = None
    axles: int | None = None
    emissions: float | None = None
    fuel_type: str | None = None

    # Processing fields
    normalized: list[str] = field(default_factory=list)

    detected_brand: str | None = None
    detected_model: str | None = None
    detected_category : str | None = None
    detected_seats : int | None = None
    detected_weight : str | None = None
    weight_measure_update : float | None = None
    detected_emissions : float | None = None
    detected_fuel : str | None = None
    green : str | None = None
    mileage : float | None = None
    detected_manufacturer : str | None = None
    manufacturer_country : str | None = None
    confidence: float = 0.0

    errors: list[str] = field(default_factory=list)