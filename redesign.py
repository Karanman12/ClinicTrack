import re

filepath = r'c:\Users\manda\OneDrive\Documents\Clinic_TrackPro\templates\start.html'
with open(filepath, 'r', encoding='utf-8') as f:
    c = f.read()

# Replace CSS Variables
c = re.sub(r'--bg-page:.*?;', '--bg-page: #F2F1ED;', c)
c = re.sub(r'--bg-surface:.*?;', '--bg-surface: #FFFFFF;', c)
c = re.sub(r'--bg-navbar:.*?;', '--bg-navbar: rgba(242, 241, 237, 0.85);', c)
c = re.sub(r'--btn-primary:.*?;', '--btn-primary: #111111;', c)
c = re.sub(r'--btn-primary-hover:.*?;', '--btn-primary-hover: #333333;', c)
c = re.sub(r'--btn-ghost-text:.*?;', '--btn-ghost-text: #111111;', c)
c = re.sub(r'--btn-ghost-border:.*?;', '--btn-ghost-border: #D1D0CB;', c)
c = re.sub(r'--btn-ghost-hover:.*?;', '--btn-ghost-hover: #E8E7E3;', c)
c = re.sub(r'--text-heading:.*?;', '--text-heading: #111111;', c)
c = re.sub(r'--text-body:.*?;', '--text-body: #3A3A3A;', c)
c = re.sub(r'--text-muted:.*?;', '--text-muted: #6B6A66;', c)
c = re.sub(r'--text-link:.*?;', '--text-link: #111111;', c)
c = re.sub(r'--border:.*?;', '--border: #E8E7E3;', c)
c = re.sub(r'--badge-bg:.*?;', '--badge-bg: #FFFFFF;', c)
c = re.sub(r'--badge-text:.*?;', '--badge-text: #111111;', c)
c = re.sub(r'--input-border:.*?;', '--input-border: #E8E7E3;', c)
c = re.sub(r'--bg-footer:.*?;', '--bg-footer: #F2F1ED;', c)

# Replace hover shadows
c = re.sub(r'box-shadow: 0 10px 25px -5px rgba\(74, 157, 228, 0\.25\), 0 8px 10px -6px rgba\(74, 157, 228, 0\.25\);', 'box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.05);', c)
c = re.sub(r'box-shadow: 0 20px 25px -5px rgba\(0, 0, 0, 0\.1\), 0 10px 10px -5px rgba\(0, 0, 0, 0\.04\);', 'box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.01);', c)
c = re.sub(r'shadow-primary/20', 'shadow-black/10', c)
c = re.sub(r'shadow-primary/25', 'shadow-black/10', c)
c = re.sub(r'border-2 border-primary', 'border border-black', c)
c = re.sub(r'bg-primary text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider shadow-sm', 'bg-black text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider shadow-sm', c)

# Replace colored icons in features to monochromatic or subtle
c = re.sub(r'bg-orange-500/10 text-orange-500', 'bg-black/5 text-black', c)
c = re.sub(r'group-hover:bg-orange-500', 'group-hover:bg-black', c)
c = re.sub(r'bg-emerald-500/10 text-emerald-500', 'bg-black/5 text-black', c)
c = re.sub(r'group-hover:bg-emerald-500', 'group-hover:bg-black', c)
c = re.sub(r'bg-purple-500/10 text-purple-500', 'bg-black/5 text-black', c)
c = re.sub(r'group-hover:bg-purple-500', 'group-hover:bg-black', c)
c = re.sub(r'bg-teal-500/10 text-teal-500', 'bg-black/5 text-black', c)
c = re.sub(r'group-hover:bg-teal-500', 'group-hover:bg-black', c)
c = re.sub(r'bg-red-500/10 text-red-500', 'bg-black/5 text-black', c)
c = re.sub(r'group-hover:bg-red-500', 'group-hover:bg-black', c)
c = re.sub(r'bg-primary/10 text-primary', 'bg-black/5 text-black', c)

# Contact section colors
c = re.sub(r'bg-gradient-to-br from-\[#4A9DE4\] to-\[#2B609E\]', 'bg-black', c)

# Wave colors
c = re.sub(r"colorPeak: '#f5d87a'", "colorPeak: '#E8E7E3'", c)
c = re.sub(r"colorEdge: '#ffe9a8'", "colorEdge: '#F2F1ED'", c)
c = re.sub(r"colorPeak: '#5aaff5'", "colorPeak: '#DCDAD3'", c)
c = re.sub(r"colorEdge: '#a8d8ff'", "colorEdge: '#F2F1ED'", c)

# Wave fade gradient colors (rgba(244, 248, 252 -> rgba(242, 241, 237)
c = c.replace('rgba(244, 248, 252', 'rgba(242, 241, 237')

# Form hover/focus borders
c = re.sub(r'border-primary', 'border-black', c)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(c)

print("Redesign applied.")
