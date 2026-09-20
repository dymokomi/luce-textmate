#!/usr/bin/env python3
"""Run luce-textmate's test blocks in native and C comparison modes."""
import argparse
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--base", type=Path, default=ROOT.parent / ("luce-base/build/luce-base.exe" if os.name == "nt" else "luce-base/build/luce-base"))
parser.add_argument("--luce", type=Path, default=ROOT.parent / ("luce/build/luce.exe" if os.name == "nt" else "luce/build/luce"))
args = parser.parse_args()
env = dict(os.environ, LUCE_BASE=str(args.base.resolve()))
modules = ["json.luc", "grammar.luc", "tokenizer.luc"]
for name in modules:
    module = ROOT / "src/luce_textmate" / name
    for flags in [["--native"], ["--backend=c"]]:
        subprocess.run([str(args.luce.resolve()), "test", str(module), "--build", *flags], check=True, env=env, timeout=240)
print("PASS luce-textmate modules, native and comparison modes")
