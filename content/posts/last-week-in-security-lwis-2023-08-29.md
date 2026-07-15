Title: Last Week in Security (LWiS) - 2023-08-29
Date: 2023-08-29 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-08-29
Author: Erik
Summary: DEF CON 31 tools and so much more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-08-07 to 2023-08-29.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://techcommunity.microsoft.com/t5/microsoft-365-blog/introducing-python-in-excel-the-best-of-both-worlds-for-data/ba-p/3905482" target="_blank">Introducing Python in Excel: The Best of Both Worlds for Data Analysis and Visualization</a>. Looks like macros are back on the menu!</li>
<li><a href="https://www.youtube.com/c/x33fcon" target="_blank">X33fcon talks</a>. Some good talks this year as usual.</li>
<li><a href="https://techcommunity.microsoft.com/t5/microsoft-365-defender-blog/microsoft-defender-for-identity-expands-its-coverage-with-new-ad/ba-p/3894215" target="_blank">Microsoft Defender for Identity expands its coverage with new AD CS sensor!</a>. Yes but you have to pay 💰</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.bitsadmin.com/living-off-the-foreign-land-windows-as-offensive-platform" target="_blank">Living Off the Foreign Land</a>. As EDR gets better, the move is to simply get a reverse SOCKS agent on a target machine and run all the "malware" on the comfort of your own machine. This series is a great intro to the world of "living off the foreign land."</li>
<li><a href="https://app.docguard.io/examples" target="_blank">Real World Examples: The top AVs in the world missed all of these attacks</a>. Some excellent examples of real world phishing documents that are currently getting past most AV.</li>
<li><a href="https://research.nccgroup.com/2023/08/22/dancing-offbit-the-story-of-a-single-character-typo-that-broke-a-chacha-based-prng/" target="_blank">Dancing Offbit: The Story of a Single Character Typo that Broke a ChaCha-Based PRNG</a>. Those bitwise operations will bite ya.</li>
<li><a href="https://portswigger.net/research/smashing-the-state-machine" target="_blank">Smashing the state machine: the true potential of web race conditions</a>. Paper by <a href="https://twitter.com/albinowax" target="_blank">@albinowax</a>  discussing the impact of race conditions and real world use cases (like gitlab) of exploitation.</li>
<li><a href="https://blog.xpnsec.com/lapsv2-internals/" target="_blank">LAPS 2.0 Internals</a>. <a href="https://twitter.com/_xpn_" target="_blank">@_xpn_</a> Dropping some knowledge on how LAPS 2.0 works along with BOF code 🫶.</li>
<li><a href="https://www.binarydefense.com/resources/blog/demystifying-dll-hijacking-understanding-the-intricate-world-of-dynamic-link-library-attacks/" target="_blank">Demystifying DLL Hijacking</a>. Some insight into some DLL Hijacking detection logic and methodology.</li>
<li><a href="https://shorsec.io/blog/dll-notification-injection/" target="_blank">DLL Notification Injection</a>. New “threadless” process injection technique that works by utilizing the concept of DLL Notification Callbacks in local and remote processes.</li>
<li><a href="https://github.com/nyxgeek/track_the_planet/blob/main/nyxgeek_Track_the_Planet_2023.08.14.pdf" target="_blank">Track The Planet</a>. Super cool talk from DEF CON 31. How username enumeration via the Microsoft cloud leads to tracking the world. Talk title is 👌</li>
<li><a href="https://www.pentestpartners.com/security-blog/a-broken-marriage-abusing-mixed-vendor-kerberos-stacks/" target="_blank">A broken marriage. Abusing mixed vendor Kerberos stacks</a>. DEF CON 31 talk -&gt; Blog. Accounts are susceptible to user spoofing when providing Kerberos tickets to *nix based services joined to an Active Directory realm. Gssapi-abuse is the tool section of this post.</li>
<li><a href="https://blog.neuvik.com/journey-into-windows-kernel-exploitation-the-basics-fff72116ca33" target="_blank">Journey into Windows Kernel Exploitation: The Basics</a>. Driver exploitation and abuse has been around forever. Here's a quick intro.</li>
<li><a href="https://www.youtube.com/watch?v=uyI5rgR0D-s" target="_blank">SharpSCCM Demos - 2023 Black Hat USA Arsenal</a>. The SCCM train continues. If you have not dove into SCCM abuse primatives, get on it! Don't believe us? Just faster forward to 4:46...</li>
<li><a href="https://posts.specterops.io/site-takeover-via-sccms-adminservice-api-d932e22b2bf" target="_blank">Site Takeover via SCCM's AdminService API</a>. The SCCM AdminService API is vulnerable to NTLM relaying 🤑</li>
<li><a href="https://sh3llsp4wn.github.io/Shellcode-With-The-Default-Linux-Toolchain/" target="_blank">Offensive Tool Development - The Shellcode Compiler Was Right There All Along...</a>. TLDR; Linker scripts can be used to generate shellcode via C in a fairly platform agnostic way.</li>
<li><a href="https://www.trustedsec.com/blog/the-client-server-relationship-a-match-made-in-heaven/" target="_blank">The Client/Server Relationship — A Match Made In Heaven</a>. <a href="https://twitter.com/exploitph" target="_blank">@exploitph</a> and <a href="https://twitter.com/jsecurity101" target="_blank">@jsecurity101</a> share some insight into detecting Kerberos-based attacks.</li>
<li><a href="https://citizenlab.ca/2023/08/vulnerabilities-in-sogou-keyboard-encryption/" target="_blank">Vulnerabilities in Sogou Keyboard encryption expose keypresses to network eavesdropping</a>. "...which render sensitive data such as the keystrokes that users type decipherable to network eavesdroppers"</li>
<li><a href="https://github.blog/2023-08-17-mtls-when-certificate-authentication-is-done-wrong/" target="_blank">mTLS: When certificate authentication is done wrong</a>. Any post that starts with an RFC screenshot is going to be a good time. Turns out you can do lots of nasty things with certificate parsing.</li>
<li><a href="https://blog.cloudflare.com/2023-phishing-report/" target="_blank">Introducing Cloudflare's 2023 phishing threats report</a>. How would your red team campaigns stack up?</li>
<li><a href="https://dazzyddos.github.io/posts/Naughty_Hooking_Detoxifying_Memory/" target="_blank">Naughty Hooking Detoxifying Memory Before Doing Crime</a>. An impressive amount of step-by-step screenshots and basics here.</li>
<li><a href="https://www.elastic.co/security-labs/forget-vulnerable-drivers-admin-is-all-you-need" target="_blank">Forget vulnerable drivers - Admin is all you need</a>. Perhaps the most exciting research of this post? Tons of fun can be had in the kernel, and if you don't need vulnerable drivers (easy detection point) then its game on...</li>
<li><a href="https://exploit.ph/des-is-useful.html" target="_blank">DES Is Useful... Sometimes</a>. Probably worth throwing an asktgt with the des option at every DC in your next assessment. Maybe you'll get lucky?</li>
<li><a href="https://blog.scrt.ch/2023/08/14/cve-2022-41099-analysis-of-a-bitlocker-drive-encryption-bypass/" target="_blank">CVE-2022-41099 - Analysis of a BitLocker Drive Encryption Bypass</a>. There is going to be a long tail on this one as it requires some manual intervention to apply the patch fully.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/DotNetRussell/Ensemble" target="_blank">Ensemble</a> - A Bug Bounty Platform that allows hunters to issue commands over a geo-distributed cluster. Gives some botnet like feels 🤔.</li>
<li><a href="https://github.com/deepinstinct/ContainYourself" target="_blank">ContainYourself</a> - DEF CON 31 Tool. Abuses the Windows containers framework to bypass EDRs.</li>
<li><a href="https://github.com/deepinstinct/NoFilter" target="_blank">NoFilter</a> - DEF CON 31 Tool. Abuses the Windows Filtering Platform for privilege escalation.</li>
<li><a href="https://github.com/ShorSec/DllNotificationInjection" target="_blank">DllNotificationInjection</a> - DEF CON 31 Tool. POC of a new “threadless” process injection technique.</li>
<li><a href="https://github.com/g0ldencybersec/CloudRecon" target="_blank">CloudRecon</a> - DEF CON 31 Tool. Suite of tools for red teamers and bug hunters to find ephemeral and development assets in their campaigns and hunts.</li>
<li><a href="https://github.com/g0ldencybersec/EasyEASM" target="_blank">EasyEASM</a> DEF CON 31 Tool. Zero-dollar attack surface management tool. "The industry is dominated by $30k vendors selling "Attack Surface Management," but OG bug bounty hunters and red teamers know the truth" 👀</li>
<li><a href="https://github.com/CCob/gssapi-abuse" target="_blank">gssapi-abuse</a> - DEF CON 31 Tool. Impersonating AD users on *nix based hosts? Noice. Looks like <a href="https://github.com/GhostPack/Rubeus/commit/64114442ef21263a579e0bfbf1478f3e5d89a133" target="_blank">rubeus</a> was updated as well.</li>
<li><a href="https://github.com/SafeBreach-Labs/DoubleDrive" target="_blank">DoubleDrive</a> - BH23 Tool. A fully-undetectable ransomware that utilizes OneDrive to encrypt target files.</li>
<li><a href="https://github.com/xpn/RandomTSScripts/tree/master/apppoolcreddecrypt" target="_blank">apppoolcreddecrypt</a> - A POC to show how IIS App Pool credentials are decrypted without appcmd.exe.</li>
<li><a href="https://github.com/florylsk/NtRemoteLoad" target="_blank">NtRemoteLoad</a> - Remote Shellcode injector using indirect native syscalls to inject shellcode into another process (based on HWSyscalls by ShorSec)</li>
<li><a href="https://github.com/praetorian-inc/konstellation" target="_blank">konstellation</a> - Konstellation is a configuration-driven CLI tool to enumerate cloud resources and store the data into Neo4j. Think Bloodhound for k8s.</li>
<li><a href="https://github.com/BishopFox/mellon" target="_blank">mellon</a> - Open Supervised Device Protocol attack tool (and the Elvish word for friend).</li>
<li><a href="https://github.com/Octoberfest7/CVE-2023-36874_BOF" target="_blank">CVE-2023-36874_BOF</a> - Weaponized CobaltStrike BOF for CVE-2023-36874 Windows Error Reporting LPE.</li>
<li><a href="https://github.com/DarkCoderSc/SharpShellPipe" target="_blank">SharpShellPipe</a> - This lightweight C# demo application showcases interactive remote shell access via named pipes and the SMB protocol.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.shaunography.com/from-domain-user-to-domain-admin-da-from-da-to-global-admin-ga.html" target="_blank">From Domain User to Domain Admin (DA), From DA to Global Admin (GA)</a> - Nice walkthrough of one method of escalating from DA to GA.</li>
<li><a href="https://www.r-tec.net/r-tec-blog-evade-signature-based-phishing-detections.html" target="_blank">Evade signature-based phishing detections</a> - Quick reminder that evading security controls doesn't always have to be complex. Safe browsing isn't immune.</li>
<li><a href="https://www.youtube.com/watch?v=o4T3NTl-vCg" target="_blank">ProjectDiscovery Tools in 180 seconds</a> - A bit sales-y but if you don't know about PD tools, this is a quick intro of their open-source tooling and capabilities.</li>
<li><a href="https://www.codeproject.com/Articles/19165/Vista-UAC-The-Definitive-Guide" target="_blank">Vista UAC: The Definitive Guide</a> - UAC under the hood hidden gem from 2008!</li>
<li><a href="https://ntdoc.m417z.com/" target="_blank">NTDoc</a> - Native API online documentation, based on the System Informer (formerly Process Hacker).</li>
<li><a href="https://grahamhelton.com/blog/ssh-cheatsheet/" target="_blank">SSH Cheatsheet</a> - Friendly reminder that when you'll forget SCP/SSH commands</li>
<li><a href="https://github.com/BinBashBanana/html-obfuscator" target="_blank">html-obfuscator</a> -  Easily obfuscate your html!</li>
<li><a href="https://github.com/RePRGM/Nimperiments" target="_blank">Nimperiments</a> - Random projects written in Nim. Check out EvilLsassTwin!</li>
<li><a href="https://github.com/hasherezade/tiny_tracer" target="_blank">tiny_tracer</a> - A Pin Tool for tracing API calls and instructions.</li>
<li><a href="https://github.com/snowcra5h/windows-api-function-cheatsheets" target="_blank">windows-api-function-cheatsheets</a> - A reference of Windows API function calls.</li>
<li><a href="https://github.com/xnl-h4ck3r/xnLinkFinder" target="_blank">xnLinkFinder</a> - HTTP Crawling and Javascript scraping/extraction for enumeration.</li>
<li><a href="https://github.com/GJDuck/e9patch" target="_blank">e9patch</a> - Static binary rewriting tool.</li>
<li><a href="https://github.com/skellyb0n3s/Infinite-Storage-Glitch" target="_blank">Infinite-Storage-Glitch</a> - I wonder a red teamer would use this for 🤔</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 354 (+0)</p>
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
