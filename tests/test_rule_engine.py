#test_rule_engine.py
# Import Path to build file paths safely
from pathlib import Path  # Standard library for filesystem paths

# Import the rule loader to load rules.json
from app.rules.rule_loader import load_rules_from_file  # Local module for JSON rules

# Import the rule engine to apply rules to applications
from app.rules.rule_engine import apply_rules  # Local module for rule evaluation


# Define a test function to verify that a low credit score is declined
def test_low_score_decline():
    # Build the path to rules.json
    rules_path = Path("app/rules/rules.json")

    # Load rules from the JSON file
    rules = load_rules_from_file(str(rules_path))

    # Create an application with a low credit score
    application = {
        "credit_score": 550,  # Below 600, should trigger DECLINE
        "income": 80000,
        "utilization": 30,
        "delinquency_flag": False,
        "requested_amount": 5000,
    }

    # Apply rules to the application
    result = apply_rules(application, rules)

    # Assert that the decision is DECLINE
    assert result["decision"] == "DECLINE"

    # Assert that the rule_id is R1 (from rules.json)
    assert result["rule_id"] == "R1"


# Define a test function to verify that a high score with clean history is approved
def test_high_score_approve():
    # Build the path to rules.json
    rules_path = Path("app/rules/rules.json")

    # Load rules from the JSON file
    rules = load_rules_from_file(str(rules_path))

    # Create an application with a high credit score and no delinquency
    application = {
        "credit_score": 720,  # Above 700
        "income": 90000,
        "utilization": 20,
        "delinquency_flag": False,  # Clean history
        "requested_amount": 7000,
    }

    # Apply rules to the application
    result = apply_rules(application, rules)

    # Assert that the decision is APPROVE
    assert result["decision"] == "APPROVE"

    # Assert that the rule_id is R3 (from rules.json)
    assert result["rule_id"] == "R3"
