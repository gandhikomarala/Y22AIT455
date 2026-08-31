"""Unit tests for analytics_aggregation handler node 007."""
import pytest
from backend.services.analytics_aggregation.service_handler_007 import ServiceHandlerNode007, ServicePayload007

def test_node_health_invariants_007():
    node = ServiceHandlerNode007()
    assert node.verify_health_invariants() is True

def test_node_payload_init_007():
    p = ServicePayload007()
    assert p.service == "analytics_aggregation"

def test_node_transaction_execution_007():
    node = ServiceHandlerNode007()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

