Title: Last Week in Security (LWiS) - 2024-02-07
Date: 2024-02-07 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-02-07
Author: Erik
Summary: All the Ivanti 0days, FTX SIM swap (<a href="https://twitter.com/briankrebs" target="_blank">@briankrebs</a>), Unmanaged CLR patching (<a href="https://twitter.com/kyleavery_" target="_blank">@kyleavery_</a>), Midnight Blizzard fallout (<a href="https://twitter.com/_wald0" target="_blank">@_wald0</a>), Arachne mythic webshell (<a href="https://twitter.com/its_a_feature_" target="_blank">@its_a_feature_</a> ), and more!

<aside class="m-note m-success">
<h3>Ludus Release</h3>
<p>Our latest project, Ludus - the easiest way to deploy and manage testing infrastructure, is now live and fully open source! It will greatly improve your red or blue team quality of life.
Let us know what you think!</p>
<p><a href="https://ludus.cloud" target="_blank">ludus.cloud</a></p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-01-29 to 2024-02-07.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://anydesk.com/en/public-statement" target="_blank">AnyDesk Incident Response 2-2-2024</a> - An RMM company, AnyDesk, was breached. "Customers Urged to Reset Passwords." Is breaching the upstream RMM company the ultimate traitorware?</li>
<li><a href="https://forums.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways?language=en_US" target="_blank">Ivanti</a> - We're up to four (4) CVEs. <a href="https://www.cisa.gov/news-events/directives/supplemental-direction-v1-ed-24-01-mitigate-ivanti-connect-secure-and-ivanti-policy-secure" target="_blank">CISA</a> is ordering everyone to disconnect all instances of Ivanti Connect Secure and Ivanti Policy Secure solution products from agency networks. Even Assetnote is getting in the action with a <a href="https://www.assetnote.io/resources/research/ivantis-pulse-connect-secure-auth-bypass-round-two" target="_blank">new authentication bypass</a>. What a mess!</li>
<li><a href="https://blog.cloudflare.com/thanksgiving-2023-security-incident" target="_blank">Thanksgiving 2023 security incident</a> - Threat actor utilized stolen credentials from the October 2023 <a href="https://sec.okta.com/articles/2023/10/tracking-unauthorized-access-oktas-support-system" target="_blank">Okta</a> compromise to access Cloudflare's network. TLDR - Threat actors were in Cloudflare's internal wiki, bug database, and established persistent access to the Atlassian server but 2FA prevented most lateral movement. Cloudflare even returned the hardware that was connected to a console server the actors attempted but failed to gain access to. Now that is serious remediation!</li>
<li><a href="https://www.windowslatest.com/2024/02/01/first-look-windows-11-is-getting-native-macos-or-linux-like-sudo-command/" target="_blank">First look: Windows 11 is getting native macOS or Linux-like Sudo command</a> - The Sudo, “superuser do,” command is coming to Windows 11 as part of the developer settings. <a href="https://en.wikipedia.org/wiki/Embrace,_extend,_and_extinguish" target="_blank">Embrace, extend, and extinguish</a>.</li>
<li><a href="https://bughunters.google.com/blog/4562175388155904/externalizing-the-google-domain-tiers-concept" target="_blank">Externalizing the Google Domain Tiers Concept</a> - Google's Security Team has introduced the concept of <a href="https://github.com/google/bughunters/tree/main/domain-tiers" target="_blank">Domain Tiers</a>  to categorize approximately 10,000 domains based on sensitivity, helping prioritize security efforts. The tiering system, with five levels (Tier 0 being the highest sensitivity), aids in identifying potential vulnerabilities and influences Google Vulnerability Reward payouts. This is really dope!</li>
<li><a href="https://www.resecurity.com/blog/article/hundreds-of-network-operators-credentials-found-circulating-in-dark-web" target="_blank">Hundreds of network operators' credentials found circulating in the Dark Web</a> - An attacker named 'Snow' compromised RIPE NCC account credentials, leading to a three-hour service outage and over 1,572 compromised customer credentials across various regional internet registries. Fun times.</li>
<li><a href="https://www.bleepingcomputer.com/news/security/vastaamo-hacker-traced-via-untraceable-monero-transactions-police-says/" target="_blank">Vastaamo hacker traced via 'untraceable' Monero transactions, police says</a> - "KRP did not disclose the exact mechanism for tracing the Monero transactions, citing the need to protect sensitive investigative techniques that can prove invaluable in future cases. Thus, the exact methods involved are unclear." However, the suspect used a centralize exchange to exchange between BTC and XMR and eventually an email address linked to a server managed by the suspect. Seems like a lot of opportunities to find the suspect other than breaking XMR privacy, and I highly doubt that has happened. <a href="https://www.binance.com/en/support/announcement/binance-will-delist-ant-multi-vai-xmr-on-2024-02-20-f73b083ba6834771b07dbe5319917ae5" target="_blank">Binance Will Delist XMR on 2024-02-20</a>, which may be related. Reminder: the <a href="https://www.un.org/en/about-us/universal-declaration-of-human-rights" target="_blank">Universal Declaration of Human Rights</a> Article 12 states privacy is a universal human right and not a crime. Using XMR for crimes is a crime, the same way using USD cash for crimes is a crime.</li>
<li><a href="https://krebsonsecurity.com/2024/02/arrests-in-400m-sim-swap-tied-to-heist-at-ftx/" target="_blank">Arrests in $400M SIM-Swap Tied to Heist at FTX?</a>. Three Americans charged with orchestrating SIM-swapping attacks resulting in over $400 million of stolen crypto, likely from FTX. The attacks took place between March 2021 and April 2023. There is no excuse to use SMS based 2FA for anything important after all these SIM swaps. Phone companies are not the place to outsource your identity verification!</li>
<li><a href="https://blog.qualys.com/vulnerabilities-threat-research/2024/01/30/qualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog" target="_blank">Qualys TRU Discovers Important Vulnerabilities in GNU C Library's syslog()</a>. The two technical write ups are linked at the bottom of the post. Put CVE-2023-6246, CVE-2023-6779, and CVE-2023-6780 on your PoC watch list as they will be nice Linux LPEs.</li>
<li><a href="https://www.cnn.com/2024/02/04/asia/deepfake-cfo-scam-hong-kong-intl-hnk/index.html" target="_blank">Finance worker pays out $25 million after video call with deepfake 'chief financial officer'</a>. The best deepfake we know about. Put this on your "why you should care" slide for your next vishing assessment.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://practical365.com/mfa-status-user-accounts/" target="_blank">How to Report the MFA Status for Entra ID User Accounts</a> - Good defender/sysadmin article to deduce who's using MFA by combining authentication methods &amp; signin logs.</li>
<li><a href="https://sensepost.com/blog/2024/sensecon-23-from-windows-drivers-to-an-almost-fully-working-edr/" target="_blank">Sensecon 23: from Windows drivers to an almost fully working EDR</a> - The author of the post wrote <a href="https://github.com/sensepost/mydumbedr" target="_blank">MyDumbEDR</a> to learn more about EDRs and windows internals. Awesome write-up!</li>
<li><a href="https://cloudbrothers.info/en/anonymous-ip-address-involving-apple-icloud-private-relay/" target="_blank">Anonymous IP address involving Apple iCloud Private Relay</a> - <a href="https://support.apple.com/en-us/102602" target="_blank">iCloud Private Relay</a> is being used by their iPhone users to "anonymize" their traffic. Well, that is causing some issues for defenders. Some defenders might allowlist these relays on their SIEM or security tooling. Time for red teams to look into using this if you haven't already.</li>
<li><a href="https://www.invictus-ir.com/news/the-curious-case-of-dangerdev-protonmail-me" target="_blank">The curious case of DangerDev@protonmail.me</a> - A detailed blog post on an AWS incident response use-case from a month long attack. Initial access via exposed access key, some recon via SES and IAM API calls, privilege escalation via AttachUserPolicy, and more.</li>
<li><a href="https://www.outflank.nl/blog/2024/02/01/unmanaged-dotnet-patching/" target="_blank">Unmanaged .NET Patching</a> - Patching .NET functions from an unmanaged CLR host, to massage managed code at runtime by <a href="https://twitter.com/kyleavery_" target="_blank">@kyleavery_</a>.</li>
<li><a href="https://www.mandiant.com/resources/blog/unc4990-evolution-usb-malware" target="_blank">Evolution of UNC4990: Uncovering USB Malware's Hidden Depths</a> - Always fun to read threat actor tradecraft. This one particularly stood out because threat actors are using vimeo[.]com and arstechnica[.]com to host payloads in addition to their usual registered domains.</li>
<li><a href="https://posts.specterops.io/microsoft-breach-what-happened-what-should-azure-admins-do-da2b7e674ebc" target="_blank">Microsoft Breach — What Happened? What Should Azure Admins Do?</a> - Excellent blog post to summarize the <a href="https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/" target="_blank">Midnight Blizzard</a> breach by Andy Robbins.</li>
<li><a href="https://lsecqt.github.io/Red-Teaming-Army/active-directory/enumeration/visualizing-acls-with-adalanche/" target="_blank">Visualizing ACLs with Adalanche</a> - An alternative to Bloodhound when enumerating AD. Maybe not as signatured as Sharphound for those looking for a quick option. We originally talked about Adalanche all the way back in LWiS 2021-06-14!</li>
<li><a href="https://hackerone.com/reports/2327341" target="_blank">CVE-2024-21733 Apache Tomcat HTTP Request Smuggling</a> - Imaging getting creds as your initial access on a red team by pulling this off 🤯. Of course the password was <cite>Dec2023!</cite>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/sleeptok3n/RoleCrawl" target="_blank">RoleCrawl</a> - PowerShell tool designed to audit User and Group role assignments in Azure, covering both subscription and resource scopes.</li>
<li><a href="https://github.com/cosad3s/hfinder" target="_blank">hfinder</a> - Help recon of hostnames from specific ASN or CIDR, thanks to Robtex and BGP.HE</li>
<li><a href="https://github.com/Slowerzs/ThievingFox" target="_blank">ThievingFox</a> - A collection of post-exploitation tools to gather credentials from various password managers and windows utilities. Came with a <a href="https://blog.slowerzs.net/posts/thievingfox/" target="_blank">blog post</a>.</li>
<li><a href="https://github.com/Cyb3rWard0g/IntelRAGU" target="_blank">IntelRAGU</a> - An open-source initiative to document and share experiments to apply Retrieval Augmented Generation (RAG) techniques to Threat Intelligence searching capabilities.</li>
<li><a href="https://github.com/MythicAgents/arachne" target="_blank">arachne</a> is a Mythic webshell payload for Windows (aspx) and Linux (php). When run alone, the arachne container reaches out to the specified URL to issue tasking. When an agent links via P2P to an arachne agent, then that agent will remotely reach out to the specified URL to issue tasking. Check out the blog: <a href="https://posts.specterops.io/spinning-webs-unveiling-arachne-for-web-shell-c2-26c40f570ea1" target="_blank">Spinning Webs — Unveiling Arachne for Web Shell C2</a>.</li>
<li><a href="https://github.com/Acebond/ReverseSocks5" target="_blank">ReverseSocks5</a> - Single executable reverse SOCKS5 proxy written in Golang. This is v2 which adds SOCKS5 support.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/d-Rickyy-b/certstream-server-go" target="_blank">certstream-server-go</a> - This project aims to be a drop-in replacement for the certstream server by Calidog. This tool aggregates, parses, and streams certificate data from multiple certificate transparency logs via websocket connections to the clients.</li>
<li><a href="https://github.com/mlcsec/SigFinder" target="_blank">SigFinder</a> - Identify binaries with Authenticode digital signatures signed to an internal CA/domain. This could be useful when pillaging SCCM distribution point servers.</li>
<li><a href="https://github.com/v-byte-cpu/wirez" target="_blank">wirez</a> - redirect all TCP/UDP traffic of any program to SOCKS5 proxy.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 367 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
