"""Unit tests for rate_limiter_governance handler node 015."""
import pytest
from backend.services.rate_limiter_governance.service_handler_015 import ServiceHandlerNode015, ServicePayload015

def test_node_health_invariants_015():
    node = ServiceHandlerNode015()
    assert node.verify_health_invariants() is True

def test_node_payload_init_015():
    p = ServicePayload015()
    assert p.service == "rate_limiter_governance"

def test_node_transaction_execution_015():
    node = ServiceHandlerNode015()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

