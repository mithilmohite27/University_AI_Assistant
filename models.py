from dataclasses import dataclass, field
from typing import List, Optional, Dict
from enum import Enum

class UniversityType(Enum):
    PUBLIC = "public"
    PRIVATE = "private"

@dataclass
class University:
    name: str
    type: UniversityType
    location: Dict[str, str] = field(default_factory=lambda: {
        "city": "", "region": "", "country": "", "address": ""
    })
    rankings: Dict[str, int] = field(default_factory=dict)
    tuition: Dict[str, float] = field(default_factory=dict)
    programs: List[str] = field(default_factory=list)
    admission_rate: Optional[float] = None
    student_population: Optional[int] = None
    international_student_info: Dict[str, str] = field(default_factory=dict)
    facilities: List[str] = field(default_factory=list)
    website: Optional[str] = None

@dataclass
class UniversitySearchState:
    location: str
    filters: Dict[str, any] = field(default_factory=dict)
    universities: List[University] = field(default_factory=list)
    cost_of_living: Dict[str, float] = field(default_factory=dict)
    local_transport: Dict[str, str] = field(default_factory=dict)
    running_summary: Optional[str] = None
    research_loop_count: int = 0
    sources_gathered: List[str] = field(default_factory=list)
    web_research_results: List[Dict[str, str]] = field(default_factory=list)