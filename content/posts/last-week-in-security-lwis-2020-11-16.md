Title: Last Week in Security (LWiS) - 2020-11-16
Date: 2020-11-16 23:30
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-11-16
Author: Erik
Summary: AV bypasses for common C2s (<a href="https://twitter.com/ShitSecure" target="_blank">@ShitSecure</a>), Big Sur firewall bypass (<a href="https://twitter.com/patrickwardle" target="_blank">@patrickwardle</a>), 10 vulns in Bitdefender (<a href="https://twitter.com/0xlandave" target="_blank">@0xlandave</a>), Win7 LPE (<a href="https://twitter.com/itm4n" target="_blank">@itm4n</a>), COM mapping tool (<a href="https://twitter.com/hotnops" target="_blank">@hotnops</a>), hooks for Windows password dumping (<a href="https://twitter.com/last0x00" target="_blank">@last0x00</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-11-09 to 2020-11-16.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://specterops.io/so-con2020" target="_blank">SO-CON 2020</a> is a conference by SpecterOps and has great talks lined up for 2020-11-20!</li>
<li><a href="https://old.reddit.com/r/hackintosh/comments/jsziec/whats_new_in_macos_11_big_sur/" target="_blank">What's new in macOS 11, Big Sur!</a>. Apple's latest OS was released last Thursday, and one of the best sources for what's new is the hackintosh subreddit.</li>
<li><a href="https://www.macrumors.com/2020/11/15/m1-chip-emulating-x86-benchmark/" target="_blank">Apple Silicon M1 Emulating x86 is Still Faster Than Every Other Mac in Single Core Benchmark</a>. Apple released their in house ARM-based chips last week for the 13" MacBook Pro, MacBook Air, and Mac mini. They said it was fast, but this benchmark really shows it. Even emulating x86, a Macbook Air scored higher on single-core performance than a 2020 iMac with an Intel i9-10910 (10 cores at 3.6 GHz). Seriously impressive. In multicore benchmarks, the Mac mini with M1 is surprisingly high on the all time <a href="https://browser.geekbench.com/mac-benchmarks" target="_blank">benchmarks</a> list.</li>
<li><a href="https://blog.cryptohack.org/macos-ocsp-disaster" target="_blank">Can't open apps on macOS: an OCSP disaster waiting to happen</a>. While Apple was making amazing strides with its new silicon, it was also being dragged through the mud for its Gatekeeper implementation. This post is the most honest (spoiler: Apple isn't collecting executable hashes every time you launch them), and discusses the missteps of the implementation. There is a place for this type of security mechanism, but it should be designed with privacy first - especially from a company that plays the privacy card as hard as Apple does. Apple has <a href="https://support.apple.com/en-us/HT202491" target="_blank">issued a statement (bottom)</a> with vague promises. At this point, Linux distros are the last OSs left without telemetry baked in (and <a href="https://popcon.ubuntu.com/" target="_blank">some distros</a> have it).</li>
<li><a href="https://twitter.com/patrickwardle/status/1327726496203476992" target="_blank">Big Sur allows apps to bypass firewalls</a>. Apple news again, and this is impressively poor showing. How this got past all the meetings and approvals it must have taken is beyond me. Apple has exempted many Apple applications from being routed through new frameworks on Big Sur that Apple requires 3rd party firewalls to use (no more kexts). I guess Apple was convinced it would help with their mission to have things "just work," but if a user is installing a 3rd party firewall, they probably know what they are doing...</li>
<li><a href="https://www.chadduffey.com/2020/11/20H2.html" target="_blank">Windows 20H2 changes</a> is a comparison of Windows 10 2004 and Windows 10 20H2 installations. Could be a menu of new things to look into for vulnerabilities, or just new legitimate service names to hide your persistence.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://landave.io/2020/11/bitdefender-upx-unpacking-featuring-ten-memory-corruptions/" target="_blank">Bitdefender: UPX Unpacking Featuring Ten Memory Corruptions</a>. Antivirus products have been the target or researchers in the past, but finding 10 memory corruptions in a single feature of one is impressive. The timeline of disclosure also contains more than a few 🤦.</li>
<li><a href="https://securitylab.github.com/research/Ubuntu-gdm3-accountsservice-LPE" target="_blank">How to get root on Ubuntu 20.04 by pretending nobody’s /home</a>. This is a super strange bug that requires physical access to a Ubuntu machine with a GUI. By tricking the accounts-daemon to thinking you a new user, you get root! Demo <a href="https://youtu.be/8IjTq7GBupw" target="_blank">here</a>.</li>
<li><a href="https://sick.codes/extraordinary-vulnerabilities-discovered-in-tcl-android-tvs-now-worlds-3rd-largest-tv-manufacturer/" target="_blank">Extraordinary Vulnerabilities Discovered in TCL Android TVs, Now World’s 3rd Largest TV Manufacturer.</a>. TCL's heavily modified Android TV implementation is full of holes. Or maybe a better description is that is is a hole with some non-hole parts, possibly on accident. You have all your IoT on a separate network right?</li>
<li><a href="https://skelsec.medium.com/duping-av-with-handles-537ef985eb03" target="_blank">Duping AV with handles</a>. Calling OpenProcess on lsass is a big red flag for most AV. However, some things do "legitimately" open handles (like <a href="https://community.mcafee.com/t5/ePolicy-Orchestrator-ePO/Lsass-Process-Access/m-p/639215/highlight/true#M67953" target="_blank">AV itself</a>). Using debug privileges, a process can find these legitimate handles and clone them, fooling some AV. Code <a href="https://github.com/skelsec/pypykatz/blob/8ad07f2f6f0c4904f9a77c711f693d6c794a7fb4/pypykatz/commons/winapi/local/function_defs/live_reader_ctypes.py#L82" target="_blank">here</a>.</li>
<li><a href="https://medium.com/@kanytu/firefox-and-how-a-website-could-steal-all-of-your-cookies-581fe4648e8d" target="_blank">Firefox: How a website could steal all your cookies</a>. The older Firefox Fennec (v68.9.0) on Android was vulnerable to a complex attack chain that allowed for an attacker to download the cookies.sql file from users after a single click. This feels like a nation-state style vulnerability that would be used against targeted individuals.</li>
<li><a href="https://s3cur3th1ssh1t.github.io/Customizing_C2_Frameworks/" target="_blank">Customizing C2-Frameworks for AV-Evasion</a> walks through some AV evasion techniques for Powershell Empire, Pupy, and Covenant.</li>
<li><a href="https://kennysong.github.io/adversarial.js/" target="_blank">adversarial.js</a> is a really well done demo of how machine learning classifier models can be tricked with images that remain easily discernible to humans. Next time a vendor leans on ML, know that it isn't a silver bullet. Maybe if you had <a href="https://www.engadget.com/nvidia-dgx-station-a100-80gb-tensor-core-gpu-announcement-140027589.html" target="_blank">320GB of GPU memory</a> things would be different.</li>
<li><a href="https://research.nccgroup.com/2020/11/11/decrypting-openssh-sessions-for-fun-and-profit/" target="_blank">Decrypting OpenSSH sessions for fun and profit</a>. If you have a memory image of a server with an active SSH connection, and a pcap of that SSH session, you can decrypt it! Code <a href="https://github.com/fox-it/OpenSSH-Session-Key-Recovery" target="_blank">here</a>.</li>
<li><a href="https://www.gosecure.net/blog/2020/11/13/forget-your-perimeter-part-2-four-vulnerabilities-in-pulse-connect-secure/" target="_blank">Forget Your Perimeter Part 2: Four Vulnerabilities in Pulse Connect Secure</a>. As VPNs become vital for business, they also become bigger targets for adversaries. This is an nice vulnerability chain that goes from XSS to RCE. GoSecure included details on a neat trick to get access to the unencrypted filesystem of the Pulse Secure appliance as well, which could apply to other appliances you may be hacking.</li>
<li><a href="https://swarm.ptsecurity.com/advanced-mssql-injection-tricks/" target="_blank">Advanced MSSQL Injection Tricks</a>. MSSQL is often see in enterprise environments. Now you can pwn it in new and fun ways!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://posts.specterops.io/apollo-and-mythic-a-myth-worth-retelling-207893ea8b51" target="_blank">Apollo and Mythic: A Myth Worth Retelling</a>. Apollo was in last weeks edition of this blog, but this post digs into some of the features it has. Apollo + Mythic is a powerful combination.</li>
<li><a href="https://itm4n.github.io/windows-registry-rpceptmapper-eop/" target="_blank">Windows RpcEptMapper Service Insecure Registry Permissions EoP</a>. While only effective against Windows 7, this local privilege escalation vulnerability is a classic case of seeing something strange and digging into it, reading the docs, and coming away with an interesting result.</li>
<li><a href="https://github.com/last-byte/HppDLL" target="_blank">HppDLL</a> enables local password dumping using MsvpPasswordValidate hooks. Explanation <a href="https://offnotes.notso.pro/abusing-credentials/dumping-credentials/msvppasswordvalidate-hook" target="_blank">here</a>.</li>
<li><a href="https://github.com/ComodoSecurity/openedr" target="_blank">openedr</a> is free and open source platform allows you to analyze what’s happening across your entire environment at base-security-event level. The repo is a little light on details for now, but this is one to watch.</li>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2075" target="_blank">Issue 2075: Windows: Local Spooler CVE-2020-1337 Bypass</a>. Microsoft finally actually patched the local spooler local privilege escalation vulnerability in Windows 10. This issue has a PoC if you come across any machines that don't have the November 2020 patch.</li>
<li><a href="https://github.com/hotnops/COM_Mapper" target="_blank">COM_Mapper</a> is a tool to create COM class/interface relationships in neo4j. Like BloodHound for COM!</li>
<li><a href="https://github.com/hackerhouse-opensource/exploits/blob/master/aix53l-libc.c" target="_blank">aix53l-libc.c</a>. If you are unfortunate enough to gain access to an AIX machine, you can root it easily now with this 0day that exploits a buffer overflow in the handling of locale environment variables.</li>
<li><a href="https://github.com/Martyx00/ghinja" target="_blank">ghinja</a> is a plugin to embed Ghidra Decompiler into Binary Ninja.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/c9fe/22120" target="_blank">22120</a> is a tool to self-host the Internet with an offline archive. Similar to ArchiveBox, SingleFile and WebMemex.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
