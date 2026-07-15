Title: Last Week in Security (LWiS) - 2021-04-26
Date: 2021-04-27 19:25
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-04-26
Author: Erik
Summary: New APIs/syscalls for EDR bypass (<a href="https://twitter.com/yarden_shafir" target="_blank">@yarden_shafir</a>), UAF browser exploit dev (<a href="https://twitter.com/33y0re" target="_blank">@33y0re</a>), PowerView replacement [EDD] (<a href="https://twitter.com/FortyNorthSec" target="_blank">@FortyNorthSec</a>), phishing banner defeat (<a href="https://twitter.com/whynotsecurity" target="_blank">@whynotsecurity</a>), packer teardown (<a href="https://twitter.com/fumik0_" target="_blank">@fumik0_</a>), NANDcromancy (<a href="https://twitter.com/atredis" target="_blank">@Atredis</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-04-19 to 2021-04-26.</p>
<aside class="m-note m-warning">
<h3>Delay</h3>
<p>Sorry for the delay, an initial beacon came in for a new assessment late Monday night.</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://portswigger.net/daily-swig/ill-advised-research-on-linux-kernel-lands-computer-scientists-in-hot-water" target="_blank">Ill-advised research on Linux kernel lands computer scientists in hot water</a>. Researchers from the University of Minnesota purposely introduced bugs into the Linux Kernel as part of a study on the potential to introduce bugs into open source projects. I'm not sure why this was necessary as plenty of real bugs are already committed to open source projects, including the Linux kernel, that result in exploitable bugs. Linux maintainers responded, appropriately, by banning any contributions from a University of Minnesota email account. The researchers have issued  <a href="https://lore.kernel.org/lkml/CAK8KejpUVLxmqp026JY7x5GzHU2YJLPU8SzTZUNXU2OXC70ZQQ@mail.gmail.com/" target="_blank">an open letter to the Linux community</a>, but the damage has been done.</li>
<li><a href="https://brew.sh/2021/04/21/security-incident-disclosure/" target="_blank">Security Incident Disclosure (Brew)</a>. Due to a way the Brew project's (package manager) GitHub actions were configured, it was possible to hide code from <cite>git_diff</cite> which would trick the auto-merge action into thinking only the version number was updated. This would allow an attacker to add malicious code to any Brew package without any human review. The issue has been fixed by disabling the automerge action as well as other steps including manual review.</li>
<li><a href="https://www.theregister.com/2021/04/25/dan_kaminsky_obituary/" target="_blank">Computer security world in mourning over death of Dan Kaminsky, aged 42</a>. A star in the infosec community, Dan most famously worked to fix <a href="https://www.kb.cert.org/vuls/id/800113" target="_blank">multiple DNS implementations vulnerable to cache poisoning</a>, gave multiple Blackhat and DEF CON talks, and was generally just a good person. His loss at a young age (due to diabetic ketoacidosis) is a reminder to step away from the keyboard and enjoy life.</li>
<li><a href="https://tmpout.sh/1/" target="_blank">tmp.0ut Volume 1</a> is an homage to classic hacker zines packed full of great ELF knowledge.</li>
<li><a href="https://medium.com/cloud-security/google-chrome-dns-security-bypass-9a1e10e02114" target="_blank">Google Chrome DNS Security Bypass</a>. A Chrome "feature" called Async-DNS will perform DNS lookups to Google's DNS servers regardless of how the host is configured. This post also includes ways to disable this on Windows and macOS (add the <cite>--disable-async-dns</cite> flag to the command line), as it could prevent DNS based defenses or logging. If you rely on an internal DNS server, blocking UDP 53 outbound on your firewall is a temporary solution until Google starts using DNS-over-HTTPS for this "feature." Switching to Firefox is a permanent solution.</li>
<li><a href="https://www.bleepingcomputer.com/news/security/revil-gang-tries-to-extort-apple-threatens-to-sell-stolen-blueprints/" target="_blank">REvil gang tries to extort Apple, threatens to sell stolen blueprints</a>. Two interesting pieces of this story: The the stolen blueprints seem to <a href="https://www.macrumors.com/2021/04/21/macbook-pro-stolen-schematics-ports/" target="_blank">confirm Apple's plans to add more ports and remove touch bar</a> (all power users are happy about this), and the ransom is requested not it Bitcoin but in a much lesser known cryptocurrency called Monero which has true privacy.</li>
<li><a href="https://blog.cloudflare.com/project-jengo-redux-cloudflares-prior-art-search-bounty-returns/" target="_blank">Project Jengo Redux: Cloudflare’s Prior Art Search Bounty Returns</a>. Patent trolls are a symptom of a broken patent system, but Cloudflare's response to them is fantastic. A $100,000 bounty to invalidate the patents used by the trolls is a solution that can have positive outcome for Cloudflare and generate some publicity about this flaw in the patent system.</li>
<li><a href="https://www.clickstudios.com.au/advisories/Incident_Management_Advisory-01-20210424.pdf" target="_blank">clickstudios Passwordstate Incident Management Advisory #01</a>. Supply chain attacks are here to stay, and what better software to hijack an update for than a password manager? Any critical systems should be protected by FIDO2 (U2F) hardware tokens. FIDO2 keys are a one-time investment that can save untold amounts of damage later on.</li>
<li><a href="https://signal.org/blog/cellebrite-vulnerabilities/" target="_blank">Exploiting vulnerabilities in Cellebrite UFED and Physical Analyzer from an app's perspective</a>. Despite the questionable cryptocurrency moves, Signal proves it still has edge with this shade-ridden post about possibly, maybe, definitely including some Cellebrite parser 0days in a random selection of Signal user's devices. Interesting to see if this plays out in court with evidence rejected as it may have been tampered with or deleted by one of these exploits. Is it enough to cast doubt on any user's Signal data collected with Cellebrite?</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://windows-internals.com/thread-and-process-state-change/" target="_blank">Thread and Process State Change</a>. A new Windows insider build added some APIs and syscalls to suspend and resume threads. This created new opportunities to sneakily handle some of the most monitored parts of process injection on Windows. Example code included at the end of the post.</li>
<li><a href="https://fumik0.com/2021/04/24/anatomy-of-a-simple-and-popular-packer/" target="_blank">Anatomy of a simple and popular packer</a>. Curious how popular packers are used to deliver "main stream" malware? This post tears apart <a href="https://www.virustotal.com/gui/file/10192ceb4aa066216989c2b83dd3b460f0264d6672f64d1dff2addbe07fb1a5a/detection" target="_blank">Ficker Stealer</a> and exposes the tricks it uses. Some of these techniques may be useful in your next adversary emulation engagement.</li>
<li><a href="https://blog.sektor7.net/#!res/2021/perunsfart.md" target="_blank">Perun's Fart - yet another unhooking method</a>. While many unhooking methods read a fresh copy of ntdll.dll from disk, this method simply starts a new process in a suspended state and copies ntdll.dll from that process which has no hooks as it has not started execution yet.</li>
<li><a href="https://0xhop.github.io/" target="_blank">AV Evasion Part 1</a>. This post covers some basic AV evasion. If you are new to the game, this is a good place to start.</li>
<li><a href="https://www.atredis.com/blog/2021/4/23/live-nand-swap" target="_blank">NANDcromancy: Live Swapping NAND Flash</a>. This is true hardware hacking sorcery. Replacing a NAND chip while a device is powered on is some next level hardware hacking.</li>
<li><a href="https://connormcgarr.github.io/browser1/" target="_blank">Exploit Development: Browser Exploitation on Windows - Understanding Use-After-Free Vulnerabilities</a>. This post is a full start to finish walkthrough of a use-after-free bug in IE 8 on Windows 7 x86 from crash, to vulnerability identification, to shell. Careful Connor, any more complete and SANS will charge $7,500 a week for this.</li>
<li><a href="https://objective-see.com/blog/blog_0x64.html" target="_blank">All Your Macs Are Belong To Us: bypassing macOS's file quarantine, gatekeeper, and notarization requirements</a>. This now patched technique was found in the wild (0day) and managed to bypass all the protections put in place since 2015 to keep users from infecting themselves. Some times you have to test assumptions about security products to find a bypass. Just because something should never work, doesn't mean it won't.</li>
<li><a href="https://labs.sentinelone.com/relaying-potatoes-dce-rpc-ntlm-relay-eop/" target="_blank">Relaying Potatoes: Another Unexpected Privilege Escalation Vulnerability in Windows RPC Protocol</a>. Potato exploits refuse to die, and in a special circumstance (you have a shell in session 0 and a Domain Admin has a shell in session 1) <a href="https://github.com/antonioCoco/RemotePotato0" target="_blank">RemotePotato0</a> can escalate you to Domain Admin. Best/Worst of all, Microsoft labeled this a "won't fix."</li>
<li><a href="https://www.trustedsec.com/blog/azure-application-proxy-c2/" target="_blank">Azure Application Proxy C2</a>. With Azure killing domain fronting, these types of "proxy C2" will become more popular.</li>
<li><a href="https://whynotsecurity.com/blog/external-email-warning-bypass/" target="_blank">MS External Email Warning Bypass</a>. When you put banners into user controlled HTML, you're going to have a bad time. Pro tip: look for the specific inserted HTML in a reply before you craft your defeat for your specific target.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/TheWover/CertStealer" target="_blank">CertStealer</a> is a .NET tool for stealing and importing certificates in the Windows certificate store without touching disk. Useful for red team operations where you need to poach a certificate for pivoting purposes and want to do so with an in-memory post-ex payload.</li>
<li><a href="https://github.com/juliourena/SharpNoPSExec" target="_blank">SharpNoPSExec</a> is a fileless lateral movement tool that will query all services and randomly pick one with a start type disable or manual, the current status stopped and with LocalSystem privileges to reuse them. Once it select the service it will save its current state, replace the binary path with the payload of your choice and execute it. After waiting 5 seconds it will restore the service configuration.</li>
<li><a href="https://fortynorthsecurity.com/blog/meet-edd-he-helps-enumerate-domain-data/" target="_blank">Meet EDD - He Helps Enumerate Domain Data</a>. EDD is a .NET tool to enumerate Windows domain designed to be similar to the now unmaintained PowerView.</li>
<li><a href="https://github.com/itm4n/PPLdump" target="_blank">PPLdump</a> is a tool that implements a userland exploit that was initially discussed by James Forshaw (a.k.a. <a href="https://twitter.com/tiraniddo" target="_blank">@tiraniddo</a>) - in this <a href="https://googleprojectzero.blogspot.com/2018/08/windows-exploitation-tricks-exploiting.html" target="_blank">blog post</a> - for dumping the memory of any PPL as an administrator.</li>
<li><a href="https://github.com/hfiref0x/AsIo3Unlock" target="_blank">AsIo3Unlock</a> is a proof-of-concept bypass of pseudo-security caller check implemented in AsIO3, "unlocking" this driver for usage with FULL R/W access.</li>
<li><a href="https://github.com/ExAndroidDev/fakemeeting" target="_blank">fakemeeting</a> is a tool for creating fake meeting invites. More details <a href="https://www.exandroid.dev/2021/04/24/phishing-with-fake-meeting-invite/" target="_blank">here</a>.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/lawiet47/STFUEDR" target="_blank">STFUEDR</a>. Everyone knows that userland hooks can be defeated, but some EDRs use drivers and kernel hooks. This project uses a driver signing bypass to defeat even those hooks!</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
