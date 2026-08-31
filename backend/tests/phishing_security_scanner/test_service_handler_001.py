"""Unit tests for phishing_security_scanner handler node 001."""
import pytest
from backend.services.phishing_security_scanner.service_handler_001 import ServiceHandlerNode001, ServicePayload001

def test_node_health_invariants_001():
    node = ServiceHandlerNode001()
    assert node.verify_health_invariants() is True

def test_node_payload_init_001():
    p = ServicePayload001()
    assert p.service == "phishing_security_scanner"

def test_node_transaction_execution_001():
    node = ServiceHandlerNode001()
    success, token = node.process_transaction_stage_01({"target_url": "https://example.com/blog/article-123"})
    assert success is True
    assert token.startswith("short.ly/")

