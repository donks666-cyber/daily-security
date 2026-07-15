Title: Last Week in Security (LWiS) - 2022-12-12
Date: 2022-12-12 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-12-12
Author: Erik
Summary: Apple data privacy, ChatGPT vs bug bounty, Syscall Hooks in Windows (<a href="https://twitter.com/Denis_Skvortcov" target="_blank">@Denis_Skvortcov</a>), SMSgate, Standalone Managed Service Accounts (<a href="https://twitter.com/simondotsh" target="_blank">@simondotsh</a>), StealthHook (<a href="https://twitter.com/x86matthew" target="_blank">@x86matthew</a>), and more!

<aside class="m-note m-warning">
<h3>year += 1</h3>
<p>This will be the last LWiS of 2022. See you next year!</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-12-05 to 2022-12-12.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.apple.com/newsroom/2022/12/apple-advances-user-security-with-powerful-new-data-protections/" target="_blank">Apple advances user security with powerful new data protections</a>. This is a great step forward for a company who has marketed "privacy" but technically had some work to do. While iMessage has always been end-to-end encrypted, iCloud backups, which contain all your iMessages conveniently have not been. Thus, with a simple court order, all your iPhone contents are available to any legally valid request. With this change, everything except Email, Contacts, and Calendar are encrypted on iCloud, rendering those data requests useless. iMessage Contact Key Verification feels a lot like Signal, and security key support for iCloud accounts is long overdue. While none of these steps are groundbreaking, Apple is pushing the boundaries for "mainstream" tech privacy.</li>
<li><a href="https://portswigger.net/daily-swig/chatgpt-bid-for-bogus-bug-bounty-is-thwarted" target="_blank">ChatGPT bid for bogus bug bounty is thwarted</a>. It was inevitable. Perhaps bugs will be triaged by AI soon, and the AIs can fight it out amongst themselves.</li>
<li><a href="https://www.theverge.com/2022/11/30/23486753/anker-eufy-security-camera-cloud-private-encryption-authentication-storage" target="_blank">Anker's Eufy lied to us about the security of its security cameras</a>. Last week's story was only about the notification image, but it appears that you could get an unencrypted stream URL from Eufy cameras that worked over the internet until recently. So much for local only. I repeat: Put your cameras on a VLAN without egress, and VPN in to view them - trust no one.</li>
<li><a href="https://r2c.dev/blog/2022/semgrep-release-v1-announcement/" target="_blank">Releasing Semgrep 1.0</a>. Now you have no excuse for not using it to find vulns.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://unit42.paloaltonetworks.com/next-gen-kerberos-attacks/" target="_blank">Precious Gemstones: The New Generation of Kerberos Attacks</a>. This is a great refresher if you have missed the last few Kerberos attack releases and need to catch up.</li>
<li><a href="https://the-deniss.github.io/posts/2022/12/08/hooking-system-calls-in-windows-11-22h2-like-avast-antivirus.html" target="_blank">Hooking System Calls in Windows 11 22H2 like Avast Antivirus. Research, analysis and bypass</a>. It boils down to an undocumented Windows kernel method and structure to implement syscall hooks. "This is a very brave and cool feature." This post contains good general investigative process documentation that will be applicable to kernel hackers and other low level devs.</li>
<li><a href="https://mayfly277.github.io/posts/GOADv2-pwning-part11/" target="_blank">GOAD - part 11 - ACL</a>. The latest in a series that walks through the excellent <a href="https://github.com/Orange-Cyberdefense/GOAD" target="_blank">GOAD</a> vulnerable active directory environment.</li>
<li><a href="https://www.synacktiv.com/en/publications/cool-vulns-dont-live-long-netgear-and-pwn2own.html" target="_blank">Cool vulns don't live long - Netgear and Pwn2Own</a>. Having two vulnerabilities patched the day before a competition is heartbreaking. Perhaps parallel discovery?</li>
<li><a href="https://googleprojectzero.blogspot.com/2022/12/exploiting-CVE-2022-42703-bringing-back-the-stack-attack.html" target="_blank">Exploiting CVE-2022-42703 - Bringing back the stack attack</a> "This exploit demonstrates a highly reliable and agnostic technique that can allow a broad spectrum of uncontrolled arbitrary write primitives to achieve kernel code execution on x86 platforms.""</li>
<li><a href="https://www.directdefense.com/part-3-i-hope-this-vishing-call-finds-you-well/" target="_blank">Part 3: I Hope This Vishing Call Finds You Well…</a>. Vishing can be that extra push to get a phishing campaign across the line. It is being used by adversaries to great effect already; consider adding it to your next service offering.</li>
<li><a href="https://research.nccgroup.com/2022/12/12/klee-for-the-cve/" target="_blank">Replicating CVEs with KLEE</a>. Symbolic execution engines for bug hunting aren't new, but <a href="https://klee.github.io/" target="_blank">KLEE</a> is new to me.</li>
<li><a href="https://www.pentagrid.ch/en/blog/open-source-sms-gateway-for-pentest-projects/" target="_blank">An open source SMS gateway for pentest projects</a>. <a href="https://github.com/pentagridsec/smsgate" target="_blank">smsgate</a> holds the code.</li>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2346" target="_blank">Issue 2346: Windows: HTTP.SYS Kerberos PAC Verification Bypass EoP</a>. A tasty LPE (now patched).</li>
<li><a href="https://simondotsh.com/infosec/2022/12/12/assessing-smsa.html" target="_blank">Assessing Standalone Managed Service Accounts</a>. Managed Service Accounts (MSA) have automatic password management, but that doesn't mean the passwords can't be dumped, hashes reused, and account privileges abused.</li>
<li><a href="https://www.x86matthew.com/view_post?id=stealth_hook" target="_blank">StealthHook - A method for hooking a function without modifying memory protection</a>. "This post describes a method for stealthily hooking a function without modifying memory protection. By overwriting a global pointer or virtual table entry that is nested within the target function, it is possible to hook the function without raising suspicion because many of these memory regions already have write permissions enabled."</li>
<li><a href="https://github.com/Cacti/cacti/security/advisories/GHSA-6p93-p743-35gf" target="_blank">Unauthenticated Command Injection (Cacti)</a>. An authentication bypass and a command injection combine for a deadly bug.</li>
<li><a href="https://i.blackhat.com/EU-22/Thursday-Briefings/EU-22-Fitzl-Knockout-Win-Against-TCC.pdf" target="_blank">[PDF] Knockout win against TCC, a.k.a. 20+ NEW ways to bypass your macOS privacy mechanisms</a>. Two of the best macOS security researchers team up to take down TCC.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/kleiton0x00/RedditC2" target="_blank">RedditC2</a> - Abusing Reddit API to host the C2 traffic, since most of the blue-team members use Reddit, it might be a great way to make the traffic look legit.</li>
<li><a href="https://github.com/lucasmccabe/emailGPT" target="_blank">emailGPT</a> - a quick and easy interface to generate emails with ChatGPT.</li>
<li><a href="https://github.com/praetorian-inc/noseyparker" target="_blank">noseyparker</a>  is a command-line program that finds secrets and sensitive information in textual data and Git history.</li>
<li><a href="https://github.com/gmh5225/CVE-2022-44721-CsFalconUninstaller" target="_blank">CVE-2022-44721 Crowdstrike Falcon Uninstaller</a>.</li>
<li><a href="https://github.com/zcgonvh/DCOMPotato" target="_blank">DCOMPotato</a> - Exploit collection for some Service DCOM Object local privilege escalation vulnerabilities (SeImpersonatePrivilege abuse).</li>
<li><a href="https://github.com/CodeXTF2/WindowSpy" target="_blank">WindowSpy</a> is a Cobalt Strike Beacon Object File meant for targetted user surveillance. The goal of this project was to trigger surveillance capabilities only on certain targets, e.g. browser login pages, confidential documents, vpn logins etc.</li>
<li><a href="https://github.com/sandialabs/wiretap" target="_blank">Wiretap</a> is a transparent, VPN-like proxy server that tunnels traffic via WireGuard and requires no special privileges to run.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/SikretaLabs/BlueMap" target="_blank">BlueMap</a> helps penetration testers and red teamers to perform Azure auditing, discovery &amp; enumeration, and exploitation in interactive mode that saves complex opsec and overhead that usually exists in Azure penetration testing engagements.</li>
<li><a href="https://objectifsecurite.gitlab.io/tproxy/" target="_blank">TProxy</a> is an interception proxy for TCP traffic. It can be used to monitor, drop, modify or inject packets in an existing TCP connection. For monitoring purposes, TProxy has the ability to decrypt incoming TLS traffic and re-encrypt outgoing packets. It also leverages Wireshark dissectors to build a dissection tree of each intercepted packet.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 422 (+1)</p>
<p>Blogs monitored: 330 (+3)</p>
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
