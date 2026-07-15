Title: Last Week in Security (LWiS) - 2021-07-06
Date: 2021-07-06 22:45
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-07-06
Author: Erik
Summary: PrintNightmare saga (<a href="https://twitter.com/cube0x0" target="_blank">@cube0x0</a>, <a href="https://twitter.com/gentilkiwi" target="_blank">@gentilkiwi</a>, + others), Gatekeeper bypass (<a href="https://twitter.com/theevilbit" target="_blank">@theevilbit</a>), DLL sideloading finder (<a href="https://twitter.com/ConsciousHacker" target="_blank">@ConsciousHacker</a>), Sudo LPE on vCenter (<a href="https://twitter.com/saidelike" target="_blank">@saidelike</a>), intro to Windows driver exploits (<a href="https://twitter.com/gf_256" target="_blank">@gf_256</a>), linux compatible C# merge tool (<a href="https://twitter.com/_EthicalChaos_" target="_blank">@_EthicalChaos_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-06-28 to 2021-07-06.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.wired.com/story/kaseya-supply-chain-ransomware-attack-msps/" target="_blank">A New Kind of Ransomware Tsunami Hits Hundreds of Companies</a>. REvil used certutil and MsMpEng.exe sideloading to great effect after compromising a popular managed service software provider.</li>
<li><a href="https://twitter.com/chrismlacy/status/1409727836093513729" target="_blank">Telco injects ads into Google SMS 2FA Messages</a>. If you needed any more ammo for why SMS 2FA is the worst kind of 2FA (but still much better than no 2FA!) here it is.</li>
<li><a href="https://blog.newsblur.com/2021/06/28/story-of-a-hacking/" target="_blank">How a Docker footgun led to a vandal deleting NewsBlur's MongoDB database</a>. As someone who has dealt with UFW and Docker issues as well as a NewsBlur user I feel this post. TLDR: Docker will bypass UFW and its really hard to get them to work together.</li>
<li><a href="https://twitter.com/YanZiShuang/status/1410964781885018112" target="_blank">Windows 11 LPE tweeted</a>. First blood?</li>
<li><a href="https://www.nsa.gov/news-features/press-room/Article/2677750/nsa-partners-release-cybersecurity-advisory-on-brute-force-global-cyber-campaign/" target="_blank">NSA, Partners Release Cybersecurity Advisory on Brute Force Global Cyber Campaign</a>. Looks like the GRU is brute forcing public logins. This is your weekly reminder to force 2FA for all users.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://donjon.ledger.com/kaspersky-password-manager/" target="_blank">Kaspersky Password Manager: All your passwords are belong to us</a>. The silly UX prevented this poorly seeded password generator that causes every instance of Kaspersky Password Manager in the world will generate the exact same password at a given second from being caught earlier. Or <em>dons tinfoil hat</em> maybe something else did...</li>
<li><a href="https://blog.assetnote.io/2021/06/27/uber-account-takeover-voicemail/" target="_blank">Taking over Uber accounts through voicemail</a>. This is an attack enabled by the fact Uber will deliver OTP codes via audio to voicemail, and the fact that voicemail boxes are usually very easy to compromise. Ensure your scoping document allows for this type of attack before attempting, as multiple parties are involved.</li>
<li><a href="https://medium.com/manomano-tech/a-red-team-operation-leveraging-a-zero-day-vulnerability-in-zoom-80f57fb0822e" target="_blank">A Red Team Operation Leveraging a zero-day vulnerability in Zoom</a>. Unpacking and adding payloads to legitimate installers is a nifty trick. Without complete verification of all files in an MSI this is possible, and the best part is these applications are likely allow-listed by AV/EDR or the SOC.</li>
<li><a href="https://googleprojectzero.blogspot.com/2021/06/an-epyc-escape-case-study-of-kvm.html" target="_blank">An EPYC escape: Case-study of a KVM breakout</a>. This post describes a vulnerability in KVM’s AMD-specific code and discuss how this bug can be turned into a full virtual machine escape. This is the first public writeup of a KVM guest-to-host breakout that does not rely on bugs in user space components such as QEMU.</li>
<li><a href="https://theevilbit.github.io/posts/gatekeeper_not_a_bypass/" target="_blank">GateKeeper - Not a Bypass (Again)</a>. macOS' Gatekeeper alerts users when executing files that have been downloaded, but it doesn't alert on notarized dynamic library loads, even if they have the quarantine attribute set. How this be abused? Malicious screen savers, color picker plugins, preference panes etc can be used to execute arbitrary code from the internet without any warnings. Getting the files to the correct locations is an exercise left to the reader.</li>
<li><a href="https://www.trustedsec.com/blog/bits-persistence-for-script-kiddies/" target="_blank">BITS Persistence for Script Kiddies</a>. This technique is likely monitored by EDR but is worth having in your tool bag none the less.</li>
<li><a href="https://github.com/irsl/gcp-dhcp-takeover-code-exec" target="_blank">gcp-dhcp-takeover-code-exec</a>. By predicting the seed to the random number generator used by Debian's DHCP client, a malicious user with access to a VM in the same subnet of a rebooting VM can impersonate the metadata service and add a malicious ssh key to the victim VM. The practical implications of this are very limited, but it remains unpatched.</li>
<li><a href="https://securityintelligence.com/posts/windows-features-dll-sideloading/" target="_blank">Hunting for Windows “Features” with Frida: DLL Sideloading</a>. DLL sideloading is an underutilized technique, but as it is hard to detect, advanced adversaries are using it. The new <a href="https://github.com/ConsciousHacker/WFH" target="_blank">WFH</a> tool uses Frida to identify potentially sideload-able DLLs in programs.</li>
<li><a href="https://3xpl01tc0d3r.blogspot.com/2021/07/resource-based-constrained-delegation.html" target="_blank">Abusing Resource-Based Constrained Delegation (RBCD) using Linux</a>. RBCD is a confusing misconfiguration present in some Active Directory environments. This post has both an offensive and defensive walkthrough.</li>
<li><a href="https://ethicalchaos.dev/2021/07/04/merging-c-assemblies-using-dnmerge/" target="_blank">Merging C# Assemblies using dnMerge</a>. This new C# assembly merge tool is a plugin for MSBuild that plays nicely with dotnet and uses LZMA for more efficient compression than Costura, allowing more tools to stay under the 1MB limit of Cobalt Strike's execute-assembly command.</li>
<li><a href="https://research.nccgroup.com/2021/07/06/exploiting-the-sudo-baron-samedit-vulnerability-cve-2021-3156-on-vmware-vcenter-server-7-0/" target="_blank">Exploiting the Sudo Baron Samedit vulnerability (CVE-2021-3156) on VMWare vCenter Server 7.0</a>. This in depth post digs into how the Sudo LPE works, what vCenter/Photon OS is, and how they adapted the exploit to work against vCenter 7.</li>
<li><a href="https://research.nccgroup.com/2021/06/28/exploit-mitigations-keeping-up-with-evolving-and-complex-software-hardware/" target="_blank">Exploit mitigations: keeping up with evolving and complex software/hardware</a>. This projects aims to answer the question, "does my current environment have mitigation X?"</li>
<li><a href="https://github.com/stong/CVE-2020-15368" target="_blank">How to exploit a vulnerable windows driver</a>. AsRock took <a href="http://rweverything.com/" target="_blank">RWEverything</a>, slapped some AES encryption (with hardcoded key) on the ioctl calls, and shipped it as a product. A quick overwrite of BeepDeviceControl and you have kernel execution.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><dl>
<dt><a href="https://github.com/afwu/PrintNightmare" target="_blank">PrintNightmare</a>. The print spooler in Windows has a vulnerability that allows any domain user to install a print driver and achieve remote code execution.</dt>
<dd><ul>
<li>Also check out the <a href="https://github.com/cube0x0/CVE-2021-1675" target="_blank">Impacket implementation</a> which also includes a C# variant for local privilege escalation (or there is <a href="https://github.com/hlldz/CVE-2021-1675-LPE" target="_blank">CVE-2021-1675-LPE</a>).</li>
<li><a href="https://twitter.com/StanHacked/status/1410405688766042115" target="_blank">Some testing</a> has shown that domain controllers are vulnerable even after the June patch, possibly related to the "Point &amp; Print" feature or perhaps <a href="https://twitter.com/gentilkiwi/status/1410621282446495749" target="_blank">"BuiltinPre-Windows 2000 Compatible Access"</a>.</li>
<li>Confused? Check <a href="https://twitter.com/StanHacked/status/1410929974358515719/photo/1" target="_blank">this flow chart</a>.</li>
<li>For detection <a href="https://www.reddit.com/r/msp/comments/ob6y02/critical_vulnerability_printnightmare_exposes/" target="_blank">this msp thread</a> is great and there are <a href="https://blog.0patch.com/2021/07/free-micropatches-for-printnightmare.html" target="_blank">free micropatches</a> and a collection of resources <a href="https://github.com/cado-security/DFIR_Resources_REvil_Kaseya" target="_blank">on GitHub</a>.</li>
<li><a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527" target="_blank">Official Microsoft Response</a></li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/ant4g0nist/ManuFuzzer" target="_blank">ManuFuzzer</a> is an LLVM-based binary, coverage-guided fuzzing framework for macOS . It is simple to integrate coverage-guided fuzzing with ManuFuzzer: just define a special function, update some build flags, and you have instant binary-only, coverage-guided fuzzing (only basic-block coverage). Using ManuFuzzer, you can instrument one or more selected frameworks for coverage and fuzz the target functions/library.</li>
<li><a href="https://github.com/0xDivyanshu/Injector" target="_blank">Injector</a> is a complete arsenal of memory injection and other techniques for red-teaming in Windows written in C#. This is a good base for writing your own loader, or testing EDR detections in a purple team scenario.</li>
<li><a href="https://github.com/G4lB1t/pstf2" target="_blank">pstf2</a>  is an implementation of an HTTP server capable of passive browser fingerprinting to detect and block security scanning services from accessing hosted payloads.</li>
<li><a href="https://github.com/ajpc500/RelayRumbler" target="_blank">RelayRumbler</a> is a proof-of-concept tool that attempts to retrieve the configuration from the memory dump of an <a href="https://labs.f-secure.com/tools/c3/" target="_blank">F-Secure C3 Relay</a> executable.</li>
<li><a href="https://github.com/kkent030315/PageTableInjection" target="_blank">PageTableInjection</a> is a proof-of-concept of the page table injection technique to inject malicious code into the arbitrary user processes. Be sure to read "The Problem" section to understand stability issues.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/dsnezhkov/shutter" target="_blank">shutter</a>. Not sure how I missed this gem. The goal of Shutter is to manage windows network stack communication via Windows Filtering Platform. Management can include blocking or permitting traffic based on IP or an executable that initiates or receives the traffic. This is useful to blackhole event logging, defensive agent communication, or explicitly permit specific executables to communicate if they have been previously restricted by policy and runs totally in memory. How good is that expensive EDR if it can't call home?</li>
<li><a href="https://github.com/dandare100/agentstub" target="_blank">agentstub</a> ssh agent forwarding is a big win for attackers with root on a compromised machine, and this tool illustrates some private key operations that can be done with the ssh-agent like signing files with RSA private keys.</li>
<li><a href="https://github.com/dahall/Vanara" target="_blank">Vanara</a> is set of .NET libraries for Windows implementing P/Invoke calls to many native Windows APIs with supporting wrappers. Use this to easily add P/Invoke calls to your next C# tool.</li>
<li><a href="https://github.com/praetorian-inc/PortBender" target="_blank">PortBender</a> is a TCP port redirection utility that allows a red team operator to redirect inbound traffic destined for one TCP port (e.g., 445/TCP) to another TCP port (e.g., 8445/TCP). PortBender includes an aggressor script that operators can leverage to integrate the tool with Cobalt Strike. However, because the tool is implemented as a reflective DLL, it can integrate with any C2 framework supporting loading modules through a "ReflectiveLoader" interface. Be aware this loads a driver, WinDivert64.sys.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
