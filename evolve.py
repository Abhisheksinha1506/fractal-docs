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
    # CAP growth to prevent exceeding GitHub file size limits
    if len(new_axiom) > 100000:
        print(f"⚠️ Axiom length ({len(new_axiom)}) exceeds 100k cap. Pruning to maintain stability.")
        new_axiom = new_axiom[:100000]
    
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

    summary = f"The fractal plant has reached iteration {state['iteration']}. It currently consists of {len(new_axiom)} symbols, forming a complex branching structure with {new_axiom.count('[')} unique branches."
    update_readme(summary)


def update_readme(summary):
    from pathlib import Path
    from datetime import datetime
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
        new_inner = f"""
*{summary} ({timestamp})*
"""
        readme_path.write_text(prefix + new_inner + suffix)
    except Exception as e: print(f"⚠️ README Update Failed: {e}")
if __name__ == "__main__":
    evolve()

