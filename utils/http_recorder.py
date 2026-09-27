"""Her testde gonderilen sorgulari ve alinan cavablari yadda saxlayir.

BaseClient her cavabi bura yazir, conftest.py ise test bitende
bunlari report-a elave edir.
"""
import json
from urllib.parse import urlparse

import allure

_responses = []


def record(response, *args, **kwargs):
    _responses.append(response)
    _attach_to_allure(response)


def _attach_to_allure(response):
    """Allure report-da her sorgu ayrica addim (step) kimi gorunur."""
    req = response.request
    title = f"{req.method} {urlparse(req.url).path} -> {response.status_code}"
    with allure.step(title):
        allure.attach(req.url, name="URL", attachment_type=allure.attachment_type.TEXT)
        if req.body:
            allure.attach(_pretty(req.body, limit=None), name="Request body",
                          attachment_type=allure.attachment_type.JSON)
        allure.attach(_pretty(response.text, limit=None), name="Response body",
                      attachment_type=allure.attachment_type.JSON)


def reset():
    _responses.clear()


def endpoints() -> str:
    """Testin cagirdigi endpoint-ler, meselen: 'POST /api/cards/status'"""
    seen = []
    for r in _responses:
        name = f"{r.request.method} {urlparse(r.request.url).path}"
        if name not in seen:
            seen.append(name)
    return ", ".join(seen)


def as_text() -> str:
    return "\n\n".join(_format(r) for r in _responses)


def _format(response) -> str:
    req = response.request
    ms = int(response.elapsed.total_seconds() * 1000)
    return (
        f">>> {req.method} {req.url}\n"
        f"Request body:\n{_pretty(req.body)}\n"
        f"<<< {response.status_code} ({ms} ms)\n"
        f"Response body:\n{_pretty(response.text)}"
    )


def _pretty(body, limit=3000) -> str:
    if not body:
        return "(bos)"
    if isinstance(body, bytes):
        body = body.decode("utf-8", errors="replace")
    try:
        text = json.dumps(json.loads(body), indent=2, ensure_ascii=False)
    except ValueError:
        text = str(body)
    if limit and len(text) > limit:
        text = text[:limit] + f"\n... ({len(text) - limit} simvol kesildi)"
    return text
