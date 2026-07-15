Title: Last Week in Security (LWiS) - 2024-01-30
Date: 2024-01-30 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-01-30
Author: Erik
Summary: Fastly to block domain fronting 🔜, EDR bypass via VEH (<a href="https://twitter.com/VirtualAllocEx" target="_blank">@VirtualAllocEx</a>), BOFHound enhancements (<a href="https://twitter.com/Tw1sm" target="_blank">@Tw1sm</a>), Frameless BITB (<a href="https://twitter.com/waelmas01" target="_blank">@waelmas01</a>), Asus ndays (<a href="https://twitter.com/suidpit" target="_blank">@suidpit</a> + <a href="https://twitter.com/Th3Zer0" target="_blank">@Th3Zer0</a>), and more!

<aside class="m-note m-success">
<h3>Sponsorship</h3>
<p>LWiS is fully independent! If you are interested in sponsoring a post and getting your content in front of technical cybersecurity professionals actively looking for new things, please reach out to blog (at) badsectorlabs.com</p>
<p>Reminder: Newsletter <a href="https://subscribe.badsectorlabs.com/subscription/form" target="_blank">Sign up</a> is live!</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-01-22 to 2024-01-30.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.thestack.technology/how-russia-hacked-microsoft-ms-graph/" target="_blank">How Russian spooks hacked Microsoft, the gap in its “morally indefensible” response, and what CISOs can learn from the attack</a> - Fallout from the story that broke last week. We could see some changes coming to the Microsoft Graph API in the near future.</li>
<li><a href="https://www.cobaltstrike.com/blog/introducing-the-mutator-kit-creating-object-file-monstrosities-with-sleep-mask-and-llvm" target="_blank">Introducing the Mutator Kit: Creating Object File Monstrosities with Sleep Mask and LLVM</a> - Cobalt Strike team has introduced the mutator kit, which uses an LLVM obfuscator to break in-memory YARA scanning of the sleep mask. This continues their "Evasion through flexibility" strategy.</li>
<li><a href="https://portswigger.net/polls/top-10-web-hacking-techniques-2023" target="_blank">Top 10 web hacking techniques of 2023</a> - We look forward to this list every year. Cast your votes!</li>
<li><a href="https://techcommunity.microsoft.com/t5/windows-it-pro-blog/wmi-command-line-wmic-utility-deprecation-next-steps/ba-p/4039242" target="_blank">WMI command line (WMIC) utility deprecation: Next steps</a> - For the whoami.exe crew (thats not you of course), wmic.exe is being retired! WMI is still available via powershell.</li>
<li><a href="https://techcommunity.microsoft.com/t5/windows-server-news-and-best/introducing-windows-server-2025/ba-p/4026374" target="_blank">Introducing Windows Server 2025!</a> - Yet we're still seeing 2003, 2008, and 2012 in almost every engagement? Sweet!</li>
<li><a href="https://lists.torproject.org/pipermail/anti-censorship-team/2023-October/000328.html" target="_blank">Fastly to block domain fronting in February 2024</a>. All good things must come to an end. Fastly was by far the largest CDN that supported fronting. Now it's just the smaller players. See <a href="https://arxiv.org/pdf/2310.17851v3.pdf" target="_blank">[PDF] Measuring CDNs susceptible to Domain Fronting</a>.</li>
<li><a href="https://www.wyden.senate.gov/news/press-releases/wyden-releases-documents-confirming-the-nsa-buys-americans-internet-browsing-records-calls-on-intelligence-community-to-stop-buying-us-data-obtained-unlawfully-from-data-brokers-violating-recent-ftc-order" target="_blank">Wyden Releases Documents Confirming the NSA Buys Americans' Internet Browsing Records</a>. Did you read the terms of your ISP contract? Spoiler: they told you they are going to sell all your netflow and DNS to whomever they want. Remember: <a href="https://www.justsecurity.org/10318/video-clip-director-nsa-cia-we-kill-people-based-metadata/" target="_blank">“We Kill People Based on Metadata”</a>.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://swarm.ptsecurity.com/bypassing-browser-tracking-protection-for-cors-misconfiguration-abuse/" target="_blank">Bypassing browser tracking protection for CORS misconfiguration abuse</a> Blog that talks about bypassing browser tracking protection through CORS misconfiguration abuse, explaining the CORS web protocol, detailing specific HTTP headers used in CORS, and highlights vulns associated with misconfigurations, with a focus on Access-Control-Allow-Credentials.</li>
<li><a href="https://www.cryptic.red/post/shipping-your-private-key-cve-2023-43870-paxton-do-a-lenovo" target="_blank">Shipping your Private Key - CVE-2023-43870, Paxton do a Lenovo</a> - A vuln (CVE-2023-43870) in Paxton Access's Net2 software, revealing that the default installation of Net2 includes a vulnerable certificate authority (CA) key, allowing an attacker to intercept HTTPS traffic on machines running Net2 or those that installed the CA as instructed by the Web API.</li>
<li><a href="https://redops.at/en/blog/leveraging-fake-dlls-guard-pages-and-veh-for-enhanced-detection" target="_blank">Leveraging Fake DLLs, Guard Pages, and VEH for Enhanced Detection</a> - Unconventional but very interesting detection mechanism used in conjunction with EDR, based on a combination of process environment block (PEB) modification, the use of fake DLLs and guard pages, and the use of vectored exception handling.</li>
<li><a href="https://redops.at/en/blog/syscalls-via-vectored-exception-handling" target="_blank">Syscalls via Vectored Exception Handling</a> - Executing the native APIs used in the context of loading shellcode using syscalls via Vectored Exception Handling (Vectored Syscalls). <a href="https://twitter.com/passthehashbrwn/status/1749511433161732493" target="_blank">VEH has some haters</a>.</li>
<li><a href="https://www.horizon3.ai/cve-2024-0204-fortra-goanywhere-mft-authentication-bypass-deep-dive/" target="_blank">CVE-2024-0204: Fortra GoAnywhere MFT Authentication Bypass Deep-Dive</a> - Fortras (yes the same Fortra that sells Cobalt Strike) GoAnywhere MFT product has an auth bypass. PoC for <a href="https://github.com/horizon3ai/CVE-2024-0204" target="_blank">CVE-2024-0204</a> is already out.</li>
<li><a href="https://posts.redteamtacticsacademy.com/macros-unleashed-redefining-red-teaming-with-advanced-macro-strategies-part-2-24552c501da7" target="_blank">Macros Unleashed: Redefining Red Teaming with Advanced Macro Strategies-Part 2</a> - Not very OPSEC friendly but still good references nonetheless. Are macros making a comeback? Maybe they never left for some.</li>
<li><a href="https://redsiege.com/blog/2024/01/graphstrike-developer/" target="_blank">GraphStrike: Anatomy of Offensive Tool Development</a>. The <a href="https://github.com/RedSiege/GraphStrike" target="_blank">GraphStrike</a> tool was in last LWiS, but this blog post wasn't. Enjoy!</li>
<li><a href="https://pushsecurity.com/blog/phishing-microsoft-teams-for-initial-access/" target="_blank">Phishing Microsoft Teams for initial access</a> - Not really news that <a href="https://www.microsoft.com/en-us/security/blog/2023/09/12/malware-distributor-storm-0324-facilitates-ransomware-access/" target="_blank">Teams</a> is being used to delivery payloads/links but this is a good write up with screenshots on how it is done. Discussed last year by BHIS in <a href="https://www.youtube.com/live/z3bMvf4Rh-M?si=Q4yAXQHw-cGK_y-1&amp;t=29025" target="_blank">BSides Orlando 2023</a>.</li>
<li><a href="https://posts.specterops.io/bofhound-session-integration-7b88b6f18423" target="_blank">BOFHound: Session Integration</a>. <a href="https://github.com/coffeegist/bofhound" target="_blank">bofhound</a> has been around for a while but just got some extra powers related to session data and local group data.</li>
<li><a href="https://adepts.of0x.cc/gtbcc-pwned/" target="_blank">A christmas tale: pwning GTB Central Console (CVE-2024-22107 &amp; CVE-2024-22108)</a>. A good run through from ISO download to RCE.</li>
<li><a href="https://www.shielder.com/blog/2024/01/hunting-for-~~un~~authenticated-n-days-in-asus-routers/" target="_blank">Hunting for Unauthenticated n-days in Asus Routers</a>. The use of Qiling to emulate the firmware is neat as they had to emulate nvram for configuration storage.</li>
<li><a href="https://itm4n.github.io/printnightmare-exploitation/" target="_blank">A Practical Guide to PrintNightmare in 2024</a>. PrintNightmare may be a memory, but the core of the issue - printer drivers install as SYSTEM on Windows - hasn't changed. I love these kinds of "work around the problem" hacks. This post is true hacking and even drops some automation (powershell) to help exploit vulnerable scenarios.</li>
<li><a href="https://skii.dev/rook-to-xss/" target="_blank">Rook to XSS: How I hacked chess.com with a rookie exploit</a>. Ah the days of myspace worms. Simpler times.</li>
<li><a href="https://rbf.dev/blog/2024/01/how-apple-accidentally-broke-my-spotify/" target="_blank">How Apple accidentally broke my Spotify client</a>. Not really cybersecurity related, but the level of depth in the investigation was so deep it was basically a vulnerability write up. Impressive. Spoiler: it was DNS (because of course it was).</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/FalconForceTeam/SOAPHound" target="_blank">SOAPHound</a> - This made some noise this week. A custom-developed .NET data collector tool which can be used to enumerate Active Directory environments via the Active Directory Web Services (ADWS) protocol.</li>
<li><a href="https://github.com/REDMED-X/InjectKit" target="_blank">InjectKit</a> -  Modified versions of the Cobalt Strike Process Injection Kit</li>
<li><a href="https://github.com/Cracked5pider/Stardust" target="_blank">Stardust</a> - A modern 64-bit position independent implant template. Came with a good blog if you want to take a look <a href="https://5pider.net/blog/2024/01/27/modern-shellcode-implant-design/" target="_blank">here</a>.</li>
<li><a href="https://grroxy.com/" target="_blank">Grroxy</a> - Another competitor to Burpsuite Pro? <a href="https://caido.io/" target="_blank">Caido</a> is another one that comes to mind.</li>
<li><a href="https://github.com/waelmas/frameless-bitb" target="_blank">Frameless BITB</a> - A new approach to Browser In The Browser (BITB) without the use of iframes, allowing the bypass of traditional framebusters implemented by login pages like Microsoft and the use with Evilginx. Even came with a <a href="https://www.youtube.com/watch?v=p1opa2wnRvg" target="_blank">demo</a>.</li>
<li><a href="https://github.com/rasta-mouse/CsWhispers" target="_blank">CsWhispers</a> - Source generator to add D/Invoke and indirect syscall methods to a C# project.</li>
<li><a href="https://github.com/floesen/EventLogCrasher" target="_blank">EventLogCrasher</a> - Proof of concept for a bug, that allows any user to crash the Windows Event Log service of any other Windows 10/Windows Server 2022 machine on the same domain. The crash occurs in wevtsvc!VerifyUnicodeString when an attacker sends a malformed UNICODE_STRING object to the ElfrRegisterEventSourceW method exposed by the RPC-based EventLog Remoting Protocol.</li>
<li><a href="https://github.com/florylsk/ExecIT" target="_blank">ExecIT</a> - Execute shellcode files with rundll32.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://sonictk.github.io/asm_tutorial/" target="_blank">Understanding Windows x64 Assembly</a> - Add this to your Windows programming reading list.</li>
<li><a href="https://www.hub.trimarcsecurity.com/post/trimarc-whitepaper-owner-or-pwnd" target="_blank">Trimarc Whitepaper: Owner or Pwnd?</a> - This whitepaper touches on all aspects of AD ownership: Organizational Units (OUs), Computers, Groups, Users, AD Certificate Services (ADCS), Group Policy Objects (GPOs), and even Active Directory Integrated DNS (ADI DNS).</li>
<li><a href="https://github.com/AykutSarac/jsoncrack.com" target="_blank">jsoncrack.com</a> - ✨ Innovative and open-source visualization application that transforms various data formats, such as JSON, YAML, XML, CSV and more, into interactive graphs.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 366 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
