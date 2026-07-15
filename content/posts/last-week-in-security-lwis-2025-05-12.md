Title: Last Week in Security (LWiS) - 2025-05-12
Date: 2025-05-12 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-05-12
Author: Erik
Summary: SysAid RCE (<a href="https://x.com/SinSinology" target="_blank">@SinSinology</a> + <a href="https://x.com/watchTowrcyber" target="_blank">@watchtowrcyber</a>), defendnot (<a href="https://x.com/es3n1n" target="_blank">@es3n1n</a>), iOS widget hacks (<a href="https://x.com/brycebostwick1" target="_blank">@brycebostwick1</a>), Sword of Secrets (<a href="https://x.com/GiliYankovitch" target="_blank">@GiliYankovitch</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-05-05 to 2025-05-12.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2025/05/using-ai-to-stop-tech-support-scams-in.html" target="_blank">Using AI to stop tech support scams in Chrome</a> - Google is now shipping an LLM inside of Chrome to determine if never before seen sites that have "specific triggers" like using the keyboard lock API are phishing pages. Only users with Enhanced Protection mode enabled send the LLM output to Google's Safe Browsing servers.</li>
<li><a href="https://techcrunch.com/2025/05/09/florida-bill-requiring-encryption-backdoors-for-social-media-accounts-has-failed/" target="_blank">Florida bill requiring encryption backdoors for social media accounts has failed</a> - Stay vigilant. They'll be back.</li>
<li><a href="https://www.youtube.com/@specterops/videos" target="_blank">[YouTube] SpecterOps</a> - SpecterOps Con 2025 (SO-CON) videos are now available!</li>
<li><a href="https://www.crowdsupply.com/nyx-software-security-solutions/sword-of-secrets" target="_blank">Sword of Secrets - A new open-source hardware CTF challenge</a> - This upcoming hardware CTF looks promising. There is code already on <a href="https://github.com/gili-yankovitch/SwordOfSecrets" target="_blank">GitHub</a>.</li>
<li><a href="https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/sts-recommendations-for-windows-server" target="_blank">Microsoft now recommends disabling Secure Time Seeding</a> - It seemed like a good idea to pull time data from SSL handshakes, but it turns out lots of implementations fill the time field with random data (i.e. OpenSSL) which can cause dates to swing wildly on Windows. This can cause serious issues with things like SQL servers. <a href="https://ludus.cloud/" target="_blank">Ludus</a> will disable STS on all windows templates in the next release.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.synacktiv.com/en/publications/open-source-toolset-of-an-ivanti-csa-attacker" target="_blank">Open-Source Toolset of an Ivanti CSA Attacker</a> - The Ivanti hackers used some open source tooling like <a href="https://github.com/zema1/suo5" target="_blank">suo5</a>, <a href="https://github.com/EddieIvan01/iox" target="_blank">iox</a>, and <a href="https://github.com/Ridter/atexec-pro" target="_blank">atexec-pro</a> which Maxence Fossat and team have written some good detections for.</li>
<li><a href="https://googleprojectzero.blogspot.com/2025/05/breaking-sound-barrier-part-i-fuzzing.html" target="_blank">Breaking the Sound Barrier Part I: Fuzzing CoreAudio with Mach Messages</a> - Knowledge-driven fuzzing leds to a high impact bug in macOS.</li>
<li><a href="https://github.com/google/security-research/blob/master/pocs/linux/kernelctf/CVE-2024-26809_lts_cos/docs/exploit.md" target="_blank">Exploit detail about CVE-2024-26809</a> - A nftables use after free exploit in Linux &gt;= 6.1-rc1 and &gt;= 5.15.54 allows for local privilege escalation. Exploit: <a href="https://github.com/google/security-research/blob/master/pocs/linux/kernelctf/CVE-2024-26809_lts_cos/exploit/lts-6.1.79/exploit.c" target="_blank">Linux 6.1.79</a>.</li>
<li><a href="https://blog.es3n1n.eu/posts/how-i-ruined-my-vacation/" target="_blank">How I ruined my vacation by reverse engineering WSC</a> - <a href="https://x.com/es3n1n" target="_blank">@es3n1n</a> is the author of <a href="https://github.com/es3n1n/no-defender" target="_blank">no-defender</a> which used an Avast antivirus binary to disable windows defender. Now they are back with a pure C++ version that doesn't require any external binaries.</li>
<li><a href="https://labs.watchtowr.com/sysowned-your-friendly-rce-support-ticket/" target="_blank">SysOwned, Your Friendly Support Ticket - SysAid On-Premise Pre-Auth RCE Chain (CVE-2025-2775 And Friends)</a> - "disclosing vulnerability research that allowed us to gain pre-authenticated Remote Command Execution against yet another enterprise-targeting product - specifically, SysAid On-Premise." If I were an enterprise cybersecurity product team, I would just hire watchTowr to save myself the public posting of exploits at this point.</li>
<li><a href="https://mrbruh.com/asusdriverhub/" target="_blank">One-Click RCE in ASUS’s Preinstalled Driver Software</a> - Hell hath no fury like a curious hacker. The worst part is the ASUS WiFi still didn't work after all that.</li>
<li><a href="https://scrapco.de/blog/fuzzing-windows-defender-with-loadlibrary-in-2025.html" target="_blank">Fuzzing Windows Defender with loadlibrary in 2025</a> - Fuzzing Windows components with on Linux is still a bit of magic, but this post explored using <a href="https://github.com/AFLplusplus/AFLplusplus" target="_blank">AFLplusplus</a> and <a href="https://github.com/google/honggfuzz" target="_blank">honggfuzz</a> along with a <a href="https://github.com/v-p-b/loadlibrary/tree/x64_waffle" target="_blank">forked loadlibrary</a> to make it work.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Thunter-HackTeam/EvilentCoerce" target="_blank">EvilentCoerce</a> - A practical NTLM relay attack using the MS-EVEN RPC protocol and antivirus-assisted coercion.</li>
<li><a href="https://github.com/sudonoodle/BOF-entra-authcode-flow" target="_blank">BOF-entra-authcode-flow</a> - Beacon Object File (BOF) to obtain Entra tokens via authcode flow. Details in the blog post: <a href="https://www.infosecnoodle.com/p/obtaining-microsoft-entra-refresh" target="_blank">Obtaining Microsoft Entra Refresh Tokens via Beacon</a>.</li>
<li><a href="https://github.com/es3n1n/defendnot" target="_blank">defendnot</a> - An even funnier way to disable windows defender. (through WSC api).</li>
<li><a href="https://github.com/hellofromdaniel/nyxppl/" target="_blank">nyxppl</a> - Windows Protected Process Light toggle tool — dynamically finds offsets and patches EPROCESS using RTCore64.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/CroodSolutions/AutoPwnKey" target="_blank">AutoPwnKey</a> - AutoPwnKey is a red teaming framework and testing tool using AutoHotKey (AHK), which at the time of creation proves to be quite evasive. It is our hope that this tool will be useful to red teams over the short term, while over the long term help AV/EDR vendors improve how they handle AHK scripts.</li>
<li><a href="https://www.youtube.com/watch?v=NdJ_y1c_j_I" target="_blank">[YouTube] Apple’s Widget Backdoor</a> - Bryce is a hacker in the true sense of the word. "A hacker is a person skilled in information technology who achieves goals by non-standard means." He hacks with the clock and timer APIs as well as fonts to create fluid animations in widgets, which Apple doesn't allow, except for their own clock app of course. He's also a great presenter, even if you don't care about iOS widgets at all the video is entertaining and interesting. Code: <a href="https://github.com/brycebostwick/WidgetAnimation/" target="_blank">WidgetAnimation</a> - Proof of concept for Animated iOS Widgets using Public APIs.</li>
<li><a href="https://github.com/cipher387/API-s-for-OSINT" target="_blank">API-s-for-OSINT</a> - List of API's for gathering information about phone numbers, addresses, domains etc.</li>
<li><a href="https://github.com/kernelwernel/VMAware" target="_blank">VMAware</a> - VM detection library and tool.</li>
<li><a href="https://github.com/Maldev-Academy/LsassHijackingViaReg" target="_blank">LsassHijackingViaReg</a> - Injecting DLL into LSASS at boot.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 452 (+1)</p>
<p>Blogs monitored: 416 (+3)</p>
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
