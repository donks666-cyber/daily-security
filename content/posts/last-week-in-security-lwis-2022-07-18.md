Title: Last Week in Security (LWiS) - 2022-07-18
Date: 2022-07-18 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-07-18
Author: Erik
Summary: Oauth hijacks (<a href="https://twitter.com/fransrosen" target="_blank">@fransrosen</a>), Macros are back, but also not (<a href="https://twitter.com/serghei" target="_blank">@serghei</a>), AD magic (<a href="https://twitter.com/_dirkjan" target="_blank">@_dirkjan</a>), Altiris for lateral movement (<a href="https://twitter.com/__invictus_" target="_blank">@__invictus_</a>), next level token stealing (<a href="https://twitter.com/HarmJ0y" target="_blank">@harmj0y</a>), xss to cread stealing (<a href="https://twitter.com/hoodoer" target="_blank">@hoodoer</a>), and more!

<aside class="m-note m-warning">
<h3>Catching up</h3>
<p>This is a rapid-fire 2 week recap - most entries will have no commentary. Regularly scheduled LWiS will return next week!</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-07-05 to 2022-07-18.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/microsoft/microsoft-rolls-back-decision-to-block-office-macros-by-default/" target="_blank">Microsoft rolls back decision to block Office macros by default</a>. If you are a big enough Microsoft customer you can escalate your trouble ticket all the way up to rolling back a security feature? VBA macros will continue to be a popular initial access vector it seems.</li>
<li><a href="https://pypi.org/security-key-giveaway/" target="_blank">PyPI 2FA Security Key Giveaway</a></li>
<li><a href="https://csrc.nist.gov/News/2022/pqc-candidates-to-be-standardized-and-round-4" target="_blank">PQC Standardization Process: Announcing Four Candidates to be Standardized, Plus Fourth Round Candidates</a></li>
<li><a href="https://www.apple.com/newsroom/2022/07/apple-expands-commitment-to-protect-users-from-mercenary-spyware/" target="_blank">Apple expands industry-leading commitment to protect users from highly targeted mercenary spyware</a>. Apple does <em>not</em> expand any ability to look at basic system logs from the phone though...</li>
<li><a href="https://www.ghacks.net/2022/07/17/facebook-has-started-to-encrypt-links-to-counter-privacy-improving-url-stripping/" target="_blank">Facebook has started to encrypt links to counter privacy-improving URL Stripping</a>.</li>
<li><a href="https://comsec.ethz.ch/wp-content/files/retbleed_sec22.pdf" target="_blank">[PDF] RETBLEED: Arbitrary Speculative Code Execution with Return Instructions</a></li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.signal-labs.com/blog/rediscovering-epic-games-0-days" target="_blank">Rediscovering Epic Games 0-Days (Forever Unpatched?)</a>. Installers are rich hunting ground for file overwrite/file delete vulnerabilities.</li>
<li><a href="https://labs.detectify.com/2022/07/06/account-hijacking-using-dirty-dancing-in-sign-in-oauth-flows/" target="_blank">Account hijacking using "dirty dancing" in sign-in OAuth-flows</a>. Oauth flows can be complicated, and thus vulnerable to strange edge cases. Excellent work here to explore some interesting ways to leak data and exploit login flows.</li>
<li><a href="https://pre.empt.dev/posts/maelstrom-etw-amsi/" target="_blank">Maelstrom: Working with AMSI and ETW for Red and Blue</a></li>
<li><a href="https://pre.empt.dev/posts/maelstrom-edr-kernel-callbacks-hooks-and-callstacks/" target="_blank">Maelstrom: EDR Kernel Callbacks, Hooks, and Call Stacks</a></li>
<li><a href="https://www.zerodayinitiative.com/blog/2022/7/13/cve-2022-30136-microsoft-windows-network-file-system-v4-remote-code-execution-vulnerability" target="_blank">CVE-2022-30136: Microsoft Windows Network File System v4 Remote Code Execution Vulnerability</a></li>
<li><a href="https://dirkjanm.io/abusing-forgotten-permissions-on-precreated-computer-objects-in-active-directory/" target="_blank">Abusing forgotten permissions on computer objects in Active Directory</a></li>
<li><a href="https://www.mdsec.co.uk/2022/07/altiris-methods-for-lateral-movement/" target="_blank">Altiris Methods for Lateral Movement</a></li>
<li><a href="https://www.inversecos.com/2022/07/heap-overflows-on-ios-arm64-heap.html" target="_blank">Heap Overflows on iOS ARM64: Heap Grooming, Use-After-Free (Part 3)</a></li>
<li><a href="https://simondotsh.com/infosec/2022/07/11/dirsync.html" target="_blank">DirSync: Leveraging Replication Get-Changes and Get-Changes-In-Filtered-Set</a></li>
<li><a href="https://idov31.github.io/2022-07-14-lord-of-the-ring0-p1/" target="_blank">Lord Of The Ring0 - Part 1 | Introduction</a></li>
<li><a href="https://www.microsoft.com/security/blog/2022/07/13/uncovering-a-macos-app-sandbox-escape-vulnerability-a-deep-dive-into-cve-2022-26706/" target="_blank">Uncovering a macOS App Sandbox escape vulnerability: A deep dive into CVE-2022-26706</a></li>
<li><a href="https://blog.sunggwanchoi.com/recreating-an-iso-payload-for-fun-and-no-profit/" target="_blank">Recreating an ISO Payload for Fun and No Profit</a></li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2278" target="_blank">Issue 2278: Windows: LSA Service LsapGetClientInfo Impersonation Level Check EoP</a></li>
<li><a href="https://rollingpwn.github.io/rolling-pwn/" target="_blank">Rolling Pwn Attack</a>. Honda keyless entry hack.</li>
<li><a href="https://posts.specterops.io/koh-the-token-stealer-41ca07a40ed6" target="_blank">Koh: The Token Stealer</a></li>
<li><a href="https://github.com/JetP1ane/Affinis" target="_blank">Affinis</a> Recurrent Neural Network SubDomain Discovery Tool</li>
<li><a href="https://gist.github.com/hoodoer/f58ac94755ba2faf5d971d4350a580ed" target="_blank">stealCredsPayload.js</a> from <a href="https://www.trustedsec.com/blog/scraping-login-credentials-with-xss/" target="_blank">Scraping Login Credentials With XSS</a>.</li>
<li><a href="https://github.com/mttaggart/crux" target="_blank">crux</a> A proof-of-concept malicious Chrome extension</li>
<li><a href="https://github.com/m3rcer/Chisel-Strike" target="_blank">Chisel-Strike</a> A .NET XOR encrypted cobalt strike aggressor implementation for chisel to utilize faster proxy and advanced socks5 capabilities.</li>
<li><a href="https://github.com/netero1010/RDPHijack-BOF" target="_blank">RDPHijack-BOF</a> Cobalt Strike Beacon Object File (BOF) that uses WinStationConnect API to perform local/remote RDP session hijacking.</li>
<li><a href="https://github.com/hackerhouse-opensource/iscsicpl_bypassUAC" target="_blank">iscsicpl_bypassUAC</a> UAC bypass for x64 Windows 7 - 11</li>
<li><a href="https://github.com/persistence-info/persistence-info.github.io" target="_blank">persistence-info.github.io</a> tries to gather an information about Windows persistence mechanisms to make the protection/detection more efficient. Most of the information is well known for years, being actively used within various scenarios.</li>
<li><a href="https://github.com/ChoiSG/OneDriveUpdaterSideloading" target="_blank">OneDriveUpdaterSideloading</a> Payload for DLL sideloading of the OneDriveUpdater.exe, based on the PaloAltoNetwork Unit42's blog post.</li>
<li><a href="https://github.com/Cracked5pider/CoffeeLdr" target="_blank">CoffeeLdr</a> Beacon Object File Loader.</li>
<li><a href="https://github.com/RedTeamPentesting/pretender" target="_blank">pretender</a>  Your MitM sidekick for relaying attacks featuring DHCPv6 DNS takeover as well as mDNS, LLMNR and NetBIOS-NS spoofing.</li>
<li><a href="https://github.com/aniqfakhrul/powerview.py" target="_blank">powerview.py</a> PowerView alternative.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.raycast.com/" target="_blank">Raycast</a> is a blazingly fast, totally extendable launcher. It lets you complete tasks, calculate, share common links, and much more.</li>
<li><a href="https://github.com/CervantesSec/cervantes" target="_blank">cervantes</a> is an opensource collaborative platform for pentesters or red teams who want to save time to manage their projects, clients, vulnerabilities and reports in one place.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 419 (+0)</p>
<p>Blogs monitored: 317 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
