Title: Last Week in Security (LWiS) - 2025-07-14
Date: 2025-07-14 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-07-14
Author: Erik
Summary: LudusHound (<a href="https://x.com/bagelByt3s" target="_blank">@bagelByt3s</a>), SpeechRuntimeMove (<a href="https://x.com/ShitSecure" target="_blank">@ShitSecure</a>), Havoc Pro (<a href="https://x.com/C5pider" target="_blank">@C5pider</a>), FortiWeb RCE (<a href="https://x.com/SinSinology" target="_blank">@SinSinology</a>), SailPoint IQService RCE (<a href="https://x.com/NetSPI" target="_blank">@NetSPI</a>), Altiris RCE (<a href="https://x.com/lefterispan" target="_blank">@lefterispan</a>), WAF bypass (<a href="https://x.com/nyxgeek" target="_blank">@nyxgeek</a> ), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-07-07 to 2025-07-14.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.infinitycurve.org/blog/introduction" target="_blank">Havoc Professional: A Lethal Presence</a> - <a href="https://github.com/HavocFramework/Havoc" target="_blank">Havoc</a> made a splash when it was released on 2022-09-11. Now Paul (<a href="https://x.com/C5pider" target="_blank">@C5pider</a>) is gearing up to release a professional version with some unique features like a built in virtual machine.</li>
<li><a href="https://www.reuters.com/sustainability/boards-policy-regulation/meta-wont-tweak-pay-or-consent-model-further-despite-risk-eu-fines-sources-say-2025-07-11/" target="_blank">Exclusive: Meta won't tweak pay-or-consent model further despite risk of EU fines, sources say</a> - Meta has had enough of what it sees as EU over regulation. If you take away the data collection that allows Meta to be profitable, and not enough EU users opt to pay for Meta services, I don't see why Meta would continue to operate in the EU. People have been conditioned to pay for services with their data, in part thanks to services like Facebook, but the genie is out of the bottle. Will EU citizens call for change if Meta pulls completely out of the EU? Would any other social media site dare to grow in the EU if they knew they could simply be shut off by regulators?</li>
<li><a href="https://krebsonsecurity.com/2025/07/uk-charges-four-in-scattered-spider-ransom-group/" target="_blank">UK Arrests Four in ‘Scattered Spider’ Ransom Group</a> - The gang famous for calling up IT support and resetting employee passwords to gain access to sensitive systems is slowly getting arrested. The oldest was only 20 years old.</li>
<li><a href="https://blog.raw.pm/en/about-the-hype-around-xbow/" target="_blank">About the hype around XBOW</a> - "XBOW is an AI that is 1st on HackerOne," is a technically true statement, but with a lot of caveats.</li>
<li><a href="https://www.theguardian.com/world/2025/jul/08/swedish-pm-safety-strava-data-bodyguards-ulf-kristersson-running-cycling-routes" target="_blank">Swedish PM’s private address revealed by Strava data shared by bodyguards</a> - This is at least the 4th public incident of OPSEC fails on Strava. Default public is a bad default. Previously it was <a href="https://www.securityweek.com/fitness-app-strava-gives-away-location-of-biden-trump-and-other-leaders-french-newspaper-says/" target="_blank">U.S. Secret Service</a>, or <a href="https://www.lemonde.fr/en/france/article/2024/10/27/how-emmanuel-macron-can-be-tracked-watch-the-first-episode-of-stravaleaks_6730708_7.html" target="_blank">Emmanuel Macron's Bodyguards</a>, or <a href="https://www.theguardian.com/world/2018/jan/28/fitness-tracking-app-gives-away-location-of-secret-us-army-bases" target="_blank">secret US army bases</a>.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://specterops.io/blog/2025/07/14/ludushound-raising-bloodhound-attack-paths-to-life/" target="_blank">LudusHound: Raising BloodHound Attack Paths to Life</a> - What if you could rebuild your/your customer's network in your lab, automatically? Every Active Directory object and relationship, including user accounts, group structures, delegation settings, GPO links, and domain trusts? Now you can thanks to Beyviel David's work! LudusHound connects to a BloodHound server via its API and creates a <a href="https://ludus.cloud/" target="_blank">Ludus</a> configuration file that can be used to build a network in Ludus. The community that's been building on Ludus, expanding it with features, roles, templates, and tools is really cool to see.</li>
<li><a href="https://www.r-tec.net/r-tec-blog-revisiting-cross-session-activation-attacks.html" target="_blank">Revisiting Cross Session Activation Attacks</a> - A remote COM hijack that allows code execution in the context of a user session on a remote machine is a powerful lateral movement technique. Imagine having admin access to a machine that a domain admin is logged into, and getting a callback as the domain admin without having to dump credentials or inject into processes.</li>
<li><a href="https://labs.watchtowr.com/pre-auth-sql-injection-to-rce-fortinet-fortiweb-fabric-connector-cve-2025-25257/" target="_blank">Pre-Auth SQL Injection to RCE - Fortinet FortiWeb Fabric Connector (CVE-2025-25257)</a> - Unauthenticated SQL Injection. <a href="https://github.com/watchtowrlabs/watchTowr-vs-FortiWeb-CVE-2025-25257?ref=labs.watchtowr.com" target="_blank">POC for CVE-2025-25257</a> also dropped. Yes, this one is NEW. Worth noting this was "discovered" in February so don't forget to hunt through your data from this year. There are some really fun tricks to SQLi exploitation in this write up from the king of RCE, Sina Kheirkhah.</li>
<li><a href="https://www.synacktiv.com/en/publications/from-cheap-iot-toy-to-your-smartphone-getting-rce-by-leveraging-a-companion-app" target="_blank">From Cheap IOT Toy to Your Smartphone: Getting Rce by Leveraging a Companion App</a> - That app on your phone may open you up to exploits over the network when the package vulnerable libraries. Android still makes it difficult, but where there is a will, there is a shell.</li>
<li><a href="https://aff-wg.org/2025/07/13/taking-them-to-the-shitter-an-analysis-of-vendor-abuse-of-security-research-in-the-wild/" target="_blank">Taking them to the SHITTER: an analysis of vendor abuse of security research in-the-wild</a> - Raphael Mudge is in his <a href="https://www.youtube.com/watch?v=XamC7-Pt8N0" target="_blank">F*** You</a> era and I'm here for it. Can't we all just get along and respect the work of others? I wonder how much the marketing team was involved with the wording of the post? Mudge also released an update to <a href="https://aff-wg.org/2025/07/09/tradecraft-garden-tilling-the-soil/" target="_blank">Tradecraft Garden</a>.</li>
<li><a href="https://gpuhammer.com/" target="_blank">GPUHammer: Rowhammer Attacks on GPU Memories are Practical</a> - Will you give up 10% of your GPU speed and 6.25% of your GPU's memory capacity to prevent bit flips? I doubt it.</li>
<li><a href="https://www.netspi.com/blog/technical-blog/network-pentesting/remote-code-execution-sailpoint-iqservice/" target="_blank">Set Sail: Remote Code Execution in SailPoint IQService via Default Encryption Key</a> - You won't be surprised to find the service runs as SYSTEM.</li>
<li><a href="https://www.lrqa.com/en/cyber-labs/remote-code-execution-in-broadcom-altiris-irm/" target="_blank">CVE-2025-5333: Remote Code Execution in Broadcom Altiris IRM</a> - Sometime the endpoint detection and response (EDR) software is the initial access vector are the same.</li>
<li><a href="https://trustedsec.com/blog/azures-front-door-waf-wtf-ip-restriction-bypass" target="_blank">Azure's Front Door WAF WTF: IP Restriction Bypass</a> - What determines the IP of a request? Microsoft thinks a header is good enough.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/rtecCyberSec/SpeechRuntimeMove" target="_blank">SpeechRuntimeMove</a> - Lateral Movement as loggedon User via Speech Named Pipe COM &amp; ISpeechNamedPipe + COM Hijacking.</li>
<li><a href="https://github.com/Wh04m1001/CVE-2025-48799" target="_blank">CVE-2025-48799</a> - This is PoC for CVE-2025-48799, an elevation of privilege vulnerability in Windows Update service.</li>
<li><a href="https://github.com/ChoiSG/SharpSilentChrome" target="_blank">SharpSilentChrome</a> - SharpSilentChrome is a C# project that "silently" installs browser extensions on Google Chrome or MS Edge by updating the browsers' Preferences and Secure Preferences files. Currently, it only supports Windows. [Check out <a href="https://ludus.cloud/" target="_blank">Ludus</a> in the PoC video!]</li>
<li><a href="https://github.com/socfortress/wazuh-mcp-server" target="_blank">wazuh-mcp-server</a> - Repo to hold wazuh manager mcp server.</li>
<li><a href="https://github.com/nyxgeek/frontdoor_waf_wtf" target="_blank">frontdoor_waf_wtf</a> - Script to check Azure Front Door WAF for insecure RemoteAddr variable.</li>
<li><a href="https://github.com/vysecurity/ExfilServer" target="_blank">ExfilServer</a> - Client-side Encrypted Upload Server Python Script.</li>
<li><a href="https://github.com/BlWasp/WDSFinder" target="_blank">WDSFinder</a> - A simple tool to identify WDS servers in Active Directory.</li>
<li><a href="https://github.com/Idov31/NovaHypervisor" target="_blank">NovaHypervisor</a> - NovaHypervisor is a defensive x64 Intel host based hypervisor. The goal of this project is to protect against kernel based attacks (either via Bring Your Own Vulnerable Driver (BYOVD) or other means) by safeguarding defense products (AntiVirus / Endpoint Protection) and kernel memory structures and preventing unauthorized access to kernel memory.</li>
<li><a href="https://github.com/ricardojoserf/DoubleTeam" target="_blank">DoubleTeam</a> - Listener that spawns a new tmux window for each incoming reverse shell + Supports listening on many ports.</li>
<li><a href="https://github.com/badhive/stitch" target="_blank">stitch</a> - Rewrite and obfuscate code in compiled binaries.</li>
<li><a href="https://github.com/liamg/CVE-2025-48384" target="_blank">CVE-2025-48384</a> - PoC for CVE-2025-48384 - Breaking Git with a carriage return and cloning RCE. More info <a href="https://dgl.cx/2025/07/git-clone-submodule-cve-2025-48384#_" target="_blank">here</a>.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/AlmondOffSec/DCOMRunAs" target="_blank">DCOMRunAs</a> - Lateral movement with DCOM DLL hijacking.</li>
<li><a href="https://github.com/Alia5/PiCCANTE" target="_blank">PiCCANTE</a> - PiCCANTE is a powerful tool for exploring and reversing CAN busses of vehicles, based on Raspberry Pi Pico (any model).</li>
<li><a href="https://github.com/MickeyDB/Neo4jWordlistHarvester" target="_blank">Neo4jWordlistHarvester</a> - LdapWordlistHarvester but then with neo4j.</li>
<li><a href="https://forms.gle/SGLqk7ADWKnJNsR97" target="_blank">Hacker Family Feaud Survey</a> - Fill out this quick survey to create the answers to a "Hacker Family Feud" content for DEF CON 33.</li>
<li><a href="https://github.com/alexpasmantier/television" target="_blank">television</a> - A cross-platform, fast and extensible general purpose fuzzy finder 📺.</li>
<li><a href="https://github.com/TheManticoreProject/FindOldSIDTraces" target="_blank">FindOldSIDTraces</a> - A cross-platform tool to find traces of old SIDs remaining in LDAP objects of the Active Directory.</li>
<li><a href="https://github.com/two06/LinkedIntel" target="_blank">LinkedIntel</a> - LinkedIn recon the easy way.</li>
<li><a href="https://arxiv.org/abs/2507.07210" target="_blank">WatchWitch: Interoperability, Privacy, and Autonomy for the Apple Watch</a> - Researchers reverse engineered the closed down ecosystem of Apple Watches and opened compatability with Android.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 455 (+0)</p>
<p>Blogs monitored: 423 (+0)</p>
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
