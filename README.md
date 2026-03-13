# Sunbliss Garden

A peaceful summer retreat built using A-Frame, a web framework for building virtual reality experiences.

## Overview

This project renders a relaxing virtual scene entirely within the browser using HTML-like declarative components via A-Frame. The scene features:
- A lush green field with scattered patches of grass clusters to create depth.
- Decorative elements like a wooden patio table, textured with realistic assets, and two matching chairs.
- Scattered details on the table including stylized cups, plates, and milk/milo tins with custom branding.
- A blocky "person" model made completely out of primitive shapes.

## Assets Used

- `table.jpg` - Placed to form the wood texture on the patio table and chairs.
- `metal.png` - Used as a shiny metallic layer for tin bodies and lids.
- `milk.jpg`, `milo.png` - Real-world logo labels attached to the tins.

## How to Run

Because this project relies on fetching texture files over the network from your local machine, it is highly recommended you run this on a local web server (like XAMPP, Live Server, `python -m http.server`, etc.) rather than opening the HTML file directly as `file://`.

Open `index.html` through your preferred local server to dive into the scene.

## Controls

- **Mouse:** Click and drag to look around.
- **Keyboard:** Use `W`, `A`, `S`, `D` to walk along the grass.
