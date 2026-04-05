#failover_service.py
# Import typing for type hints to improve readability and tooling
from typing import Dict, Any  # typing is a standard library module for type annotations


# Define a function that simulates checking the health of the primary DMP system
def check_dmp_health() -> bool:
    # For hackathon purposes, we return False or True based on a simple toggle
    # In a real system, this would call an actual health endpoint or service
    dmp_is_healthy = False  # Hard-coded to False to force stand-in engine usage in demo

    # Return the simulated health status
    return dmp_is_healthy


# Define a function that simulates calling the primary DMP decision engine
def call_dmp_engine(application: Dict[str, Any]) -> Dict[str, Any]:
    # This is a placeholder implementation for hackathon demo only
    # In a real system, this would make an HTTP call or MQ request to FICO DMP
    return {
        "decision": "REFER",  # Simulated decision from DMP
        "rule_id": "DMP_ENGINE",  # Indicate that DMP made the decision
        "reason_code": "DMP_PLACEHOLDER",  # Placeholder reason code
        "description": "Decision returned from simulated DMP engine.",  # Explanation
        "limit_cap": None  # No limit cap in this placeholder
    }
