Title: Last Week in Security (LWiS) - 2025-05-19
Date: 2025-05-19 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-05-19
Author: Erik
Summary: Certipy 5 (<a href="https://x.com/ly4k_" target="_blank">@ly4k_</a>), MobileIron pwnage (<a href="https://x.com/chudyPB" target="_blank">@chudyPB</a>), new CRTO pricing (<a href="https://x.com/_ZeroPointSec" target="_blank">@_ZeroPointSec</a>), Volatility 3 parity (<a href="https://x.com/volatility" target="_blank">@volatility</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-05-12 to 2025-05-19.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.zeropointsecurity.co.uk/blog/new-site-launch" target="_blank">New Site Launch</a> - Zero Point Security (from <a href="https://x.com/_RastaMouse" target="_blank">@_RastaMouse</a>) the company behind the increasingly popular Certified Red Team Operator (CRTO) course, has a new site and new lab provider backend. Best of all, exams are now on-demand (previously had to be scheduled) and retakes are free. Awesome!</li>
<li><a href="https://www.reuters.com/sustainability/climate-energy/ghost-machine-rogue-communication-devices-found-chinese-inverters-2025-05-14/" target="_blank">Rogue communication devices found in Chinese solar power inverters</a> - This article makes bold claims, with little fact or evidence, from "two people." I don't doubt it's happening, but find a device and show it if you're going to write an article. It reminds me of the 2018 classic: <a href="https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies" target="_blank">The Big Hack: How China Used a Tiny Chip to Infiltrate U.S. Companies</a> which led to... nothing (except <a href="https://finance.yahoo.com/quote/SMCI/history/?period1=1538524800&amp;period2=1538697600" target="_blank">tanking $SMCI</a>).</li>
<li><a href="https://security.googleblog.com/2025/05/advanced-protection-mobile-devices.html" target="_blank">Advanced Protection: Google’s Strongest Security for Mobile Devices</a> - Apple has "Lockdown mode," Google now has "Advanced Protection." End-to-end encrypted security logs stored in the cloud is a really cool feature that is sure to have advanced attackers thinking twice about using that 0day on a phone with Advanced Protection enabled.</li>
<li><a href="https://virtualize.sh/blog/ground-control-to-major-trial/" target="_blank">Ground control to Major Trial</a> - Oh boy, if you host nearly 4,000 VMs on a platform, it's time to pay for a license. One wonders if the cost (person-hours) of creating the trial-refresh system and then updating the trial license every month was more than a license. I suspect it was.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.watchtowr.com/expression-payloads-meet-mayhem-cve-2025-4427-and-cve-2025-4428/" target="_blank">Expression Payloads Meet Mayhem - Ivanti EPMM Unauth RCE Chain (CVE-2025-4427 and CVE-2025-4428)</a> - Your weekly watchTowr blog, this time its MobileIron aka Ivanti moble device management (MDM). Always a great detailed read.</li>
<li><a href="https://code-white.com/blog/ivanti-desktop-and-server-management/" target="_blank">Analyzing the Attack Surface of Ivanti's DSM</a> - Ivanti's Desktop &amp; Server Management (DSM) product allows for centralized distribution of software packages, so similar to MDM, but for desktops and servers. This detailed article focuses on software management on Windows hosts, and all the pitfalls you may run into before the software is End-Of-Life'd in December 2026. Because no one will be running it after that, right?</li>
<li><a href="https://necromancerlabs.com/research/papers/2025/gost-in-the-protocol/" target="_blank">GOst in the Protocol: Hunting Ligolo with JARM Fingerprinting in the wild</a> - "We identified three distinct JARM signatures that reliably identify Ligolo proxy servers in the wild: one for Ligolo 0.7.x, one for Ligolo 0.8.x, and one for Ligolo-MP (which is shared with Sliver C2)." Beyond a simple JARM signature, the post explores how to verify that what looks like Ligolo, actually is. They dropped a tool to do so: <a href="https://github.com/Necromancerlabs/Hunting-Ligolo" target="_blank">Hunting-Ligolo</a>.</li>
<li><a href="https://starlabs.sg/blog/2025/05-breaking-out-of-restricted-mode-xss-to-rce-in-visual-studio-code/" target="_blank">Breaking Out of Restricted Mode: XSS to RCE in Visual Studio Code</a> - Even if you open a file in Restricted Mode by clicking "No, I don't trust the authors," a cross site scripting (XSS) issue in iPython could launch another instance of Visual Studio Code without Restricted Mode which allows for full command execution. Should probably be opening these repos in throw away virtual machines (perhaps setup automatically with <a href="https://ludus.cloud/" target="_blank">Ludus</a>).</li>
<li><a href="https://github.com/google/security-research/security/advisories/GHSA-qx2m-rcpc-v43v" target="_blank">Oracle VM VirtualBox - VM escape via VGA device</a> - The timeline from report to fix to disclosure is impressively fast on this one.</li>
<li><a href="https://blog.zsec.uk/commit-stomping/" target="_blank">Commit Stomping - Manipulating Git Histories to Obscure the Truth</a> - "Git’s distributed and trust-based design can be turned into a technique for deception." This post gives some more detail to git commit "stomping" following the release of <a href="https://github.com/ZephrFish/RepoMan" target="_blank">RepoMan</a>.</li>
<li><a href="https://whiteknightlabs.com/2025/05/19/harnessing-the-power-of-cobalt-strike-profiles-for-edr-evasion-part-2/" target="_blank">Harnessing the Power of Cobalt Strike Profiles for EDR Evasion – Part 2</a> - "The last three updates has introduced a lot of flexibility for the operator. From post-exploitation DLL string removal, ability to hook high-level API via BeaconGate, the introduction of PrependLoader and its evasive features and much more, makes Cobalt Strike a more ready-to-use tool and a more customizable one."</li>
<li><a href="https://infosecfacts.github.io/content/Evading%20Defender%20with%20Python%20and%20Meterpreter%20Shellcode:%20Part%201.html" target="_blank">Evading Defender With Python And Meterpreter Shellcode: Part 1</a> - Sometimes, the simple things work.</li>
<li><a href="https://blog.fndsec.net/2025/05/16/the-context-only-attack-surface/" target="_blank">New Process Injection Class: The CONTEXT-Only Attack Surface</a> - The opposite of the last entry, a very deep dive into process injection, and a new method: <a href="https://github.com/Friends-Security/RedirectThread" target="_blank">RedirectThread</a> - Playing around with Thread Context Hijacking. Building more evasive primitives to use as alternative for existing process injection techniques.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/badsectorlabs/ludus_adaptix_c2" target="_blank">ludus_adaptix_c2</a> - An Ansible role that install the Adaptix C2 server and/or client on Debian based hosts. [This one is ours 😊]</li>
<li><a href="https://github.com/ly4k/Certipy/discussions/270" target="_blank">The Future of Certipy and the Release of v5 &amp; ESC16</a> - A massive release for Certipy which includes a new ADCS attack: <a href="https://github.com/ly4k/Certipy/wiki/06-%E2%80%90-Privilege-Escalation#esc16-security-extension-disabled-on-ca-globally" target="_blank">ESC16</a>.</li>
<li><a href="https://github.com/Krypteria/Neo4LDAP" target="_blank">Neo4LDAP</a> - Neo4LDAP is a query and visualization tool focused on Active Directory environments. It combines LDAP syntax with graph-based data analysis in Neo4j, offering an alternative approach to tools like BloodHound.</li>
<li><a href="https://github.com/dmcxblue/Claude-C2" target="_blank">Claude-C2</a> - Utilizing an MCP Server to communicate with your C2.</li>
<li><a href="https://github.com/CompassSecurity/EntraFalcon" target="_blank">EntraFalcon</a> - A lightweight PowerShell tool for assessing the security posture of Microsoft Entra ID environments. It helps identify privileged objects, risky assignments, and potential misconfigurations. More at: <a href="https://blog.compass-security.com/2025/04/introducing-entrafalcon-a-tool-to-enumerate-entra-id-objects-and-assignments/" target="_blank">Introducing EntraFalcon</a>.</li>
<li><a href="https://github.com/tastypepperoni/NetImpostor" target="_blank">NetImpostor</a> - Gain another host's network access permissions by establishing a stateful connection with a spoofed source IP. More at: <a href="https://tastypepperoni.medium.com/stateful-connection-with-spoofed-source-ip-netimpostor-ece8b950a981" target="_blank">Stateful Connection With Spoofed Source IP — NetImpostor</a>.</li>
<li><a href="https://volatilityfoundation.org/announcing-the-official-parity-release-of-volatility-3/" target="_blank">Announcing the Official Parity Release of Volatility 3!</a> - The best memory analysis tool can now "fully replace Volatility 2."</li>
<li><a href="https://github.com/jailbreakdotparty/dirtyZero" target="_blank">dirtyZero</a> - Basic customization app using CVE-2025-24203. Patched in iOS 18.4.</li>
<li><a href="https://github.com/wh1te4ever/CVE-2025-31258-PoC" target="_blank">CVE-2025-31258-PoC</a> - 1day practice - Escape macOS sandbox (partial) using RemoteViewServices. <a href="https://youtube.com/watch?v=GlReVUh_4W4" target="_blank">Video PoC</a>.</li>
<li><a href="https://github.com/andreisss/Living-off-the-COM-Type-Coercion-Abuse" target="_blank">Living-off-the-COM-Type-Coercion-Abuse</a> - This technique leverages PowerShell's .NET interop layer and COM automation to achieve stealthy command execution by abusing implicit type coercion.</li>
<li><a href="https://github.com/itaymigdal/PowerDodder" target="_blank">PowerDodder</a> - Persist like a Dodder.</li>
<li><a href="https://github.com/Octoberfest7/zip_smuggling" target="_blank">zip_smuggling</a> - Python3 utility for creating zip files that smuggle additional data for later extraction.</li>
<li><a href="https://github.com/cybersectroll/TrollDisappearKey" target="_blank">TrollDisappearKey</a> is a loader which allows loading of .exe assemblies (provide URL to assembly) without amsi scanning taking place during assembly.load().</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/WellKnitTech/LockBitPanelDB" target="_blank">LockBitPanelDB</a> - Repo of the SQL database from the LockBit panel being hacked. More info: <a href="https://www.bleepingcomputer.com/news/security/lockbit-ransomware-gang-hacked-victim-negotiations-exposed/" target="_blank">LockBit ransomware gang hacked, victim negotiations exposed</a>.</li>
<li><a href="https://github.com/Tablecruncher/tablecruncher" target="_blank">tablecruncher</a> - A lightweight, powerful CSV editor for macOS, Windows and Linux — with built-in JavaScript macros.</li>
<li><a href="https://github.com/kapellos/LNKSmuggler" target="_blank">LNKSmuggler</a> - A Python script for creating <cite>.lnk</cite> (shortcut) files with embedded encoded data and packaging them into ZIP archives.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 452 (+0)</p>
<p>Blogs monitored: 417 (+1)</p>
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
