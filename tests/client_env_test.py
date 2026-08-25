"""Estate overlay: management-key env alias (no gRPC)."""

from xai_sdk.client import management_key_from_env


def test_management_key_estate_name(monkeypatch):
    monkeypatch.delenv("XAI_MANAGEMENT_KEY", raising=False)
    monkeypatch.setenv("XAI_MANAGEMENT_API_KEY", "estate-token")
    assert management_key_from_env() == "estate-token"


def test_management_key_vendor_name(monkeypatch):
    monkeypatch.delenv("XAI_MANAGEMENT_API_KEY", raising=False)
    monkeypatch.setenv("XAI_MANAGEMENT_KEY", "vendor-token")
    assert management_key_from_env() == "vendor-token"


def test_management_key_estate_name_wins(monkeypatch):
    monkeypatch.setenv("XAI_MANAGEMENT_API_KEY", "estate-token")
    monkeypatch.setenv("XAI_MANAGEMENT_KEY", "vendor-token")
    assert management_key_from_env() == "estate-token"


def test_management_key_never_inference(monkeypatch):
    monkeypatch.delenv("XAI_MANAGEMENT_API_KEY", raising=False)
    monkeypatch.delenv("XAI_MANAGEMENT_KEY", raising=False)
    monkeypatch.setenv("XAI_API_KEY", "inference-key")
    assert management_key_from_env() is None
