Title: Last Week in Security (LWiS) - 2025-01-20
Date: 2025-01-20 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-01-20
Author: Erik
Summary: Windows LPE (<a href="https://x.com/MrAle_98" target="_blank">@MrAle_98</a>), CLR OPSEC (<a href="https://x.com/passthehashbrwn" target="_blank">@passthehashbrwn</a>), WinRM BOFs (<a href="https://x.com/falconforceteam" target="_blank">@falconforceteam</a>), Bitlocker bypass (<a href="https://x.com/Neodyme" target="_blank">@Neodyme</a>), BloodHound CLI (<a href="https://x.com/cmaddalena" target="_blank">@cmaddalena</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-01-13 to 2025-01-20.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">Celebrate the 'Month of On-Prem Red Teaming' with Altered Security!</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p>Altered Security offers multiple Red Team courses for both on-prem and Azure with affordable and enterprise-like hands-on labs. Each course comes with an industry-recognized certification. We are the creators of the Certified Red Team Professional (CRTP), CRTE, CARTP and more. Our courses and labs are designed by experts who have more than a decade's experience of training and speaking at BlackHat USA, DEF CON and other respected conferences. Join more than 40K professionals from 130+ countries.</p>
<p>We are celebrating January 2025 as the 'Month of On-Prem Red Teaming.'</p>
<p>Enjoy <strong>20% OFF</strong> on all on-prem courses using <strong><a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">RED20OFF</a></strong> (Stripe) from 20th January to 31st January 2025.</p>
</aside><ul>
<li><a href="https://www.whitehouse.gov/briefing-room/presidential-actions/2025/01/16/executive-order-on-strengthening-and-promoting-innovation-in-the-nations-cybersecurity/" target="_blank">Executive Order on Strengthening and Promoting Innovation in the Nation’s Cybersecurity</a> - The White House drops one last cybersecurity executive order before the transition. Nothing really novel here: follow best practices, FedRAMP all the things, do security better.</li>
<li><a href="https://www.justice.gov/opa/pr/justice-department-and-fbi-conduct-international-operation-delete-malware-used-china-backed" target="_blank">Justice Department and FBI Conduct International Operation to Delete Malware Used by China-Backed Hackers</a> - I suppose the FBI accessing US computers is now standard operating procedure. This is the second widely published case after 2021's <a href="https://www.vice.com/en/article/fbi-removes-web-shells-microsoft-exchange/" target="_blank">FBI Accesses Computers Around Country to Delete Microsoft Exchange Hacks</a>. A creative use of warrants.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://posts.specterops.io/intune-attack-paths-part-1-4ad1882c1811" target="_blank">Intune Attack Paths — Part 1</a> - SpecterOps has been leading the charge on Intue attacks, and this post is a great overview of all the red team things you can do with it.</li>
<li><a href="https://goodworkaround.com/2025/01/17/accessing-resources-cross-tenant-using-managed-service-identities/" target="_blank">Accessing resources cross tenant using managed service identities</a> - This could be used to allow an "attacker tenant" to access resources in a "victim tenant."</li>
<li><a href="https://securityintelligence.com/x-force/being-a-good-clr-host-modernizing-offensive-net-tradecraft/" target="_blank">Being a good CLR host - Modernizing offensive .NET tradecraft</a> - Custom common language runtime (CLR) loading is key to good OPSEC. "If you are still trying to reflectively load an assembly named Seatbelt in whatever year you are reading this then I would suggest you close this blog post and pursue a more fulfilling activity." 🤣 Code here: <a href="https://github.com/xforcered/Being-A-Good-CLR-Host" target="_blank">Being-A-Good-CLR-Host</a>.</li>
<li><a href="https://bishopfox.com/blog/raink-llms-document-ranking" target="_blank">raink: Use LLMs for Document Ranking</a> - Seems off topic, but Bishop Fox uses for problems like, "Which of these code diffs most likely fixes the issue described in following security advisory?" Code here: <a href="https://github.com/BishopFox/raink/tree/main" target="_blank">raink</a>.</li>
<li><a href="https://falconforce.nl/exploring-winrm-plugins-for-lateral-movement/" target="_blank">Exploring WinRM plugins for lateral movement</a> - We had no idea WinRM could use plugins, and this post introduces a custom plugin for lateral movement as well as ways to move over files without Defender detection.</li>
<li><a href="https://neodyme.io/en/blog/bitlocker_screwed_without_a_screwdriver/" target="_blank">Windows BitLocker -- Screwed without a Screwdriver</a> - Very indepth post on Bitlocker and how to pull off a downgrade + PXE boot attack to get unencrypted data. However, it requires access to the unlocked machine to get the Boot Configuration Data (BCD) to create the modified BCD which puts the Bitlocker key in memory but then boots via PXE. I suspect there is a way to make a generalized BCD and then put this whole attack on a Pi Zero or similar. The <a href="https://media.ccc.de/v/38c3-windows-bitlocker-screwed-without-a-screwdriver" target="_blank">38c3 talk</a> on the topic was well done and includes a demo.</li>
<li><a href="https://neodyme.io/en/blog/com_hijacking_1/" target="_blank">The Key to COMpromise - Pwning AVs and EDRs by Hijacking COM Interfaces, Part 1</a> - Exploit the EDR on a Windows machine to get SYSTEM! Slides: <a href="https://github.com/neodyme-labs/38c3_com_talk" target="_blank">38c3_com_talk</a>.</li>
<li><a href="https://www.netspi.com/blog/technical-blog/hardware-and-embedded-systems-penetration-testing/practical-methods-for-decapping-chips/" target="_blank">Practical Methods for Decapping Chips</a> - A niche topic not often discussed. Neat to see a post on the prerequisite physical attack required on many chips before glitching or other attacks can take place.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/MrAle98/CVE-2024-49138-POC" target="_blank">CVE-2024-49138-POC</a> - Windows LPE Proof of Concept that exploits <a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-49138" target="_blank">CVE-2024-49138</a> in CLFS.sys.</li>
<li><a href="https://github.com/synacktiv/CVE-2024-43468" target="_blank">CVE-2024-43468</a> - Microsoft Configuration Manager (ConfigMgr / SCCM) 2403 Unauthenticated SQL injections (CVE-2024-43468) exploit. This one will be big for years to come I predict. Unpatched SCCM results in total network pwnage from any unauthenticated endpoint that can reach a management point. Full write up <a href="https://www.synacktiv.com/advisories/microsoft-configuration-manager-configmgr-2403-unauthenticated-sql-injections" target="_blank">here</a>.</li>
<li><a href="https://www.openwall.com/lists/oss-security/2025/01/14/3" target="_blank">RSYNC: 6 vulnerabilities</a> - A heap buffer overflow leads to RCE. A tale as old as time.</li>
<li><a href="https://github.com/Michaeladsl/Patronusx" target="_blank">Patronusx</a> - This tool captures command line inputs during security assessments, meticulously redacts any sensitive information, and organizes the data by command type.</li>
<li><a href="https://github.com/vysecurity/IPFilter" target="_blank">IPFilter</a> - IP address filter by City.</li>
<li><a href="https://github.com/dreadnode/dyana" target="_blank">dyana</a> - A sandbox environment designed for loading, running and profiling a wide range of files, including machine learning models, ELFs, Pickle, Javascript and more.</li>
<li><a href="https://ssd-disclosure.com/ssd-advisory-palo-alto-expedition-rce-regionsdiscovery/" target="_blank">SSD Advisory – Palo Alto Expedition RCE (RegionsDiscovery)</a> - "A vulnerability in the /API/regionsDiscovery.php endpoint allows unauthenticated attackers to trigger a call to an Apache Spark server (attacker controlled) which can then be used to cause the execution of arbitrary code." This feels like an echo of <a href="https://en.wikipedia.org/wiki/Log4Shell" target="_blank">Log4Shell</a>.</li>
<li><a href="https://github.com/watchtowrlabs/CVE-2025-0282" target="_blank">Ivanti Connect Secure IFT TLS Stack Overflow pre-auth RCE (CVE-2025-0282)</a> - "This is purposefully broken in non-trivial ways and will require effort to work as outlined previously in our exploitation technique blogpost." Not to worry, <a href="https://github.com/sfewer-r7/CVE-2025-0282" target="_blank">PoC for CVE-2025-0282</a>, appear to be fully functional (for 22.7r2.4 anyway).</li>
<li><a href="https://github.com/Teach2Breach/rust_template" target="_blank">rust_template</a> - A template for Rust projects to be able to compile as an exe or a dll with sRDI compatibility for windows.</li>
<li><a href="https://github.com/google/security-research/blob/master/pocs/linux/kernelctf/CVE-2024-27397_mitigation/docs/exploit.md" target="_blank">CVE-2024-27397</a> - A local privilege escalation in Linux 4.1 to 6.8 exists if you can create user/net namespaces. The exploit itself is 100% effective, but the KSLR bypass is 90% effective (and may differ based on CPU).</li>
<li><a href="https://posts.specterops.io/introducing-bloodhound-cli-7dfaf82e2df8" target="_blank">Introducing BloodHound CLI</a> - A new Go command line tool to install and manage a Bloodhound server.</li>
<li><a href="https://github.com/byt3bl33d3r/gemini-web-navigator" target="_blank">gemini-web-navigator</a> - Experiments with Google Gemini's Vision capabilities for LLM driven/aided web navigation and desktop manipulation.</li>
<li><a href="https://github.com/racoten/BetterNetLoader" target="_blank">BetterNetLoader</a> - A version of NetLoader, Execute Assemblies and Bypass ETW and AMSI using Hardware Breakpoints.</li>
<li><a href="https://github.com/x64dbg/DataExplorer" target="_blank">DataExplorer</a> - The DataExplorer plugin integrates the pattern language from ImHex into x64dbg.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/lklynet/injectly" target="_blank">injectly</a> - I think this is meant for web design agencies, but it feels like a red team tool to manage and update phishing sites.</li>
<li><a href="https://github.com/jdu2600/Etw-SyscallMonitor" target="_blank">Etw-SyscallMonitor</a> - Monitors ETW for security relevant syscalls maintaining the set called by each unique process.</li>
<li><a href="https://github.com/orcasecurity-research/AIGoat" target="_blank">AIGoat</a> - AIGoat: A deliberately Vulnerable AI Infrastructure. Learn AI security through solving our challenges.</li>
<li><a href="https://github.com/rainerzufalldererste/windows_x64_shellcode_template" target="_blank">windows_x64_shellcode_template</a> - An easily modifiable shellcode template for Windows x64 written in C.</li>
<li><a href="https://github.com/geerlingguy/mini-rack" target="_blank">mini-rack</a> - Miniature rack builds, for portable or compact Homelabs.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 443 (+0)</p>
<p>Blogs monitored: 401 (+0)</p>
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
