Title: Last Week in Security (LWiS) - 2022-07-25
Date: 2022-07-25 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-07-25
Author: Erik
Summary: The end of PPLdump (<a href="https://twitter.com/itm4n" target="_blank">@itm4n</a>), beacon detection (<a href="https://twitter.com/domchell" target="_blank">@domchell</a>), 30k Wordpress XXS+SQLi (<a href="https://twitter.com/MrTuxracer" target="_blank">@MrTuxracer</a>), string encryption in c++ (<a href="https://twitter.com/mcbroom_evan" target="_blank">@mcbroom_evan</a>), create a DLL hijack (<a href="https://twitter.com/x86matthew" target="_blank">@x86matthew</a>), and more!

<aside class="m-note m-warning">
<h3>Summer break</h3>
<p>This is the last LWiS until after BSides LV/DEF CON. Hope to see you there!</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-07-18 to 2022-07-25.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://confluence.atlassian.com/doc/questions-for-confluence-security-advisory-2022-07-20-1142446709.html" target="_blank">Questions For Confluence Security Advisory 2022-07-20</a>. "A remote, unauthenticated attacker with knowledge of the hardcoded password could exploit this to log into Confluence and access any pages the confluence-users group has access to." What year is it again?</li>
<li><a href="https://www.zyxel.com/support/Zyxel-security-advisory-authenticated-directory-traversal-vulnerabilities-of-firewalls.shtml" target="_blank">Zyxel security advisory for local privilege escalation and authenticated directory traversal vulnerabilities of firewalls</a>. At least they are authenticated vulnerabilities?</li>
<li><a href="https://security.googleblog.com/2022/07/dns-over-http3-in-android.html" target="_blank">DNS-over-HTTP/3 in Android</a>. This is going to make DNS over HTTP/3 tunneling harder to pick out due to the volume of legitimate requests.</li>
<li><a href="https://decoded.avast.io/janvojtesek/the-return-of-candiru-zero-days-in-the-middle-east/" target="_blank">The Return of Candiru: Zero-days in the Middle East</a>. A sophisticated campaign that used a compromised site to host a WebRTC 0day (affecting at least Chrome, possibly other browsers) isn't your every day drive by compromise.</li>
<li><a href="https://blog.google/threat-analysis-group/continued-cyber-activity-in-eastern-europe-observed-by-tag/" target="_blank">Continued cyber activity in Eastern Europe observed by TAG</a>. Fake mobile DDoS app to "help stop Russian aggression against Ukraine," actually sent all your information to Russia. At least the "number of installs was miniscule."</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://itm4n.github.io/the-end-of-ppldump/" target="_blank">The End of PPLdump</a>. The July 2022 update changes how PPL processes to no longer rely on Known DLLs, a critical step in the PPLdump bypass. Check the post for the full RE teardown of NTDLL.dll.</li>
<li><a href="https://research.nccgroup.com/2022/07/25/technical-advisory-multiple-vulnerabilities-in-nuki-smart-locks-cve-2022-32509-cve-2022-32504-cve-2022-32502-cve-2022-32507-cve-2022-32503-cve-2022-32510-cve-2022-32506-cve-2022-32508-cve-2/" target="_blank">Technical Advisory - Multiple vulnerabilities in Nuki smart locks</a>. As the saying goes: "The 'S' in IoT stands for security."</li>
<li><a href="https://www.mdsec.co.uk/2022/07/part-1-how-i-met-your-beacon-overview/" target="_blank">How I Met Your Beacon</a>. This currently 2 part series takes a look at the behavioral tells of popular C2 frameworks, highlighting common anomalies that make beacons of all types stand out. The implicit message is that Nighthawk, MDSec's own commercial C2 doesn't display these anomalies. <a href="https://www.mdsec.co.uk/2022/07/part-2-how-i-met-your-beacon-cobalt-strike/" target="_blank">Part 2</a> includes new network based detections for Cobalt Strike Team Servers.</li>
<li><a href="https://www.rcesecurity.com/2022/07/WordPress-Transposh-Exploiting-a-Blind-SQL-Injection-via-XSS/" target="_blank">WordPress Transposh: Exploiting a Blind SQL Injection via XSS</a>. This little manuever netted Julien $30,000 in bounties and forced WordPress's removal of the plugin from its directory.</li>
<li><a href="https://posts.specterops.io/encrypting-strings-at-compile-time-4141dafe5b41" target="_blank">Encrypting Strings at Compile Time</a>. A single header file can encrypt your C++ strings at compile time, but be aware that tweaks will be needed to defat <a href="https://github.com/mandiant/flare-floss" target="_blank">FLARE Obfuscated String Solver</a>.</li>
<li><a href="https://www.x86matthew.com/view_post?id=add_exe_import" target="_blank">AddExeImport - Add a hardcoded DLL dependency to any EXE</a>. No DLL hijack convenient for your use? Create one! Another cool, creative technique from x86matthew. Be aware, signatures will no longer be valid.</li>
<li><a href="https://voidsec.com/browser-exploitation-firefox-cve-2011-2371/" target="_blank">Browser Exploitation: Firefox Integer Overflow - CVE-2011-2371</a>. An older vulnerability, but a great introduction to heap vulnerabilities in browsers.</li>
<li><a href="https://mgeeky.tech/protectmytooling/" target="_blank">ProtectMyTooling - Don't detect tools, detect techniques</a>. A suite of tools to rid yourself of static signatures and force Blue teams to detect techniques instead.</li>
<li><a href="https://outpost24.com/blog/Better-proxy-than-story" target="_blank">Phishing: Better Proxy than Story</a> details a "modern" phishing stack.</li>
<li><a href="https://dispatch.redteams.fyi/red-team-edr-bypass-team/" target="_blank">Red Team? Or EDR Bypass Team</a>. An interesting post on where value is derived from a red team assessment.</li>
<li><a href="https://starlabs.sg/blog/2022/07-gitlab-project-import-rce-analysis-cve-2022-2185/" target="_blank">Gitlab Project Import RCE Analysis (CVE-2022-2185)</a>. This was a nasty vulnerability (CVSS 9.9) in Gitlab where a crafted project import resulted in RCE. How you ask? this post breaks it down in detail.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Wh04m1001/DiagTrackEoP" target="_blank">DiagTrackEoP</a> - another way to abuse SeImpersonate privilege.</li>
<li><a href="https://github.com/ezra-buckingham/terry-the-terraformer" target="_blank">terry-the-terraformer</a> A Python CLI tool for deploying red team infrastructure across multiple cloud providers, all integrated with a virtual Nebula network.</li>
<li><a href="https://github.com/PaloAltoNetworks/IAM-Deescalate" target="_blank">IAM-Deescalate</a> IAM-Deescalate helps mitigate privilege escalation risk in AWS identity and access management (IAM). More info <a href="https://unit42.paloaltonetworks.com/iam-deescalate/" target="_blank">here</a>.</li>
<li><a href="https://github.com/last-byte/RIPPL" target="_blank">RIPPL</a> is a tool that abuses a usermode only exploit to manipulate PPL processes on Windows (patched in the July 2022 patch).</li>
<li><a href="https://github.com/enkomio/AlanFramework" target="_blank">AlanFramework</a> - A C2 post-exploitation framework. This framework has been around for a while, but last week became open source (Attribution-NonCommercial-NoDerivatives 4.0 International).</li>
<li><a href="https://github.com/codewhitesec/Lastenzug" target="_blank">Lastenzug</a> - Socks4a proxy leveraging PIC, Websockets and static obfuscation on assembly level.</li>
<li><a href="https://github.com/randorisec/CVE-2022-34918-LPE-PoC" target="_blank">CVE-2022-34918-LPE-PoC</a> - This exploit has been written for the kernel Linux ubuntu 5.15.0-39-generic. More details <a href="https://randorisec.fr/crack-linux-firewall/" target="_blank">here</a>.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Ben-Lichtman/ropr" target="_blank">ropr</a> - A blazing fast™ multithreaded ROP Gadget finder. ropper / ropgadget alternative.</li>
<li><a href="https://github.com/wikiZ/RedGuard" target="_blank">RedGuard</a>  "is a derivative work of the C2 facility pre-flow control technology." Looks a lot like <a href="https://github.com/mgeeky/RedWarden" target="_blank">RedWarden</a>?</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 419 (+0)</p>
<p>Blogs monitored: 317 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
