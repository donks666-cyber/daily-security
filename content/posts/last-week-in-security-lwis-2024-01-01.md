Title: Last Week in Security (LWiS) - 2024-01-01
Date: 2024-01-01 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-01-01
Author: Erik
Summary: Ghidriff (<a href="https://twitter.com/clearbluejar" target="_blank">@clearbluejar</a>), Linux exploitation (<a href="https://twitter.com/kevin_backhouse" target="_blank">@kevin_backhouse</a>), win32 keylogger (<a href="https://twitter.com/_ixty_" target="_blank">@_ixty_</a>), BLUFFS bluetooth exploit (<a href="https://twitter.com/francozappa" target="_blank">@francozappa</a>), sleep lexer and parser (<a href="https://twitter.com/mcbroom_evan" target="_blank">@mcbroom_evan</a>), ring0 from VBA (<a href="https://twitter.com/0xDISREL" target="_blank">@0xDISREL</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week(s). This post covers 2023-12-04 to 2024-01-01.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.youtube.com/watch?v=7VWNUUldBEE" target="_blank">Operation Triangulation: What You Get When Attack iPhones of Researchers</a>. The most complex double-exploitation chain I have seen in a long time. Ask yourself - if the actor that deployed this is willing to burn and entire 1-click chain just to package it with a 0-click, what do they have on the shelf or are using very sparingly?</li>
<li><a href="https://krebsonsecurity.com/2023/12/blackcat-ransomware-raises-ante-after-fbi-disruption/" target="_blank">BlackCat Ransomware Raises Ante After FBI Disruption</a>. If you poke the bear, you best be prepared to wrestle it.</li>
<li><a href="https://msrc.microsoft.com/blog/2023/12/microsoft-addresses-app-installer-abuse/" target="_blank">Microsoft addresses App Installer abuse</a>. This is actually the second time Microsoft has had to disable ms-appinstaller URI scheme. This time it's because <a href="https://www.microsoft.com/en-us/security/blog/2023/12/28/financially-motivated-threat-actors-misusing-app-installer/" target="_blank">Financially motivated threat actors misusing App Installer</a>.</li>
<li><a href="https://www.npr.org/2023/12/19/1219984002/artificial-intelligence-can-find-your-location-in-photos-worrying-privacy-expert" target="_blank">Artificial intelligence can find your location in photos, worrying privacy experts</a>. OSINT experts have been doing this for decades, AI just makes it avaialable to the masses, and easy.</li>
<li><a href="https://www.businessinsider.com/google-maps-location-data-history-stored-locally-2023-12" target="_blank">Google will no longer hold onto people's location data in Google Maps — meaning it can't turn that info over to the police</a>. A rare privacy win out of Google.</li>
<li><a href="https://www.bleepingcomputer.com/news/security/ubiquiti-users-report-having-access-to-others-unifi-routers-cameras/" target="_blank">Ubiquiti users report having access to others' UniFi routers, cameras</a>. When you connect your core infrastructure to the internet, you had better trust the security of whatever you connect it to.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2023/CVE-2023-36033.html" target="_blank">CVE-2023-36033: Windows DWM Core Library Elevation of Privilege Vulnerability</a>. This is an in-the-wild 0day Windows LPE that uses a two stage execution to get SYSTEM.</li>
<li><a href="https://github.blog/2023-12-13-securing-our-home-labs-frigate-code-review/" target="_blank">Securing our home labs: Frigate code review</a>. CodeQL finds some CVEs yet again.</li>
<li><a href="https://www.praetorian.com/blog/sonicwall-wxa-authentication-bypass-and-rce-vulnerability/" target="_blank">SonicWall WXA - Authentication Bypass and Remote Code Execution Vulnerability</a>. A nice walkthrough of image download to RCE in a few hours.</li>
<li><a href="https://portswigger.net/research/finding-that-one-weird-endpoint-with-bambdas" target="_blank">Finding that one weird endpoint, with Bambdas</a>. Bambdas are a fun new feature of Burp Suite to quickly test for things in your project files directly inside the proxy. This post has some nice examples of how they can be used.</li>
<li><a href="https://github.blog/2023-12-06-cueing-up-a-calculator-an-introduction-to-exploit-development-on-linux/" target="_blank">Cueing up a calculator: an introduction to exploit development on Linux</a>. A great intro to modern Linux exploit development that addresses mitigations found on modern Linux operating systems.</li>
<li><a href="https://portswigger.net/research/blind-css-exfiltration" target="_blank">Blind CSS Exfiltration: exfiltrate unknown web pages</a>. The new <cite>:has</cite> selector can be used to exfiltrate data from sites that have a blind HTML injection vulnerability.</li>
<li><a href="https://blog.exodusintel.com/2023/12/11/safari-hold-still-for-nan-minutes/" target="_blank">Safari, Hold Still for NaN Minutes!</a>. Some browser exploitation content from the team at Exodus.</li>
<li><a href="https://pagedout.institute/download/PagedOut_003_beta1.pdf" target="_blank">[PDF] Paged Out Volume 3</a>. Hacker zines are making a comeback and I'm here for it.</li>
<li><a href="https://malwaretech.com/2023/12/silly-edr-bypasses-and-where-to-find-them.html" target="_blank">Silly EDR Bypasses and Where To Find Them</a>. Bypass EDR detections with "forced exceptions." Code <a href="https://github.com/MalwareTech/EDRception" target="_blank">here</a>. Confused by what user mode hooks are? Check out <a href="https://malwaretech.com/2023/12/an-introduction-to-bypassing-user-mode-edr-hooks.html" target="_blank">An Introduction to Bypassing User Mode EDR Hooks</a>.</li>
<li><a href="https://www.synacktiv.com/en/publications/writing-a-decent-win32-keylogger-13" target="_blank">Writing A Decent WIN32 Keylogger</a>. This three part series covers the ins and outs of writing a keylogger for Windows that handles unicode and other edge cases. The tool is called <a href="https://github.com/synacktiv/keebcap" target="_blank">keebcap</a>.</li>
<li><a href="https://binarly.io/posts/The_Far_Reaching_Consequences_of_LogoFAIL/index.html" target="_blank">The Far-Reaching Consequences of LogoFAIL</a>. That cool boot logo in UEFI is probably a vulnerability.</li>
<li><a href="https://francozappa.github.io/post/2023/bluffs-ccs23/" target="_blank">BLUFFS: Bluetooth Forward and Future Secrecy Attacks and Defenses</a>. This 10+ year old flaw in Bluetooth forces devices to negoitate a short session key which can be brute forced.</li>
<li><a href="https://secret.club/2023/12/24/riscy-business.html" target="_blank">RISC-Y Business: Raging against the reduced machine</a>. Protect your "intelectual property" by writing your own RISC virtual machine in your binary. Code is at <a href="https://github.com/thesecretclub/riscy-business" target="_blank">riscy-business</a>.</li>
<li><a href="https://book.hacktricks.xyz/pentesting-web/browser-extension-pentesting-methodology" target="_blank">Browser Extension Pentesting Methodology</a>. New detailed writeup on how to approach a Browser Extension.</li>
<li><a href="https://research.checkpoint.com/2023/rust-binary-analysis-feature-by-feature/" target="_blank">Rust Binary Analysis, Feature by Feature</a>. An extreamly thurough break down of Rust binary analysis.</li>
<li><a href="https://swisskyrepo.github.io/InternalAllTheThings/" target="_blank">Internal All The Things - Active Directory and Internal Pentest Cheatsheets</a>. An impressive collection of Active Directory techniques.</li>
<li><a href="https://disrel.com/posts/Ring0VBA-Getting-Ring0-Using-a-Goddamn-Word-Document/" target="_blank">Ring0VBA - Getting Ring0 Using a Goddamn Word Document</a>. Absolute madness.</li>
<li><a href="https://cyb3rops.medium.com/introducing-yara-forge-a77cbb77dcab" target="_blank">Introducing YARA-Forge</a>. If you deal with yara rules (defense or testing your offensive tools), this project will likely help you organize and optimize all your rules.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/EvanMcBroom/sleepy" target="_blank">sleepy</a> - A lexer and parser for Sleep. Read more <a href="https://posts.specterops.io/sleepy-python-tooling-for-sleep-7a96d9d650ee" target="_blank">here</a>.</li>
<li><a href="https://blog.thinkst.com/2023/12/a-beta-canarytoken-for-active-directory-credentials.html" target="_blank">A (beta) Canarytoken for Active Directory Credentials</a>. Perhaps one of the most effective canary tokens yet. Slightly more complicated than just dropping a file, but it will be extremely effective in catching red teams and adversaries.</li>
<li><a href="https://github.com/synacktiv/frinet" target="_blank">frinet</a> - Frida-based tracer for easier reverse-engineering on Android, iOS, Linux, Windows and most related architectures.</li>
<li><a href="https://github.com/Maldev-Academy/Christmas" target="_blank">Christmas</a> - By splitting up the injection actions across different spawned processes, none of the spawned processes generate enough signal to trip EDR (in theory).</li>
<li><a href="https://github.com/BishopFox/sj" target="_blank">sj</a> - A tool for auditing endpoints defined in exposed (Swagger/OpenAPI) definition files. See <a href="https://bishopfox.com/blog/swagger-jacker-auditing-openapi-definition-files" target="_blank">this post</a> for more info.</li>
<li><a href="https://clearbluejar.github.io/posts/ghidriff-ghidra-binary-diffing-engine/" target="_blank">Ghidriff: Ghidra Binary Diffing Engine</a>. Back in my day, BinDiff was paid software. This is a great addition to your reverse engineering/diffing toolbox, and fully open source!</li>
<li><a href="https://github.com/synacktiv/bbs" target="_blank">bbs</a> - bbs is a router for SOCKS and HTTP proxies. It exposes a SOCKS5 (or HTTP CONNECT) service and forwards incoming requests to proxies or chains of proxies based on the request's target. Routing can be configured with a PAC script (if built with PAC support), or through a JSON file.</li>
<li><a href="https://github.com/hackerhouse-opensource/SignToolEx" target="_blank">SignToolEx</a> - Patching "signtool.exe" to accept expired certificates for code-signing.</li>
<li><a href="https://github.com/hackerhouse-opensource/WMIProcessWatcher" target="_blank">WMIProcessWatcher</a> - A CIA tradecraft technique to asynchronously detect when a process is created using WMI.</li>
<li><a href="https://github.com/hackerhouse-opensource/Marble" target="_blank">Marble</a> - The CIA's Marble Framework is designed to allow for flexible and easy-to-use obfuscation when developing tools.</li>
<li><a href="https://github.com/KpwnZ/Def1nit3lyN0tAJa1lbr3akTool" target="_blank">Def1nit3lyN0tAJa1lbr3akTool</a> - A jailbreak tool for all arm64 devices on iOS 16.0 to iOS 16.5.</li>
<li><a href="https://github.com/Leo4j/Amnesiac" target="_blank">Amnesiac</a> - Amnesiac is a post-exploitation framework entirely written in PowerShell and designed to assist with lateral movement within Active Directory environments.</li>
<li><a href="https://gist.github.com/testanull/dac6029d306147e6cc8dce9424d09868" target="_blank">SharePoint Pre-Auth Code Injection RCE chain CVE-2023-29357 &amp; CVE-2023-24955 PoC</a> - Sharepoint RCE.</li>
<li><a href="https://github.com/netero1010/EDRSilencer" target="_blank">EDRSilencer</a> - A tool uses Windows Filtering Platform (WFP) to block Endpoint Detection and Response (EDR) agents from reporting security events to the server. This is similar to <a href="https://github.com/dsnezhkov/shutter" target="_blank">shutter</a> (shoutout to <a href="https://twitter.com/naksyn" target="_blank">@naksyn</a>).</li>
<li><a href="https://htmlpreview.github.io/?https://github.com/NationalSecurityAgency/ghidra/blob/Ghidra_11.0_build/Ghidra/Configurations/Public_Release/src/global/docs/ChangeHistory.html" target="_blank">Ghidra 11.0</a>. 11.0 brings the "Bsim" binary similarity tool, better Go binary support, and initial Rust binary support.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Velocidex/Linpmem" target="_blank">Linpmem</a> is a linux memory acquisition tool.</li>
<li><a href="https://github.com/bensadeh/tailspin" target="_blank">tailspin</a> - 🌀 A log file highlighter.</li>
<li><a href="https://github.com/lap1nou/CLR_Heap_encryption" target="_blank">CLR_Heap_encryption</a>. This is a POC for a CLR sleep obfuscation attempt. It use IHostMemoryManager interface to control the memory allocated by the CLR. Turns out you can use both ICorRuntimeHost and ICLRRuntimeHost at the same time, so we can still use ICorRuntimeHost to run an assembly from memory while having all the benefits from ICLRRuntimeHost.</li>
<li><a href="https://github.com/zzzteph/sheye" target="_blank">sheye</a> - Opensource assets and vulnerability scanning tool.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 365 (+1)</p>
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
