Title: Last Week in Security (LWiS) - 2022-01-03
Date: 2022-01-03 23:25
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-01-03
Author: Erik
Summary: New RE training (<a href="https://twitter.com/zeroperil" target="_blank">@ZeroPeril</a>), macOS Gatekeeper bypass (<a href="https://twitter.com/ethicalhax" target="_blank">@ethicalhax</a> + <a href="https://twitter.com/patrickwardle" target="_blank">@patrickwardle</a>), remote PS (<a href="https://twitter.com/dazzyddos" target="_blank">@dazzyddos</a>), LastPass breach? (<a href="https://twitter.com/WPalant" target="_blank">@WPalant</a>), Log4j to pwn Unifi (<a href="https://twitter.com/sprocket_ed" target="_blank">@sprocket_ed</a>), O365 file spoof for phishing (<a href="https://twitter.com/mrd0x" target="_blank">@mrd0x</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-12-20 to 2022-01-03.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://thehackernews.com/2021/12/china-suspends-deal-with-alibaba-for.html" target="_blank">China suspends deal with Alibaba for not sharing Log4j 0-day first with the government</a>. Note this isn't as bad as the headline makes it seems, as China only suspended a "cooperative partnership... regarding cybersecurity threats and information-sharing platforms." Regardless, it sends a clear message. If you find a vulnerability in China, you'd better tell the government about it before anyone else.</li>
<li><a href="https://zeroperil.co.uk/training-course-announcement/" target="_blank">ZeroPeril Deep dive into executable packers &amp; malware unpacking Training Course Announcement</a>. New fully remote training that uses x86/x64dbg. Training is fully remote (Teams).</li>
<li><a href="https://palant.info/2021/12/29/how-did-lastpass-master-passwords-get-compromised/" target="_blank">How did LastPass master passwords get compromised?</a>. A number of users received emails that their master password had correctly been used from a suspicious location, even after changing it. Is this an email error or something deeper? Either way, not a good look for LastPass, which has already <a href="https://www.vice.com/en/article/pkd88v/lastpass-free-accounts-will-now-work-on-either-your-phone-or-computer-not-both" target="_blank">lost credibility</a>.</li>
<li><a href="https://twitter.com/miketheitguy/status/1477097527593734144" target="_blank">In 2022, YYMMDDhhmm formatted times exceed signed int range, breaking Microsoft services</a>. Duct tape and glue. It's all just duct tape and glue.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://sensepost.com/blog/2021/android-application-testing-using-windows-11-and-windows-subsystem-for-android/" target="_blank">Android Application Testing Using Windows 11 and Windows Subsystem for Android</a>. You've heard of the Windows subsystem for Linux, but how about the Windows subsystem for Andrid? Now you can use your favorite mobile assessment tools like objection and Burp suite without needing a real android device!</li>
<li><a href="https://dhiyaneshgeek.github.io/mobile/security/2021/12/25/hopper-disassembler/" target="_blank">Hopper Disassembler</a>. This post shows how to use Hopper to bypass simple jailbreak detection by modifying a single jump instruction. Sometimes it is that simple, but the trick is knowing which byte to change.</li>
<li><a href="https://positive.security/blog/ms-teams-1-feature-4-vulns" target="_blank">MS Teams: 1 feature, 4 vulnerabilities</a>. None of these are severe, but some are simple issues that you wouldn't expect a market leader in connectivity to be making.</li>
<li><a href="https://arxiv.org/pdf/2112.05719.pdf" target="_blank">Attacks on Wireless Coexistence: Exploiting Cross-Technology Performance Features for Inter-Chip Privilege Escalation (PDF)</a>. System on a Chip (SoC) designs can include multiple wireless technologies with shared components. This overlap can lead to one compromised protocol being able to read or edit data on another medium via the shared resources.</li>
<li><a href="https://www.sprocketsecurity.com/blog/how-to-exploit-log4j-vulnerabilities-in-vmware-vcenter" target="_blank">How to exploit Log4j vulnerabilities in VMWare vCenter</a>. Unauthenticated remote code execution as root against vCenter via Log4j. The post covers good post-exploitation options and even drops the PoC: <a href="https://github.com/puzzlepeaches/Log4jCenter" target="_blank">Log4jCenter</a>.</li>
<li><a href="https://objective-see.com/blog/blog_0x6A.html" target="_blank">Where's the Interpreter!? (CVE-2021-30853)</a>. This dead-simple Gatekeeper bypass makes you wonder what other silly tricks are out there. Patrick doesn't stop at the PoC and dives deep into the root cause of this bug. Notably this fix is absent for Catalina (10.15.7), however my very limited testing indicates it may not be vulnerable.</li>
<li><a href="https://research.checkpoint.com/2021/a-deep-dive-into-doublefeature-equation-groups-post-exploitation-dashboard/" target="_blank">A Deep Dive into DoubleFeature, Equation Group’s Post-Exploitation Dashboard</a>. If you're interested in what "real" APT malware looks like, this long post covers a lot of tools.</li>
<li><a href="https://dazzyddos.github.io/posts/Remote-Process-Enumeration-with-WTS-Set-Of-APIs/" target="_blank">Remote Process Enumeration with WTS Set of Windows APIs</a>. With the proper privileges you can get a remote process list using standard Windows APIs. This would be a nice tool to avoid machines with EDR or other programs running.</li>
<li><a href="https://dawnslab.jd.com/CVE-2021-31956/" target="_blank">CVE-2021-31956 vulnerability analysis (Chinese)</a>. This post explores CVE-2021-31956, a local privilege escalation within Windows due to a kernel memory corruption bug which was patched within the June 2021 Patch Tuesday and contains actual exploit code.</li>
<li><a href="https://windows-internals.com/hyperguard-secure-kernel-patch-guard-part-1-skpg-initialization/?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=hyperguard-secure-kernel-patch-guard-part-1-skpg-initialization" target="_blank">HyperGuard – Secure Kernel Patch Guard: Part 1 – SKPG Initialization</a></li>
<li><a href="https://rastamouse.me/dumping-lsass-with-duplicated-handles/" target="_blank">Dumping LSASS with Duplicated Handles</a>. Rastamouse walks through how to use duplicated handles to dump LSASS which builds on his previous post on enumerating and duplicating handles. It still dumps to disk, so a pure in-memory implementation will get you even more evasion points.</li>
<li><a href="https://www.sprocketsecurity.com/blog/another-log4j-on-the-fire-unifi" target="_blank">Another Log4j on the fire: Unifi</a>. Another great walkthrough on how to go from login page to backdoored appliance from Nicholas at Sprocket Security. 67,000 exposed instances on shodan... RIP in peace.</li>
<li><a href="https://mrd0x.com/phishing-o365-spoofed-cloud-attachments/?no-cache=1" target="_blank">Phishing With Spoofed Cloud Attachments</a>. "Abuse the way O365 Outlook renders cloud attachments to make malicious executable cloud attachments look like harmless files." This is phishing gold. Paired with a nice sandbox aware firewall/redirector it will likely yield success with a simple docuement.pdf.exe payload because the mail looks so good.</li>
<li><a href="https://boringappsec.substack.com/p/edition-14-to-waf-or-not-to-waf" target="_blank">Edition 14: To WAF or not to WAF</a> Effectiveness of WAFs are a hotly debated subject in AppSec circles. This post tries to bring a structure to that discussion.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Cracked5pider/KaynLdr" target="_blank">KaynLdr</a> is a Reflective Loader written in C / ASM. It uses direct syscalls to allocate virtual memory as RW and changes it to RX. It erases the DOS and NT Headers to make it look less suspicious in memory.</li>
<li><a href="https://github.com/pwn1sher/WMEye" target="_blank">WMEye</a> is a post exploitation tool that uses WMI Event Filter and MSBuild Execution for lateral movement.</li>
<li><a href="https://github.com/Yamato-Security/hayabusa" target="_blank">hayabusa</a> is a sigma-based threat hunting and fast forensics timeline generator for Windows event logs. Reminds me of <a href="https://github.com/countercept/chainsaw" target="_blank">chainsaw</a>.</li>
<li><a href="https://research.nccgroup.com/2021/12/29/tool-release-shouganaiyo-loader-a-tool-to-force-jvm-attaches/" target="_blank">Tool Release – shouganaiyo-loader: A Tool to Force JVM Attaches</a>. This loader forces Java agents to be loaded and can inject Java or JVMTI agents into Java processes (Sun/Oracle HotSpot or OpenJ9).</li>
<li><a href="https://github.com/airbus-cert/Invoke-Bof" target="_blank">Invoke-Bof</a> loads any Beacon Object File using Powershell!</li>
<li><a href="https://github.com/cedowens/Inject_Dylib" target="_blank">Inject_Dylib</a> is Swift code to programmatically perform dylib injection.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://gitlab.com/invuls/pentest-projects/pcf" target="_blank">Pentest Collaboration Framework</a> is an open source, cross-platform, and portable toolkit for automating routine processes when carrying out vulnerability testing.</li>
<li><a href="https://github.com/andyjsmith/Registry-Spy" target="_blank">Registry-Spy</a> is a cross-platform registry browser for raw Windows registry files written in Python.</li>
<li><a href="https://github.com/FlamingSpork/iptable_evil" target="_blank">iptable_evil</a> is a very specific backdoor for iptables that allows all packets with the evil bit set, no matter the firewall rules. While this specific implementation is modeled on a joke RFC, the code could easily be modified to be more stealthy/useful.</li>
<li><a href="https://github.com/MichaelDim02/Narthex" target="_blank">Narthex</a> is a modular &amp; minimal dictionary generator for Unix and Unix-like operating system written in C and Shell. It contains autonomous Unix-style programs for the creation of personalized dictionaries that can be used for password recovery &amp; security assessments.</li>
<li><a href="https://github.com/spieglt/whatfiles" target="_blank">whatfiles</a> is a Linux utility that logs what files another program reads/writes/creates/deletes on your system. It traces any new processes and threads that are created by the targeted process as well.</li>
<li><a href="https://hatsploit.netlify.app/" target="_blank">The HatSploit Framework</a> is a modular penetration testing platform that enables you to write, test, and execute exploit code.</li>
<li><a href="https://github.com/diversenok/TokenUniverse" target="_blank">TokenUniverse</a> is an advanced tool for working with access tokens and Windows security policy.</li>
<li><a href="https://github.com/mitchmoser/LACheck" target="_blank">LACheck</a> is a multithreaded C# .NET assembly local administrative privilege enumeration. That's underselling it though, this has lots of cool enumeration capabilities such as remote EDR driver enumeration.</li>
<li><a href="https://dustinbrett.com/" target="_blank">Desktop environment in the browser</a>. This is just... wow. Code here: <a href="https://github.com/DustinBrett/daedalOS" target="_blank">daedalOS</a>.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
