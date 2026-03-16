import os

cards = [
    {
        "id": "project1",
        "icon": "⚡",
        "title": "FastRoboEyes",
        "subtitle": "High-Performance Rendering Engine",
        "desc1": "Hardware-optimized animation",
        "desc2": "pipeline built for robotics platforms.",
        "tags": [("C++", 45), ("Python", 60)],
        "glow1": "rgba(56, 189, 248, 0.5)",  # cyan
        "glow2": "rgba(99, 102, 241, 0.4)",  # indigo
    },
    {
        "id": "project2",
        "icon": "🧠",
        "title": "AdaptiFocus",
        "subtitle": "AI Attention Management",
        "desc1": "AI-driven productivity platform",
        "desc2": "with behavioral analytics.",
        "tags": [("FastAPI", 65), ("Docker", 60)],
        "glow1": "rgba(168, 85, 247, 0.5)",  # purple
        "glow2": "rgba(236, 72, 153, 0.4)",  # pink
    },
    {
        "id": "project3",
        "icon": "🌐",
        "title": "SDN Testbed",
        "subtitle": "Software Defined Networking",
        "desc1": "Experimental SDN environment",
        "desc2": "on Raspberry Pi clusters.",
        "tags": [("Linux", 50), ("Network", 70)],
        "glow1": "rgba(234, 179, 8, 0.4)",   # yellow
        "glow2": "rgba(239, 68, 68, 0.4)",   # red
    }
]

template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 230" width="100%" height="100%">
  <defs>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="35" result="blur" />
    </filter>
    <linearGradient id="glassGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.08)" />
      <stop offset="100%" stop-color="rgba(255,255,255,0.01)" />
    </linearGradient>
    <linearGradient id="borderGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.25)" />
      <stop offset="100%" stop-color="rgba(255,255,255,0.04)" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="15" stdDeviation="20" flood-color="#000" flood-opacity="0.4" />
    </filter>
  </defs>

  <circle cx="40" cy="40" r="70" fill="{glow1}" filter="url(#glow)" />
  <circle cx="340" cy="190" r="80" fill="{glow2}" filter="url(#glow)" />

  <rect x="15" y="15" width="350" height="200" rx="20" ry="20" fill="url(#glassGradient)" stroke="url(#borderGradient)" stroke-width="1.5" filter="url(#shadow)" />

  <g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
    <text x="40" y="58" font-size="24">{icon}</text>
    <text x="75" y="56" font-size="22" font-weight="700" fill="#ffffff" letter-spacing="0.5px">{title}</text>
    
    <text x="40" y="94" font-size="14" font-weight="600" fill="#e5e7eb">{subtitle}</text>
    
    <text x="40" y="128" font-size="13" fill="#9ca3af" font-weight="400">{desc1}</text>
    <text x="40" y="148" font-size="13" fill="#9ca3af" font-weight="400">{desc2}</text>
    
    {tags_svg}
  </g>
</svg>"""

for card in cards:
    tags_svg = ""
    current_x = 40
    for tag_name, tag_width in card["tags"]:
        tags_svg += f'<rect x="{current_x}" y="170" width="{tag_width}" height="24" rx="6" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.15)"/>\\n    '
        text_x = current_x + (tag_width / 2)
        tags_svg += f'<text x="{text_x}" y="186" font-size="11" font-weight="600" fill="#e5e7eb" text-anchor="middle">{tag_name}</text>\\n    '
        current_x += tag_width + 10
        
    svg_str = template.format(
        glow1=card["glow1"],
        glow2=card["glow2"],
        icon=card["icon"],
        title=card["title"],
        subtitle=card["subtitle"],
        desc1=card["desc1"],
        desc2=card["desc2"],
        tags_svg=tags_svg
    )
    
    with open(f"./{card['id']}.svg", "w") as f:
        f.write(svg_str)
