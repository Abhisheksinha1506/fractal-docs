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

    with open(readme_path, 'w') as f:
        f.write(readme_content)

if __name__ == "__main__":
    evolve()
