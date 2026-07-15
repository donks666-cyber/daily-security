Title: Last Week in Security (LWiS) - 2021-06-21
Date: 2021-06-21 21:10
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-06-21
Author: Erik
Summary: AD pwnage (<a href="https://twitter.com/harmj0y" target="_blank">@harmj0y</a>, <a href="https://twitter.com/tifkin_" target="_blank">@tifkin_</a>, and <a href="https://twitter.com/elad_shamir" target="_blank">@elad_shamir</a>), ImageLoad bypass (<a href="https://twitter.com/_batsec_" target="_blank">@_batsec_</a>), bofnet_executeassembly (<a href="https://twitter.com/william_knows" target="_blank">@william_knows</a>), reverse port knocking on Windows (<a href="https://twitter.com/TheXC3LL" target="_blank">@TheXC3LL</a>), LNK generator (<a href="https://twitter.com/Jean_Maes_1994" target="_blank">@Jean_Maes_1994</a>), payload automation (<a href="https://twitter.com/binaryfaultline" target="_blank">@BinaryFaultline</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-06-14 to 2021-06-21.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://blog.torproject.org/snowflake-in-tor-browser-stable" target="_blank">Snowflake moving to stable in Tor Browser 10.5</a>. This is an interesting solution for users in restrictive environments that uses volunteer browsers as WebRTC proxies for the initial bridge connection into the Tor network. The initial broker connection uses domain fronting on Azure, so this may not last very long (or will be forced to switch providers).</li>
<li><a href="https://about.fb.com/news/2021/06/testing-in-headset-vr-ads/" target="_blank">Testing In-Headset VR Ads</a>. Facebook buys occulus. Facebook puts ads in occulus VR. No one is surprised.</li>
<li><a href="https://forums.rockylinux.org/t/rocky-linux-8-4-available-now/3015" target="_blank">Rocky Linux 8.4 Available Now</a>. After Red Hat/CentOS was sold to IBM, predictably big blue cut support for the community supported CentOS and turned it into a rolling release (breaking lots of LTS promises in the process). The community responded and in just 7 months a stable replacement distro is available! The <a href="https://github.com/rocky-linux/rocky-tools/tree/main/migrate2rocky" target="_blank">migrate2rocky</a> makes moving from CentOS 8 to Rocky easy.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://posts.specterops.io/certified-pre-owned-d95910965cd2" target="_blank">Certified Pre-Owned</a>. This is a long post, and a longer whitepaper, but if you attack or defend Active Directory it's a must read. The number of ways you can misconfigure AD certificate services is pretty incredible, and despite being documented as dangerous, they are common (like unconstrained delegation). Lots of tooling is linked in the post, but there is also <a href="https://github.com/RemiEscourrou/Invoke-Leghorn" target="_blank">Invoke-Leghorn</a> and <a href="https://www.riskinsight-wavestone.com/en/2021/06/microsoft-adcs-abusing-pki-in-active-directory-environment/" target="_blank">Microsoft ADCS – Abusing PKI in Active Directory Environment</a>.</li>
<li><a href="https://shenaniganslabs.io/2021/06/21/Shadow-Credentials.html" target="_blank">Shadow Credentials: Abusing Key Trust Account Mapping for Account Takeover</a>. Just when you had enough AD for the week, <a href="https://github.com/eladshamir/Whisker" target="_blank">Whisker</a> drops to make DACL-based attacks against User and Computer objects in Active Directory much easier. There are some caveats, like Windows Server 2016 Functional Level in Active Directory and at least one Windows Server 2016 Domain Controller with a digital certificate for server authentication installed, but with those fulfilled, account access becomes much easier than before thanks to Windows Hello for Business. Hello to new access.</li>
<li><a href="https://thezerohack.com/apple-vulnerability-bug-bounty" target="_blank">How I Found A Vulnerability To Hack iCloud Accounts and How Apple Reacted To It</a>. Bug bounties can be great, but when the researcher and company can't agree on exploitability or severity, there can be bad blood. This research showed how an attacker could use a large number (28,000) of IP address to bypass rate limits and guess a 6 digit reset code for iCloud accounts.</li>
<li><a href="https://www.elastic.co/blog/process-ghosting-a-new-executable-image-tampering-attack" target="_blank">What you need to know about Process Ghosting, a new executable image tampering attack</a>. By creating an executable as "DELETE PENDING," defender (and possibly other EDRs) will be unable to scan it and thus block execution. PoC <a href="https://github.com/hasherezade/process_ghosting" target="_blank">here</a>.</li>
<li><a href="https://www.avanan.com/blog/attackers-take-advantage-of-new-google-doc-exploit" target="_blank">Attackers Take Advantage of New Google Docs Exploit</a>. This boils down to a fancy way to have your phishing pages hosted on docs.google.com, but it is likely effective none the less.</li>
<li><a href="https://www.mdsec.co.uk/2021/06/bypassing-image-load-kernel-callbacks/" target="_blank">Bypassing Image Load Kernel Callbacks</a>. As EDRs move to kernel drivers, image load callbacks are what is being used to detect DLL loads. This library reimplements the Windows loader from scratch in userspace to prevent these callbacks from being sent to the kernel. Impressive stuff, and it can even load DLLs directly from memory - something the Windows loader cannot do. This library will likely be seen in any new loader or RAT going forward. Be sure to check out this <a href="https://github.com/moloch--/DarkLoadLibrary" target="_blank">llvm-obfuscator</a> enabled fork as well.</li>
<li><a href="https://github.com/1d8/publications/tree/main/monday-cnc" target="_blank">monday-cnc</a>. Like any service with an API that can store and retieve data, planning site Monday.com can be used as a command and control channel. This write up includes a simple python PoC that could be adapted for use with <a href="https://github.com/FSecureLABS/C3" target="_blank">C3</a> or Cobalt Strike's external C2.</li>
<li><a href="https://blog.ret2.io/2021/06/16/intro-to-pac-arm64/" target="_blank">The Oddest Place You Will Ever Find PAC - Exploiting the notoriously unsafe gets() on a PAC-protected ARM64 binary</a>. This is a walk through of bypassing pointer authentication (ARM 8.3 feature seen in iOS). The interactive features of the post are pretty amazing.</li>
<li><a href="https://adepts.of0x.cc/connectionless-shells/" target="_blank">Knock! Knock! The postman is here! (abusing Mailslots and PortKnocking for connectionless shells)</a>. The use of "reverse port knocking" by varying the source port is an interesting tactic, but like the post says, be wary of NATing or other network hops that will interfere with this.</li>
<li><a href="https://redteamer.tips/click-your-shortcut-and-you-got-pwned/" target="_blank">Click your shortcut and… you got pwned.</a>. Up your adversary emulation game with this LNK generator and you too can be NOBELIUM.</li>
<li><a href="https://blog.redxorblue.com/2021/06/introducing-striker-and-payload.html" target="_blank">Introducing Striker and the Payload Automation Libraries</a>. If you have multiple team servers and multiple payloads, the payload generation process can be painful unless automated. The python libraries introduced in this post can help you build your own pipeline.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/CCob/BOF.NET/pull/1" target="_blank">bofnet_executeassembly</a>. If you aren't using BOF.NET you are missing out. With this pull request, there is no excuse as you can drop in standard .NET assemblies and use them without any modification as a BOF. No more fork and run - opsec++. More details in <a href="https://williamknowles.io/bofnet_executeassembly-native-in-process-execution-of-net-assemblies-in-cobalt-strike/" target="_blank">this blog post</a>.</li>
<li><a href="https://github.com/Almorabea/Polkit-exploit" target="_blank">Polkit-exploit</a> is a proof of concept for an authentication bypass on polkit, which allows unprivileged user to call privileged methods using DBus (blog post in LWiS 2021-06-14).</li>
<li><a href="https://github.com/barrracud4/image-upload-exploits" target="_blank">image-upload-exploits</a> is a nice collection of ways to potentially leverage image uploads on web applications for data leaks or even shells!</li>
<li><a href="https://github.com/Mr-B0b/BloodCheck" target="_blank">BloodCheck</a> enables Red and Blue Teams to manage multiple Neo4j databases and run Cypher queries against a BloodHound dataset.</li>
<li><a href="https://github.com/m0rv4i/Syscalls-Extractor" target="_blank">Syscalls-Extractor</a> is a script for automatically extracting syscall numbers for an OS.</li>
<li><a href="https://github.com/emadshanab/admin-login" target="_blank">admin-login</a> is a wordlist of potential admin panels for web app testing.</li>
<li><a href="https://github.com/Sentinel-One/brick" target="_blank">brick</a>  is a small tool designed to identify potentially vulnerable SMM modules in a UEFI firmware image. It is comprised out of a collection of modules (implemented as IDAPython scripts), each responsible for identifying a specific vulnerability/anti-pattern in SMM code.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/kaganisildak/malwarescarecrow" target="_blank">malwarescarecrow</a> is a tool designed to make physical devices detectable by malware and make system look like virtual machine.</li>
<li><a href="https://github.com/CorentinJ/Real-Time-Voice-Cloning" target="_blank">Real-Time-Voice-Cloning</a>. This vishing (voice phishing) implications of this are scary. Imagine calling a supervisor to get audio samples, then using those to train the model and create a script to demand action on a phishing email from an employee. Demo <a href="https://www.youtube.com/watch?v=-O_hYhToKoA" target="_blank">here</a>.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
