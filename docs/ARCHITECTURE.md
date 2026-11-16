# Architecture

The project separates the mod format and public API from the mechanism used to execute code inside the game.

## Layers

1. **Mod packages** — versioned `.hlmod` archives with a manifest, content definitions, and optional assets.
2. **Contracts** — stable interfaces that code mods target. These must not depend on a particular injector.
3. **Core** — discovery, validation, dependency ordering, registration orchestration, and diagnostics.
4. **Runtime backend** — replaceable adapter responsible for communicating with the running game.
5. **Game adapter** — maps our documented content definitions to verified Hoop Land IL2CPP/game structures.

## Why backend-neutral?

The earlier BepInEx IL2CPP macOS experiment reached chainloader initialization and then crashed. We should not assume that backend is compatible. Keeping it behind an interface lets us investigate alternatives without changing every mod package.

## Current boundary

The contracts and packaging tools are a framework foundation. The simulated host is only for tests. No supported runtime injector currently exists in this repository, and sample JSON definitions are not yet guaranteed to match the game's internal schema.

## Safety

Treat code mods as executable programs with the current user's permissions. Do not load untrusted DLLs. Test runtime experiments against a separate game copy, never the Steam installation.
