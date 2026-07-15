Title: Last Week in Security (LWiS) - 2022-11-28
Date: 2022-11-28 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-11-28
Author: Erik
Summary: AWS AppSync exploit (<a href="https://twitter.com/Frichette_n" target="_blank">@Frichette_n</a>), F5 unauth RCE, Meta's new VCS, Chrome exploitation (<a href="https://twitter.com/jack_halon" target="_blank">@jack_halon</a>), Kerberoasting customization (<a href="https://twitter.com/ben0xa" target="_blank">@Ben0xA</a>), macOS sandbox escape (<a href="https://twitter.com/_r3ggi" target="_blank">@_r3ggi</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-11-14 to 2022-11-28.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://securitylabs.datadoghq.com/articles/appsync-vulnerability-disclosure/" target="_blank">A Confused Deputy Vulnerability in AWS AppSync</a>. The cloud is just someone else's computer. And sometimes it has vulnerabilities too. This one is particularly bad; case insensitivity led to the ability to access resources in other AWS accounts - aka the worst thing possible in a cloud provider. There is a reason some workloads should stay on prem - but only if your on prem security is better than AWS's ability to prevent cross account access (unlikely).</li>
<li><a href="https://stability.ai/blog/stable-diffusion-v2-release" target="_blank">Stable Diffusion 2.0 Release</a>. AI is shaping up to be a major disruptor. Play with it locally with <a href="https://diffusionbee.com/" target="_blank">DiffusionBee</a>. Want to be more awed by the power of AI? Read <a href="https://ai.facebook.com/blog/cicero-ai-negotiates-persuades-and-cooperates-with-people/" target="_blank">this</a>.</li>
<li><a href="https://krebsonsecurity.com/2022/11/researchers-quietly-cracked-zeppelin-ransomware-keys/" target="_blank">Researchers Quietly Cracked Zeppelin Ransomware Keys</a>. Score one for the good guys.</li>
<li><a href="https://www.rapid7.com/blog/post/2022/11/16/cve-2022-41622-and-cve-2022-41800-fixed-f5-big-ip-and-icontrol-rest-vulnerabilities-and-exposures/" target="_blank">CVE-2022-41622 and CVE-2022-41800 (FIXED): F5 BIG-IP and iControl REST Vulnerabilities and Exposures</a>. Another border device manufacturer with RCE...</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.proofpoint.com/us/blog/threat-insight/nighthawk-and-coming-pentest-tool-likely-gain-threat-actor-notice" target="_blank">Nighthawk: An Up-and-Coming Pentest Tool Likely to Gain Threat Actor Notice</a>. This post digs into some of the technical details of the Nighthawk commercial C2 agent. MDSec claims the same was collected as part of legitimate red team activity and posted their own rebuttal: <a href="https://www.mdsec.co.uk/2022/11/nighthawk-with-great-power-comes-great-responsibility/" target="_blank">Nighthawk: With Great Power Comes Great Responsibility</a>.</li>
<li><a href="https://googleprojectzero.blogspot.com/2022/11/mind-the-gap.html" target="_blank">Mind the Gap</a>. TLDR: The patch gap is real, take advantage of it.</li>
<li><a href="https://www.synacktiv.com/en/publications/a-dive-into-microsoft-defender-for-identity.html" target="_blank">A dive into Microsoft Defender for Identity</a>. Some good ideas for detecting MDI after you land a phish or start an internal assessment with low privileges.</li>
<li><a href="https://thalpius.com/2022/11/15/microsoft-defender-for-identity-encrypted-password/" target="_blank">Microsoft Defender for Identity Encrypted Password</a>. More MDI fun, along with a tool release: <a href="https://github.com/thalpius/Microsoft-Defender-for-Identity-Encrypted-Password" target="_blank">Microsoft-Defender-for-Identity-Encrypted-Password</a>.</li>
<li><a href="https://windows-internals.com/an-end-to-kaslr-bypasses/" target="_blank">An End to KASLR Bypasses?</a>. The new THREATINT_PROCESS_SYSCALL_USAGE ETW event coming to Windows 11 23H2 might make API based kernel address leaks, VM detection, and hardware persistence more difficult to get away with undetected.</li>
<li><a href="https://www.zerodayinitiative.com/blog/2022/11/22/cve-2022-40300-sql-injection-in-manageengine-privileged-access-management" target="_blank">CVE-2022-40300: SQL Injection in ManageEngine Privileged Access Management</a>. "A remote authenticated attacker can exploit the vulnerability by sending a crafted request to the target server. Successful exploitation could lead to arbitrary SQL code execution in the security context of the database service, which runs with SYSTEM privileges."</li>
<li><a href="https://jhalon.github.io/chrome-browser-exploitation-2/" target="_blank">Chrome Browser Exploitation, Part 2: Introduction to Ignition, Sparkplug and JIT Compilation via TurboFan</a>. Another meaty post on Chrome internals and exploitation - the best browser exploit series since Connor McGarr's posts on <a href="https://connormcgarr.github.io/type-confusion-part-1/" target="_blank">Edge exploitation</a>.</li>
<li><a href="https://redhuntlabs.com/blog/analysing-misconfigured-firebase-apps-a-tale-of-unearthing-data-breaches-wave-10.html" target="_blank">Analysing Misconfigured Firebase Apps: A Tale of Unearthing Data Breaches (Wave 10)</a>. Back in the day I worked on an app with a firebase backend and the permission model was non-trivial. Not surprised this research showed that 20% of tested firebase instances exposed data. Want to try your hand at it? Check out <a href="https://github.com/securebinary/firebaseExploiter" target="_blank">firebaseExploiter</a>.</li>
<li><a href="https://www.fortinet.com/blog/threat-research/debugging-net-malware-in-a-multi-stage-malware-deployment" target="_blank">Tips and Tricks: Debugging .NET Malware in a Multi-Stage Malware Deployment</a>. .NET may be easy to decompile but it can still be tricky to trace a mutli-stage dropper all the way back.</li>
<li><a href="https://www.trustedsec.com/blog/the-art-of-bypassing-kerberoast-detections-with-orpheus/" target="_blank">The Art of Bypassing Kerberoast Detections with Orpheus</a>. Kerberoasting becomes fully customizable with the <a href="https://github.com/trustedsec/orpheus" target="_blank">orpheus</a> tool. Beware of honeySPNs, but otherwise, targeted-roast away!</li>
<li><a href="https://wojciechregula.blog/post/macos-sandbox-escape-via-terminal/" target="_blank">macOS Sandbox Escape vulnerability via Terminal</a>. One ENV variable could be set to escape the sandbox on macOS!</li>
<li><a href="https://blog.karims.cloud/2022/11/26/yet-another-azure-vm-persistence.html" target="_blank">Yet Another Azure VM Persistence Using Bastion Shareable Links</a>. Convenient.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://sapling-scm.com/" target="_blank">Sapling: A Scalable, User-Friendly Source Control System</a>. Meta open sourced their in house version control system. Don't worry, it's written in Rust.</li>
<li><a href="https://github.com/enkomio/BrokenFlow" target="_blank">BrokenFlow</a> A simple PoC to invoke an encrypted shellcode by using an hidden call.</li>
<li><a href="https://github.com/wavvs/nanorobeus" target="_blank">nanorobeus</a> COFF file (BOF) for managing Kerberos tickets.</li>
<li><a href="https://github.com/chronicle/GCTI/tree/main/YARA/CobaltStrike" target="_blank">GCTI CobaltStrike rules</a>. 165 yara rules for CobaltStrike. More info <a href="https://cloud.google.com/blog/products/identity-security/making-cobalt-strike-harder-for-threat-actors-to-abuse" target="_blank">here</a>.</li>
<li><a href="https://github.com/Coldzer0/ReverseSock5Proxy" target="_blank">ReverseSock5Proxy</a> A tiny Reverse Sock5 Proxy written in C.</li>
<li><a href="https://github.com/ironmansoftware/psmsi" target="_blank">psmsi</a> Create MSIs using PowerShell.</li>
<li><a href="https://github.com/ShadowMccc/MemoryEvasion" target="_blank">MemoryEvasion</a> A Cobalt Strike memory evasion loader for redteamers.</li>
<li><a href="https://github.com/H4de5-7/geacon_pro" target="_blank">geacon_pro</a> A cross-platform Cobalt Strike Beacon written in Go, supports 4.1+.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/primait/nuvola" target="_blank">nuvola</a> is a tool to dump and perform automatic and manual security analysis on AWS environments configurations and services using predefined, extensible and custom rules created using a simple Yaml syntax.</li>
<li><a href="https://ofrak.com/" target="_blank">ofrak</a> is a binary analysis and modification platform that combines the ability to unpack, analyze, modify, and repack binaries.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 421 (+0)</p>
<p>Blogs monitored: 328 (+1)</p>
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
