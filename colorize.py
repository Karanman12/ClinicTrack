import re

filepath = r'c:\Users\manda\OneDrive\Documents\Clinic_TrackPro\templates\start.html'
with open(filepath, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Primary buttons: back to the original vibrant blue
c = c.replace("--btn-primary: #4F46E5;", "--btn-primary: #4A9DE4;")
c = c.replace("--btn-primary-hover: #4338CA;", "--btn-primary-hover: #3587CD;")

# 2. Links use blue
c = c.replace("--text-link: #4F46E5;", "--text-link: #4A9DE4;")

# 3. Badge: golden warmth
c = c.replace("--badge-bg: #EDE9FE;", "--badge-bg: #FFF8E7;")
c = c.replace("--badge-text: #6D28D9;", "--badge-text: #A8861E;")

# 4. Success dot: original green
c = c.replace("--state-success: #10B981;", "--state-success: #3A9679;")

# 5. Wave ribbons: original gold and blue
c = c.replace("colorPeak: '#FF8A66'", "colorPeak: '#f5d87a'", 1)
c = c.replace("colorEdge: '#FFBB99'", "colorEdge: '#ffe9a8'", 1)
c = c.replace("colorPeak: '#7C6BFF'", "colorPeak: '#5aaff5'", 1)
c = c.replace("colorEdge: '#B0A3FF'", "colorEdge: '#a8d8ff'", 1)

# 6. Contact section: blue gradient
c = c.replace(
    "bg-gradient-to-br from-[#6C3AED] via-[#7C3AED] to-[#4F46E5]",
    "bg-gradient-to-br from-[#4A9DE4] to-[#2B609E]"
)

# 7. Feature icon colors: vibrant mixed with blue tones
c = c.replace("bg-indigo-500/10 text-indigo-600 flex items-center justify-center mb-6 group-hover:bg-indigo-500",
              "bg-blue-500/10 text-blue-600 flex items-center justify-center mb-6 group-hover:bg-blue-500", 1)

# 8. Most Popular badge: blue gradient
c = c.replace(
    "bg-gradient-to-r from-[#6C3AED] to-[#4F46E5] text-white",
    "bg-gradient-to-r from-[#4A9DE4] to-[#2B609E] text-white"
)

# 9. Pricing popular card border: blue
c = c.replace("border-2 border-[#6C3AED] shadow-lg", "border-2 border-[#4A9DE4] shadow-lg")

# 10. Accordion hover: blue accent
c = c.replace("hover:border-indigo-400/40", "hover:border-blue-400/40")

# 11. Form input focus: blue
c = c.replace("focus:outline-none focus:border-indigo-500", "focus:outline-none focus:border-blue-500")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(c)

print("Gold and blue colors restored!")
