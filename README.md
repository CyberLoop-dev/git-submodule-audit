<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:0f766e&height=170&section=header&text=Git%20Submodule%20Audit&fontColor=ffffff&fontSize=34" alt="Git Submodule Audit banner"/></p>
<p align="center"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=19&duration=2800&pause=900&center=true&vCenter=true&width=620&lines=Audit%20Git%20submodule%20state%3BFind%20missing%20working%20trees%3BRead-only%20repository%20checks" alt="Typing title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/git-submodule-audit?style=flat-square" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/git-submodule-audit?style=flat-square" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/git-submodule-audit?style=flat-square" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/git-submodule-audit?style=flat-square" alt="Last commit"/></p>
<p align="center"><img src="assets/mark.svg" width="520" alt="Git Submodule Audit illustration"/></p>

## 🧭 Overview
Git Submodule Audit reads `.gitmodules` and compares each configured path with the working tree. It flags missing paths, uninitialized directories, and local-only URLs that may not work for collaborators.

## ✨ Features
- 🧩 Read submodule names, paths, and URLs from `.gitmodules`
- 📂 Detect missing paths and uninitialized submodule directories
- ⚠️ Flag file URLs and absolute local paths
- 🔒 Never runs `git submodule update` or modifies the repository

## 🖥️ Demo
No hosted demo is provided. Run the tool locally using the quick-start command.

## 🚀 Quick Start
Requires Python 3.10 or newer.

```bash
python main.py ./
```

Run the test suite with:

```bash
python -m unittest discover -s tests -v
```

## 🧰 Tech Stack
- Python standard library
- `argparse` CLI and `unittest`
- Read-only inspection by default

## 🗂️ Folder Structure
```text
.
├── .github/workflows/ci.yml
├── assets/mark.svg
├── tests/test_main.py
├── main.py
├── pyproject.toml
└── README.md
```

## 🗺️ Roadmap
- [ ] Add more edge-case fixtures
- [ ] Improve machine-readable output
- [ ] Keep the core workflow dependency-free

## 🤝 Contributing
Issues and focused pull requests are welcome. Add regression tests for parser and reporting changes.

## 📄 License
MIT License. See [LICENSE](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:0f172a&height=100&section=footer" alt="Animated wave footer"/></p>
