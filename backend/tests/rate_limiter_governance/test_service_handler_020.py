"""Unit tests for rate_limiter_governance handler node 020."""
import pytest
from backend.services.rate_limiter_governance.service_handler_020 import ServiceHandlerNode020, ServicePayload020

def test_node_health_invariants_020():
    node = ServiceHandlerNode020()
    assert node.verify_health_invariants() is True

def test_node_payload_init_020():
    p = ServicePayload020()
    assert p.service == "rate_limiter_governance"

def test_node_transaction_execution_020():
    node = ServiceHandlerNode020()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

