Title: Last Week in Security (LWiS) - 2024-09-23
Date: 2024-09-23 17:50
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-09-23
Author: Erik
Summary: 0-click macOS RCE (<a href="https://x.com/turmio_" target="_blank">@Turmio_</a>), sudo iptables LPE (<a href="https://x.com/suidpit" target="_blank">@suidpit</a> + <a href="https://x.com/smaury92" target="_blank">@smaury92</a>), SkeletonCookie ☠️🍪 (<a href="https://x.com/buffaloverflow" target="_blank">@buffaloverflow</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-09-16 to 2024-09-23.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://specterops.io/specter-bash/" style="color: #3bd267;" target="_blank">Specter Bash 2024</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p>Dare to join us for the ultimate SpecterOps experience! From October 7-10 in Denver, dive into spine-tingling offensive and defensive trainings like our renowned Red Team Operations course and the all-new Identity-driven Offensive Tradecraft course. When night falls, gear up for thrilling evening events with Specters and fellow training participants; it'll be scary-fun!</p>
<p><b>Save 25% on in-person tickets with code</b> <code>LWIS</code>. <a href="https://specterops.io/specter-bash/" style="color: #3bd267;" target="_blank">Secure your spot now!</a></p>
</aside><ul>
<li><a href="https://discord.com/blog/meet-dave-e2ee-for-audio-video" target="_blank">Meet Dave: Discord's New End-to-End Encryption for Audio &amp; Video</a> - Notably absent: text chat encryption.</li>
<li><a href="https://media.defense.gov/2024/Sep/18/2003547016/-1/-1/0/CSA-PRC-LINKED-ACTORS-BOTNET.PDF" target="_blank">[PDF] People's Republic of China-Linked Actors Compromise Routers and IoT Devices for Botnet Operations</a> - 🇨🇳 was rocking a botnet of 1.2 million compromises (385,000 unique in 🇺🇸 alone).</li>
<li><a href="https://www.twcert.org.tw/en/cp-139-8087-c3e70-2.html" target="_blank">D-Link WiFi router - Hidden Functionality</a> - At what point does "hidden functionality" become a backdoor? Sure feels like "sending specific packets" is the same as "triggering the backdoor."</li>
<li><a href="https://blog.torproject.org/tor-is-still-safe/" target="_blank">Is Tor still safe to use?</a> - The Tor project responds to the recent news about de-anonymizing Tor "Ricochet" users. The Tor project says the attack is not possible when using modern Tor services ("vanguards-lite" or the vanguards addon).</li>
<li><a href="https://www.youtube.com/watch?v=wVyu7NB7W6Y" target="_blank">Exposing The Flaw In Our Phone System</a> - SS7 attacks have been known in the security community for a long time, but this is probably the biggest stage they have been shown on (Veritasium + Linus Tech Tips).</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/unc2970-backdoor-trojanized-pdf-reader/" target="_blank">An Offer You Can Refuse: UNC2970 Backdoor Deployment Using Trojanized PDF Reader</a> - The use of a legitimate PDF reader with a DLL side-load is a clever way to deploy a backdoor. Getting the user to use the PDF reader feels a little clunky, but I'm sure with the right pretext many users will happily run it.</li>
<li><a href="https://mikko-kenttala.medium.com/zero-click-calendar-invite-critical-zero-click-vulnerability-chain-in-macos-a7a434fc887b" target="_blank">Zero-Click Calendar invite — Critical zero-click vulnerability chain in macOS</a> - This has to be one of the more complex vulnerability chains I've seen in a while. Zero click to get iCloud photos (or generic RCE) is impressive given the sandboxing and security features in macOS.</li>
<li><a href="https://research.openanalysis.net/credflusher/kiosk/stealer/stealc/amadey/autoit/2024/09/11/cred-flusher.html" target="_blank">AutoIt Credential Flusher - Forcing users to enter credentials so they can be stolen</a> - "Stealer" malware (i.e. keyloggers with builtin exfiltration) are now opening browsers in kiosk mode and navigating to google to get users to enter their credentials (which are then stolen). As most users have never seen kiosk mode, they likely don't know how to get out of it which leaves them the option to input their credentials.</li>
<li><a href="https://www.hexacorn.com/blog/2024/09/14/the-delayed-import-table-phantomdll-opportunities/" target="_blank">The delayed import-table phantomDLL opportunities</a> - While the post itself is interesting, I like it more because it doesn't work, but educates the reader throughout the process. A good reminder that we usually only read about successes, and its ok to publish dead ends.</li>
<li><a href="https://labs.jumpsec.com/ntlm-relaying-making-the-old-new-again/" target="_blank">NTLM Relaying - Making the Old New Again</a> - No new techniques, but a good referesher using modern tools for older attacks.</li>
<li><a href="https://labs.nettitude.com/blog/binary-ninja-plugin-fix-stomped-imports/" target="_blank">Binary Ninja Plugin: fix-stomped-imports</a> - When malware stomps their own PE header, it can make it difficult to reverse engineer, but the crew at Nettitude made a Binary Ninja plugin to reconstruct teh Import Address Table to see what API calls are being made. The tool is <a href="https://github.com/nettitude/binja-fix-stomped-imports" target="_blank">binja-fix-stomped-imports</a>.</li>
<li><a href="https://www.shielder.com/blog/2024/09/a-journey-from-sudo-iptables-to-local-privilege-escalation/" target="_blank">A Journey From sudo iptables To Local Privilege Escalation</a> - There are Windows LPEs and Linux kernel LPEs often, but this is a good old fashion Linux userland LPE.</li>
<li><a href="https://securitylabs.datadoghq.com/articles/abusing-entra-id-administrative-units/" target="_blank">Hidden in Plain Sight: Abusing Entra ID Administrative Units for Sticky Persistence</a> - Hidden membership Administrative Units (AUs) allow attackers to maintain concealed privileges of Entra ID objects and protect their accounts with restricted management AUs. Support for these attacks has been added to <a href="https://github.com/DataDog/stratus-red-team" target="_blank">stratus-red-team</a>.</li>
<li><a href="https://modexp.wordpress.com/2024/09/16/windows_arm64/" target="_blank">Shellcode: Windows on ARM64/AArch64</a> - A good primer on Windows on ARM64 shellcode.</li>
<li><a href="https://blog.amberwolf.com/blog/2024/september/skeleton-cookie-breaking-into-safeguard-with-cve-2024-45488/" target="_blank">Skeleton Cookie: Breaking into Safeguard with CVE-2024-45488</a> - "In this post, we crack open an authentication bypass vulnerability we discovered in the Safeguard for Privileged Passwords product. This vulnerability, assigned CVE-2024-45488, is internally known as “Skeleton Cookie”. We'll demonstrate how this vulnerability can be exploited to gain full administrative access to the virtual appliance. From there, an attacker can extract passwords and achieve Remote Code Execution."</li>
<li><a href="https://lyra.horse/blog/2024/09/using-youtube-to-steal-your-files/" target="_blank">Using YouTube to steal your files</a> - "a one-click clickjacking attack that chains a Google Slides YouTube embed path traversal to three separate redirects to gain editor access on a Drive file/folder."</li>
<li><a href="https://blog.quarkslab.com/exploiting-chamilo-during-a-red-team-engagement.html" target="_blank">Exploiting Chamilo during a Red Team engagement</a> - Exploiting an open-source app your client is running for initial access. Now that's a red team doing a real red team vs a pentest.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/bi-zone/CVE-2024-7965" target="_blank">CVE-2024-7965</a> - This repository contains PoC for CVE-2024-7965. This is the vulnerability in the Chrome V8 that occurs only within ARM64.</li>
<li><a href="https://github.com/SpiralBL0CK/CVE-2024-40431-CVE-2022-25479-EOP-CHAIN" target="_blank">CVE-2024-40431-CVE-2022-25479-EOP-CHAIN</a> - Local privilege Escalation for Windows that exploits the Realtek driver RtsPer.sys.</li>
<li><a href="https://github.com/sudonoodle/Aggressor-NTFY/" target="_blank">Aggressor-NTFY</a> - Cobalt Strike notifications via NTFY.</li>
<li><a href="https://github.com/sensepost/gowitness/releases/tag/3.0.0" target="_blank">gowitness 3.0</a> - A golang, web screenshot utility using Chrome Headless. The 3.0 update is a big one, with a new UI, new API, library support, reworked CLI, and more!</li>
<li><a href="https://github.com/saw-your-packet/CloudShovel" target="_blank">CloudShovel</a> - A tool for scanning public or private AMIs for sensitive files and secrets. The tool follows the research made on AWS CloudQuarry where we scanned 20k+ public AMIs.</li>
<li><a href="https://github.com/DataDog/undocumented-aws-api-hunter" target="_blank">undocumented-aws-api-hunter</a> - A tool to uncover undocumented APIs from the AWS Console.</li>
<li><a href="https://github.com/BlackSnufkin/NyxInvoke" target="_blank">NyxInvoke</a> - NyxInvoke is a Rust CLI tool for running .NET assemblies, PowerShell, and BOFs with Patchless AMSI and ETW bypass features. with Dual-build support.</li>
<li><a href="https://www.sectemplates.com/2024/09/announcing-the-security-exceptions-program-pack-10.html" target="_blank">Announcing the Security Exceptions program pack 1.0</a> - "Every company establishes processes to identify security vulnerabilities, prioritize them, develop solutions, and, in some cases, strategically accept risk either temporarily or permanently. Security exceptions are closely tied to vulnerability management and involve escalating risks to the appropriate decision-makers, who determine whether delaying a fix or accepting the risk without addressing it is the right strategic decision. This release provides a simplified, repeatable process for managing exceptions."</li>
<li><a href="https://github.com/p0dalirius/winacl" target="_blank">winacl</a> - A Go library for working with Windows access control lists, security descriptors, and more.</li>
<li><a href="https://github.com/itm4n/PPLrevenant" target="_blank">PPLrevenant</a> - Bypass LSA protection using the BYODLL technique.</li>
<li><a href="https://github.com/hyperreality/c2-vulnerabilities" target="_blank">c2-vulnerabilities</a> - A few CVEs from open-source C2 frameworks. Don't expose your C2? Covenant, Havoc, Ninja, Shad0w, and sliver affected. Full writeup <a href="https://blog.includesecurity.com/2024/09/vulnerabilities-in-open-source-c2-frameworks/" target="_blank">here</a>.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/zimnyaa/remotechrome" target="_blank">remotechrome</a> - dump Chrome cookies remotely with atexec and CDP.</li>
<li><a href="https://github.com/oldkingcone/BYOSI" target="_blank">BYOSI</a> - Evade EDR's the simple way, by not touching any of the API's they hook.</li>
<li><a href="https://github.com/0x11DFE/file-unpumper" target="_blank">file-unpumper</a> - Tool that can be used to trim useless things from a PE file such as the things a file pumper would add.</li>
<li><a href="https://github.com/atuinsh/atuin" target="_blank">atuin</a> - ✨ Magical shell history.</li>
<li><a href="https://github.com/dena-sohrabi/There" target="_blank">There</a> - Track timezones 🌍.</li>
<li><a href="https://github.com/sw33tLie/uff" target="_blank">uff</a> - unleashed ffuf.</li>
<li><a href="https://blog.projectdiscovery.io/simplifying-xss-detection-with-nuclei/" target="_blank">Simplifying XSS Detection with Nuclei - A New Approach</a> - Nulcie with a new XSS detection engine!</li>
<li><a href="https://github.com/MalwareSupportGroup/PolyDrop" target="_blank">PolyDrop</a> - A BYOSI (Bring-Your-Own-Script-Interpreter) Rapid Payload Deployment Toolkit.</li>
<li><a href="https://github.com/nicholasaleks/Damn-Vulnerable-Drone" target="_blank">Damn-Vulnerable-Drone</a> - Damn Vulnerable Drone is an intentionally vulnerable drone hacking simulator based on the popular ArduPilot/MAVLink architecture, providing a realistic environment for hands-on drone hacking.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 438 (+2)</p>
<p>Blogs monitored: 392 (+3)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
