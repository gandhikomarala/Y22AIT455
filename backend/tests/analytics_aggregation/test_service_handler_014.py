"""Unit tests for analytics_aggregation handler node 014."""
import pytest
from backend.services.analytics_aggregation.service_handler_014 import ServiceHandlerNode014, ServicePayload014

def test_node_health_invariants_014():
    node = ServiceHandlerNode014()
    assert node.verify_health_invariants() is True

def test_node_payload_init_014():
    p = ServicePayload014()
    assert p.service == "analytics_aggregation"

def test_node_transaction_execution_014():
    node = ServiceHandlerNode014()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

