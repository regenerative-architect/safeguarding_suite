# Safeguarding Next-Gen OS

A dependency-light HTML/PWA workbench designed around a prevention objective: make harmful behavior harder to perform, easier to detect, less rewarding, and less transmissible across generations—while preserving privacy, due process, human agency, repair, and legitimate dissent.

## Run

- **Fastest:** open `index.html`. Core reading, calculators, planners, search, stories, JSON export/import and most local tools work without a server.
- **Full PWA:** serve the folder over HTTPS or localhost. Example: `python -m http.server 8080`, then open `http://localhost:8080/`.
- Service workers do **not** run from `file://`; the UI reports this honestly.

## Architecture

- Vanilla HTML/CSS/JS; no required framework or account.
- Route registry drives top navigation, side navigation and breadcrumbs.
- IndexedDB stores workspace records; localStorage stores small UI preferences.
- JSON export/import provides data portability.
- Service worker precaches the app shell for offline use when hosted.
- BroadcastChannel provides same-origin multi-tab collaboration.
- Optional internet peer-room adapter is user-triggered and degrades safely if unavailable.
- Deterministic planning is the default; no AI is needed for core decisions.
- Diagnostics report browser capabilities rather than assuming they exist.

## Safety architecture

This is a systems-design and educational tool, not a person-risk classifier, guilt detector, medical diagnostic, policing system, or substitute for professional safeguarding procedures. Early-signal tools intentionally aggregate categories and counts rather than names. Scores are planning heuristics, not empirical predictions.

## Main modules

1. Harm Friction OS
2. Intergenerational Safeguarding Dashboard
3. Integrity-by-Design Toolkit
4. Early Signal Commons
5. Exploitability Surface Mapper
6. Reward Reversal Engine
7. Narrative Immunity OS
8. Restorative Accountability Ledger
9. Safeguarding Simulation Lab
10. Protective Ecosystem Command Center
11. Story Lab (10 narrative concepts)
12. Deterministic Safeguarding Planner
13. Evidence & Provenance Ledger
14. Collaboration Room
15. Prompt Foundry
16. Diagnostics & Capability Lab
17. Simplified Advanced Guides

## Deployment notes

For GitHub Pages, upload the bundle contents to the repository root or `/docs`, enable Pages, and open the HTTPS site once online so the service worker can populate its cache. If you modify files, bump the cache version in `sw.js` before deployment.

## Attribution & licenses

Architecture and feature concepts were adapted from the user-provided **Feature Fusion Foundry** and the Safeguarding Next-Gen conversation. No proprietary third-party source code was copied. Code in this bundle is provided under the MIT License in `LICENSE`.

Credit: Foster + Navi / Planetary Restoration Archive.
