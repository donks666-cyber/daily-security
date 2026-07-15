Title: Last Week in Security (LWiS) - 2024-07-08
Date: 2024-07-08 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-07-08
Author: Erik
Summary: 👻 Ghostscript exploit (<a href="https://x.com/thomasrinsma" target="_blank">@thomasrinsma</a>), CSPT2CSRF (<a href="https://x.com/maxenceschmitt" target="_blank">@maxenceschmitt</a>), Puppet Forge pwn (<a href="https://x.com/adnanthekhan" target="_blank">@adnanthekhan</a>), WhatsUp Gold RCE+privesc (<a href="https://x.com/SinSinology" target="_blank">@SinSinology</a>), UDRL-less beacon (<a href="https://x.com/naksyn" target="_blank">@naksyn</a>), EDRPrison (<a href="https://x.com/senzee1984" target="_blank">@senzee1984</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-07-01 to 2024-07-08.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.twilio.com/en-us/changelog/Security_Alert_Authy_App_Android_iOS" target="_blank">Security Alert: Update to the Authy Android (v25.1.0) and iOS App (v26.1.0)</a> - If you've ever used Authy your phone number has likely been leaked.</li>
<li><a href="https://www.youtube.com/playlist?list=PLJK0fZNGiFU_Zh8PkjCws_Rw_8WdWKyd7" target="_blank">SO-CON 2024 Youtube Playlist</a> - All the talks from SpecterOps Con 2024 are available!</li>
<li><a href="https://www.youtube.com/watch?v=Nh99d3YnpI4" target="_blank">Kuba Gretzky: Keynote: A Smooth Sea Never Made a Skilled Phisherman</a> - The x33fcon keynote and demo of upcoming Evilginx Pro is available.</li>
<li><a href="https://www.propublica.org/article/cyber-safety-board-never-investigated-solarwinds-breach-microsoft" target="_blank">The President Ordered a Board to Probe a Massive Russian Cyberattack. It Never Did.</a> - "DHS acknowledges that the board needs more resources and investigative muscle." CISA's budget for 2024 is $2,800,000,000 (2.8 billion USD), DHS's is $103.2 billion.</li>
<li><a href="https://securelist.com/cloudsorcerer-new-apt-cloud-actor/113056/" target="_blank">CloudSorcerer - A new APT targeting Russian government entities</a> - "...cyberespionage tool used for stealth monitoring, data collection, and exfiltration via Microsoft Graph". COM objects + Microsoft Graph API. Not a TTP seen or mentioned in the 2024 threat reports disclosed by vendors earlier this year.</li>
<li><a href="https://tailscale.com/blog/via" target="_blank">New options for granular network policy</a> - For the tailscale users, IP sets are a thing now. Check it out!</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.3nailsinfosec.com/post/edrprison-borrow-a-legitimate-driver-to-mute-edr-agent" target="_blank">EDRPrison: Borrow a Legitimate Driver to Mute EDR Agent</a> - In the age of advanced EDR, what if you just didn't allow the EDR to communicate? The next step of this research would be to profile the EDR and determine "check ins" vs "detections" and only filter out detections so the machine still reports green on the EDR dashboard.</li>
<li><a href="https://research.checkpoint.com/2024/exploring-compiled-v8-javascript-usage-in-malware/" target="_blank">Exploring Compiled v8 Javascript Usage in Malware</a> - You've probably heard about javascript "web assembly" but did you know you can compile javascript into V8 bytecode (assuming your javascript engine is Chrome/Node's V8)? Malware authors are taking advantage of antivirus blinds spots for V8, as it's just-in-time compilation is hard to monitor and signature. <a href="https://github.com/suleram/View8" target="_blank">View8</a> is the tool that aided in the analysis.</li>
<li><a href="https://codeanlabs.com/blog/research/cve-2024-29510-ghostscript-format-string-exploitation/" target="_blank">CVE-2024-29510 - Exploiting Ghostscript using format strings</a> - Gostscript underpins most document conversion libraries, so this code execution and sandbox escape vulnerability is pretty severe.</li>
<li><a href="https://www.synacktiv.com/en/publications/github-actions-exploitation-untrusted-input" target="_blank">Github Actions Exploitation: Untrusted Input</a> - More CI/CD exploitation on the largest code hosting platform.</li>
<li><a href="https://blog.doyensec.com/2024/07/02/cspt2csrf.html" target="_blank">Exploiting Client-Side Path Traversal to Perform Cross-Site Request Forgery - Introducing CSPT2CSRF</a> - Client-Side Path-Traversal vulnerabilities have been long overlooked, but can be used to do some interesting Cross-Site Request Forgery attacks.</li>
<li><a href="https://adepts.of0x.cc/vba-rwx-addendum/" target="_blank">VBA: overwriting R/W/X memory in a reliable way</a> - The VBA masters are at it again.</li>
<li><a href="https://adnanthekhan.com/2024/07/02/roguepuppet-a-critical-puppet-forge-supply-chain-vulnerability/" target="_blank">RoguePuppet - A Critical Puppet Forge Supply Chain Vulnerability</a> - A GitHub Actions CI/CD misconfiguration within Puppet Lab's public GitHub repositories allowed anyone with a GitHub account to push official modules to Puppet Forge. If you use Puppet you should be pinning your packages to specific, known good, versions.</li>
<li><a href="https://summoning.team/blog/progress-whatsup-gold-rce-cve-2024-4885/" target="_blank">WhatsUp Gold Pre-Auth RCE GetFileWithoutZip Primitive</a> - Unauthenticated path traversal leads to unauthenticated remote code execution. Don't worry, there is a <a href="https://summoning.team/blog/progress-whatsup-gold-privesc-setadminpassword-cve-2024-5009/" target="_blank">privilege escalation in WhatsUp Gold</a> too.</li>
<li><a href="https://www.snailload.com/" target="_blank">SnailLoad - Remote Network Latency Measurements Leak User Activity</a> - The latency of loading resources from an "attacker" controlled server while doing other network activities can sometimes reveal your other activity. Curious how much "noise" (other machines, etc) this technique can tolerate, and the papers states that faster connections are less prone to traffic classification. "I need this 1Gb/1Gb plan for security" is now valid?!</li>
<li><a href="https://www.naksyn.com/cobalt%20strike/2024/07/02/raising-beacons-without-UDRLs-teaching-how-to-sleep.html" target="_blank">Raising Beacons without UDRLs and Teaching them How to Sleep</a> - Calling the DLL's entry point twice with a different dwReason value to trigger different behavior is cleaver. Lots of good technical detail in this post. <a href="https://github.com/naksyn/DojoLoader" target="_blank">DojoLoader</a> is the PoC.</li>
<li><a href="https://posts.specterops.io/like-shooting-phish-in-a-barrel-926c1905bb4b" target="_blank">Like Shooting Phish in a Barrel</a> - Some good ideas on getting around link crawlers.</li>
<li><a href="https://sensepost.com/blog/2024/dumping-lsa-secrets-a-story-about-task-decorrelation/" target="_blank">Dumping LSA secrets: a story about task decorrelation</a> - Crowdstrike prevention bypass to dump LSA. Might still work!</li>
<li><a href="https://www.xintra.org/blog/lateral-movement-entraid-cross-tenant-synchronization" target="_blank">Detecting Lateral Movement in Entra ID: Cross Tenant Synchronization</a> - Includes some detection engineering logic for defenders/purple teamers.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/senzee1984/EDRPrison" target="_blank">EDRPrison</a> - Leverage a legitimate WFP callout driver to prevent EDR agents from sending telemetry.</li>
<li><a href="https://github.com/suleram/View8" target="_blank">View8</a> - Decompiles serialized V8 objects back into high-level readable code.</li>
<li><a href="https://github.com/naksyn/DojoLoader" target="_blank">DojoLoader</a> - Generic PE loader for fast prototyping evasion techniques.</li>
<li><a href="https://github.com/ManuelBerrueta/FlowAnalyzer" target="_blank">FlowAnalyzer</a> - FlowAnalyzer is a tool to help in testing and analyzing OAuth 2.0 Flows, including OpenID Connect (OIDC).</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/whokilleddb/ETWListicle" target="_blank">ETWListicle</a> - List the ETW provider(s) in the registration table of a process.</li>
<li><a href="https://github.com/fern89/runpe-x64" target="_blank">runpe-x64</a> - RunPE adapted for x64 and written in C, does not use RWX.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 430 (+3)</p>
<p>Blogs monitored: 384 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
