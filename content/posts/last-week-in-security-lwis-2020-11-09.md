Title: Last Week in Security (LWiS) - 2020-11-09
Date: 2020-11-10 15:30
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-11-09
Author: Erik
Summary: New Mythic agent (<a href="https://twitter.com/djhohnstein" target="_blank">@djhohnstein</a>), mobile app interception tools (<a href="https://twitter.com/EvilPenguin_" target="_blank">@EvilPenguin_</a>), CobaltStrike 4.2 and C2 docs (<a href="https://twitter.com/AndrewChiles" target="_blank">@AndrewChiles</a>), AD post-ex toolkit (<a href="https://twitter.com/FuzzySec" target="_blank">@FuzzySec</a>), proxy awareness for CS (<a href="https://twitter.com/lefterispan" target="_blank">@lefterispan</a>), user-mode unhooking ( <a href="https://twitter.com/slaeryan" target="_blank">@slaeryan</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-11-02 to 2020-11-09.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.fireeye.com/blog/threat-research/2020/11/live-off-the-land-an-overview-of-unc1945.html" target="_blank">Live off the Land? How About Bringing Your Own Island? An Overview of UNC1945</a>. Linux based APTs don't get much attention, and APTs that target Solaris, even less - until now. Mandiant exposes all the tricks of an APT group that used a Solaris SSH 0day for initial access, and deployed quite a suite of tools (including an entire QEMU VM) once in the network.</li>
<li><a href="https://www.raspberrypi.org/products/raspberry-pi-400/" target="_blank">Raspberry Pi 400 launched</a>. This new Raspberry Pi introduces a new form factor, the computer-as-a-keyboard. A new board incorporates the Raspberry Pi 4 (4GB) into a small keyboard. One notable change is a slightly updated processor with a 1.8 GHz quad-core ARMv8 chip (vs 1.5 GHz in the standard 4), and a massive heatsink to keep it from overheating. With its ability to run dual 4k displays, this portable computer could be perfect for students or anyone who needs a basic computing environment. I am also interested to see it being used as a thin client device.</li>
<li><a href="https://www.chromium.org/Home/chromium-security/root-ca-policy" target="_blank">Chrome Root Program</a>. Chrome will start shipping its own root Certification Authorities (CA) store instead of relying on the operating system's CA store. Mozilla already does this in Firefox, and it will present challenges to enterprises that deploy their own root CAs for HTTPS interception or other purposes.</li>
<li><a href="https://www.ic3.gov/Media/News/2020/201103-3.pdf" target="_blank">Cyber ActorsTarget Misconfigured SonarQube Instances to Access Proprietary Source Code of US Government Agencies and Businesses</a>. The FBI reveals that threat actors have stolen private and US Government source code due to misconfigurations in SonarQube instances. This is a great example of why having a government backdoor "only for the good guys" is a terrible idea.</li>
<li><a href="https://blog.cobaltstrike.com/2020/11/06/cobalt-strike-4-2-everything-but-the-kitchen-sink/" target="_blank">Cobalt Strike 4.2 – Everything but the kitchen sink</a> details the improvements in the most recent release of the commercial red team tool. Many are welcome quality of life additions (better key logging and screenshot support), but there is also good low level improvements for in-memory evasion and templates for artifacts the the named-pipe beacon uses to communicate with post-exploitation jobs. ThreatExpress has the latest malleable C2 additions <a href="https://github.com/threatexpress/malleable-c2" target="_blank">documented nicely</a>.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://0xpat.github.io/Malware_development_part_5/" target="_blank">Malware development part 5</a>. This is a continuation of a great series on malware (or red team tool) development. This one covers parent PID spoofing, process protection, environmental keying and bruteforce decryption of malware data and configuration.</li>
<li><a href="https://blog.qsecure.com.cy/posts/traditional-signature-based-antivirus-evasion-tests/" target="_blank">Traditional Signature Based Antivirus Evasion Tests</a>. Simple string manipulation is good enough to get a ~50% reduction in detections on virus total. Not bad.</li>
<li><a href="https://labs.sentinelone.com/resourceful-macos-malware-hides-in-named-fork/" target="_blank">Resourceful macOS Malware Hides in Named Fork</a>. Named Forks are the alternate data streams (ADS) of the macOS world, and just like ADSs on Windows, they will be abused by malware to hide payloads. This post shows the full chain from download to execution. The helpful icons for gatekeeper bypass could prove useful for your next macOS phishing engagement.</li>
<li><a href="https://posts.specterops.io/sharing-the-myth-d14eb1b4fc23" target="_blank">Sharing the Myth</a>. Apfell became Mythic a few months ago, and it is an impressive framework. This post shows how it is architected and introduced a C# agent called <a href="https://github.com/MythicAgents/Apollo" target="_blank">Apollo</a>.</li>
<li><a href="https://heynowyouseeme.blogspot.com/2020/11/privileged-arbitrary-file-read-cve-2020.html" target="_blank">Privileged arbitrary file read (CVE-2020-16938) with The Sleuth Kit</a>. This regression in Windows 10 2004 allows any user to access any file on the system, but only via raw NTFS. 7zip was used in the <a href="https://twitter.com/jonasLyk/status/1316104870987010048" target="_blank">original PoC</a>, and a <a href="https://github.com/ioncodes/CVE-2020-16938" target="_blank">native PoC exists</a>, but this post shows how to "exploit" this bug using The Sleuth Kit binaries.</li>
<li><a href="https://www.ired.team/offensive-security/code-injection-process-injection/writing-custom-shellcode-encoders-and-decoders" target="_blank">Writing Custom Shellcode Encoders and Decoders</a>. At some point you will likely have to use some shellcode on target. Encode or encrypt it to make defender's jobs a little harder and bypass static signatures.</li>
<li><a href="https://offensivedefence.co.uk/posts/covenant-profiles-templates/" target="_blank">Using Custom Covenant Listener Profiles &amp; Grunt Templates to Elude AV</a>. Covenant is a great C2, but its default Grunts are well signatured. This post shows how to do some basic modifications to change the signatures a bit.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/EncodeGroup/AggressiveProxy" target="_blank">AggressiveProxy</a> is a combination of a .NET 3.5 binary (LetMeOutSharp) and a Cobalt Strike aggressor script (AggressiveProxy.cna). Once LetMeOutSharp is executed on a workstation, it will try to enumerate all available proxy configurations and try to communicate with the Cobalt Strike server over HTTP(s) using the identified proxy configurations. The story behind the tool can be found <a href="https://medium.com/encode-threat-labs/aggressiveproxy-a-tale-of-two-proxies-and-a-sad-beacon-43042a04a0d0" target="_blank">here</a>.</li>
<li><a href="https://github.com/slaeryan/AQUARMOURY/tree/master/Shellycoat" target="_blank">Shellycoat</a> is a utility designed to aid in bypassing User-Mode hooks utilized by AV/NGAV/EDR/Sandboxes/DLP etc. to gain visibility into potentially suspicious actions. It is a DLL or PIC shellcode blob that can be injected into a process and will "clean" that processes ntdll using direct syscalls to remove any hooks. Use this with a custom loader before executing your malicious payload to bypass AV.</li>
<li><a href="https://github.com/xforcered/StandIn" target="_blank">StandIn</a> is a "small" AD post-compromise toolkit. It allows for all kinds of enumeration including LDAP objects, ASREP, SPNs, Unconstrained/constrained delegation, DC's, Groups Operations, and Machine Object Operations.</li>
<li><a href="https://blog.didierstevens.com/2020/11/07/1768-k/" target="_blank">1768 K</a> is a tool to decode and dump the configuration of Cobalt Strike beacons from memory from the great Didier Stevens (1768 Kelvin is the melting point of Cobalt).</li>
<li><a href="https://github.com/lightspin-tech/red-kube" target="_blank">red-kube</a> is a red team cheat sheet based on kubectl commands. As more things get containerized, it's good to know how to break k8s.</li>
<li><a href="https://github.com/evilpenguin/APKProxyHelper" target="_blank">APKProxyHelper</a> patches an apk for proxying and repacks back to an apk. For iOS the author has a tweak called <a href="https://github.com/evilpenguin/SSLBypass" target="_blank">SSLBypass</a> that does what it says on the tin.</li>
<li><a href="https://github.com/Mr-Un1k0d3r/SCShell/tree/master/CS-BOF" target="_blank">SCShell</a> now comes with a Cobalt Strike BOF. Fileless lateral movement was never as easy!</li>
<li><a href="https://legalhackers.com/advisories/Git-LFS-RCE-Exploit-CVE-2020-27955.html" target="_blank">Git Large File Storage / Git LFS (git-lfs) - Remote Code Execution (RCE)</a>. It's been a while since we heard from Dawid Golunski (3 years?), but he is back with a RCE that can be triggered by a <cite>git clone</cite> command. Demo <a href="https://youtu.be/tlptOf9w274" target="_blank">here</a>.</li>
<li><a href="https://github.com/hot3eed/xpcspy" target="_blank">xpcspy</a> implements bidirectional XPC message interception for iOS and macOS.</li>
<li><a href="https://github.com/hackerschoice/gsocket" target="_blank">gsocket</a> is an end-to-end encrypted relay network that allows for advanced features beyond simple TCP and SFTP, like mounting a remote file system. As of now, self-hosting a relay is not an option and all traffic goes through <cite>gs.thc.org</cite>. Perhaps it's an elaborate honey pot?!</li>
<li><a href="https://github.com/redcode-labs/Coldfire" target="_blank">Coldfire</a> is a Go malware development framework that includes a lot of the basic functions all good malware needs, from logging to sandbox detection.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/C-Sto/gosecretsdump" target="_blank">gosecretsdump</a>. Impacket is great, but sometimes it can be really slow. When your NTDS.dit file is measured in GBs, it's time to break out the Go for significant speed boost. Also works on SAM/SYSTEM backups, or even local SAM/SYSTEM if run as SYSTEM.</li>
<li><a href="https://github.com/tomnomnom/gron" target="_blank">gron</a> transforms JSON into discrete assignments to make it easier to grep for what you want and see the absolute 'path' to it. It eases the exploration of APIs that return large blobs of JSON but have terrible documentation. It may fill gaps that <a href="https://stedolan.github.io/jq/" target="_blank">jq</a> can't in your workflow.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
