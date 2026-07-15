Title: Last Week in Security (LWiS) - 2020-08-17
Date: 2020-08-17 23:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-08-17
Author: Erik
Summary: Azure AD to on-prem lateral movement by <a href="https://twitter.com/_wald0" target="_blank">@_wald0</a>, a new Windows un-hooking project from <a href="https://twitter.com/peterwintrsmith" target="_blank">@peterwintrsmith</a>, 🔥 Russian Linux malware analysis from <a href="https://twitter.com/NSACyber" target="_blank">@NSACyber</a>, modern AV evasion primer from <a href="https://twitter.com/_batsec_" target="_blank">@_batsec_</a>, dumping LSASS from the kernel by <a href="https://twitter.com/zerosum0x0" target="_blank">@zerosum0x0</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-08-10 to 2020-08-17.</p>
<aside class="m-note m-warning">
<h3>Risky Business</h3>
<p>If you aren't a regular listener of the Risky Business podcast, I highly recommend it. It is my only "must listen" podcast each week because it's so information dense. Check out my short appearance on <a href="https://risky.biz/RB594/" target="_blank">Risky Business #594 -- How ESNIs will change censorship and NDR</a>.</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://securelist.com/ie-and-windows-zero-day-operation-powerfall/97976/" target="_blank">Internet Explorer and Windows zero-day exploits used in Operation PowerFall</a>. Two 0days were used in this campaign that targeted a South Korean company, a user-after-free in IE 11 on Windows 10, and an elevation of privilege related to kernel memory handling. Even if you are on Windows 10, Internet Explorer is a bad idea.</li>
<li><a href="https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF" target="_blank">Russian GRU 85th GTsSSDeploys PreviouslyUndisclosed Drovorub Malware</a>. The NSA and FBI tear down Russian Linux malware and dig into all the details in this 39 page (!) report. They specifics on the server configuration shows that they had access to live C2 nodes. This tactic of naming and shaming nationstate malware started with the US CYBERCOM twitter, and its good to see it carry over into well researched reports.</li>
<li><a href="https://www.offensive-security.com/offsec/retiring-ctp-intro-new-courses/" target="_blank">New Developments: Retiring CTP and Introducing New Courses</a>. CTP/OSCE are soon to be retired and replaced with three separate courses that must be complete to earn a "new OSCE." While I agree that OSCE is out of date, it does introduce good content, and I'm sure students will not be excited to have to pay for 3 courses to earn a certificate that used to be one. However, Offensive Security provides the best reasonably priced, hands on, recognized certificates out there (besides rastamouse's <a href="https://www.zeropointsecurity.co.uk/red-team-ops" target="_blank">Red Team Ops</a>).</li>
<li><a href="https://revolte-attack.net/" target="_blank">Call Me Maybe: Ea­ves­drop­ping En­cryp­ted LTE Calls With Re­VoL­TE</a>. Another instance of the RFC not matching implementation. Base station (eNodeB) implementations of VoLTE reuse keystreams for concurrent calls, allowing a malicious actor to capture a call, place another, and use the keystream from the second to decrypt the first. Demo <a href="https://youtu.be/FiiELuFvwu0" target="_blank">here</a>.</li>
<li><a href="https://krebsonsecurity.com/2020/08/microsoft-put-off-fixing-zero-day-for-2-years/" target="_blank">Microsoft Put Off Fixing Zero Day for 2 Years</a>. Brian Krebs digs into <a href="https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1464" target="_blank">CVE-2020-1464</a>, an issue with how Windows validates file signatures commonly used to execute jar based attacks. Triage is hard, but this seems like an issue that should have been fixed much faster.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://blog.dylan.codes/defending-your-malware/" target="_blank">Defending Your Malware</a> is a post by the author of <a href="https://github.com/bats3c/shad0w" target="_blank">shad0w</a> that serves as a great primer on modern Windows antivirus/EDR evasion techniques.</li>
<li><a href="https://www.mnemonic.no/blog/introducing-snicat" target="_blank">SNIcat: Circumventing the guardians</a>. Given my <a href="https://youtu.be/TDg092qe50g" target="_blank">interest in SNI</a>, this post was interesting. They use the SNI and then subsequent return or non-return of the server certificate to send data to a server, even if the domain has been blocked by an intercepting firewall. Interesting technique, but also extremely loud. Code <a href="https://github.com/mnemonic-no/SNIcat" target="_blank">here</a>.</li>
<li><a href="https://zerosum0x0.blogspot.com/2020/08/sassykitdi-kernel-mode-tcp-sockets.html" target="_blank">SassyKitdi: Kernel Mode TCP Sockets + LSASS Dump</a>. This post describes a kernel mode payload for Windows NT called "SassyKitdi" (LSASS + Rootkit + TDI). This payload is of a nature that can be deployed via remote kernel exploits such as EternalBlue, BlueKeep, and SMBGhost, as well as from local kernel exploits, i.e. bad drivers. This exploit payload is universal from (at least) Windows 2000 to Windows 10, and without having to carry around weird DKOM offsets. A cool project that attacks LSASS dumping from a lower level.</li>
<li><a href="https://secret.club/2020/08/14/macos-entitlements.html" target="_blank">Abusing MacOS Entitlements for code execution</a>. This post shows interesting ways of persisting (or potentially gaining initial access) on macOS by abusing "weak" entitlements.</li>
<li><a href="https://posts.specterops.io/death-from-above-lateral-movement-from-azure-to-on-prem-ad-d18cb3959d4d" target="_blank">Death from Above: Lateral Movement from Azure to On-Prem AD</a>. This is very cool research from <a href="https://twitter.com/_wald0" target="_blank">@_wald0</a> on how to use Azure AD to execute code as SYSTEM on any endpoint managed by ConfigMgr/Intune/Endpoint Manager. The cloud is a scary place.</li>
<li><a href="https://www.mdsec.co.uk/2020/08/firewalker-a-new-approach-to-generically-bypass-user-space-edr-hooking/" target="_blank">FireWalker: A New Approach to Generically Bypass User-Space EDR Hooking</a>. The EDR hooking arms race started by <a href="https://github.com/outflanknl/Dumpert" target="_blank">Dumpert</a> gets a new weapon with the release of <a href="https://github.com/mdsecactivebreach/firewalker" target="_blank">firewalker</a>.</li>
<li><a href="https://voidsec.com/cve-2020-1337-printdemon-is-dead-long-live-printdemon/" target="_blank">CVE-2020-1337 – PrintDemon is dead, long live PrintDemon!</a>. Another good example of a patch not killing a bug. This is a bypass for CVE-2020-1048, and for the good work gets the best CVE number of the year. PoC <a href="https://github.com/sailay1996/cve-2020-1337-poc" target="_blank">here</a> and <a href="https://github.com/math1as/CVE-2020-1337-exploit" target="_blank">here</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/chrismarget/eidc32proxy" target="_blank">eidc32proxy</a>. Is a pure Go proxy for eidc32 proximity systems. It allows for "skeleton key" credentials to operate locks without logging to the controler. Check out the demo <a href="https://www.youtube.com/watch?v=ghiHXK4GEzE&amp;t=6335" target="_blank">here</a>.</li>
<li><a href="https://github.com/trailofbits/sinter" target="_blank">sinter</a> is a 100% user-mode endpoint security agent for macOS 10.15 and above, written in Swift. This is inspired by Google's Santa but doesn't require a kernel extension (which is not allowed in macOS 11) and has more features.</li>
<li><a href="https://github.com/checkymander/Zolom" target="_blank">Zolom</a> is a C# executable with embedded Python that can be used reflectively to run python code on systems without Python installed. Yo dawg, I heard you like high level languages <a href="https://knowyourmeme.com/memes/xzibit-yo-dawg" target="_blank">...</a></li>
<li><a href="https://github.com/PwnDexter/SharpEDRChecker" target="_blank">SharpEDRChecker</a> checks running processes, process metadata, DLLs loaded into your current process and the each DLLs metadata, common install directories, installed services and each service binaries metadata, installed drivers and each drivers metadata, all for the presence of known defensive products such as AV's, EDR's and logging tools.</li>
<li><a href="https://posts.specterops.io/a-change-of-mythic-proportions-21debeb03617" target="_blank">A Change of Mythic Proportions</a>. Apfell C2 is now Mythic C2 which better reflects how adaptable it is. This update is a big one, so if you have checked out Apfell in the past, be sure to take another look.</li>
<li><a href="https://github.com/klinix5/Windows-Setup-EoP" target="_blank">Windows-Setup-EoP</a>. This is an exploit for a time of check/time of use vulnerability in the windows "feature update" (i.e. 1909 to 2004) process. Demo <a href="https://www.youtube.com/watch?v=rRxfZQ0jPLA" target="_blank">here</a>.</li>
<li><dl>
<dt>VMProtect Tools</dt>
<dd><ul>
<li><a href="https://github.com/0xnobody/vmpattack" target="_blank">vmpattack</a> is a VMProtect to Virtual-machine Translation Intermediate Language (VTIL) lifter. This can help get VMProtected binaries into a state that will help with analysis.</li>
<li><a href="https://github.com/can1357/NoVmp" target="_blank">NoVmp</a> is a project devirtualizing VMProtect x64 3.0 - 3.5 (latest) into optimized VTIL and optionally recompiling back to x64 using the VTIL library.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/blunderbuss-wctf/wacker" target="_blank">wacker</a> is the first (I think?) tool for WPA3 dictionary attacks!</li>
<li><a href="https://posts.specterops.io/cve-2020-14979-local-privilege-escalation-in-evga-precisionx1-cf63c6b95896" target="_blank">CVE-2020–14979: Local Privilege Escalation in EVGA Precision X1</a>. Poorly written drivers are the gift that keep on giving. In this case, local privilege escalation is the gift. This driver is included in <a href="https://github.com/eclypsium/Screwed-Drivers" target="_blank">Screwed-Drivers</a>.</li>
<li><a href="https://github.com/magisterquis/dnsfserv" target="_blank">dnsfserv</a> is a fileserver over DNS, with wrapper library and example stager. You never know when you might be in a super restricted env and need to stage over DNS.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
