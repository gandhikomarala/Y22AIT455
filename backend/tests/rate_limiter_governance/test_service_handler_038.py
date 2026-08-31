"""Unit tests for rate_limiter_governance handler node 038."""
import pytest
from backend.services.rate_limiter_governance.service_handler_038 import ServiceHandlerNode038, ServicePayload038

def test_node_health_invariants_038():
    node = ServiceHandlerNode038()
    assert node.verify_health_invariants() is True

def test_node_payload_init_038():
    p = ServicePayload038()
    assert p.service == "rate_limiter_governance"

def test_node_transaction_execution_038():
    node = ServiceHandlerNode038()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

