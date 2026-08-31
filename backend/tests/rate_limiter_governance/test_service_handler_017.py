"""Unit tests for rate_limiter_governance handler node 017."""
import pytest
from backend.services.rate_limiter_governance.service_handler_017 import ServiceHandlerNode017, ServicePayload017

def test_node_health_invariants_017():
    node = ServiceHandlerNode017()
    assert node.verify_health_invariants() is True

def test_node_payload_init_017():
    p = ServicePayload017()
    assert p.service == "rate_limiter_governance"

def test_node_transaction_execution_017():
    node = ServiceHandlerNode017()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

