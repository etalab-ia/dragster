"""
Manual test script for Dragster skills.
Run this to test skills with an existing agent.

Usage:
    export LETTA_API_KEY=your_key
    export AGENT_ID=your_test_agent_id
    uv run python tests/test_skills_manual.py
"""
import os
import sys
from letta_client import Letta

# Test scenarios
TEST_SCENARIOS = [
    {
        "name": "liteparse - PDF parsing",
        "input": "I have a PDF file at ./tests/fixtures/sample.pdf. Can you help me parse it?",
        "expected_keywords": ["lit", "parse", "pdf", "markdown"],
    },
    {
        "name": "setup-knowledge-base - indexing",
        "input": "I want to create a searchable knowledge base from my markdown documents in ./docs",
        "expected_keywords": ["qmd", "collection", "index", "embed"],
    },
    {
        "name": "search-knowledge-base - querying",
        "input": "Search my knowledge base for information about authentication",
        "expected_keywords": ["qmd", "query", "search", "results"],
    },
]


def run_test(client: Letta, agent_id: str, scenario: dict) -> dict:
    """Run a single test scenario."""
    print(f"\n📋 Testing: {scenario['name']}")
    print(f"   Input: {scenario['input']}")
    
    # Send message to agent
    response = client.agents.messages.create(
        agent_id=agent_id,
        messages=[{"role": "user", "content": scenario["input"]}],
    )
    
    # Extract assistant response
    assistant_message = ""
    for msg in response.messages:
        if hasattr(msg, "content") and msg.content:
            assistant_message += msg.content
    
    # Check for expected keywords
    found_keywords = []
    missing_keywords = []
    for keyword in scenario["expected_keywords"]:
        if keyword.lower() in assistant_message.lower():
            found_keywords.append(keyword)
        else:
            missing_keywords.append(keyword)
    
    passed = len(found_keywords) >= len(scenario["expected_keywords"]) // 2
    
    print(f"   Found keywords: {found_keywords}")
    if missing_keywords:
        print(f"   Missing keywords: {missing_keywords}")
    print(f"   Result: {'✅ PASS' if passed else '❌ FAIL'}")
    
    return {
        "name": scenario["name"],
        "passed": passed,
        "found_keywords": found_keywords,
        "missing_keywords": missing_keywords,
        "response_preview": assistant_message[:200] + "..." if len(assistant_message) > 200 else assistant_message,
    }


def main():
    api_key = os.getenv("LETTA_API_KEY")
    agent_id = os.getenv("AGENT_ID")
    
    if not api_key:
        print("❌ LETTA_API_KEY environment variable not set")
        sys.exit(1)
    
    if not agent_id:
        print("❌ AGENT_ID environment variable not set")
        print("   Create a test agent at https://app.letta.com and set AGENT_ID")
        sys.exit(1)
    
    client = Letta(api_key=api_key)
    
    print(f"🧪 Testing agent: {agent_id}")
    print("\n" + "=" * 60)
    
    results = []
    
    for scenario in TEST_SCENARIOS:
        result = run_test(client, agent_id, scenario)
        results.append(result)
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    
    passed = sum(1 for r in results if r["passed"])
    total = len(results)
    
    for r in results:
        status = "✅" if r["passed"] else "❌"
        print(f"{status} {r['name']}")
    
    print(f"\nTotal: {passed}/{total} passed ({passed/total*100:.0f}%)")
    
    # Exit with proper code
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
