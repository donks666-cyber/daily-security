Title: Last Week in Security (LWiS) - 2023-06-15
Date: 2023-06-15 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-06-15
Author: Erik
Summary: A months worth of news, techniques, tools and exploits!

<aside class="m-note m-warning">
<h3>Catching up</h3>
<p>This is a rapid-fire 3 week recap - most entries will have no commentary. Regularly scheduled LWiS will return 2023-06-26!</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week(s). This post covers 2023-05-22 to 2023-06-15.</p>
<section id="news">
<h2>News</h2>
<p>MOVEIt</p>
<blockquote>
<ul>
<li><a href="https://blog.assetnote.io/2023/06/07/moveit-transfer-patch-diff-adventure/" target="_blank">Patch Diffing Progress MOVEIt Transfer RCE (CVE-2023-34362)</a></li>
<li><a href="https://blog.assetnote.io/2023/06/13/moveit-transfer-part-two/" target="_blank">MOVEIt Transfer RCE Part Two (CVE-2023-34362)</a></li>
<li><a href="https://www.praetorian.com/blog/moveit-vulnerability/" target="_blank">MOVEit! An Overview of CVE-2023-34362</a></li>
<li><a href="https://unit42.paloaltonetworks.com/threat-brief-moveit-cve-2023-34362/" target="_blank">CVE-2023-34362: MOVEit Transfer SQL Injection Vulnerability Threat Brief (Updated)</a></li>
<li><a href="https://www.horizon3.ai/moveit-transfer-cve-2023-34362-deep-dive-and-indicators-of-compromise/" target="_blank">MOVEit Transfer CVE-2023-34362 Deep Dive and Indicators of Compromise</a></li>
</ul>
</blockquote>
<ul>
<li><a href="https://krebsonsecurity.com/2023/06/barracuda-urges-replacing-not-patching-its-email-security-gateways/" target="_blank">Barracuda Urges Replacing — Not Patching — Its Email Security Gateways</a>. Yikes.</li>
<li><a href="https://www.fortinet.com/blog/psirt-blogs/analysis-of-cve-2023-27997-and-clarifications-on-volt-typhoon-campaign" target="_blank">Analysis of CVE-2023-27997 and Clarifications on Volt Typhoon Campaign</a>. Also yikes.</li>
<li><a href="https://securelist.com/operation-triangulation/109842/" target="_blank">Operation Triangulation: iOS devices targeted with previously unknown malware</a>. Related: <a href="https://www.vice.com/en/article/ak33w8/russian-fsb-accuses-us-of-hacking-thousands-of-iphones-in-russia" target="_blank">Russian FSB Accuses U.S. of Hacking Thousands of iPhones in Russia</a></li>
<li><a href="https://security.googleblog.com/2023/06/announcing-chrome-browser-full-chain.html" target="_blank">Announcing the Chrome Browser Full Chain Exploit Bonus</a>. $180,000 for a full chain Chrome exploit? Seems low.</li>
<li><a href="https://security.googleblog.com/2023/05/time-to-challenge-yourself-in-2023-google-ctf2023.html" target="_blank">Time to challenge yourself in the 2023 Google CTF!</a></li>
<li><a href="https://security.googleblog.com/2023/05/google-trust-services-acme-api_0503894189.html" target="_blank">Google Trust Services ACME API available to all users at no cost</a></li>
<li><a href="https://www.kali.org/blog/kali-linux-2023-2-release/" target="_blank">Kali Linux 2023.2 Release (Hyper-V &amp; PipeWire)</a></li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/" target="_blank">Volt Typhoon targets US critical infrastructure with living-off-the-land techniques</a></li>
<li><a href="https://www.mandiant.com/resources/blog/vmware-esxi-zero-day-bypass" target="_blank">VMware ESXi Zero-Day Used by Chinese Espionage Actor to Perform Privileged Guest Operations on Compromised Hypervisors</a></li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.doyensec.com//2023/06/13/messing-around-with-aws-batch-for-privilege-escalations.html" target="_blank">Messing Around With AWS Batch For Privilege Escalations</a></li>
<li><a href="https://secret.club/2023/06/05/spoof-pe-sections.html" target="_blank">Abusing undocumented features to spoof PE section headers</a></li>
<li><a href="https://github.blog/2023-06-15-codeql-zero-to-hero-part-2-getting-started-with-codeql/" target="_blank">CodeQL zero to hero part 2: getting started with CodeQL</a></li>
<li><a href="https://gts3.org/assets/papers/2023/jeong:utopia.pdf" target="_blank">[PDF] UTOPIA: Automatic Generation of Fuzz Driver using Unit Tests</a>. Finally a paper that actually released the <a href="https://github.com/Samsung/UTopia" target="_blank">source code</a>.</li>
<li><a href="https://portswigger.net/research/how-i-choose-a-security-research-topic" target="_blank">How I choose a security research topic</a></li>
<li><a href="https://bishopfox.com/blog/exploit-cve-2022-42475" target="_blank">A More Complete Exploit for Fortinet CVE-2022-42475</a></li>
<li><a href="https://www.securesystems.de/blog/active-directory-spotlight-attacking-the-microsoft-configuration-manager/" target="_blank">Active Directory Spotlight: Attacking The Microsoft Configuration Manager (SCCM/MECM)</a>. Don't skip this one.</li>
<li><a href="https://dirkjanm.io/obtaining-domain-admin-from-azure-ad-via-cloud-kerberos-trust/" target="_blank">Obtaining Domain Admin from Azure AD by abusing Cloud Kerberos Trust</a></li>
<li><a href="https://labs.jumpsec.com/ligolo-quality-of-life-on-red-team-engagements/" target="_blank">Ligolo: Quality of Life on Red Team Engagements</a></li>
<li><a href="https://lockboxx.blogspot.com/2023/05/red-team-story-time.html" target="_blank">Red Team Story Time!</a>. You don't even need code execution to get impactful data compromise.</li>
<li><a href="https://jhftss.github.io/CVE-2022-32902-Patch-One-Issue-and-Introduce-Two/" target="_blank">CVE-2022-32902: Patch One Issue and Introduce Two</a></li>
<li><a href="https://summoning.team/blog/vmware-vrealize-network-insight-rce-cve-2023-20887/" target="_blank">Pre-authenticated RCE in VMware vRealize Network Insight CVE-2023-20887</a></li>
<li><a href="https://posts.specterops.io/understanding-telemetry-kernel-callbacks-1a97cfcb8fb3" target="_blank">Understanding Telemetry: Kernel Callbacks</a></li>
<li><a href="https://posts.specterops.io/less-smartscreen-more-caffeine-ab-using-clickonce-for-trusted-code-execution-1446ea8051c5" target="_blank">Less SmartScreen More Caffeine: (Ab)Using ClickOnce for Trusted Code Execution</a>. Great "new" initial access method.</li>
<li><a href="https://blog.stratumsecurity.com/2023/06/01/sqli-the-road-to-bypassing-an-industry-leading-waf/" target="_blank">Bypassing An Industry-Leading WAF and Exploiting SQLi</a></li>
<li><a href="https://www.trustedsec.com/blog/onedrive-to-enum-them-all/" target="_blank">OneDrive to Enum Them All</a></li>
<li><a href="https://voidsec.com/reverse-engineering-terminator-aka-zemana-antimalware-antilogger-driver/" target="_blank">Reverse Engineering Terminator aka Zemana AntiMalware/AntiLogger Driver</a></li>
<li><a href="https://hackcompute.com/hacking-epp-servers/" target="_blank">can I speak to your manager? hacking root EPP servers to take control of zones</a></li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://cvexploits.io/" target="_blank">CVExploits Search</a> - Your comprehensive database for CVE exploits from across the internet.</li>
<li><a href="https://github.com/BishopFox/cloudfoxable" target="_blank">cloudfoxable</a> - Create your own vulnerable by design AWS penetration testing playground.</li>
<li><a href="https://github.com/Occamsec/CVE-2023-2825" target="_blank">CVE-2023-2825</a> - GitLab CVE-2023-2825 PoC. This PoC leverages a path traversal vulnerability to retrieve the /etc/passwd file from a system running GitLab 16.0.0.</li>
<li><a href="https://github.com/sinsinology/CVE-2023-20887" target="_blank">CVE-2023-20887</a> - VMWare vRealize Network Insight Pre-Authenticated RCE (CVE-2023-20887).</li>
<li><a href="https://github.com/g3tsyst3m/elevationstation" target="_blank">elevationstation</a> - elevate to SYSTEM any way we can!</li>
<li><a href="https://github.com/DarkCoderSc/SharpFtpC2" target="_blank">SharpFtpC2</a> - A Streamlined FTP-Driven Command and Control Conduit for Interconnecting Remote Systems.</li>
<li><a href="https://github.com/ThatLing/limba" target="_blank">limba</a> - compile-time control flow obfuscation using mba.</li>
<li><a href="https://github.com/eversinc33/Banshee" target="_blank">Banshee</a> - Experimental Windows x64 Kernel Driver/Rootkit.</li>
<li><a href="https://github.com/S12cybersecurity/RDPCredentialStealer" target="_blank">RDPCredentialStealer</a> - steals credentials provided by users in RDP using API Hooking with Detours in C++.</li>
<li><a href="https://github.com/WKL-Sec/HiddenDesktop" target="_blank">HiddenDesktop</a> - HVNC for Cobalt Strike.</li>
<li><a href="https://github.com/Octoberfest7/DropSpawn_BOF" target="_blank">DropSpawn_BOF</a> - CobaltStrike BOF to spawn Beacons using DLL Application Directory Hijacking.</li>
<li><a href="https://github.com/ZeroMemoryEx/Terminator" target="_blank">Terminator</a> - Reproducing Spyboy technique to terminate all EDR/XDR/AVs processes.</li>
<li><a href="https://github.com/b1-team/superman" target="_blank">superman</a> - Kill processes protected by antivirus during offensive activities.</li>
<li><a href="https://github.com/ZeroMemoryEx/Blackout" target="_blank">Blackout</a> - kill anti-malware protected processes (BYOVD).</li>
<li><a href="https://github.com/Kudaes/EPI" target="_blank">EPI</a> - Process injection through entry points hijacking.</li>
<li><a href="https://github.com/S3cur3Th1sSh1t/Ruy-Lopez" target="_blank">Ruy-Lopez</a> This repository contains the Proof-of-Concept(PoC) for a new approach to completely prevent DLLs from being loaded into a newly spawned process.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/dmaasland/mcfridafee" target="_blank">mcfridafee</a></li>
<li><a href="https://github.com/makeplane/plane" target="_blank">plane</a> - Open Source JIRA, Linear and Height Alternative. Plane helps you track your issues, epics, and product roadmaps in the simplest way possible.</li>
<li><a href="https://github.com/naksyn/PythonMemoryModule" target="_blank">PythonMemoryModule</a> - pure-python implementation of MemoryModule technique to load dll and unmanaged exe entirely from memory.</li>
<li><a href="https://github.com/avito-tech/deepsecrets" target="_blank">deepsecrets</a> -  Secrets scanner that understands code.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 347 (+3)</p>
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
