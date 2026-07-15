Title: Last Week in Security (LWiS) - 2021-02-01
Date: 2021-02-01 23:06
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-02-01
Author: Erik
Summary: Sudo LPE (<a href="https://twitter.com/bl4sty" target="_blank">@bl4sty</a>), Cobalt Strike patching for evasion (<a href="https://twitter.com/_xpn_" target="_blank">@_xpn_</a>), web bruteforcing (<a href="https://twitter.com/Xst3nZ" target="_blank">@Xst3nZ</a>), customizing phishlets (<a href="https://twitter.com/Bb_hacks" target="_blank">@Bb_hacks</a>), Kerberos LPE on Linux (<a href="https://twitter.com/xassiz" target="_blank">@xassiz</a>), shared file C2 (<a href="https://twitter.com/scriptmonkey_" target="_blank">@scriptmonkey_</a>), homograph tool (<a href="https://twitter.com/evilsocket" target="_blank">@evilsocket</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-01-25 to 2021-02-01.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.armis.com/resources/iot-security-blog/nat-slipstreaming-v2-0-new-attack-variant-can-expose-all-internal-network-devices-to-the-internet/" target="_blank">NAT Slipstreaming v2.0: New Attack Variant Can Expose All Internal Network Devices to The Internet</a>. This updated version of Samy Kamkar's work from last fall shows how a new primitive, H.323 ALG, is used to create holes in a NAT device which allow access to arbitrary IPs/ports behind it from the internet. Demo <a href="https://youtu.be/M-6ppoYDEV4" target="_blank">here</a>.</li>
<li><a href="https://krebsonsecurity.com/2021/01/international-action-targets-emotet-crimeware/" target="_blank">International Action Targets Emotet Crimeware</a>. "Operation Ladybird" saw the raiding and arrests at multiple locations across Europe linked to Emotet operators. They even release <a href="https://youtu.be/_BLOmClsSpc" target="_blank">a video</a> of one such raid.</li>
<li><a href="https://googleprojectzero.blogspot.com/2021/01/a-look-at-imessage-in-ios-14.html" target="_blank">A Look at iMessage in iOS 14</a>. With iMessage being a standard target for 0 or 1 click exploits, Apple has introduced a new "BlastDoor" service and other improvements to make these attacks much more difficult.</li>
<li><a href="https://twitter.com/patrickwardle/status/1356148680886079491" target="_blank">Top macOS researcher escapes the rat race</a>. Patrick Wardle has been the go-to guy for macOS research and malware analysis. He has given countless conference talks, found just as man 0days, and is now publishing all his macOS utilities as open source under the GPL. This "sponsorship" model of security research is interesting, and I hope it enables more people to focus on interesting problems while also giving back to the community that supports them.</li>
<li><a href="https://www.technologyreview.com/2021/01/30/1017086/cdc-44-million-vaccine-data-vams-problems/" target="_blank">What went wrong with America’s $44 million vaccine data system?</a>. I fully admit this is a difficult problem to solve. But is it a $42 million no-bid contract difficult problem? Has America learned nothing from the <a href="https://www.govtech.com/health/Column-HealthCaregov-Lessons-from-a-Fiasco.html" target="_blank">healthcare.gov fiasco</a>? The sad reality is there is likely a team of overworked developers at Deloitte trying their best to make VAMS work, and they will see almost none of that $42 million.</li>
<li><a href="https://twitter.com/mtarral/status/1354845868214669314" target="_blank">OSWatcher updated and organized into GitHub org</a>. This project captures the changes between operating system versions as git commits, which makes it easy to pinpoint exactly when a file was added to an OS, along with lots of metadata about the files. This is a project that can help both red and blue teams as it provides foundational information about target operating systems.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://s3cur3th1ssh1t.github.io/A-tale-of-EDR-bypass-methods/" target="_blank">A tale of EDR bypass methods</a>. If you only click one link from this week's blog, click this one. It's a full recap of the last two years of EDR bypasses for Windows with detail on each method. Lots of things to explore from this one if you haven't been keeping a close eye on EDR bypasses.</li>
<li><a href="https://www.trustedsec.com/blog/tailoring-cobalt-strike-on-target/" target="_blank">Tailoring Cobalt Strike on Target</a>. Cobalt Strike beacons have to be configured before delivery, but in strict environments a wrong user agent can start an investigation and potentially loose access. <a href="https://twitter.com/_xpn_" target="_blank">@_xpn_</a> shows how red teamers can perform some basic recon on target and then patch a Cobalt Strike beacon to blend in before the first connection to C2 is ever made. Demo <a href="https://youtu.be/fE4nPA_eeZE" target="_blank">here</a>, code <a href="https://gist.github.com/xpn/6c40d620607e97c2a09c70032d32d278" target="_blank">here</a>.</li>
<li><a href="https://www.blackarrow.net/from-n-day-exploit-to-kerberos-eop-in-linux-environments/" target="_blank">From N-day exploit to Kerberos EoP in Linux environments</a>. This is textbook advanced adversary emulation. Faced with a fully up to date Red Hat machine, the BlackArrow red team researched and developed a working exploit for an Nday with no public PoC. Their PoC is available <a href="https://github.com/blackarrowsec/redteam-research/tree/master/CVE-2018-1685" target="_blank">on GitHub</a>.</li>
<li><a href="https://labs.nettitude.com/blog/introducing-fcomm-c2-lateral-movement/" target="_blank">Introducing FComm – C2 Lateral Movement</a>. FComm provides an additional communication method for the PoshC2 framework. It provides a way to circumvent certain lateral movement limitations using file-based communications. This is a neat way to communicate in a restricted environment where two machines have common access to files (usually via a file share). This can be slow, but has the advantage of no visible TCP/IP connection to defenders. FComm has been merged into <a href="https://github.com/nettitude/PoshC2" target="_blank">PoshC2</a>.</li>
<li><a href="https://secret.club/2021/01/29/touch-lockscreen-bypass.html" target="_blank">BitLocker touch-device lockscreen bypass</a>. This is the second lockscreen bypass using a similar technique in a short time. Once you get the narrator to jump to the windows behind the lockscreen, an attacker can execute code from a thumb drive fairly easily. Demo <a href="https://youtu.be/JAVRAeSJGwg" target="_blank">here</a>. Do not leave your devices unattended, but especially do not leave your devices powered on an unattended.</li>
<li><a href="https://shells.systems/customising-an-existing-evilginx-phishlet-to-work-with-modern-citrix/" target="_blank">Customizing an existing evilginx phishlet to work with modern Citrix</a>. This is a great post that shows what really happens on engagements. Find a tool, spin it up, test it out - failure. Troubleshoot, fail, troubleshoot fail, repeat until success. I'm storing this one away for my next use of <a href="https://github.com/kgretzky/evilginx2" target="_blank">evilginx2</a> against a constantly changing login portal.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt">Heap-based buffer overflow in Sudo (CVE-2021-3156)</a>. While it sounds similar to <a href="https://www.sudo.ws/alerts/pwfeedback.html">CVE-2019-18634</a> (<a href="https://blog.badsectorlabs.com/last-week-in-security-lwis-2020-02-10.html">LWiS 2020-02-10</a>) this vulnerability affects default configurations, and has been around for 9 years. I suspect an exploit for this will become the <a href="https://dirtycow.ninja/">DirtyCow</a> of 2021. There is a good <a href="https://www.kalmarunionen.dk/writeups/sudo/">writeup</a> that uses a fake libnss load to get a shell, and a <a href="https://github.com/blasty/CVE-2021-3156">PoC</a> from a different source. Want to play with different exploits? Grab <a href="https://github.com/apogiatzis/docker-CVE-2021-3156">docker-CVE-2021-3156</a>. Funny enough, while testing this exploit <a href="https://seclists.org/oss-sec/2021/q1/88">another minor issue in Sudo was discovered</a>.</li>
<li><a href="https://github.com/evilsocket/ditto" target="_blank">ditto</a> is a tool for IDN homograph attacks and detection. This could make your next phishing engagement really blend in.</li>
<li><a href="https://github.com/koutto/web-brutator" target="_blank">web-brutator</a> if a fast, modular, web interface bruteforcer. Sometimes you want to throw some credentials at a web login without writing all the boilerplate. This includes modules for many known content management systems and makes it easy to write your own custom brute-forcing module.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.procdot.com/index.htm" target="_blank">ProcDOT</a> turns thousands of monitored activities into a big behavioral picture - actually a graph - which can be interactively explored making behavioral malware analysis as efficient as it never was before. It takes in Procmon and pcap to generate the graph.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
