Title: Last Week in Security (LWiS) - 2021-11-22
Date: 2021-11-22 20:45
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-11-22
Author: Erik
Summary: AFL++ on Android (<a href="https://twitter.com/Gr33nh4t" target="_blank">@Gr33nh4t</a>), Qualcomm NPU exploits (<a href="https://twitter.com/mmolgtm/" target="_blank">@mmolgtm</a>), sysWhipser research (<a href="https://twitter.com/CaptMeelo" target="_blank">@CaptMeelo</a>), TPM sniffing (Julien Oberson), CheckCert and SQLRecon (<a href="https://twitter.com/sanjivkawa" target="_blank">@sanjivkawa</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-11-16 to 2021-11-22.</p>
<aside class="m-note m-warning">
<h3>Break</h3>
<p>Last Week in Security will be taking a week off next week. Spend time with the new goodies you got as part of <a href="https://github.com/0x90n/InfoSec-Black-Friday" target="_blank">InfoSec Black Friday Deals 2021</a>.</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://github.blog/2021-11-15-githubs-commitment-to-npm-ecosystem-security/" target="_blank">GitHub’s commitment to npm ecosystem security</a>. Dependancy package security is a hard problem to solve, but it seems NPM has gotten a lot of flak recently. Mandatory 2FA and other measures may help. "But I use rust," you say? Read on...</li>
<li><a href="https://kerkour.com/rust-crate-backdoor/" target="_blank">Backdooring Rust crates for fun and profit</a>. Running other people's code easily is a bedrock feature of any software dependency or library manager. It's quite difficult to make sure that code isn't malicious.</li>
<li><a href="https://www.malwaretech.com/2021/11/an-in-depth-look-at-hacking-back-active-defense-and-cyber-letters-of-marque.html" target="_blank">An in-depth look at hacking back, active defense, and cyber letters of marque</a>. Interesting conclusion (government should be in control) for a guy who prevented a malware outbreak with "active defense" as a civilian. Perhaps that gives more weight to his argument, having "seen the other side?" I have yet to read any opinion pieces by current or former government offensive security professionals on the matter - aside from <a href="https://www.securityweek.com/experts-analyze-proposed-bill-allowing-private-entities-hack-back%E2%80%99" target="_blank">Jake Williams</a> of course.</li>
<li><a href="https://www.zdnet.com/article/emotet-once-the-worlds-most-dangerous-malware-is-back/" target="_blank">Emotet, once the world's most dangerous malware, is back</a>. What is dead my never die? Keep track of the threat <a href="https://urlhaus.abuse.ch/browse/tag/emotet/" target="_blank">here</a>.</li>
<li><a href="https://www.forescout.com/research-labs/nucleus-13/" target="_blank">NUCLEUS:13</a>. The IoT/OT/embedded OS from Siemens, <a href="https://www.plm.automation.siemens.com/global/en/products/embedded/nucleus-rtos.html" target="_blank">Nucleus RTOS</a>, had flaws in its TCP/IP stack including a buffer overflow in the FTP USER command. The <a href="https://github.com/Forescout/project-memoria-detector" target="_blank">project-memoria-detector</a> can help identify the TCP/IP stack of a device if you think you may have some Nucleus systems in your environment.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://alephsecurity.com/2021/11/16/fuzzing-qemu-android/" target="_blank">AFL++ on Android with QEMU support</a>. Ever wanted to fuzz close-source libraries directly on your Android phone? Now you can!</li>
<li><a href="https://blog.cobaltstrike.com/2021/11/17/nanodump-a-red-team-approach-to-minidumps-cobalt-strike/" target="_blank">Nanodump: A Red Team Approach to Minidumps</a>. The tool has been out for a while, but this post explains the motivation and technical details.</li>
<li><a href="https://securitylab.github.com/research/qualcomm_npu/" target="_blank">Fall of the machines: Exploiting the Qualcomm NPU (neural processing unit) kernel driver</a>. Some interesting bugs found in the NPU driver accessible from the untrusted app sandbox on (presumably) lots of Android devices.</li>
<li><a href="https://captmeelo.com//redteam/maldev/2021/11/18/av-evasion-syswhisper.html" target="_blank">When You sysWhisper Loud Enough for AV to Hear You</a>. Static syscalls have their signatures. This post explores some work arounds, but some *Gate (Hell's, Heaven's, etc) would prevent these artifacts in your code at all (but introduce others).</li>
<li><a href="https://research.nccgroup.com/2021/11/18/an-illustrated-guide-to-elliptic-curve-cryptography-validation/" target="_blank">An Illustrated Guide to Elliptic Curve Cryptography Validation</a>. Elliptic curves are becoming the standard way to perform asymmetric cryptography, but how do they actually work? This post can serve as a refresher for that college cryptography class you took or didn't take.</li>
<li><a href="https://posts.specterops.io/active-directory-attack-paths-is-everyone-this-bad-44b7538402c" target="_blank">Active Directory Attack Paths — “Is it always this bad?”</a>. From experience: yes. This post is mostly an ad for Bloodhound Enterprise, but that's ok.</li>
<li><a href="https://peterjson.medium.com/some-notes-about-microsoft-exchange-deserialization-rce-cve-2021-42321-110d04e8852" target="_blank">Some notes about Microsoft Exchange Deserialization RCE (CVE-2021–42321)</a>. After ProxyShell, Exchange got some serious attention and to no one's surprise more RCE fell out of it. This one affected Exchange 2016 CU21/22 and 2019 CU10/1 but he post goes into technical detail and stops just short of a PoC.</li>
<li><a href="https://wafzsucks.medium.com/hacksys-extreme-vulnerable-driver-arbitrary-write-null-new-solution-7d45bfe6d116" target="_blank">HackSys Extreme Vulnerable Driver — Arbitrary Write NULL (New Solution)</a>. This is a very detailed post on a cool privilege escalation against a vulnerable by design driver.</li>
<li><a href="https://mrd0x.com/abusing-google-drives-email-file-functionality/?no-cache=1" target="_blank">Abusing Google Drive's Email File Functionality</a>. This is a great way to abuse legitimate services to deliver phishing emails. Very tricky!</li>
<li><a href="https://rastamouse.me/externalc2-net/" target="_blank">ExternalC2.NET</a>. This is the post that explains the tool released last week.</li>
<li><a href="https://www.exandroid.dev/2021/11/20/pentest-tale-dumping-cleartext-credentials-from-antivirus/" target="_blank">Pentest tale - Dumping cleartext credentials from antivirus</a>. Sometimes memory dumps and findstr is all it takes to find credentials of value.</li>
<li><a href="https://captmeelo.com//redteam/maldev/2021/11/22/picky-ppid-spoofing.html" target="_blank">Picky PPID Spoofing</a>. This post has some good example code to help find svchost processes with your integrity level to allow them to be used as a PPID for your process.</li>
<li><a href="https://labs.jumpsec.com/no-logs-no-problem-incident-response-without-windows-event-logs/" target="_blank">No Logs? No Problem! Incident Response without Windows Event Logs</a>. You can also read this as, "All the things you need to clean up to help stay undetected."</li>
<li><a href="https://jonpalmisc.com/2021/11/22/cve-2021-40531" target="_blank">Using CVE-2021-40531 for RCE with Sketch</a>. "This post covers a vulnerability in Sketch that I discovered back in July — CVE-2021-40531. In its simplest form, it is a macOS quarantine bypass, but in context it can be used for remote code execution."</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Tldraw/Tldraw" target="_blank">tldraw</a> is a tiny little drawing app. Check it out at <a href="https://www.tldraw.com/" target="_blank">tldraw.com</a>.</li>
<li><a href="https://github.com/microsoft/msticpy" target="_blank">msticpy</a>. Ever wonder how Microsoft's MSTIC threat hunt group finds evil? msticpy is a library for InfoSec investigation and hunting in Jupyter Notebooks with many data analysis features.</li>
<li><a href="https://github.com/ariary/fileless-xec" target="_blank">fileless-xec</a> is a stealth dropper executing remote binaries without dropping them on disk.</li>
<li><a href="https://blog.scrt.ch/" target="_blank">TPM sniffing</a>. With $49 of hardware you too can read a bitlocker key as it leaves the TPM of a laptop. TPM 2.0 has support to encrypt this value, but until then/even after consider adding a second factor to your laptop's decryption routine (PIN, hardware key, etc).</li>
<li><a href="https://github.com/skahwah/CheckCert" target="_blank">CheckCert</a> A small utility to request the SSL certificate from a public or private web application implemented in C# and as a BOF.</li>
<li><a href="https://github.com/skahwah/SQLRecon" target="_blank">SQLRecon</a> is a C# MS SQL toolkit designed for offensive reconnaissance and post-exploitation.</li>
<li><a href="https://github.com/dievus/Oh365UserFinder" target="_blank">Oh365UserFinde</a> is used for identifying valid o365 accounts and domains without the risk of account lockouts. The tool parses responses to identify the "IfExistsResult" flag is null or not, and responds appropriately if the user is valid.</li>
<li><a href="https://github.com/securifybv/Visual-Studio-BOF-template" target="_blank">Visual-Studio-BOF-template</a> is a baseline template that can be reused to develop BOFs with Visual Studio without having to worry about dynamic function resolution syntax, stripping symbols, compiler configurations, C++ name mangling, or unexpected runtime errors.</li>
<li><a href="https://github.com/oXis/GPUSleep" target="_blank">GPUSleep</a> moves the beacon image to GPU memory before the beacon sleeps, and move it back to main memory after sleeping. Check out the blog post <a href="https://oxis.github.io/GPUSleep/" target="_blank">here</a>.</li>
<li><a href="https://github.com/S3cur3Th1sSh1t/MultiPotato" target="_blank">MultiPotato</a> is another "potato" to get SYSTEM via SeImpersonate privileges, but this one is different since tt doesn't contain any SYSTEM auth trigger for weaponization so the code can be used to integrate your favorite trigger by yourself. Also, tt's not only using CreateProcessWithTokenW to spawn a new process. Instead you can choose between CreateProcessWithTokenW, CreateProcessAsUserW, CreateUser and BindShell.</li>
<li><a href="https://github.com/icyguider/DumpNParse" target="_blank">DumpNParse</a>  is a Combination LSASS Dumper and LSASS Parser adapted from other projects.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/frankwxu/digital-forensics-lab" target="_blank">digital-forensics-lab</a> is a free hands-on digital forensics labs for students and faculty. Note that on windows it actually <a href="https://github.com/ariary/fileless-xec/blob/45c897a93469aa5391511520808fc5dbfd9c2251/pkg/execwindows/exec_windows.go#L72" target="_blank">drops the binary to disk</a> and runs it, going against the very name of the project...</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
