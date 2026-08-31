"""Unit tests for key_generation_service handler node 010."""
import pytest
from backend.services.key_generation_service.service_handler_010 import ServiceHandlerNode010, ServicePayload010

def test_node_health_invariants_010():
    node = ServiceHandlerNode010()
    assert node.verify_health_invariants() is True

def test_node_payload_init_010():
    p = ServicePayload010()
    assert p.service == "key_generation_service"

def test_node_transaction_execution_010():
    node = ServiceHandlerNode010()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

