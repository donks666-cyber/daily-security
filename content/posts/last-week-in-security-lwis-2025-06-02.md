Title: Last Week in Security (LWiS) - 2025-06-02
Date: 2025-06-02 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-06-02
Author: Erik
Summary: Stealth syscalls (<a href="https://x.com/darkrelaylabs" target="_blank">@darkrelaylabs</a>), VM introspection (<a href="https://x.com/memN0ps" target="_blank">@memn0ps</a>), Marebackup LPE (<a href="https://x.com/itm4n" target="_blank">@itm4n</a>), Azure Arc C2 (<a href="https://x.com/ZephrFish" target="_blank">@ZephrFish</a>), Obfusk8 (<a href="https://x.com/x86byte" target="_blank">@x86byte</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-05-27 to 2025-06-02.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2025/05/sustaining-digital-certificate-security-chrome-root-store-changes.html" target="_blank">Sustaining Digital Certificate Security - Upcoming Changes to the Chrome Root Store</a> - "Chrome's confidence in the reliability of Chunghwa Telecom and Netlock as CA (certificate authority) Owners included in the Chrome Root Store has diminished due to patterns of concerning behavior observed over the past year." On 2025-08-01, Chrome will no longer trust certificates issued by Chunghwa Telecom and Netlock. There are still 109 unique CA's in the <a href="https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/root_store.md" target="_blank">Chrome Root Store</a>.</li>
<li><a href="https://therecord.media/australia-ransomware-victims-must-report-payments" target="_blank">Australian ransomware victims now must tell the government if they pay up</a> - This only applies to the top 6.5% of businesses in Australia, and is only reported to the Australian Signals Directorate (ASD). While it resembles the rules for <a href="https://www.crcgroup.com/Tools-and-Intel/post/sec-update-new-cybersecurity-disclosure-rules" target="_blank">public companies in the United States</a>, this looks more like ASD wants to know if a large ransomware campaign is hitting Australia before they read about it all over the news.</li>
<li><a href="https://pure.tugraz.at/ws/portalfiles/portal/89650227/Final_Paper_Usenix.pdf" target="_blank">[PDF] CHOICEJACKING: Compromising Mobile Devices through Malicious Chargers like a Decade ago</a> - Your phone now asks you to trust an unknown device when connected, but what if that unknown device was itself also a keyboard and clicked accept for you? Works on Android and iOS devices in anywhere from 1.3 to 23 seconds. 10/10 hack.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.darkrelay.com/post/stealth-syscall-execution-bypass-edr-detection" target="_blank">Stealth Syscall Execution: Bypassing ETW, Sysmon, and EDR Detection</a> - Some good ideas for your next loader.</li>
<li><a href="https://secret.club/2025/06/02/hypervisors-for-memory-introspection-and-reverse-engineering.html" target="_blank">Hypervisors for Memory Introspection and Reverse Engineering</a> - This post serves as a great introduction to using hypervisor "shims" to inspect and manipulate Windows "guests." Plus it uses the term "hyperjacking" (using your hypervsior shim to inject/highjack the operating system's own hypervisor to disable protections) which is pretty awesome.</li>
<li><a href="https://blog.dfsec.com/ios/2025/05/30/blasting-past-ios-18/" target="_blank">Blasting Past iOS 18</a> - This, and the fact that you can target a huge population thanks to relatively homogenous hardware, is why an iOS 0day costs millions of dollars.</li>
<li><a href="https://starlabs.sg/blog/2025/05-gone-in-5-seconds-how-warn_on-stole-10-minutes/" target="_blank">Gone in 5 Seconds: How WARN_ON Stole 10 Minutes</a> - If you prefer Android exploitation, this write up on CVE-2023-6241 is great.</li>
<li><a href="https://googleprojectzero.blogspot.com/2025/05/the-windows-registry-adventure-8-exploitation.html" target="_blank">The Windows Registry Adventure #8: Practical exploitation of hive memory corruption</a> - I didn't know the windows registry hive used a custom memory allocator. The Windows registry is critical to Windows security, and exploiting it leads to SYSTEM more often than not.</li>
<li><a href="https://itm4n.github.io/hijacking-the-windows-marebackup-scheduled-task-for-privilege-escalation/" target="_blank">Hijacking the Windows "MareBackup" Scheduled Task for Privilege Escalation</a> - Windows search order makes a single vulnerable entry in the system's PATH an exploitable condition. In this case, a default schedule task can be started by any user on the system to run an arbitrary exe (renamed to powershell.exe).</li>
<li><a href="https://www.netspi.com/blog/technical-blog/red-teaming/elevating-privileges-with-sonicwall-netextender/" target="_blank">CVE-2025-23009 &amp; CVE-2025-23010: Elevating Privileges with SonicWall NetExtender</a> - Another Windows local privilege escalation (LPE), this time vai the third party SonicWall NetExtender client.</li>
<li><a href="https://blog.zsec.uk/azure-arc-c2aas/" target="_blank">LOLCLOUD - Azure Arc - C2aaS</a> - Use Azure as your command and control, including connecting to remote shell instances from the Azure portal! Notice the signature <a href="https://ludus.cloud/" target="_blank">Ludus</a> red desktop background in the endpoint folder creation screenshot. 😊</li>
<li><a href="https://www.thexero.co.uk/wifi/wireless-pivots" target="_blank">Wireless Pivots: How Trusted Networks Become Invisible Threat Vectors</a> - The power of probe requests to known less-secure networks is shown here. Sure, your corporate WiFi is EAP-TLS (Extensible Authentication Protocol - Transport Layer Security) with your own public-key infrastructure for end-to-end trust, but your employees connect to their home WiFi which isn't (it's WPA2 personal), and when they come back to work, an attacker can use those probe requests to set up a rouge access point, convince the device to join their "home" network and capture hashes.</li>
<li><a href="https://specterops.io/blog/2025/05/28/revisiting-com-hijacking/" target="_blank">Revisiting COM Hijacking</a> - An old favorite persistence method for Windows. And another <a href="https://ludus.cloud/" target="_blank">Ludus</a> desktop in the PoC video. 😊</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/MEhrn00/boflink" target="_blank">boflink</a> - Linker for Beacon Object Files.</li>
<li><a href="https://github.com/goforj/godump" target="_blank">godump</a> - A minimal, developer-friendly pretty-printer and debug dumper for Go structs, inspired by Laravel’s dump() and Symfony’s VarDumper.</li>
<li><a href="https://github.com/x86byte/Obfusk8" target="_blank">Obfusk8</a> - Obfusk8: Obfuscation library based on C++17 for windows binaries.</li>
<li><a href="https://github.com/Termitty/termitty" target="_blank">termitty</a> - The terminal automation framework.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://blog.zsec.uk/creativity-is-not-dead/" target="_blank">The Human Element: Why AI-Generated Content Is Killing Authenticity</a> - A reminder that Last Week in Security is 100% curated and written by humans.</li>
<li><a href="https://github.com/carloslack/KoviD" target="_blank">KoviD</a> - Red-Team Linux kernel rootkit.</li>
<li><a href="https://undetectag.com/products/undetectag" target="_blank">Undetectag</a> - "This printed circuit disc turns off your AirTag for 4 hours, and then turn it on again for 1 hour, reducing the chance that the thief is able to locate it."</li>
<li><a href="https://www.youtube.com/watch?v=IWP-8IMzQU8" target="_blank">Deep Dive: BadSuccessor – Full Active Directory Compromise</a> - Step by step walkthrough of last week's BadSuccessor attack, two ways plus some detection guidance.</li>
<li><a href="https://github.com/microsandbox/microsandbox" target="_blank">microsandbox</a> - Self-Hosted Platform for Secure Execution of Untrusted User/AI Code.</li>
<li><a href="https://github.com/Macmod/ldapx" target="_blank">ldapx</a> - Flexible LDAP proxy that can be used to inspect &amp; transform all LDAP packets generated by other tools on the fly. [You should watch <a href="https://www.youtube.com/watch?v=mKRS5Iyy7Qo" target="_blank">DEF CON 32 - MaLDAPtive</a> to understand the coolness of this tool.]</li>
<li><a href="https://blog.deeb.ch/posts/maldev-myths/" target="_blank">MalDev Myths</a> - "Since years i see techniques used in MalDev which are obsolete since a long time, or just applied wrongly."</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 453 (+1)</p>
<p>Blogs monitored: 422 (+2)</p>
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
