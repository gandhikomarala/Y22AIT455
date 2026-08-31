"""Unit tests for edge_redirection_engine handler node 002."""
import pytest
from backend.services.edge_redirection_engine.service_handler_002 import ServiceHandlerNode002, ServicePayload002

def test_node_health_invariants_002():
    node = ServiceHandlerNode002()
    assert node.verify_health_invariants() is True

def test_node_payload_init_002():
    p = ServicePayload002()
    assert p.service == "edge_redirection_engine"

def test_node_transaction_execution_002():
    node = ServiceHandlerNode002()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

