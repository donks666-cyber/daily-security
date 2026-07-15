Title: Last Week in Security (LWiS) - 2022-06-14
Date: 2022-06-14 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-06-14
Author: Erik
Summary: RE an iOS app (<a href="https://twitter.com/inversecos" target="_blank">@inversecos</a>), More Azure Managed Identity attacks (<a href="https://twitter.com/_wald0" target="_blank">@_wald0</a>), excellent hardware hacking (<a href="https://twitter.com/matthiasdeeg" target="_blank">@matthiasdeeg</a>), printer pwnage (<a href="https://twitter.com/nikaiw" target="_blank">@Nikaiw</a>, <a href="https://twitter.com/JRomainG" target="_blank">@JRomainG</a>, <a href="https://twitter.com/_trou_" target="_blank">@_trou_</a>), BloodHound false positive reduction (<a href="https://twitter.com/simondotsh" target="_blank">@simondotsh</a>), Ghostwriter 3.0 (<a href="https://twitter.com/cmaddalena" target="_blank">@cmaddalena</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-06-06 to 2022-06-14.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.cobaltstrike.com/blog/theres-another-new-deputy-in-town/" target="_blank">There's Another New Deputy in Town</a>. SOCKS5 support may finally be coming to Cobalt Strike.</li>
<li><a href="https://krebsonsecurity.com/2022/06/krebsonsecurity-in-new-netflix-series-on-cybercrime/" target="_blank">KrebsOnSecurity in New Netflix Series on Cybercrime</a>. Might be worth a watch but I always worry these shows will be too much drama and not enough technical detail for my taste.</li>
<li><a href="https://kotaku.com/war-thunder-tank-classified-military-document-leak-chin-1849005359" target="_blank">ANOTHER Guy Has Leaked Classified Military Documents On The SAME TANK GAME'S forums</a>. Not all that relevant, but goes to show that useful information can be fond in the strangest places.</li>
<li><a href="https://clickstudios.com.au/advisories/Incident_Management_Advisory-03-20220607.pdf" target="_blank">[PDF] clickstudios Passwordstate Incident Management Advisory #03</a>. A digital signing certificate published online for 2 days was enough for it to be scooped up and used by a malware crew. No one is safe from the scrapers.</li>
<li><dl>
<dt>Logo'd bugs</dt>
<dd><ul>
<li><a href="https://pacmanattack.com/" target="_blank">PACMAN Attacking ARM Pointer Authentication with Speculative Execution</a>. I'd put this in the same camp as spectre, if you already have privilieged code execution, this may be useful, otherwise its a fun academic exercise but has a very narrow useful window.</li>
<li><a href="https://www.hertzbleed.com/" target="_blank">Hertzbleed Attack</a>. This one may be slightly more useful, with the potential to extract key material from "constant time" cryptographic routines, even remotely. Intel and AMD are affected, with the potential for ARM chips to be vulnerable as well. Code <a href="https://github.com/FPSG-UIUC/hertzbleed" target="_blank">here</a>.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://www.theverge.com/2022/6/13/23165535/google-suspends-ai-artificial-intelligence-engineer-sentient" target="_blank">Google suspends engineer who claims its AI is sentient</a>. You can read the <em>editied</em> chat transcripts <a href="https://cajundiscordian.medium.com/is-lamda-sentient-an-interview-ea64d916d917" target="_blank">here</a> and decide for yourself. Either way this is 10/10 marketing for Google.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.inversecos.com/2022/06/how-to-reverse-engineer-and-patch-ios.html" target="_blank">How to Reverse Engineer and Patch an iOS Application for Beginners: Part I</a>. There is a need for these kinds of write ups that introduce a complex topic from first principles. Unfortunately, by the time people learn the skills, they don't write the posts! You'll need a mac and a jailbroken iOS device to follow along at home.</li>
<li><a href="https://posts.specterops.io/managed-identity-attack-paths-part-2-logic-apps-52b29354fc54" target="_blank">Managed Identity Attack Paths, Part 2 and 3</a>. Two more posts in the series started last week.</li>
<li><a href="https://blog.syss.com/posts/hacking-usb-flash-drives-part-1/" target="_blank">Hacking Some More Secure USB Flash Drives (Part I)</a>. Some very in-depth hardware hacking against "secure" USB drives.</li>
<li><a href="https://cr.culbertreport.com/2022/06/covenant-in-2022.html" target="_blank">Covenant In 2022</a>. This post has some ideas on how to wrap or modify grunts to bypass some EDR solutions.</li>
<li><a href="https://www.zerodayinitiative.com/blog/2022/6/7/cve-2022-26937-microsoft-windows-network-file-system-nlm-portmap-stack-buffer-overflow" target="_blank">CVE-2022-26937: Microsoft Windows Network File System NLM Portmap Stack Buffer Overflow</a>. RCE as SYSTEM but careful, "unsuccessful exploitation results in a crash of the target system." No PoC available yet.</li>
<li><a href="https://blog.notso.pro/2022-06-12-avoiding-cyber-nihilism/" target="_blank">Avoiding B.A.D. behaviour: The difficult relationship between nihilism, cybersecurity professionals and Being-A-Dick behaviour</a>. Not technical, but potentially useful.</li>
<li><a href="https://doar-e.github.io/blog/2022/06/11/pwn2own-2021-canon-imageclass-mf644cdw-writeup/" target="_blank">Pwn2Own 2021 Canon ImageCLASS MF644Cdw writeup</a>. An unbound base64 decode leads to RCE in a printer. Great post that goes from firmware extraction to RCE.</li>
<li><a href="https://arstechnica.com/information-technology/2022/06/hackers-out-to-steal-a-tesla-can-create-their-very-own-personal-key/" target="_blank">Gone in 130 seconds: New Tesla hack gives thieves their own personal key</a>. This feels like something a basic internal security audit would have found?</li>
<li><a href="https://simondotsh.com/infosec/2022/06/14/bloodhound-contains-edge.html" target="_blank">Beware of BloodHound's Contains Edge</a>. AD relationships are complex, and mapping them is tricky which leads to some false positives. This post contains a potential "fix" for a <cite>Contains</cite> false positive situation.</li>
<li><a href="https://posts.specterops.io/introducing-ghostwriter-v3-0-db462a1c688c" target="_blank">Introducing Ghostwriter v3.0</a>. The report and domain management tool turns 3.0! It can be managed with a new CLI tool and has support for CVSS scoring among other fixes and additions.</li>
<li><a href="https://theevilbit.github.io/posts/amfi_launch_constraints/" target="_blank">AMFI Launch Constraints - First Quick Look</a>. New security restrictions on system binaries in macOS Ventura will kill a whole exploit class!</li>
<li><a href="https://www.x86matthew.com/view_post?id=proc_env_injection" target="_blank">ProcEnvInjection - Remote code injection by abusing process environment strings</a>. Another unique injection technique from x86matthew.</li>
<li><a href="https://blog.sonarsource.com/zimbra-mail-stealing-clear-text-credentials-via-memcache-injection/" target="_blank">Zimbra Email - Stealing Clear-Text Credentials via Memcache injection</a>. Very cool bug and exploit!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/tr3ee/CVE-2022-23222" target="_blank">CVE-2022-23222</a> - Linux Kernel eBPF Local Privilege Escalation.</li>
<li><a href="https://github.com/aaronsvk/CVE-2022-30075" target="_blank">CVE-2022-30075</a> - Tp-Link Archer AX50 Authenticated RCE (CVE-2022-30075).</li>
<li><a href="https://github.com/palant/apk-instrumentation" target="_blank">apk-instrumentation</a> Some tools to rewrite code of release APK packages.</li>
<li><a href="https://github.com/sensity-ai/dot#installation" target="_blank">dot</a> The Deepfake Offensive Toolkit.</li>
<li><a href="https://github.com/vxunderground/VX-API" target="_blank">VX-API</a> Malware rapid development framework. "We've released the vx-underground "VX-API", a Windows malware rapid application development framework written in C/C++. It is a compilation of code written by @smelly__vx &amp; @am0nsec. A lot of work needs to be done (including a ReadMe file). More to come."</li>
<li><a href="https://github.com/ariary/Dogwalk-rce-poc" target="_blank">Dogwalk-rce-poc</a> 🐾Dogwalk PoC (using diagcab file to obtain RCE on windows).</li>
<li><a href="https://github.com/KarimPwnz/sourcegraph-scripts" target="_blank">sourcegraph-scripts</a> Scripts for Sourcegraph search results. Useful for static analysis.</li>
<li><a href="https://gitlab.com/ORCA666/kcthijacklib" target="_blank">kcthijacklib</a> - A Small Library For a Cleaner Execution.</li>
<li><a href="https://github.com/Flangvik/collector" target="_blank">collector</a> - Utility to analyse, ingest and push out credentials from common data sources during an internal penetration test.</li>
<li><a href="https://github.com/Accenture/FirmLoader" target="_blank">FirmLoader</a> is an IDA plugin that allows to automatically identify parts of the memory for the firmware images extracted from microcontrollers.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/leesoh/np" target="_blank">np</a> - A tool to parse, deduplicate, and query multiple port scans.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 416 (+0)</p>
<p>Blogs monitored: 311 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
