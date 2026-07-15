Title: Last Week in Security (LWiS) - 2022-09-06
Date: 2022-09-06 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-09-06
Author: Erik
Summary: Nmap turns 25 (<a href="https://twitter.com/nmap" target="_blank">@nmap</a>), PersistAssist (<a href="https://twitter.com/Grimmie" target="_blank">@Grimmie</a>), SCM attack toolkit (<a href="https://twitter.com/h4wkst3r" target="_blank">@h4wkst3r</a>), nf_tables privesc (<a href="https://twitter.com/saidelike" target="_blank">@saidelike</a>), the BloodHound Attack Research Kit (<a href="https://twitter.com/_wald0" target="_blank">@_wald0</a>), MS Teams Phreaking (<a href="https://twitter.com/moritz_abrell" target="_blank">@moritz_abrell</a>), blinding Sysmon (<a href="https://twitter.com/testert01" target="_blank">@testert01</a> + <a href="https://twitter.com/thefLinkk" target="_blank">@thefLinkk</a>), EvilnoVNC (<a href="https://twitter.com/JoelGMSec" target="_blank">@JoelGMSec</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-08-29 to 2022-09-06.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://seclists.org/nmap-announce/2022/1" target="_blank">Nmap 7.93 - 25th Anniversary Release!</a>. The network scanner you know and love turns 25.</li>
<li><a href="https://www.vice.com/en/article/k7b3bz/china-accuses-nsa-hacking-military-research-university" target="_blank">China Accuses NSA of Hacking Its Military Research University</a> “Regardless of whether the claims are true or false, this coordination of official statements and covert activity may be part of a broader propaganda campaign to negatively portray the U.S. and show off Chinese cybersecurity capabilities,” Zhang told VICE World News.</li>
<li><a href="https://twitter.com/malwrhunterteam/status/1559244860636413952" target="_blank">Clop ransomware gang published screenshots that show SCADA interfaces for a UK water supplier</a>. This is not the first ICS hack, and will not be the last. The stakes of cybersecurity are only increasing as we become more connected and reliant on connected infrastructure.</li>
<li><a href="https://www.thetechoutlook.com/news/technology/security/was-tiktok-hacked-by-a-user-against-the-west/?mc_cid=24dbc826cf&amp;mc_eid=ad8c97ece0" target="_blank">Was tiktok hacked by a user 'Against the West'?</a>. It's still not clear if this was an actual breach or a breach of a 3rd party scraping service.</li>
<li><a href="https://outflank.nl/outflank-2.0/" target="_blank">HelpSystems welcomes Outflank</a>. The Dutch cybersecurity startup with some impressive tooling and initial access work gets acquired by the US based HelpSystems who also scooped up Cobalt Strike. This may aid US based purchases of Outflanks "Offensive Security Toolkit."</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.fox-it.com/2022/09/02/sharkbot-is-back-in-google-play/" target="_blank">Sharkbot is back in Google Play</a>. Good breakdown of Android malware.</li>
<li><a href="https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/" target="_blank">How to Decrypt Manage Engine PMP Passwords for Fun and Domain Admin - a Red Teaming Tale</a>. It's a great day when you can find and decrypt password managers on red team engagements. The use of a password manager to diversify passwords across sites and generate truly random passwords still greatly outweighs the risk of having all passwords centralized. My go-to recommendation is Bitwarden, an open source option that just <a href="https://bitwarden.com/blog/accelerating-value-for-bitwarden-users-bitwarden-raises-usd100-million/" target="_blank">raised $100 million</a>. You can self-host the backend with <a href="https://github.com/dani-garcia/vaultwarden" target="_blank">vaultwarden</a> and use the official applications, but their free tier is good enough for many use cases.</li>
<li><a href="https://fortynorthsecurity.com/blog/persistassist-your-persistence-assistant/" target="_blank">PersistAssist: Your Persistence Assistant!</a>. PersistAssist is a fully modular persistence framework written in C# which automates persistence deployment and clean up. Code <a href="https://github.com/FortyNorthSecurity/PersistAssist" target="_blank">here</a>.</li>
<li><a href="https://posts.specterops.io/automating-azure-abuse-research-part-2-3e5bbe7a20c0" target="_blank">Automating Azure Abuse Research — Part 2</a>. This post dives into the BloodHound Attack Research Kit (<a href="https://github.com/BloodHoundAD/BARK" target="_blank">BARK</a>) and explains how the BloodHound Enterprise team uses BARK to perform so-called “continuous abuse primitive validation.”</li>
<li><a href="https://research.nccgroup.com/2022/09/01/settlers-of-netlink-exploiting-a-limited-uaf-in-nf_tables-cve-2022-32250/" target="_blank">SETTLERS OF NETLINK: Exploiting a limited UAF in nf_tables (CVE-2022-32250)</a>. The amount of work for a modern Linux privesc to work is impressive. This post breaks down each step of the exploitation discovery process.</li>
<li><a href="https://blog.syss.com/posts/abusing-ms-teams-direct-routing/" target="_blank">Abusing Microsoft Teams Direct Routing</a>. An external, unauthenticated attacker is able to send specially crafted SIP messages, that pretend to originate from Microsoft and are therefore correctly classified by the victim's Session Border Controller. As a result, unauthorized external calls are made through the victim's phone line (toll fraud).</li>
<li><a href="https://codewhitesec.blogspot.com/2022/09/attacks-on-sysmon-revisited-sysmonente.html" target="_blank">Attacks on Sysmon Revisited - SysmonEnte</a>. The state of the art in blinding Sysmon has arrived. <a href="https://github.com/codewhitesec/SysmonEnte" target="_blank">SysmonEnte</a> is an impressive tool.</li>
<li><a href="https://www.naksyn.com/edr%20evasion/2022/09/01/operating-into-EDRs-blindspot.html" target="_blank">Living-Off-the-Blindspot - Operating into EDRs' blindspot</a>. Signed, widely used tools combined with lack of dynamic code introspection makes the perfect storm for EDR evasion.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://ssd-disclosure.com/ssd-advisory-linux-config_watch_queue-lpe/" target="_blank">SSD Advisory - Linux CONFIG_WATCH_QUEUE LPE</a>. A vulnerability in the way Linux handles the CONFIG_WATCH_QUEUE allows local attackers to reach a race condition and use this to elevate their privileges to root. PoC and Exploit included.</li>
<li><a href="https://github.com/JoelGMSec/EvilnoVNC" target="_blank">EvilnoVNC</a> - Ready to go Phishing Platform built on noVNC. Why intercept creds when you can have your victim use a real browser you control?</li>
<li><a href="https://github.com/MWR-CyberSec/PXEThief" target="_blank">PXEThief</a> is a set of tooling that can extract passwords from the Operating System Deployment functionality in Microsoft Endpoint Configuration Manager. You'll probably also want <a href="https://github.com/MWR-CyberSec/configmgr-cryptderivekey-hashcat-module" target="_blank">configmgr-cryptderivekey-hashcat-module</a>, a Hashcat module that can crack a password used to derive an AES-128 key with CryptDeriveKey from CryptoAPI.</li>
<li><a href="https://github.com/hackerhouse-opensource/MsSettingsDelegateExecute" target="_blank">MsSettingsDelegateExecute</a>. Bypass UAC on Windows 10/11 x64 using ms-settings DelegateExecute registry key.</li>
<li><a href="https://github.com/hackerhouse-opensource/NoFaxGiven" target="_blank">NoFaxGiven</a>. Code Execution &amp; Persistence in NETWORK SERVICE FAX Service.</li>
<li><a href="https://web.archive.org/web/20220906052810/https://github.com/veritas501/CVE-2022-2639-PipeVersion/blob/master/exploit.c" target="_blank">CVE-2022-2639-PipeVersion</a>. It was taken down before I even got to it. Untested. Kernels 3.13 to 5.18 are vulnerable (<a href="https://github.com/torvalds/linux/commit/cefa91b2332d7009bc0be5d951d6cbbf349f90f8" target="_blank">fix</a> committed 2022-04-15).</li>
<li><a href="https://github.com/dr4k0nia/Origami" target="_blank">Origami</a> - Packer compressing .net assemblies, (ab)using the PE format for data storage. Updated last week with .NET Core support, Costura support, and a simplified loader.</li>
<li><a href="https://github.com/ps1337/reinschauer" target="_blank">reinschauer</a> - A PoC to remotely control Windows machines over Websockets.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/h4wkst3r/SCMKit" target="_blank">SCMKit</a> allows the user to specify the Source Code Management system and attack module to use, along with specifying valid credentials (username/password or API key) to the respective SCM system. Currently, the SCM systems that SCMKit supports are GitHub Enterprise, GitLab Enterprise and Bitbucket Server. The attack modules supported include reconnaissance, privilege escalation and persistence.</li>
<li><a href="https://github.com/headwaymaps/headway" target="_blank">Headway</a> Self-hostable maps stack, powered by OpenStreetMap.</li>
<li><a href="https://it.digitaino.com/use-touchid-to-authenticate-sudo-on-macos/" target="_blank">Use TouchID to Authenticate sudo on macOS</a>. Your TouchID equipped Mac can easily be configured to use your fingerprint to approve sudo commands.</li>
<li><a href="https://universalshards.com/p/the-immediate-sound-of-distant-hammers" target="_blank">The Immediate Sound of Distant Hammers</a>. The first sci-fi short story from Universal Shards in over a year!</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 420 (+0)</p>
<p>Blogs monitored: 322 (+2)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
