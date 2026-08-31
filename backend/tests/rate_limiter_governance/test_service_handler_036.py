"""Unit tests for rate_limiter_governance handler node 036."""
import pytest
from backend.services.rate_limiter_governance.service_handler_036 import ServiceHandlerNode036, ServicePayload036

def test_node_health_invariants_036():
    node = ServiceHandlerNode036()
    assert node.verify_health_invariants() is True

def test_node_payload_init_036():
    p = ServicePayload036()
    assert p.service == "rate_limiter_governance"

def test_node_transaction_execution_036():
    node = ServiceHandlerNode036()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

