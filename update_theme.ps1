$content = Get-Content "rightwellness.html" -Raw

# Replace variables in root
$content = $content.Replace("--deep-purple: #2D1B4E;", "--navy-dark: #00263E;")
$content = $content.Replace("--mid-purple: #4A2D7A;", "--navy-mid: #00456C;")
$content = $content.Replace("--light-purple: #7B5EA7;", "--navy-light: #006093;")
$content = $content.Replace("--burgundy: #6B1E35;", "--teal-dark: #00666D;")
$content = $content.Replace("--wine: #8B2E42;", "--teal-deep: #004D52;")
$content = $content.Replace("--muted-gold: #B8965A;", "--teal-main: #008C95;")
$content = $content.Replace("--off-white: #F5F2EC;", "--off-white: #F5F7FA;")
$content = $content.Replace("--warm-grey: #E8E4DC;", "--warm-grey: #E2E8ED;")
$content = $content.Replace("--soft-beige: #EDE8DF;", "--soft-beige: #EAF0F4;")
$content = $content.Replace("--charcoal: #1A1614;", "--charcoal: #0F171E;")
$content = $content.Replace("--text-body: #3D3530;", "--text-body: #1E2A34;")
$content = $content.Replace("--text-muted: #7A7169;", "--text-muted: #5C6B77;")

# Replace variable usages
$content = $content.Replace("--deep-purple", "--navy-dark")
$content = $content.Replace("--mid-purple", "--navy-mid")
$content = $content.Replace("--light-purple", "--navy-light")
$content = $content.Replace("--burgundy", "--teal-dark")
$content = $content.Replace("--wine", "--teal-deep")
$content = $content.Replace("--muted-gold", "--teal-main")

# Replace RGB values
$content = $content.Replace("rgba(45,27,78", "rgba(0,38,62")
$content = $content.Replace("rgba(184,150,90", "rgba(0,140,149")
$content = $content.Replace("rgba(107,30,53", "rgba(0,102,109")
$content = $content.Replace("rgba(245,242,236", "rgba(245,247,250")
$content = $content.Replace("rgba(232,228,220", "rgba(226,232,237")

# Replace other colors
$content = $content.Replace("#1A0D2E", "#001826")
$content = $content.Replace("#2D1B4E", "#00263E")
$content = $content.Replace("#3D1A2E", "#003A42")
$content = $content.Replace("#CBB070", "#00AAB5")
$content = $content.Replace("#C4B4A0", "#B0C4CC")
$content = $content.Replace("#9E8E7E", "#8A9EA8")
$content = $content.Replace("#7A6558", "#637A85")
$content = $content.Replace("#2A1F35", "#001D30")
$content = $content.Replace("#4A3050", "#003354")
$content = $content.Replace("#6B4565", "#004978")
$content = $content.Replace("#1C1410", "#0C1217")
$content = $content.Replace("#3D2820", "#18242E")
$content = $content.Replace("#5A3C2E", "#253745")

# Replace Logo
$content = $content.Replace('<a href="#" class="nav-logo">right<span>WELLNESS</span></a>', '<a href="#" class="nav-logo" style="display:flex; align-items:center;"><img src="wellnessLogo.svg" alt="rightWELLNESS" style="height: 40px; width: auto;"></a>')

$content = $content.Replace('<a href="#" class="nav-logo">right<span style="color:var(--teal-main)">WELLNESS</span></a>', '<a href="#" class="nav-logo" style="display:flex; align-items:center;"><img src="wellnessLogo.svg" alt="rightWELLNESS" style="height: 40px; width: auto; filter: brightness(0) invert(1);"></a>')

[IO.File]::WriteAllText("rightwellness.html", $content)
