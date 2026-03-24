"""Agent factory for letta-evals letta_code target.

Returns the pre-configured agent ID from the AGENT_ID environment variable.
This ensures the eval suite uses an existing agent with skills already loaded,
rather than creating a fresh agent per sample.
"""

import os

from letta_client import AsyncLetta
from letta_evals.models import Sample


async def get_agent(client: AsyncLetta, sample: Sample) -> str:
    """Return the pre-configured agent ID from environment."""
    agent_id = os.environ.get("AGENT_ID")
    if not agent_id:
        raise ValueError(
            "AGENT_ID environment variable not set. "
            "Create a test agent at https://app.letta.com and set AGENT_ID."
        )
    return agent_id
