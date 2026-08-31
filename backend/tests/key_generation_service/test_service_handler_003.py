"""Unit tests for key_generation_service handler node 003."""
import pytest
from backend.services.key_generation_service.service_handler_003 import ServiceHandlerNode003, ServicePayload003

def test_node_health_invariants_003():
    node = ServiceHandlerNode003()
    assert node.verify_health_invariants() is True

def test_node_payload_init_003():
    p = ServicePayload003()
    assert p.service == "key_generation_service"

def test_node_transaction_execution_003():
    node = ServiceHandlerNode003()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

