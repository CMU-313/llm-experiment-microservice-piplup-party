from app import app
import pytest


def test_home_route():
    client = app.test_client()
    r = client.get("/translate?content=hola")
    d = r.get_json()
    assert r.status_code == 200
    assert "is_english" in d and "translated_content" in d


def test_empty_input():
    c = app.test_client()
    d = c.get("/translate?content=").get_json()
    assert d["is_english"] is True


def test_mock_error(monkeypatch):
    import src.translator
    def broken(_): raise Exception("mock fail")
    monkeypatch.setattr(src.translator, "translate_content", broken)
    client = app.test_client()
    res = client.get("/translate?content=hola")
    assert res.status_code == 200

