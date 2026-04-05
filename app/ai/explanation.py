#AI folder
# Import typing utilities for type hints
from typing import Dict, Any  # typing is a standard library module for type annotations


# Define a function that generates a simple explanation for the decision
# In a real Wells Fargo environment, this would call Tachyon or an internal LLM
def generate_explanation(decision_payload: Dict[str, Any]) -> str:
    # Extract the decision from the payload
    decision = decision_payload.get("decision")

    # Extract the rule description for human readability
    description = decision_payload.get("description")

    # Extract the reason code for audit and traceability
    reason_code = decision_payload.get("reason_code")

    # Build a simple explanation string
    explanation = (
        f"The application was evaluated and resulted in a '{decision}' decision. "
        f"Reason: {reason_code}. Details: {description}."
    )

    # Return the explanation text
    return explanation
