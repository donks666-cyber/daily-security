Title: Last Week in Security (LWiS) - 2020-10-19
Date: 2020-10-19 23:40
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-10-19
Author: Erik
Summary: Ryzen Driver LPE by <a href="https://twitter.com/h0mbre_" target="_blank">@h0mbre_</a>, Discord desktop RCE by <a href="https://twitter.com/kinugawamasato" target="_blank">@kinugawamasato</a>, Azure Pipeline abuse by <a href="https://twitter.com/Flangvik" target="_blank">@Flangvik</a>, macOS TCC tricks by <a href="https://twitter.com/_xpn_" target="_blank">@_xpn_</a>, AWS enumeration bug by <a href="https://twitter.com/frichette_n" target="_blank">@Frichette_n</a>, new loader from <a href="https://twitter.com/Cribdragg3r" target="_blank">@Cribdragg3r</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-10-12 to 2020-10-19.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://krebsonsecurity.com/2020/10/microsoft-uses-copyright-law-to-disrupt-trickbot-botnet/" target="_blank">Microsoft Uses Trademark Law to Disrupt Trickbot Botnet</a>. Just days after Trickbot was disrupted by USCYBERCOM (allegedly), Microsoft uses a unique legal trick to shut down additional C2 infrastructure by forcing hosting providers and telecom companies to block access to the C2 infrastructure.</li>
<li><a href="https://portswigger.net/daily-swig/german-police-raid-tech-firm-finfisher-over-spyware-allegations" target="_blank">German police raid tech firm FinFisher over spyware allegations</a>. FinFisher is accused of selling surveillance software, to oppressive regimes around the world (Turkey, Ethiopia, Bahrain, the UAE, and Egypt). FinFisher was <a href="https://www.vice.com/en/article/z4mzze/a-hacker-claims-to-have-leaked-40gb-of-docs-on-government-spy-tool-finfisher" target="_blank">spectacularly breached</a> back in 2014 when it was owned by UK based Gamma Group (<a href="https://pastebin.com/raw/cRYvK4jb" target="_blank">writeup</a>).</li>
<li><a href="https://www.securify.nl/advisory/java-deserialization-vulnerability-in-qradar-remotejavascript-servlet" target="_blank">Java deserialization vulnerability in QRadar RemoteJavaScript Servlet</a>. Nothing quite as face-palm-able as having RCE in your security product. The RCE is authenticated, but still not a good look.</li>
<li><a href="https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16898" target="_blank">CVE-2020-16898 Windows TCP/IP Remote Code Execution Vulnerability</a>. Patch Tuesday reveals a critical unauthenticated potential RCE in the Windows TCP/IP stack when it handles ICMPv6 Router Advertisement packets. While this is bad, the protections in tcpip.sys will make a RCE PoC difficult. Patch or apply the workaround regardless. More details <a href="http://blog.pi3.com.pl/?p=780" target="_blank">here</a>.</li>
<li><a href="https://www.justice.gov/opa/pr/international-statement-end-end-encryption-and-public-safety" target="_blank">International Statement: End-To-End Encryption and Public Safety</a>. Five Eyes (FVEY) intel alliance countries of Australia, Canada, New Zealand, the UK, and US were joined by India and Japan in calling for tech firms to “enable law enforcement access to content” upon production of a warrant, in the name of public safety. This same strategy was <a href="https://en.wikipedia.org/wiki/Crypto_Wars#PC_era" target="_blank">attempted in the 90s</a>. However, end-to-end encryption is easy to implement now, and mathematics/cryptography cannot be banned. If implemented, bad actors will continue to use end-to-end encryption while citizen's privacy is destroyed.</li>
<li><a href="https://www.tripwire.com/state-of-security/vert/sonicwall-vpn-portal-critical-flaw-cve-2020-5135/" target="_blank">SonicWall VPN Portal Critical Flaw (CVE-2020-5135)</a>. Nearly 800,000 SonicWall VPNs are vulnerable to new remote code execution bug. The bug is in the SSLVPN, which is exposed to the internet as part of its functionality. Tripwire VERT says that a "code execution exploit is likely feasible."</li>
<li><a href="https://blog.t8012.dev/plug-n-pwn/" target="_blank">Plug'nPwn - Connect to Jailbreak</a>. The recent T2 security chip jailbreak has been productized and is now as easy as connecting a special cable/device to an Apple laptop. I expect this to be productize further into a full tool with additional features like a keylogger. Demo <a href="https://youtu.be/LRoTr0HQP1U" target="_blank">here</a>.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://dtm.uk/wuauclt/" target="_blank">Code execution via the Windows Update client (wuauclt)</a>. The UpdateDeploymentProvider option to wuaclt.exe allows for code execution via a DLL. This is likely a AppLocker bypass, and has been <a href="https://www.joesandbox.com/analysis/215088/0/html" target="_blank">seen in the wild (Startup)</a>.</li>
<li><a href="https://h0mbre.github.io/RyzenMaster_CVE/#" target="_blank">CVE-2020-12928 Exploit Proof-of-Concept, Privilege Escalation in AMD Ryzen Master AMDRyzenMasterDriver.sys</a>. Another vulnerable driver, another LPE. This post does a great job of walking through the discovery process and supplies a PoC.</li>
<li><a href="https://research.nccgroup.com/2020/10/15/theres-a-hole-in-your-soc-glitching-the-mediatek-bootrom/">There’s A Hole In Your SoC: Glitching The MediaTek BootROM</a>. Glitching physical devices is an area of research that is gaining more traction (covered in <a href="https://blog.badsectorlabs.com/last-week-in-security-lwis-2020-08-31.html">LWiS 2020-08-31</a> and <a href="https://blog.badsectorlabs.com/last-week-in-security-lwis-2020-09-28.html">LWiS 2020-09-28</a>). As software protections become more effective, look for hardware based attacks to become more popular.</li>
<li><a href="https://medium.com/red-teaming-with-a-blue-team-mentaility/a-look-at-python-less-office-macros-for-macos-b1bf5c1488f1" target="_blank">Running JXA Payloads from macOS Office Macros</a>. While nothing groundbreaking, the move away from python for macOS macro attacks will likely bypass some specific detections. Note that this technique still lands you in the sandbox.</li>
<li><a href="https://labs.sentinelone.com/leveraging-ld_audit-to-beat-the-traditional-linux-library-preloading-technique/" target="_blank">Leveraging LD_AUDIT to Beat the Traditional Linux Library Preloading Technique</a>. While most red teamers know about LD_PRELOAD to run code in the context of processes or intercept functions on Linux, LD_AUDIT will actually run before LD_PRELOAD which gives defenders a change to disable preloading, and red teamers the ability to use a lesser known technique with the same functionality. <a href="https://github.com/ForensicITGuy/libpreloadvaccine" target="_blank">libpreloadvaccine</a> is a projects for defenders that uses this technique.</li>
<li><a href="https://medium.com/bugbountywriteup/recipe-for-a-successful-phishing-campaign-part-1-2-dc23d927ec55" target="_blank">Recipe for a successful phishing campaign</a>. This post and its part 2 companion are great starting points for anyone new to phishing engagements.</li>
<li><a href="https://mksben.l0.cm/2020/10/discord-desktop-rce.html" target="_blank">Discord Desktop app RCE</a>. Another Electron app, another RCE. Consider this a must read if you are shipping or assessing an Electron based application. Demo <a href="https://youtu.be/0f3RrvC-zGI" target="_blank">here</a>.</li>
<li><a href="https://flangvik.com/azure/devops/privesc/abuse/2020/10/15/from-pipeline-to-production.html" target="_blank">Abusing pipelines to hijack production</a>. This is an example of successful red teaming showing the impact of a compromised developer account by seeing how much access Azure Pipelines could give a malicious user.</li>
<li><a href="https://blog.xpnsec.com/we-need-to-talk-about-macl/" target="_blank">We Need To Talk About MACL</a>. This post is a low level look at how user consent dialogs are handled on macOS, and sometimes how they are automatically dismissed. Of course by digging into the details, a CVE was waiting where arbitrary directories or files could be accessed without the user actually consenting. This is patched in 10.15.6.</li>
<li><a href="https://frichetten.com/blog/aws-api-enum-vuln/" target="_blank">Enumerate AWS API Permissions Without Logging to CloudTrail</a>. 645 different API actions across 40 different AWS services are affected by a bug (feature?) that allows you to query services with a malformed X-Amz-Target header and based on the 404 or 403 response, you can determine the level of access to the service without logging the request in CloudTrail. Sneaky! <a href="https://github.com/Frichetten/aws_stealth_perm_enum" target="_blank">aws_stealth_perm_enum</a> has the code.</li>
<li><a href="https://www.sans.org/blog/red-team-tactics-hiding-windows-services/" target="_blank">Red Team Tactics: Hiding Windows Services</a>. Hide your persistence from <cite>sc query</cite>, <cite>Get-Services</cite>, and the GUI!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/R4yGM/stegbrute" target="_blank">stegbrute</a> is a fast steganography bruteforce tool written in Rust (useful for CTFs).</li>
<li><a href="https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16938" target="_blank">CVE-2020-16938 Windows Kernel Information Disclosure Vulnerability</a>. Normally I wouldn't put a link to a Microsoft Advisory, but this one is so trivial to exploit, that <a href="https://twitter.com/jonasLyk/status/1316104870987010048" target="_blank">7zip can read any file on a Windows disk</a> (if Bitlocker is not in use) by directly opening the physical device.</li>
<li><a href="https://github.com/cribdragg3r/Alaris" target="_blank">Alaris</a> is a protective and Low Level Shellcode Loader the defeats modern EDR systems with direct syscalls, DLL blocking, PPID spoofing, and shellcode encryption. Well written blog describing the tool <a href="https://sevrosecurity.com/2020/10/14/alaris-a-protective-loader/" target="_blank">here</a>.</li>
<li><a href="https://github.com/Yaxser/CobaltStrike-BOF" target="_blank">CobaltStrike-BOF</a> are DCOM and WMI lateral movement BOFs for Cobalt Strike.</li>
<li><a href="https://github.com/cedowens/MacC2" target="_blank">MacC2</a> is a python-based macOS C2 that uses internal API calls instead of command line utilities.</li>
<li><a href="https://github.com/D00MFist/InSync" target="_blank">InSync</a> is a macOS Finder persistence technique. Code is 3 months old but only made public 2020-10-19.</li>
<li><a href="https://github.com/FSecureLABS/CalendarPersist" target="_blank">CalendarPersist</a> is a JXA script to allow programmatic persistence via macOS Calendar.app alerts. Blog post <a href="https://labs.f-secure.com/blog/operationalising-calendar-alerts-persistence-on-macos" target="_blank">here</a>. It's a big week for macOS tools!</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/omaidf/PrismX" target="_blank">PrismX</a> is a Cloud Security Dashboard, providing a single source of truth for cloud security issues based on AWS CIS Security Benchmarks. The dashboard provides a high-level overview for executives as well as actionable data for individual contributors with built-in JIRA integration.</li>
<li><a href="https://github.com/STMSolutions/RmiTaste" target="_blank">RmiTaste</a> allows security professionals to detect, enumerate, interact and exploit RMI services by calling remote methods with gadgets from ysoserial.</li>
<li><a href="https://github.com/moonD4rk/HackBrowserData" target="_blank">HackBrowserData</a> is a cross platform Go tool to decrypt passwords for most browser.</li>
<li><a href="https://github.com/passthehashbrowns/SharpBuster" target="_blank">SharpBuster</a> is a C# implementation of a directory brute forcing tool. It's designed to be used via Cobalt Strike's execute-assembly and similar tools, when running a similar tool over a SOCKS proxy is not feasible.</li>
<li><a href="https://github.com/slyd0g/SharpCrashEventLog" target="_blank">SharpCrashEventLog</a> crashes the Windows event log 3 times which keeps it down for 24 hours. Blog post <a href="https://limbenjamin.com/articles/crash-windows-event-logging-service.html" target="_blank">here</a>.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
