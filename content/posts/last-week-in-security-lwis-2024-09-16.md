Title: Last Week in Security (LWiS) - 2024-09-16
Date: 2024-09-16 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-09-16
Author: Erik
Summary: MSSQL domain privesc (<a href="https://x.com/_nullbind" target="_blank">@_nullbind</a>), .mobi whois takeover (<a href="https://x.com/watchtowrcyber" target="_blank">@watchtowrcyber</a>), LLM CTF (<a href="https://x.com/bishopfox" target="_blank">@bishopfox</a>), mac filesystem 🪄 (<a href="https://x.com/gergely_kalman" target="_blank">@gergely_kalman</a>), AlcaWASM writeup (<a href="https://x.com/suidpit/" target="_blank">@suidpit</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-09-09 to 2024-09-16.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://www.sprocketsecurity.com/resources/aob-sprocket-pentsters" style="color: #3bd267;" target="_blank">Sprocket Security - Ahead of the Breach Podcast</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p>The Sprocket Security testing team discusses innovative techniques and methodologies they frequently use as part of Continuous Penetration Testing. They talk about 403 bypass techniques, their favorite findings in the past few months, and Will Vandevanter's presentation at the DEF CON Recon village on his latest tool, <a href="https://github.com/BuffaloWill/whoiswatcher" target="_blank">whoiswatcher</a>.</p>
</aside><ul>
<li><a href="https://x.com/BetaProfiles/status/1834223912429015551" target="_blank">[X] Activation Lock for iPhone components</a> - iOS 18 will lock replaceable components of an iPhone to the iCloud account, making the steal-and-part-out pipeline much more difficult. Thieves would have to phish the phone's original owner, or defeat the activation lock on each component when parting out the phone. Apple is making iPhones less attractive to steal with each release.</li>
<li><a href="https://www.reversinglabs.com/blog/fake-recruiter-coding-tests-target-devs-with-malicious-python-packages" target="_blank">Fake recruiter coding tests target devs with malicious Python packages</a> - 🇰🇵 is at it again, this time serving malware to software development recruits while posing as financial services firm (in this case Capital One) recruiters on LinkedIn. <a href="https://unit42.paloaltonetworks.com/threat-assessment-north-korean-threat-groups-2024/" target="_blank">North Korean Threat Groups</a> have been very active recently.</li>
<li><a href="https://krebsonsecurity.com/2024/09/bug-left-some-windows-pcs-dangerously-unpatched/" target="_blank">Bug Left Some Windows PCs Dangerously Unpatched</a> - "Build version numbers crossed into a range that triggered a code defect." The build system for Windows and Windows Updates must be a wild place.</li>
<li><a href="https://www.mastercard.com/news/press/2024/september/mastercard-invests-in-continued-defense-of-global-digital-economy-with-acquisition-of-recorded-future/" target="_blank">Mastercard invests in continued defense of global digital economy with acquisition of Recorded Future</a> - A cool $2.65 billion for threat intel company Recorded Future. Some say <a href="https://vulncheck.com/blog/mastercard-recorded-future-acquisition" target="_blank">Intelligence is the Most Important and Most Lucrative Asset in Cybersecurity</a>.</li>
<li><a href="https://www.prnewswire.com/news-releases/k1-acquires-mariadb-a-leading-database-software-company-and-appoints-new-ceo-302243508.html" target="_blank">K1 Acquires MariaDB, a Leading Database Software Company, and Appoints New CEO</a> - You were using Postgres anyway, right? <a href="https://web.archive.org/web/20200703115804/https://www.computerworld.com/article/3463901/dead-database-walking-mysql-s-creator-on-why-the-future-belongs-to-m" target="_blank">History repeats itself</a>.</li>
<li><a href="https://www.servethehome.com/docker-raises-prices-up-to-80-percent-and-more/" target="_blank">Docker Raises Prices Up to 80 Percent and More</a> - You were using <a href="https://podman-desktop.io/" target="_blank">Podman Desktop</a> or <a href="https://orbstack.dev/" target="_blank">OrbStack</a> anyway, right? Note: this does not affect the docker CLI, only Docker Desktop.</li>
<li><a href="https://www.fortinet.com/blog/business-and-technology/notice-of-recent-security-incident" target="_blank">Notice of Recent Security Incident</a> - Been a while Fortinet, welcome back!</li>
<li><a href="https://www.justice.gov/opa/pr/former-cia-officer-sentenced-10-years-prison-conspiracy-commit-espionage" target="_blank">Former CIA Officer Sentenced to 10 Years in Prison for Conspiracy to Commit Espionage</a> - To be convicted for this at 71 years old! Wild!</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.watchtowr.com/we-spent-20-to-achieve-rce-and-accidentally-became-the-admins-of-mobi/" target="_blank">We Spent $20 To Achieve RCE And Accidentally Became The Admins Of .MOBI</a> - This is worth a careful read. An expired domain leads to complete chaos, from RCE to TLS certificates for any .mobi domain. A post that makes you wonder how we've gotten this far with the underlying infrastructure of the internet.</li>
<li><a href="https://rhinosecuritylabs.com/cloud-security/cloudgoat-walkthrough-glue_privesc/" target="_blank">CloudGoat Official Walkthrough Series: 'glue_privesc'</a> - There isn't a ton of "cloud" based offensive resources out there so it's great to see a practical walkthrough.</li>
<li><a href="https://www.synacktiv.com/en/publications/defend-against-vampires-with-10-gbps-network-encryption" target="_blank">Defend Against Vampires With 10 Gbps Network Encryption</a> - If your fiber transits uncontrolled spaces (or even if it doesn't), you can use WireGuard and Linux routers on either end to encrypt all trunk'd VLAN traffic with almost no overhead when tuned properly.</li>
<li><a href="https://bishopfox.com/blog/large-language-models-llm-ctf-lab" target="_blank">Exploring Large Language Models: Local LLM CTF &amp; Lab</a> - I believe this is the first <em>local</em> LLM CTF. Code is: <a href="https://github.com/BishopFox/local-llm-ctf" target="_blank">local-llm-ctf</a>.</li>
<li><a href="https://gergelykalman.com/the-forgotten-art-of-filesystem-magic-alligatorcon-2024-slides.html" target="_blank">The forgotten art of filesystem magic - Alligatorcon 2024 slides</a> - Over $150,000 from Apple in bug bounty dollars from understanding filesystems better than the developers. If you're interested in macOS security, this is a must-read.</li>
<li><a href="https://sec-consult.com/blog/detail/msi-installer-repair-to-system-a-detailed-journey/" target="_blank">Microsoft Windows MSI Installer - Repair to SYSTEM - A detailed journey</a> - Until the September 2024 patch Tuesday, you could use some Windows MSI installers to escalate to SYSTEM during a "repair." SEC Consult released <a href="https://github.com/sec-consult/msiscan" target="_blank">msiscan</a> a scanning tool for identifying local privilege escalation issues in vulnerable MSI installers, as well as a few Yara rules with the post.</li>
<li><a href="https://deda.lol/posts/2024-09-12-escape_alcawasm/" target="_blank">AlcaWASM Challenge Writeup - Pwning an In-Browser Lua Interpreter</a> - The <a href="https://memorycorruption.net/posts/rce-lua-factorio/" target="_blank">Factorio hacker</a> released a challenge along with the write-up. This post is a well-written walkthrough of the more interesting parts of the challenge.</li>
<li><a href="https://fortbridge.co.uk/research/feeld-dating-app-nudes-data-publicly-available/" target="_blank">Feeld Dating App - Your Nudes and Data Were Publicly Available</a> - Looks like the 🌶️ dating app Feeld had more indirect object reference (IDOR) vulnerabilities than secured endpoints. GraphQL and IDOR, name a more iconic duo.</li>
<li><a href="https://www.netspi.com/blog/technical-blog/network-pentesting/hijacking-sql-server-credentials-with-agent-jobs-for-domain-privilege-escalation/" target="_blank">Hijacking SQL Server Credentials using Agent Jobs for Domain Privilege Escalation</a> - "In this blog I'll introduce SQL Server credential objects and discuss how they can be abused by threat actors to execute code as either a SQL Server login, local Windows user, or Domain user. I'll also cover how to enable logging that can be used to detect the associated behavior. This should be interesting to penetration testers, red teamers, and DBAs looking for legitimate authentication work arounds."</li>
<li><a href="https://services.google.com/fh/files/misc/standardizing-privileged-access-architecture-for-multi-cloud.pdf" target="_blank">[PDF] Standardizing Privileged Access Architecture for Multi-Cloud</a> 85 page white paper on securing IAM in AWS, Azure, and GCP.</li>
<li><a href="https://www.pentestpartners.com/security-blog/living-off-the-land-gpo-style/" target="_blank">Living off the land, GPO style</a> - "The ability to edit  Group Policy Object (GPOs) from non-domain joined computers using the native Group Policy editor has been on my list for a long time.  This blog post takes a deep dive into what steps were taken to find out why domain joined machines are needed in the first place and what options we had to trick the Group Policy Manager MMC snap-in into believing the computer was domain joined."</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/horizon3ai/CVE-2024-29847" target="_blank">CVE-2024-29847</a> - Ivanti EPM AgentPortal RCE Vulnerability.</li>
<li><a href="https://vulncheck.com/blog/go-exploit-external-c2s" target="_blank">VulnCheck go-exploit External C2s</a> - New go-exploit feature in 1.25.0 allows anyone to easily develop and integrate their own C2.</li>
<li><a href="https://github.com/JohnHammond/recaptcha-phish" target="_blank">recaptcha-phish</a> - Phishing with a fake reCAPTCHA.</li>
<li><a href="https://github.com/w1th4d/JarPlant" target="_blank">JarPlant</a> - Java archive implant toolkit.</li>
<li><a href="https://github.com/rotarydrone/GlobalUnProtect" target="_blank">GlobalUnProtect</a> - Decrypt GlobalProtect configuration and cookie files.</li>
<li><a href="https://github.com/sec-consult/msiscan" target="_blank">msiscan</a> - Scanning tool for identifying local privilege escalation issues in vulnerable MSI installers.</li>
<li><a href="https://github.com/nyxgeek/cloudkicker" target="_blank">cloudkicker</a> - self-hosted Azure OSINT tool.</li>
<li><a href="https://github.com/orhun/binsider" target="_blank">binsider</a> - Analyze ELF binaries like a boss 😼🕵️‍♂️.</li>
<li><a href="https://github.com/watchtowrlabs/CVE-2024-40711" target="_blank">CVE-2024-40711</a> - Exploit for Veeam backup and Replication Pre-Auth Deserialization CVE-2024-40711.</li>
<li><a href="https://github.com/fortra/No-Consolation" target="_blank">No-Consolation</a> - A BOF that runs unmanaged PEs inline. Updated to run PE's in the main thread with the <cite>--inthread</cite> option!</li>
<li><a href="https://www.evilsocket.net/2024/09/13/Introducing-bettercap-2-4-0-CAN-bus-hacking-WiFi-bruteforcing-and-builtin-web-UI/" target="_blank">Introducing Bettercap 2.4.0: Can-Bus Hacking, Wifi Bruteforcing and Builtin Web UI</a> - Bettercap is my favorite modern wireless tool. Now it's even better!</li>
<li><a href="https://github.com/CCob/DGPOEdit" target="_blank">DGPOEdit</a> - Disconnected GPO Editor - A Group Policy Manager launcher to allow editing of domain GPOs from non-domain joined machines.</li>
<li><a href="https://github.com/S3N4T0R-0X0/BEAR" target="_blank">BEAR</a> - Bear C2 is a compilation of C2 scripts, payloads, and stagers used in simulated attacks by Russian APT groups, Bear features a variety of encryption methods, including AES, XOR, DES, TLS, RC4, RSA and ChaCha to secure communication between the payload and the operator machine.</li>
<li><a href="https://github.com/Dump-GUY/EXE-or-DLL-or-ShellCode" target="_blank">EXE-or-DLL-or-ShellCode</a> - Just a simple silly PoC demonstrating executable "exe" file that can be used like exe, dll or shellcode...</li>
<li><a href="https://github.com/magisterquis/alpt4ats" target="_blank">alpt4ats</a> - A Lazy Programmer's Tips for Avoiding the SOC ~ BSides Belfast 2024.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://orca.security/resources/blog/typosquatting-in-github-actions/" target="_blank">Watch the Typo: Our PoC Exploit for Typosquatting in GitHub Actions</a> - A missing 's' at the end of 'actions' could mean the difference between a standard GitHub action deployment and a supply chain attack.</li>
<li><a href="https://www.elastic.co/security-labs/sequel-on-persistence-mechanisms" target="_blank">Linux Detection Engineering - A Sequel on Persistence Mechanisms</a> - A good catalog of less stealthy Linux persistence techniques.</li>
<li><a href="https://github.com/CCob/DGPOEdit" target="_blank">DGPOEdit</a> - Disconnected GPO Editor - A Group Policy Manager launcher to allow editing of domain GPOs from non-domain joined machines.</li>
<li><a href="https://blog.projectdiscovery.io/azure-config-review-with-nuclei/" target="_blank">Azure Config Review - Nuclei Templates v10.0.0 🎉</a> - The fan favorite continues to crank out new features!</li>
<li><a href="https://github.com/yasukata/zpoline" target="_blank">zpoline</a> - system call hook for Linux.</li>
<li><a href="https://yaak.app/blog/now-open-source" target="_blank">Yaak Is Now Open Source</a> - The latest desktop API client (think postman) is now MIT licensed and open source.</li>
<li><a href="https://github.com/outflanknl/macho-loader" target="_blank">macho-loader</a> - POC position-independent reflective loader for Mach-O dylibs.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 437 (+1)</p>
<p>Blogs monitored: 391 (+2)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
