from __future__ import annotations
import json, re, subprocess, sys, tempfile
from pathlib import Path

EXCLUDE_RE = re.compile(r"(^|/)(\.git|node_modules|\.next|\.venv|venv|dist|build)(/|$)|(^|/)(package-lock\.json|pnpm-lock\.yaml|yarn\.lock)$|\.(svg|png|jpe?g|gif|webp|ico|pdf|zip)$", re.I)
SENSITIVE_PATH_RE = re.compile(r"(^|/)(\.env($|\.)|.*\.session($|\.)|id_rsa($|\.)|id_ed25519($|\.)|credentials?($|\.)|secrets?($|\.))|\.(pem|p12|pfx|key)$", re.I)

def run(*args: str) -> str:
    return subprocess.run(args, check=True, text=True, capture_output=True).stdout

def detect(path: str | None = None, *, all_files: bool = False) -> dict:
    cmd = ["detect-secrets", "scan"]
    if all_files:
        cmd += ["--all-files", "--exclude-files", EXCLUDE_RE.pattern]
    elif path:
        cmd.append(path)
    return json.loads(subprocess.run(cmd, check=True, text=True, capture_output=True).stdout)

def findings(data: dict):
    return [(f, item) for f, items in data.get("results", {}).items() for item in items]

def main() -> int:
    problems = [f"árvore atual: {f}:{item.get('line_number', '?')} — {item.get('type', 'possível segredo')}" for f, item in findings(detect(all_files=True))]
    for raw in sorted(set(run("git", "log", "--all", "--format=", "--name-only").splitlines())):
        path = raw.strip()
        if path and not path.endswith(".env.example") and SENSITIVE_PATH_RE.search(path):
            problems.append(f"histórico: nome de arquivo sensível alcançável: {path}")
    patch = run("git", "log", "--all", "-p", "--no-color", "--format=")
    current = ""; lines = []
    for line in patch.splitlines():
        if line.startswith("diff --git a/"):
            m = re.match(r"diff --git a/(.*?) b/(.*)", line); current = m.group(2) if m else ""; continue
        if not current or EXCLUDE_RE.search(current) or line.startswith(("+++", "---")): continue
        if line.startswith(("+", "-")):
            value = line[1:]
            if not re.fullmatch(r"\s*[0-9a-f]{40,64}\s*", value, re.I): lines.append(value)
    if lines:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".txt") as h:
            h.write("\n".join(lines)); tmp = h.name
        try: hist = findings(detect(tmp))
        finally: Path(tmp).unlink(missing_ok=True)
        problems += [f"histórico: possível segredo em conteúdo alcançável — {item.get('type', 'detector desconhecido')}" for _, item in hist]
    if problems:
        print("Falha na auditoria dedicada de segredos:\n" + "\n".join(f"- {p}" for p in problems)); return 1
    print("detect-secrets: árvore atual e histórico alcançável sem achados pelos detectores habilitados."); return 0

if __name__ == "__main__": sys.exit(main())
