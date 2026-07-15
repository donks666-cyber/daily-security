Title: Last Week in Security (LWiS) - 2020-06-15
Date: 2020-06-16 16:50
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-06-15
Author: Erik
Summary: A new tunneling tool from <a href="https://twitter.com/shantanukhande" target="_blank">@shantanukhande</a>, new rootkit tradecraft and kernel mode payload from <a href="https://twitter.com/zerosum0x0" target="_blank">@zerosum0x0</a>, XSS via copy and paste by <a href="https://twitter.com/securitum_com" target="_blank">@securitum_com</a>, <a href="https://twitter.com/zecops" target="_blank">@ZecOps</a> drops a Windows 10 unauth RCE, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-06-08 to 2020-06-15.
MITRE ATT&amp;CK techniques are in brackets where appropriate.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://github.com/whid-injector/WHID" target="_blank">WHID</a> is a GSM-enabled WiFi HID injector that is now available <a href="https://www.aliexpress.com/item/4000357298489.html" target="_blank">on AliExpress</a> for just $37.90.</li>
<li><a href="https://blog.zecops.com/vulnerabilities/smbleedingghost-writeup-chaining-smbleed-cve-2020-1206-with-smbghost/" target="_blank">SMBleedingGhost Writeup: Chaining SMBleed (CVE-2020-1206) with SMBGhost</a> affects Windows 10 1903 and 1909 (1909 until <a href="https://support.microsoft.com/en-us/help/4560960/windows-10-update-kb4560960" target="_blank">KB4560960</a> from 2020-06-09, 1903 after <a href="https://support.microsoft.com/en-us/help/4512941/windows-10-update-kb4512941" target="_blank">KB4512941</a> from 2019-08-30, and before <a href="https://support.microsoft.com/en-us/help/4560960/windows-10-update-kb4560960" target="_blank">KB4560960</a>). It's a critical vulnerability (unauthenticated remote code execution), but the impact is limited to a subset of Windows versions.</li>
<li><a href="https://www.ehpus.com/post/smtp-injection-in-gsuite" target="_blank">SMTP Injection in Gsuite</a> allowed Zohar Shachar to spoof email from any @google.com address. This is a great find, and proof that there is still Bug Bounty gold even in the most popular applications.</li>
<li><a href="https://www.cybereason.com/blog/cybereason-honeypot-multistage-ransomware" target="_blank">Cybereason’s Newest Honeypot Shows How Multistage Ransomware Attacks Should Have Critical Infrastructure Providers on High Alert</a>. This is the second time this honey pot has been written about, but this time the attackers appear to be much more sophisticated. The attackers deployed ransomware early, but waited until the compromised as many systems as possible before detonating it for maximum effect. Would your environment have caught them early enough to prevent disaster?</li>
<li><a href="https://krebsonsecurity.com/2020/06/microsoft-patch-tuesday-june-2020-edition/" target="_blank">Microsoft Patch Tuesday, June 2020 Edition</a>. Krebs is always my go-to source for the Patch Tuesday round up.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://medium.com/@shantanukhande/red-team-using-sharpchisel-to-exfil-internal-network-e1b07ed9b49" target="_blank">Red Team: Using SharpChisel to exfil internal network</a>. Building off his post last week on wrapping Go in C#, <a href="https://twitter.com/shantanukhande" target="_blank">@shantanukhande</a> shows how to use Chisel to tunnel out of a network using websockets hosted by CloudFlare. This one is sure to give network defenders a hard time.</li>
<li><a href="https://zerosum0x0.blogspot.com/2020/06/heresys-gate-kernel-zwntdll-scraping.html" target="_blank">"Heresy's Gate": Kernel Zw*/NTDLL Scraping + "Work Out": Ring 0 to Ring 3 via Worker Factories</a>. Not a vulnerability, but rather rootkit tradecraft to execute private syscalls and a new kernel mode exploit payload.</li>
<li><a href="https://kieczkowska.com/2020/06/15/airdrop-forensics/" target="_blank">AirDrop Forensics</a> is a good dive into AirDrop, where to find AirDrop artifacts on macOS systems, how to analyze them, as well as how Bluetooth makes it possible for anyone nearby to guess your email &amp; phone number.</li>
<li><a href="https://research.securitum.com/the-curious-case-of-copy-paste/" target="_blank">The Curious Case of Copy &amp; Paste – on risks of pasting arbitrary content in browsers</a>. This writeup is a summary of research on issues in handling copying and pasting in: browsers, popular WYSIWYG editors, and websites which can lead to cross site scripting. Perhaps a new watering hole vector?</li>
<li><a href="http://jultika.oulu.fi/files/nbnfioulu-202004201485.pdf" target="_blank">Effectiveness of Linux Rootkit Detection Tools</a> is a masters thesis that tests common rootkit detection capabilities against various kernel mode and user mode rootkits. If nothing else it provides a single source of build steps for popular open source linux rootkits.</li>
<li><a href="https://www.solomonsklash.io/pe-parsing-defeating-hooking.html" target="_blank">PE Parsing and Defeating AV/EDR API Hooks in C++</a> This post is a look at defeating AV/EDR-created API hooks with code available <a href="https://github.com/SolomonSklash/UnhookingPOC" target="_blank">here</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><p><a href="https://github.com/mxrch/penglab" target="_blank">penglab</a> - Abuse of Google Colab for fun and profit. Google Colab is a free cloud service based on Jupyter Notebooks for machine-learning education and research. It provides a runtime fully configured for deep learning and free-of-charge access to a robust GPU. I'm surprised it took this long to get abused.</p>
</li>
<li><p>Windows Local Privilege Escalation [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</p>
<blockquote>
<ul>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=1945#c7" target="_blank">Windows: Insecure CSharedStream Object EoP</a> The great <a href="https://twitter.com/tiraniddo" target="_blank">@tiraniddo</a> develops his 8 month old "Won't Fix" Windows local privilege escalation bug into a full blown normal user to SYSTEM PoC. Expect to see this weaponized and in use in by next week and have a long shelf life.</li>
<li><a href="https://github.com/FuzzySecurity/Sharp-Suite#virttophys" target="_blank">VirtToPhys</a> is a small PoC to demonstrate how you can calculate the physical address for a kernel virtual address when exploiting driver bugs that allow you to map physical memory. VirtToPhys uses MsIo.sys, a WHQL signed driver that gives you colorful lights on your RAM (yes, seriously), <a href="https://github.com/active-labs/Advisories/blob/master/2019/ACTIVE-2019-012.md" target="_blank">CVE-2019-18845</a>.</li>
<li><a href="https://gist.github.com/ThunderGunExpress/5bd759bcc2dc6bac1ee22d9c62fd6c9a" target="_blank">SuRestore.cpp</a> - If you find yourself in the Backup Operators group, this little gem based on <a href="https://decoder.cloud/2018/02/12/the-power-of-backup-operatos/" target="_blank">older research</a> may be able to get you a SYSTEM shell.</li>
<li><a href="https://github.com/rxwx/spoolsystem">spoolsystem</a>  is a CNA script for Cobalt Strike which uses <a href="https://twitter.com/itm4n?lang=en">@itm4n</a> Print Spooler named pipe impersonation trick (<a href="https://blog.badsectorlabs.com/last-week-in-security-lwis-2020-05-18.html">LWiS 2020-05-18</a>) to gain SYSTEM privileges without creating any new process or relying on cross-process shellcode injection (if the selfinject method is used).</li>
</ul>
</blockquote>
</li>
<li><p><a href="https://github.com/libimobiledevice" target="_blank">libimobiledevice</a> is a collection of projects that allow for cross-platform protocol library to access iOS devices. This is the first release after a three year hiatus, and sees the release of two new tools, <a href="https://github.com/libimobiledevice/libirecovery/" target="_blank">libirecovery</a> and <a href="https://github.com/libimobiledevice/idevicerestore/" target="_blank">idevicerestore</a>.</p>
</li>
<li><p><a href="https://github.com/RedLectroid/SearchOutlook" target="_blank">SearchOutlook</a> is a C# tool to search through a running instance of Outlook for keywords.</p>
</li>
<li><p><a href="https://github.com/theryangeary/choose" target="_blank">choose</a> is a human-friendly and fast alternative to cut and (sometimes) awk. This may prove useful for cleaner pipelines for automated reconnaissance, etc.</p>
</li>
<li><p><a href="https://github.com/CCob/SharpBlock" target="_blank">SharpBlock</a> is a method of bypassing EDR's active projection DLL's by preventing entry point execution. Blog post <a href="https://ethicalchaos.dev/2020/06/14/lets-create-an-edr-and-bypass-it-part-2/" target="_blank">here</a>.</p>
</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/cloudflare/utahfs" target="_blank">UtahFS</a> is an encrypted storage system that provides a user-friendly FUSE drive backed by cloud storage in Go by CloudFlare. Use this to store things securely in the cloud - think DropBox but encrypted locally before upload.</li>
<li><a href="https://github.com/m4ll0k/Atlas" target="_blank">Atlas</a> is an open source tool that can suggest sqlmap tampers to bypass WAF/IDS/IPS. The tool is based on returned status code.</li>
<li><a href="https://github.com/urbanadventurer/urlcrazy/" target="_blank">urlcrazy</a> generates and tests domain typos and variations to detect and perform typo squatting, URL hijacking, phishing, and corporate espionage.</li>
<li><a href="https://github.com/S3cur3Th1sSh1t/PowerSharpPack" target="_blank">PowerSharpPack</a> is many useful offensive CSharp Projects wrapped into Powershell for easy usage.</li>
<li><a href="https://github.com/jafarlihi/revp" target="_blank">revp</a> is a C++ reverse HTTP proxy that works on Linux, Windows, and macOS.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
