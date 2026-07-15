Title: Last Week in Security (LWiS) - 2022-03-28
Date: 2022-03-28 23:35
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-03-28
Author: Erik
Summary: RCE on a NAS (<a href="https://twitter.com/alexjplaskett" target="_blank">@alexjplaskett</a>, <a href="https://twitter.com/saidelike" target="_blank">@saidelike</a>, and <a href="https://twitter.com/fidgetingbits" target="_blank">@FidgetingBits</a>), Double Fetch vulns (<a href="https://twitter.com/N1ckDunn" target="_blank">@N1ckDunn</a>), Razer LPE (<a href="https://twitter.com/matthiasdeeg" target="_blank">@matthiasdeeg</a>), DFIR cloud automation (<a href="https://twitter.com/zawadidone" target="_blank">@ZawadiDone</a>), Ubuntu LPE (<a href="https://twitter.com/ETenal7" target="_blank">@ETenal7</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-03-21 to 2022-03-28.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://chromereleases.googleblog.com/2022/03/stable-channel-update-for-desktop_25.html" target="_blank">Google is aware that an exploit for CVE-2022-1096 exists in the wild.</a>. Not everyday you see a Chrome 0day in the wild. Update your browser!</li>
<li><a href="https://blog.google/threat-analysis-group/countering-threats-north-korea/" target="_blank">Countering threats from North Korea</a>. The care put into the exploit kit decoy sites is impressive. When a significant portion of your GDP is from cybercrime, I suppose you get pretty good at it.</li>
<li><a href="https://blog.exodusintel.com/2022/03/23/free-nday-subscription/" target="_blank">Exodus Intelligence is offering their N-Day vulnerability subscription for FREE from April 1st through July 1st</a>. I've been "added to the queue" but no N-Days yet.</li>
<li><a href="https://www.sophos.com/en-us/security-advisories/sophos-sa-20220321-utm-9710" target="_blank">Resolved Security Vulnerabilities in Sophos (SG) UTM 9.710 MR10 (CVE-2022-0386, CVE-2022-0652)</a>. A post-auth SQL injection vulnerability in the Mail Manager of Sophos UTM can lead to RCE. SSL VPN bugs are hot right now, consider replacing your VPN appliances with <a href="https://www.wireguard.com/" target="_blank">WireGuard</a> (its faster too).</li>
<li><a href="https://www.vice.com/en/article/dypj77/grimes-said-she-orchestrated-cyber-attack-that-shut-down-hipster-runoff" target="_blank">Grimes Said She Orchestrated Cyberattack That Shut Down ‘Hipster Runoff’</a>. Famous person admits to crimes - nothing happens. A tale as old as time. How many years in prison would a teen in America get for a DDoS plus "erasing backups" (shell access?)?</li>
<li><a href="https://blog.cloudflare.com/cloudflare-investigation-of-the-january-2022-okta-compromise/" target="_blank">Cloudflare’s investigation of the January 2022 Okta compromise</a>. This has some actionable steps if you are an Okta customer. For more, check out <a href="https://www.trustedsec.com/blog/trustedsec-okta-breach-recommendations/" target="_blank">TrustedSec Okta Breach Recommendations</a>.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://research.nccgroup.com/2022/03/25/mining-data-from-cobalt-strike-beacons/" target="_blank">Mining data from Cobalt Strike beacons</a>. A new library designed to parse Cobalt Strike configruations. Perhaps its time to move away from Cobalt Strike.</li>
<li><a href="https://research.nccgroup.com/2022/03/24/remote-code-execution-on-western-digital-pr4100-nas-cve-2022-23121/" target="_blank">Remote Code Execution on Western Digital PR4100 NAS (CVE-2022-23121)</a>. This is a very detailed walkthrough of a information leak and unchecked return value exploit for a NAS. I love that adding some 'sleep()'s fixed the exploit in the Pwn2Own competition to net them a success.</li>
<li><a href="https://research.nccgroup.com/wp-content/uploads/2022/03/NCC_Group_Whitepaper_DoubleFetch2022_Report_2022-03-25_v1.0.pdf" target="_blank">[PDF] Double Fetch Vulnerabilities in C and C++</a>. Double Fetch is where checks are properly done for a fetch, but the second fetch is unchecked. This allows an attaker to modify the data between the fetches.</li>
<li><a href="https://blog.syss.com/posts/razer-lpe-attack/" target="_blank">Yet Another Local Privilege Escalation Attack via Razer Synapse Installer (CVE-2021-44226)</a>. Gaming peripherals have been a goldmine of LPEs recently, and Razer is no exception.</li>
<li><a href="https://www.sentinelone.com/labs/pwning-microsoft-azure-defender-for-iot-multiple-flaws-allow-remote-code-execution-for-all/" target="_blank">Pwning Microsoft Azure Defender for IoT | Multiple Flaws Allow Remote Code Execution for All</a>. "Unauthenticated attackers can remotely compromise devices protected by Microsoft Azure Defender for IoT by abusing vulnerabilities in Azure’s Password Recovery mechanism." It's bad when you have to number your "Unauthenticated Remote Code Execution As Root" findings because there are more than one.</li>
<li><a href="https://zawadidone.nl/automating-dfir-using-cloud-services/" target="_blank">Automating DFIR using Cloud services</a>. IR is never fun, but automation to make it less painful can help!</li>
<li><a href="https://etenal.me/archives/1825" target="_blank">CVE-2022-27666: Exploit esp6 modules in Linux kernel</a>. Buffer and heap exploits can get confusing quickly, but this write up includes amazing animations that show how data is arranged in memory and make it much easier to understand. I hope this technique of write ups catches on.</li>
<li><a href="https://offsec.almond.consulting/ldap-relays-for-initial-foothold-in-dire-situations.html" target="_blank">LDAP relays for initial foothold in dire situations</a>. NTLM relaying may be locked down in an environment, but LDAP remains an option. This post pushes the boundaries to relay harder with LDAP. Defenses included at the end as well!</li>
<li><a href="https://twitter.com/mpgn_x64/status/1508463912890548234" target="_blank">Every "Guest" you invite in your Microsoft Team meetings can list users from other groups</a>. Flip those toggles!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/MythicAgents/tetanus" target="_blank">tetanus</a> is a Mythic C2 agent targeting Linux and Windows hosts written in Rust.</li>
<li><a href="https://github.com/N4kedTurtle/DelegationBOF" target="_blank">DelegationBOF</a> uses LDAP to check a domain for known abusable Kerberos delegation settings. Currently, it supports RBCD, Constrained, Constrained w/Protocol Transition, and Unconstrained Delegation checks.</li>
<li><a href="https://github.com/0xsp-SRD/OffensivePascal" target="_blank">OffensivePascal</a> is a Pascal Offsec repo for malware dev and red teaming 🚩.</li>
<li><a href="https://github.com/RICSecLab/CVE-2019-0708" target="_blank">CVE-2019-0708</a> is a  BlueKeep proof of concept allowing pre-auth RCE on Windows 7.</li>
<li><a href="https://github.com/waldo-irc/YouMayPasser" target="_blank">YouMayPasser</a> is an x64 implementation of <a href="https://github.com/JLospinoso/gargoyle" target="_blank">Gargoyle</a>. Don't sleep on this one ;)</li>
<li><a href="https://github.com/p0dalirius/ctfd-parser" target="_blank">ctfd-parser</a> is a python script to dump all the challenges locally of a CTFd-based Capture the Flag.</li>
<li><a href="https://github.com/octeep/wireproxy" target="_blank">wireproxy</a> is a Wireguard client that exposes itself as a socks5 proxy</li>
<li><a href="https://github.com/breakpointHQ/TCC-ClickJacking" target="_blank">TCC-ClickJacking</a> is a proof of concept for a clickjacking attack on macOS.</li>
<li><a href="https://github.com/Sh0ckFR/DLLirant" target="_blank">DLLirant</a> is a tool to automatize the DLL Hijacking researches on a specified binary.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/XaFF-XaFF/Cronos-Rootkit" target="_blank">Cronos-Rootkit</a> is Windows 10/11 x64 ring 0 rootkit. Cronos is able to hide processes, protect and elevate them with token manipulation.</li>
<li><a href="https://github.com/NHAS/reverse_ssh" target="_blank">reverse_ssh</a> is a cross platform RAT that uses SSH as the transport protocol. This allows the use of native SSH with all the niceties that SSH offers (port forwarding, scp, etc).</li>
<li><a href="https://github.com/c3c/ADExplorerSnapshot.py" target="_blank">ADExplorerSnapshot.py</a> is an AD Explorer snapshot parser. It is made as an ingestor for BloodHound, and also supports full-object dumping to NDJSON.</li>
<li><a href="https://github.com/mttaggart/OffensiveNotion" target="_blank">OffensiveNotion</a> uses Notion as a platform for offensive operations.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 411 (+3)</p>
<p>Blogs monitored: 294 (+4)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
