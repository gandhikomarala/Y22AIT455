"""Unit tests for key_generation_service handler node 040."""
import pytest
from backend.services.key_generation_service.service_handler_040 import ServiceHandlerNode040, ServicePayload040

def test_node_health_invariants_040():
    node = ServiceHandlerNode040()
    assert node.verify_health_invariants() is True

def test_node_payload_init_040():
    p = ServicePayload040()
    assert p.service == "key_generation_service"

def test_node_transaction_execution_040():
    node = ServiceHandlerNode040()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

