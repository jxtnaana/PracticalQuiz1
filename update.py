import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace ground layers
ground_pattern = r"<!-- LAYER 1.*?<!-- ════════════════════════════════\n\s*ROUND PATIO TABLE"
replacement_ground = """<!-- LAYER 1 – TEXTURED GRASS -->
    <a-plane position="0 0 0" rotation="-90 0 0" width="140" height="140" src="#tex-grass" repeat="20 20" roughness="0.8"></a-plane>

    <!-- ════════════════════════════════
       ROUND PATIO TABLE"""

text = re.sub(ground_pattern, replacement_ground, text, flags=re.DOTALL)

# Replace head and face
head_pattern = r"<!-- ── HEAD ── -->.*?<!-- ── HAIR"
replacement_head = """<!-- ── HEAD (TEXTURED) ── -->
      <a-sphere position="0 1.612 0" radius="0.168" src="#tex-face" rotation="0 180 0">
      </a-sphere>

      <!-- ── HAIR"""

text = re.sub(head_pattern, replacement_head, text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done")
