"""Unit tests for edge_redirection_engine handler node 013."""
import pytest
from backend.services.edge_redirection_engine.service_handler_013 import ServiceHandlerNode013, ServicePayload013

def test_node_health_invariants_013():
    node = ServiceHandlerNode013()
    assert node.verify_health_invariants() is True

def test_node_payload_init_013():
    p = ServicePayload013()
    assert p.service == "edge_redirection_engine"

def test_node_transaction_execution_013():
    node = ServiceHandlerNode013()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

