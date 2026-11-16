# Getting started

This repository is the backend-neutral foundation for a Hoop Land Demo modding ecosystem.

## Current capabilities

- Portable mod API contracts and replaceable runtime-backend interface
- Mod manifest model and dependency ordering
- Content-pack manifest examples
- Python `.hlmod` package utility
- Simulated dry-run host for testing the managed pipeline

## Important limitation

This is **not yet an in-game injector**. Hoop Land is a Unity IL2CPP game. A compatible runtime backend and verified mappings from our content formats to the game's actual data structures are still required before mods can change the live game.

Keep the Steam installation untouched. Use a separate copy for all future runtime experiments.

## Requirements

- Python 3 for package tooling
- .NET 10 SDK to build the solution locally
- GitHub Actions can build the project in the cloud

## Python package checks

```bash
python3 tools/hlmod.py validate samples/ContentPackMod
bash tests/verify_samples.sh
python3 tools/hlmod.py pack samples/ContentPackMod
python3 tools/hlmod.py validate samples/ContentPackMod.hlmod
```

## Build and dry-run

```bash
dotnet build HoopLand.ModLoader.sln -c Release
dotnet run --project tools/HoopLand.ModLoader.DryRun --configuration Release -- --mods samples --game-version 1.09.6
```

The dry-run host uses a fake backend. It does not launch, inject into, or modify Hoop Land.

## Safety

Code mods run with the permissions of the current user. The manifest permission list is descriptive and is not a security sandbox. Only install code mods you trust.

Read [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and [docs/DEVELOPMENT_PLAN.md](docs/DEVELOPMENT_PLAN.md) before attempting runtime work.
