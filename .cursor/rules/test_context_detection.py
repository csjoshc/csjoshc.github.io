#!/usr/bin/env python3
"""
Context Detection Test Script
Tests the new context-aware rule application system
"""

def detect_context(query):
    """Simple context detection implementation"""
    query_lower = query.lower()

    # Informational queries
    if any(keyword in query_lower for keyword in [
        'what', 'show', 'list', 'display', 'tell me', 'explain', 'describe'
    ]):
        return 'informational'

    # Development queries (but not documentation)
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
    if any(keyword in query_lower for keyword in [
        'document', 'readme', 'guide', 'tutorial', 'manual',
        'explain', 'describe', 'overview', 'summary'
    ]):
        return 'documentation'

    return 'general'

def get_applicable_rules(context):
    """Return rules that should apply for the given context"""
    base_rules = ['01-context-detection']

    if context == 'informational':
        return base_rules + ['10-markdown-general', '60-ai-interaction-patterns', '90-terminal-management']
    elif context == 'development':
        return base_rules + ['all development rules for relevant technologies']
    elif context == 'operational':
        return base_rules + ['52-build-process', '60-ai-interaction-patterns', '90-terminal-management']
    elif context == 'documentation':
        return base_rules + ['10-markdown-general', '60-ai-interaction-patterns']
    else:
        return base_rules + ['relevant contextual rules']

def test_context_detection():
    """Test the context detection system"""
    test_cases = [
        ("what .cursor/rules are currently applied ?", "informational"),
        ("write a Python function to calculate fibonacci", "development"),
        ("run the build process", "operational"),
        ("create documentation for the API", "documentation"),
        ("show me the project structure", "informational"),
        ("fix this CSS layout issue", "development"),
        ("check the deployment status", "operational"),
    ]

    print("🧪 Context Detection Test Results")
    print("=" * 50)

    for query, expected in test_cases:
        detected = detect_context(query)
        status = "✅" if detected == expected else "❌"
        applicable = get_applicable_rules(detected)

        print(f"{status} Query: '{query}'")
        print(f"   Expected: {expected}")
        print(f"   Detected: {detected}")
        print(f"   Rules: {applicable}")
        print()

if __name__ == "__main__":
    test_context_detection()
