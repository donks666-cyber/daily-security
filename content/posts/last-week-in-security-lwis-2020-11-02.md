Title: Last Week in Security (LWiS) - 2020-11-02
Date: 2020-11-02 23:50
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-11-02
Author: Erik
Summary: NAT Slipstreaming by <a href="https://twitter.com/samykamkar" target="_blank">@samykamkar</a>, a new AV evasion method by <a href="https://twitter.com/jxy__s" target="_blank">@jxy__s</a>, Kerberoasting in pure VBA by <a href="https://twitter.com/TheXC3LL" target="_blank">@TheXC3LL</a>, Linux LPE by <a href="https://twitter.com/scannell_simon" target="_blank">@scannell_simon</a>, browser extension vulnerabilities from <a href="https://twitter.com/WPalant" target="_blank">@WPalant</a>, new Maldoc techniques from <a href="https://twitter.com/Matt_Grandy_" target="_blank">@Matt_Grandy_</a>, a new autonomous red team tool from <a href="https://twitter.com/privateducky" target="_blank">@privateducky</a> and team, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-10-26 to 2020-11-02.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.offensive-security.com/pen300-osep/" target="_blank">PEN-300 Evasion Techniques and Breaching Defenses</a> is a new course from Offesnive Security, the company behind the famous OSCP.</li>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2104" target="_blank">Windows Kernel cng.sys pool-based buffer overflow in IOCTL 0x390400</a>. Google's Project Zero discloses a Windows local privilege escalation/sandbox escape vulnerability that is being actively exploited, likely in connection with their previously disclosed heap buffer overflow in Chrome/Freetype. Chained together this could be a very effective "watering hole" attack where browsing to a page causes a target to be implanted.</li>
<li><a href="https://o365blog.com/post/teams-policies/" target="_blank">Abusing Teams client protocol to bypass Teams security policies</a>. Microsoft Teams only enforces protocols (i.e. Guests cannot delete messages) on the client side. Intercepting the client request and server response for settings allows complete bypass of any restrictions.</li>
<li><a href="https://www.prelude.org/" target="_blank">Prelude</a> is a new "autonomous red team tool packaged as a simple, beautiful desktop application." There is a <a href="https://youtu.be/Hz8K-jdqpBY" target="_blank">preview</a> available and it looks very slick. From the minds behind <a href="https://github.com/mitre/caldera" target="_blank">caldera</a>, I have high hopes and will be keeping a close eye on the development of Prelude.</li>
<li><a href="https://public.intel471.com/blog/revil-ransomware-interview-russian-osint-100-million/" target="_blank">Alleged REvil member spills details on group’s ransomware operations</a>. I guess even ransomware crews have leaks. Some notable details include the revenue ($100 Million USD per year), and the fact they run an affiliate program where they pay (up to $8 million) per target.</li>
<li><a href="https://www.fireeye.com/blog/threat-research/2020/10/threatpursuit-vm-threat-intelligence-and-hunting-virtual-machine.html" target="_blank">Welcome to ThreatPursuit VM: A Threat Intelligence and Hunting Virtual Machine</a>. Fireeye keeps the VMs coming with ThreatPursuit. This follows their successful <a href="https://github.com/fireeye/flare-vm" target="_blank">flare-vm</a> and <a href="https://github.com/fireeye/commando-vm" target="_blank">commando-vm</a>. The commitment to automated Windows setup is admirable.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://jxy-s.github.io/herpaderping/" target="_blank">Process Herpaderping</a> is a method of obscuring the intentions of a process by modifying the content on disk after the image has been mapped. This can be used to bypass some (most?) AVs and some file integrity monitoring solutions depending on when and how the perform their checks of files on disk. It can fool Windows Defender into <a href="https://twitter.com/gentilkiwi/status/1321001331755286529" target="_blank">thinking mimikatz is "signed"</a> as well.</li>
<li><a href="https://adepts.of0x.cc/kerberoast-vba-macro/" target="_blank">Hacking in an epistolary way: implementing kerberoast in pure VBA</a>. What if you did every stage of your attack via phishing payloads? VBA is technically <a href="https://en.wikipedia.org/wiki/Turing_completeness" target="_blank">Turing complete</a>, so it is technically possible. This post explores how to Kerberoast in pure VBA. Half amazing, half insane.</li>
<li><a href="https://scannell.me/fuzzing-for-ebpf-jit-bugs-in-the-linux-kernel/" target="_blank">Fuzzing for eBPF JIT bugs in the Linux kernel</a>. This post shows how a a writeup lead a researcher to conduct his own research and in doing so found a new vulnerability in the patch! This local privilege escalation vulnerability affects Linux kernels with the "patched" eBPF verifier before 5.8.15 (starting at 5.6.1, 5.5.14, and 5.4.29). No public PoC yet.</li>
<li><a href="https://palant.info/2020/10/28/what-would-you-risk-for-free-honey/" target="_blank">What would you risk for free Honey?</a>. Browser extensions don't often get the attention they deserve from security professionals. This post exposes some serious issues with the popular "Honey" extension, in this case four different ways the Honey server could run arbitrary code on any website you visit while it is installed.</li>
<li><a href="https://fortynorthsecurity.com/blog/maldoc-fu-some-ideas-for-malicious-document-delivery/" target="_blank">MalDoc Fu - Some Ideas for Malicious Document Delivery</a>. Maldocs (macro enable malicious documents) are a favorite of phishing engagements, but as people and technologies slowly get better, they are becoming less successful. This post explores some new advanced forms of Maldocs to hide your malicious payloads and bypass current AV. Well done!</li>
<li><a href="https://swarm.ptsecurity.com/remote-desktop-services-shadowing/" target="_blank">Remote Desktop Services Shadowing – Beyond the Shadowed Session</a>. RDP Shadowing is the process of connecting to an already open RDP session. This is useful for legitimate purposes, and could be very useful for red team purposes as well. With some registry changes, it can be made silent and red teamers can effectively spy on legitimate RDP sessions.</li>
<li><a href="https://swapcontext.blogspot.com/2020/11/uac-bypasses-from-comautoapprovallist.html" target="_blank">UAC bypasses from COMAutoApprovalList</a> details the two newest additions to <a href="https://github.com/hfiref0x/UACME" target="_blank">UACME</a> that use the Windows COM object model classes with enabled elevation.</li>
<li><a href="https://labs.f-secure.com/blog/print-c2" target="_blank">Using and detecting C2 printer pivoting</a> explores a very interesting "esoteric C2 channel" of using print jobs to communicate on a Windows network.</li>
<li><a href="https://samy.pl/slipstream/" target="_blank">NAT Slipstreaming</a> allows an attacker to remotely access any TCP/UDP service bound to a victim machine, bypassing the victim's NAT/firewall (arbitrary firewall pinhole control), just by the victim visiting a website. The <a href="https://en.wikipedia.org/wiki/Samy_%28computer_worm%29" target="_blank">fastest-spreading virus</a> author is back with more great research. This abuses SIP Application Layer Gateway (maybe enabled by default) and bad packet fragmentation handling to allow browsers to generate what (bad) routers think are arbitrary packets. This allows all kinds of things like opening ports to other internal devices by just having a user run some javascript by browsing a website. Very cool, but possibly limited to sketchy defaults and poor packet fragmentation handling.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/hausec/MaliciousClickOnceMSBuild" target="_blank">MaliciousClickOnceMSBuild</a> is a C# Project that will take an MSBuild payload and run it with MSBuild via ClickOnce. Be aware that without a valid certificate it will trigger a smartscreen warning.</li>
<li><a href="https://github.com/CCob/BOF.NET" target="_blank">BOF.NET</a> is a small native BOF object combined with the BOF.NET managed runtime that enables the development of Cobalt Strike BOFs directly in .NET. BOF.NET removes the complexity of native compilation along with the headaches of manually importing native API. Now you can write your BOFs in .NET instead of C!</li>
<li><a href="https://github.com/Ben0xA/HoneyCreds" target="_blank">HoneyCreds</a> is a network credential injection tool to detect responder and other network poisoners. Set this up with a legitimate looking username and easy to crack password and trigger on any use of the account in your environment.</li>
<li><a href="https://github.com/jas502n/CVE-2020-14882" target="_blank">CVE-2020-14882</a>. Oh boy, a single GET gets unauthenticated remote code execution against Oracle Web Logic. The patch is <a href="https://twitter.com/chybeta/status/1322131143034957826" target="_blank">amazingly poor</a> as well.</li>
<li><a href="https://github.com/mindcollapse/MalwareMultiScan" target="_blank">MalwareMultiScan</a> is a self-hosted VirusTotal / MetaDefender wannabe with API, demo UI and Scanners running in Docker. Like other self-hosted AV scanners, it only runs Linux based AVs (and Windows Defender). This joins <a href="https://github.com/maliceio/malice" target="_blank">malice</a>, <a href="https://github.com/saferwall/saferwall" target="_blank">saferwall</a>, and <a href="https://github.com/jampe/MultiAV-Extended" target="_blank">MultiAV-Extended</a> for self hosted AV scanning solutions.</li>
<li><a href="https://github.com/bohops/UltimateWDACBypassList" target="_blank">UltimateWDACBypassList</a> is a centralized resource for previously documented WDAC/Device Guard/UMCI bypass techniques.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/dendronhq/dendron" target="_blank">dendron</a> is a local-first, markdown based, hierarchical note-taking application built on top of VSCode and friends. Similar to <a href="https://obsidian.md/" target="_blank">Obsidian</a> or <a href="https://roamresearch.com/" target="_blank">Roam</a>, but open source and free.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
