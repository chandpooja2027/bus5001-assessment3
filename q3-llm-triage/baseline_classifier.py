def rule_based_triage(message):
    """Simple keyword-based classifier for comparison."""
    message_lower = message.lower()
    result = {
        "issue_category": "unknown",
        "urgency": "LOW",
        "sentiment": "NEUTRAL",
        "followup_required": False,
        "recommended_team": "General",
        "brief_summary": message[:100],
        "method": "rule_based"
    }
    
    # Category rules
    if any(w in message_lower for w in ["water", "leak", "flood", "damp"]):
        result["issue_category"] = "water_leak"
        result["recommended_team"] = "Facilities"
    elif any(w in message_lower for w in ["energy", "electricity", "aircon", "light", "power", "overnight"]):
        result["issue_category"] = "energy_waste"
        result["recommended_team"] = "Facilities"
    elif any(w in message_lower for w in ["recycling", "waste", "bin", "contamination", "trash"]):
        result["issue_category"] = "waste_contamination"
        result["recommended_team"] = "Facilities"
    elif any(w in message_lower for w in ["access", "ramp", "entrance", "blocked", "wheelchair"]):
        result["issue_category"] = "accessibility_barrier"
        result["recommended_team"] = "Accessibility_Services"
    elif any(w in message_lower for w in ["supplier", "vendor", "procurement"]):
        result["issue_category"] = "supplier_compliance"
        result["recommended_team"] = "Procurement"
    
    # Urgency rules
    if any(w in message_lower for w in ["critical", "emergency", "hazardous", "unsafe", "fire"]):
        result["urgency"] = "CRITICAL"
        result["followup_required"] = True
    elif any(w in message_lower for w in ["all morning", "all day", "running", "overnight", "two days", "again", "no one"]):
        result["urgency"] = "HIGH"
        result["followup_required"] = True
    elif any(w in message_lower for w in ["broken", "not working", "problem"]):
        result["urgency"] = "MEDIUM"
    
    # Sentiment
    if any(w in message_lower for w in ["frustrated", "again", "no one", "complaint", "seems to be"]):
        result["sentiment"] = "NEGATIVE"
    elif any(w in message_lower for w in ["want to report", "there is"]):
        result["sentiment"] = "REPORTING"
    
    return result

# Test
test_messages = [
    "There is a water leak in Building C that has been running all morning.",
    "The recycling bins are contaminated again and no one seems to be checking them.",
    "The air conditioning is running overnight in an empty office.",
    "I want to report that one of our suppliers may not meet our sustainability policy.",
    "The accessible entrance near the main building has been blocked for two days."
]

print("RULE-BASED BASELINE RESULTS:\n")
for msg in test_messages:
    result = rule_based_triage(msg)
    print(f"Message: {msg}")
    print(f"Result: {result}")
    print("-" * 60)
