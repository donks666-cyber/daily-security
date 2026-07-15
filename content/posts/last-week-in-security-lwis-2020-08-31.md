Title: Last Week in Security (LWiS) - 2020-08-31
Date: 2020-08-31 22:45
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-08-31
Author: Erik
Summary: Prevent .NET exit in loaded code by <a href="https://twitter.com/domchell" target="_blank">@domchell</a>, file delete to SYSTEM PoC by <a href="https://twitter.com/404death" target="_blank">@404death</a>, <a href="https://twitter.com/tesla" target="_blank">@Tesla</a> is targeted for insider ransomware recently (failed) and was completely owned in 2017, <a href="https://twitter.com/djhohnstein" target="_blank">@djhohnstein</a> shows how to load Go modules in memory, great new features in Octopus 1.2 from <a href="https://twitter.com/mohammadaskar2" target="_blank">@mohammadaskar2</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-08-24 to 2020-08-31.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://electrek.co/2020/08/27/tesla-fbi-prevent-ransomware-hack-gigafactory-nevada/" target="_blank">Tesla and FBI prevented $1 million ransomware hack at Gigafactory Nevada</a>. If offered $1,000,000 to introduce malware into your computer systems, how many of your employees would report it like the Tesla employee did? Insider threats just got a new poster child.</li>
<li><a href="https://electrek.co/2020/08/27/tesla-hack-control-over-entire-fleet/" target="_blank">The Big Tesla Hack: A hacker gained control over the entire fleet, but fortunately he’s a good guy</a>. More Tesla news last week, with a full network compromise starting with a salvaged car. Impressive/frightening ability to scan and move laterally undetected once in the network as well. With this state of security at Tesla, is anyone lining up to have a different company run by Elon Musk <a href="https://www.neuralink.com/" target="_blank">implant your brain and control it via Bluetooth</a>?</li>
<li><a href="https://palant.info/2020/08/31/a-grim-outlook-on-the-future-of-browser-add-ons/" target="_blank">A grim outlook on the future of browser add-ons</a>. The war on browser extensions is already in its second act. Another strike against mobile comes with Firefox limiting which add-ons are allowed on mobile. While <a href="https://www.wired.com/story/google-chrome-ad-blockers-extensions-api/" target="_blank">Google Says It Isn't Killing Ad Blockers - Ad Blockers Disagree</a> was the first salvo, mobile is the latest battleground.</li>
<li><a href="https://unit42.paloaltonetworks.com/state-of-exploit-development/" target="_blank">The State of Exploit Development: 80% of Exploits Publish Faster than CVEs</a>. No surprise, 80% of the exploits on Exploit-DB were published before their corresponding CVE with an average 23 day lead time. If you only rely on CVEs being issued before you patch, you're behind the curve.</li>
<li><a href="https://hackerone.com/reports/783877" target="_blank">Remote Code Execution in Slack desktop apps + bonus</a>. This is a critical vulnerability in Slack's desktop client with a PoC that netted the research $1,750 for the ability to execute code on client machines by just sending a message to a user and having them click a preview. SecuriTeam <a href="https://twitter.com/SecuriTeam_SSD/status/1300016510522531840" target="_blank">claim</a> they will pay $10,000 for such a bug. Either way, Slack got off easy with this one and most researchers agree the payout was much too low.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://github.com/sailay1996/delete2SYSTEM" target="_blank">delete2SYSTEM</a> - Weaponizing for Arbitrary Files/Directories Delete bugs to Get NT AUTHORITYSYSTEM. This tool uses Windows Error Reporting to load a DLL.</li>
<li><a href="https://teamhydra.blog/2020/08/25/bypassing-credential-guard/" target="_blank">Bypassing Credential Guard</a>. This post builds on <a href="https://blog.xpnsec.com/exploring-mimikatz-part-1/" target="_blank">earlier work</a> to enable wdigest on Windows machines with Credential Guard enabled, all from memory. The <a href="https://gist.github.com/N4kedTurtle/8238f64d18932c7184faa2d0af2f1240" target="_blank">PoC</a> is a bit rough and not OPSEC safe, but would be a great foundation for a custom implementation.</li>
<li><a href="https://github.com/rgeoghan/app-password-persistence/blob/master/README.md" target="_blank">app-password-persistence</a> shows how to use Microsoft 365 app passwords for persistent access to a compromised account, even if MFA is enabled.</li>
<li><a href="https://swarm.ptsecurity.com/grafana-6-4-3-arbitrary-file-read/" target="_blank">Grafana 6.4.3 Arbitrary File Read</a>. The use of <cite>LOAD DATA INFILE</cite> and a rogue MySQL server can lead to arbitrary file read when adding a data source in Grafana.</li>
<li><a href="https://raelize.com/posts/raelize-fi-reference-model/" target="_blank">Fault Injection Reference Model (FIRM)</a>. Fault Injection, or "Glitching" as it's commonly called, has been responsible for a number of high profile hardware hacks recently (Nintendo Switch and PS3). This post is a good primer on what fault injection is and how it can expose vulnerabilities.</li>
<li><a href="https://posts.specterops.io/malware-development-pt-1-dynamic-module-loading-in-go-1121f07f3a5a" target="_blank">Malware Development Pt. 1: Dynamic Module Loading in Go</a>. If you are writing tools in Go, this is a good source of ideas on how to execute Go dynamically in memory. Code <a href="https://github.com/djhohnstein/librarian" target="_blank">here</a>.</li>
<li><a href="https://www.mdsec.co.uk/2020/08/massaging-your-clr-preventing-environment-exit-in-in-process-net-assemblies/" target="_blank">Massaging your CLR: Preventing Environment.Exit in In-Process .NET Assemblies</a>. This post shows a technique to patch .NET assemblies to prevent them from calling exit and exiting whatever tool you used to load them.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/hhlxf/USO_Info_Leak" target="_blank">USO_Info_Leak</a> contains two 0day heap address leak bugs in the usosvc service. The author claims to have 44 more Windows 10 elevation of privilege bugs that have been submitted to Microsoft but not handled well. I'll be following them closely to see if more are released.</li>
<li><a href="https://github.com/mhaskar/Octopus/releases/tag/v1.2" target="_blank">Octopus</a> isn't new but v1.2 sees a host of new features including: shellcode generation for x86 and x64, spoofed arguments, word macro generation, better AV evasion, and an indicator to show privileged user shells. More info <a href="https://shells.systems/octopus-v1-2-stable-shellcode-generation-spoofed-args-agent-and-much-more/" target="_blank">here</a>.</li>
<li><a href="https://github.com/hahwul/jwt-hack" target="_blank">jwt-hack</a> is a swiss-army knife for JSON web tokens, to include a dictionary attack.</li>
<li><a href="https://github.com/antonioCoco/RunasCs/releases/tag/1.3" target="_blank">RunasCs</a> isn't new but v1.3 brings the ability to redirect stdout, stdin, and stderr to a remote host as well as other new features and fixes.</li>
<li><a href="https://github.com/dantheman213/sonarhawk" target="_blank">sonarhawk</a> is a tool to create precise maps of WiFi networks using commodity GPS hardware and a portable computer. Supports Linux, MacOS, and Windows. Useful for mapping WiFi networks while on physical red team engagements or wardriving/warwalking. Similar to the Kismet plugin <a href="https://gitlab.com/SoliForte777/Kestrel" target="_blank">Kestrel</a>.</li>
<li><a href="https://github.com/c3r34lk1ll3r/gdb_2_root" target="_blank">gdb_2_root</a> is a script for rooting x86_64 Google Play Android 10 images in an emulator.</li>
<li><a href="https://github.com/AllsafeCyberSecurity/LazyGhidra" target="_blank">LazyGhidra</a> adds convenience functions to Ghidra like <a href="https://github.com/L4ys/LazyIDA" target="_blank">LazyIDA</a> does for IDA Pro.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Soulghost/iblessing" target="_blank">iblessing</a> is an iOS security exploiting toolkit, it mainly includes application information collection, static analysis and dynamic analysis. It can be used for reverse engineering, binary analysis and vulnerability mining.</li>
<li><a href="https://github.com/fO-000/bluescan" target="_blank">bluescan</a> is a powerful Bluetooth scanner for scanning BR/LE devices, LMP, SDP, GATT and vulnerabilities!</li>
<li><a href="https://github.com/LasCC/Hack-Tools" target="_blank">Hack-Tools</a> is the all-in-one Red Team extension for Web Pentester. Useful features include: Dynamic Reverse Shell generator (PHP, Bash, Ruby, Python, Perl, Netcat), XSS Payloads, SQLi payload, LFI payloads, Base64 encoder/decoder, hash generator, and more.</li>
<li><a href="https://github.com/RedTeamPentesting/monsoon" target="_blank">monsoon</a> is a fast HTTP enumerator that allows you to execute a large number of HTTP requests, filter the responses and display them in real-time.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
