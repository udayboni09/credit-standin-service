#simulator.py
# Import typing utilities for type hints
from typing import List, Dict, Any  # typing is a standard library module for type annotations

# Import the decision service to reuse the same logic as the API
from app.services.decision_service import process_application  # Local business logic


# Define a function that simulates multiple applications
def run_simulation(applications: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # Initialize an empty list to store results for each application
    results = []

    # Loop through each application in the input list
    for app in applications:
        # Process the application using the same logic as the API
        decision = process_application(app)

        # Append the decision result to the results list
        results.append(decision)

    # Return the list of decision results
    return results
