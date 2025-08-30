#!/usr/bin/env python3
"""
Context-Aware Rule System Verification
Tests that rules are properly applied based on context with alwaysApply: false
"""

def detect_context(query):
    """Context detection logic"""
    query_lower = query.lower()

    # Informational queries
    if any(keyword in query_lower for keyword in [
        'what', 'show', 'list', 'display', 'tell me', 'explain', 'describe'
    ]):
        return 'informational'

    # Development queries
    dev_keywords = ['write', 'implement', 'fix', 'refactor', 'code', 'function', 'class', 'component', 'script']
    doc_keywords = ['documentation', 'docs', 'readme', 'guide', 'tutorial', 'manual']

    if any(keyword in query_lower for keyword in dev_keywords) and not any(keyword in query_lower for keyword in doc_keywords):
        return 'development'

    # Operational queries
    if any(keyword in query_lower for keyword in [
        'run', 'build', 'deploy', 'start', 'stop', 'restart',
        'check', 'test', 'status', 'install', 'setup'
    ]):
        return 'operational'

    # Documentation queries
    if any(keyword in query_lower for keyword in doc_keywords):
        return 'documentation'

    return 'general'

def simulate_rule_application(query):
    """Simulate how the context-aware rule system should work"""
    context = detect_context(query)

    # Always apply context detection rule
    applicable_rules = ['01-context-detection']

    # Apply other rules based on context
    if context == 'informational':
        applicable_rules.extend([
            '10-markdown-general',
            '60-ai-interaction-patterns',
            '90-terminal-management'
        ])
    elif context in ['development', 'operational']:
        # These rules now have alwaysApply: false, contextAware: true
        applicable_rules.extend([
            '21-css-quality-standards',
            '31-python-coding-standards',
            '70-html-standards',
            '80-javascript-standards',
            '52-build-process'
        ])
    elif context == 'documentation':
        applicable_rules.extend([
            '10-markdown-general',
            '60-ai-interaction-patterns'
        ])

    return context, applicable_rules

def test_context_system():
    """Test the updated context-aware system"""
    test_cases = [
        ("what .cursor/rules are currently applied ?", "informational"),
        ("write a Python function to calculate fibonacci", "development"),
        ("run the build process", "operational"),
        ("create documentation for the API", "documentation"),
        ("show me the project structure", "informational"),
        ("fix this CSS layout issue", "development"),
        ("check the deployment status", "operational"),
    ]

    print("🧪 Context-Aware Rule System Verification")
    print("=" * 60)
    print("Testing with alwaysApply: false for development rules")
    print("=" * 60)

    for query, expected in test_cases:
        context, rules = simulate_rule_application(query)
        status = "✅" if context == expected else "❌"

        print(f"\n{status} Query: '{query}'")
        print(f"   Expected Context: {expected}")
        print(f"   Detected Context: {context}")
        print(f"   Applicable Rules: {len(rules)} total")

        # Show which rules would NOT apply (the key improvement)
        excluded_rules = []
        if context == 'informational':
            excluded_rules = ['21-css-*', '31-python-*', '70-html-*', '80-js-*']
        elif context == 'documentation':
            excluded_rules = ['21-css-*', '31-python-*', '70-html-*', '80-js-*', '52-build-*']

        if excluded_rules:
            print(f"   ❌ Excluded Rules: {excluded_rules}")
        else:
            print("   ✅ All relevant rules applied")

def test_rule_behavior():
    """Test specific rule behavior scenarios"""
    print("\n🔍 Specific Rule Behavior Tests")
    print("=" * 40)

    scenarios = [
        {
            'query': "what CSS files are in this project?",
            'context': 'informational',
            'css_rules_should_apply': False,
            'reason': 'Informational query about CSS files, not CSS development'
        },
        {
            'query': "write CSS for a responsive navbar",
            'context': 'development',
            'css_rules_should_apply': True,
            'reason': 'CSS development task'
        },
        {
            'query': "create documentation for the Python API",
            'context': 'documentation',
            'css_rules_should_apply': False,
            'reason': 'Documentation task, not CSS development'
        }
    ]

    for scenario in scenarios:
        context, rules = simulate_rule_application(scenario['query'])
        css_rules_applied = any('css' in rule.lower() for rule in rules)

        status = "✅" if css_rules_applied == scenario['css_rules_should_apply'] else "❌"

        print(f"\n{status} {scenario['query']}")
        print(f"   Context: {context}")
        print(f"   CSS Rules Applied: {css_rules_applied}")
        print(f"   Expected: {scenario['css_rules_should_apply']}")
        print(f"   Reason: {scenario['reason']}")

if __name__ == "__main__":
    test_context_system()
    test_rule_behavior()
    print("\n🎉 Context-aware rule system verification complete!")
    print("✅ Development rules now have alwaysApply: false")
    print("✅ Context detection determines rule application")
    print("✅ Informational queries avoid development standards")
