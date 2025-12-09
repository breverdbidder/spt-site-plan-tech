"""
SPT Parking Calculator
Created by Ariel Shapira, Solo Founder | Everest Capital of Brevard LLC

Calculates parking requirements based on:
- ITE Parking Generation Manual (5th Edition)
- Florida Building Code
- Palm Bay / Brevard County local amendments
"""

from dataclasses import dataclass
from typing import Optional, Dict, List
import math


@dataclass
class ParkingRequirement:
    """Parking calculation result"""
    use_type: str
    gross_sf: float
    units: Optional[int]
    base_ratio: str
    required_spaces: int
    ada_spaces: int
    total_spaces: int
    notes: List[str]


# Brevard County / Palm Bay Parking Ratios
PARKING_RATIOS = {
    # Residential
    "single_family": {"ratio": 2.0, "unit": "dwelling unit", "notes": "2 spaces per DU"},
    "multi_family": {"ratio": 1.5, "unit": "dwelling unit", "notes": "1.5 spaces per DU + guest parking"},
    "townhouse": {"ratio": 2.0, "unit": "dwelling unit", "notes": "2 spaces per DU"},
    "senior_housing": {"ratio": 0.5, "unit": "dwelling unit", "notes": "0.5 spaces per DU"},
    
    # Commercial
    "retail": {"ratio": 4.0, "unit": "1,000 SF GFA", "notes": "4 spaces per 1,000 SF"},
    "shopping_center": {"ratio": 4.5, "unit": "1,000 SF GLA", "notes": "4.5 spaces per 1,000 SF GLA"},
    "restaurant": {"ratio": 10.0, "unit": "1,000 SF", "notes": "10 spaces per 1,000 SF or 1 per 3 seats"},
    "fast_food": {"ratio": 12.0, "unit": "1,000 SF", "notes": "12 spaces per 1,000 SF"},
    "bank": {"ratio": 4.0, "unit": "1,000 SF", "notes": "4 spaces per 1,000 SF + queue for drive-thru"},
    
    # Office
    "office_general": {"ratio": 3.0, "unit": "1,000 SF", "notes": "3 spaces per 1,000 SF"},
    "office_medical": {"ratio": 5.0, "unit": "1,000 SF", "notes": "5 spaces per 1,000 SF"},
    "office_dental": {"ratio": 4.5, "unit": "1,000 SF", "notes": "4.5 spaces per 1,000 SF"},
    
    # Industrial
    "warehouse": {"ratio": 1.0, "unit": "1,000 SF", "notes": "1 space per 1,000 SF"},
    "manufacturing": {"ratio": 1.5, "unit": "1,000 SF", "notes": "1.5 spaces per 1,000 SF"},
    "flex_space": {"ratio": 2.0, "unit": "1,000 SF", "notes": "2 spaces per 1,000 SF"},
    
    # Institutional
    "church": {"ratio": 0.33, "unit": "seat", "notes": "1 space per 3 seats"},
    "school_elementary": {"ratio": 2.0, "unit": "classroom", "notes": "2 spaces per classroom"},
    "school_high": {"ratio": 8.0, "unit": "classroom", "notes": "8 spaces per classroom"},
    "daycare": {"ratio": 1.0, "unit": "employee + 1 per 10 children", "notes": "Drop-off lane required"},
    
    # Recreation
    "gym_fitness": {"ratio": 5.0, "unit": "1,000 SF", "notes": "5 spaces per 1,000 SF"},
    "hotel": {"ratio": 1.0, "unit": "room", "notes": "1 space per room + employee parking"},
}


# ADA Parking Requirements (2010 ADA Standards)
ADA_REQUIREMENTS = [
    (25, 1),      # 1-25 spaces: 1 accessible
    (50, 2),      # 26-50 spaces: 2 accessible
    (75, 3),      # 51-75 spaces: 3 accessible
    (100, 4),     # 76-100 spaces: 4 accessible
    (150, 5),     # 101-150 spaces: 5 accessible
    (200, 6),     # 151-200 spaces: 6 accessible
    (300, 7),     # 201-300 spaces: 7 accessible
    (400, 8),     # 301-400 spaces: 8 accessible
    (500, 9),     # 401-500 spaces: 9 accessible
    (1000, 2),    # 501-1000: 2% of total (using 2 as base increment)
]


def calculate_ada_spaces(total_spaces: int) -> int:
    """Calculate required ADA accessible spaces"""
    if total_spaces <= 0:
        return 0
    
    for threshold, required in ADA_REQUIREMENTS:
        if total_spaces <= threshold:
            return required
    
    # Over 1000 spaces: 20 + 1 for each 100 over 1000
    return 20 + math.ceil((total_spaces - 1000) / 100)


def calculate_van_accessible(ada_spaces: int) -> int:
    """At least 1 in 6 accessible spaces must be van accessible"""
    return max(1, math.ceil(ada_spaces / 6))


