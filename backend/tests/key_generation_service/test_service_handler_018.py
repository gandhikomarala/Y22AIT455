"""Unit tests for key_generation_service handler node 018."""
import pytest
from backend.services.key_generation_service.service_handler_018 import ServiceHandlerNode018, ServicePayload018

def test_node_health_invariants_018():
    node = ServiceHandlerNode018()
    assert node.verify_health_invariants() is True

def test_node_payload_init_018():
    p = ServicePayload018()
    assert p.service == "key_generation_service"

def test_node_transaction_execution_018():
    node = ServiceHandlerNode018()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

