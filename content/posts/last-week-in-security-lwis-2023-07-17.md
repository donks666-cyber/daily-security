Title: Last Week in Security (LWiS) - 2023-07-17
Date: 2023-07-17 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-07-17
Author: Erik
Summary: Microsoft O365 was compromised for a few months for 25 customers, block EDR DLL loading (<a href="https://twitter.com/ShitSecure" target="_blank">@ShitSecure</a>), stashing shellcode in 3D models (<a href="https://twitter.com/TrustedSec" target="_blank">@TrustedSec</a>), AMSI bypasses (<a href="https://twitter.com/pfiatde" target="_blank">@pfiatde</a>), Atlassian Companion macOS RCE (<a href="https://twitter.com/_r3ggi" target="_blank">@_r3ggi</a>), the smallest C# binary (<a href="https://twitter.com/washi_dev" target="_blank">@washi_dev</a>), &gt;350 blogs monitored, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-07-10 to 2023-07-17.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.microsoft.com/en-us/security/blog/2023/07/14/analysis-of-storm-0558-techniques-for-unauthorized-email-access/" target="_blank">Analysis of Storm-0558 techniques for unauthorized email access</a>. This was the story of the week. TLDR stolen Microsoft account (MSA) consumer signing key (still unclear how it was stolen) was used to forge Azure AD tokens. This shouldn't be possible, but due to a bug in the Azure code it was. The actor used these forged tokens to pillage 25 private and US government unclassified Office365 accounts.</li>
<li><a href="https://unit42.paloaltonetworks.com/cve-2023-36884-rce/" target="_blank">CVE-2023-36884 - Microsoft Office and Windows HTML Remote Code Execution: Threat Brief (Updated)</a>. You have <a href="https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#attack-surface-reduction-rules-by-type" target="_blank">the attack surface reduction rule enabled</a> that blocks this (Block all Office applications from creating child processes) already, right?</li>
<li><a href="https://news.sophos.com/en-us/2023/07/11/microsoft-revokes-malicious-drivers-in-patch-tuesday-culling/" target="_blank">Microsoft Revokes Malicious Drivers in Patch Tuesday Culling</a>  Over 100 malicious drivers were revoked this month. 100 were signed by Microsoft themselves. 🤦</li>
<li><a href="https://www.lemonde.fr/en/france/article/2023/07/06/france-set-to-allow-police-to-spy-through-phones_6044269_7.html" target="_blank">France set to allow police to spy through phones</a>. "Covering laptops, cars and other connected objects as well as phones, the measure would allow the geolocation of suspects in crimes punishable by at least five years' jail. Devices could also be remotely activated to record sound and images of people suspected of terror offenses, as well as delinquency and organized crime." Curious how this will work with open source software/hardware. Will all devices sold in france require this backdoor? Will it then be illegal to use devices without the backdoor?</li>
<li><a href="https://therecord.media/senate-dea-bill-targets-end-to-end-encryption-requires-companies-to-report-drugs" target="_blank">Senate bill crafted with DEA targets end-to-end encryption, requires online companies to report drug activity</a>. Not to be outdone by France, the DEA tries to kill end-to-end encryption by including wording holding companies accountable for conduct they don't report if they “deliberately blind” themselves to the violations. Apple's latest iCloud encryption updates surely violate this. Hopefully their lobbying can stop this.</li>
<li><a href="https://www.first.org/cvss/calculator/4.0?utm_source=tldrsec.com" target="_blank">CVSS v4.0 calculator - PUBLIC PREVIEW</a>. Get those 9.8's ready!</li>
<li><a href="https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2023-0010" target="_blank">SonicWall GMS and Analytics affected by multiple vulnerabilities</a>. I just want 1 week where there isn't an edge security device with a 9+ CVSS bug...</li>
<li><a href="https://devblogs.microsoft.com/identity/aad-rebrand/" target="_blank">Azure AD is being renamed to Microsoft Entra ID</a>. You must get a bonus for a rename at Microsoft. Shoutout to the SMS/SCCM/MECM/ConfigMgr/Microsoft Endpoint Manager team. Hey, at least we get <a href="https://badoption.eu/blog/2023/07/12/entra_phish.html" target="_blank">Phishing PoC for Entra Rebranding</a>.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://code-white.com/blog/2023-07-from-blackbox-dotnet-remoting-to-rce/" target="_blank">From Blackbox .NET Remoting to Unauthenticated Remote Code Execution</a>. I respect the struggle to find obscure DLLs (he says, with two Windows Embedded installs running just to find DLLs).</li>
<li><a href="https://www.directdefense.com/tales-from-the-road-a-cyber-security-breach-is-only-a-phone-call-away/" target="_blank">Tales From the Road: A Cyber Security Breach is Only A Phone Call Away</a>. If you don't have a phone call capability (spoofing) in your red team offering, you are behind the curve as even <a href="https://www.scmagazine.com/brief/cybercrime/uber-revolut-hacks-perpetrated-by-teen-lapsus-member" target="_blank">teenagers</a> are doing it.</li>
<li><a href="https://s3cur3th1ssh1t.github.io/Cat_Mouse_or_Chess/" target="_blank">Cat &amp; Mouse - or Chess?</a>. What if you can hook the function in ntdll.dll that loads DLLs and prevent it from loading EDR dlls? A great question, and it turns out, you can!</li>
<li><a href="https://www.trustedsec.com/blog/modeling-malicious-code-hacking-in-3d/" target="_blank">Modeling Malicious Code: Hacking in 3D</a>. It's goofy, but why not store some shellcode in a 3D model?</li>
<li><a href="https://posts.specterops.io/performance-diagnostics-and-wmi-21f3e01790d3" target="_blank">Performance, Diagnostics, and WMI</a>. "Performance Monitor offers some interesting ways for attackers to extend their lateral movement or persistence opportunities by hijacking a service's performance DLL. With this, we gain a novel WMI lateral movement primitive and I do believe there is a lot more to be explored here." Grab the <a href="https://github.com/0xthirteen/PerfExec" target="_blank">PoC</a>.</li>
<li><a href="https://ssd-disclosure.com/ssd-advisory-edgerouters-and-aircube-miniupnpd-heap-overflow/" target="_blank">SSD Advisory - EdgeRouters and AirCube miniupnpd Heap Overflow</a>. It's LAN side, thankfully.</li>
<li><a href="https://www.kroll.com/en/insights/publications/cyber/ghostscript-cve-2023-36664-remote-code-execution-vulnerability" target="_blank">Proof of Concept Developed for Ghostscript CVE-2023-36664 Code Execution Vulnerability</a>. Update those LibreOffice installs.</li>
<li><a href="https://www.uptycs.com/blog/new-poc-exploit-backdoor-malware" target="_blank">PoC Exploit: Fake Proof of Concept with Backdoor Malware</a>. The disclaimer at the bottom of this post isn't just for fun.</li>
<li><a href="https://badoption.eu/blog/2023/07/15/divideconqer.html" target="_blank">Poch, Poch, is this thing on? Bypass AMSI with Divide &amp; Conquer</a>. Defender is the first level boss of any malware dev.</li>
<li><a href="https://www.wojciechregula.blog/post/macos-atlassian-companion-rce/" target="_blank">macOS Atlassian Companion Remote Code Execution</a>. Click edit on a confluence page, believe it or not, straight to RCE.</li>
<li><a href="https://blog.washi.dev/posts/tinysharp/" target="_blank">How small is the smallest .NET Hello World binary?</a>. 834 bytes (with additional trailing zero bytes). But boy are there some hacks to get there.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/EspressoCake/BOF_Development_Docker" target="_blank">BOF_Development_Docker</a> - A VSCode devcontainer for development of COFF files with batteries included.</li>
<li><a href="https://github.com/ldpreload/BlackLotus" target="_blank">BlackLotus</a> is an innovative UEFI Bootkit designed specifically for Windows. It incorporates a built-in Secure Boot bypass and Ring0/Kernel protection to safeguard against any attempts at removal.</li>
<li><a href="https://github.com/hfiref0x/WubbabooMark" target="_blank">WubbabooMark</a> - Debugger Anti-Detection Benchmark.</li>
<li><a href="https://github.com/CognisysGroup/HadesLdr" target="_blank">HadesLdr</a> - Shellcode Loader Implementing Indirect Dynamic Syscall, API Hashing, Fileless Shellcode retrieving using Winsock2.</li>
<li><a href="https://github.com/irsl/curlshell" target="_blank">curlshell</a> - reverse shell using curl.</li>
<li><a href="https://github.com/mvelazc0/BadZure" target="_blank">BadZure</a> - BadZure orchestrates the setup of Azure Active Directory tenants, populating them with diverse entities while also introducing common security misconfigurations to create vulnerable tenants with multiple attack paths.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/mertdas/PrivKit" target="_blank">PrivKit</a> is a simple beacon object file that detects privilege escalation vulnerabilities caused by misconfigurations on Windows OS.</li>
<li><a href="https://github.com/florylsk/RecycledInjector" target="_blank">RecycledInjector</a> - Native Syscalls Shellcode Injector.</li>
<li><a href="https://www.r-tec.net/r-tec-blog-resource-based-constrained-delegation.html" target="_blank">Resource Based Constrained Delegation - Practical Guide for Active Directory Privilege Escalation and Lateral Movement</a>. Very thorough article on RBCD.</li>
<li><a href="https://github.com/Mr-Un1k0d3r/Cookie-Graber-BOF" target="_blank">Cookie-Graber-BOF</a> - C or BOF file to extract WebKit master key to decrypt user cookie.</li>
<li><a href="https://github.com/namazso/MagicSigner" target="_blank">MagicSigner</a> - Signtool for expired certificates.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 352 (+4)</p>
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
