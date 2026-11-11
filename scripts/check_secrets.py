#!/usr/bin/env python3
"""Fail (exit 1) if anything that looks like a secret is found in the repo.
Usage:  python scripts/check_secrets.py          (scans the whole repo)
Hook:   cp scripts/check_secrets.py .git/hooks/pre-commit-check.py && echo 'python .git/hooks/pre-commit-check.py' >> .git/hooks/pre-commit
"""
import re, sys, pathlib

PATTERNS = {
    "Google/Gemini API key":      r"AIza[0-9A-Za-z_\-]{30,}|AQ\.[0-9A-Za-z_\-]{30,}",
    "JWT (Qdrant / Supabase...)": r"eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}",
    "key= in URL":                r"[?&](key|api_key|apikey|token)=[^&\"'\s{]{12,}",
    "Bearer token":               r"Bearer\s+(?!<|YOUR)[A-Za-z0-9_\-\.]{20,}",
    "api-key header value":       r"\"name\":\s*\"(api-key|x-goog-api-key|Authorization)\",\s*\"value\":\s*\"(?!\s*\")[^\"]{12,}\"",
    "Qdrant cloud host":          r"(?<!YOUR-CLUSTER-ID)\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\.[a-z0-9\-]+\.aws\.cloud\.qdrant\.io",
    "Google Sheet / Drive ID":    r"/d/1[A-Za-z0-9_\-]{43}",
    "Windows user path":          r"C:\\\\+Users\\\\+[^\\\"]+",
}
SKIP = {".git", "node_modules"}
bad = 0
for p in pathlib.Path(".").rglob("*"):
    if not p.is_file() or any(s in p.parts for s in SKIP) or p.name == "check_secrets.py":
        continue
    try:
        text = p.read_text(encoding="utf-8")
    except Exception:
        continue
    for label, rx in PATTERNS.items():
        for m in re.finditer(rx, text):
            bad += 1
            print(f"{p}: {label}: {m.group(0)[:18]}...")
print("OK - no secrets found" if not bad else f"\n{bad} possible secret(s) found - do NOT commit.")
sys.exit(1 if bad else 0)
