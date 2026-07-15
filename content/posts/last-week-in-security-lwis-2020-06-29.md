Title: Last Week in Security (LWiS) - 2020-06-29
Date: 2020-06-29 13:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-06-29
Author: Erik
Summary: 1,566 hijackable DLLs in Windows 10 from <a href="https://twitter.com/wietze" target="_blank">@Wietze</a>, a Bitdefender RCE from visiting a website by <a href="https://twitter.com/WPalant" target="_blank">@WPalant</a>, CobaltStrike Beacon Object File implementations start dropping (like <a href="https://twitter.com/ilove2pwn_" target="_blank">@ilove2pwn_</a>'s), a Docker Desktop for Windows LPE from <a href="https://twitter.com/spaceraccoonsec" target="_blank">@spaceraccoonsec</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-06-22 to 2020-06-29.
MITRE ATT&amp;CK techniques are in brackets where appropriate.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><dl>
<dt><a href="https://blog.cobaltstrike.com/2020/06/25/cobalt-strike-4-1-the-mark-of-injection/" target="_blank">Cobalt Strike 4.1 – The Mark of Injection</a>. The beacon object files feature teased last week has been released along with improved safe-inject and more tunable SMB and TCP traffic parameters to defeat signature based detections.</dt>
<dd><ul>
<li><a href="https://github.com/realoriginal/bof-NetworkServiceEscalate/tree/master/source" target="_blank">bof-NetworkServiceEscalate</a> is one of the first useful Beacon Object File implementations released. Expect more soon!</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://www.macrumors.com/roundup/wwdc/" target="_blank">2020 Worldwide Developers Conference</a>. Apple announced a lot, but the big news was the 2-year transition of macOS to custom ARM chips. iOS exploit developers just got a whole new target space! The A12X powered Developer Transition Kits (ARM based Mac Mini) have started to arrive, and it's only a matter of time before security researchers get their hands on some.</li>
<li><a href="https://lists.zx2c4.com/pipermail/wireguard/2020-June/005588.html" target="_blank">WireGuard Merged Into OpenBSD</a>. Get ready for native WireGuard in the kernel in pfSense and OPNSense firewalls.</li>
<li><a href="https://www.amnesty.org/en/latest/research/2020/06/moroccan-journalist-targeted-with-network-injection-attacks-using-nso-groups-tools/" target="_blank">Moroccan Journalist Targeted With Network Injection Attacks Using NSO Group’s Tools</a>. "Network Injection" attacks and rouge cell towers, this thorough report from Amnesty International lays out in detail how NSO Group assisted the Moroccan government in performing exploitation of journalists. The evidence of NSO Group willfully ignoring how its products are used is mounting, and I wouldn't be surprised if they are next up on <a href="https://www.vice.com/en_us/article/vb5agy/phineas-fisher-offers-dollar100000-bounty-for-hacks-against-banks-and-oil-companies" target="_blank">Phineas Fisher's</a> hit list.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://www.trustedsec.com/blog/msbuild-a-profitable-sidekick/" target="_blank">MSBuild: A Profitable Sidekick!</a> If you aren't familiar with MSBuild for application whitelisting bypass this post shows its power and gives a real-life example of its usage in a network.</li>
<li><a href="https://www.contextis.com/us/blog/zoom-in-simulated-targeted-attacks" target="_blank">Zoom In: Emulating 'Exploit Purchase' in Simulated Targeted Attacks</a>. The title buries the lead; the team at context found a local privilege escalation 0day in a Zoom service installed by default on Windows, effectively exploited it, and responsibly disclosed it. The post shares details of how they found the 0day but cuts off before they give any juicy details of how they weaponized it. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><a href="https://www.wietzebeukema.nl/blog/hijacking-dlls-in-windows" target="_blank">Hijacking DLLs in Windows</a>. DLL Hijacking is nothing new, but this post shows how useful it still is. Windows 10 v1909 has 1,566 potentially hijackable entries for a base install. Impressive. <a href="https://twitter.com/wietze" target="_blank">@Wietze</a> also includes prevention and detection steps. [<a class="m-text m-dim" href="https://attack.mitre.org/beta/techniques/T1574/001/" target="_blank">T1574.001 Hijack Execution Flow: DLL Search Order Hijacking</a>]</li>
<li><a href="https://palant.info/2020/06/22/exploiting-bitdefender-antivirus-rce-from-any-website/" target="_blank">Exploiting Bitdefender Antivirus: RCE from any website</a>. Antivirus programs are basically benevolent rootkits, and this post shows what happens when insecure coding practices meet privileged applications. In this case, Bitdefender sometimes injects responses into all browsers on the host (no plugin required), for features such as "SafeSearch." This mechanism relies on HTTP headers (sent to any site) and can be used to spawn the Bitdefender "Safepay" browser without user interaction which is then exploited via command injection - all by just visiting a malicious site. I think its time antivirus companies left the browser work to browser companies.</li>
<li><a href="https://isc.sans.edu/forums/diary/Using+Shell+Links+as+zerotouch+downloaders+and+to+initiate+network+connections/26276/" target="_blank">Using Shell Links as zero-touch downloaders and to initiate network connections</a>. LNK files on Windows have been used for malicious purposes for a while (at least as far back as 2010 with Stuxnet). This post is a good overview of what they can do. Recently a <a href="https://blog.vincss.net/2020/06/cve49-microsoft-windows-lnk-remote-code-execution-vuln-cve-2020-1299-eng.html" target="_blank">double-free bug (CVE-2020-1299)</a> was found that could lead to remote code execution if a users clicks a LNK.</li>
<li><a href="https://www.directdefense.com/how-your-red-team-hid-in-your-readers-espkey-attacks/" target="_blank">How Your Red Team “HID” in Your Readers - ESPKey Attacks</a>. If you perform physical assessments HID attacks are likely a major part of your work. Direct Defense skips the badge cloning and goes straight for the reader with a tiny microcontroller (ESPKey) that allows badge and pin data collection and replay.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/michelin/ChopChop" target="_blank">ChopChop</a> is a CLI for scanning endpoints and identifying exposition of services/files/folders through the webroot. Add this to your tool list for web assessments or bug bounties.</li>
<li><a href="https://whynotsecurity.com/blog/max/" target="_blank">Max</a> is a command line tool to interact with the Neo4j database that powers BloodHound. This tool allows easy access to users and groups with lots of good built in filters. It also allows raw Cypher queries against the database for advanced users. [<a class="m-text m-dim" href="https://attack.mitre.org/beta/techniques/T1087/002/" target="_blank">T1087.002 Account Discovery: Domain Account</a>]</li>
<li><a href="https://github.com/hadur-borzsei-kallo/SharpHungarian" target="_blank">SharpHungarian</a> is a rough proof of concept that uses comments on a VirusTotal file for command and control. [<a class="m-text m-dim" href="https://attack.mitre.org/beta/techniques/T1102/002/" target="_blank">T1102.002 Web Service: Bidirectional Communication</a>]</li>
<li><a href="https://github.com/NVISO-BE/FileSearcher" target="_blank">FileSearcher</a> is an unmanaged assembly file searcher for when a fully interactive beacon session is not opsec safe enough. Find those Passwords.txt or Passwords.xlsx files easily with this tool. [<a class="m-text m-dim" href="https://attack.mitre.org/beta/techniques/T1005/" target="_blank">T1005 Data from Local System</a>]</li>
<li><a href="https://github.com/jfmaes/Clippi-B" target="_blank">Clippi-B</a> is an unmanaged assembly clipboard stealer for use with CobaltStrike or any other unmanaged CLR loader (i.e. shad0w). [<a class="m-text m-dim" href="https://attack.mitre.org/beta/techniques/T1115/" target="_blank">T1115 Clipboard Data</a>]</li>
<li><a href="https://github.com/ffuf/pencode" target="_blank">pencode</a> is a tool that helps you to create payload encoding chains. It has been designed to be used in automation wherever it is required to apply multiple encodings to a payload (and possibly inserting the payload to a template in between). This will be helpful for web application penetration testers or bug bounties.</li>
<li><a href="https://github.com/veggiedefender/browsertunnel" target="_blank">browsertunnel</a> is a tool for exfiltrating data from the browser using the DNS protocol. It achieves this by abusing dns-prefetch, a feature intended to reduce the perceived latency of websites by doing DNS lookups in the background for specified domains. DNS traffic does not appear in the browser's debugging tools, is not blocked by a page's Content Security Policy (CSP), and is often not inspected by corporate firewalls or proxies, making it an ideal medium for smuggling data in constrained scenarios. [<a class="m-text m-dim" href="https://attack.mitre.org/beta/techniques/T1071/004/" target="_blank">T1071.004 Application Layer Protocol: DNS</a>]</li>
<li><a href="https://github.com/spaceraccoon/CVE-2020-10665" target="_blank">CVE-2020-10665</a> is a proof of concept for Docker Desktop Local Privilege Escalation on Windows. This is the same researcher from last week's Starbucks writeup. Well done! [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><a href="https://github.com/0xeb-bp/cve-2020-1054" target="_blank">CVE-2020-1054</a> is a proof of concept for a Windows 7 kernel vulnerability that leads to local privilege escalation. Blog post with details <a href="https://0xeb-bp.github.io/blog/2020/06/15/cve-2020-1054-analysis.html" target="_blank">here</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><a href="https://github.com/C-Sto/BananaPhone" target="_blank">BananaPhone</a> is a pure-go implementation of using direct syscalls in the spirit of <a href="https://github.com/am0nsec/HellsGate" target="_blank">HellsGate</a> (LWiS 2020-06-08). [<a class="m-text m-dim" href="https://attack.mitre.org/beta/techniques/T1027/005/" target="_blank">T1027.005 Obfuscated Files or Information: Indicator Removal from Tools</a>]</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/team-video/aviary.sh" target="_blank">aviary.sh</a> is a minimal distributed configuration management in bash. Each host periodically fetches the latest version of the inventory to see what roles it should be performing. If you have struggled with Ansible, Chef, Puppet, or Salt in the past or they were just too much for a simple configuration management job, give aviary.sh a shot. Need slightly more power but don't wan't to step all the way up to the "major" configuration managers? <a href="https://github.com/Fizzadar/pyinfra" target="_blank">pyinfra</a> might be what you are looking for.</li>
<li><a href="https://github.com/tchx84/Flatseal" target="_blank">Flatseal</a> is a graphical utility to review and modify basic permissions from your Flatpak applications. If last week's news about Flatpak security got you worried, Flatseal can help audit applications or modify them for malicious redistribution during an assessment.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
