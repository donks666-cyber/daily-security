Title: Last Week in Security (LWiS) - 2023-01-02
Date: 2023-01-02 22:35
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-01-02
Author: Erik
Summary: x64dbg scripts and plugins (<a href="https://twitter.com/_n1ghtw0lf" target="_blank">@_n1ghtw0lf</a>), ShellcodeMutator (<a href="https://twitter.com/m0rv4i" target="_blank">@m0rv4i</a>), Dirty-Vanity (<a href="https://twitter.com/eliran_nissan" target="_blank">@eliran_nissan</a>), Windows Kernel dev 101 (<a href="https://twitter.com/v3ded" target="_blank">@V3ded</a>), detailed Chrome exploitation (<a href="https://twitter.com/jack_halon" target="_blank">@jack_halon</a>), PassTheChallenge (<a href="https://twitter.com/ly4k_" target="_blank">@ly4k_</a>) and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-12-12 to 2023-01-02.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/" target="_blank">[LastPass] Notice of Recent Security Incident</a>. The breach from August is worse than initially reported, with encrypted password vaults stolen. Despite their encryption, weak master passwords or <a href="https://twitter.com/cryptopathic/status/1606416137771782151" target="_blank">perhaps other issues</a> could lead to passwords and other information leaking to the perpetrators. If you use a password manager (cloud based or not), the loss of your vault has to be part of your threat model. Other services have been <a href="https://blog.1password.com/not-in-a-million-years/" target="_blank">quick to capitalize on LastPass' failure</a>.</li>
<li><a href="https://security.googleblog.com/2022/12/announcing-osv-scanner-vulnerability.html" target="_blank">Announcing OSV-Scanner: Vulnerability Scanner for Open Source</a>. Google launches an <a href="https://github.com/google/osv-scanner" target="_blank">open source dependency vulnerability scanner</a> based on their <a href="https://osv.dev/" target="_blank">OSV</a> database.</li>
<li><a href="https://www.wiz.io/blog/owassrf-a-new-exploit-for-exchange-vulnerabilities-exploited-in-the-wild-everythi" target="_blank">OWASSRF, a new exploit for Exchange vulnerabilities, exploited in the wild: everything you need to know</a>. At this point, self-hosting Microsoft Exchange is an extremely risky proposition. Unless it's behind a VPN or Zero Trust Network Access (making it hard to use with Outlook/etc), you're asking for compromise.</li>
<li><a href="https://www.recordedfuture.com/2022-adversary-infrastructure-report" target="_blank">2022 Adversary Infrastructure Report</a>. Cobalt Strike still dominates.</li>
<li><a href="https://www.zerodayinitiative.com/advisories/ZDI-22-1690/" target="_blank">Linux Kernel ksmbd Use-After-Free Remote Code Execution Vulnerability</a>. In the unlikely case you are running SMB using the new kernel module and not samba, update now or face unauthenticated RCE.</li>
<li><a href="https://www.ic3.gov/Media/Y2022/PSA221221" target="_blank">Cyber Criminals Impersonating Brands Using Search Engine Advertisement Services to Defraud Users</a>. The title is a bit bland, but this is official FBI communication encouraging the use of ad blockers. I've heard stories of companies that force uBlock Origin as part of their managed Chrome install to great effect.</li>
<li><a href="https://clo.ng/blog/sunsetting-detectionlab/" target="_blank">Sunsetting DetectionLab</a>. One of the best automated lab tools is ending development. The scene is set for an open source, modular, lab infrastructure system to be released...</li>
<li><a href="https://cracktheelf.github.io/rules" target="_blank">Crack the ELF RE challenges</a> - "Here are some reverse-engineering challenges I've made on my spare time."</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.exodusintel.com/2022/12/19/linux-kernel-exploiting-a-netfilter-use-after-free-in-kmalloc-cg/" target="_blank">Linux Kernel: Exploiting a Netfilter Use-after-Free in kmalloc-cg</a>. Some great technical Linux exploitation detail in this write up.</li>
<li><a href="https://adepts.of0x.cc/dlopen-from-memory-php/" target="_blank">Spice up your persistence: loading PHP extensions from memory</a>. This technique is neat as your backdoor lives in the PHP process with only some suspect memory maps to give it away after loading from disk (and unloading the disk backed copy of the backdoor).</li>
<li><a href="https://n1ght-w0lf.github.io/tutorials/writing-x64dbg-scripts/" target="_blank">Writing x64dbg scripts</a> and <a href="https://n1ght-w0lf.github.io/tutorials/writing-x64dbg-plugins/" target="_blank">Writing x64dbg plugins</a> will help you level up your x64dbg game.</li>
<li><a href="https://research.nccgroup.com/2022/12/22/puckungfu-a-netgear-wan-command-injection/" target="_blank">Puckungfu: A NETGEAR WAN Command Injection</a>. This command injection requires control of DNS on the WAN side of the router.</li>
<li><a href="https://research.nccgroup.com/2022/12/19/meshyjson-a-tp-link-tdpserver-json-stack-overflow/" target="_blank">MeshyJSON: A TP-Link tdpServer JSON Stack Overflow</a>. In contrast to the relatively simple command injection exploit in Puckungfu, this exploit is a address leak and heap spray to bypass KASLR to execute a ROP gadget. Impressive stuff.</li>
<li><a href="https://labs.nettitude.com/blog/exploiting-onlyoffice-web-sockets-for-unauthenticated-remote-code-execution/" target="_blank">CVE-2021-43444 to 43449: Exploiting ONLYOFFICE Web Sockets for Unauthenticated Remote Code Execution</a>. This is a great read for any web app pentesters. The inital bug doesn't look so bad, but the chain to RCE is impressive.</li>
<li><a href="https://v3ded.github.io/redteam/red-team-tactics-writing-windows-kernel-drivers-for-advanced-persistence-part-1" target="_blank">Red Team Tactics: Writing Windows Kernel Drivers for Advanced Persistence (Part 1)</a>. This post is all lab/dev setup and a Hello World, but the series could get interesting quickly. For a finished series, check out <a href="https://idov31.github.io/2022/07/14/lord-of-the-ring0-p1.html" target="_blank">Lord Of The Ring0</a>.</li>
<li><a href="https://www.sentinelone.com/labs/labscon-replay-breaking-firmware-trust-from-the-other-side-exploiting-early-boot-phases-pre-efi/" target="_blank">LABScon Replay | Breaking Firmware Trust From The Other Side: Exploiting Early Boot Phases (Pre-Efi)</a>. You've heard of bootkits, but what about pre-bootkits?</li>
<li>Trend Micro drops 2x macOS LPE posts: <a href="https://www.trendmicro.com/en_us/research/22/l/diving-into-an-old-exploit-chain-and-discovering-3-new-sip-bypas.html" target="_blank">Diving into an Old Exploit Chain and Discovering 3 new SIP-Bypass Vulnerabilities</a> and <a href="https://www.trendmicro.com/en_us/research/22/l/a-technical-analysis-of-cve-2022-22583-and-cve-2022-32800.html" target="_blank">A Technical Analysis of CVE-2022-22583 and CVE-2022-32800</a>.</li>
<li><a href="https://unit42.paloaltonetworks.com/sandbox-evasion-memory-detection/" target="_blank">Navigating the Vast Ocean of Sandbox Evasions</a>. Palo Alto's sandbox is custom and has fixes for many common sandbox detections. Would your detections get caught in this sandbox?</li>
<li><a href="https://jhalon.github.io/chrome-browser-exploitation-3/" target="_blank">Chrome Browser Exploitation, Part 3: Analyzing and Exploiting CVE-2018-17463</a>. Part 3 of the amazingly detailed browser exploitation series is here!</li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2022/12/19/gatekeepers-achilles-heel-unearthing-a-macos-vulnerability/" target="_blank">Gatekeeper's Achilles heel: Unearthing a macOS vulnerability</a>. Microsoft digs into a strange "AppleDouble" file format and finds a Gatekeeper bypass.</li>
<li><a href="https://rastamouse.me/net-startup-hooks/" target="_blank">.NET Startup Hooks</a>. If you can set environment variables for .NET programs, you can inject arbitrary code. Could be a useful persistence technique as there are built in .NET binaries in Windows.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://labs.nettitude.com/blog/shellcode-source-mutations/" target="_blank">Avoiding Detection with Shellcode Mutator</a>. By randomly adding nops or nop equivalent instructions, <a href="https://github.com/nettitude/ShellcodeMutator" target="_blank">ShellcodeMutator</a> can break yara rules that look for specific assembly sequences in shellcode.</li>
<li><a href="https://github.com/deepinstinct/Dirty-Vanity" target="_blank">Dirty-Vanity</a> - A POC for the new injection technique, abusing windows fork API to evade EDRs. See the slides from BlackHat EU <a href="https://i.blackhat.com/EU-22/Thursday-Briefings/EU-22-Nissan-DirtyVanity.pdf" target="_blank">here</a>.</li>
<li><a href="https://github.com/binderlabs/DirCreate2System" target="_blank">DirCreate2System</a> - Weaponizing to get NT SYSTEM for Privileged Directory Creation Bugs with Windows Error Reporting.</li>
<li><a href="https://github.com/kiks7/CVE-2022-2602-Kernel-Exploit" target="_blank">CVE-2022-2602-Kernel-Exploit</a> and <a href="https://github.com/LukeGix/CVE-2022-2602" target="_blank">CVE-2022-2602</a> are Linux LPEs for Linux kernel upstream stable 5.4.x, 5.15.x, and later versions. 5.10.x may be vulnerable as well.</li>
<li><a href="https://github.com/Octoberfest7/Cohab_Processes" target="_blank">Cohab_Processes</a> - A small Aggressor script to help Red Teams identify foreign processes on a host machine.</li>
<li><a href="https://blog.sektor7.net/#!res/2022/cafebiba.md" target="_blank">CaFeBiBa - COFF parser</a> - a COFF parser for binaries compiled with MSVC.</li>
<li><a href="https://github.com/winsecurity/Offensive-Rust" target="_blank">Offensive-Rust</a> - Various offensive techniques in Rust.</li>
<li><a href="https://github.com/mlcsec/ASRenum-BOF" target="_blank">ASRenum-BOF</a> - Cobalt Strike BOF that identifies Attack Surface Reduction (ASR) rules, actions, and exclusion locations.</li>
<li><a href="https://github.com/kkent030315/CVE-2022-42046" target="_blank">CVE-2022-42046</a> - CVE-2022-42046 Proof of Concept of wfshbr64.sys local privilege escalation via DKOM.</li>
<li><a href="https://github.com/namazso/linux_injector" target="_blank">linux_injector</a> - A simple ptrace-less shared library injector for x64 Linux.</li>
<li><a href="https://github.com/Idov31/Venom" target="_blank">Venom</a> is a library that meant to perform evasive communication using stolen browser socket.</li>
<li><a href="https://github.com/gh0x0st/wanderer" target="_blank">wanderer</a> - An open-source process injection enumeration tool written in C#.</li>
<li><a href="https://github.com/Wra7h/PowerShell-Scripts/blob/main/Invoke-Retractor/Invoke-Retractor.ps1" target="_blank">Invoke-Retractor</a> - Build a Seatbelt executable containing only commands you specify.</li>
<li><a href="https://github.com/rad9800/WTSRM2" target="_blank">WTSRM2</a> - Writing Tiny Small Reliable Malware 2. This has a ton of cool features, worth a look.</li>
<li><a href="https://github.com/ly4k/PassTheChallenge" target="_blank">PassTheChallenge</a> - Recovering NTLM hashes from Credential Guard. See the blog post for more <a href="https://research.ifcr.dk/pass-the-challenge-defeating-windows-defender-credential-guard-31a892eee22" target="_blank">details</a>.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/JamesWoolfenden/pike" target="_blank">pike</a> is a tool for determining the permissions or policy required for IAC code.</li>
<li><a href="https://github.com/tailscale/policies" target="_blank">policies</a> - Security policies for Tailscale.</li>
<li><a href="https://iximiuz.com/en/posts/ssh-tunnels/" target="_blank">A Visual Guide to SSH Tunnels: Local and Remote Port Forwarding</a>. I use SSH tunnels on a daily basis, and this is a great visual guide to anyone new to the concept (or as a reference if you forget!).</li>
<li><a href="https://github.com/mprimi/portable-secret" target="_blank">portable-secret</a> - Better privacy without special software.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 422 (+0)</p>
<p>Blogs monitored: 330 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
