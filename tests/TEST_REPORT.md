# Test Report

## Verified

- JavaScript syntax (`assets/app.js`, `sw.js`) via `node --check`.
- HTML parses successfully.
- No duplicate static IDs.
- Route registry matches route sections.
- Every literal JavaScript `#id` reference resolves to a static HTML ID.
- Manifest icon path exists.
- Every local asset in the service-worker app-shell list exists.
- Required 10-system / 10-story content anchors are present.
- Bundle file tree and SHA-256 checksums generated.

## Browser execution limitation

An attempted Chromium/Playwright smoke test could not run because the execution environment blocks browser navigation by administrator policy. The block applied to localhost HTTP, `file://`, and `data:` URLs, so it was not an application-origin or service-worker error. Therefore routing, IndexedDB persistence, PWA registration, downloads, responsive behavior and optional Trystero networking are statically reviewed but not claimed as browser-executed here.

## Recommended deployment smoke test

After publishing over HTTPS or localhost:

1. open the site and verify the splash dismisses;
2. navigate every side-menu route and an unknown hash;
3. run the deterministic planner and scenario lab;
4. add an evidence record, reload and confirm persistence;
5. export JSON, re-import it, then test malformed JSON rejection;
6. install/reload the PWA and verify offline app-shell access;
7. open two tabs and test BroadcastChannel room messaging;
8. optionally test internet P2P with non-sensitive text only;
9. test mobile drawer, keyboard navigation, focus, reduced motion and print;
10. review console/network logs for errors before public deployment.
