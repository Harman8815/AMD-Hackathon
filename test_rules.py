import json

def search_rules(query, rules_file="rules.json"):
    with open(rules_file, "r") as f:
        rules = json.load(f)
    
    query = query.lower()
    matches = []
    for rule in rules:
        if query in rule["parameter"].lower() or query in rule["rule_text"].lower():
            matches.append(rule)
    return matches

# Test
print(search_rules("rib"))
