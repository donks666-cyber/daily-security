Title: Last Week in Security (LWiS) - 2024-01-15
Date: 2024-01-15 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-01-15
Author: Erik
Summary: SSPI in Python (<a href="https://twitter.com/snovvcrash" target="_blank">@snovvcrash</a>), executing shellcode from VBA (<a href="https://twitter.com/TheXC3LL" target="_blank">@TheXC3LL</a>), Mirth Connect pre-auth RCE (<a href="https://twitter.com/Horizon3Attack" target="_blank">@Horizon3Attack</a>), Visual Studio LPE (<a href="https://twitter.com/filip_dragovic" target="_blank">@filip_dragovic</a>), DLL injection LPE (<a href="https://twitter.com/m417z" target="_blank">@m417z</a>), Android ARM64 reversing (<a href="https://twitter.com/Dauntless" target="_blank">@Dauntless</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-01-08 to 2024-01-15.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://labs.watchtowr.com/welcome-to-2024-the-sslvpn-chaos-continues-ivanti-cve-2023-46805-cve-2024-21887/" target="_blank">Welcome To 2024, The SSLVPN Chaos Continues - Ivanti CVE-2023-46805 &amp; CVE-2024-21887</a>. At this point, if you have an SSL VPN, just throw it away. Use WireGuard and sleep better at night.</li>
<li><a href="https://bishopfox.com/blog/its-2024-and-over-178-000-sonicwall-firewalls-are-publicly-exploitable" target="_blank">It's 2024 and Over 178,000 SonicWall Firewalls are Publicly Exploitable</a>. No one took my advice from the previous story. These vulnerabilities are over two years old.</li>
<li><a href="https://www.elttam.com/blog/talkback-intro/" target="_blank">Keeping Up With the Pwnses</a>. A cybersecurity news aggregator? Wait, but thats what I am!?</li>
<li><a href="https://about.gitlab.com/releases/2024/01/11/critical-security-release-gitlab-16-7-2-released/" target="_blank">GitLab Critical Security Release: 16.7.2, 16.6.4, 16.5.6</a>. A vulnerability so bad it <a href="https://twitter.com/rwincey/status/1745659710089437368" target="_blank">fits in a tweet</a>.</li>
<li><a href="https://twitter.com/matteyeux/status/1746510424281866486" target="_blank">Seems like someone pushed a bunch of iBoot symbols to Hexrays's Lumina server</a>. This is either an Apple employee or a researcher who (accidentally?) pushed their iBoot symbols to a public symbol server. A nice gift for iOS researchers.</li>
<li><a href="https://twitter.com/lauriewired/status/1745871465592094970" target="_blank">Airdrop doesn't use cryptographic salts, and rainbow tables are easily able to de-anonymize users</a>. Due to the design of AirDrop, with a little pre-computing and hard drive space it is trivial to de-anonymize users with AirDrop enabled (at least get their phone number). Read more: <a href="https://eprint.iacr.org/2021/893.pdf" target="_blank">[PDF] DEMO: AirCollect: Efficiently Recovering Hashed Phone Numbers Leaked via Apple AirDrop</a>. This has been a known issue to Apple since 2019...</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://swarm.ptsecurity.com/python-sspi-teaching-impacket-to-respect-windows-sso/" target="_blank">Python ❤️ SSPI: Teaching Impacket to Respect Windows SSO</a>. With a little bring your own interpreter (i.e. <a href="https://github.com/naksyn/Pyramid" target="_blank">Pyramid</a>), impacket can now use the tickets already cached on the box you have access to without needing to know any plain text credentials.</li>
<li><a href="https://adepts.of0x.cc/vba-hijack-pointers-rwa/" target="_blank">VBA: having fun with macros, overwritten pointers &amp; R/W/X memory</a>. The things that have been done with VBA that VBA was never supposed to do are impressive.</li>
<li><a href="https://badoption.eu/blog/2024/01/12/teams5.html" target="_blank">Teams external participant splash screen bypass # 2</a>. Phish where the users are. And if Microsoft "patches" a bypass of the external user warning, just... bypass it again!</li>
<li><a href="https://www.horizon3.ai/writeup-for-cve-2023-43208-nextgen-mirth-connect-pre-auth-rce/" target="_blank">Writeup for CVE-2023-43208: NextGen Mirth Connect Pre-Auth RCE</a> . Another entry in "a patch is not always the end of a vulnerability," one of my favorite series.</li>
<li><a href="https://www.mdsec.co.uk/2024/01/cve-2024-20656-local-privilege-escalation-in-vsstandardcollectorservice150-service/" target="_blank">CVE-2024-20656 - Local Privilege Escalation in the VSStandardCollectorService150 Service</a>. Bind mounts strike again. Great find and write up. PoC: <a href="https://github.com/Wh04m1001/CVE-2024-20656" target="_blank">CVE-2024-20656</a>.</li>
<li><a href="https://m417z.com/Privilege-escalation-using-the-XAML-diagnostics-API-CVE-2023-36003/" target="_blank">Privilege escalation using the XAML diagnostics API (CVE-2023-36003)</a>. Another Windows LPE! PoC: <a href="https://github.com/m417z/CVE-2023-36003-POC" target="_blank">CVE-2023-36003-POC</a>.</li>
<li><a href="https://blog.nviso.eu/2024/01/15/deobfuscating-android-arm64-strings-with-ghidra-emulating-patching-and-automating/" target="_blank">Deobfuscating Android ARM64 strings with Ghidra: Emulating, Patching, and Automating</a>. Some hardcore Android ARM64 reversing and debugging content.</li>
<li><a href="https://philkeeble.com/automation/cicd/CICD-Goat-Walkthrough-Part-1/" target="_blank">CICD-Goat Setup and Easy Challenge walkthrough (WhiteRabbit, MadHatter, Duchess)</a>. The fact you can deploy your own CTFd and multiple vulnerable CI systems with a single docker compose is awesome! There is a <a href="https://philkeeble.com/automation/cicd/CICD-Goat-Walkthrough-Part-2/" target="_blank">part 2</a> as well, but try to solve them on your own first!</li>
<li><a href="https://github.com/Valentin-Metz/writeup_factorio" target="_blank">writeup_factorio</a> - Writeup of a remote code execution in Factorio by supplying a modified save file.</li>
<li><a href="https://adnanthekhan.com/2024/01/10/cve-2023-49291-and-more-a-potential-actions-nightmare/" target="_blank">CVE-2023-49291 and More – A Potential Actions Nightmare</a> - Loving all these github action attacks. The developer workflow is becoming more and more of an attack surface.</li>
<li><a href="https://rift.stacktitan.com/chi_part_1/" target="_blank">The Covert Hardware Implant: Part 1</a> - "...we use our hardware implants in real-world Red Team operations while constantly evolving the form factor to align with the most effective solution for the mission"</li>
<li><a href="https://blog.shodan.io/deep-dive-http-favicon/" target="_blank">Deep Dive: http.favicon</a> - Favicons have been making a come back the past few years. Don't sleep on this recon data point.</li>
<li><a href="https://zolutal.github.io/aslrnt/" target="_blank">ASLRn't: How memory alignment broke library ASLR</a> . Oof. I guess that's why you do defense in depth.</li>
<li><a href="https://medium.com/@sam0-0/bypassing-payments-in-apple-for-free-trails-for-lifetime-8e3019dfe57b" target="_blank">Bypassing Payments in Apple for Free Trails for Lifetime</a>. The ability to create unlimited AppleIDs without a phone number or credit card may be responsible for the uptick in iMessage spam seen recently.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://kiosk.vsim.xyz/#" target="_blank">Kiosk Tooling</a>. Next time you only have a browser and need to break out, browse to this site for some potential quick wins.</li>
<li><a href="https://github.com/secgroundzero/CS-Aggressor-Scripts" target="_blank">CS-Aggressor-Scripts</a> - Aggressor Scripts for Cobalt Strike (that post data to a Slack Channel).</li>
<li><a href="https://github.com/myshell-ai/OpenVoice" target="_blank">OpenVoice</a> - Instant voice cloning by MyShell. I have warned of this, and now it is here and easy to use. Vishing will never be the same.</li>
<li><a href="https://github.com/TheCyb3rAlpha/BobTheSmuggler" target="_blank">BobTheSmuggler</a> -  "Bob the Smuggler": A tool that leverages HTML Smuggling Attack and allows you to create HTML files with embedded 7z/zip archives. The tool would compress your binary (EXE/DLL) into 7z/zip file format, then XOR encrypt the archive and then hides inside PNG/GIF image file format (Image Polyglots).</li>
<li><a href="https://github.com/LaresLLC/SuperSharpShares" target="_blank">SuperSharpShares</a> -  SuperSharpShares is a tool designed to automate enumerating domain shares, allowing for quick verification of accessible shares by your associated domain account.</li>
<li><a href="https://www.pinvoke.dev/" target="_blank">pinvoke.dev</a> - Code-generated P/Invoke signatures.</li>
<li><a href="https://github.com/decoder-it/DFSCoerce-exe-2/" target="_blank">DFSCoerce-exe-2</a> - DFSCoerce exe revisited version with custom authentication.</li>
<li><a href="https://github.com/EpicGames/raddebugger" target="_blank">raddebugger</a> - A native, user-mode, multi-process, graphical debugger.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/usdAG/FlowMate" target="_blank">FlowMate</a> - a BurpSuite extension that brings taint analysis to web applications, by tracking all parameters send to a target application and matches their occurrences in the responses.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 366 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
