Title: Last Week in Security (LWiS) - 2025-04-28
Date: 2025-04-28 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-04-28
Author: Erik
Summary: TTTracer unmasks sleep obfs (<a href="https://x.com/felixm_pw/status/1916240199266320832" target="_blank">@felixm_pw</a>), GitHub spoofing (<a href="https://x.com/pfiatde" target="_blank">@pfiatde</a>), Synology RCE (<a href="https://x.com/ret2systems" target="_blank">@ret2systems</a>), netify scraper (<a href="https://x.com/Jhaddix" target="_blank">@Jhaddix</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-04-21 to 2025-04-28.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.kali.org/blog/new-kali-archive-signing-key/" target="_blank">A New Kali Linux Archive Signing Key</a> - "Bad news for Kali Linux users! In the coming day(s), apt update is going to fail for pretty much everyone out there... We lost access to the signing key of the repository, so we had to create a new one." Many professionals use this operating system with elevated privileges in customer networks. Update your signing key, or use the new 2025.1c installer.</li>
<li><a href="https://windscribe.com/blog/windscribe-greek-court-case/" target="_blank">That one time I got charged with a criminal offense on behalf of a Windscribe user</a> - Windscribe VPN defends it's "no logs" claim in court. Mullvad has done this before in 2023, as has Signal.</li>
<li><a href="https://arstechnica.com/gadgets/2025/04/android-phones-will-soon-reboot-themselves-after-sitting-unused-for-3-days/" target="_blank">Android phones will soon reboot themselves after sitting unused for 3 days</a> - iOS was the first major mobile OS to do it, now Android follows suit.</li>
</ul>
<ul><li><a href="https://app.presspool.ai/engage/179" style="color: #3bd267;" target="_blank">MFA for machines</a> <span class="m-label m-flat m-success">Sponsored</span> - Aembit, the non-human identity and access management company, is announcing the launch of its Identity Federation Hub at RSAC. Designed for DevOps and security teams, this new capability eliminates the operational and security risks of long-lived secrets by enabling seamless workload identity federation across clouds and services – without forcing developers to write custom auth logic. <a href="https://app.presspool.ai/engage/179" style="color: #3bd267;" target="_blank">Learn more about Aembit.</a></li></ul></section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://denniskniep.github.io/posts/09-device-code-phishing/" target="_blank">Phishing despite FIDO, leveraging a novel technique based on the Device Code Flow</a> - Phishing resistant multifactor authentication (i.e. hardware tokens) can be bypassed if Device Code Flow is enabled in Azure Entra, even if the hardware token is the only "allowed" authentication method. This novel extension of the technique uses a shadow browser and instantly redirects the victim to legitimate site (login.microsoft.com). The <a href="https://gist.github.com/user-attachments/assets/bf6d1c2d-7199-4394-824d-e6f57e8136a2" target="_blank">demo</a> is pretty wild. PoC is <a href="https://github.com/denniskniep/DeviceCodePhishing" target="_blank">DeviceCodePhishing</a>. <a href="https://github.com/nromsdahl/squarephish2" target="_blank">squarephish2</a> is another Entra device code phishing tool released last week focused on QR codes.</li>
<li><a href="https://blog.felixm.pw/rude_awakening.html" target="_blank">Rude Awakening: Unmasking Sleep Obfuscation With TTTracer</a> - "Traditional memory dumps are ineffective against implants leveraging sleep obfuscation since you'll most likely be dumping junk data. However, since tttracer.exe is taking a capture of a full execution, if we capture for long enough the decrypted implant should be recorded." However, you need to be suspicious of a process before you can use this technique, so its more of an incident response task than something you can find "unknown bad" with. However, tttracer.exe is preinstalled on Windows, which is nice.</li>
<li><a href="https://www.darknavy.org/blog/fatal_vulnerabilities_compromising_dji_control_devices/" target="_blank">Fatal Vulnerabilities Compromising DJI Control Devices</a> - Five vulnerabilities combine for a total takedown of DJI's RC Plus controller.</li>
<li><a href="https://badoption.eu/blog/2025/04/25/github.html" target="_blank">Having fun with Github</a> - A few different techniques to spoof Github commits, but the most fun is using issues to send emails from Github with your content - ripe for a nice targeted phishing campaign.</li>
<li><a href="https://www.romainthomas.fr/post/25-04-windows-arm64-qbdi-fuzzing/" target="_blank">Fuzzing Windows ARM64 closed-source binary</a> - Window is slowly moving to ARM, and the tooling is following right along. <a href="https://github.com/romainthomas/windows-arm64-qbdi-fuzzing" target="_blank">windows-arm64-qbdi-fuzzing</a> is the repo that goes with the post.</li>
<li><a href="https://snoolie.gay/blog/CVE-2024-27876" target="_blank">libAppleArchive: Arbitrary File Write</a> - A Gatekeeper bypass for macOS, so long as you know the target's $TMPDIR. <a href="https://github.com/0xilis/CVE-2024-27876" target="_blank">CVE-2024-27876</a> is the proof of concept.</li>
<li><a href="https://decoder.cloud/2025/04/24/from-ntlm-relay-to-kerberos-relay-everything-you-need-to-know/" target="_blank">From NTLM relay to Kerberos relay: Everything you need to know</a> - As NTLM is slowly phased out, Kerberos will become the standard authentication method in Windows networks. While Kerberos by itself does not prevent relay attacks (signing and channel binding do that), it does make relaying a bit more complicated. This post does a good job explaining how Kerberos relaying works.</li>
<li><a href="https://modexp.wordpress.com/2025/04/27/beacon-object-files-vs-tiny-executables/" target="_blank">Beacon Object Files vs Tiny EXE Files</a> - While Beacon Object Files (BOFs) have become the standard unit of "technique execution" among red teams, what if tiny EXEs were introduced instead of BOFs. Debugging would be a lot easier, that's for sure.</li>
<li><a href="https://blog.ret2.io/2025/04/23/pwn2own-soho-2024-diskstation/" target="_blank">Exploiting the Synology DiskStation with Null-byte Writes</a> - RET2 Systems write ups are always worth the read. This time they use a null byte write to get root on a Synology DS1823xs+ NAS.</li>
<li><a href="https://labs.watchtowr.com/fire-in-the-hole-were-breaching-the-vault-commvault-remote-code-execution-cve-2025-34028/" target="_blank">Fire In The Hole, We’re Breaching The Vault - Commvault Remote Code Execution (CVE-2025-34028)</a> - At this point, if I was a company and saw watchTowr in my web logs downloading my product, I don't think I would sleep very well at night. Another "hmm what is this" to remote code execution journey - memes included. <a href="https://github.com/watchtowrlabs/watchTowr-vs-Commvault-PreAuth-RCE-CVE-2025-34028?ref=labs.watchtowr.com" target="_blank">watchTowr-vs-Commvault-PreAuth-RCE-CVE-2025-34028</a> is the PoC.</li>
<li><a href="https://williamknowles.io/net-gac-and-nic-hijacking-for-lateral-movement/" target="_blank">.NET GAC and NIC hijacking for lateral movement</a> - This is one of the coolest lateral movement techniques I've read about in a long time. The ability to decouple the upload from the execution will make this very tricky to detect.</li>
<li><a href="https://blog.zsec.uk/common-tool-errors-kerberos/" target="_blank">Common Tool Errors - Kerberos</a> - A good post to keep handy when doing anything Kerberos related.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/harishsg993010/damn-vulnerable-MCP-server" target="_blank">damn-vulnerable-MCP-server</a> - Damn Vulnerable MCP Server.</li>
<li><a href="https://github.com/denniskniep/DeviceCodePhishing" target="_blank">DeviceCodePhishing</a> - This is a novel technique that leverages the well-known Device Code phishing approach. It dynamically initiates the flow when the victim opens the phishing link and instantly redirects them to the authentication page. Capable of bypassing FIDO, even if FIDO is the only authentication method available to the victim.</li>
<li><a href="https://github.com/nromsdahl/squarephish2" target="_blank">squarephish2</a> is an advanced phishing tool that uses a technique combining the OAuth Device Code authentication flow and QR codes.</li>
<li><a href="https://github.com/andreisss/Ghosting-AMSI" target="_blank">Ghosting-AMSI</a> - AMSI Bypass via RPC Hijack (NdrClientCall3) This technique exploits the COM-level mechanics AMSI uses when delegating scan requests to antivirus (AV) providers through RPC.</li>
<li><a href="https://www.netspi.com/blog/technical-blog/web-application-pentesting/getting-shells-at-terminal-velocity-with-wopper/" target="_blank">Getting Shells at Terminal Velocity with Wopper</a> - Automate the use of malicious plugins to get shells on Wordpress with Wopper. <a href="https://github.com/NetSPI/wopper" target="_blank">wopper</a> is the GitHub.</li>
<li><a href="https://github.com/dagowda/PrimeEncryptor" target="_blank">PrimeEncryptor</a> - PrimeEncryptor is a flexible Dynamic Shellcode Encryptor designed to generate encrypted shellcode using multiple encryption techniques.</li>
<li><a href="https://github.com/Arcanum-Sec/Scopify" target="_blank">Scopify</a> - Scopify is a Python command-line tool designed for penetration testers and bug bounty hunters to quickly gather and analyze infrastructure information (CDN, Hosting, SaaS) for a target company by scraping netify.ai. Developed by <a href="https://x.com/Jhaddix" target="_blank">@Jhaddix</a> and Arcanum Information Security.</li>
<li><a href="https://github.com/thatwinterquiet/logon_monitor" target="_blank">logon_monitor</a> - A BOF to regularly check for active users on a target.</li>
<li><a href="https://github.com/dest-3/Chronos" target="_blank">Chronos</a> - Time-Based Detection and Response for Safety-Critical Real-Time Embedded Systems - EDR Kernel Extension for FreeRTOS.</li>
<li><a href="https://github.com/githubesson/paradox" target="_blank">paradox</a> - macos stealer poc.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/chainreactors/malice-network" target="_blank">malice-network</a> - Next Generation C2 Framework.</li>
<li><a href="https://github.com/chainreactors/rem-community" target="_blank">rem-community</a> - proxy/tunnel everything for red team!.</li>
<li><a href="https://github.com/aniqfakhrul/powerview.py" target="_blank">powerview.py</a> - Just another Powerview alternative but on steroids.</li>
<li><a href="https://github.com/pad-ws/pad.ws" target="_blank">pad.ws</a> - Whiteboard as an IDE, draw and code in your browser.</li>
<li><a href="https://github.com/0xPrimo/KMDllInjector" target="_blank">KMDllInjector</a> - kernel-mode DLL Injector.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 451 (+1)</p>
<p>Blogs monitored: 412 (+2)</p>
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
