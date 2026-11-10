"""Minimal service for OCI deployment verification."""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Interaction Tree", docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f6f5f0">
<title>Interaction Tree · 준비 중</title>
<style>
* { box-sizing: border-box; }
body { margin: 0; min-height: 100vh; min-height: 100svh; background: #f6f5f0;
  color: #243b30; font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif; }
main { min-height: 100vh; min-height: 100svh; max-width: 1120px; margin: auto;
  padding: 40px 32px; display: flex; flex-direction: column; }
.brand { font-size: 16px; font-weight: 650; letter-spacing: -.4px; }
section { margin: auto 0; padding: 80px 0; }
.symbol { width: 68px; height: 68px; margin-bottom: 38px; }
.label { font-size: 12px; letter-spacing: 2px; color: #6c7b6e; }
h1 { margin: 22px 0; font-size: clamp(38px, 7vw, 76px); line-height: 1.2; letter-spacing: -3px; font-weight: 600; }
p { margin: 0; color: #6c7b6e; font-size: 16px; line-height: 1.9; word-break: keep-all; }
footer { padding-top: 24px; border-top: 1px solid #dcded5; display: flex;
  justify-content: space-between; gap: 16px; color: #6c7b6e; font-size: 12px; }
.status { display: flex; align-items: center; gap: 8px; }
.dot { width: 6px; height: 6px; border-radius: 50%; background: #789871; }
@media (max-width: 480px) { main { padding: 28px 24px; } h1 { letter-spacing: -1.8px; } footer { flex-direction: column; } }
</style>
</head>
<body>
<main>
<header class="brand">Interaction Tree</header>
<section aria-labelledby="title">
<svg class="symbol" viewBox="0 0 68 68" fill="none" aria-hidden="true">
<path d="M34 60V34M34 44L17 27M34 37L51 20" stroke="#365c42" stroke-width="2" stroke-linecap="round"/>
<circle cx="17" cy="22" r="9" fill="#dce6d3"/>
<circle cx="51" cy="16" r="10" fill="#bed0ae"/>
<circle cx="34" cy="30" r="8" fill="#789871"/>
<path d="M23 60H45" stroke="#365c42" stroke-width="2" stroke-linecap="round"/>
</svg>
<div class="label">WORK IN PROGRESS</div>
<h1 id="title">새로운 연결을<br>준비하고 있습니다.</h1>
<p>지금은 사이트 공사 중입니다.<br>조금 더 나은 모습으로 곧 찾아뵙겠습니다.</p>
</section>
<footer><span>© Interaction Tree</span><span class="status"><span class="dot" aria-hidden="true"></span>준비 중</span></footer>
</main>
</body>
</html>"""
