Title: Last Week in Security (LWiS) - 2020-10-05
Date: 2020-10-05 23:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-10-05
Author: Erik
Summary: Sysmon exploit by <a href="https://twitter.com/0x00dtm" target="_blank">@0x00dtm</a>, physical smartcard/kerberos attack tools by <a href="https://twitter.com/_EthicalChaos_" target="_blank">@_EthicalChaos_</a>, UACMe update (and Defender bypasses) by <a href="https://twitter.com/hFireF0X" target="_blank">@hFireF0X</a>, dynamic instrumentation by <a href="https://twitter.com/rh0main" target="_blank">@rh0main</a>, a new checksec from <a href="https://twitter.com/mtarral" target="_blank">@mtarral</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-09-28 to 2020-10-05.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/uhs-hospitals-hit-by-reported-country-wide-ryuk-ransomware-attack/" target="_blank">UHS hospitals hit by reported country-wide Ryuk ransomware attack</a>. Two weeks ago was the first possible death related to ransomware. There are at least three being reported due to this. Of note, while many ransomware crews stated they would not target hospitals when the pandemic started, Ryuk remained silent.</li>
<li><a href="https://home.treasury.gov/system/files/126/ofac_ransomware_advisory_10012020_1.pdf" target="_blank">Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments</a>. Cybersecurity firms now need to register as money services to legally make ransomware payments, and "payments demanded as a result of malicious cyber-enabled activities will be reviewed by OFAC on a case-by-case basis with a presumption of denial."</li>
<li><a href="https://www.intezer.com/ost-map/#" target="_blank">OST Map</a> from Intezer connects threat actors with the tools they use. This is an interesting resource for adversary emulation purposes. If you enjoy this you may also like the <a href="https://embed.kumu.io/0b023bf1a971ba32510e86e8f1a38c38#apt-index/" target="_blank">CyberWar Map</a>.</li>
<li><a href="https://sectigo.com/resource-library/sectigo-to-be-acquired-by-gi-partners" target="_blank">Sectigo to Be Acquired by GI Partners</a>. The Root CA shell game continues (Sectigo used to be Comodo). This will trigger another round of compliance checks.</li>
<li><a href="https://til.simonwillison.net/til/til/bash_escaping-a-string.md" target="_blank">Escaping strings in Bash using !:q</a>. A quick tip for bash users.</li>
<li><a href="https://github.blog/2020-09-30-code-scanning-is-now-available/" target="_blank">Code scanning is now available!</a>. GitHub code scanning attempts to find vulnerabilities in your code via static analysis before it gets deployed. They are using the acquisition of Semmle to push CodeQL even further. This proactive approach is a good thing for security.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://shells.systems/defeat-bitdefender-total-security-using-windows-api-unhooking-to-perform-process-injection/" target="_blank">Defeat Bitdefender total security using windows API unhooking to perform process injection</a>. This post shows practical API unhooking and how to discover/repair hooked API calls using <a href="https://x64dbg.com/" target="_blank">x64dbg</a>.</li>
<li><a href="https://undev.ninja/sysmon-internals-from-file-delete-event-to-kernel-code-execution/" target="_blank">Sysmon Internals - From File Delete Event to Kernel Code Execution</a>. In addition to some file delete and shredding detection bypasses, this post shows how the file delete event logging is actually a write-what-where primitive from usermode to the Windows kernel. It goes on to exploit this into full kernel code execution. Demo <a href="https://mega.nz/file/h8FmGDrY#kInVJtXYY5kMj6Rk3aqNHsAHYPIYZuSdyVsxeXeJ7CA" target="_blank">here</a>, code <a href="https://github.com/NtRaiseHardError/Sysmon" target="_blank">here</a>. The post also includes detections and a YARA rule as well.</li>
<li><a href="https://ethicalchaos.dev/2020/10/04/attacking-smart-card-based-active-directory-networks/" target="_blank">Attacking Smart Card Based Active Directory Networks</a>. On networks where physical smart cards are in use (government uses them heavily), <a href="https://github.com/ccob/Rubeus" target="_blank">Rubeus</a> can now be used with a smartcard and PIN stolen with <a href="https://github.com/CCob/PinSwipe" target="_blank">PinSwipe</a> to get a kerberos TGT that is valid for 7 days.</li>
<li><a href="https://blog.ropnop.com/storing-tokens-in-browser/" target="_blank">How to Store Session Tokens in a Browser (and the impacts of each)</a>. Modern web applications have to store session tokens in the browser some how, and there are many different ways to do it. This post shows examples of each, and how they can be accessed if the page is vulnerable to cross site scripting (XSS).</li>
<li><a href="https://www.gremwell.com/breaking-jcaptcha-tensorflow-aocr" target="_blank">Breaking JCaptcha using Tensorflow and AOCR</a>. Simple Captchas are no match for machine learning. Integrate this into your attack workflow when brute forcing or spraying is allowed.</li>
<li><a href="https://www.gremwell.com/firefox-xss-302" target="_blank">Forcing Firefox to Execute XSS Payloads during 302 Redirects</a>. A GET parameter reflected into the HTTP response of a 302 allows for XSS using one of the tricks listed in this short post.</li>
<li><a href="https://swapcontext.blogspot.com/2020/10/uacme-35-wd-and-ways-of-mitigation.html" target="_blank">UACMe 3.5, WD and the ways of mitigation</a>. The canonical source of UAC bypasses, UACMe has been updated to 3.5, and lots of old code was removed. The author also broke down each working bypass and provided potential defender bypasses in this post and added the bypasses to the 3.5 release.</li>
<li><a href="https://dfir.ru/2020/10/03/exporting-registry-hives-from-a-live-system/" target="_blank">Exporting registry hives from a live system</a>. This Digital Forensics &amp; Incident Response blog post is aimed at IR practitioners looking to recover live forensics but is just as useful for red teamers looking to gather information from registry hives.</li>
<li><a href="https://www.romainthomas.fr/publication/20-bh-asia-dbi/" target="_blank">Dynamic Binary Instrumentation Techniques to Address Native Code Obfuscation</a>. This is a very cool talk on instrumenting Android applications to aid in reverse engineering.</li>
<li><a href="https://www.lykosec.com/blog/the-hidden-dangers-of-network-printers" target="_blank">The Hidden Dangers of Network Printers</a>. On engagements open printers are often discovered. This post shows the potential dangers of printers in the enterprise.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/3CORESec/SIEGMA" target="_blank">SIEGMA</a> aims to automate the creation of SIEM rule consumables by leveraging a pre-defined set of configurations/mappings and by utilizing the <a href="https://github.com/Neo23x0/sigma" target="_blank">sigma</a> rule format and engine.</li>
<li><a href="https://github.com/mez-0/DecryptRDCManager" target="_blank">DecryptRDCManager</a> is a .NET port of <a href="https://github.com/nettitude/PoshC2/blob/master/resources/modules/Decrypt-RDCMan.ps1" target="_blank">Decrypt-RDCMan.ps1</a> which was written by <a href="https://twitter.com/benpturner" target="_blank">Ben Turner</a> and <a href="https://twitter.com/scriptmonkey_" target="_blank">Rich Hicks</a>. This tool will decrypt credentials from <a href="https://techcommunity.microsoft.com/t5/exchange-team-blog/introducing-remote-desktop-connection-manager-rdcman-2-2/ba-p/592989" target="_blank">Remote Desktop Manager</a> by using the functionality from the <a href="https://github.com/mez-0/DecryptRDCManager/blob/master/DLLs/RDCMan.dll" target="_blank">RDCMan.DLL</a>.</li>
<li><a href="https://github.com/rasta-mouse/Fork-n-Run" target="_blank">Fork-n-Run</a>. This is great raw C# material for building into your own tools (PPID spoofing, BlockDLLs, argument spoofing, comms via pipes).</li>
<li><a href="https://github.com/dafthack/MFASweep" target="_blank">MFASweep</a> is a PowerShell script that attempts to log in to various Microsoft services using a provided set of credentials and will attempt to identify if MFA is enabled. Depending on how conditional access policies and other multi-factor authentication settings are configured some protocols may end up being left single factor. It also has an additional check for ADFS configurations and can attempt to log in to the on-prem ADFS server if detected. Be warned, this will attempt 7 authentications, so be sure to use a correct password or possibly get locked out! Blog post <a href="https://www.blackhillsinfosec.com/exploiting-mfa-inconsistencies-on-microsoft-services/" target="_blank">here</a>.</li>
<li><a href="https://github.com/EncodeGroup/AggressiveGadgetToJScript" target="_blank">AggressiveGadgetToJScript</a> is a Cobalt Strike Aggressor script to generate GadgetToJScript payloads. It uses the QueueUserAPC injection method and injects into notepad.exe (you should change this).</li>
<li><a href="https://github.com/kkamagui/bitleaker" target="_blank">bitleaker</a> is a complete physical attack tool (bootable USB) that leverages <a href="https://nvd.nist.gov/vuln/detail/CVE-2018-6622" target="_blank">CVE-2018-6622</a> (BIOS sleep TPM bug) and the new <a href="https://nvd.nist.gov/vuln/detail/CVE-2020-0526" target="_blank">CVE-2020-0526</a> to enable the mounting of Bitlocker encrypted drives without the user's password which is normally required. If devices are out of your physical control (work from home, travel) this bug/exploit applies to you. Update your systems to the latest BIOS firmware, disable sleep in the BIOS, or use BitLocker with a PIN to mitigate this.</li>
<li><a href="https://github.com/denandz/GLORP" target="_blank">GLORP</a> is a command line HTTP intercept proxy. The idea is to provide a CLI based tool for when you wanna-look-at-this-thing-real-quick and not fire up yet another full-fat container/vm/whatever with Burp and so forth. Looking for more GUI? Read on...</li>
<li><a href="https://github.com/dstotijn/hetty" target="_blank">hetty</a> is an HTTP toolkit for security research. It aims to become an open source alternative to commercial software like Burp Suite Pro, with powerful features tailored to the needs of the infosec and bug bounty community. Currently in the early stages, this is an interesting project to watch.</li>
<li><a href="https://github.com/Neo23x0/Raccine" target="_blank">Raccine</a> is a simple ransomware vaccine that kills the process tree that invokes vssadmin or wmic calls to delete volume shadow copies by registering as a debugger for vssadmin and wmic. This is a neat trick that will likely work against many ransomware variants.</li>
<li><a href="https://github.com/elsaland/elsa" target="_blank">elsa</a> is a minimal, fast and secure runtime for Javascript and Typescript written in Go. This could be used to create an embedded scripting environment in your Go malware a la <a href="https://github.com/gen0cide/gscript" target="_blank">gscript</a>.</li>
<li><a href="https://github.com/zznop/sploit" target="_blank">sploit</a> is a Go package that aids in binary analysis and exploitation. Think of it as the start of a Go version of <a href="https://github.com/Gallopsled/pwntools" target="_blank">pwntools</a>.</li>
<li><a href="https://github.com/epi052/feroxbuster" target="_blank">feroxbuster</a> is a fast, simple, recursive content discovery tool written in Rust.</li>
<li><a href="https://github.com/AltF5/CSharp-CmdLineHelper-Parser" target="_blank">CSharp-CmdLineHelper-Parser</a> is a "no frills" 1 class-only, C# .NET command line parser with support for - and / args, switches only, and Name : Values. This will be useful for small C# projects.</li>
<li><a href="https://github.com/Wenzel/checksec.py" target="_blank">checksec.py</a> is a complete checksec tool in python with rich terminal output. It supports PE and ELF files and there is an exe in the Github release.</li>
<li><a href="https://github.com/sickcodes/Docker-eyeOS" target="_blank">Docker-eyeOS</a> runs iOS (xnu-arm64) in a Docker container! Supports KVM + iOS kernel debugging (GDB)! It's like having your own local <a href="https://corellium.com/" target="_blank">Corellium</a>.</li>
<li><a href="https://www.praetorian.com/blog/tool-for-password-spraying-emulation" target="_blank">A New Tool for Password Spraying Emulation</a>. Spray at scale using GCP/AWS with this new tool from Praetorian. Code <a href="https://github.com/praetorian-inc/trident" target="_blank">here</a>.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/vulmon/Vulmap" target="_blank">Vulmap</a> is an online local vulnerability scanner. It's aimed at organizations to do vulnerability scanning across their fleets, but it can also be used for one off checks to see what is available to privesc.</li>
<li><a href="https://github.com/sdnewhop/grinder" target="_blank">grinder</a> is a python framework to automatically discover and enumerate hosts from different back-end systems (Shodan, Censys). Add this to your enumeration pipeline.</li>
<li><a href="https://github.com/mxrch/ghunt" target="_blank">GHunt</a> is a tool to investigate Google Accounts given only an email.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
