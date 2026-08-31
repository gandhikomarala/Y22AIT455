"""Unit tests for analytics_aggregation handler node 005."""
import pytest
from backend.services.analytics_aggregation.service_handler_005 import ServiceHandlerNode005, ServicePayload005

def test_node_health_invariants_005():
    node = ServiceHandlerNode005()
    assert node.verify_health_invariants() is True

def test_node_payload_init_005():
    p = ServicePayload005()
    assert p.service == "analytics_aggregation"

def test_node_transaction_execution_005():
    node = ServiceHandlerNode005()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

