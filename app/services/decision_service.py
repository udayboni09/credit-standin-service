#decision_service.py
# Import the rule loader to load rules.json from disk
from app.rules.rule_loader import load_rules_from_file  # Local module for reading JSON rules

# Import the rule engine to evaluate rules against the application
from app.rules.rule_engine import apply_rules  # Local module containing rule evaluation logic

# Import Path to safely construct file paths
from pathlib import Path  # pathlib is a standard library module for filesystem paths


# Define a function that orchestrates the decision-making process
def process_application(application: dict) -> dict:
    # Build the path to the rules.json file using Path for OS-independent behavior
    rules_path = Path("app/rules/rules.json")  # Path object pointing to rules.json

    # Load the rules from the JSON file
    rules = load_rules_from_file(str(rules_path))  # Convert Path to string for loader

    # Apply the rules to the incoming application
    decision_result = apply_rules(application, rules)  # Returns a structured decision dictionary

    # Return the final decision result to the API layer
    return decision_result  # This will be converted into a Pydantic response model
