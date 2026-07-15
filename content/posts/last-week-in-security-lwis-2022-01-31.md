Title: Last Week in Security (LWiS) - 2022-01-31
Date: 2022-01-31 20:25
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-01-31
Author: Erik
Summary: pkexec Linux LPE (<a href="https://twitter.com/jogibharat" target="_blank">@jogibharat</a>), .NET remoting (<a href="https://twitter.com/codewhitesec" target="_blank">@codewhitesec</a>), usernames from CUCM (<a href="https://twitter.com/n00py1" target="_blank">@n00py1</a>), Notepad++ persistence (<a href="https://twitter.com/_RastaMouse" target="_blank">@_RastaMouse</a>), Mythic update (<a href="https://twitter.com/its_a_feature_" target="_blank">@its_a_feature_</a>), modern password spraying (<a href="https://twitter.com/sprocketsec" target="_blank">@SprocketSec</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-01-25 to 2022-01-31.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://blog.qualys.com/vulnerabilities-threat-research/2022/01/25/pwnkit-local-privilege-escalation-vulnerability-discovered-in-polkits-pkexec-cve-2021-4034" target="_blank">PwnKit: Local Privilege Escalation Vulnerability Discovered in polkit’s pkexec (CVE-2021-4034)</a>. Easily the biggest story of the last week. This is the <a href="https://dirtycow.ninja/" target="_blank">Dirty COW</a> of 2022, except even more stable and trivial to exploit. There are countless PoCs on github. <a href="https://github.com/moloch--/poc-cve-2021-4034" target="_blank">poc-cve-2021-4034</a> compiles nicely into a single executable.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://mrd0x.com/phishing-google-users-by-spoofing-previews/?no-cache=1" target="_blank">Custom Previews For Malicious Attachments</a>. This is a nice phishing technique that allows attackers to create fake previews for their malicious attachment with Google Mail using an intercepting proxy.</li>
<li><a href="https://rhinosecuritylabs.com/network-security/bypassing-little-snitch-firewall/" target="_blank">Bypassing Little Snitch Firewall with Empty TCP Packets</a>. Some nifty macOS tradecraft to bypass the popular client firewall. However, you'd have to bake this in to your initial access method or have advance knowledge of little snitch use.</li>
<li><a href="https://codewhitesec.blogspot.com/2022/01/dotnet-remoting-revisited.html" target="_blank">.NET Remoting Revisited</a>. This deprecated .NET architecture is still seen in older .NET projects, and this post breaks down how it works and how it can be exploited.</li>
<li><a href="https://www.ryanpickren.com/safari-uxss" target="_blank">Hacking the Apple Webcam (again)</a>. 4 0days combine to give an attacker full control over every website visited by the victim and camera access. This bug chain included a universal XSS and netted Ryan $100,500. Given the level of access achieved, that payout seems reasonable.</li>
<li><a href="https://www.n00py.io/2022/01/unauthenticated-dumping-of-usernames-via-cisco-unified-call-manager-cucm/" target="_blank">Unauthenticated Dumping of Usernames via Cisco Unified Call Manager (CUCM)</a>. If you've ever dealt with Cisco phone systems, this post will bring back memories. If not, stash it away for when you inevitably do.</li>
<li><a href="https://offensivedefence.co.uk/posts/notepad++/" target="_blank">Notepad++ Plugins for Persistence</a>. These types of semi-legitimate persistence are great and usually undetected.</li>
<li><a href="https://posts.specterops.io/mythic-2-3-an-interface-reborn-854c7803eca1" target="_blank">Mythic 2.3 — An Interface Reborn</a>. Mythic has become one of the major C2 players in the red team space thanks to its flexibility. This update looks great, and I look forward to trying out all the new features.</li>
<li><a href="https://www.sprocketsecurity.com/blog/how-to-bypass-mfa-all-day#" target="_blank">Password spraying and MFA bypasses in the modern security landscape</a>. You don't read much about password spraying these days, but done right it can be a useful technique. This post is a good example of how to spray correctly.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/DataDog/stratus-red-team" target="_blank">stratus-red-team</a> is "Atomic Red Team™" for the cloud, allowing to emulate offensive attack techniques in a granular and self-contained manner.</li>
<li><a href="https://github.com/ORCA666/T.D.P" target="_blank">T.D.P.</a> - Thread Description Poisoning uses SetThreadDescription and GetThreadDescription functions to hide the payload from memory scanners.</li>
<li><a href="https://github.com/KaLendsi/CVE-2022-21882" target="_blank">CVE-2022-21882</a> is the win32k LPE bypass CVE-2021-1732.</li>
<li><a href="https://github.com/S3cur3Th1sSh1t/NimGetSyscallStub" target="_blank">NimGetSyscallStub</a> gets fresh Syscalls from a fresh ntdll.dll copy. This code can be used as an alternative to the already published awesome tools NimlineWhispers and NimlineWhispers2 by @ajpc500 or ParallelNimcalls.</li>
<li><a href="https://github.com/dosxuz/DefenderStop" target="_blank">DefenderStop</a> is a C# project to stop the defender service using via token impersonation.</li>
<li><a href="https://github.com/carlospolop/PurplePanda" target="_blank">PurplePanda</a> fetches resources from different cloud/saas applications focusing on permissions in order to identify privilege escalation paths and dangerous permissions in the cloud/saas configurations. Note that PurplePanda searches both privileges escalation paths within a platform and across platforms.</li>
<li><a href="https://github.com/chvancooten/NimPackt-v1" target="_blank">NimPackt-v1</a> is a Nim-based packer for .NET (C#) executables and shellcode targeting Windows. It automatically wraps the payload in a Nim binary that is compiled to Native C and as such harder to detect and reverse engineer.</li>
<li><a href="https://github.com/utkusen/wholeaked" target="_blank">wholeaked</a>. s a file-sharing tool that allows you to find the responsible person in case of a leakage. I could see this being useful for sending multiple copies of phishing documents and seeing which ones end up on Virus Total or similar sites.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Mahlet-Inc/hobbits" target="_blank">hobbits</a> is a multi-platform GUI for bit-based analysis, processing, and visualization. This reminds me of the <a href="https://www.sweetscape.com/010editor/#templates" target="_blank">010 Editor</a> and its templates.</li>
<li><a href="https://github.com/Tw1sm/spraycharles" target="_blank">spraycharles</a> a low and slow password spraying tool, designed to spray on an interval over a long period of time.</li>
<li><a href="https://github.com/xm1k3/cent" target="_blank">cent</a> or Community edition nuclei templates, a simple tool that allows you to organize all the Nuclei templates offered by the community in one place.</li>
<li><a href="https://learnfrida.info/" target="_blank">Frida HandBook</a> is an amazing resource for all things binary instrumentation.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
