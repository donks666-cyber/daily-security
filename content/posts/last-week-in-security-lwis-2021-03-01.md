Title: Last Week in Security (LWiS) - 2021-03-01
Date: 2021-03-01 23:50
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-03-01
Author: Erik
Summary: JSON interop vulns (<a href="https://twitter.com/theBumbleSec" target="_blank">@theBumbleSec</a>), PHPWind RCE presentation (<a href="https://twitter.com/orange_8361" target="_blank">@orange_8361</a>), infra automation (<a href="https://twitter.com/cedowens" target="_blank">@cedowens</a>), AMSI knowledge (<a href="https://twitter.com/ShitSecure" target="_blank">@ShitSecure</a>), actual magic (<a href="https://twitter.com/justinetunney" target="_blank">@JustineTunney</a>), modular password spraying (<a href="https://twitter.com/0xZDH" target="_blank">@0xZDH</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-02-22 to 2021-03-01.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://swarm.ptsecurity.com/unauth-rce-vmware/" target="_blank">Unauthorized RCE in VMware vCenter</a>. If you haven't patched your vCenter and it's <a href="https://www.shodan.io/search?query=http.title:%22ID_VC_Welcome%22" target="_blank">exposed to the internet</a> (why!?), you may want to start incident response. To make it worse, this unauthenticated RCE gets you SYSTEM on windows based vCenters, and the PhotonOS based Linux appliance is <a href="https://twitter.com/steventseeley/status/1364975734545149957" target="_blank">vulnerable to the recent sudo heap overflow</a>. <a href="https://github.com/horizon3ai/CVE-2021-21972" target="_blank">PoCs</a> <a href="https://github.com/QmF0c3UK/CVE-2021-21972-vCenter-6.5-7.0-RCE-POC" target="_blank">have</a> <a href="https://github.com/NS-Sp4ce/CVE-2021-21972" target="_blank">dropped</a>.</li>
<li><a href="https://www.kali.org/blog/kali-linux-2021-1-release/" target="_blank">Kali Linux 2021.1 Release (Command-Not-Found)</a>. The go-to offensive security distro has its first release of 2021. There are a bunch of small updates and new tools, but the coolest new feature is the two new sponsorships (BC Security and ffuf author Joohoi). I like this model that supports open source tool authors!</li>
<li><a href="https://krebsonsecurity.com/2021/03/is-your-browser-extension-a-botnet-backdoor/" target="_blank">Is Your Browser Extension a Botnet Backdoor?</a> Krebs breaks down the "Infatica" residential proxy model that relies on "participating" browser extensions. As more and more sensitive information moves to browsers, extensions will become bigger targets - <a href="https://www.proofpoint.com/us/blog/threat-insight/ta413-leverages-new-friarfox-browser-extension-target-gmail-accounts-global" target="_blank">believe me</a>.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://labs.bishopfox.com/tech-blog/an-exploration-of-json-interoperability-vulnerabilities" target="_blank">An Exploration of JSON Interoperability Vulnerabilities</a>. Like any standard, there are many ways to parse JSON. When multiple services are used in a product and their parsers differ interesting vulnerabilities can pop up. This post is very thorough, and even has <a href="https://github.com/BishopFox/json-interop-vuln-labs/" target="_blank">labs</a> for you to follow along and try things out. Very cool.</li>
<li><a href="https://blog.orange.tw/2021/02/a-journey-combining-web-and-binary-exploitation.html" target="_blank">A Journey Combining Web Hacking and Binary Exploitation in Real World!</a> The master of unauthenticated remote code execution exploits is back - this time with a full explanation of a PHPWind RCE. This combines web app techniques with classic binary exploitation for shells.</li>
<li><a href="https://www.synacktiv.com//en/publications/pwn2own-tokyo-2020-defeating-the-tp-link-ac1750.html" target="_blank">Pwn2Own Tokyo 2020: Defeating the TP-Link AC1750</a>. A mix of hardware hacking and binary exploitation come together for an unauthenticated root RCE on the LAN side of the TP-Link AC1750 router.</li>
<li><a href="https://medium.com/red-teaming-with-a-blue-team-mentaility/infra-automation-primer-red-team-edition-b4c613308beb" target="_blank">Infra Automation Primer (Red Team Edition)</a>. If you are tired of setting up infrastructure for your red team engagements by hand, this primer will get you started with bash and terraform.</li>
<li><a href="https://s3cur3th1ssh1t.github.io/Powershell-and-the-.NET-AMSI-Interface/" target="_blank">The difference between Powershell only &amp; process specific AMSI bypasses</a>. If you have ever bypassed Powershell AMSI only to have your loaded .NET blocked, this post explains why and offers a solution.</li>
<li><a href="https://www.tenable.com/security/research/tra-2021-07" target="_blank">Dell EMC OpenManage Server Administrator Authentication Bypass</a>. This "simple" auth bypass cleverly uses the "Manage Remote Node" feature and points it to localhost to bypass auth checks and get a valid, logged-in session cookie.</li>
<li><a href="https://isc.sans.edu/forums/diary/Unprotecting+Malicious+Documents+For+Inspection/27126/" target="_blank">Unprotecting Malicious Documents For Inspection</a>. Malicious documents often password protect their VBA code. However, in order for the document to be portable, the hashed password must be in the document as well. If you can find that hash and replace it with a known hash, you now know the password to the VBA!</li>
<li><a href="https://sec.stealthcopter.com/cve-2020-28243/" target="_blank">CVE-2020-28243 SaltStack Minion Local Privilege Escalation</a>. SaltStack has had some pretty <a href="https://gist.github.com/SwitHak/8e7fa45b5656c691ddf13c8c47e8fda6" target="_blank">serious vulnerabilities</a> over the years, so this LPE seems quant in comparison, but could give root access to an user on a machine managed by Salt.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/3ndG4me/spraygen" target="_blank">spraygen</a> is a password list generator for password spraying - prebaked with goodies like sports team names, seasons, years, etc.</li>
<li><a href="https://github.com/S4R1N/BadOutlook" target="_blank">BadOutlook</a> is a simple PoC which leverages the Outlook Application Interface (COM Interface) to execute shellcode on a system based on a specific trigger subject line. This can be used to build an Entire C2 Framework that relies on E-Mails as a mean of communication (Where the Implant never speaks to the internet directly).</li>
<li><a href="https://github.com/neex/1u.ms" target="_blank">1u.ms</a> is a small set of zero-configuration DNS utilities for assisting in detection and exploitation of SSRF-related vulnerabilities. It provides easy to use DNS rebinding utility, as well as a way to get resolvable resource records with any given contents. A hosted version is available at <a href="http://1u.ms/" target="_blank">1u.ms</a>. You may want to protect the <cite>/last</cite> and <cite>/log</cite> endpoints if self-hosting.</li>
<li><a href="https://github.com/cribdragg3r/Alaris" target="_blank">Alaris</a> is not technically a new tool (LWiS 2020-10-19), but it has had a major update to use direct syscalls with <a href="https://github.com/jthuraisamy/SysWhispers2" target="_blank">SysWhispers2</a>, a new builder, and new dynamic encryption primitives.</li>
<li><a href="https://justine.lol/redbean/index.html" target="_blank">redbean - single-file distributable web server</a>. This is both a zip file that contains all content that is served and a truly cross platform (Windows, Linux, MacOS, and BSD) binary webserver. This may be actual magic.</li>
<li><a href="https://github.com/ChaitanyaHaritash/Callback_Shellcode_Injection" target="_blank">Callback_Shellcode_Injection</a> contains POCs for shellcode injection via callbacks. These uncommon API calls are likely much less monitored than standard methods of shellcode injection (although they still use VirtualAlloc).</li>
<li><a href="https://github.com/grines/goc2" target="_blank">goc2</a> is a new macOS post exploitation C2 framework. Pairs with <a href="https://github.com/grines/goc2-agent/blob/main/mac/agent.go" target="_blank">goc2-agent</a>.</li>
<li><a href="https://github.com/0xZDH/Omnispray" target="_blank">Omnispray</a> aims to replace tools such as o365spray and provide a modular framework to expand enumeration and spraying beyond just a single target/application.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/brittonhayes/pillager" target="_blank">pillager</a> is designed to provide a simple means of leveraging Go's strong concurrency model to recursively search directories for sensitive information in files. Once pillager finds files that match the specified pattern, the file is scanned using a series of concurrent workers that each take a line of the file from the job queue and hunt for sensitive pattern matches. The available pattern filters can be defined in a rules.toml file or you can use the default ruleset.</li>
<li><a href="https://github.com/deepinstinct/LsassSilentProcessExit" target="_blank">LsassSilentProcessExit</a> is a new method of causing WerFault.exe to dump lsass.exe process memory to disk for credentials extraction via silent process exit mechanism without crashing lsass.exe.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
