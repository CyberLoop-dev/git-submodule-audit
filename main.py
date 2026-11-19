import argparse
import configparser
import json
import re
from pathlib import Path

def audit(root):
    root = Path(root)
    config = root / ".gitmodules"
    if not config.exists():
        return [{"issue": "missing-gitmodules", "message": "No .gitmodules file found."}]
    parser = configparser.ConfigParser(interpolation=None, strict=False)
    try:
        parser.read(config, encoding="utf-8")
    except configparser.Error as exc:
        return [{"issue": "invalid-gitmodules", "message": str(exc)}]
    findings = []
    for section in parser.sections():
        if not section.lower().startswith("submodule "):
            continue
        path_value = parser.get(section, "path", fallback="").strip()
        url = parser.get(section, "url", fallback="").strip()
        if not path_value:
            findings.append({"name": section, "issue": "missing-path", "message": "Submodule has no path."})
            continue
        target = (root / path_value).resolve()
        if root.resolve() not in target.parents and target != root.resolve():
            findings.append({"name": section, "path": path_value, "issue": "path-outside-root", "message": "Configured path escapes the repository."})
            continue
        if not target.exists():
            issue = "missing-working-tree"
        elif not ((target / ".git").exists()):
            issue = "uninitialized"
        else:
            issue = None
        if issue:
            findings.append({"name": section, "path": path_value, "issue": issue, "message": "Submodule working tree is not initialized."})
        if url.startswith("file://") or Path(url).is_absolute() or re.match(r"^[A-Za-z]:[\\/]", url):
            findings.append({"name": section, "path": path_value, "issue": "local-only-url", "message": "Submodule URL appears to be machine-specific."})
        if not url:
            findings.append({"name": section, "path": path_value, "issue": "missing-url", "message": "Submodule has no URL."})
    return findings

def main():
    parser = argparse.ArgumentParser(description="Audit .gitmodules without changing the repository.")
    parser.add_argument("path", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    findings = audit(args.path)
    if args.json:
        print(json.dumps(findings, indent=2))
    else:
        for item in findings:
            print(f"{item.get('path', item.get('name','repository'))}: {item['issue']} — {item['message']}")
        print(f"\n{len(findings)} finding(s).")

if __name__ == "__main__":
    main()
