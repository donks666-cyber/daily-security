Title: Last Week in Security (LWiS) - 2026-03-30
Date: 2026-03-30 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2026-03-30
Author: Erik
Summary: 🏟️❤️🤖 Ludus MCP/Skills (<a href="https://x.com/badsectorlabs" target="_blank">@badsectorlabs</a>), Grapefruit 📱 security suite (<a href="https://x.com/CodeColorist" target="_blank">@CodeColorist</a>), 2 Citrix NetScaler posts (<a href="https://x.com/AlizTheHax0r" target="_blank">@AlizTheHax0r</a> + <a href="https://x.com/_McCaulay" target="_blank">@_mccaulay</a>), 🔒 BIOS bypass (<a href="https://x.com/craigsblackie" target="_blank">@craigsblackie</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2026-03-24 to 2026-03-30.</p>
<aside class="m-block m-success">
<h3>🏟️ ❤️ 🤖</h3>
<p><a href="https://ludus.cloud" target="_blank">Ludus</a> started as a dream: What if you could create the perfect lab environment for your current needs with minimal effort but maximum flexibility? With the release of <a href="https://gitlab.com/badsectorlabs/ludus-mcp" target="_blank">ludus-mcp</a> and <a href="https://gitlab.com/badsectorlabs/ludus-skills" target="_blank">ludus-skills</a> you can now build lab environments with natural language! You can prompt, "create a range with 2 VLANs: in the first put a domain controller for the domain example.com and a domain joined windows 11 workstation with office 2019 installed; in the second VLAN put an elastic server and put the elastic agent on all three machines." and your agent + Ludus will do all the heavy lifting! The MCP exposes just three tools to keep your context window clean and save you valuable tokens. Check out the <a href="https://docs.ludus.cloud/docs/using-ludus/mcp" target="_blank">docs</a> to get started.</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.macrumors.com/2026/03/27/critical-security-alerts-sent-to-ios-17-iphones/" target="_blank">Apple Now Sending Critical Security Alerts to iPhones Running iOS 17 and Earlier</a> - With multiple exploit kits appearing in the wild the past few weeks, it looks like Apple is taking a new step to get older OSs up to date. Apple recently stated, <a href="https://techcrunch.com/2026/03/27/apple-says-no-one-using-lockdown-mode-has-been-hacked-with-spyware/" target="_blank">“We are not aware of any successful mercenary spyware attacks against a Lockdown Mode-enabled Apple device.”</a> They've also stepped up their game in regard to the <a href="https://daringfireball.net/2026/03/apple_enclaves_neo_camera_indicator" target="_blank">on-screen camera indicator</a>.</li>
<li><a href="https://www.outflank.nl/blog/2026/03/26/introducing-cobalt-strike-research-labs/" target="_blank">Introducing Cobalt Strike Research Labs</a> - You can now upgrade your Cobalt Strike subscription with "cutting-edge, ready-to-use research tooling for Cobalt Strike, including custom UDRLs, Sleep Masks, UDC2 channels, and post-exploitation capabilities."</li>
<li><a href="https://www.techdirt.com/2026/03/12/the-wyden-siren-goes-off-again-well-be-stunned-by-what-the-nsa-is-doing-under-section-702/" target="_blank">The Wyden Siren Goes Off Again: We'll Be “Stunned” By What the NSA Is Doing Under Section 702</a> - "I strongly believe that this matter can and should be declassified and that Congress needs to debate it openly before Section 702 is reauthorized. In fact, when it is eventually declassified, the American people will be stunned that it took so long and that Congress has been debating this authority with insufficient information."</li>
<li><a href="https://indianexpress.com/article/world/us-news/fbi-director-kash-patels-personal-inbox-breached-iranian-hackers-leak-private-photos-resume-10605119/" target="_blank">FBI director Kash Patel’s personal email breached: Iran-linked hackers leak private photos, resume</a> - Looks like the classic data breach password reuse. Expected for most people, pretty embarrassing for the FBI director. How is there not a process to make sure these people at least enroll in the free <a href="https://landing.google.com/intl/en_in/advancedprotection/" target="_blank">Advanced Protection Program</a>?</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.watchtowr.com/the-sequels-are-never-as-good-but-were-still-in-pain-citrix-netscaler-cve-2026-3055-memory-overread/" target="_blank">The Sequels Are Never As Good, But We're Still In Pain (Citrix NetScaler CVE-2026-3055 Memory Overread)</a> - "Citrix advises that the vulnerability is only exploitable if the appliance is 'configured as a SAML IDP'. This is a cursed configuration to begin with, and we can think of no appliance more poorly-suited to the task of being an IdP than this class of network device." 🤣</li>
<li><a href="https://labs.watchtowr.com/please-we-beg-just-one-weekend-free-of-appliances-citrix-netscaler-cve-2026-3055-memory-overread-part-2/" target="_blank">Please, We Beg, Just One Weekend Free Of Appliances (Citrix NetScaler CVE-2026-3055 Memory Overread Part 2)</a> - A GET request returns kilobytes of arbitrary memory from an unpatched Citrix NetScaler. Session IDs show up rather quickly, leading to authentication bypass.</li>
<li><a href="https://www.mdsec.co.uk/2026/03/disabling-security-features-in-a-locked-bios/" target="_blank">Disabling Security Features in a Locked BIOS</a> - From locked BIOS to SYSTEM shell, this post shows what can be done with physical access and a willingness to flash a chip.</li>
<li><a href="https://specterops.io/blog/2026/03/26/leveling-up-secure-code-reviews-with-claude-code/" target="_blank">Leveling Up Secure Code Reviews with Claude Code</a> - The "Educational Mode" prompt is neat. The latest generation of models is good enough that you can treat it like a very persistent coworker. What's crazy is that these tools only get better from here (lookout for <a href="https://m1astra-mythos.pages.dev/" target="_blank">Claude Mythos</a>).</li>
<li><a href="https://pwn.guide/free/cryptography/audio-steganography" target="_blank">Audio Steganography in Supply Chain Attacks</a> - The supply chain attacks from last week had some interesting WAV audio files that hid the payloads in the sound. Props for creativity!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/badsectorlabs/ludus-mcp" target="_blank">ludus-mcp</a> - MCP server for managing <a href="https://ludus.cloud" target="_blank">Ludus</a> cyber ranges.</li>
<li><a href="https://github.com/badsectorlabs/ludus-skills" target="_blank">ludus-skills</a> - AI agent skills <a href="https://ludus.cloud" target="_blank">Ludus</a> cyber ranges.</li>
<li><a href="https://codecolor.ist/grapefruit/" target="_blank">Open-source mobile security testing suite</a> - The "Grapefruit" mobile testing tool is back!</li>
<li><a href="https://github.com/whokilleddb/emulat3" target="_blank">emulat3</a> - Step through PE functions or shellcode instruction-by-instruction (amd64).</li>
<li><a href="https://github.com/GoogleCloudPlatform/scion" target="_blank">scion</a> - Run multiple agents in parallel — each in its own container, with its own workspace, collaborating on your code or project files simultaneously.</li>
<li><a href="https://github.com/craigsblackie/8FC8_Patcher" target="_blank">8FC8_Patcher</a> - Patcher for Dell 8FC8 suffix UEFI written in Python.</li>
<li><a href="https://github.com/blacklanternsecurity/red-run" target="_blank">red-run</a> - Security assessment toolkit for Claude Code.</li>
<li><a href="https://github.com/ZerkerEOD/krakenhashes/releases/tag/v2.0.0" target="_blank">KrakenHashes v2.0.0</a> - RBAC, SSO, priority based scheduling, passkey support, and more in this big update of the distributed password cracking system.</li>
<li><a href="https://github.com/ZakiPedio/BridgeHead" target="_blank">BridgeHead</a> - Native C++ access to Active Directory over ADWS, no .NET, no WCF, no HTTP stack.</li>
<li><a href="https://github.com/Meowmycks/trustme" target="_blank">trustme</a> - BOF to impersonate TrustedInstaller via DISM API trigger and thread impersonation.</li>
<li><a href="https://github.com/y637F9QQ2x/NOFILTER-NFEXEC" target="_blank">NOFILTER-NFEXEC</a> - Havoc C2 BOF — WFP kernel-space SYSTEM escalation + command execution with indirect syscalls, patchless AMSI/ETW bypass, and return address spoofing.</li>
<li><a href="https://github.com/backdoorskid/CustomLoadImage" target="_blank">CustomLoadImage</a> - Stealthy .NET assembly loading using AssemblyNative::LoadFromBuffer.</li>
<li><a href="https://github.com/Christopher-Schulze/QuicFuscate" target="_blank">QuicFuscate</a> - Efficiency-centric, anti-censorship QUIC/HTTP/3 VPN protocol with adaptive FEC and SIMD-accelerated AEAD.</li>
<li><a href="https://github.com/Pouzor/homelable" target="_blank">homelable</a> - Self-hosted homelab infrastructure visualizer — interactive network diagram with live status monitoring.</li>
<li><a href="https://github.com/Whispergate/InfraGuard" target="_blank">InfraGuard</a> is a Command &amp; Control Redirection Proxy and Manager which protects your Red Team Infrastructure against threat attribution.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/gadievron/raptor" target="_blank">raptor</a> - Raptor turns Claude Code into a general-purpose AI offensive/defensive security agent. By using Claude.md and creating rules, sub-agents, and skills, and orchestrating security tool usage, we configure the agent for adversarial thinking, and perform research or attack/defense operations.</li>
<li><a href="https://justinjackson.ca/xslt?utm_campaign=unsupervised-learning-no-522&amp;utm_medium=referral&amp;utm_source=newsletter.danielmiessler.com" target="_blank">Don't Kill My Pretty RSS Feed</a> - Pour one out for XSLT.</li>
<li><a href="https://github.com/a13xp0p0v/kernel-hack-drill" target="_blank">kernel-hack-drill</a> - This is a playground for the Linux kernel exploitation experiments. Only basic methods. Just for fun.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 496 (+0)</p>
<p>Blogs monitored: 443 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>X: <a href="https://x.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
