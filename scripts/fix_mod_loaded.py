import argparse
import json
import re
from pathlib import Path


NAMESPACE_PATTERN = re.compile(r"\b([a-z0-9_.-]+):[a-z0-9_./-]+\b")
IGNORED_NAMESPACES = {"minecraft", "c", "forge", "neoforge", "kubejs"}


def collect_namespaces(node, found):
    if isinstance(node, dict):
        for value in node.values():
            collect_namespaces(value, found)
        return
    if isinstance(node, list):
        for value in node:
            collect_namespaces(value, found)
        return
    if isinstance(node, str):
        for match in NAMESPACE_PATTERN.finditer(node):
            namespace = match.group(1)
            if namespace not in IGNORED_NAMESPACES:
                found.add(namespace)


def update_conditions(data):
    namespaces = set()
    collect_namespaces(data, namespaces)

    if not namespaces:
        return False

    conditions = data.get("neoforge:conditions")
    if not isinstance(conditions, list):
        conditions = []

    existing = {
        entry.get("modid")
        for entry in conditions
        if isinstance(entry, dict)
        and entry.get("type") == "neoforge:mod_loaded"
        and isinstance(entry.get("modid"), str)
    }

    changed = False
    for namespace in sorted(namespaces):
        if namespace in existing:
            continue
        conditions.append({"type": "neoforge:mod_loaded", "modid": namespace})
        changed = True

    if changed or "neoforge:conditions" in data:
        data["neoforge:conditions"] = conditions
        return True

    return False


def process_file(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False

    if not isinstance(data, dict):
        return False

    changed = update_conditions(data)
    if changed:
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return changed


def is_recipe_file(root, path):
    relative_parts = path.relative_to(root).parts
    return len(relative_parts) >= 3 and relative_parts[1] == "recipe"


def main():
    parser = argparse.ArgumentParser(
        description="Scan recipe JSON files and add neoforge:mod_loaded conditions for all referenced namespaces."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".pakku/overrides/kubejs/data",
        help="Root directory containing datapack JSON files.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        raise SystemExit(f"Path does not exist: {root}")

    changed_files = 0
    for path in sorted(root.rglob("*.json")):
        if not is_recipe_file(root, path):
            continue
        if process_file(path):
            changed_files += 1

    print(f"Updated {changed_files} recipe files under {root}")


if __name__ == "__main__":
    main()
