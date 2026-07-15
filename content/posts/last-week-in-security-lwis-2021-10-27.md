Title: Last Week in Security (LWiS) - 2021-10-27
Date: 2021-10-27 21:49
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-10-27
Author: Erik
Summary: Windows LPE 0day (<a href="https://twitter.com/KLINIX5" target="_blank">@KLINIX5</a>), and lots more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-10-19 to 2021-10-27.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.reuters.com/technology/exclusive-governments-turn-tables-ransomware-gang-revil-by-pushing-it-offline-2021-10-21/" target="_blank">EXCLUSIVE Governments turn tables on ransomware gang REvil by pushing it offline</a>. Congrats to <a href="https://www.risky.biz/RB642/" target="_blank">Patrick Gray</a>; they finally released the hounds!</li>
<li><a href="https://portswigger.net/daily-swig/infosec-skills-gap-widens-in-all-regions-bar-asia-pacific-report" target="_blank">Infosec skills gap widens in all regions bar Asia-Pacific – report</a>. "(ISC)² now estimates the global infosec skills gap to stand at around 2.7 million unfilled positions worldwide... The underlying issue isn’t just that demand is growing, it is that the jobs market consistently can’t attract enough people into cybersecurity careers to service demand."</li>
<li><a href="https://security.googleblog.com/2021/10/pixel-6-setting-new-standard-for-mobile.html" target="_blank">Pixel 6: Setting a new standard for mobile security</a>. The flagship phone from Google comes with 5 years of security updates (matching iPhones), as well as a feature that looks like a built in Android version of <a href="https://www.iverify.io/individuals" target="_blank">iVerify</a>.</li>
<li><a href="https://propertyofthepeople.org/document-detail/?doc-id=21088576" target="_blank">March 2019 FBI CAST Cellular Analysis &amp; Geo-Location Field Resource Guide</a>. Well this is interesting. Note: this document was acquired legally via a public record act request.</li>
<li><a href="https://citizenlab.ca/2021/10/breaking-news-new-york-times-journalist-ben-hubbard-pegasus/" target="_blank">New York Times Journalist Ben Hubbard Hacked with Pegasus after Reporting on Previous Hacking Attempts</a>. Is this the first confirmed case of a US person being hacked with NSO exploit presumably by a Saudi-linked operator (Jeff Bezos hack-and-leak had weak attribution)? Are the "gloves off" now? Artifacts go back as late as 2018.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://googleprojectzero.blogspot.com/2021/10/using-kerberos-for-authentication-relay.html" target="_blank">Using Kerberos for Authentication Relay Attacks</a>. The great James Forshaw is back with a tome on Kerberos for relaying.</li>
<li><a href="https://googleprojectzero.blogspot.com/2021/10/windows-exploitation-tricks-relaying.html" target="_blank">Windows Exploitation Tricks: Relaying DCOM Authentication</a>. Kerberos wasn't enough, so DCOM got the James Forshaw treatment too.</li>
<li><a href="https://www.synacktiv.com/en/publications/car-hijacking-swapping-a-single-bit.html" target="_blank">Car hijacking swapping a single bit</a>. These physical attacks are always cool to me. The same basic principle of exploitation applies to them: to exploit a system, you often must totally understanding it - sometimes better than the designers.</li>
<li><a href="https://alephsecurity.com/2020/01/14/ruckus-wireless/" target="_blank">Don't Ruck Us Too Hard - Owning Ruckus AP devices</a>. This research involved a cool setup of Ghidra and dockerized QEMU emulation. Any IoT or embedded researchers should read this.</li>
<li><a href="https://gerhard-wagner.medium.com/double-spending-bug-in-polygons-plasma-bridge-2e0954ccadf1" target="_blank">Double spending bug in Polygon’s Plasma bridge</a>. This bug was awarded a $2 million USD bounty. Perhaps it's time to switch focus to cryptocurrencies and smart contracts.</li>
<li><a href="https://www.sentinelone.com/labs/alphagolang-a-step-by-step-go-malware-reversing-methodology-for-ida-pro/" target="_blank">AlphaGolang | A Step-by-Step Go Malware Reversing Methodology for IDA Pro</a>. If you've ever had to reverse Go programs, you know it's a mess. <a href="https://github.com/SentineLabs/AlphaGolang" target="_blank">AlphaGolang</a> aims to help the analysis with IDA Pro with a series of helpful scripts.</li>
<li><a href="https://redteamer.tips/servers-are-overrated-bypassing-corporate-proxies-abusing-serverless-for-fun-and-profit/" target="_blank">Servers are overrated – Bypassing corporate proxies (ab)using serverless for fun and profit.</a>. This post comes complete with a "bug not a vuln" which lets you register subdomains of azurewebsites.net that includes reserved words like "microsoft."</li>
<li><a href="https://v3ded.github.io/redteam/utilizing-programmatic-identifiers-progids-for-uac-bypasses" target="_blank">Utilizing Programmatic Identifiers (ProgIDs) for UAC Bypasses</a>. Woah.</li>
<li><a href="https://posts.specterops.io/formalized-curiosity-3c550ece803e" target="_blank">Formalized Curiosity</a>. This post is a good look at a process for conducting research.</li>
<li><a href="https://voidsec.com/driver-buddy-reloaded/" target="_blank">Driver Buddy Reloaded</a>. Use this on your hunt for Windows driver vulns!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/klinix5/ProfSvcLPE" target="_blank">ProfSvcLPE</a> is an currently unpatched local privilege escalation that shares the same root cause as <a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34484" target="_blank">CVE-2021-34484</a>, but wasn't properly patched. The repo contains a word doc with a writeup as well.</li>
<li><a href="https://github.com/Tylous/ZipExec" target="_blank">ZipExec</a> is a unique technique to execute binaries from a password protected zip on Windows.</li>
<li><a href="https://github.com/Rices/Phishious" target="_blank">Phishious</a> is an open-source Secure Email Gateway (SEG) evaluation toolkit designed for red-teamers. This is the coolest tool I've seen in a while.</li>
<li><a href="https://github.com/gtworek/PSBits/tree/master/FakeAMSI" target="_blank">FakeAMSI</a>. Have you ever persisted by pretending to e an antivirus product?</li>
<li><a href="https://github.com/klezVirus/SharpSelfDelete" target="_blank">SharpSelfDelete</a> is a C# implementation of the research by @jonaslyk and the drafted PoC from @LloydLabs.</li>
<li><a href="https://github.com/ly4k/CallbackHell" target="_blank">CallbackHell</a> is an exploit for CVE-2021-40449 - Win32k Elevation of Privilege Vulnerability (LPE)</li>
<li><a href="https://github.com/EspressoCake/DLL_Imports_BOF" target="_blank">DLL_Imports_BOF</a> is a BOF to parse the imports of a provided PE-file, optionally extracting symbols on a per-dll basis.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/efoncubierta/cloudspec" target="_blank">cloudspec</a> is an open source tool for validating your resources in your cloud providers using a logical language.</li>
<li><a href="https://github.com/z1pti3/jimi" target="_blank">jimi</a> is an automation first no-code platform designed and developed originally for Security Orchestration and Response. Since its launch jimi has developed into a fully fledged IT automation platform which effortlessly integrates with your existing tools unlocking the potential for autonomous IT and Security operations.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
