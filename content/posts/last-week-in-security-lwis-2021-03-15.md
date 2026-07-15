Title: Last Week in Security (LWiS) - 2021-03-15
Date: 2021-03-15 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-03-15
Author: Erik
Summary: Bloodhound Enterprise (<a href="https://twitter.com/_wald0" target="_blank">@_wald0</a>), reproducing ProxyLogon (<a href="https://twitter.com/amlweems" target="_blank">@amlweems</a>), Wireshark 1-click RCE (<a href="https://twitter.com/positive_sec" target="_blank">@positive_sec</a>), free IOC API (<a href="https://twitter.com/abuse_ch" target="_blank">@abuse_ch</a>), VM detection trick (<a href="https://twitter.com/gsuberland" target="_blank">@gsuberland</a>), IoT 🐚s via PCI (<a href="https://twitter.com/_p0ly_" target="_blank">@_p0ly_</a>), opensource AirTags (<a href="https://twitter.com/Sn0wfreeze" target="_blank">@Sn0wfreeze</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-03-08 to 2021-03-15.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><dl>
<dt>Proxylogin fallout</dt>
<dd><ul>
<li><a href="https://www.praetorian.com/blog/reproducing-proxylogon-exploit/" target="_blank">Reproducing the Microsoft Exchange Proxylogon Exploit Chain</a>. If you're wondering how hard it would be to generate an in-house version of Proxylogon using just the patches and public information, look no further. This post is full of technical details and the steps the Praetorian team took to recreate the exploit chain. This is an excellent resource for aspiring n-day writers. A PoC based on this article is <a href="https://github.com/alt3kx/CVE-2021-26855_PoC" target="_blank">available on Github</a>.</li>
<li><a href="https://github.com/sophoslabs/metasploit_gather_exchange" target="_blank">metasploit_gather_exchange</a> is a metasploit framework module for gathering information from an Exchange Server via powershell to list and export mailboxes as pst files. Details in this <a href="https://news.sophos.com/en-us/2021/03/09/sophoslabs-offensive-security-releases-post-exploitation-tool-for-exchange/" target="_blank">blog post</a>.</li>
<li><a href="https://msrc-blog.microsoft.com/2021/03/15/one-click-microsoft-exchange-on-premises-mitigation-tool-march-2021/" target="_blank">One-Click Microsoft Exchange On-Premises Mitigation Tool – March 2021</a>. This official tool from Microsoft shows the severity of the issue. Unfortunately it is very likely too late for any vulnerable instances. I suppose if there was <a href="https://twitter.com/irsdl/status/1367006759521579010" target="_blank">suspicion that Microsoft somehow leaked the exploit</a> I would be trying to make it easy to mitigate the vulnerabilities too...</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://specterops.io/bloodhound-enterprise" target="_blank">Bloodhound Enterprise</a>. From the creators of BloodHound, a SaaS technology that continuously identifies and quantifies the most critical Active Directory choke points. Measurable, practical remediation guidance enables the elimination of millions of attack paths within your existing Active Directory architecture. The product is scheduled for release this summer (2021) and I am excited to see it help organizations lock down their AD environment.</li>
<li><a href="https://www.theregister.com/2021/03/10/ovh_strasbourg_fire/" target="_blank">OVH data centre destroyed by fire in Strasbourg – all services unavailable</a>. This is your weekly reminder that the cloud is just someone else's computer. Backups still matter!</li>
<li><a href="https://security.googleblog.com/2021/03/introducing-sigstore-easy-code-signing.html" target="_blank">Introducing sigstore: Easy Code Signing &amp; Verification for Supply Chain Integrity</a>. Let's Encrypt but for code signing. Most importantly: "sigstore will be free to use for all developers and software providers, with sigstore’s code and operation tooling being 100% open source." This is a good step that I hope lots of developers use. Imagine being able to subscribe to a monitor service for all the dependancies in your project. The transparency may also provides an OSINT opportunity for red teams. You can monitor the progress of the tools <a href="https://github.com/sigstore" target="_blank">on GitHub</a>.</li>
<li><a href="https://www.vice.com/en/article/y3g8wb/hacker-got-my-texts-16-dollars-sakari-netnumber" target="_blank">A Hacker Got All My Texts for $16</a>. A layered network of providers eventually allows the complete re-routing of SMS messages, with no verification or notification to the end user (since fixed by the one provider tested). The fact that 3 separate companies were involved means that there are APIs that allow this with no verification. What would it take for an attacker to either find a new provider that does not do verification or create their own to gain access to the APIs? If a services offers app based (or better, hardware key based) multifactor authentication, choose it over SMS every time.</li>
<li><a href="https://arxiv.org/pdf/2103.02282.pdf" target="_blank">Who Can Find My Devices? Security and Privacy of Apple’s Crowd-Sourced Bluetooth Location Tracking System</a>. This report on the closed source tracking system (and upcoming AirTags) that will help locate lost devices by using every Apple device with Bluetooth as a global sensor has some flaws. However, it's clear that care was taken in the design to preserve privacy more so than other similar systems (e.g. Tile). Don't want to wait for AirTags? Build your own now using <a href="https://github.com/seemoo-lab/openhaystack" target="_blank">openhaystack</a>. Due to the private design of the Apple system, it will be hard (impossible?) to prevent this kind of third party use.</li>
<li><a href="https://abuse.ch/blog/introducing-threatfox/" target="_blank">Introducing ThreatFox</a>. ThreatFox is a community driven project from the creator of abuse.ch and MalwareBazaar where security researchers and threat analysts can share indicators of compromise (IOCs) with the infosec community for free, and without the need of a registration.</li>
<li><a href="https://www.fortinet.com/blog/threat-research/netbounce-threat-actor-tries-bold-approach-to-evade-detection" target="_blank">Whitelist Me, Maybe? “Netbounce” Threat Actor Tries A Bold Approach To Evade Detection</a>. Imagine being so confident in your malware, you email it directly to one of the 2 vendors that have marked you malicious in VirusTotal and ask to be whitelisted. No such luck this time, but how many times has it worked?</li>
<li><a href="https://security.googleblog.com/2021/03/a-spectre-proof-of-concept-for-spectre.html" target="_blank">A Spectre proof-of-concept for a Spectre-proof web</a>. It's pretty wild that the Google team managed to get Spectre working via Javascript in a sandboxed browser, but perhaps the most interesting bit of this post is, "in our tests the attack was successful on several other processors, including the Apple M1 ARM CPU, without any major changes."</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://devilinside.me/blogs/reproducing-ndays-qiling" target="_blank">Reproducing n-day vulnerabilities and writing N-day based fuzzer with Qiling</a>. The techniques in this post can be used to start your own fuzzing, and the existence of one bug means more could be hiding in adjacent functions.</li>
<li><a href="https://gitlab.com/wireshark/wireshark/-/issues/17232" target="_blank">Code execution in Wireshark via non-http(s) schemes in URL fields</a>. Ever wanted to phish a defender or incident responder? Some protocol handlers in Wireshark can be used to get 1-click remote code execution.</li>
<li><a href="https://research.nccgroup.com/2021/03/10/technical-advisory-dell-supportassist-local-privilege-escalation-cve-202-21518/" target="_blank">Technical Advisory: Dell SupportAssist Local Privilege Escalation (CVE-2021-21518)</a>. DLL hijacking will likely never die on Windows, and this post shows how it can be exploited for local privilege escalation. This specific vulnerability only affects systems with Dell SupportAssit 3.7 or greater distributed in a 3 month window in the fall of 2020.</li>
<li><a href="https://labs.nettitude.com/blog/vm-detection-tricks-part-2-driver-thread-fingerprinting/" target="_blank">VM Detection Tricks, Part 2: Driver Thread Fingerprinting</a>. Grahm Sutherland is back with another VM detection trick, this time a way to use tread information to detect if HyperV's vmbus driver is loaded. This technique could be used generally to detect any driver that spawns multiple threads without any suspicious queries. The PoC is <a href="https://github.com/nettitude/hyperv-driver-thread-detection-poc" target="_blank">on github</a>.</li>
<li><a href="https://www.synacktiv.com//en/publications/dumping-the-sonos-one-smart-speaker.html" target="_blank">Dumping the Sonos One smart speaker</a>. Getting root shells on IoT hardware via UART and JTAG: tired. Getting shells via PCI direct memory access attacks: wired. Using the wifi card's mini-PCI connection David Berard is able to not only dump the running kernel, but modify it to get a shell.</li>
<li><a href="https://posts.specterops.io/abstracting-scheduled-tasks-3b6451f6a1c5" target="_blank">Abstracting Scheduled Tasks</a>. How many ways are there to schedule tasks on Windows? Lots.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://www.openwall.com/lists/oss-security/2021/03/09/3" target="_blank">git: malicious repositories can execute remote code while cloning</a>. As someone who clones a lot of git repos, this one is personal. From the advisory: On case-insensitive filesystems, with support for symbolic links, if Git is configured globally to apply delay-capable clean/smudge filters (such as Git LFS), Git could be fooled into running remote code during a clone. Update your git clients! Windows has LFS enabled by default and is vulnerable (other OSs have to enable LFS). This is also not the first git LFS vulnerability (see <a href="https://exploitbox.io/vuln/Git-Git-LFS-RCE-Exploit-CVE-2020-27955.html" target="_blank">CVE-2020-27955</a>).</li>
<li><a href="https://github.com/grimm-co/NotQuite0DayFriday/tree/trunk/2021.03.12-linux-iscsi" target="_blank">Three distinct vulnerabilities discovered by GRIMM while researching the Linux kernel combine as LPE</a>. A kernel pointer leak plus a heap buffer overflow allows for local privilege escalation on modern Linux (RHEL 8.1-8.3).</li>
<li><a href="https://github.com/p3nt4/RunDLL.Net" target="_blank">RunDLL.Net</a> is a project to execute .Net assemblies using Rundll32.exe.</li>
<li><a href="https://github.com/SecIdiot/FOLIAGE" target="_blank">FOLIAGE</a>. This is an interesting project that implements a DNS-over-HTTPS persistence stager with memory obfuscation a la <a href="https://github.com/JLospinoso/gargoyle" target="_blank">gargoyle</a>. This project uses NtContinue as the "gadget" which gets around argument limits to manipulate the return address to NtTestAlert() which allows the code to run the next time it is called.</li>
<li><a href="https://github.com/latortuga71/DisablePPLDriverPoc" target="_blank">DisablePPLDriverPoc</a> is a custom driver to disable protected process light and dump lsass. The driver is not signed, so it must be loaded via a driver signing bypass to work.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Yardanico/cosmonim" target="_blank">cosmonim</a> is a simple example to show how can you use <a href="https://github.com/jart/cosmopolitan" target="_blank">cosmopolitan</a> with Nim. Could this be used to write the ultimate cross platform dropper for those cases where an exploit could land you on a Windows or Linux machine?</li>
<li><a href="https://github.com/harporoeder/ebpfsnitch" target="_blank">ebpfsnitch</a> is a Linux Application Level Firewall based on eBPF and NFQUEUE. It is inspired by <a href="https://github.com/evilsocket/opensnitch" target="_blank">opensnitch</a> and <a href="https://douaneapp.com/" target="_blank">Douane</a> but utilizing modern kernel abstractions - without a kernel module.</li>
<li><a href="https://github.com/sombralibre/http_bridge" target="_blank">http_bridge</a> is a client that allows for socks5 proxying over standard HTTP verbs (no CONNECT) through a Linux server running PHP. Similar to <a href="https://github.com/cbeuw/Cloak" target="_blank">Cloak</a>.</li>
<li><a href="https://github.com/nodauf/Go-RouterSocks" target="_blank">Go-RouterSocks</a> managing multiple <a href="https://github.com/jpillora/chisel" target="_blank">chisel</a> sessions can be a pain. This tool exposes a single socks5 proxy port, and allows dynamic routing of networks to specific chisel sessions.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
