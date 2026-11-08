"""The Pydantic AI ReAct loop (LLM ⇄ tools): factory builds the Agent, loop drives it.

:mod:`nail.agent.loop` drives ``agent.iter()`` as the harness ``TurnHandler``, streaming
model nodes into the canonical :mod:`nail.entities.events` (ADR-0002 §1-2).
"""
