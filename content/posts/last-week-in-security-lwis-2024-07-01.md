Title: Last Week in Security (LWiS) - 2024-07-01
Date: 2024-07-01 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-07-01
Author: Erik
Summary: Chrome RCE (<a href="https://x.com/mmolgtm" target="_blank">@mmolgtm</a>), Windows LPE (<a href="https://x.com/carrot_c4k3" target="_blank">@carrot_c4k3</a> + <a href="https://x.com/tykawaii98" target="_blank">@tykawaii98</a>), Xerox RCEs+LPE (<a href="https://x.com/_mohemiv" target="_blank">@_mohemiv</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-06-24 to 2024-07-01.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><p>regreSSHion (CVE-2024-6387)</p>
<blockquote>
<ul>
<li><a href="https://www.qualys.com/2024/07/01/cve-2024-6387/regresshion.txt" target="_blank">regreSSHion: RCE in OpenSSH's server, on glibc-based Linux systems (CVE-2024-6387)</a> - The Qualys team drops an unauthenticated remote code execution vulerability in OpenSSH, possibly the most audited software project ever. It's a race condition that takes ~10,000 attempts on x86 to exploit, so any type of <a href="https://github.com/fail2ban/fail2ban" target="_blank">fail2ban</a>, <a href="https://www.sshguard.net/" target="_blank">SSHGuard</a>, or similar protection will likely mitigate the vulnerability, but everyone should update ASAP. This one will have a long tail of exposure - SSH is everywhere. The OpenSSH project recently announced support for built in rate limiting: <a href="https://marc.info/?l=openbsd-cvs&amp;m=171769392207688&amp;w=2" target="_blank">PerSourcePenalties and PerSourcePenaltyExemptList</a> and the dates line up 🤔.</li>
<li><a href="https://dustri.org/b/notes-on-regresshion-on-musl.html" target="_blank">Notes on regreSSHion on musl</a> - "OpenSSH sshd on musl-based systems is not vulnerable to RCE via CVE-2024-6387 (regreSSHion)." However, it could still deadlock the sshd process.</li>
<li><a href="https://github.com/acrono/cve-2024-6387-poc" target="_blank">cve-2024-6387-poc</a> - UNVERIFIED! Do your own code review and testing. 32-bit PoC for CVE-2024-6387 — mirror of the original 7etsuo/cve-2024-6387-poc (Deleted).</li>
</ul>
</blockquote>
</li>
<li><p><a href="https://sansec.io/research/polyfill-supply-chain-attack" target="_blank">Polyfill supply chain attack hits 100K+ sites</a> - Polyfill[.]io was bought by a Chinese company ~6 months ago, but this attack looks more widespread: <a href="https://www.bleepingcomputer.com/news/security/polyfillio-bootcdn-bootcss-staticfile-attack-traced-to-1-operator/" target="_blank">Polyfill.io, BootCDN, Bootcss, Staticfile attack traced to 1 operator</a>. Cloudflare stepped in and autoamtically replaced <a href="https://blog.cloudflare.com/automatically-replacing-polyfill-io-links-with-cloudflares-mirror-for-a-safer-internet" target="_blank">polyfill.io links with Cloudflare's mirror for a safer Internet</a>.</p>
</li>
<li><p><a href="https://techcrunch.com/2024/06/27/portswigger-the-company-behind-the-burp-suite-of-security-testing-tools-swallows-112m/" target="_blank">PortSwigger, the company behind the Burp Suite of security testing tools, swallows $112M</a> - What does this mean against the Caido vs BurpSuite Pro debate? Congrats to PortSwigger nonetheless.</p>
</li>
<li><p><a href="https://www.bleepingcomputer.com/news/security/teamviewers-corporate-network-was-breached-in-alleged-apt-hack/" target="_blank">TeamViewer's corporate network was breached in alleged APT hack</a> - A very popular remote monitoring and management tool vendor breached. You can follow the security <a href="https://www.teamviewer.com/en/resources/trust-center/statement/?" target="_blank">update</a> here. Ouch.</p>
</li>
<li><p><a href="https://security.googleblog.com/2024/06/sustaining-digital-certificate-security.html" target="_blank">Sustaining Digital Certificate Security - Entrust Certificate Distrust</a> - Google Chrome will stop trusting Entrust root certificates in October. Why? See for yourself: <a href="https://bugzilla.mozilla.org/buglist.cgi?o2=greaterthaneq&amp;short_desc_type=casesubstring&amp;o1=notequals&amp;v1=Graveyard&amp;classification=Client%20Software&amp;classification=Developer%20Infrastructure&amp;classification=Components&amp;classification=Server%20Software&amp;classification=Other&amp;classification=Graveyard&amp;v2=2015-11-01&amp;f1=classification&amp;bug_status=UNCONFIRMED&amp;bug_status=NEW&amp;bug_status=ASSIGNED&amp;bug_status=REOPENED&amp;bug_status=RESOLVED&amp;bug_status=VERIFIED&amp;bug_status=CLOSED&amp;short_desc=Entrust&amp;f2=creation_ts&amp;component=CA%20Certificate%20Compliance&amp;query_format=advanced&amp;list_id=17064895" target="_blank">Entrust on Bugzilla</a>. The process to trust certificate authorites is one of those critical processes that underpins the entire system but almost no one acknowledges or understands (it's the <a href="https://en.wikipedia.org/wiki/Federal_Reserve" target="_blank">Federal Reserve</a> of cybersecurity).</p>
</li>
<li><p><a href="https://techcommunity.microsoft.com/t5/microsoft-entra-blog/introducing-the-microsoft-entra-powershell-module/ba-p/4173546" target="_blank">Introducing the Microsoft Entra PowerShell module</a> - Time to update your Azure/Entra tooling!</p>
</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://s4dbrd.com/evading-etw-based-detections/" target="_blank">Evading Event Tracing for Windows (ETW)-Based Detections</a> - This post explores Event Tracing for Windows (ETW), its components, and various techniques to evade ETW-based detections, including tampering with ETW trace sessions, hijacking sessions, and patching ETW functions to bypass endpoint detection and response systems. Good read!</li>
<li><a href="https://www.magonia.io/blog/commonly-abused-linux-access-detection-strategies" target="_blank">Commonly Abused Linux Initial Access Techniques and Detection Strategies</a> - Bring back linux tradecraft!</li>
<li><a href="https://github.blog/2024-06-26-attack-of-the-clones-getting-rce-in-chromes-renderer-with-duplicate-object-properties/" target="_blank">Attack of the clones: Getting RCE in Chrome's renderer with duplicate object properties</a> - Browsers are some of the most complex yet security critical peices of software available today. This post shows the details of an exploit that had to be re-worked due to code hardening, but still led to RCE from a single page visit.</li>
<li><a href="https://www.darknavy.org/blog/exploiting_steam_usual_and_unusual_ways_in_the_cef_framework/" target="_blank">Exploiting Steam: Usual and Unusual Ways in the CEF Framework</a> - Sometimes instead of attacking the browser itself, it's easier to attack the plumbing that connects it to the rest of the system.</li>
<li><a href="https://www.assetnote.io/resources/research/why-nested-deserialization-is-harmful-magento-xxe-cve-2024-34102" target="_blank">Why nested deserialization is harmful: Magento XXE (CVE-2024-34102)</a> - Another high impact CVE against Magento discovered by Assetnote.</li>
<li><a href="https://v3rtigo.org/posts/emux-ludus/" target="_blank">Creating an Emux Environment With Ludus</a> - Great walkthrough for those looking to get started with embedded hacking!</li>
<li><a href="https://www.troyhunt.com/the-state-of-data-breaches/" target="_blank">The State of Data Breaches</a> - Troy Hunt, owner of <a href="https://haveibeenpwned.com/" target="_blank">haveibeenpwned</a>  writes about what he's seeing across the industry.</li>
<li><a href="https://labs.jumpsec.com/putting-the-c2-in-c2loudflare/" target="_blank">Putting the C2 in C2loudflare</a> - How to bring up an entire C2 infrastructure with all your tooling and their corresponding redirectors using Azure Snapshots, Cloudflare and Tmux Resurrect.</li>
<li><a href="https://www.synacktiv.com/en/publications/github-actions-exploitation-introduction" target="_blank">Github Actions Exploitation: Introduction</a> - A basic introduction into Github action exploitation. Note: Github has an enterprise offering that can be hosted on-prem by large customers. Look for it on your next red team.</li>
<li><a href="https://googleprojectzero.blogspot.com/2024/06/the-windows-registry-adventure-3.html" target="_blank">The Windows Registry Adventure #3: Learning resources</a> - If you ever read a write-up and think "how in the world did they figure this out?" perhaps the answer is lots and lots of research. This post is a good example of how exploitation usually involves knowing a system better than most of its authors.</li>
<li><a href="https://swarm.ptsecurity.com/inside-xerox-workcentre-two-unauthenticated-rces/" target="_blank">Inside Xerox WorkCentre: Two Unauthenticated RCEs</a> - 2x RCEs and an LPE against a big Xerox multifunction machine.</li>
<li><a href="https://labs.watchtowr.com/auth-bypass-in-un-limited-scenarios-progress-moveit-transfer-cve-2024-5806/" target="_blank">Auth. Bypass In (Un)Limited Scenarios - Progress MOVEit Transfer (CVE-2024-5806)</a> - "Editors note: This blog post is everything - a beautiful vulnerability and a masterclass in fun exploitation chains." Agree.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Cipher7/ApexLdr" target="_blank">ApexLdr</a> - ApexLdr is a DLL Payload Loader written in C.</li>
<li><a href="https://github.com/CICADA8-Research/RemoteKrbRelay" target="_blank">RemoteKrbRelay</a> - Remote Kerberos Relay made easy! Advanced Kerberos Relay Framework.</li>
<li><a href="https://github.com/mertdas/SharpIncrease" target="_blank">SharpIncrease</a> - A Tool that aims to evade av with binary padding.</li>
<li><a href="https://github.com/tykawaii98/CVE-2024-30088" target="_blank">CVE-2024-30088</a> - A Windows LPE that stems from a Time-of-Check to Time-of-Use (TOCTOU) vulnerability within the function NtQueryInformationToken, particularly in the handling of the AuthzBasepCopyoutInternalSecurityAttributes function.</li>
<li><a href="https://github.com/ynwarcs/CVE-2023-24871" target="_blank">CVE-2023-24871</a> - POCs &amp; exploit for CVE-2023-24871 (Windows RCE + LPE).</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/khyrenz/parseusbs" target="_blank">parseusbs</a> - Parses USB connection artifacts from offline Registry hives.</li>
<li><a href="https://cerbersec.com/2024/06/30/becoming-a-red-teamer.html" target="_blank">Becoming a Red Teamer</a> - Recent changes in red team tooling has sparked a debate. Here is a quick take on the topic of what it takes to become a red teamer.</li>
<li><a href="https://www.thebirtproject.com/" target="_blank">The BIRT Project</a> - "Our goal is to support incident responders by providing them with effective tools that exceed their needs. As a 100% bootstrapped project, we are motivated by our extensive experience in cybersecurity and a deep understanding of the challenges faced in incident response. We recognize the need for quick and accurate responses in the face of today's changing threats. "</li>
<li><a href="https://nicholas.carlini.com/writing/2024/why-i-attack.html" target="_blank">Why I attack</a> - An perspective on why to do research and make your research public. Controversial topic but always good to stay informed and have these conversations.</li>
<li><a href="https://github.com/ChrisTitusTech/winutil" target="_blank">winutil</a> - Chris Titus Tech's Windows Utility - Install Programs, Tweaks, Fixes, and Updates.</li>
<li><a href="https://github.com/Raphire/Win11Debloat" target="_blank">Win11Debloat</a> - A simple, easy to use powershell script to remove bloatware apps from windows, disable telemetry, bing in windows search aswell as perform various other changes to declutter and improve your windows experience. This script works for both windows 10 and windows 11.</li>
<li><a href="https://github.com/vin01/poc-cve-2024-38396" target="_blank">poc-cve-2024-38396</a> - PoC for iTerm2 CVEs CVE-2024-38396 and CVE-2024-38395 which allow code execution.</li>
<li><a href="https://github.com/ergrelet/themida-unmutate" target="_blank">themida-unmutate</a> - Static deobfuscator for Themida/WinLicense/Code Virtualizer's mutation-based obfuscation.</li>
<li><a href="https://encore.dev/blog/queueing" target="_blank">Queueing - An interactive study of queueing strategies</a> - Neat interactive site to learn about queueing strategies.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 427 (+0)</p>
<p>Blogs monitored: 383 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
