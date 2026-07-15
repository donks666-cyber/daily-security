Title: Last Week in Security (LWiS) - 2025-09-22
Date: 2025-09-22 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-09-22
Author: Erik
Summary: Getting Global Admin in every Entra tenant (<a href="https://x.com/_dirkjan" target="_blank">@_dirkjan</a>), WebSocket Turbo Intruder (<a href="https://x.com/zakfedotkin" target="_blank">@zakfedotkin</a>), PureRAT analysis (<a href="https://x.com/Tera0017" target="_blank">@Tera0017</a>), direct syscalls in Zig (<a href="https://x.com/zux0x3a" target="_blank">@zux0x3a</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-09-15 to 2025-09-22.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.koi.security/incident/shai-hulud-npm-supply-chain-attack-crowdstrike-tinycolor" target="_blank">Live Updates: Shai-Hulud, The Most Dangerous NPM Breach In History Affecting CrowdStrike and Hundreds of Popular Packages</a> - Another NPM breach. If you're using NPM, it's tike to take steps to protect yourself. Consider using pnpm with a <a href="https://pnpm.io/settings#minimumreleaseage" target="_blank">minimumReleaseAge</a> in the configuration to delay package updates and using <a href="https://github.com/containers/bubblewrap" target="_blank">bubblewrap</a> in a <a href="https://news.ycombinator.com/item?id=45271988" target="_blank">script</a> to invoke package managers. Credit to <a href="https://x.com/cyb3rops/status/1968282946306994323" target="_blank">Florian Roth @cyb3rops</a> for the suggestions.</li>
<li><a href="https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_ftc_on_microsoft_kerberoasting_ransomwarepdf.pdf" target="_blank">[PDF] I write to request that the Federal Trade Commission (FTC) investigate and hold Microsoft responsible for its gross cybersecurity negligence</a> - US Senator <a href="https://en.wikipedia.org/wiki/Ron_Wyden" target="_blank">Ron Wyden</a> drops terms like Kerberoasting and RC4 in a letter to the FCC. Ron Wyden is the one who called for the <a href="https://www.cisa.gov/resources-tools/resources/CSRB-Review-Summer-2023-MEO-Intrusion" target="_blank">Cyber Safety Review Board Report on Summer 2023 Microsoft Online Exchange Incident</a>, so it's possible this request could result in action. However, the Cyber Safety Review Board was <a href="https://www.securityinfowatch.com/cybersecurity/article/55263590/trump-administration-disbands-cyber-safety-review-board" target="_blank">disbanded</a> 6 days into the second Trump administration.</li>
<li><a href="https://www.legislature.mi.gov/documents/2025-2026/billintroduced/House/pdf/2025-HIB-4938.pdf" target="_blank">[PDF] House Bill No. 4938</a> - "An internet service provider providing internet service in this state shall implement mandatory filtering technology to prevent residents of this state from accessing prohibited material. An internet service provider providing internet service in this state shall actively monitor and block known circumvention tools." The US state of Michigan could join China, Russia, Pakistan, and Myanmar in banning VPNs. No US state has attempted to ban VPNs before, even as part of age verification requirements. The fact the bill's sponsor asked the Michigan State Police if banning pornography/VPNs was <a href="https://home.mirs.news/post/schriver-looks-to-pull-the-plug-on-internet-pornography" target="_blank">“something you guys are equipped to enforce?”</a> makes me think this bill is engagement bait and not a serious attempt to change laws. I suppose it worked.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://dirkjanm.io/obtaining-global-admin-in-every-entra-id-tenant-with-actor-tokens/" target="_blank">One Token to rule them all - obtaining Global Admin in every Entra ID tenant via Actor tokens</a> - This is the most impactful vulnerability since <a href="https://en.wikipedia.org/wiki/EternalBlue" target="_blank">EternalBlue</a>. Since this was a vulnerability in the Azure/Entra cloud, it affected all Microsoft cloud users but also could be patched by Microsoft for all customers at once. The potential damage of this vulnerability being found by a malicious actor cannot be understated. I hope Microsoft compensated Dirk-jan appropriately.</li>
<li><a href="https://portswigger.net/research/websocket-turbo-intruder-unearthing-the-websocket-goldmine" target="_blank">WebSocket Turbo Intruder: Unearthing the WebSocket Goldmine</a> - Web applications with real time features often use WebSockets to communicate between the client and server reusing a connection. This can be opaque to testers and often goes unexplored, however vulnerabilities lurk any place data is processed, and <a href="https://github.com/d0ge/WebSocketTurboIntruder" target="_blank">WebSocketTurboIntruder</a>  allows you to fuzz WebSockets with custom Python code.</li>
<li><a href="https://research.checkpoint.com/2025/under-the-pure-curtain-from-rat-to-builder-to-coder/" target="_blank">Under the Pure Curtain: From Rat to Builder to Coder</a> - Check Point Research does a great job documenting the full, multi-step infection chain from "click fix" lure, to an open source intermediate remote access tool, and finally a full fledged "commercial" remote access tool.</li>
<li><a href="https://0xsp.com/security%20research%20%20development%20srd/malware%20research/implementing-hells-gate-in-zig-part-1/" target="_blank">Implementing Hell’s Gate in Zig – Part 1</a> - Zig is an up and coming language (i.e. used in <a href="https://github.com/ghostty-org/ghostty" target="_blank">ghostty</a>), and this post ports a Rust implementation of the direct syscall technique for Windows called Hell's Gate to Zig. The Code is available in <a href="https://github.com/0xsp-SRD/zig_offsec" target="_blank">zig_offsec</a>.</li>
<li><a href="https://volticks.github.io/CVE-2025-21692-nday-writeup/" target="_blank">CVE-2025-21692 nday writeup</a> - A buffer underflow/out of bounds read in the packet scheduling queueing ETS (Enhanced Transmission Selection) qdisc can be used as a write primitive and eventually remote code execution in the Linux kernel. Code available here: <a href="https://github.com/volticks/CVE-2025-21692-poc" target="_blank">CVE-2025-21692-poc</a>.</li>
<li><a href="https://www.huntress.com/blog/dangers-of-storing-unencrypted-passwords" target="_blank">Huntress Threat Advisory: The Dangers of Storing Unencrypted Passwords</a> - A threat actor found plaintext Huntress recovery codes on a Huntress customer's desktop, and used them to close Huntress security alerts, disable the Huntress agent, and deploy ransomware. In this case, Huntress was used as <a href="https://gitlab.com/badsectorlabs/iscariot-suite" target="_blank">traitorware</a>.</li>
<li><a href="https://www.atlanticcouncil.org/in-depth-research-reports/issue-brief/mythical-beasts-diving-into-the-depths-of-the-global-spyware-market/" target="_blank">Mythical Beasts: Diving into the depths of the global spyware market</a> - "The authors found that the number of US-based investors in spyware has notably increased in the past year," and, "the authors elaborated on the central role that resellers and brokers play in the spyware market, while being a notably under-researched set of actors."</li>
<li><a href="https://specterops.io/blog/2025/09/18/more-fun-with-wmi/" target="_blank">More Fun With WMI</a> - <cite>MSFT_MTProcess</cite> is a class on Server operating systems that can perform similar functions to <cite>Win32_Process</cite>. There are also ways to install it remotely on workstations.</li>
<li><a href="https://nighthawkc2.io/automating-operations/" target="_blank">Automating Operations with Nighthawk</a> - The ability to extend and automate your command and control servers and agents is critical for high level red teams.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/TwoSevenOneT/EDR-Freeze" target="_blank">EDR-Freeze</a> - EDR-Freeze is a tool that puts a process of EDR, AntiMalware into a coma state.</li>
<li><a href="https://github.com/0xthirteen/WMI_Proc_Dump" target="_blank">WMI_Proc_Dump</a> - Dump processes over WMI with MSFT_MTProcess.</li>
<li><a href="https://github.com/0xthirteen/mtprocess" target="_blank">mtprocess</a> - Python script to leverage MSFT_MTProcess WMI class.</li>
<li><a href="https://www.openwall.com/presentations/NullconBerlin2025-LKRG/" target="_blank">Linux Kernel Runtime Guard (LKRG) 1.0</a> is a Linux kernel module that performs runtime integrity checking of the kernel and detection of security vulnerability exploits against the kernel, prevention of and response to successful attacks, and encrypted remote logging.</li>
<li><a href="https://github.com/praetorian-inc/google-redirector" target="_blank">google-redirector</a> - A lightweight redirector for Google Cloud Run, enabling domain fronting via Google-owned infrastructure. See: <a href="https://www.praetorian.com/blog/domain-fronting-is-dead-long-live-domain-fronting/" target="_blank">Domain Fronting is Dead. Long Live Domain Fronting!</a> (not to be confused with my DEF CON 28 talk <a href="https://media.defcon.org/DEF%20CON%2028/DEF%20CON%20Safe%20Mode%20presentations/DEF%20CON%20Safe%20Mode%20-%20Erik%20Hunstad%20-%20Domain%20Fronting%20is%20Dead%20Long%20Live%20Domain%20Fronting.pdf" target="_blank">[PDF] Domain Fronting is Dead, Long Live Domain Fronting</a>)</li>
<li><a href="https://github.com/initstring/TTPx" target="_blank">TTPx</a> - Red Team reporting and analytics platform.</li>
<li><a href="https://github.com/Hexorg/Ouroboros" target="_blank">Ouroboros</a> - Decompiler written in Rust.</li>
<li><a href="https://kson.org/docs/blog/2025/09/17/introducing-kson/" target="_blank">Introducing KSON</a> - "Anywhere a human is reading or editing YAML/JSON/TOML, KSON may be used as a more effective interface on that data." KSON is a superset of JSON but written like YAML.</li>
<li><a href="https://github.com/1r0BIT/TaskHound" target="_blank">TaskHound</a> - Tool to enumerate privileged Scheduled Tasks on Remote Systems.</li>
<li><a href="https://github.com/guardian-nexus/auditkit" target="_blank">auditkit</a> - Open source SOC2 compliance scanner - Alternative to $20k/year tools.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/0xsp-SRD/ZigStrike" target="_blank">ZigStrike</a> - ZigStrike, a powerful Payload Delivery Pipeline developed in Zig, offering a variety of injection techniques and anti-sandbox features.</li>
<li><a href="https://github.com/0xricksanchez/like-dbg" target="_blank">like-dbg</a> - Fully dockerized Linux kernel debugging environment.</li>
<li><a href="https://www.exaforce.com/blogs/ghost-in-the-script" target="_blank">Ghost in the Script: Impersonating Google App Script projects for stealthy persistence</a> - "Apps Script projects can serve as stealthy persistence mechanisms if left unmonitored. Attackers can impersonate them to hide cryptomining, privileged service accounts, or other malicious resources inside your environment."</li>
<li><a href="https://github.com/KingOfTheNOPs/Get-NetNTLM" target="_blank">Get-NetNTLM</a> - Internal Monologue BOF.</li>
<li><a href="https://github.com/ofkm/arcane" target="_blank">arcane</a> - Modern Docker Management, Designed for Everyone.</li>
<li><a href="https://github.com/withoutbg/withoutbg" target="_blank">withoutbg</a> - Open source image background removal model.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 458 (+0)</p>
<p>Blogs monitored: 424 (+0)</p>
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
