Title: Last Week in Security (LWiS) - 2022-08-30
Date: 2022-08-30 22:21
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-08-30
Author: Erik
Summary: AceLdr (<a href="https://twitter.com/kyleavery_" target="_blank">@kyleavery_</a>), DLL fun (<a href="https://twitter.com/Wietze" target="_blank">@Wietze</a> + <a href="https://twitter.com/ConsciousHacker" target="_blank">@ConsciousHacker</a>), CI/CD pwnage (<a href="https://twitter.com/smarticu5" target="_blank">@smarticu5</a>), Kerberos LPE (<a href="https://twitter.com/monoxgas" target="_blank">@monoxgas</a> + <a href="https://twitter.com/tiraniddo" target="_blank">@tiraniddo</a>), Burp ➡️ C2 profile (<a href="https://twitter.com/codex_tf2" target="_blank">@codex_tf2</a>), AD CS + PIV (<a href="https://twitter.com/_EthicalChaos_" target="_blank">@_EthicalChaos_</a>), and more!

<aside class="m-note m-warning">
<h3>Summer break++</h3>
<p>In addition to the summer break, I had some red teaming work take priority over this blog.
Sorry for the delay! This post will be links only as I dig back out of my 5,000+ unread blogs and tweets.</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-07-25 to 2022-08-30.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://access.redhat.com/security/cve/CVE-2022-2414" target="_blank">Unauth XXE (CVE-2022-2414) in FreeIPA</a> Check the image <a href="https://twitter.com/ptswarm/status/1559893047327997954/photo/1" target="_blank">here</a>.</li>
<li><a href="https://training.zeropointsecurity.co.uk/courses/red-team-ops-ii" target="_blank">Red Team Ops II</a> RTO II is a continuation (not a replacement) of Red Team Ops and aims to build on its foundation.  The primary focus of this course is to provide more advanced OPSEC tactics and defense bypass strategies.</li>
<li><a href="https://twitter.com/vxunderground/status/1562550443712352256" target="_blank">Leaked documents</a> show the purchase (and documentation of) an $8,000,000 iOS Remote Code Execution 0day access as a service... service.</li>
<li><a href="https://www.trendmicro.com/en_us/research/22/h/ransomware-actor-abuses-genshin-impact-anti-cheat-driver-to-kill-antivirus.html" target="_blank">Ransomware Actor Abuses Genshin Impact Anti-Cheat Driver to Kill Antivirus</a></li>
<li><a href="https://www.cobaltstrike.com/blog/cobalt-strike-4-7-the-10th-anniversary-edition/" target="_blank">Cobalt Strike 4.7: The 10th Anniversary Edition</a>. Seeing some issues with UDRLs that were working on 4.6, be sure to test before you update prod!</li>
<li><a href="https://www.modzero.com/modlog/archives/2022/08/22/ridiculous_vulnerability_disclosure_process_with_crowdstrike_falcon_sensor/index.html" target="_blank">Ridiculous vulnerability disclosure process with CrowdStrike Falcon Sensor</a></li>
<li><a href="https://dazzyddos.github.io/posts/Offensive-Lateral-Movement/" target="_blank">Offensive Lateral Movement Workshop</a> - Free and online in September.</li>
<li><a href="https://www.vice.com/en/article/qjkvxv/how-a-third-party-sms-service-was-used-to-take-over-signal-accounts" target="_blank">How a Third-Party SMS Service Was Used to Take Over Signal Accounts</a>. TLDR: Set up a Signal PIN if you don't have one yet!</li>
<li><a href="https://security.googleblog.com/2023/08/Announcing-Googles-Open-Source-Software-Vulnerability-Rewards-Program%20.html" target="_blank">Announcing Google's Open Source Software Vulnerability Rewards Program</a></li>
<li><a href="https://www.washingtonpost.com/technology/interactive/2022/twitter-whistleblower-sec-spam/" target="_blank">Former security chief claims Twitter buried 'egregious deficiencies'</a>. Getting hired to report security issues and being ignored? Mudge could be a red team consultant.</li>
<li><a href="https://srcincite.io/blog/2022/08/11/i-am-whoever-i-say-i-am-infiltrating-vmware-workspace-one-access-using-a-0-click-exploit.html" target="_blank">IAM Whoever I Say IAM :: Infiltrating VMWare Workspace ONE Access Using a 0-Click Exploit</a></li>
<li><a href="https://posts.specterops.io/introducing-bloodhound-4-2-the-azure-refactor-1cff734938bd" target="_blank">Introducing BloodHound 4.2 — The Azure Refactor</a></li>
<li><a href="https://youtu.be/5nKk_-Lvhzo" target="_blank">SANS ICS HyperEncabulator</a>. Not as good as the <a href="https://youtu.be/RXJKdh1KZ0w" target="_blank">Rockwell iteration</a>, but pretty solid.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://swarm.ptsecurity.com/discovering-domains-via-a-time-correlation-attack/" target="_blank">Discovering Domains via a Time-Correlation Attack on Certificate Transparency</a></li>
<li><a href="https://research.nccgroup.com/2022/01/13/10-real-world-stories-of-how-weve-compromised-ci-cd-pipelines/" target="_blank">10 real-world stories of how we've compromised CI/CD pipelines</a></li>
<li><a href="https://i.blackhat.com/USA-22/Wednesday/US-22-Forshaw-Taking-Kerberos-To-The-Next-Level.pdf" target="_blank">[PDF] Taking Kerberos To The Next Level</a></li>
<li><a href="https://www.akamai.com/blog/security/authentication-coercion-windows-server-service" target="_blank">CVE-2022-30216 - Authentication coercion of the Windows “Server” service</a>. The latest coercion technique for Windows.</li>
<li><a href="https://jsecurity101.medium.com/wmi-internals-part-2-522f3e97709a" target="_blank">WMI Internals Part 2 - Reversing a WMI Provider</a></li>
<li><a href="https://www.accidentalrebel.com/malware-sandbox-evasion-in-x64-assembly-by-checking-ram-size-part-2.html" target="_blank">Malware sandbox evasion in x64 assembly by checking ram size - Part 2</a></li>
<li><a href="https://ezrabuckingham.com/blog/containerizing-red-team-infra/" target="_blank">DevAttackOps: Containerizing Red Team Infrastructure (Part 1)</a> and <a href="https://ezrabuckingham.com/blog/containers-ci_cd/" target="_blank">DevAttackOps: Container CI/CD Pipelines (Part 2)</a></li>
<li><a href="https://z4ksec.github.io/posts/masky-release-v0.0.3/" target="_blank">Masky release (v0.0.3)</a> - Masky is a python library providing an alternative way to remotely dump domain users' credentials thanks to an ADCS. A command line tool has been built on top of this library in order to easily harvest PFX, NT hashes and TGT on a larger scope.</li>
<li><a href="https://www.pentestpartners.com/security-blog/living-off-the-land-ad-cs-style/" target="_blank">Living off the land, AD CS style</a>. This post introduces the <a href="https://github.com/CCob/PIVert" target="_blank">PIVert</a> tool to abuse AD CS.</li>
<li><a href="https://northwave-security.com/harvesting-active-directory-credentials-via-http-request-smuggling/" target="_blank">Harvesting Active Directory credentials via HTTP Request Smuggling</a></li>
<li><a href="https://pre.empt.dev/posts/maelstrom-static-review/" target="_blank">Maelstrom: Static OpSec Review</a>. This series continues to be superb.</li>
<li><a href="https://palant.info/2022/08/10/anatomy-of-a-basic-extension/" target="_blank">Anatomy of a basic extension</a>. As the world moves to SaaS, the browser becomes the OS, and malware will be written as extensions.</li>
<li><a href="https://www.wiz.io/blog/the-cloud-has-an-isolation-problem-postgresql-vulnerabilities" target="_blank">The cloud has an isolation problem: PostgreSQL vulnerabilities affect multiple cloud vendors</a>. How Wiz Research uncovered multiple related vulnerabilities in PostgreSQL-as-a-Service offerings from GCP, Azure, and others.</li>
<li><a href="https://labs.jumpsec.com/abusing-shareduserdata-for-defense-evasion-and-exploitation-2/" target="_blank">Abusing SharedUserData For Defense Evasion and Exploitation</a></li>
<li><a href="https://modexp.wordpress.com/2022/08/22/base_n_compression/" target="_blank">Shellcode: Base-N Decoding for Text-Only Compression and Obfuscation</a></li>
<li><a href="https://blog.orange.tw/2022/08/lets-dance-in-the-cache-destabilizing-hash-table-on-microsoft-iis.html" target="_blank">Let's Dance in the Cache - Destabilizing Hash Table on Microsoft IIS!</a>. When Orange writes, you should read.</li>
<li><a href="https://blog.ret2.io/2022/08/17/macos-dblmap-kernel-exploitation/" target="_blank">The LDT, a Perfect Home for All Your Kernel Payloads</a>. Using the HIB segment to bypass KASLR on x86-based macOS.</li>
<li><a href="https://shells.systems/post-bypassing-applocker-by-abusing-hashinfo/" target="_blank">Bypassing AppLocker by abusing HashInfo</a></li>
<li><a href="https://www.x86matthew.com/view_post?id=clipboard_inject" target="_blank">ClipboardInject - Abusing the clipboard to inject code into remote processes</a></li>
<li><a href="https://icebreaker.team/blogs/sleeping-with-control-flow-guard/" target="_blank">Sleeping With Control Flow Guard</a></li>
<li><a href="https://www.ambionics.io/blog/hacking-watchguard-firewalls" target="_blank">Blind exploits to rule WatchGuard firewalls</a>. This is one of the craziest exploit development writeups I've read in a while. Impressive ability to keep going in the face of adversity.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/rad9800/TamperingSyscalls" target="_blank">TamperingSyscalls</a> is a 2 part novel project consisting of argument spoofing and syscall retrieval which both abuse EH in order to subvert EDRs. This project consists of both of these projects in order to provide an alternative solution to direct syscalls.</li>
<li><a href="https://gitlab.com/ORCA000/entropyfix" target="_blank">EntropyFix</a> is a tool with no ascii art that reduces the entropy of your payload.</li>
<li><a href="https://github.com/zeronetworks/BlueHound" target="_blank">BlueHound</a> is an open-source tool that helps blue teams pinpoint the security issues that actually matter. By combining information about user permissions, network access and unpatched vulnerabilities, BlueHound reveals the paths attackers would take if they were inside your network.</li>
<li><a href="https://github.com/kyleavery/AceLdr" target="_blank">AceLdr</a> Cobalt Strike UDRL for memory scanner evasion. [This is the best UDRL yet.]</li>
<li><a href="https://hijacklibs.net/" target="_blank">Hijack Libs</a> - The database contains 341 Sideloading, 88 Environment Variable, 8 Phantom and 5 Search Order entries.</li>
<li><a href="https://github.com/CodeXTF2/Burp2Malleable" target="_blank">Burp2Malleable</a> Quick python utility I wrote to turn HTTP requests from burp suite into Cobalt Strike Malleable C2 profiles.</li>
<li><a href="https://github.com/iilegacyyii/ExportDumper" target="_blank">ExportDumper</a> A small tool to dump the export table of PE files. The primary use case was intended for use within DLL proxying.</li>
<li><a href="https://github.com/ConsciousHacker/WFH" target="_blank">WFH</a> - Windows Feature Hunter (WFH) is a proof of concept python script that uses Frida, a dynamic instrumentation toolkit, to assist in potentially identifying common “vulnerabilities” or “features” within Windows executables. WFH currently has the capability to automatically identify potential Dynamic Linked Library (DLL) sideloading and Component Object Model (COM) hijacking opportunities at scale.</li>
<li><a href="https://github.com/evilsocket/jscythe" target="_blank">jscythe</a> - Abuse the node.js inspector mechanism in order to force any node.js/electron/v8 based process to execute arbitrary javascript code.</li>
<li><a href="https://github.com/markakd/dirtycred" target="_blank">DirtyCred</a> is a kernel exploitation concept that swaps unprivileged kernel credentials with privileged ones to escalate privilege. Instead of overwriting any critical data fields on kernel heap, DirtyCred abuses the heap memory reuse mechanism to get privileged.</li>
<li><a href="https://github.com/layer8secure/SilentHound" target="_blank">SilentHound</a> - Quietly enumerate an Active Directory Domain via LDAP parsing users, admins, groups, etc.</li>
<li><a href="https://github.com/nccgroup/jwt-reauth" target="_blank">jwt-reauth</a> is a Burp plugin to cache authentication tokens from an "auth" URL, and then add them as headers on all requests going to a certain scope.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://gist.github.com/gladiatx0r/1ffe59031d42c08603a3bde0ff678feb" target="_blank">From RPC to RCE - Workstation Takeover via RBCD and MS-RPChoose-Your-Own-Adventure</a> - You'll also want <a href="https://github.com/Hackndo/WebclientServiceScanner" target="_blank">WebclientServiceScanner</a>.</li>
<li><a href="https://defaultinator.com/" target="_blank">Defaultinator</a> is a data repository for storing and querying default passwords for common devices and applications.</li>
<li><a href="https://github.com/hakluke/hakscale" target="_blank">hakscale</a> - Distribute ordinary bash commands over many systems.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 420 (+1)</p>
<p>Blogs monitored: 320 (+3)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