def calculate_parking(
    use_type: str,
    gross_sf: float = 0,
    units: int = 0,
    seats: int = 0,
    employees: int = 0,
    custom_ratio: Optional[float] = None
) -> ParkingRequirement:
    """
    Calculate parking requirements for a given use.
    
    Args:
        use_type: Type of use (from PARKING_RATIOS keys)
        gross_sf: Gross square footage
        units: Number of dwelling units (for residential)
        seats: Number of seats (for assembly uses)
        employees: Number of employees
        custom_ratio: Override standard ratio if local code differs
    
    Returns:
        ParkingRequirement object with calculation details
    """
    notes = []
    
    if use_type not in PARKING_RATIOS:
        notes.append(f"⚠️ Unknown use type '{use_type}', using general office ratio")
        use_type = "office_general"
    
    ratio_info = PARKING_RATIOS[use_type]
    ratio = custom_ratio if custom_ratio else ratio_info["ratio"]
    unit_type = ratio_info["unit"]
    notes.append(ratio_info["notes"])
    
    # Calculate base requirement
    if "dwelling unit" in unit_type:
        required = math.ceil(ratio * units)
        notes.append(f"Calculation: {ratio} × {units} units = {required} spaces")
    elif "1,000 SF" in unit_type:
        sf_units = gross_sf / 1000
        required = math.ceil(ratio * sf_units)
        notes.append(f"Calculation: {ratio} × {sf_units:.2f} (1,000 SF) = {required} spaces")
    elif "seat" in unit_type:
        required = math.ceil(ratio * seats)
        notes.append(f"Calculation: {ratio} × {seats} seats = {required} spaces")
    elif "room" in unit_type:
        required = math.ceil(ratio * units)
        notes.append(f"Calculation: {ratio} × {units} rooms = {required} spaces")
    elif "classroom" in unit_type:
        required = math.ceil(ratio * units)
        notes.append(f"Calculation: {ratio} × {units} classrooms = {required} spaces")
    else:
        required = math.ceil(ratio * (gross_sf / 1000))
        notes.append(f"Default calculation based on SF")
    
    # Calculate ADA requirements
    ada_spaces = calculate_ada_spaces(required)
    van_accessible = calculate_van_accessible(ada_spaces)
    notes.append(f"ADA: {ada_spaces} accessible spaces ({van_accessible} van accessible)")
    
    # Total (ADA spaces are included in total, not additional)
    total = required
    
    return ParkingRequirement(
        use_type=use_type,
        gross_sf=gross_sf,
        units=units,
        base_ratio=f"{ratio} per {unit_type}",
        required_spaces=required,
        ada_spaces=ada_spaces,
        total_spaces=total,
        notes=notes
    )


def calculate_mixed_use(uses: List[Dict]) -> Dict:
    """
    Calculate parking for mixed-use development with potential shared parking reduction.
    
    Args:
        uses: List of dicts with keys: use_type, gross_sf, units, seats
    
    Returns:
        Dict with individual and total requirements plus shared parking analysis
    """
    results = []
    total_required = 0
    
    for use in uses:
        result = calculate_parking(
            use_type=use.get("use_type", "office_general"),
            gross_sf=use.get("gross_sf", 0),
            units=use.get("units", 0),
            seats=use.get("seats", 0)
        )
        results.append(result)
        total_required += result.required_spaces
    
    # Shared parking analysis (simplified ULI model)
    # Peak times vary by use - potential for 10-15% reduction
    shared_potential = math.ceil(total_required * 0.85)  # 15% potential reduction
    
    return {
        "individual_calculations": [r.__dict__ for r in results],
        "total_without_sharing": total_required,
        "shared_parking_potential": shared_potential,
        "potential_reduction": total_required - shared_potential,
        "ada_total": calculate_ada_spaces(shared_potential),
        "notes": [
            "Shared parking analysis based on ULI Shared Parking methodology",
            "Actual reduction requires detailed time-of-day analysis",
            "Local jurisdiction approval required for shared parking credits"
        ]
    }


# Example usage
if __name__ == "__main__":
    # Example: Multi-story mixed use building
    print("=" * 60)
    print("SPT Parking Calculator - Example Analysis")
    print("Created by Ariel Shapira, Solo Founder")
    print("=" * 60)
    
    # Single use example
    print("\n📊 Single Use Example: 50-unit Apartment Building")
    result = calculate_parking(
        use_type="multi_family",
        units=50
    )
    print(f"  Use Type: {result.use_type}")
    print(f"  Units: {result.units}")
    print(f"  Ratio: {result.base_ratio}")
    print(f"  Required Spaces: {result.required_spaces}")
    print(f"  ADA Spaces: {result.ada_spaces}")
    print(f"  Notes: {result.notes}")
    
    # Mixed use example
    print("\n📊 Mixed Use Example: Retail + Office + Restaurant")
    mixed = calculate_mixed_use([
        {"use_type": "retail", "gross_sf": 10000},
        {"use_type": "office_general", "gross_sf": 20000},
        {"use_type": "restaurant", "gross_sf": 3000}
    ])
    print(f"  Total Without Sharing: {mixed['total_without_sharing']} spaces")
    print(f"  Shared Parking Potential: {mixed['shared_parking_potential']} spaces")
    print(f"  Potential Reduction: {mixed['potential_reduction']} spaces")
    print(f"  Total ADA Required: {mixed['ada_total']} spaces")
