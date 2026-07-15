Title: Last Week in Security (LWiS) - 2023-06-26
Date: 2023-06-26 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-06-26
Author: Erik
Summary: More Fortinet RCE (<a href="https://twitter.com/frycos" target="_blank">@frycos</a>), alloc-less injection (<a href="https://twitter.com/bohops" target="_blank">@bohops</a>), embedded system hacking (<a href="https://twitter.com/levaronsky" target="_blank">@levaronsky</a>), miniDLNA head exploitation (<a href="https://twitter.com/hyprdude" target="_blank">@hyprdude</a>), dump creds from sshd (<a href="https://twitter.com/jm33_m0" target="_blank">@jm33_m0</a>), MS Teams phishing (<a href="https://twitter.com/CorbridgeMax" target="_blank">@CorbridgeMax</a> + <a href="https://twitter.com/tde_sec" target="_blank">@tde_sec</a>), ThreatCheck + Ghidra (<a href="https://twitter.com/_RastaMouse" target="_blank">@_RastaMouse</a>), driver dev for red team (<a href="https://twitter.com/V3ded" target="_blank">@V3ded</a>), and more!

<aside class="m-note m-warning">
<h3>A break</h3>
<p>LWiS will be taking a week off next week and will return 2023-07-10.</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-06-12 to 2023-06-26.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2023/06/google-cloud-awards-313337-in-2022-vrp.html" target="_blank">Google Cloud Awards $313,337 in 2022 VRP Prizes</a>. This is how you incentivize bug bounty hunters.</li>
<li><a href="https://blog.cloudflare.com/masque-building-a-new-protocol-into-cloudflare-warp/" target="_blank">Donning a MASQUE: building a new protocol into Cloudflare WARP</a>. Lookout WireGuard, there is a new standard in town.</li>
<li><a href="https://marcoramilli.com/2023/06/22/2023-breaches-and-incidents-personal-notes/" target="_blank">2023 Breaches and Incidents: Personal Notes</a>. Stolen credentials are up, phishing is down. Use a good password manager appropriately.</li>
<li><a href="https://forum.proxmox.com/threads/proxmox-ve-8-0-released.129319/" target="_blank">Proxmox VE 8.0 released!</a>. Proxmox is a free and open source hypervisor that will feel familiar to VMWare ESXi users. I switched years ago and have been quite happy.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://secfault-security.com/blog/libreoffice.html" target="_blank">LibreOffice Arbitrary File Write (CVE-2023-1883)</a>. Did you know that LibreOffice has an MS Access competitor? Did you know you it can do arbitrary file writes?</li>
<li><a href="https://starlabs.sg/blog/2023/06-the-old-the-new-and-the-bypass-one-clickopen-redirect-to-own-samsung-s22-at-pwn2own-2022/" target="_blank">The Old, The New and The Bypass - One-click/Open-redirect to own Samsung S22 at Pwn2Own 2022</a>. An open redirect doesn't sound exciting, but it can turn a tap into a shell.</li>
<li><a href="https://alephsecurity.com/2023/06/19/electra-smart/" target="_blank">Why is it so hot here? Hacking Electra Smart air conditioners for fun and profit</a>. Some great embedded systems hacking here. If you want to talk embedded systems hacking, or try your had hacking some devices be sure to stop by the <a href="https://twitter.com/EmbeddedVillage" target="_blank">@EmbeddedVillage</a> at DEF CON.</li>
<li><a href="https://bishopfox.com/blog/cve-2023-27997-vulnerability-scanner-fortigate" target="_blank">CVE-2023-27997 Vulnerability Scanner for FortiGate Firewalls</a>. A vulnerability scanner sounds boring, but the technique to validate this heap overflow without crashing the firewall is pretty unique.</li>
<li><a href="https://bohops.com/2023/06/09/no-alloc-no-problem-leveraging-program-entry-points-for-process-injection/" target="_blank">No Alloc, No Problem: Leveraging Program Entry Points for Process Injection</a>. Up your process injection game with some lesser known techniques.</li>
<li><a href="https://frycos.github.io/vulns4free/2023/06/18/fortinac.html" target="_blank">FortiNAC - Just a few more RCEs</a>. "Shortly after the first CVE-2022-39952 disclosures I thought, why not looking at this product in the patched version 9.4.1 to find some more vulnerabilities?" Love it.</li>
<li><a href="https://www.gosecure.net/blog/2023/06/21/aws-waf-clients-left-vulnerable-to-sql-injection-due-to-unorthodox-mssql-design-choice/" target="_blank">AWS WAF Clients Left Vulnerable to SQL Injection Due to Unorthodox MSSQL Design Choice</a>. SQL is tricky and WAFs can get tripped up by "unique" query syntax.</li>
<li><a href="https://blog.coffinsec.com/0day/2023/06/19/minidlna-cve-2023-33476-exploits.html" target="_blank">chonked pt.2: exploiting cve-2023-33476 for remote code execution</a>. This is some hardcore exploit development content.</li>
<li><a href="https://www.synacktiv.com/en/publications/exploring-android-heap-allocations-in-jemalloc-new" target="_blank">Exploring Android Heap allocations in jemalloc 'new'</a>. If you like the previous post, you'll love this deep dive into heap allocation in Android.</li>
<li><a href="https://labs.jumpsec.com/advisory-idor-in-microsoft-teams-allows-for-external-tenants-to-introduce-malware/" target="_blank">Advisory: IDOR in Microsoft Teams Allows for External Tenants to Introduce Malware</a>. This was reported and "did not meet the bar for immediate servicing." "When this vulnerability is combined with social engineering via Teams it becomes very easy to start a back-and-forth conversation, jump on a call, share screens, and more. By comparison, it makes social engineering via email feel very stagnant, and stop-start." Guess what I am trying out tomorrow?</li>
<li><a href="https://msrc.microsoft.com/blog/2023/06/potential-risk-of-privilege-escalation-in-azure-ad-applications/" target="_blank">Potential Risk of Privilege Escalation in Azure AD Applications</a>. Email claims for authorization can lead to easy privilege escalation. Don't use it!</li>
<li><a href="https://offensivedefence.co.uk/posts/threatcheck-ghidra/" target="_blank">Bypassing Defender with ThreatCheck &amp; Ghidra</a>. A good short tutorial on finding signature bytes, translating them back to source code, and making modifications as appropriate.</li>
<li><a href="https://www.nassiben.com/video-based-crypta" target="_blank">Exploiting a Video Camera's Rolling Shutter to Recover Secret Keys from Devices Using Video Footage of Their Power LED</a>. Camera has to be at 6ft or less and record constant signing activity for a period of minutes but still, very cool side channel.</li>
<li><a href="https://www.sentinelone.com/labs/automating-string-decryption-and-other-reverse-engineering-tasks-in-radare2-with-r2pipe/" target="_blank">Automating String Decryption and Other Reverse Engineering Tasks in radare2 With r2pipe</a>. Automate some tedious RE work with radare2.</li>
<li><a href="https://v3ded.github.io/redteam/red-team-tactics-writing-windows-kernel-drivers-for-advanced-persistence-part-2" target="_blank">Red Team Tactics: Writing Windows Kernel Drivers for Advanced Persistence (Part 2)</a>. This is turning into some interesting work. The skeleton of an ICMP rootkit is taking shape.</li>
<li><a href="https://posts.specterops.io/what-is-tier-zero-part-1-e0da9b7cdfca" target="_blank">What is Tier Zero — Part 1</a>. Good discussion of AD design principles for security, what really needs protecting, and how to think about it.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/jm33-m0/SSH-Harvester" target="_blank">SSH-Harvester</a> - Harvest passwords automatically from OpenSSH server. More details <a href="https://jm33.me/openssh-server-mi-ma-shou-ge-ji.html" target="_blank">here</a>.</li>
<li><a href="https://github.com/Wh04m1001/CVE-2023-29343" target="_blank">CVE-2023-29343</a> - LPE in Sysmon version 14.14.</li>
<li><a href="https://github.com/Wh04m1001/CVE-2023-20178" target="_blank">CVE-2023-20178</a> - PoC for Arbitrary File Delete vulnerability in Cisco Secure Client (tested on 5.0.01242) and Cisco AnyConnect (tested on 4.10.06079).</li>
<li><a href="https://github.com/Idov31/Jormungandr" target="_blank">Jormungandr</a> is a kernel implementation of a COFF loader, allowing kernel developers to load and execute their COFFs in the kernel.</li>
<li><a href="https://github.com/frkngksl/NimExec" target="_blank">NimExec</a> - Fileless Command Execution for Lateral Movement in Nim.</li>
<li><a href="https://github.com/trustedsec/CS_COFFLoader" target="_blank">CS_COFFLoader</a> - a COFF loader written in C#.</li>
<li><a href="https://github.com/Accenture/Spartacus/releases/tag/v2.0.0" target="_blank">Spartacus-v2.0.0</a>. Not a new tool but a big release for the DLL/COM Hijacking Toolkit (2.0 added COM hijacking).</li>
<li><a href="https://github.com/The-Z-Labs/bof-launcher" target="_blank">bof-launcher</a> - Beacon Object File (BOF) launcher - library for executing BOF files in C/C++/Zig applications.</li>
<li><a href="https://github.com/mansk1es/GhostFart" target="_blank">GhostFart</a> - Unhook NTDLL without triggering "PspCreateProcessNotifyRoutine".</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/dievus/msLDAPDump" target="_blank">msLDAPDump</a> - LDAP enumeration tool implemented in Python3.</li>
<li><a href="https://github.com/BeichenDream/SharpToken" target="_blank">SharpToken</a> - Windows Token Stealing Expert.</li>
<li><a href="https://github.com/neuroforgede/docker-swarm-proxy" target="_blank">docker-swarm-proxy</a> - What if you wanted a docker exec, but for Docker swarm? - Control any node in the swarm from your CLI.</li>
<li><a href="https://github.com/x0reaxeax/PageSplit" target="_blank">PageSplit</a> - Splitting and executing shellcode across multiple pages.</li>
<li><a href="https://github.com/wunderwuzzi23/ropci" target="_blank">ropci</a> - So, you think you have MFA? AAD/ROPC/MFA bypass testing tool.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 348 (+1)</p>
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
