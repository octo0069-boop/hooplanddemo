#!/usr/bin/env python3
"""Small standard-library .hlmod package utility."""
import argparse, json, pathlib, zipfile, sys

def manifest(folder):
    p = folder / "mod.json"
    if not p.is_file():
        raise ValueError(f"missing {p}")
    data = json.loads(p.read_text(encoding="utf-8"))
    for key in ("id", "version", "name"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f"manifest requires non-empty '{key}'")
    return data

def validate(path):
    path = pathlib.Path(path)
    if path.is_dir():
        m = manifest(path)
    elif zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            candidates = [n for n in names if n.endswith("/mod.json") or n == "mod.json"]
            if not candidates: raise ValueError("package contains no mod.json")
            m = json.loads(z.read(candidates[0]))
            for key in ("id", "version", "name"):
                if not isinstance(m.get(key), str) or not m[key].strip():
                    raise ValueError(f"manifest requires non-empty '{key}'")
    else:
        raise ValueError("expected a mod folder or .hlmod ZIP")
    print(f"VALID: {m['id']} {m['version']} — {m['name']}")

def pack(folder, output):
    folder = pathlib.Path(folder)
    m = manifest(folder)
    output = pathlib.Path(output or (folder.parent / (folder.name + ".hlmod")))
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(folder.rglob("*")):
            if p.is_file(): z.write(p, p.relative_to(folder).as_posix())
    print(f"PACKED: {output} ({m['id']})")

def install(package, mods):
    package, mods = pathlib.Path(package), pathlib.Path(mods)
    with zipfile.ZipFile(package) as z:
        z.testzip() and (_ for _ in ()).throw(ValueError("corrupt ZIP"))
        names = z.namelist()
        mf = next((n for n in names if n.endswith("/mod.json") or n == "mod.json"), None)
        if not mf: raise ValueError("package contains no mod.json")
        m = json.loads(z.read(mf))
        target = mods / m["id"]
        if target.exists(): raise ValueError(f"target already exists: {target}")
        target.mkdir(parents=True, exist_ok=True)
        for n in names:
            p = pathlib.PurePosixPath(n)
            if p.is_absolute() or ".." in p.parts: raise ValueError("unsafe package path")
            out = target.joinpath(*p.parts)
            if n.endswith("/"): out.mkdir(parents=True, exist_ok=True)
            else:
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(z.read(n))
    print(f"INSTALLED: {target}")

def list_mods(mods):
    root = pathlib.Path(mods)
    if not root.exists(): return
    for p in sorted(root.iterdir()):
        try:
            m = manifest(p)
            print(f"{m['id']} {m['version']} [installed] {m['name']}")
        except Exception: continue

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("validate", "pack"):
        q = sub.add_parser(name); q.add_argument("path")
        if name == "pack": q.add_argument("--output")
    q = sub.add_parser("install"); q.add_argument("package"); q.add_argument("--mods", required=True)
    q = sub.add_parser("list"); q.add_argument("mods")
    a = ap.parse_args()
    try:
        if a.cmd == "validate": validate(a.path)
        elif a.cmd == "pack": pack(a.path, a.output)
        elif a.cmd == "install": install(a.package, a.mods)
        elif a.cmd == "list": list_mods(a.mods)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr); return 1
    return 0
if __name__ == "__main__": raise SystemExit(main())
