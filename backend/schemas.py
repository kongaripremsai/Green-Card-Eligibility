from pydantic import BaseModel

class Applicant(BaseModel):
    family_in_us: bool
    job_offer: bool
    education: str
    investment: float
    refugee_status: bool
    country_in_dv_list: bool