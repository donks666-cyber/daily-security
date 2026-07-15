Title: Last Week in Security (LWiS) - 2025-02-17
Date: 2025-02-17 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-02-17
Author: Erik
Summary: PAN-OS auth bypass (<a href="https://x.com/hash_kitten" target="_blank">@hash_kitten</a>), Outlook drafts as C2 (<a href="https://x.com/elasticseclabs" target="_blank">@elasticseclabs</a>), Ludus powered SocGholish analysis (<a href="https://x.com/RussianPanda9xx" target="_blank">@RussianPanda9xx</a>), kernel UAF (<a href="https://x.com/h0mbre_" target="_blank">@h0mbre_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-02-10 to 2025-02-17.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2025/02/doges-gov-site-lampooned-as-coders-quickly-realize-it-can-be-edited-by-anyone/" target="_blank">DOGE’s .gov site lampooned as coders quickly realize it can be edited by anyone</a> - "So far, it's clear that DOGE has gained access to data systems at the Centers for Medicare and Medicaid Services, the US Agency for International Development, the Department of Veterans Affairs, the Department of Education, and the US Treasury. And most recently, DOGE got software approval to potentially transfer 'vast amounts of data' out of the Department of Labor’s systems." What a time to be a foreign cyber actor. Perhaps DOGE doesn't know that <a href="https://www.usaspending.gov/" target="_blank">USA Spending</a> already exists and even has an <a href="https://api.usaspending.gov/" target="_blank">API</a> and full <a href="https://onevoicecrm.my.site.com/usaspending/s/database-download" target="_blank">database downloads</a>? Archive.org has captures of the defacement (may take a few seconds to load): <a href="https://web.archive.org/web/20250214092653/https://doge.gov/workforce?orgId=7cd300eb-cf3f-47f5-90f1-9e66a8bc8d07" target="_blank">Example 1</a>, <a href="https://web.archive.org/web/20250214103459/https://doge.gov/workforce?orgId=1" target="_blank">Example 2</a>.</li>
</ul>
<ul><li><a href="https://app.presspool.ai/engage/62" style="color: #3bd267;" target="_blank">Detect shadow AI hidden in the apps you build or use</a> <span class="m-label m-flat m-success">Sponsored</span> - NowSecure offers a comprehensive suite of automated mobile app security and privacy testing solutions, penetration testing, and training services to reduce risk. Trusted by many of the world’s most demanding organizations, NowSecure protects millions of app users across banking, insurance, high tech, retail, healthcare and government. <a href="https://app.presspool.ai/engage/62" style="color: #3bd267;" target="_blank">Talk to a specialist to understand your AI risks.</a></li></ul></section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.youtube.com/watch?v=F5m2JxplnXk" target="_blank">Modding the Gulf of Mexico Back</a> - Regardless of your feelings on the name of a body of water, this video has some great client-side web hacking.</li>
<li><a href="https://dl.acm.org/doi/pdf/10.1145/3658644.3690189" target="_blank">[PDF] SysBumps: Exploiting Speculative Execution in System Calls for Breaking KASLR in macOS for Apple Silicon</a> - Speculative execution comes for Apple Silicon. Patched in macOS 15.2. PoC: <a href="https://github.com/koreacsl/SysBumps" target="_blank">SysBumps</a>.</li>
<li><a href="https://www.assetnote.io/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os" target="_blank">Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)</a> - The complexity of nginx reverse proxying to an Apache server, which then internally redirects to itself, combined with a simple authentication on/off header that is fully trusted lead to an authentication bypass via path confusion. While each individual part of the chain is "secure" the way they are combined leads to a critical vulnerability.</li>
<li><a href="https://trac-labs.com/dont-ghost-the-socgholish-ghostweaver-backdoor-574154dd9983" target="_blank">Don’t Ghost the SocGholish: GhostWeaver Backdoor</a> - Fake update popups deliver formstealer malware. <a href="https://ludus.cloud" target="_blank">Ludus</a> was <a href="https://x.com/RussianPanda9xx/status/1890524372743381328" target="_blank">used in the analysis</a>. Curious how <a href="https://docs.ludus.cloud/docs/enterprise/" target="_blank">Ludus Enterprise</a> can help your analysts? Get in touch!</li>
<li><a href="https://www.elastic.co/security-labs/finaldraft" target="_blank">You've Got Malware: FINALDRAFT Hides in Your Drafts</a> - A solid malware tear down, with the interesting feature being C2 via email drafts in Outlook online using the Microsoft Graph API using an embedded token (not the compromised user's account). "3rd party C2" is heating up as network defenders get better.</li>
<li><a href="https://brutecat.com/articles/leaking-youtube-emails" target="_blank">Leaking the email of any YouTube user for $10,000</a> - Some very creative hacking here. Setting the recording title to 2.5 million characters so the notification never got sent was great.</li>
<li><a href="https://h0mbre.github.io/Patch_Gapping_Google_COS/" target="_blank">Patch-Gapping the Google Container-Optimized OS for $0</a> - Detailed use-after-free exploit in the Linux kernel with a proof of concept. I believe this is <a href="https://nvd.nist.gov/vuln/detail/CVE-2025-21700" target="_blank">CVE-2025-21700</a>.</li>
<li><a href="https://neodyme.io/en/blog/com_hijacking_3/#vulnerability-1-leveraging-file-deletion-for-lpe" target="_blank">The Key to COMpromise - Downloading a SYSTEM shell, Part 3</a> - More COM hacking, this time against Webroot Endpoint Protect and Checkpoint Harmony to gain SYSTEM privileges.</li>
<li><a href="https://blog.quarkslab.com/first-analysis-of-apples-usb-restricted-mode-bypass-cve-2025-24200.html" target="_blank">First analysis of Apple's USB Restricted Mode bypass (CVE-2025-24200)</a> - Looks like some older protocols allowed for the simple (?) bypass of USB restricted mode on iOS &lt; 18.3.1? Does the user have to have "Switch Control" enabled for this to work? The Apple announcement makes it sound like that is not the case.</li>
</ul>
<ul><li><a href="https://app.presspool.ai/engage/75" style="color: #3bd267;" target="_blank">2025 IT Risk and Compliance Benchmark Report release</a> <span class="m-label m-flat m-success">Sponsored</span> - Hyperproof, a trusted platform for operationalizing compliance and risk management, has released its 6th annual IT Risk and Compliance Benchmark Report. Based on insights from 1,000 IT and GRC professionals, the in-depth report contains insights on trends shaping the GRC space in 2025. <a href="https://app.presspool.ai/engage/75" style="color: #3bd267;" target="_blank">See the report.</a></li></ul></section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/decoder-it/ChgPass" target="_blank">ChgPass</a> - is a Windows standalone executable tool that allows you to change the password of user/computer accounts in Active Directory (AD) via MS-SAMR protocol. This tool can be used when you have the necessary permissions on the objects but need a simple way to set passwords using a standalone exe command line. More info: <a href="https://decoder.cloud/2025/02/11/changing-windows-passwords-in-the-most-complex-way/" target="_blank">Changing Windows Passwords in the Most Complex Way</a>.</li>
<li><a href="https://github.com/synacktiv/captaincredz" target="_blank">captaincredz</a> - CaptainCredz is a modular and discreet password-spraying tool.</li>
<li><a href="https://github.com/C5Hackr/ARM64_AmsiPatch" target="_blank">ARM64_AmsiPatch</a> - With the rise of ARM64 as an emerging architecture for Windows on ARM devices, there is an increasing need to understand and adapt low-level techniques traditionally used on x86_64 systems to this new platform. This repository demonstrates how AMSI (Antimalware Scan Interface) patching can be translated to ARM64, showcasing the fundamental differences and similarities in opcode manipulation between x86_64 and ARM64 architectures.</li>
<li><a href="https://github.com/CodeXTF2/WebcamBOF" target="_blank">WebcamBOF</a> - Webcam capture capability for Cobalt Strike as a BOF, with in-memory download options.</li>
<li><a href="https://github.com/sensepost/susinternals" target="_blank">susinternals</a> - A python implementation of PSExec's native service implementation.</li>
<li><a href="https://github.com/Chocapikk/wpprobe" target="_blank">wpprobe</a> - A fast WordPress plugin enumeration tool.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/KingKDot/PowerCrypt" target="_blank">PowerCrypt</a> - The best powershell obfuscator ever made.</li>
<li><a href="https://github.com/logangoins/Stifle" target="_blank">Stifle</a> - .NET Post-Exploitation Utility for Abusing Explicit Certificate Mappings in ADCS.</li>
<li><a href="https://github.com/ashirt-ops/ashirt-server?tab=readme-ov-file" target="_blank">ashirt-server</a> - Adversary Simulators High-Fidelity Intelligence and Reporting Toolkit.</li>
<li><a href="https://github.com/ashirt-ops/ashirt" target="_blank">ashirt</a> - It records your screenshots and code, then lets you upload to ASHIRT.</li>
<li><a href="https://github.com/ashirt-ops/aterm" target="_blank">aterm</a> - It records your terminal, then lets you upload to ASHIRT.</li>
<li><a href="https://github.com/x86matthew/Playable3DMaze" target="_blank">Playable3DMaze</a> - A playable version of Microsoft's old 3DMaze screensaver from Windows 9x.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 444 (+0)</p>
<p>Blogs monitored: 405 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
