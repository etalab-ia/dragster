#!/usr/bin/env python
"""
Delete agents named 'letta-evals-judge-agent' from Letta Cloud.

These agents are created by letta-evals during evaluation runs.

Usage:
    export LETTA_API_KEY=your_key
    uv run python scripts/delete_judge_agents.py

Options:
    --dry-run    List agents that would be deleted without deleting
    --yes        Skip confirmation prompt
"""
import os
import sys
from letta_client import Letta


def find_judge_agents(client: Letta) -> list:
    """Find all agents named 'letta-evals-judge-agent'."""
    agents = []
    after = None

    while True:
        page = client.agents.list(name="letta-evals-judge-agent", after=after, limit=100)
        agents.extend(page)
        # Check if there's a next page
        after = getattr(page, 'after', None) or getattr(page, 'next_cursor', None)
        if not after or len(page) < 100:
            break

    return agents


def delete_agents(client: Letta, agents: list, dry_run: bool = False) -> None:
    """Delete the given agents."""
    if not agents:
        print("No agents found with name 'letta-evals-judge-agent'")
        return

    print(f"Found {len(agents)} agent(s) to delete:")
    for agent in agents:
        created = agent.created_at.strftime("%Y-%m-%d %H:%M") if agent.created_at else "unknown"
        print(f"  - {agent.id} (created: {created})")

    if dry_run:
        print("\n[DRY RUN] Would delete these agents. Run without --dry-run to delete.")
        return

    deleted = 0
    failed = 0

    for agent in agents:
        try:
            client.agents.delete(agent.id)
            print(f"  ✅ Deleted {agent.id}")
            deleted += 1
        except Exception as e:
            print(f"  ❌ Failed to delete {agent.id}: {e}")
            failed += 1

    print(f"\nDeleted {deleted} agent(s), {failed} failure(s)")


def main():
    api_key = os.getenv("LETTA_API_KEY")
    if not api_key:
        print("❌ LETTA_API_KEY environment variable not set")
        print("   Get your API key from https://app.letta.com/api-keys")
        sys.exit(1)

    # Parse args
    dry_run = "--dry-run" in sys.argv
    skip_confirm = "--yes" in sys.argv or "-y" in sys.argv

    client = Letta(api_key=api_key)

    print("🔍 Searching for agents named 'letta-evals-judge-agent'...")
    agents = find_judge_agents(client)

    if not agents:
        print("No agents found.")
        sys.exit(0)

    if dry_run:
        delete_agents(client, agents, dry_run=True)
        sys.exit(0)

    # Confirm deletion
    if not skip_confirm:
        print(f"\n⚠️  Will delete {len(agents)} agent(s)")
        response = input("Continue? [y/N] ")
        if response.lower() != "y":
            print("Aborted.")
            sys.exit(1)

    delete_agents(client, agents, dry_run=False)


if __name__ == "__main__":
    main()
