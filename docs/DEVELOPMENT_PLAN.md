# Development plan

## Phase 1 — Modding foundation
- [x] Define a backend-neutral public API
- [x] Define a package manifest and content-pack examples
- [x] Add validation and package tooling
- [x] Add a simulated backend for dry-run tests

## Phase 2 — Build verification
- [x] Add a GitHub Actions build workflow
- [ ] Run the first cloud build and fix compile/test failures
- [ ] Publish a versioned framework artifact

## Phase 3 — Game compatibility research
- [ ] Build a read-only IL2CPP inspection tool in an isolated copy
- [ ] Identify safe game lifecycle hooks
- [ ] Verify actual game data structures and serialization
- [ ] Prototype a runtime adapter without modifying the Steam install

## Phase 4 — Player-facing mod ecosystem
- [ ] Mod manager UI (enable, disable, update, dependency warnings)
- [ ] Team/player/league/tournament editors
- [ ] Court, jersey, logo, and UI asset workflows
- [ ] Gameplay and animation extension points
- [ ] Documentation and compatibility tests for mod authors

A phase is not complete until its tests and limitations are documented. A successful build does not mean in-game injection works.
