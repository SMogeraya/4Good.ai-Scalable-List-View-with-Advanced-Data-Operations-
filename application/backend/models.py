from pydantic import BaseModel
from typing import Optional

class Job(BaseModel):
    job_title: str
    company: Optional[str]
    location: Optional[str]
    employment_type: Optional[str]
    experience_required: Optional[str]
    salary: Optional[str]
    industry: Optional[str]
    posted_date: Optional[str]
