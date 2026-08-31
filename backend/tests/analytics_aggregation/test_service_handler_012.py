"""Unit tests for analytics_aggregation handler node 012."""
import pytest
from backend.services.analytics_aggregation.service_handler_012 import ServiceHandlerNode012, ServicePayload012

def test_node_health_invariants_012():
    node = ServiceHandlerNode012()
    assert node.verify_health_invariants() is True

def test_node_payload_init_012():
    p = ServicePayload012()
    assert p.service == "analytics_aggregation"

def test_node_transaction_execution_012():
    node = ServiceHandlerNode012()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

