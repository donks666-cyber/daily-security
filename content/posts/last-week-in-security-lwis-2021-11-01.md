Title: Last Week in Security (LWiS) - 2021-11-01
Date: 2021-11-01 22:00
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-11-01
Author: Erik
Summary: DLL proxying with artifact kit (<a href="https://twitter.com/joevest" target="_blank">@joevest</a>), lateral movement 101 (<a href="https://twitter.com/_RastaMouse" target="_blank">@_RastaMouse</a>), Windows kernel driver hooking (<a href="https://twitter.com/cerbersec" target="_blank">@cerbersec</a>), macOS XAR arbitrary file write (<a href="https://twitter.com/buffaloverflow" target="_blank">@buffaloverflow</a>), malapi.io launch (<a href="https://twitter.com/mrd0x" target="_blank">@mrd0x</a>), protobuf in sqlmap (<a href="https://twitter.com/APTortellini" target="_blank">@APTortellini</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-10-26 to 2021-11-01.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2021/11/trick-treat-paying-leets-and-sweets-for.html" target="_blank">Trick &amp; Treat! 🎃 Paying Leets and Sweets for Linux Kernel privescs and k8s escapes</a>. Exploit a k8s environment to earn $31,337-$50,337 USD! More details <a href="https://google.github.io/kctf/vrp" target="_blank">here</a>.</li>
<li><a href="https://security.googleblog.com/2021/10/protecting-your-device-information-with.html" target="_blank">Protecting your device information with Private Set Membership</a>. This cryptographic process could be useful for all kinds of sensitive data lookups (i.e. is my password in a breach?).</li>
<li><a href="https://malapi.io/" target="_blank">MalAPI.io launches</a>.  MalAPI.io can be used when developing malware (for legal purposes of course) or when analyzing the source code of malware. It's a MITRE ATT&amp;CK matrix for Windows APIs.</li>
<li><a href="https://defcon.org/html/defcon-30/dc-30-cfce.html" target="_blank">Announcing the DEF CON 30 Call For Contests &amp; Events!</a>. Start planning early!</li>
<li><a href="https://www.ekioh.com/devblog/google-docs-in-a-clean-room-browser/" target="_blank">Google Docs in a clean-room browser</a>. Just an example of how much duct tape and glue</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://twitter.com/patrickwardle/status/1453850551267905542" target="_blank">Neat SIP bypass for macOS</a>. system_installd executes a zsh shell and has an entitlement to bypass SIP. Microsoft found a way to leverage this to run commands with the same entitlement with /etc/zshenv. How many more ways are there? Full Microsoft post: <a href="https://www.microsoft.com/security/blog/2021/10/28/microsoft-finds-new-macos-vulnerability-shrootless-that-could-bypass-system-integrity-protection/" target="_blank">Shrootless</a>.</li>
<li><a href="https://blog.cobaltstrike.com/2021/10/29/create-a-proxy-dll-with-artifact-kit/" target="_blank">Create a proxy DLL with artifact kit</a>. DLL proxying is a great way to persist and in some cases elevate privileges. This post shows how to use the official artifact kit to turn a Cobalt Strike DLL into a "function proxy."</li>
<li><a href="https://offensivedefence.co.uk/posts/lateral-movement-101/" target="_blank">Lateral Movement 101</a>. The old favorites are here, but perhaps there are details you've missed? Rasta also dropped new C# related projects today: <a href="https://rastamouse.me/d-invoke-baguette/" target="_blank">D/Invoke Baguette</a>.</li>
<li><a href="https://blog.nviso.eu/2021/10/29/kernel-karnage-part-2-back-to-basics/" target="_blank">Kernel Karnage – Part 2 (Back to Basics)</a>. EDRs are moving to the kernel, and drivers can provide great local privilege escalation opportunities. This post explores the ability to hook other driver's (EDR) functions. Want to start debugging the windows kernel? This <a href="https://jmpesp.me/windows-kernel-debugging-101/" target="_blank">101 post</a> was released yesterday.</li>
<li><a href="https://research.nccgroup.com/2021/10/28/technical-advisory-apple-xar-arbitrary-file-write-cve-2021-30833/" target="_blank">Technical Advisory – Apple XAR – Arbitrary File Write (CVE-2021-30833)</a>. These types of archive extraction arbitrary file writes can be great for phishing and even local privilege escalation (if a program accepts an archive and extracts it at a higher privilege level). Fixed in 12.0.1.</li>
<li><a href="https://theevilbit.github.io/posts/cve_2021_30920/" target="_blank">CVE-2021-30920 - CVE-2021-1784 strikes back - TCC bypass via mounting</a>. macOS 12 has a regression that allows users to mount over ~/Library and this the TCC database. Yikes! Fixed in 12.0.1.</li>
<li><a href="https://aptw.tf/2021/10/27/exploiting-protobuf-webapps.html" target="_blank">Tortellini in Brodobuf</a>. Serializing data just adds a layer of unpacking, not security. This post goes from manual decode and exploitation proof to writing a sqlmap tamper script to automate it.</li>
<li><a href="https://redteaming.co.uk/2021/10/28/understanding-syscalls/" target="_blank">Understanding SysCalls Manipulation</a>. Direct syscalls have been around for a while, but this technique makes sure they jmp back to memory space of NTDLL.DLL to avoid suspicious of the kernel returning to program memory space it should't (i.e. the location of your direct syscall). Sneaky! PoC <a href="https://gist.github.com/benpturner/43b46506e4f98e5b860f72c3a6c42367" target="_blank">here</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/righteousgambitresearch/quiet-riot" target="_blank">quiet-riot</a> is an enumeration tool for scalable, unauthenticated validation of AWS principals; including AWS Acccount IDs, root e-mail addresses, users, and roles. Check out the blog post <a href="https://blog.traingrc.com/introducing-quiet-riot-c595cfa629e" target="_blank">here</a>.</li>
<li><a href="https://github.com/rasta-mouse/DInvoke" target="_blank">DInvoke</a> is a library to dynamically invoke arbitrary unmanaged code from managed code without P/Invoke. Fork of D/Invoke by TheWover, but refactored to .NET Standard 2.0 and split into individual <a href="https://nuget.code-offensive.net/?q=DInvoke" target="_blank">NuGet packages</a>.</li>
<li><a href="https://github.com/ByteJunkies-co-uk/Metsubushi" target="_blank">Metsubushi</a> is a Go project to generate droppers with encrypted payloads automatically.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/splunk/melting-cobalt" target="_blank">melting-cobalt</a> scans for Cobalt Strike teamservers, grabs beacons that allow staging, and stores their configs. No reason to leave staging enabled these days...</li>
<li><a href="https://github.com/cybersecsi/dockerized-android" target="_blank">dockerized-android</a> is a container-based framework to enable the integration of mobile components in security training platforms.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
