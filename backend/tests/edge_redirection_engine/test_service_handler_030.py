"""Unit tests for edge_redirection_engine handler node 030."""
import pytest
from backend.services.edge_redirection_engine.service_handler_030 import ServiceHandlerNode030, ServicePayload030

def test_node_health_invariants_030():
    node = ServiceHandlerNode030()
    assert node.verify_health_invariants() is True

def test_node_payload_init_030():
    p = ServicePayload030()
    assert p.service == "edge_redirection_engine"

def test_node_transaction_execution_030():
    node = ServiceHandlerNode030()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

