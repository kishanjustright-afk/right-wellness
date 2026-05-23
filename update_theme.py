import re

def update_theme():
    with open("rightwellness.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Replacements for root variables block
    content = content.replace("--deep-purple: #2D1B4E;", "--navy-dark: #00263E;")
    content = content.replace("--mid-purple: #4A2D7A;", "--navy-mid: #00456C;")
    content = content.replace("--light-purple: #7B5EA7;", "--navy-light: #006093;")
    content = content.replace("--burgundy: #6B1E35;", "--teal-dark: #00666D;")
    content = content.replace("--wine: #8B2E42;", "--teal-deep: #004D52;")
    content = content.replace("--muted-gold: #B8965A;", "--teal-main: #008C95;")
    content = content.replace("--off-white: #F5F2EC;", "--off-white: #F5F7FA;")
    content = content.replace("--warm-grey: #E8E4DC;", "--warm-grey: #E2E8ED;")
    content = content.replace("--soft-beige: #EDE8DF;", "--soft-beige: #EAF0F4;")
    content = content.replace("--charcoal: #1A1614;", "--charcoal: #0F171E;")
    content = content.replace("--text-body: #3D3530;", "--text-body: #1E2A34;")
    content = content.replace("--text-muted: #7A7169;", "--text-muted: #5C6B77;")

    # Replace variable names in the rest of the document
    content = content.replace("--deep-purple", "--navy-dark")
    content = content.replace("--mid-purple", "--navy-mid")
    content = content.replace("--light-purple", "--navy-light")
    content = content.replace("--burgundy", "--teal-dark")
    content = content.replace("--wine", "--teal-deep")
    content = content.replace("--muted-gold", "--teal-main")

    # Replace RGBA hardcoded values
    content = content.replace("rgba(45,27,78", "rgba(0,38,62")  # deep-purple -> navy-dark
    content = content.replace("rgba(184,150,90", "rgba(0,140,149") # muted-gold -> teal-main
    content = content.replace("rgba(107,30,53", "rgba(0,102,109") # burgundy -> teal-dark
    content = content.replace("rgba(245,242,236", "rgba(245,247,250") # off-white
    content = content.replace("rgba(232,228,220", "rgba(226,232,237") # warm-grey

    # We also have hex values hardcoded in some places like:
    # #1A0D2E, #2D1B4E, #3D1A2E, #1A0D2E
    content = content.replace("#1A0D2E", "#001826")
    content = content.replace("#2D1B4E", "#00263E")
    content = content.replace("#3D1A2E", "#003A42")
    # #CBB070 -> lighter teal
    content = content.replace("#CBB070", "#00AAB5")
    # #C4B4A0, #9E8E7E, #7A6558 -> image background blocks (can make them teal/grey)
    content = content.replace("#C4B4A0", "#B0C4CC")
    content = content.replace("#9E8E7E", "#8A9EA8")
    content = content.replace("#7A6558", "#637A85")
    
    # Other color hexes in editorial block
    content = content.replace("#2A1F35", "#001D30")
    content = content.replace("#4A3050", "#003354")
    content = content.replace("#6B4565", "#004978")
    content = content.replace("#1C1410", "#0C1217")
    content = content.replace("#3D2820", "#18242E")
    content = content.replace("#5A3C2E", "#253745")

    # Replace logos
    # Line 1459: <a href="#" class="nav-logo">right<span>WELLNESS</span></a>
    content = content.replace('<a href="#" class="nav-logo">right<span>WELLNESS</span></a>', 
                              '<a href="#" class="nav-logo"><img src="wellnessLogo.svg" alt="rightWELLNESS Logo" style="height: 32px; width: auto; margin-top: 5px;"></a>')
    
    # Line 2018: <a href="#" class="nav-logo">right<span style="color:var(--teal-main)">WELLNESS</span></a>
    content = content.replace('<a href="#" class="nav-logo">right<span style="color:var(--teal-main)">WELLNESS</span></a>',
                              '<a href="#" class="nav-logo"><img src="wellnessLogo.svg" alt="rightWELLNESS Logo" style="height: 48px; width: auto; filter: brightness(0) invert(1);"></a>')
                              
    with open("rightwellness.html", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_theme()
