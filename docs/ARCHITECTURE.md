# Architecture

## Objective function

The platform organizes prevention around six system levers:

1. reduce harmful opportunity;
2. improve proportionate visibility and detection;
3. reduce harmful rewards;
4. interrupt social/intergenerational transmission;
5. strengthen accountability, repair and safe off-ramps;
6. increase protective capacity.

The UI deliberately avoids a single "bad actor" score. Every heuristic is attached to a workflow, environment, institution, narrative or scenario.

## Capability ladder

- Level 0 — static/read-only reference.
- Level 1 — local interactive planning and simulation.
- Level 2 — durable local state through IndexedDB.
- Level 3 — hosted offline readiness through a service worker.
- Level 4 — same-origin collaboration through BroadcastChannel.
- Level 5 — optional internet peer collaboration adapter.
- Level 6 — optional AI/research integrations can be added behind explicit consent and provenance boundaries.

Advanced layer failure must not break lower levels.

## State model

`workspace` contains preferences, progress, signals, restorative records, evidence records, notes, planner runs and story mappings. IndexedDB is the durable local source of truth. JSON export is the portable interchange format.

## Deterministic planner

The planner uses explicit rules rather than hidden inference:

intent -> scope -> harm pathway -> system levers -> privacy constraints -> intervention patterns -> failure modes -> measurement plan -> review gates.

Recommendations are reproducible for the same inputs. Scores are heuristics and are never treated as predictions of individual behavior.

## Privacy and anti-inversion

- Avoid person-level threat scores.
- Collect the minimum data necessary.
- Prefer aggregate weak signals over dossiers.
- Separate allegation, evidence, adjudication and repair.
- Keep appeal and correction paths visible.
- Do not let gamification reward accusation volume, punishment, surveillance or conflict.
- Explain degraded/offline modes.
- Require explicit user action before external network features.
