Title: Last Week in Security (LWiS) - 2022-01-10
Date: 2022-01-10 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-01-10
Author: Erik
Summary: More JDNI to RCE (<a href="https://twitter.com/jfrog" target="_blank">@jfrog</a>), parallel loader (<a href="https://twitter.com/peterwintrsmith" target="_blank">@peterwintrsmith</a> and <a href="https://twitter.com/cube0x0" target="_blank">@cube0x0</a>), MS signed phishing docs (<a href="https://twitter.com/ptrpieter" target="_blank">@ptrpieter</a> and <a href="https://twitter.com/_DaWouw" target="_blank">@_DaWouw</a>), IP-takeover vulns (<a href="https://twitter.com/sebsalla" target="_blank">@sebsalla</a>), driver loading BOF dev (<a href="https://twitter.com/cerbersec" target="_blank">@cerbersec</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-01-03 to 2022-01-10.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://github.com/h2database/h2database/security/advisories/GHSA-h376-j262-vhq6" target="_blank">RCE in H2 Console</a>. With all the dust kicked up by the JDNI injection log4j RCE, you just knew that someone would find JDNI injection elsewhere. <a href="https://jfrog.com/blog/the-jndi-strikes-back-unauthenticated-rce-in-h2-database-console/" target="_blank">"There are bound to be more packages that are affected by the same root cause as Log4Shell."</a>.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://www.mdsec.co.uk/2022/01/edr-parallel-asis-through-analysis/" target="_blank">EDR Parallel-asis through Analysis</a>. "During the development of the Nighthawk C2 MDSec stumbled upon what appears to be a new and novel technique for identifying syscall numbers for certain syscalls which may then be used to load a new copy of ntdll into memory, allowing the remaining syscalls to be read successfully without triggering any installed function hooks." Is this whole post a humble-brag/sales pitch for Nighthawk? Maybe. But I'll gladly take high quality research and PoCs to prove how cool Nighthawk is. Want it in C#? <a href="https://github.com/cube0x0/ParallelSyscalls" target="_blank">say no more</a>.</li>
<li><a href="https://pentestlab.blog/2022/01/04/domain-persistence-adminsdholder/" target="_blank">Domain Persistence – AdminSDHolder</a>. The special AdminSDHolder ACL is applied to all groups and accounts that are part of that object every hour, enabling permissions to be continuously restored to an account if detected by the blue team.</li>
<li><a href="https://pentestlab.blog/2022/01/10/domain-escalation-samaccountname-spoofing/" target="_blank">Domain Escalation – sAMAccountName Spoofing</a>. The sAMAccountName/noPac attack dropped last month, but this post shows multiple tools/attack methods to exploit it in practice. TrustedSec has a good <a href="https://www.trustedsec.com/blog/an-attack-path-mapping-approach-to-cves-2021-42287-and-2021-42278/" target="_blank">blog post</a> on detection opportunities.</li>
<li><a href="https://outflank.nl/blog/2022/01/07/a-phishing-document-signed-by-microsoft-part-2/" target="_blank">A phishing document signed by Microsoft – part 2</a>. Microsoft signed add-ins are back, and have vulnerabilities. A string of bugs/features were used/abused to enable remote XLL loading. At this point I'm not sure anyone outside of Redmond, WA knows more about office document internals than Pieter, Dima, and the team at Outflank.</li>
<li><a href="https://caniphish.com/phishing-resources/blog/compromising-australian-supply-chains-at-scale" target="_blank">Scanning millions of domains and compromising the email supply chain of Australia's most respected institutions</a>. The use a AWS Lambda and DynamoDB for distributed scanning was clever, but the number sites where SPF/DMARC checks passed just with some light EC2 cycling to get proper IPs was frightening. Very cool research!</li>
<li><a href="https://blog.nviso.eu/2022/01/10/kernel-karnage-part-8-getting-around-dse/" target="_blank">Kernel Karnage – Part 8 (Getting Around DSE)</a>. This serious has been great so far, and now that real world protections are turned back on it's really getting good. There is no PoC dropped, but enough code to get you pretty far in your own driver loading BOF adventures. Keep up the great work <a href="https://twitter.com/cerbersec" target="_blank">@cerbersec</a>.</li>
<li><a href="https://docs.microsoft.com/en-us/microsoft-365/security/defender/advanced-hunting-expert-training?view=o365-worldwide" target="_blank">Get expert training on advanced hunting</a>. This is a great collection of MS defender for endpoint and KQL training.</li>
<li><a href="https://dys2p.com/en/2021-12-tamper-evident-protection.html" target="_blank">Random Mosaic – Detecting unauthorized physical access with beans, lentils and colored rice</a>. If you ever need to be <em>really</em> sure no one has intercepted your package, this is a cool option.</li>
<li><a href="https://improsec.com/tech-blog/staging-cobalt-strike-with-mtls-using-caddy" target="_blank">Staging Cobalt Strike with mTLS using Caddy</a>. Staging is a bad idea. But what if you protected your staging endpoint with mTLS? You'd end up with <a href="https://github.com/improsec/caddystager" target="_blank">CaddyStager</a>!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/kyleavery/inject-assembly" target="_blank">inject-assembly</a> is an alternative to traditional fork and run execution for Cobalt Strike. The loader can be injected into any process, including the current Beacon. Long-running assemblies will continue to run and send output back to the Beacon, similar to the behavior of execute-assembly.</li>
<li><a href="https://github.com/rapiz1/rathole" target="_blank">rathole</a> is a lightweight, stable and high-performance reverse proxy for NAT traversal, written in Rust. An alternative to frp and ngrok.</li>
<li><a href="https://github.com/nccgroup/insject" target="_blank">insject</a> is a tool for poking at containers. It enables you to run an arbitrary command in a container or any mix of Linux namespaces. More details <a href="https://research.nccgroup.com/2022/01/08/tool-release-insject-a-linux-namespace-injector/" target="_blank">here</a>.</li>
<li><a href="https://github.com/ScarredMonk/SysmonSimulator" target="_blank">SysmonSimulator</a> is a Sysmon event simulation utility which can be used to simulate the attacks to generate the Sysmon Event logs for testing the EDR detections and correlation rules by Blue teams.</li>
<li><a href="https://github.com/DarkCoderSc/PowerRemoteDesktop" target="_blank">PowerRemoteDesktop</a> is a Remote Desktop client entirely coded in PowerShell. This could be useful for restricted environments like virtual desktops.</li>
<li><a href="https://github.com/thefLink/Hunt-Sleeping-Beacons" target="_blank">Hunt-Sleeping-Beacons</a> is a project to identify beacons which are unpacked at runtime or running in the context of another process.</li>
<li><a href="https://github.com/jklepsercyber/defender-detectionhistory-parser" target="_blank">defender-detectionhistory-parser</a> is a parser of Windows Defender's DetectionHistory forensic artifact, containing substantial info about quarantined files and executables. First one to write this as a BOF wins.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/trufflesecurity/driftwood" target="_blank">driftwood</a> is a tool that can enable you to lookup whether a private key is used for things like TLS or as a GitHub SSH key for a user.</li>
<li><a href="https://github.com/tb0hdan/domains" target="_blank">domains</a> is (probably) the world’s single largest Internet domains dataset.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
