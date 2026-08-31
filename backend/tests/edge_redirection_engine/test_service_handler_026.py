"""Unit tests for edge_redirection_engine handler node 026."""
import pytest
from backend.services.edge_redirection_engine.service_handler_026 import ServiceHandlerNode026, ServicePayload026

def test_node_health_invariants_026():
    node = ServiceHandlerNode026()
    assert node.verify_health_invariants() is True

def test_node_payload_init_026():
    p = ServicePayload026()
    assert p.service == "edge_redirection_engine"

def test_node_transaction_execution_026():
    node = ServiceHandlerNode026()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

