"""Unit tests for edge_redirection_engine handler node 027."""
import pytest
from backend.services.edge_redirection_engine.service_handler_027 import ServiceHandlerNode027, ServicePayload027

def test_node_health_invariants_027():
    node = ServiceHandlerNode027()
    assert node.verify_health_invariants() is True

def test_node_payload_init_027():
    p = ServicePayload027()
    assert p.service == "edge_redirection_engine"

def test_node_transaction_execution_027():
    node = ServiceHandlerNode027()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

