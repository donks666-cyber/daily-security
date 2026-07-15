Title: Last Week in Security (LWiS) - 2025-07-21
Date: 2025-07-21 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-07-21
Author: Erik
Summary: PIC agents (<a href="https://x.com/_rastamouse" target="_blank">@_RastaMouse</a>), ToolShell, Async BOFs (<a href="https://x.com/Cneelis" target="_blank">@Cneelis</a>), SCCM MP relays (<a href="https://x.com/unsigned_sh0rt" target="_blank">@unsigned_sh0rt</a>), RAITrigger (<a href="https://x.com/ShitSecure" target="_blank">@ShitSecure</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-07-14 to 2025-07-21.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.propublica.org/article/microsoft-digital-escorts-pentagon-defense-department-china-hackers" target="_blank">A Little-Known Microsoft Program Could Expose the Defense Department to Chinese Hackers</a> - "Digital escorts," with limited technical knowledge were supposed to oversee any work done on the Microsoft Cloud by engineers in China. “We’re trusting that what they’re doing isn’t malicious, but we really can’t tell.” 🫣 Microsoft's chief communications officer has <a href="https://x.com/fxshaw/status/1946299139068965008" target="_blank">said</a> changes have been mande and now, "no China-based engineering teams are providing technical assistance for DoD Government cloud and related services." How much code developed in China is used in the base Microsoft Cloud product, which is eventually used in the DoD Microsoft cloud? I doubt the "digital escorts" could have spotted any half-decent backdoors, when things like <a href="https://web.archive.org/web/20100103075600/http://underhanded.xcott.com/?page_id=16" target="_blank">The Underhanded C Contest</a> exist.</li>
<li><a href="https://blog.cloudflare.com/cloudflare-1-1-1-1-incident-on-july-14-2025/" target="_blank">Cloudflare 1.1.1.1 incident on July 14, 2025</a> - "It's always DNS" is the sysadmin's mantra. This time it was anycast and Cloudflare's Data Localization Suite (DLS), combined with human error and insufficient technical controls that led to a global DNS outage for 1.1.1.1 users for about an hour.</li>
<li><a href="https://community.clearlinux.org/t/all-good-things-come-to-an-end-shutting-down-clear-linux-os/10716" target="_blank">All good things come to an end: Shutting down Clear Linux OS</a> - Intel is attempting to <a href="https://www.macrotrends.net/stocks/charts/INTC/intel/revenue" target="_blank">stop the bleeding</a> by <a href="https://www.barrons.com/articles/intel-stock-price-layoffs-job-cuts-07c9459b" target="_blank">cutting thousands of jobs</a>, and stopping support for Clear Linux. The lead maintainer of Clear Linux, Arjan van de Ven is still a Fellow at Intel.</li>
<li><a href="https://krebsonsecurity.com/2025/07/microsoft-fix-targets-attacks-on-sharepoint-zero-day/" target="_blank">Microsoft Fix Targets Attacks on SharePoint Zero-Day</a> - After a few days of rampant exploitation, Microsoft has a fix for an unauthenticated remote code execution 0day in SharePoint, called "ToolShell," the legacy but popular content platform used by enterprises and governments around the world. Both of the exploits used in ToolShell may be patch bypasses for previous vulnerabilities, which makes this even more 🤦. The guidance to disconnect affected products from the public-facing Internet is difficult for a system designed to host public content. You know it's serious when Microsoft puts out <a href="https://msrc.microsoft.com/blog/2025/07/customer-guidance-for-sharepoint-vulnerability-cve-2025-53770/" target="_blank">customer guidance</a> in addition to the normal knowledge base entry.</li>
<li><a href="https://www.theverge.com/cyber-security/707116/iceblock-data-privacy-security-android-version" target="_blank">ICEBlock isn’t ‘completely anonymous’ - But no app is.</a> - An interesting outcome of having Apple or Google run all push notifications for iOS and Android is that it's now impossible to make an app completely anonymous if you want to send users a push notification. I think the only way to achieve anonymous push notifications would be to "launder" them via another app like the amazing, open source, self-hostable <a href="https://ntfy.sh/" target="_blank">ntfy</a>.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.youtube.com/watch?v=cFd_glOusLo" target="_blank">Kuba Gretzky: Wise Phishermen Never Trust The Weather</a> - The Evilginx author discussed what it takes to have a successful phishing campaign in 2025.</li>
<li><a href="https://starlabs.sg/blog/2025/07-my-blind-date-with-cve-2025-29824/" target="_blank">My 'Blind Date' with CVE-2025-29824</a> - The author creates a proof of concept (crash) using a use-after-free bug in the Windows Common Log File System (CLFS) driver for Windows.</li>
<li><a href="https://certitude.consulting/blog/en/local-privilege-escalation-citrix-virtual-apps-and-desktops/" target="_blank">CVE-2025-6759: Local Privilege Escalation in Citrix Virtual Apps and Desktops</a> - Virtual Private Network (VPN) or Virtual Desktop apps usually have some kind of SYSTEM level service to facilitate low level networking, and historically have been a great place to look for local privilege escalation bugs on Windows</li>
<li><a href="https://rastamouse.me/modular-pic-c2-agents/" target="_blank">Modular PIC C2 Agents</a> - The future is modular. From putting together custom labs using modular roles in <a href="https://ludus.cloud/" target="_blank">Ludus</a>, to building command and control (C2) agents with modular position independent code elements, the flexibility, customizability, and reusability of modular solutions outweigh their small configuration setup barrier.</li>
<li><a href="https://www.outflank.nl/blog/2025/07/16/async-bofs-wake-me-up-before-you-go-go/" target="_blank">Async BOFs – “Wake Me Up, Before You Go Go”</a> - Outflank C2 includes some new Beacon APIs to allow for threads to run while the main beacon sleeps and wake it when a user logs in or a process is started.</li>
<li><a href="https://blog.quarkslab.com/controlplane_lpe_macos.html" target="_blank">ControlPlane Local Privilege Escalation Vulnerability on macOS</a> - A detailed walkthrough of a macOS local privilege escalation via a privileged helper. While the target application is unmaintained, this technique is applicable to many applications with privileged helpers.</li>
<li><a href="https://specterops.io/blog/2025/07/15/id-like-to-speak-to-your-manager-stealing-secrets-with-management-point-relays/" target="_blank">I’d Like to Speak to Your Manager: Stealing Secrets with Management Point Relays</a> - SCCM is the gift that keeps on giving. Using some stored procedures and relaying NTLM to MSSQL, its possible to get the policy secrets for unknown machines. In practice, these are domain credentials that are (usually) overprovisioned. I love seeing the <a href="https://ludus.cloud/" target="_blank">Ludus</a> domain all over this article. More research that was made possible by an assessor being able to easily set up a complex test environment and get straight to the fun stuff!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Teach2Breach/stargate" target="_blank">stargate</a> - Locate dlls and function addresses without PEB Walk and EAT parsing.</li>
<li><a href="https://github.com/temp43487580/mprecon" target="_blank">mprecon</a> - a small script to collect information from a management point.</li>
<li><a href="https://github.com/zarkones/BloodfangC2" target="_blank">BloodfangC2</a> - Modern PIC implant for Windows (64 &amp; 32 bit).</li>
<li><a href="https://github.com/NetPenguins/ludus_redirector" target="_blank">ludus_redirector</a> - Role for setting up Redirectors in <a href="https://ludus.cloud/" target="_blank">Ludus</a>  ranges.</li>
<li><a href="https://github.com/NetPenguins/ludus_sliver" target="_blank">ludus_sliver</a> - Role for setting up Sliver C2 in <a href="https://ludus.cloud/" target="_blank">Ludus</a> ranges.</li>
<li><a href="https://github.com/EvilBytecode/Ebyte-Go-Morpher" target="_blank">Ebyte-Go-Morpher</a> is a Go program that parses, analyzes, and rewrites Go source code to apply multiple layers of obfuscation. It operates directly on the Go Abstract Syntax Tree (AST) and generates both obfuscated source files and runtime decryption logic.</li>
<li><a href="https://github.com/soltanali0/CVE-2025-53770-Exploit" target="_blank">CVE-2025-53770-Exploit</a> - SharePoint WebPart Injection Exploit Tool. [Untested, use at your own risk]</li>
<li><a href="https://github.com/rtecCyberSec/RAITrigger/" target="_blank">RAITrigger</a> - Local SYSTEM auth trigger for relaying.</li>
<li><a href="https://github.com/OleFredrik1/remoteKrbRelayx" target="_blank">remoteKrbRelayx</a> - A tool for coercing and relaying Kerberos authentication over DCOM and RPC.</li>
<li><a href="https://github.com/NetSPI/CVE-2025-4660" target="_blank">CVE-2025-4660</a> - PoC for CVE-2025-4660 demonstrating exploitation of the Forescout SecureConnector on Windows. More info <a href="https://www.netspi.com/blog/technical-blog/red-teaming/cve-2025-4660-forescout-secureconnector-rce/" target="_blank">here</a>.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/hzqst/unicorn_pe" target="_blank">unicorn_pe</a> - Unicorn PE is an unicorn based instrumentation project designed to emulate code execution for windows PE files.</li>
<li><a href="https://github.com/casp3r0x0/LoaderGate" target="_blank">LoaderGate</a> - a C# implementation for a shellcode loader that capable to bypass Cortex XDR and Sophos EDR.</li>
<li><a href="https://github.com/EgeBalci/evilreplay" target="_blank">evilreplay</a> - Seamless remote browser session control.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 455 (+0)</p>
<p>Blogs monitored: 424 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>X: <a href="https://x.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
