# 🌿 Fractal Docs (L-System Documentation)

> "Documentation that grows like a plant, branching into infinite complexity."

### 📢 Latest Status
<!-- LATEST_STATUS_START -->
*The fractal plant has reached iteration 123. It currently consists of 100000 symbols, forming a complex branching structure with 0 unique branches. (2026-02-18 07:31)*
<!-- LATEST_STATUS_END -->

### 📖 The Analogy
Have you ever noticed how a tree branch looks like a smaller version of the whole tree? That's a fractal. This repository uses a mathematical language called an "L-System" to grow text in the same way a fern or a tree grows its leaves.

We start with a single "seed" (a character like 'X'). Every day, that seed follows a set of "DNA rules" to branch out into more characters. Over time, the text becomes a massive, branching structure that looks like a digital plant.

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
