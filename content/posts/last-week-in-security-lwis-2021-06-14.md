Title: Last Week in Security (LWiS) - 2021-06-14
Date: 2021-06-14 22:45
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-06-14
Author: Erik
Summary: Decrypting Veeam passwords (<a href="https://twitter.com/checkymander" target="_blank">@checkymander</a>), bypass Windows kASLR (<a href="https://twitter.com/33y0re" target="_blank">@33y0re</a>), Code &gt; Commands (<a href="https://twitter.com/TheXC3LL" target="_blank">@TheXC3LL</a>), AWS SSO phishing (<a href="https://twitter.com/christophetd" target="_blank">@christophetd</a>), forest trust 🧙‍♂️ (<a href="https://twitter.com/_dirkjan" target="_blank">@_dirkjan</a>), syscall detection bypass (<a href="https://twitter.com/passthehashbrwn" target="_blank">@passthehashbrwn</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-06-08 to 2021-06-14.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.vice.com/en/article/7kvkqb/how-ea-games-was-hacked-slack" target="_blank">How Hackers Used Slack to Break into EA Games</a>. Nothing crazy here, but the "just ask" principle works more often than not. Most people like to be helpful, and attackers can exploit that helpfulness for access if unchecked.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://blog.checkymander.com/red%20team/veeam/decrypt-veeam-passwords/" target="_blank">Decrypting VEEAM Passwords</a>. Veeam is used in many organizations for critical systems backup (i.e. VMware virtual machines like DCs) and so the built in credential manager is a great red team target.</li>
<li><a href="https://malwation.com/offensive-approach-to-online-sandboxes-1-any-run/" target="_blank">Offensive Approach to Online Sandboxes #1 – ANY.RUN &amp; Testing With MSP</a>. The ANY.RUN sandbox is an amazing tool for quickly getting a handle on what a process does, but it doesn't make much of an effort to hide itself. This post gives good detail on how you can detect being run in an ANY.RUN sandbox, as well as a trick to extend the time you can run up to nearly 2 hours.</li>
<li><a href="https://connormcgarr.github.io/swimming-in-the-kernel-pool-part-1/" target="_blank">Exploit Development: Swimming In The (Kernel) Pool - Leveraging Pool Vulnerabilities From Low-Integrity Exploits, Part 1</a>. Conor is an inspiration. Take the time to read his posts, even if it's to just motivate yourself to dig into hard problems - or to learn about the out-of-bounds read and kASLR bypass from low integrity, thats pretty cool too.</li>
<li><a href="https://adepts.of0x.cc/netsh-portproxy-code/" target="_blank">Don't use commands, use code: the tale of Netsh &amp; PortProxy</a>. This kind of exploration and development is what separates good red teams from groups of people who know how to use tools. It also helps bypass solutions that signature the "easy" way to do things.</li>
<li><a href="https://blog.christophetd.fr/phishing-for-aws-credentials-via-aws-sso-device-code-authentication/" target="_blank">Phishing for AWS credentials via AWS SSO device code authentication</a>. As more things move to the cloud, this type of phishing will not only become more common, but more impactful. In this case, an attacker can pre-generate an AWS SSO link and send that to a user. The attacker then has an hour after the user authenticates to do whatever/persist/escalate.</li>
<li><a href="https://dirkjanm.io/active-directory-forest-trusts-part-two-trust-transitivity/" target="_blank">Active Directory forest trusts part 2 - Trust transitivity and finding a trust bypass</a>. This post explores a way to exploit cross forest trusts by forging an entire domain, and includes some hidden gems along the way - like the use of Frida to patch in a different SID in lsass or the <a href="https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-lsat/b75eaac5-e4d1-4fc0-8dae-61d838b38701" target="_blank">LsarLookupNames3</a> trick to get the SID of remote machine's local domain.</li>
<li><a href="https://research.nccgroup.com/2021/06/14/incremental-machine-leaning-by-example-detecting-suspicious-activity-with-zeek-data-streams-river-and-ja3-hashes/" target="_blank">Incremental Machine Learning by Example: Detecting Suspicious Activity with Zeek Data Streams, River, and JA3 Hashes</a>. When I talked about "fancy AI/ML" in my <a href="https://youtu.be/TDg092qe50g" target="_blank">DEF CON talk</a> this is what I had in mind. Using Zeek and ML for anomaly detections, JA3 hash outliers can be used as a data point to warrant more investigation (or not).</li>
<li><a href="https://passthehashbrowns.github.io/hiding-your-syscalls" target="_blank">Hiding your syscalls</a>. In the cat and mouse game of hooking and direct syscalling, this is the next step (for the mouse). By reading a valid (unhooked) syscall instruction and then dynamically patching that address into stubs at runtime, this technique should bypass any static "uses-direct-syscalls" signatures. Code <a href="https://github.com/passthehashbrowns/hiding-your-syscalls" target="_blank">here</a>. A similar method is used in <a href="https://github.com/crummie5/FreshyCalls/blob/master/syscall.cpp#L42" target="_blank">FreshyCalls</a>. Your move AV.</li>
<li><a href="https://posts.specterops.io/proxy-windows-tooling-via-socks-c1af66daeef3" target="_blank">Proxy Windows Tooling via SOCKS</a>. What's the best way to keep from having a tool caught on target? Don't run it on target! This post goes over how to tunnel the most common windows tools using <a href="https://www.proxifier.com/" target="_blank">Proxifier</a>.</li>
<li><a href="https://github.blog/2021-06-10-privilege-escalation-polkit-root-on-linux-with-bug/" target="_blank">Privilege escalation with polkit: How to get root on Linux with a seven-year-old bug</a>. This old bug is only present in newer distributions because of how polkit was implemented in Debian and Debian forks (i.e. Ubuntu).</li>
<li><a href="https://vuls.cert.org/confluence/display/Wiki/Finding+Privilege+Escalation+Vulnerabilities+in+Windows+using+Process+Monitor" target="_blank">Finding Privilege Escalation Vulnerabilities in Windows using Process Monitor</a>. This method of finding privescs isn't "new" but that doesn't mean it isn't effective. Check out the filter <a href="https://github.com/CERTCC/privesc" target="_blank">here</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/mavillon1/CVE-2021-33739-POC" target="_blank">CVE-2021-33739-POC</a> is an exploit for the Microsoft DWM Core Library Elevation of Privilege Vulnerability (Windows 10 1909 to 20H2 and Server Core 2004/20H2). You'll probably want to swap the included <a href="https://github.com/mavillon1/CVE-2021-33739-POC/blob/main/CVE-2021-26868%20%26%20CVE-2021-33739/exp/exp.cpp#L274" target="_blank">shellcode</a> and test in a disposable VM!</li>
<li><a href="https://themittenmac.com/monitorui-tool-release/" target="_blank">MonitorUI</a> is a GUI for Objective-See's <a href="https://objective-see.com/products/utilities.html#ProcessMonitor" target="_blank">ProcessMonitor</a> tool for macOS.</li>
<li><a href="https://github.com/frkngksl/Celeborn" target="_blank">Celeborn</a> is a Userland API Unhooker developed for learning Windows APIs and Syscall implementations. It mainly detects and patches hooking instructions in NTDLL.dll file. Written in C, targeting Windows.</li>
<li><a href="https://github.com/FuzzySecurity/Sharp-Suite#melkor" target="_blank">Melkor</a> is able to read .Net assemblies and encrypt them in memory using DPAPI with the CRYPTPROTECT_LOCAL_MACHINE flag. These assemblies are kept encrypted when they are at rest. On demand Melkor can decrypt the assemblies and execute methods from them in a separate AppDomain. Once execution finishes the AppDomain is unloaded and only the encrypted assembly remains in memory.</li>
<li><a href="https://github.com/IlanKalendarov/SharpHook" target="_blank">SharpHook</a> is inspired by the <a href="https://github.com/passthehashbrowns/SharpRDPThief" target="_blank">SharpRDPThief</a> project. It uses various API hooks in order to output the desired credentials.</li>
<li><a href="https://github.com/Maff1t/WindowsPermsPoC" target="_blank">WindowsPermsPoC</a> is a simple PoC to demonstrate that is possible to write Non writable memory and execute Non executable memory on Windows. This is possible because of the way WriteProcessMemory works and the fact developers can disable DEP for their own programs. The end result is you can write and execute from READ_ONLY tagged memory. Only on windows...</li>
<li><a href="https://github.com/N4kedTurtle/SharpTeamsDump" target="_blank">SharpTeamsDump</a> is a .Net implementation of the research published <a href="https://infinitelogins.com/2021/06/06/your-microsoft-teams-chats-arent-as-private-as-you-think/" target="_blank">here</a>. Note that is extracts messages from a log file on disk, not by interacting with Teams itself.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/lkarlslund/adalanche" target="_blank">adalanche</a> is a bloodhound-like active directory explorer written in Go. While it cannot ingest standard sharphound data, it does have its own collection mechanism.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
