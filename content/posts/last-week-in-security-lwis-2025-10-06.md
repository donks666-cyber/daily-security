Title: Last Week in Security (LWiS) - 2025-10-06
Date: 2025-10-06 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-10-06
Author: Erik
Summary: WriteAccountRestrictions fun (<a href="https://x.com/unsigned_sh0rt" target="_blank">@unsigned_sh0rt</a>), RCE in Dell UnityVSA (<a href="https://x.com/SinSinology" target="_blank">@SinSinology</a>), Unity Runtime exploit (<a href="https://x.com/ryotkak" target="_blank">@ryotkak</a>), Lenovo DCC LPE (<a href="https://x.com/0x4d5aC" target="_blank">@0x4d5aC</a>), remote control over generators (<a href="https://x.com/XeEaton" target="_blank">@XeEaton</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-09-29 to 2025-10-06.</p>
<aside class="m-note m-success">
Last Week in Security will be off next week as we focus on <a href="https://ludus.cloud" target="_blank">Ludus</a> 2.0.</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.bbc.com/news/articles/c3w5n903447o" target="_blank">'You'll never need to work again': Criminals offer reporter money to hack BBC</a> - Why spend the effort on initial access if you can buy your way in? The threat actors claim it has worked for high profile breaches in the past.</li>
<li><a href="https://sites.google.com/view/mic-e-mouse" target="_blank">Mic-E-Mouse: Covert Eavesdropping through Computer Mice</a> - Your 20,000 dpi mouse can now be used to record your speech via the vibrations in your desk.</li>
<li><a href="https://doublepulsar.com/red-hat-consulting-breach-puts-over-5000-high-profile-enterprise-customers-at-risk-in-detail-90114f18f706" target="_blank">Red Hat Consulting breach puts over 5000 high profile enterprise customers at risk — in detail</a> - 2.2GB of data including certificates from companies that were customers of Red Hat Consulting has been teased.</li>
<li><a href="https://www.nytimes.com/2025/09/18/nyregion/zelle-chase-banking-scam.html?unlocked_article_code=1.nE8.mifp.13j7oh96HfpC&amp;smid=url-share&amp;utm_source=substack&amp;utm_medium=email" target="_blank">I’ve Written About Loads of Scams. This One Almost Got Me.</a> - Always hang up and call the number yourself. You cannot trust caller ID.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://hackerhermanos.com/azbridge/" target="_blank">When Azure Relay Becomes a Red Teamer’s Highway</a> - Microsoft's Azure Relay Bridge uses outbound HTTPS to Azure in order to create TCP tunnels "from and to anywhere." The <a href="https://github.com/Azure/azure-relay-bridge" target="_blank">command line tool</a> is written in C# and open source. Creating a DLL with this and then using AppDomain Hijacking could create a very neat persistence technique...</li>
<li><a href="https://flatt.tech/research/posts/arbitrary-code-execution-in-unity-runtime/" target="_blank">CVE-2025-59489: Arbitrary Code Execution in Unity Runtime</a> - This is specifically the Android Unity Runtime (used by games like Pokemon Go), and the SELinux restrictions prevents "almost all remote exploitation scenarios." Seems pretty wild that an "app intent" string can include a shared object path to load.</li>
<li><a href="https://eaton-works.com/2025/10/06/industrial-generator-hack/" target="_blank">Taking remote control over industrial generators</a> - Just because the front end application doesn't show anything when "not authenticated" doesn't mean the API won't give up the data.</li>
<li><a href="https://h0mbre.github.io/Lucid_Dreams_1/" target="_blank">Lucid Dreams I: Lucid's First Time Fuzzing</a> - The latest installment of the ever detailed an entertaining fuzzer development series.</li>
<li><a href="https://neodyme.io/en/blog/lenovo_dcc_lpe_logic/#tldr" target="_blank">Lenovo DCC: Part 1 - A simple ACL Exploit</a> - A vendor's application allows for privilege escalation in two different ways. Always audit the standard utilities on machines for these kinds of bugs.</li>
<li><a href="https://www.rcesecurity.com/2025/09/when-audits-fail-four-critical-pre-auth-vulnerabilities-in-trufusion-enterprise/" target="_blank">When Audits Fail: Four Critical Pre-Auth Vulnerabilities in TRUfusion Enterprise</a> - The more ® and ™️s I see on a software vendor's site, the more confident I am there will be bugs. This article adds evidence to that claim.</li>
<li><a href="https://specterops.io/blog/2025/10/03/ai-gated-loader-teaching-code-to-decide-before-it-acts/" target="_blank">AI Gated Loader: Teaching Code to Decide Before It Acts</a> - Offloading your decision to run a payload or not to a 3rd party LLM and sending telemetry about customer's machines to that 3rd party seems crazy to me. It also means you're embedding an OpenAPI key into your loader (it reads from an environment variable but how is that going to work on target?) that I'm sure a malware analyst would love to put into an endless <cite>for</cite> loop draining your credits. I see only downsides to this; what am I missing?</li>
<li><a href="https://specterops.io/blog/2025/10/01/writeaccountrestrictions-war-what-is-it-good-for/" target="_blank">WriteAccountRestrictions (WAR) – What is it good for?</a> - User-Account-Restrictions allows you to modify security settings, and can lead to compromised accounts or even the entire domain. Another <a href="https://ludus.cloud" target="_blank">Ludus</a> spotting in the wild 😊</li>
<li><a href="https://labs.watchtowr.com/its-never-simple-until-it-is-dell-unityvsa-pre-auth-command-injection-cve-2025-36604/" target="_blank">It's Never Simple Until It Is (Dell UnityVSA Pre-Auth Command Injection CVE-2025-36604)</a> - If you aren't reading every watchTowr report, then you're missing out. Technical, sarcastic, excellent.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/symeonp/Lenovo-CVE-2025-8061/tree/main" target="_blank">Lenovo-CVE-2025-8061</a> - PoC for popping a system shell against the LnvMSRIO.sys driver.</li>
<li><a href="https://github.com/Nomad0x7/sekken-enum" target="_blank">sekken-enum</a> - adws enumeration bof.</li>
<li><a href="https://github.com/mordavid/NetworkHound" target="_blank">NetworkHound</a> - Advanced Active Directory network topology analyzer with SMB validation, multiple authentication methods (password/NTLM/Kerberos), and comprehensive network discovery. Export results as BloodHound‑compatible OpenGraph JSON. [Looks AI generated]</li>
<li><a href="https://github.com/watchtowrlabs/watchTowr-vs-Oracle-E-Business-Suite-CVE-2025-61882/" target="_blank">watchTowr-vs-Oracle-E-Business-Suite-CVE-2025-61882</a> - Detection Artifact Generator for Oracle E-Business Suite CVE-2025-61882. Full details in <a href="https://labs.watchtowr.com/well-well-well-its-another-day-oracle-e-business-suite-pre-auth-rce-chain-cve-2025-61882well-well-well-its-another-day-oracle-e-business-suite-pre-auth-rce-chain-cve-2025-61882/" target="_blank">Well, Well, Well. It’s Another Day.</a></li>
<li><a href="https://github.com/RootUp/XRayC2" target="_blank">XRayC2</a> - AWS X-Ray for Covert Command &amp; Control. Write up at <a href="https://medium.com/@dhiraj_mishra/ghost-in-the-cloud-weaponizing-aws-x-ray-for-command-control-7539d60f1d77" target="_blank">Ghost in the Cloud: Weaponizing AWS X-Ray for Command &amp; Control</a>.</li>
<li><a href="https://github.com/Adaptix-Framework/templates-extender" target="_blank">templates-extender</a> - Templates for developing your own listeners and agents for AdaptixC2.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/trustedsec/Titanis/" target="_blank">Titanis</a> - Windows protocol library, including SMB and RPC implementations, among others. [I missed this last week despite tweeting about it 🤦‍♂️]</li>
<li><a href="https://github.com/dis0rder0x00/obex" target="_blank">obex</a> - Blocking unwanted DLLs in user mode.</li>
<li><a href="https://github.com/goichot/OverLAPS" target="_blank">OverLAPS</a> - Supporting PoCs and scripts for my talk "OverLAPS: Overriding LAPS Logic".</li>
<li><a href="https://geospy.ai/" target="_blank">Unlock the Power of AI Image intelligence</a> - The demo gif on the homepage is worth a watch. Every image you post is now leaking your location.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 458 (+0)</p>
<p>Blogs monitored: 424 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>X: <a href="https://x.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
