Title: Last Week in Security (LWiS) - 2024-08-26
Date: 2024-08-26 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-08-26
Author: Erik
Summary: "USDoD" doxed, VEH research (<a href="https://x.com/passthehashbrwn" target="_blank">@passthehashbrwn</a>), Defender exclusions (<a href="https://x.com/dazzyddos" target="_blank">@dazzyddos</a>), CSS history leak (<a href="https://x.com/TheXC3LL" target="_blank">@TheXC3LL</a>), Cobalt Strike DNS listeners (<a href="https://x.com/VirtualAllocEx" target="_blank">@VirtualAllocEx</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-08-19 to 2024-08-26.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.cisa.gov/news-events/news/joint-odni-fbi-and-cisa-statement-iranian-election-influence-efforts" target="_blank">Joint ODNI, FBI, and CISA Statement on Iranian Election Influence Efforts</a> - CISA, ODNI, and FBI report that Iran has been targeting presidential campaigns through cyber operations and social engineering, aiming to exploit societal tensions and undermine confidence in democratic institutions.</li>
<li><a href="https://www.avweb.com/aviation-news/faa-introduces-new-cybersecurity-for-airplanes-and-aircraft-equipment/" target="_blank">FAA Proposes New Cybersecurity Standards For Aircraft</a> - The FAA is looking to standardize how it will incorporate cybersecurity standards for airworthiness. It also introduces a new term "intentional unauthorized electronic interactions (IUEI)."" The dense 36 page PDF available in the post.</li>
<li><a href="https://www.justice.gov/usao-edky/pr/pulaski-county-man-sentenced-cyber-intrusion-and-aggravated-identity-theft" target="_blank">Pulaski County Man Sentenced for Cyber Intrusion and Aggravated Identity Theft</a> - "The Defendant committed cyber intrusions, by hacking into state death registry systems to fake his own death to avoid paying his child support obligations". Seems like it would be easier to just pay your child support. Brings back memories from this <a href="https://www.youtube.com/watch?v=9FdHq3WfJgs" target="_blank">DEF CON 23 talk</a>.</li>
<li><a href="https://support.solarwinds.com/SuccessCenter/s/article/SolarWinds-Web-Help-Desk-12-8-3-Hotfix-2" target="_blank">SolarWinds Web Help Desk 12.8.3 Hotfix 2</a> - Welcome back Solarwinds. "Fixes SolarWinds Web Help Desk Hardcoded Credential Vulnerability."</li>
<li><a href="https://www.malwarebytes.com/blog/news/2024/08/hundreds-of-online-stores-hacked-in-new-campaign" target="_blank">Hundreds of online stores hacked in new campaign</a> - Malwarebytes researchers uncovered a new digital skimming campaign targeting hundreds of Magento-based online stores, where attackers injected malicious code to steal customers' payment information during checkout, affecting over 1,100 unique users across multiple compromised websites.</li>
<li><a href="https://www.justice.gov/usao-ndga/pr/united-states-files-suit-against-georgia-institute-technology-and-georgia-tech" target="_blank">United States Files Suit Against the Georgia Institute of Technology and Georgia Tech Research Corporation Alleging Cybersecurity Violations</a> - Interesting. Uncle Sam cracking down on "failure to meet cybersecurity requirements". I wonder if this trend will continue.</li>
<li><a href="https://cyble.com/blog/new-cheana-stealer-targets-vpn-user/" target="_blank">New Cheana Stealer Targets VPN Users Across Multiple Operating Systems</a> - Don't feel too smug if you're a macOS or Linux user (arch btw) watching the constant stream of Windows malware, some threat actors are equal opportunity exploiters.</li>
<li><a href="https://hackread.com/usdod-hacker-ssn-leak-reveals-brazilian-citizen/" target="_blank">USDoD Hacker Behind $3 Billion SSN Leak Reveals Himself as Brazilian Citizen</a> - The dude who leaked all those SSN was doxed and then he came clean. TLDR - Luan G, 33 year old from Brazil with &lt; 100 Instagram followers.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://redops.at/en/blog/cobalt-strike-dns-listener" target="_blank">Cobalt Strike - DNS Listener</a> - A nice and up-to-date article by <a href="https://x.com/VirtualAllocEx" target="_blank">@VirtualAllocEx</a> on how to setup Cobalt Strike DNS listeners using Azure DNS Redirectors and GoDaddy. Isn't <a href="https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/listener-infrastructue_external-c2.htm" target="_blank">External C2</a> (via "known good" providers) the standard?</li>
<li><a href="https://securityintelligence.com/x-force/using-veh-for-defense-evasion-process-injection/" target="_blank">You just got vectored - Using Vectored Exception Handlers (VEH) for defense evasion and process injection</a> - Manually manipulating Windows Vectored Exception Handlers (VEH) to evade detection and perform threadless process injection. Code <a href="https://github.com/passthehashbrowns/VectoredExceptionHandling" target="_blank">here</a>.</li>
<li><a href="https://labs.jumpsec.com/adversary-at-the-door-initial-access-and-whats-currently-on-the-menu/" target="_blank">Adversary at the Door - Initial Access and what's currently on the menu</a> - A good intro/explanation into initial access topics most red teamers deal with daily. If you're new to initial access tradecraft, this is a great place to start!</li>
<li><a href="https://www.msreverseengineering.com/blog/2024/8/20/c-unwind-metadata-1" target="_blank">C++ Unwind Exception Metadata: A Hidden Reverse Engineering Bonanza</a> - Hex-Rays 9.0 introduces support for displaying C++ exception wind and unwind metadata in MSVC/x64 targets, providing reverse engineers with valuable insights into object types, structure relationships, and inheritance hierarchies that were previously hidden or difficult to discern.</li>
<li><a href="https://adepts.of0x.cc/css-history-leaks/" target="_blank">Mixing watering hole attacks with history leak via CSS</a> - "CSS will bring you more shells than C," is a bold introduction. The use of CSS to create a fake captcha and leak browser history is pretty wicked though.</li>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/peaklight-decoding-stealthy-memory-only-malware/" target="_blank">PEAKLIGHT: Decoding the Stealthy Memory-Only Malware</a> - Mandiant identified a new memory-only dropper using a complex, multi-stage infection process. This memory-only dropper decrypts and executes a PowerShell-based downloader. This PowerShell-based downloader is being tracked as PEAKLIGHT.</li>
<li><a href="https://brownfinesecurity.com/blog/intercepting-mobile-traffic-with-caido-and-frida/" target="_blank">Intercepting Mobile Application Traffic with Caido and Frida</a> - Good walkthrough for the new Caido user crew.</li>
<li><a href="https://techcommunity.microsoft.com/t5/storage-at-microsoft/smb-security-hardening-in-windows-server-2025-amp-windows-11/ba-p/4226591" target="_blank">SMB security hardening in Windows Server 2025 &amp; Windows 11</a> - Good reference to add in some of your finding templates for reporting.</li>
<li><a href="https://thedfirreport.com/2024/08/26/blacksuit-ransomware/" target="_blank">BlackSuit Ransomware</a> - Always fun to read about ransomware group YOLO tradecraft. If it works it works!</li>
<li><a href="https://scorpiosoftware.net/2024/08/25/creating-kernel-object-type-part-1/" target="_blank">Creating Kernel Object Type (Part 1)</a> - How to create a custom kernel object type called "DataStack" in Windows using undocumented APIs.</li>
<li><a href="https://www.horizon3.ai/attack-research/disclosures/ntlm-credential-theft-in-python-windows-applications/" target="_blank">NTLM Credential Theft in Python Windows Applications</a> - Horizon3 with some research and vulns from open-source tooling. This research focuses on leaking NTLMv2 hashes from various applications.</li>
<li><a href="https://imlzq.com/apple/macos/2024/08/24/Unveiling-Mac-Security-A-Comprehensive-Exploration-of-TCC-Sandboxing-and-App-Data-TCC.html" target="_blank">Unveiling Mac Security: A Comprehensive Exploration of Sandboxing and AppData TCC</a> - From BlackHat 2024, Zhongquan Li presents a comprehensive exploration of macOS security mechanisms, revealing multiple vulnerabilities in sandboxing, quarantine protection, and TCC systems, demonstrating how seemingly harmless bugs can be chained into powerful exploit techniques for sandbox escapes and unauthorized data access across macOS versions 10.15 to 15.0.</li>
<li><a href="https://dazzyddos.github.io/posts/Abusing_Exclusions_To_Evade_Detection/" target="_blank">Abusing Exclusions To Evade Detection</a> - Some interesting techniques to leak Defender exclusions as an unprivileged user.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/c2micro/ipapocket" target="_blank">ipapocket</a> - Python library for interacting with FreeIPA network protocols.</li>
<li><a href="https://github.com/Cyxow/CVE-2024-3183-POC" target="_blank">CVE-2024-3183-POC</a> - POC for CVE-2024-3183 (FreeIPA Rosting).</li>
<li><a href="https://github.com/0x20c/CVE-2024-38856-EXP" target="_blank">CVE-2024-38856-EXP</a> - CVE-2024-38856 is a pre-authentication flaw in Apache OFBiz that can lead to remote code execution</li>
<li><a href="https://github.com/techBrandon/CAPs" target="_blank">CAPs</a> - Scripts to enumerate and report on Entra Conditional Access.</li>
<li><a href="https://github.com/Black-Frost/windows-learning/tree/main/CVE-2024-38054" target="_blank">CVE-2024-38054</a> - Windows LPE in the Kernel Streaming WOW Thunk Service Driver takes you from user straight to SYSTEM.</li>
<li><a href="https://github.com/ynwarcs/CVE-2024-38063" target="_blank">CVE-2024-38063</a> - Crash PoC for CVE-2024-38063 (RCE in tcpip.sys on Windows).</li>
<li><a href="https://github.com/Dump-GUY/IDA_PHNT_TYPES" target="_blank">IDA_PHNT_TYPES</a> - Converted phnt (Native API header files from the System Informer project) to IDA TIL, IDC (Hex-Rays).</li>
<li><a href="https://gist.github.com/jborean93/0952263a902b8008cda506752a2f0a49" target="_blank">New-ScheduledTaskSession.ps1</a> - A way to execute code remotely in the context of a scheduled task process. PoC aims to bypass NETWORK logon limitations like the Windows Update API.</li>
<li><a href="https://github.com/grahamhelton/USP" target="_blank">USP</a> - Establishes persistence on a Linux system by creating a udev rule that triggers the execution of a specified payload (binary or script).</li>
<li><a href="https://github.com/dc401/rwgopack" target="_blank">rwgopack</a> - Example Linux based packer for ELF binaries that uses ZLib to compress and then XOR cipher single byte key the payload while creating a self unpacking binary.</li>
<li><a href="https://github.com/Slon104/Common-PIN-Analysis-from-haveibeenpwned.com" target="_blank">Common-PIN-Analysis-from-haveibeenpwned.com</a> - "I gathered data from haveibeenpwned.com for every common PIN and how often it is used. I am sharing with you a complete wordlist sorted by the most popular PINs first. Feel free to download it and test your favorite PIN to see how popular it is among everybody."</li>
<li><a href="https://github.com/infosecn1nja/VeilTransfer" target="_blank">VeilTransfer</a> - VeilTransfer is a data exfiltration utility designed to test and enhance the detection capabilities. This tool simulates real-world data exfiltration techniques used by advanced threat actors, allowing organizations to evaluate and improve their security posture.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Hacker-Hermanos/C2_INFRA_WORKSHOP_DEFCON32_RED_TEAM_VILLAGE" target="_blank">C2_INFRA_WORKSHOP_DEFCON32_RED_TEAM_VILLAGE</a> - C2 Infrastructure Automation. This repository contains the materials for the C2 Infrastructure Automation workshop at DEF CON 32 Red Team Village.</li>
<li><a href="https://github.com/SafeBreach-Labs/WindowsDowndate" target="_blank">WindowsDowndate</a> - A tool that takes over Windows Updates to craft custom downgrades and expose past fixed vulnerabilities.</li>
<li><a href="https://posts.specterops.io/navigating-the-uncharted-a-framework-for-attack-path-discovery-c5a0a020a144" target="_blank">Navigating the Uncharted: A Framework for Attack Path Discovery</a> - Elad Shamir presents a framework for discovering both known and unknown attack paths. Worth a read!</li>
<li><a href="https://www.infernux.no/SecurityMonitoringAntipatterns/" target="_blank">Security Monitoring Antipatterns</a> - This article discusses common antipatterns in security monitoring, such as overemphasizing data collection, focusing solely on network data, and chasing new technologies without addressing the basics. We see this all the time in environments. Client gets pwned while they have a bunch of "Advanced Monitoring" solutions but the basics just aren't there.</li>
<li><a href="https://github.com/OtterHacker/Conferences/tree/main/Defcon32" target="_blank">Conferences</a> DEF CON 32 workshop focused on the Windows DLL Loading internals.</li>
<li><a href="https://swarm.ptsecurity.com/inside-xerox-workcentre-two-unauthenticated-rces/" target="_blank">Inside Xerox WorkCentre: Two Unauthenticated RCEs</a> - Always a good day when you can persist off the printers!</li>
<li><a href="https://github.com/CyberLocosAI/Check-Point-SE-Lab" target="_blank">Check-Point-SE-Lab</a> - A multi-cloud, scalable, modular, IaC lab built with Python, Terraform, Ansible, and Docker.</li>
<li><a href="https://github.com/secureworks/BAADTokenBroker" target="_blank">BAADTokenBroker</a> - BAADTokenBroker is a post-exploitation tool designed to leverage device-stored keys (Device key, Transport key etc..) to authenticate to Microsoft Entra ID.</li>
<li><a href="https://github.com/pushsecurity/saas-attacks" target="_blank">saas-attacks</a> - Offensive security drives defensive security. We're sharing a collection of SaaS attack techniques to help defenders understand the threats they face. #nolockdown.</li>
<li><a href="https://evotec.xyz/mastering-active-directory-hygiene-automating-stale-computer-cleanup-with-cleanupmonster/" target="_blank">Mastering Active Directory Hygiene: Automating Stale Computer Cleanup with CleanupMonster</a> - A tool designed to help orgs track down and deal with old/stale Active Directory objects.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 432 (+0)</p>
<p>Blogs monitored: 386 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
