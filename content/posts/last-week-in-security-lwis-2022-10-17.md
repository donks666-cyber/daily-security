Title: Last Week in Security (LWiS) - 2022-10-17
Date: 2022-10-17 22:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-10-17
Author: Erik
Summary: Cobalt Strike RCE (<a href="https://twitter.com/0x09AL" target="_blank">@0x09AL</a> + <a href="https://twitter.com/FuzzySec" target="_blank">@FuzzySec</a>), Docker Compose for red teams (<a href="https://twitter.com/buckinghamezra" target="_blank">@BuckinghamEzra</a>), portable malware (<a href="https://twitter.com/CaptMeelo" target="_blank">@CaptMeelo</a>), free root servers (<a href="https://twitter.com/hackerschoice" target="_blank">@hackerschoice</a>), LastPass tricks (<a href="https://twitter.com/rbmaslen" target="_blank">@rbmaslen</a>), practical attacks against NTLMv1 (<a href="https://twitter.com/n00py1" target="_blank">@n00py1</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-10-10 to 2022-10-17.</p>
<p>This week I reviewed 336 blog posts and 2350 tweets to find only the best and most relevant items to include here.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.cobaltstrike.com/blog/out-of-band-update-cobalt-strike-4-7-2/" target="_blank">Out Of Band Update: Cobalt Strike 4.7.2</a>. The rumors and tweets were true, there was RCE i 4.7.1. Read the full details in <a href="https://securityintelligence.com/posts/analysis-rce-vulnerability-cobalt-strike/" target="_blank">Analysis of a Remote Code Execution (RCE) Vulnerability in Cobalt Strike 4.7.1</a>. Here's a <a href="https://github.com/its-arun/CVE-2022-39197" target="_blank">PoC</a>.</li>
<li><a href="https://security.googleblog.com/2022/10/SecurityofPasskeysintheGooglePasswordManager.html" target="_blank">Security of Passkeys in the Google Password Manager</a>. GA later this year. With iOS/macOS already on board, nearly all mobile users will have passkeys by the end of the year. As services adopt FIDO2 solutions, offensive teams will have to adapt.</li>
<li><a href="https://www.sentinelone.com/labs/wip19-espionage-new-chinese-apt-targets-it-service-providers-and-telcos-with-signed-malware/" target="_blank">WIP19 Espionage | New Chinese APT Targets IT Service Providers and Telcos With Signed Malware</a>. APTs are using signed DLLs for DLL hijacking. Are you?</li>
<li><a href="https://twitter.com/GossiTheDog/status/1581973655453433856" target="_blank">Potential Log4shell situation</a>. Developing...</li>
<li><a href="https://blog.thc.org/disposable-root-servers" target="_blank">Disposable Root Servers</a>. This is the coolest thing I've seen in a long time. Or it's a honey pot. 50/50.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://ezrabuckingham.com/blog/deploying-containers-with-docker-compose/" target="_blank">DevAttackOps: Deploying Containers with Docker Compose (Part 3)</a>. DevOps and red teaming are friends - automate the boring stuff!</li>
<li><a href="https://www.directdefense.com/compromising-a-backup-system-by-iscsi-interface-during-a-routine-penetration-test/" target="_blank">Compromising a Backup System by iSCSI Interface During a Routine Penetration Test</a>. Don't sleep on those open iSCSI ports!</li>
<li><a href="https://gynvael.coldwind.pl/?id=754" target="_blank">Hello World under the microscope</a>. This is an interesting post that is the python version of "what does your computer do when you type google.com in a browser and hit enter."</li>
<li><a href="https://captmeelo.com//redteam/maldev/2022/10/17/independent-malware.html" target="_blank">Writing an Independent Malware</a>. Make your malware smaller (and import fewer DLLs) with the tricks in this post.</li>
<li><a href="https://www.mdsec.co.uk/2022/10/analysing-lastpass-part-1/" target="_blank">Analysing LastPass, Part 1</a>. The Chrome debugging protocol is very powerful and should be flagged by defenders any time it is invoked, but isn't (yet).</li>
<li><a href="https://www.n00py.io/2022/10/practical-attacks-against-ntlmv1/" target="_blank">Practical Attacks against NTLMv1</a>. Why work hard against good protocols when you can downgrade to NTLMv1?</li>
<li><a href="https://research.nccgroup.com/2022/10/17/toner-deaf-printing-your-next-persistence-hexacon-2022/" target="_blank">Toner Deaf - Printing your next persistence (Hexacon 2022)</a>. Go where the EDR isn't. Not only a remote root RCE, but also persistence. Very cool stuff.</li>
<li><a href="https://www.trustedsec.com/blog/set-up-an-android-hacking-lab-for-0/" target="_blank">Set up an Android Hacking Lab for $0</a>. While not as good as a physical device, an emulator will get you pretty far.</li>
<li><a href="https://pgj11.com/posts/Diamond-And-Sapphire-Tickets/" target="_blank">Diamond And Sapphire Tickets</a>. Gold is old. Upgrade your tickets to the latest precious gem.</li>
<li><a href="https://www.zscaler.com/blogs/security-research/technical-analysis-windows-clfs-zero-day-vulnerability-cve-2022-37969-part" target="_blank">Technical Analysis of Windows CLFS Zero-Day Vulnerability CVE-2022-37969 - Part 1: Root Cause Analysis</a>. A Windows privesc in the common log file system driver (CLFS.sys).</li>
<li><a href="https://cube0x0.github.io/Relaying-YubiKeys-Part-2/" target="_blank">Relaying YubiKeys Part 2</a>. I think this is the first code published that can actually interface with FIDO2 devices for phishing. Hardware tokens are good guards against phishing as they require an attacker to have access to the user's endpoint and the user and device must be present at/in the device when the attacker wants to use them OR the attacker has to control a subdomain of the valid site being targeted (if origins are not validated). This is a much more difficult situation for an attacker to achieve compared to a relatively simple MiTM proxy for TOTP or SMS 2FA on a look-a-like site. Code <a href="https://github.com/cube0x0/YubiKey-Relay" target="_blank">here</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/horizon3ai/CVE-2022-40684" target="_blank">CVE-2022-40684</a> - A proof of concept exploit for CVE-2022-40684 affecting Fortinet FortiOS, FortiProxy, and FortiSwitchManager.</li>
<li><a href="https://github.com/dr4k0nia/XorStringsNET" target="_blank">XorStringsNET</a> - Easy XOR string encryption for NET based binaries.</li>
<li><a href="https://github.com/akamai/akamai-security-research" target="_blank">akamai-security-research</a> - This repository includes code and IoCs that are the product of research done in Akamai's various security research teams. Includes a fresh Windows Workstation Service Elevation of Privilege Vulnerability.</li>
<li><a href="https://github.com/cisagov/RedEye" target="_blank">RedEye</a> - is a visual analytic tool supporting Red &amp; Blue Team operations from CISA.</li>
<li><a href="https://github.com/Warxim/CVE-2022-41852" target="_blank">CVE-2022-41852</a> - Remote Code Execution in JXPath Library (CVE-2022-41852) Proof of Concept.</li>
<li><a href="https://github.com/xpn/WAMBam" target="_blank">WAMBam</a> - Tooling related to the WAM Bam - Recovering Web Tokens From Office blog <a href="https://blog.xpnsec.com/wam-bam/" target="_blank">post</a>.</li>
<li><a href="https://github.com/OPENCYBER-FR/RustHound" target="_blank">RustHound</a> - Active Directory data collector for BloodHound written in rust. 🦀</li>
<li><a href="https://github.com/DarkCoderSc/PsyloDbg" target="_blank">PsyloDbg</a> is a very simple Windows Debugger that currently only monitor for debug events.</li>
<li><a href="https://github.com/SecureAuthCorp/impacket/pull/1425" target="_blank">Add SCCM NTLM Relay Attack #1425</a>. This is a little known but very cool attack I expect to work for decades to come.</li>
<li><a href="https://github.com/ORCx41/AtomPePacker" target="_blank">AtomPePacker</a> - A Highly capable Pe Packer.</li>
<li><a href="https://github.com/echtdefault/Janus" target="_blank">Janus</a> is a pre-build event that performs string obfuscation during compile time. This project is based off the CIA's Marble Framework.</li>
<li><a href="https://github.com/CCob/ProvisionAppx" target="_blank">ProvisionAppx</a>. Some fun lateral movement?!</li>
<li><a href="https://github.com/Dec0ne/ShadowSpray" target="_blank">ShadowSpray</a> - A tool to spray Shadow Credentials across an entire domain in hopes of abusing long forgotten GenericWrite/GenericAll DACLs over other objects in the domain.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://ohmygit.org/" target="_blank">Oh my Git! An open source game about learning Git!</a>. A resource for new (or even old) team members to help learn git.</li>
<li><a href="https://github.com/jonrau1/ElectricEye" target="_blank">ElectricEye</a> - Continuously monitor your AWS attack surface and evaluate services for configurations that can lead to degradation of confidentiality, integrity or availability. All results can be exported to Security Hub, JSON, CSV, Databases, and more for further aggregation and analysis.</li>
<li><a href="https://github.com/sensepost/wiresocks" target="_blank">wiresocks</a> A sock, with a wire, so you can tunnel all you desire. This is a great solution that may be even better than proxycap et al.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 421 (+0)</p>
<p>Blogs monitored: 326 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
