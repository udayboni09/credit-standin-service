
# Import BaseModel from pydantic to define data models for request and response validation

# Pydantic ensures that incoming JSON data is validated and converted to proper Python types

from pydantic import BaseModel  # pydantic is a widely used library for data validation

# Import Optional to allow fields that may or may not be present
from typing import Optional  # typing is a standard library module for type hints


# Define the structure of the incoming credit application request
class ApplicationRequest(BaseModel):  # Inherits from BaseModel to enable validation
    credit_score: int  # Applicant's credit score (integer)
    income: float  # Applicant's income (float for precision)
    utilization: float  # Credit utilization percentage
    delinquency_flag: bool  # Whether applicant has past delinquencies
    requested_amount: Optional[float] = None  # Optional field for loan amount


# Define the structure of the decision response returned by the rule engine
class DecisionResponse(BaseModel):  # Also inherits from BaseModel for validation
    decision: str  # Final decision (APPROVE / DECLINE / REFER)
    rule_id: str  # ID of the rule that fired
    reason_code: str  # Reason code for explainability
    description: str  # Human-readable explanation
    limit_cap: Optional[float] = None  # Optional approved limit
