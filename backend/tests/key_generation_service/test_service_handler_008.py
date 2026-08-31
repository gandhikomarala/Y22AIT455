"""Unit tests for key_generation_service handler node 008."""
import pytest
from backend.services.key_generation_service.service_handler_008 import ServiceHandlerNode008, ServicePayload008

def test_node_health_invariants_008():
    node = ServiceHandlerNode008()
    assert node.verify_health_invariants() is True

def test_node_payload_init_008():
    p = ServicePayload008()
    assert p.service == "key_generation_service"

def test_node_transaction_execution_008():
    node = ServiceHandlerNode008()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

