"""The Agents Catalog: built-in personas as bundled Markdown + a loader (ADR-0003 §5).

Each built-in agent (Build / Plan / Explore / Code-Reviewer) is a frontmatter+body Markdown file
under :mod:`nail.agents.builtin`, loaded as packaged data and validated into an
:class:`~nail.entities.agent_def.AgentDef`; :func:`~nail.agents.select.select_agent` wires a
persona into the running session. Primaries are selectable as the main agent; Explore is
subagent-only, spawned via the ``agent`` tool (ADR-0013).
"""

from __future__ import annotations

from nail.agents.loader import load_agent, load_builtin_agents
from nail.agents.select import select_agent

__all__ = ["load_agent", "load_builtin_agents", "select_agent"]
