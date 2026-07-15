Title: Last Week in Security (LWiS) - 2020-03-16
Date: 2020-03-16 01:50
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-03-16
Author: Erik
Summary: Covid-19 as a lure, using OSINT to find John McAfee (again), another wormable SMB vulnerability (think WannaCry), and tons of new tools!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-03-09 to 2020-03-16.
MITRE ATT&amp;CK techniques are in brackets where appropriate.</p>
<p>Stuck in self-quarantine? <a href="https://github.com/k4m4/movies-for-hackers" target="_blank">Movies for hackers</a> is a great list of movies and shows for hackers and cyberpunk types.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://twitter.com/qwertyoruiopz/status/1237400079465689088?s=21" target="_blank">Apple's T2 Chip is vulnerable to checkra1n</a> which could lead to unlimited attempts to decrypt a FileVault protected volume if an attacker has physical access. This leads to an interesting question: Did Apple know about the bug and subsequent fix on the A12 chip or was it patched coincidently? If they did know about it, why are they still shipping Macs with the flawed T2 which is built on the vulnerable A10 chip?</li>
<li><a href="https://cloud.google.com/blog/products/management-tools/sre-keeps-digging-to-prevent-problems" target="_blank">Finding a problem at the bottom of the Google stack</a> details the process a Google site reliability engineer took as they traced down an issue from frontend to the datacenter. An interesting story of the kinds of issues you can have at Google-scale.</li>
<li><a href="https://access.redhat.com/errata/RHSA-2020:0631" target="_blank">CVE-2020-8597</a> is a bug in the Point-to-Point Protocol (PPP) daemon for linux which allows for an unauthenticated attacker to cause a stack based buffer overflow. Right now the only <a href="https://packetstormsecurity.com/files/156662/pppd-2.4.8-Buffer-Overflow.html" target="_blank">PoC</a> is a denial of service (crash) but this will likely be weaponized soon. <a href="https://github.com/paulusmack/ppp/commit/8d7970b8f3db727fe798b65f3377fe6787575426" target="_blank">Patch</a> your VPNs! [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190 Exploit Public-Facing Application</a>]</li>
<li><a href="https://github.com/taviso/avscript" target="_blank">avscript</a> from the infamous <a href="https://twitter.com/taviso" target="_blank">Tavis Ormandy</a> contains an interactive shell that lets you test Avast's custom javascript interpreter on Linux for vulnerability research. Yes, Avast ships a custom javascript interpreter and runs untrusted javascript through it. Since this came out Avast has disabled the interpreter globally.</li>
<li><a href="https://www.reddit.com/r/blueteamsec/comments/fiy0i8/master_thread_covid19corona_threat_actor_campaigns/" target="_blank">Covid-19/Corona: Threat Actor Campaigns</a> catalogs the many instances of threat actors leveraging the global pandemic to spread malware. Standard anti-phishing rules apply, even in a pandemic. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1192/" target="_blank">T1192 Spearphishing Link</a>]</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://medium.com/@benjamindbrown/finding-mcafee-a-case-study-on-geoprofiling-and-imagery-analysis-6f16bbd5c219" target="_blank">Finding McAfee: A Case Study on Geoprofiling and Imagery Analysis</a> is a case study of one man's quest to determine the location of John McAfee from a single image and tweet and serves as a good example of the OSINT work that can be done with what seems like very little information. At least this time he wiped the <a href="https://nakedsecurity.sophos.com/2012/12/03/john-mcafee-location-exif/" target="_blank">EXIF data</a> to make it a little harder.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><dl>
<dt><a href="https://outflank.nl/blog/2020/03/11/red-team-tactics-advanced-process-monitoring-techniques-in-offensive-operations/" target="_blank">Advanced process monitoring techniques in offensive operations</a> from Outflank introduces <a href="https://github.com/outflanknl/Ps-Tools" target="_blank">Ps-Tools</a>, an advanced process monitoring toolkit for offensive operations. These tools are useful to investigate and keep an eye on compromised hosts and alert when defenders show up and start investigating your tooling. The Ps-Tools are listed below. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1005/" target="_blank">T1005 Data from Local System</a>]</dt>
<dd><ul>
<li>Psx: Shows a detailed list of all processes running on the system.</li>
<li>Psk: Shows detailed kernel information including loaded driver modules.</li>
<li>Psc: Shows a detailed list of all processes with Established TCP connections.</li>
<li>Psm: Show detailed module information from a specific process id (loaded modules, network connections e.g.).</li>
<li>Psh: Show detailed handle information from a specific process id (object handles, network connections e.g.).</li>
<li>Psw: Show Window titles from processes with active Windows.</li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt><a href="https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV200005" target="_blank">CVE-2020-0978</a> is going to be one to remember like MS08-067 and MS17-010; kernel RCE in Windows 10 1903/1909 via a buffer overflow in SMB3's new compression capability means this is wormable and we will likely see something like WannaCry/Not-Petya. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190 Exploit Public-Facing Application</a>]</dt>
<dd><ul>
<li><a href="https://github.com/eerykitty/CVE-2020-0796-PoC" target="_blank">PoC</a></li>
<li><a href="https://github.com/ollypwn/SMBGhost" target="_blank">Scanner</a></li>
<li><a href="https://github.com/technion/DisableSMBCompression" target="_blank">Mitigation</a></li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt><a href="https://github.com/thalium/icebox" target="_blank">IceBox</a> is a modified virtualbox for windows or linux that enables live, stealthy tracing and debugging on any kernel or user process. It is currently limited to one CPU per virtual machine, which may cause issues with environmental checks in malware. Perhaps this could be combined with <a href="https://github.com/hfiref0x/VBoxHardenedLoader" target="_blank">VBoxHardenedLoader</a> or <a href="https://github.com/nsmfoo/antivmdetection" target="_blank">antivmdetection</a>.</dt>
<dd><ul>
<li><a href="https://www.youtube.com/watch?v=uJnxF0gptf8" target="_blank">Demo</a></li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt>Windows Privilege Escalation Exploits! I feel bad for any exploit dev who has been sitting on Windows LPE 0days as they aren't worth much any more. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</dt>
<dd><ul>
<li><a href="https://github.com/unamer/CVE-2019-1458" target="_blank">CVE-2019-1458 Windows LPE Exploit</a> is a kernel exploit that works on x64 systems Windows 7 up to but not including Windows 10. You only get one shot per reboot, and it may cause instability, so try any of the 30 other LPEs your target is likely vulnerable to before this one. Alternative PoC with details <a href="https://github.com/piotrflorczyk/cve-2019-1458_POC" target="_blank">here</a>.</li>
<li><a href="https://itm4n.github.io/cve-2020-0787-windows-bits-eop/" target="_blank">CVE-2020-0787 - Windows BITS - An EoP Bug Hidden in an Undocumented RPC</a> details a privileged file operation abuse in Windows 10 that leads to elevation of privilege to SYSTEM. <a href="https://github.com/itm4n/BitsArbitraryFileMove" target="_blank">PoC</a></li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/hardenedlinux/harbian-audit" target="_blank">harbian-audit</a> has been updated to support hardening Debian 10 and CentOS 8.</li>
<li><a href="https://github.com/hlldz/pickl3" target="_blank">pickl3</a> is another credential phishing tool for Windows. It is nicely packaged as a refelctive DLL and comes with a cna script for Cobalt Strike. For another option, see <a href="https://github.com/shantanu561993/SharpLoginPrompt" target="_blank">SharpLoginPrompt</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1056/" target="_blank">T1056 Input Capture</a>]</li>
<li><a href="https://github.com/SuprHackerSteve/Crescendo" target="_blank">Crescendo</a> is a swift based, real time event viewer for macOS. It utilizes Apple's Endpoint Security Framework. This could be the start of an open source macOS based EDR tool!</li>
<li><dl>
<dt><a href="https://3xpl01tc0d3r.blogspot.com/2020/03/introduction-to-callidus.html" target="_blank">Callidus</a> is a new O365 C2 framework written in .NET core (C#) that supports C2 via Outlook, OneNote, or Microsoft Teams. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1102/" target="_blank">T1102 Web Service</a>]</dt>
<dd><ul>
<li><a href="https://www.blogger.com/video.g?token=AD6v5dx9n7cwmgsYVg8uUfFfV5WfxNy6KmhFFYq9sOoZx7CN8iIPEg_neNUWipHKol8--NjWdSCVS9UQti5BhlsXAZszYjwMsgpcWnHtqR6dS_D2i2vcqon9NFZsmAtgq36br8OM3gn5" target="_blank">Outlook Demo</a></li>
<li><a href="https://www.blogger.com/video.g?token=AD6v5dyksi3pVe0P5VXhsDgJmpWdmqVTCsBTijRkslBIRBPPHttYfsE9jBf89JwgQNva0n4r4Fdau2aa4r4WjVX1BR99Ps7c6nBxzTj8F_YaLKoJqV3ZeqceCBbaR2nJie5LM96-pdQ" target="_blank">OneNote Demo</a></li>
<li><a href="https://www.blogger.com/video.g?token=AD6v5dwa-4BncEp8SZWzggiJAuDgvMOB4Wx9dFT-ZjWO0dOHryToKHoS89x9CesfNxpcnSS_oC3ZXmfh-Kkj8VFKyUczaGU6W0A0nVC7pATMEmaUTv3wTVoTaME-Hi4XFMp78POrdac" target="_blank">Microsoft Teams Demo</a></li>
<li><a href="https://github.com/3xpl01tc0d3r/Callidus" target="_blank">Code</a></li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/zeropointdynamics/zelos" target="_blank">Zelos</a>  is a comprehensive binary emulation platform written in python for linux binaries. x86, x86_64, ARM, and MIPS binaries are supported, with Unicorn providing CPU emulation.</li>
<li><a href="https://github.com/BC-SECURITY/Starkiller" target="_blank">Starkiller</a> is a frontend for the PowerShell Empire fork maintained by BC Security. Along with the improvements in the 3.1 release of PowerShell Empire, Starkiller allows for easy multi-user interaction with a common C2 server. More details available on the <a href="https://www.bc-security.org/post/an-introduction-to-starkiller" target="_blank">BC Security Blog</a>.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/saferwall/saferwall" target="_blank">saferwall</a> is a self-hosted open source malware analysis platform; basically a self-hosted virus total. Once you acquire AV licenses, saferwall will spin up all the infrastructure to do malware scanning across 12 major AVs!</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
</section>
