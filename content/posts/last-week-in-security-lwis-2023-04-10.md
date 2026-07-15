Title: Last Week in Security (LWiS) - 2023-04-10
Date: 2023-04-10 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-04-10
Author: Erik
Summary: Windows installer LPE (<a href="https://twitter.com/a_denkiewicz" target="_blank">@a_denkiewicz</a>), unhooking without direct syscalls (<a href="https://twitter.com/kharosx0" target="_blank">@Kharosx0</a>), dynamic linking injection (<a href="https://twitter.com/praetorianlabs" target="_blank">@praetorianlabs</a>), suspending AV (<a href="https://twitter.com/freefirex2" target="_blank">@freefirex2</a>), dir2json (<a href="https://twitter.com/bitsadmin" target="_blank">@bitsadmin</a>), DPAPISnoop (<a href="https://twitter.com/lefterispan" target="_blank">@lefterispan</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-03-20 to 2023-04-10.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.vice.com/en/article/wxjqz4/the-cure-tried-to-stop-scalpers-brokers-are-selling-entire-ticketmaster-accounts-instead" target="_blank">The Cure Tried to Stop Scalpers. Brokers Are Selling Entire Ticketmaster Accounts Instead</a>. That's the thing about hackers, they will find a way around arbitrary restrictions.</li>
<li><a href="https://www.sophos.com/en-us/security-advisories/sophos-sa-20230404-swa-rce" target="_blank">CVE-2023-1671: Critical Pre-Auth Command Injection Vulnerability in Sophos Web Appliance</a>. "A pre-auth command injection vulnerability in the warn-proceed handler allowing execution of arbitrary code."</li>
<li><a href="https://www.cobaltstrike.com/blog/stopping-cybercriminals-from-abusing-security-tools/" target="_blank">Stopping Cybercriminals From Abusing Security Tools</a>. Is this the first time a C2 vendor has taken "proactive" action against hosted copies of its own software?</li>
<li><a href="https://www.nytimes.com/2023/03/20/world/europe/greece-spyware-hacking-meta.html" target="_blank">Meta Manager Was Hacked With Spyware and Wiretapped in Greece</a>. Unsure of the phone's OS (the capability <a href="https://www.nytimes.com/interactive/2022/12/08/us/politics/intellexa-commercial-proposal.html" target="_blank">covers both Android and iOS</a>), but it was an SMS link that appears to be the infection vector (1-click). This is your reminder to reboot your phone often - persistence of Predator was an extra 2.4 million euro add on in 2021.</li>
<li><a href="https://www.3cx.com/blog/news/desktopapp-security-alert/" target="_blank">3CX DesktopApp Security Alert</a>. One of hte bigger supply chian attacks since SolarWinds.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://github.blog/2023-03-23-build-a-secure-code-mindset-with-the-github-secure-code-game/" target="_blank">Build a secure code mindset with the GitHub Secure Code Game</a>. Learn CodeQL in a fun CTF-style "game." For pointers, be sure to read: <a href="https://github.blog/2023-03-31-codeql-zero-to-hero-part-1-the-fundamentals-of-static-analysis-for-vulnerability-research/" target="_blank">CodeQL zero to hero</a>.</li>
<li><a href="https://blog.doyensec.com//2023/03/21/windows-installer.html" target="_blank">Windows Installer EOP (CVE-2023-21800)</a>. "This blog post describes the details and methodology of our research targeting the Windows Installer (MSI) installation technology." Spoiler: "the environment variables set by the unprivileged user were also used in the context of the SYSTEM user invoked by the repair operation."</li>
<li><a href="https://www.signal-labs.com/blog/analysis-of-edr-hooks-bypasses-amp-our-rust-sample" target="_blank">In-Memory Disassembly for EDR/AV Unhooking</a>. Have your cake and eat it too. Without using hooked functions, Christopher Vella is able to call unhooked functions without direct syscalls. The <a href="https://github.com/Signal-Labs/iat_unhook_sample/blob/main/src/pe_helper.rs#L161" target="_blank">code</a> is nicely commented. It's in rust too (and probably written on arch btw).</li>
<li><a href="https://www.praetorian.com/blog/dynamic-linking-injection/" target="_blank">Dynamic Linking Injection and LOLBAS Fun</a>. Some very sneaky DLI exploitation using system binaries to drop and run secondary payloads.</li>
<li><a href="https://www.horizon3.ai/veeam-backup-and-replication-cve-2023-27532-deep-dive/" target="_blank">Veeam Backup and Replication CVE-2023-27532 Deep Dive</a>. Unauthenticated access to cleartext credentials? Yikes.</li>
<li><a href="https://fortynorthsecurity.com/blog/obfuscating-c2-traffic-with-google-cloud-functions/" target="_blank">Obfuscating C2 Traffic with Google Cloud Functions</a>. Tired of the blue team blocking your egress domains? Why not use a high reputation domain like cloudfunctions.net?</li>
<li><a href="https://thalpius.com/2023/03/23/microsoft-defender-for-identity-owin-http-listener/" target="_blank">Microsoft Defender for Identity OWIN HTTP Listener</a>. An interesting dive into MS Defender for identity's API (localhost only and cert auth protected). It has some interesting features like the ability to get a handle to the Group Managed Service Account token. Staying tuned for more.</li>
<li><a href="https://research.nccgroup.com/2023/04/05/bypassing-software-update-package-encryption-extracting-the-lexmark-mc3224i-printer-firmware-part-1/" target="_blank">Bypassing software update package encryption - extracting the Lexmark MC3224i printer firmware</a>. This part 1 is cut off in the opening summary, but <a href="https://research.nccgroup.com/2023/04/05/analyzing-a-pjl-directory-traversal-vulnerability-exploiting-the-lexmark-mc3224i-printer-part-2/" target="_blank">part 2</a> has some great low level exploitation.</li>
<li><a href="https://haggis-m.medium.com/living-off-the-land-drivers-a5d74d45e77a" target="_blank">Living Off The Land Drivers</a>. <a href="https://www.loldrivers.io/" target="_blank">loldirvers</a> is a curated list of Windows drivers used by adversaries to bypass security controls and carry out attacks.</li>
<li><a href="https://github.blog/2023-04-06-pwning-pixel-6-with-a-leftover-patch/" target="_blank">Pwning Pixel 6 with a leftover patch</a>. Excellent low level android exploitation content.</li>
<li><a href="https://blog.exodusintel.com/2023/04/06/escaping-adobe-sandbox-exploiting-an-integer-overflow-in-microsoft-windows/" target="_blank">Escaping Adobe Sandbox: Exploiting an Integer Overflow in Microsoft Windows Crypto Provider</a>. Some good low level windows Exploitation.</li>
<li><a href="https://modexp.wordpress.com/2023/04/07/shellcode-entropy-reduction-with-base-n-encoding/" target="_blank">Shellcode: Entropy Reduction With Base-32 Encoding.</a>. A custom Base-32 encoding can help data appear less random.</li>
<li><a href="https://outflank.nl/blog/2023/03/28/attacking-visual-studio-for-initial-access/" target="_blank">Attacking Visual Studio for Initial Access</a>. It turns out you don't even have to compile a malicious solution, just open it, to get pwned.</li>
<li><a href="https://posts.specterops.io/id-tap-that-pass-8f79fff839ac" target="_blank">I'd TAP That Pass</a>. Temporary Access Passwords can bypass MFA in some situations to allow pivoting into Azure from a compromised user context.</li>
<li><a href="https://www.trustedsec.com/blog/disabling-av-with-process-suspension/" target="_blank">Disabling AV With Process Suspension</a>. AV giving you a hard time? Put it on ice while you do your detected actions then bring it back like nothing happened. Be sure to test this as it can cause instability while the AV is suspended.</li>
<li><a href="https://www.wiz.io/blog/azure-active-directory-bing-misconfiguration" target="_blank">BingBang: AAD misconfiguration led to Bing.com results manipulation and account takeover</a>. Wiz has proven again and again they are the undisputed kings of cloud. Always scared/excited when a new technical post drops from Wiz.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://research.nccgroup.com/2023/04/05/tool-release-shouganaiyo-loader-a-tool-to-force-jvm-attaches/" target="_blank">Tool Release - shouganaiyo-loader: A Tool to Force JVM Attaches</a>. Inject your own Java code into processes that have disabled the agent attach API.</li>
<li><a href="https://gist.github.com/LinusHenze/728db96a836b6817ecb727cfbde606b3" target="_blank">PoC for CVE-2023-28206</a> - exploit for an out-of-bounds write in the IOSurfaceAccelerator, allowing a malicious actor to execute arbitrary code with kernel privileges on macOS/iOS by utilizing a specially crafted application. Note this is just a kernel panic PoC.</li>
<li><a href="https://github.com/0xinfection/epscalate" target="_blank">EPScalate</a> - Exploit for elevation of privilege vulnerability in QuickHeal's Seqrite EPS.</li>
<li><a href="https://github.com/lsecqt/OffensiveCpp" target="_blank">OffensiveCpp</a> - This repo contains C/C++ snippets that can be handy in specific offensive scenarios.</li>
<li><a href="https://github.com/knight0x07/PoC-Malware-TTPs/tree/main/PrintBrm-Impant-Exec" target="_blank">Implant execution via PrintBrm.exe</a> - use PrintBrm to extract &amp; execute an implant from an ISO.</li>
<li><a href="https://github.com/Maldev-Academy/EntropyReducer" target="_blank">EntropyReducer</a> - Reduce Entropy And Obfuscate Your Payload With Serialized Linked Lists.</li>
<li><a href="https://github.com/screamz2k/PhoenixC2" target="_blank">PhoenixC2</a> - Command &amp; Control-Framework created for collaboration in python3. This looks very alpha.</li>
<li><a href="https://github.com/DragoQCC/HardHatC2" target="_blank">HardHatC2</a> - A C# Command &amp; Control framework. Another alpha C2, but this one has a lot of features in the agent already.</li>
<li><a href="https://github.com/bitsadmin/dir2json" target="_blank">dir2json</a> - Tool for efficient directory enumeration. Read the <a href="https://blog.bitsadmin.com/blog/digging-for-secrets" target="_blank">blog post</a>.</li>
<li><a href="https://github.com/leftp/DPAPISnoop" target="_blank">DPAPISnoop</a> - A C# tool to output crackable DPAPI hashes from user MasterKeys.</li>
<li><a href="https://github.com/BeichenDream/GodPotato" target="_blank">GodPotato</a> - ImpersonatePrivilege == SYSTEM. At this point I think its just a feature of Windows.</li>
<li><a href="https://github.com/ZeroMemoryEx/Chaos-Rootkit" target="_blank">Chaos-Rootkit</a> - x64 ring0 Rootkit with Process Hiding and Privilege Escalation Capabilities.</li>
<li><a href="https://github.com/realoriginal/rogue" target="_blank">rogue</a> - A barebones template of 'rogue' aka a simple recon and agent deployment I built to communicate over ICMP. Well, without the ICMP code.</li>
<li><a href="https://github.com/XiaoliChan/wmiexec-Pro" target="_blank">wmiexec-Pro</a> - Lateral movement with WMI using only port 135.</li>
<li><a href="https://github.com/n00bes/inline-syscall" target="_blank">inline-syscall</a> - Inline syscalls made for MSVC supporting x64 and x86.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/nsarrazin/serge" target="_blank">serge</a> - A web interface for chatting with Alpaca through llama.cpp. Fully dockerized, with an easy to use API.</li>
<li><a href="https://0x64marsh.com/?p=689" target="_blank">Game Hacks: Among Us - IL2CPP Walkthrough</a>. The same techniques can be used to locate sensitive data and craft exploits in more serious applications.</li>
<li><a href="https://github.com/espanso/espanso" target="_blank">espanso</a> - Cross-platform Text Expander written in Rust.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 338 (+1)</p>
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
