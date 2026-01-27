from pathlib import Path
import os
import json
import datetime

def evolve():
    base_dir = os.path.dirname(__file__)
    state_path = os.path.join(base_dir, 'state.json')
    rules_path = os.path.join(base_dir, 'rules.json')
    readme_path = os.path.join(base_dir, 'README.md')

    with open(state_path, 'r') as f:
        state = json.load(f)
    
    with open(rules_path, 'r') as f:
        rules = json.load(f)

    current_axiom = state["axiom"]
    new_axiom = ""
    
    for char in current_axiom:
        new_axiom += rules.get(char, char)

    # Update state
    state["axiom"] = new_axiom
    state["iteration"] += 1
    state["last_updated"] = datetime.date.today().isoformat()
    
    with open(state_path, 'w') as f:
        json.dump(state, f, indent=4)

    # Format for README
    # We'll use a visual representation or just nested text.
    # Let's try to make it look a bit tree-like in the README.
    
    formatted_axiom = new_axiom.replace('[', '\n  [').replace(']', ']\n')
    
    readme_content = f"""# L-System Fractal Documentation

This documentation grows fractally every day.

## Current State
Iteration: {state['iteration']}
Last Updated: {state['last_updated']}

## Growth Pattern
```text
{formatted_axiom[:2000]} {"..." if len(formatted_axiom) > 2000 else ""}
```

## Raw Symbols
{new_axiom[:500]} {"..." if len(new_axiom) > 500 else ""}
"""

    # L-System special: we inject the plant visualization AND the status
    readme_content = f"""# 🌿 Fractal Docs (L-System Documentation)

> "Documentation that grows like a plant, branching into infinite complexity."

### 📢 Latest Status
<!-- LATEST_STATUS_START -->
> {summary}
<!-- LATEST_STATUS_END -->

### 📖 The Analogy
Have you ever noticed how a tree branch looks like a smaller version of the whole tree? That's a fractal. This repository uses a mathematical language called an "L-System" to grow text in the same way a fern or a tree grows its leaves.

### 🌱 Current Plant Growth (Iteration {state['iteration']})
```text
{new_axiom}
```

### 🌱 How it Evolves
This README is rewritten every night by a mathematical gardener:
1. **Reading the DNA**: The rules are stored in [rules.json](rules.json).
2. **Growing the Branch**: The current "plant" in [state.json](state.json) is expanded.
3. **Updating the Page**: The result is rendered right here in this README.

**The plant grows on its own schedule, following its internal logic.**

### 🔍 Quick Links
- [Current DNA (Rules)](rules.json) — See the branching rules.
- [Growth State](state.json) — The raw symbols of the current iteration.
- [The Gardener](evolve.py) — The script that rewrites this documentation.
"""
    with open(readme_path, 'w') as f:
        f.write(readme_content)


def update_readme(summary):
    readme_path = Path("README.md")
    if not readme_path.exists(): return
    try:
        content = readme_path.read_text()
        start = "<!-- LATEST_STATUS_START -->"
        end = "<!-- LATEST_STATUS_END -->"
        if start not in content or end not in content: return
        parts = content.split(start)
        suffix_parts = parts[1].split(end)
        prefix = parts[0] + start
        suffix = end + suffix_parts[1]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_inner = f"
*{summary} ({timestamp})*
"
        readme_path.write_text(prefix + new_inner + suffix)
    except Exception as e: print(f"⚠️ README Update Failed: {e}")
if __name__ == "__main__":
    evolve()

