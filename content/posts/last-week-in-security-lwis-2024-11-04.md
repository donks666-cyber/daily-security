Title: Last Week in Security (LWiS) - 2024-11-04
Date: 2024-11-04 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-11-04
Author: Erik
Summary: WAF bypasses (<a href="https://x.com/MDSecLabs" target="_blank">@MDSecLabs</a>), sastsweep (<a href="https://x.com/_chebuya" target="_blank">@_chebuya</a>), Early Cascade injection (<a href="https://x.com/DaWouw" target="_blank">@DaWouw</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-10-28 to 2024-11-04.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://blog.eclecticiq.com/inside-intelligence-center-lunar-spider-enabling-ransomware-attacks-on-financial-sector-with-brute-ratel-c4-and-latrodectus" target="_blank">Inside Intelligence Center: LUNAR SPIDER Enabling Ransomware Attacks on Financial Sector with Brute Ratel C4 and Latrodectus</a> - Cybercrime is adapting to the high corporate emphasis of Cobalt Strike detections/preventions.</li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2024/10/29/midnight-blizzard-conducts-large-scale-spear-phishing-campaign-using-rdp-files/" target="_blank">Midnight Blizzard conducts large-scale spear-phishing campaign using RDP files</a> - Russian threat actor is performing some intelligence collection operations. It's making headlines since threat actors are using a signed Remote Desktop Protocol (RDP) configuration file that connected to an actor-controlled server.</li>
<li><a href="https://www.justice.gov/usao-wdtx/pr/us-joins-international-action-against-redline-and-meta-infostealers" target="_blank">U.S. Joins International Action Against RedLine and META Infostealers</a> - US Department of justice and a European coalition have teamed up to disrupt Redline and META infosealers in <a href="https://www.operation-magnus.com/" target="_blank">Operation Magnus</a>.</li>
<li><a href="https://tmpout.sh/blog/vol4-cfp.html" target="_blank">tmp.0ut Volume 4 Call For Papers</a> - The site lists the areas they are looking for, including beginner-level content for some areas.</li>
<li><a href="https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html" target="_blank">From Naptime to Big Sleep: Using Large Language Models To Catch Vulnerabilities In Real-World Code</a> - Google is using large language models for bug hunting, and found an exploitable SQLite buffer overflow.</li>
<li><a href="https://community.kde.org/KDE_Linux" target="_blank">KDE Linux</a> - The KDE group releases their own Arch Linux based OS, not to be confused with <a href="https://neon.kde.org/" target="_blank">KDE neon</a>, which is Ubuntu based.</li>
<li><a href="https://trust.okta.com/security-advisories/okta-ad-ldap-delegated-authentication-username" target="_blank">Okta AD/LDAP Delegated Authentication - Username Above 52 Characters Security Advisory</a> - A username longer than 52 characters could cause a hash collision with cached authentication under certain conditions.</li>
<li><a href="https://www.msspalert.com/news/mssp-market-update-comptia-sold-to-private-equity" target="_blank">MSSP Market Update: CompTIA Sold to Private Equity</a> - The acquisitions in the training space continue, last week was Offsec, this week is CompTIA.</li>
<li><a href="https://www.cbc.ca/news/canada/canada-revenue-agency-taxpayer-accounts-hacked-1.7363440" target="_blank">Tens of thousands of taxpayer accounts hacked as CRA repeatedly paid out millions in bogus refunds</a> - The Canada Revenue Agency discovered that threat actors obtained confidential data used by one of the country's largest tax preparation firms, H&amp;R Block Canada.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.landh.tech/blog/20241028-hidden-supply-chain-links/" target="_blank">Exploiting Fortune 500 Through Hidden Supply Chain Links</a> - Supply chain will continue to be an issue for a good while. If you're a red teamer, you should be adding this to your toolkit. This article walks through a dependency confusion vulnerability in HashiCorp's Consul which affected fortune 500.</li>
<li><a href="https://posts.specterops.io/bofhound-ad-cs-integration-91b706bc7958" target="_blank">BOFHound: AD CS Integration</a> - TL;DR: BOFHound can now parse Active Directory Certificate Services (AD CS) objects, manually queried from LDAP, for review and attack path mapping within BloodHound Community Edition (BHCE).</li>
<li><a href="https://www.synacktiv.com/en/publications/exploiting-a-blind-format-string-vulnerability-in-modern-binaries-a-case-study-from" target="_blank">Exploiting a Blind Format String Vulnerability in Modern Binaries: A Case Study From Pwn2own Ireland 2024</a> - Some hardcore format string exploitation in the face of modern security measures such as Address Space Layout Randomization (ASLR), Position Independent Executables (PIE), Non-Executable memory (NX), and Full Relocation Read-Only (Full RelRO).</li>
<li><a href="https://www.sophos.com/en-us/content/pacific-rim" target="_blank">Inside the counter-offensive tactics, techniques, and procedures used to neutralize China-based threats</a> - Sophos did a little "Defend Forward" and dropped "implants" (not malware 🤣) on devices used by Chinese exploit developers to watch them as they developed their new exploits. Check out the <a href="https://news.sophos.com/en-us/2024/10/31/pacific-rim-timeline/" target="_blank">timeline</a> for a detailed breakdown of their operations.</li>
<li><a href="https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/" target="_blank">TA Phone Home: EDR Evasion Testing Reveals Extortion Actor's Toolkit</a> - Another example of security vendors using their access to monitor threat actors. If you're a red team developer, and aren't using Ludus' <a href="https://docs.ludus.cloud/docs/quick-start/testing-mode" target="_blank">testing mode</a> you are exposing your tooling.</li>
<li><a href="https://www.mdsec.co.uk/2024/10/when-wafs-go-awry-common-detection-evasion-techniques-for-web-application-firewalls/" target="_blank">When WAFs Go Awry: Common Detection &amp; Evasion Techniques for Web Application Firewalls</a> - Background and bypasses for web application firewalls.</li>
<li><a href="https://www.outflank.nl/blog/2024/10/15/introducing-early-cascade-injection-from-windows-process-creation-to-stealthy-injection/" target="_blank">Introducing Early Cascade Injection: From Windows Process Creation to Stealthy Injection</a> - After some background on process creation in Windows and Early Bird APC injection, a new process injection technique - Early Cascade injection - is introduced. However, outflank will "will not make the source code of this project public" but you can pay them for it 😉.</li>
<li><a href="https://secureyourit.co.uk/wp/2024/11/02/living-off-the-land/" target="_blank">Living off the land</a> - A quick post on using Microsoft Software Center UI to elevate from Administrator to SYSTEM.</li>
<li><a href="https://theevilbit.github.io/beyond/beyond_0035/" target="_blank">Beyond the good ol' LaunchAgents - 35 - Persist through the NVRAM - The 'apple-trusted-trampoline'</a> - This can only be used with System Integrity Protection (SIP) is disabled, so its not all that practical, but its a good look into what is possible with NVRAM.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Hacker-Hermanos/rustmerger" target="_blank">rustmerger</a> - A robust command-line tool built in Rust that makes merging and deduplicating text files a breeze. Whether you're dealing with small files or massive datasets, this tool handles the heavy lifting with parallel processing and smart error handling.</li>
<li><a href="https://github.com/EQSTLab/CVE-2024-46538" target="_blank">CVE-2024-46538</a> - PfSense Stored XSS leads to remote code execution, proof of concept.</li>
<li><a href="https://github.com/Scorpion-Security-Labs/OpenHashAPI" target="_blank">OpenHashAPI</a> - OpenHashAPI (OHA) is designed to store and maintain hashes and plaintext in a centralized database. OHA is written in Go and designed for containerized deployment. For more information see <a href="https://jakewnuk.com/static/No%20Cap%20Cracking%20Improving%20Offline%20Hash%20Recovery%20Methodologies.pdf" target="_blank">[PDF] No Cap Cracking: Improving Offline Hash Recovery Methodologies</a>.</li>
<li><a href="https://github.com/chebuya/sastsweep" target="_blank">sastsweep</a> - Automatically detect potential vulnerabilities and analyze repository metrics to prioritize open source security research targets.</li>
<li><a href="https://github.com/logangoins/Cable" target="_blank">Cable</a> - .NET post-exploitation toolkit for Active Directory reconnaissance and exploitation.</li>
<li><a href="https://github.com/joaoviictorti/rustclr" target="_blank">rustclr</a> is a powerful library for hosting the Common Language Runtime (CLR) and executing .NET binaries directly with Rust, among other operations.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/rofl0r/microsocks" target="_blank">microsocks</a> - a SOCKS5 service that you can run on your remote boxes to tunnel connections through them, if for some reason SSH doesn't cut it for you.</li>
<li><a href="https://cicada-8.medium.com/hijack-the-typelib-new-com-persistence-technique-32ae1d284661" target="_blank">Hijack the TypeLib. New COM persistence technique</a> - Introduces <a href="https://github.com/CICADA8-Research/TypeLibWalker" target="_blank">TypeLibWalker</a> to persist via TypeLib hijacking on Windows.</li>
<li><a href="https://github.com/ScrapeGraphAI/Scrapegraph-ai" target="_blank">Scrapegraph-ai</a> - Python scraper based on AI.</li>
<li><a href="https://knifecoat.com/Posts/Through+the+Looking+Glass" target="_blank">Through the Looking Glass</a> - A small post about tunnelling UDP over TCP and WireGuard Site-to-Site VPN configurations.</li>
<li><a href="https://github.com/owasp-noir/noir" target="_blank">noir</a> - Attack surface detector that identifies endpoints by static analysis.</li>
<li><a href="https://github.com/chartdb/chartdb" target="_blank">chartdb</a> - Free and open-source database diagrams editor, visualize and design your DB with a single query.</li>
<li><a href="https://github.com/MightyMoud/sidekick" target="_blank">sidekick</a> -  Bare metal to production ready in mins; your own fly server on your VPS.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 439 (+0)</p>
<p>Blogs monitored: 396 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
