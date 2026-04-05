#Rules Engine goes here
# Import typing utilities to describe types for better readability and tooling support
from typing import List, Dict, Any, Optional  # typing is a standard library module for type hints

# Define a function that evaluates a single condition against the application data
def evaluate_condition(application: Dict[str, Any], condition: Dict[str, Any]) -> bool:
    # Extract the field name from the condition (e.g., "credit_score")
    field_name = condition.get("field")
    # Extract the operator from the condition (e.g., ">=", "<", "==")
    operator = condition.get("operator")
    # Extract the value to compare against from the condition (e.g., 700)
    target_value = condition.get("value")

    # Get the actual value from the application using the field name
    actual_value = application.get(field_name)

    # If the field is missing in the application, the condition cannot be satisfied
    if actual_value is None:
        # Return False because we cannot evaluate a missing field
        return False

    # Handle equality operator "=="
    if operator == "==":
        # Return True if the actual value equals the target value
        return actual_value == target_value

    # Handle "!=" (not equal) operator
    if operator == "!=":
        # Return True if the actual value is not equal to the target value
        return actual_value != target_value

    # Handle greater-than operator ">"
    if operator == ">":
        # Return True if the actual value is strictly greater than the target value
        return actual_value > target_value

    # Handle greater-than-or-equal operator ">="
    if operator == ">=":
        # Return True if the actual value is greater than or equal to the target value
        return actual_value >= target_value

    # Handle less-than operator "<"
    if operator == "<":
        # Return True if the actual value is strictly less than the target value
        return actual_value < target_value

    # Handle less-than-or-equal operator "<="
    if operator == "<=":
        # Return True if the actual value is less than or equal to the target value
        return actual_value <= target_value

    # If the operator is not recognized, we treat the condition as not satisfied
    return False


# Define a function that checks whether an application satisfies all conditions in a rule
def rule_matches(application: Dict[str, Any], rule: Dict[str, Any]) -> bool:
    # Get the list of conditions from the rule (e.g., credit_score >= 700, delinquency_flag == False)
    conditions: List[Dict[str, Any]] = rule.get("conditions", [])

    # Iterate over each condition in the rule
    for condition in conditions:
        # Evaluate the current condition against the application
        if not evaluate_condition(application, condition):
            # If any condition fails, the rule does not match, so return False immediately
            return False

    # If all conditions passed, the rule matches the application
    return True


# Define the main function that applies a list of rules to an application
def apply_rules(
    application: Dict[str, Any],  # The input application data (e.g., credit_score, income)
    rules: List[Dict[str, Any]],  # The list of rules loaded from rules.json
    default_decision: str = "REFER"  # The fallback decision if no rule matches
) -> Dict[str, Any]:
    # Initialize a variable to store the best matching rule (if any)
    matched_rule: Optional[Dict[str, Any]] = None

    # Sort rules by priority so that lower priority number means higher precedence
    sorted_rules = sorted(
        rules,  # The list of rules to sort
        key=lambda r: r.get("priority", 9999)  # Use "priority" field, defaulting to a large number
    )

    # Iterate over each rule in priority order
    for rule in sorted_rules:
        # Check if the current rule matches the application
        if rule_matches(application, rule):
            # If it matches, store this rule as the matched rule
            matched_rule = rule
            # Break out of the loop because we only want the first matching rule
            break

    # If we found a matching rule, build a decision response based on that rule
    if matched_rule is not None:
        # Extract the decision from the rule (e.g., "APPROVE", "DECLINE", "REFER")
        decision = matched_rule.get("decision", default_decision)
        # Extract the rule_id to identify which rule fired
        rule_id = matched_rule.get("rule_id", "UNKNOWN_RULE")
        # Extract the reason_code for explainability and audit
        reason_code = matched_rule.get("reason_code", "UNKNOWN_REASON")
        # Extract a human-readable description of the rule
        description = matched_rule.get("description", "No description provided")
        # Extract an optional limit_cap (e.g., maximum approved amount)
        limit_cap = matched_rule.get("limit_cap")

        # Build and return the structured decision response as a dictionary
        return {
            "decision": decision,          # The final decision outcome
            "rule_id": rule_id,            # The ID of the rule that fired
            "reason_code": reason_code,    # The reason code for the decision
            "description": description,    # Human-readable explanation of the rule
            "limit_cap": limit_cap         # Optional limit cap (can be None)
        }

    # If no rule matched, return a default decision response
    return {
        "decision": default_decision,      # Use the default decision (e.g., "REFER")
        "rule_id": "NO_MATCH",             # Indicate that no rule matched
        "reason_code": "NO_RULE_MATCHED",  # Reason code explaining why
        "description": "No rule matched the application; default decision applied.",  # Explanation
        "limit_cap": None                  # No limit cap in default case
    }
