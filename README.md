# Hoop Land Mod Loader

A backend-neutral modding framework for **Hoop Land Demo**. The goal is to build an extensible mod ecosystem for custom teams, players, leagues, tournaments, courts, jerseys, animations, interface themes, gameplay presets, and code mods.

> **Current status:** this repository contains the mod format, portable C# contracts, loader orchestration, package tooling, sample content, and a simulated dry-run backend. It does **not** yet inject into Hoop Land or apply mods in-game.

## Start here

1. Read [README_FIRST.md](README_FIRST.md) for setup and verification steps.
2. Read [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the system design.
3. Read [docs/DEVELOPMENT_PLAN.md](docs/DEVELOPMENT_PLAN.md) for milestones and next steps.
4. Run the Python package checks:

```bash
python3 tools/hlmod.py validate samples/ContentPackMod
bash tests/verify_samples.sh
```

## Project areas

- `src/HoopLand.ModLoader.Contracts` — stable mod API and runtime backend interfaces.
- `src/HoopLand.ModLoader.Core` — mod discovery, validation, dependencies, content loading, and orchestration.
- `tools/hlmod.py` — validate, package, install, and list `.hlmod` packages.
- `tools/HoopLand.ModLoader.DryRun` — simulated host for exercising the managed pipeline without launching the game.
- `samples/ContentPackMod` — example data packs for game content categories.
- `samples/CodeMod` — example C# mod.
- `.github/workflows/build.yml` — cloud build and verification workflow.

## Safety and compatibility

Keep the Steam installation untouched. Use a separate game copy for any future runtime experiments. Installing a mod package into a folder does not make the game load it.

The target game is a Unity IL2CPP build. A compatible runtime/injection backend and verified game-specific data mappings are still required before mods can affect gameplay. The backend-neutral design keeps that research isolated from mod packages and public API contracts.

Unknown code mods can execute with the permissions of your user account. The manifest permission list is descriptive, not a security sandbox. Only use code mods you trust.

## Build status

The GitHub Actions workflow builds the C# solution, runs the package checks, executes the simulated dry-run host, and uploads a build artifact. A successful workflow validates the source and simulated pipeline; it does not establish in-game loader compatibility.

## License

No license has been selected yet. Until one is added, all rights are reserved by default.
