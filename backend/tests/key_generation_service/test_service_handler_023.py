"""Unit tests for key_generation_service handler node 023."""
import pytest
from backend.services.key_generation_service.service_handler_023 import ServiceHandlerNode023, ServicePayload023

def test_node_health_invariants_023():
    node = ServiceHandlerNode023()
    assert node.verify_health_invariants() is True

def test_node_payload_init_023():
    p = ServicePayload023()
    assert p.service == "key_generation_service"

def test_node_transaction_execution_023():
    node = ServiceHandlerNode023()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

