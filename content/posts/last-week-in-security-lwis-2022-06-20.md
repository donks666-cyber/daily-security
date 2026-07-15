Title: Last Week in Security (LWiS) - 2022-06-20
Date: 2022-06-20 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-06-20
Author: Erik
Summary: ASP .NET audit (<a href="https://twitter.com/frycos" target="_blank">@frycos</a>), iOS ROP ⛓️ (<a href="https://twitter.com/inversecos" target="_blank">@inversecos</a>), EnumDisplayMonitors to run 🐚code (<a href="https://twitter.com/marco_ramilli" target="_blank">@Marco_Ramilli</a>), pcap for problem solving (<a href="https://twitter.com/DebugPrivilege" target="_blank">@DebugPrivilege</a>), RPC vuln (<a href="https://twitter.com/s1ckb017" target="_blank">@s1ckb017</a>), 🎣 for persistence (<a href="https://twitter.com/matterpreter" target="_blank">@matterpreter</a>), Azure attack paths (<a href="https://twitter.com/ZephrFish/" target="_blank">@ZephrFish</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-06-14 to 2022-06-20.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://support.citrix.com/article/CTX460016/citrix-application-delivery-management-security-bulletin-for-cve202227511-and-cve202227512" target="_blank">Citrix Application Delivery Management Security Bulletin for CVE-2022-27511 and CVE-2022-27512</a>. Remote unauthenticated users can reset the administrator password of the device at next reboot and SSH in.</li>
<li><a href="https://krebsonsecurity.com/2022/06/microsoft-patch-tuesday-june-2022-edition/" target="_blank">Microsoft Patch Tuesday, June 2022 Edition</a>. The best news? IE is officially out of service after 27 years. Follina (MSDT 0day) also got a patch.</li>
<li><a href="https://gizmodo.com/bluetooth-tracking-iphone-airtags-1849042375" target="_blank">New Research Suggests Always-On Bluetooth Could Be Used to Track Your Phone</a>. Does your phone's Bluetooth chip have a "fingerprint?" Probably.</li>
<li><a href="https://www.technologyreview.com/2022/06/18/1054452/china-censors-social-media-comments" target="_blank">Now China wants to censor online comments</a>. Consider this when your local politicians argue that all communication needs a backdoor to "protect the children."</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://frycos.github.io/vulns4free/2022/06/17/yet-another-rpc-framework.html" target="_blank">SmarterStats - Yet Another RPC Framework</a>. This is an in-depth code audit of an ASP .NET web long analytics app.</li>
<li><a href="https://www.inversecos.com/2022/06/guide-to-reversing-and-exploiting-ios.html" target="_blank">Guide to Reversing and Exploiting iOS binaries Part 2: ARM64 ROP Chains</a>. Some more binary exploitation on iOS. Be sure to bring a jailbroken iOS device to follow along.</li>
<li><a href="https://marcoramilli.com/2022/06/15/running-shellcode-through-windows-callbacks/" target="_blank">Running Shellcode Through Windows Callbacks</a>. Unique shellcode execution techniques can help your loader stay under the radar. Check out the <a href="https://github.com/aahmad097/AlternativeShellcodeExec" target="_blank">AlternativeShellcodeExec</a> for more.</li>
<li><a href="https://m365internals.com/2022/06/19/how-do-i-approach-a-technical-topic-packet-capture-part-1/" target="_blank">How do I approach a technical topic? - Packet Capture (Part 1)</a>. I really like these types of posts that explore the methodology of solving problems.</li>
<li><a href="https://research.nccgroup.com/2022/06/16/updated-technical-advisory-and-proofs-of-concept-multiple-vulnerabilities-in-u-boot-cve-2022-30790-cve-2022-30552/" target="_blank">Updated: Technical Advisory and Proofs of Concept - Multiple Vulnerabilities in U-Boot (CVE-2022-30790, CVE-2022-30552)</a>. The U-boot advisory from 2022-06-03 gets updated and expanded.</li>
<li><a href="https://offensivedefence.co.uk/posts/ntlm-auth-firefox/" target="_blank">NTLM Authentication with Firefox &amp; FoxyProxy</a>. This post shows how to authenticate to a web page over a SOCKS connection with NTLM.</li>
<li><a href="https://s1ckb017.github.io/2022/06/17/CVE-2022-26809-Server-Side-vulnerable-point-reachability.html" target="_blank">CVE-2022-26809 Reaching Vulnerable Point starting from 0 Knowledge on RPC</a>. A great zero to PoC post, but note this particular exploit requires sending 1,048,577 packets.</li>
<li><a href="https://blog.redxorblue.com/2022/06/automating-cobalt-strike-with-python.html" target="_blank">Automating Cobalt Strike with Python</a>. The sleep language used to script Cobalt Strike is, unique, to say the least. Using something more widely known like Python helps more operators script the routine parts and focus on making assessments valuable for customers.</li>
<li><a href="https://shells.systems/oh-my-api-abusing-tyk-cloud-api-management-service-to-hide-your-malicious-c2-traffic/" target="_blank">Oh my API, abusing TYK cloud API management to hide your malicious C2 traffic</a>. As everything moves to the cloud, hiding C2 traffic alongside legitimate API endpoints will be key to staying out of SOC alerts.</li>
<li><a href="https://posts.specterops.io/hang-fire-challenging-our-mental-model-of-initial-access-513c71878767" target="_blank">Hang Fire: Challenging our Mental Model of Initial Access</a>. The term "phishing for persistence" ia a good one. Breaking the link between phish and execution makes it harder to detect.</li>
<li><a href="https://www.varonis.com/blog/rogue-shortcuts-lnking-to-badness" target="_blank">Rogue Shortcuts: LNK'ing to Badness</a>. LNKs in zips or ISOs still prove to be an effective delivery mechanism.</li>
<li><a href="https://blog.zsec.uk/azure-fundamentals-pt1/" target="_blank">Azure Attack Paths: Common Findings and Fixes (Part 1)</a>. Cloud assessments are becoming more common, and this post goes over some basics of Azure attack paths.</li>
<li><a href="https://spaceraccoon.dev/embedding-payloads-bypassing-controls-microsoft-infopath/" target="_blank">Embedding Payloads and Bypassing Controls in Microsoft InfoPath</a>. Legacy Microsoft file types and handlers (in this case <cite>.xsn</cite> files) continue to be interesting payload delivery mechanisms.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Wh04m1001/DFSCoerce" target="_blank">DFSCoerce</a> - PoC for MS-DFSNM coerce authentication using NetrDfsRemoveStdRoot method. This can be used when the Spooler service is disable, and RPC filters prevent PetitPotam/File Server VSS authentication elicitation.</li>
<li><a href="https://github.com/omair2084/CVE-2022-26937" target="_blank">CVE-2022-26937</a> - Windows Network File System crash PoC.</li>
<li><a href="https://github.com/fcccode/hunter-1" target="_blank">hunter-1</a> (l)user hunter using WinAPI calls only.</li>
<li><a href="https://github.com/wiz-sec/cloud-middleware-dataset" target="_blank">cloud-middleware-dataset</a>. This project contains cloud middleware (i.e. agents installed by cloud security providers) used across the major cloud service providers (Azure, AWS and GCP).</li>
<li><a href="https://github.com/Cracked5pider/Ekko" target="_blank">Ekko</a>. A small sleep obfuscation technique that uses CreateTimerQueueTimer to queue up the ROP chain that performs Sleep obfuscation. Detection: <a href="https://github.com/joe-desimone/patriot" target="_blank">patriot</a>.</li>
<li><a href="https://github.com/NtQuerySystemInformation/NlsCodeInjectionThroughRegistry" target="_blank">NlsCodeInjectionThroughRegistry</a> Dll injection through code page id modification in registry. Based on jonas lykk research.</li>
<li><a href="https://gist.github.com/rad9800/ccfbf5f085aff2218699d92d354fe91e" target="_blank">Using macros and constexpr to make API hashing a bit more friendly</a>.</li>
<li><a href="https://github.com/dobin/antnium" target="_blank">antnium</a> - A C2 framework and RAT written in Go. Slides about the development process <a href="https://docs.google.com/presentation/d/1UZmFo_TvSS2TvPJKlDjIW1kTVjYGGaYO86Buh2UgbaI/mobilepresent#slide=id.g11cdb36f978_1_129" target="_blank">here</a>.</li>
<li><a href="https://github.com/garrettfoster13/aced" target="_blank">aced</a> is a tool to parse and resolve a single targeted Active Directory principal's DACL. Aced will identify interesting inbound access allowed privileges against the targeted account, resolve the SIDS of the inbound permissions, and present that data to the operator.</li>
<li><a href="https://github.com/trustedsec/SliverKeylogger" target="_blank">SliverKeylogger</a> is a Sliver C2 extension to log keystrokes on Windows.</li>
<li><a href="https://github.com/EvotecIT/OfficeIMO" target="_blank">OfficeIMO</a> Fast and easy to use cross-platform .NET library that creates or modifies Microsoft Word and later also Excel files without installing any software. This could be useful to automate phishing lures.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/aahmad097/AlternativeShellcodeExec" target="_blank">AlternativeShellcodeExec</a> - Alternative Shellcode Execution Via Callbacks.</li>
<li><a href="https://github.com/pathtofile/Sealighter" target="_blank">Sealighter</a> - Sysmon-Like research tool for ETW.</li>
<li><a href="https://github.com/firefart/npmdomainchecker" target="_blank">npmdomainchecker</a> - Checks all maintainers of all NPM packages for hijackable domains.</li>
<li><a href="https://github.com/DanusMinimus/snallybuckster" target="_blank">snallybuckster</a> - Locate interesting files in grayhatwarfare.com open S3 buckets and Azure blobs automatically!</li>
<li><a href="https://github.com/trainr3kt/NoteThief" target="_blank">NoteThief</a> - Grab unsaved Notepad contents with a Beacon Object File.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 417 (+1)</p>
<p>Blogs monitored: 312 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
