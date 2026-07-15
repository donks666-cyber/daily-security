Title: Last Week in Security (LWiS) - 2024-05-13
Date: 2024-05-13 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-05-13
Author: Erik
Summary: Evading MDI (<a href="https://twitter.com/yaumn_" target="_blank">@yaumn_</a>), TAP-&gt;NTLM (<a href="https://twitter.com/_dirkjan" target="_blank">@_dirkjan</a>), ELF verifier (<a href="https://twitter.com/kev169" target="_blank">@kev169</a>), Kerberos delegation + 🦀 in beacons (<a href="https://twitter.com/_rastamouse" target="_blank">@_RastaMouse</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-05-06 to 2024-05-13.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://restoreprivacy.com/protonmail-discloses-user-data-leading-to-arrest-in-spain/" target="_blank">Proton Mail Discloses User Data Leading to Arrest in Spain</a> - People trusting VPNs is still wild.</li>
<li><a href="https://www.nbcchicago.com/news/local/ascension-cyber-attack-illinois-hospitals-evanston-hospital-systems-down/3432706/" target="_blank">Ascension hospitals report 'disruptions' to clinic operations following suspected cyber attack</a> -  Ascension is one of the largest hospital systems in Illinois, with 150 care sites and 14 hospitals, including Ascension St. Francis in Evanston.</li>
<li><a href="https://www.unisuper.com.au/about-us/media-centre/2024/a-joint-statement-from-unisuper-and-google-cloud" target="_blank">A joint statement from UniSuper CEO Peter Chun, and Google Cloud CEO, Thomas Kurian</a> - When the Google Cloud CEO has to make a statement, you know it's a big deal. UniSuper, an Australian superannuation fund, had their entire Google Cloud account deleted in "an isolated, one-of-a-kind occurrence." They were saved only because they kept a backup totally outside of Google Cloud. This will be a wild one for your tabletop exercises.</li>
<li><a href="https://krebsonsecurity.com/2024/05/how-did-authorities-identify-the-alleged-lockbit-boss/" target="_blank">How Did Authorities Identify the Alleged Lockbit Boss?</a> - Last week global law enforcement arrested the alleged leader of the LockBit ransomware gang (known online as "LockBitSupp"). Krebs has the details on how they tracked him down.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.leviathansecurity.com/blog/tunnelvision" target="_blank">TunnelVision (CVE-2024-3661): How Attackers Can Decloak Routing-Based VPNs For a Total VPN Leak</a> - With a little-used <a href="https://datatracker.ietf.org/doc/html/rfc3442" target="_blank">DHCP option</a>, an attacker in a position to send DHCP responses to a vitim (real or through a rogue DHCP server) can push specific routes that will allow them to see traffic that the user believes is protected by a VPN.</li>
<li><a href="https://www.zerodayinitiative.com/blog/2024/5/9/cve-2024-21115-an-oracle-virtualbox-lpe-used-to-win-pwn2own" target="_blank">CVE-2024-21115: An Oracle Virtualbox Lpe Used to Win Pwn2own</a> - Great, detailed write up of an out-of-bounds write leading to arbitrary WinExec -- not quite arbitrary code execution thanks to control flow guard.</li>
<li><a href="https://www.synacktiv.com/en/publications/understanding-and-evading-microsoft-defender-for-identity-pkinit-detection" target="_blank">Understanding and Evading Microsoft Defender for Identity Pkinit Detection</a> - If you want to not stand out, it's always best to look exactly like native tools. To achieve this, try the new tool: <a href="https://github.com/synacktiv/Invoke-RunAsWithCert" target="_blank">Invoke-RunAsWithCert</a> - A PowerShell script to perform PKINIT authentication with the Windows API from a non domain-joined machine.</li>
<li><a href="https://systemweakness.com/marshal-like-a-boss-with-reflective-loading-in-c-7bb0b54ddb5f" target="_blank">Marshal Like a Boss With Reflective Loading in C#</a> - This post shows how reflective loading can be combined with storing a DLL in resources to marshal functions from it into managed runtime without the need of dropping any artifacts on disk.</li>
<li><a href="https://rastamouse.me/custom-beacon-artifacts/" target="_blank">Custom Beacon Artifacts</a> - Blog post explaining how to create custom Beacon artifacts for Cobalt Strike by modifying and building executable templates in C++ and Rust, allowing for the injection and execution of Beacon shellcode in memory without detection.</li>
<li><a href="https://www.persistent-security.net/post/when-phish-proof-gets-hooked" target="_blank">When "Phish-Proof" Gets Hooked</a> - How a red team revealed a vulnerability in Okta FastPass, by exploiting the transition from the Loopback flow to the Custom URL flow, bypassing anti-phishing protections. So much Okta tradecraft lately.</li>
<li><a href="https://www.breachproof.net/blog/lethal-injection-how-we-hacked-microsoft-ai-chat-bot" target="_blank">Lethal Injection: How We Hacked Microsoft's Healthcare Chat Bot</a> - Multiple vulnerabilities in Microsoft's Azure Health Bot service that could have allowed unauthorized access to sensitive infrastructure and medical data. All patched. Cool work!</li>
<li><a href="https://dfir.ch/posts/today_i_learned_zsh_timestamps/" target="_blank">Today I Learned - Zsh History Timestamps</a> - In Zsh, commands executed during a session are logged with timestamps, but these timestamps reset upon reboot or session closure, making it useful for incident response in systems where Zsh is the default shell.</li>
<li><a href="https://whiteknightlabs.com/2024/05/07/abusing-azure-logic-apps-part-1/" target="_blank">Abusing Azure Logic Apps - Part 1</a> - Looking forward to this series. How attackers can abuse storage account privileges linked with a logic app to gain unauthorized access, execute system commands, and create workflows, focusing on the relationship between logic apps and storage accounts.</li>
<li><a href="https://www.hakupiku.com/posts/looking-back-at-the-past-4-months/" target="_blank">Looking back at the past 4 months</a> - For those thinking about starting to become a full time bug bounty hunter. An anecdote.</li>
<li><a href="https://matanber.com/blog/cspt-levels" target="_blank">Bypassing WAFs to Exploit CSPT Using Encoding Levels</a> - How to exploit Client Side Path Traversal (CSPT) vulnerabilities by bypassing Web Application Firewalls (WAFs) using different encoding levels to execute attacks such as cross-site scripting (XSS).</li>
<li><a href="https://rastamouse.me/kerberos-delegation-test-app/" target="_blank">Kerberos Delegation Test App</a> - Rasta built a ASP.NET Core to understand Kerberos protocol by capturing and decrypting real traffic.</li>
<li><a href="https://detect.fyi/the-structure-and-taxonomy-of-a-detection-knowledge-base-abe415a1ee81" target="_blank">The Structure and Taxonomy of a Detection Knowledge Base</a> - The importance of documentation in detection engineering.</li>
<li><a href="https://3sjay.github.io/2024/05/10/schneiderups-rmi-deser.html" target="_blank">Schneider Electric APC Easy UPS RCE - Java RMI Applevel Deser for JEP&amp;gt;=290</a> - RCE those pesky UPS devices all over your internal pentest.</li>
<li><a href="https://www.assetnote.io/resources/research/digging-for-ssrf-in-nextjs-apps" target="_blank">Digging for SSRF in NextJS apps</a> - The blog post explores the potential for SSRF vulns in NextJS applications due to misconfigurations, particularly focusing on the _next/image component and demonstrating how attackers can exploit these weaknesses to perform SSRF attacks, including a detailed explanation of bypassing security measures and a newly discovered SSRF vulnerability that was assigned CVE-2024-34351.</li>
<li><a href="https://blog.projectdiscovery.io/hacking-apple-with-sql-injection/" target="_blank">Hacking Apple - SQL Injection to Remote Code Execution</a> - Researchers from ProjectDiscovery identified a critical SQL injection vulnerability in Apple's Book Travel portal using Mura/Masa CMS, led to RCE, and responsibly disclosed it. Wicked!</li>
<li><a href="https://dirkjanm.io/lateral-movement-and-hash-dumping-with-temporary-access-passes-microsoft-entra/" target="_blank">Lateral movement and on-prem NT hash dumping with Microsoft Entra Temporary Access Passes</a> - Temporary passwords can give access to long term keys! Great writeup from Dirk-jan as always.</li>
<li><a href="https://labs.jumpsec.com/poisoning-pipelines-azure-devops-edition/" target="_blank">Poisoning Pipelines: Azure DevOps Edition</a> - DevOps and CI/CD solutions have come under fire recently, and this post shows how to abuse Azure DevOps to execute arbitrary code.</li>
<li><a href="https://labs.nettitude.com/blog/emulation-with-qiling/" target="_blank">Emulation with Qiling</a> - Qiling has some cool features, like the ability to fake file systems, hook functions, and even modify registers on the fly. This post shows how to use Qiling to emulate NEXXT Polaris 150 travel router.</li>
<li><a href="https://trustedsec.com/blog/xz-utils-made-me-paranoid" target="_blank">XZ Utils Made Me Paranoid</a> - If you too are paranoid due to the XZ backdoor incident, check out <a href="https://github.com/trustedsec/VerifyELF" target="_blank">VerifyELF</a> a tool to validate that there are no hooks installed into the running processes, and if there are to print out that there is and what offset the first difference is, or print out all differences.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/0xda568/IconJector" target="_blank">IconJector</a> - Unorthodox and stealthy way to inject a DLL into the explorer using icons.</li>
<li><a href="https://github.com/cybersectroll/TrollDump" target="_blank">TrollDump</a> - Injects a 64-bit managed DLL into a 64-bit managed or unmanaged process using setwindowshook.</li>
<li><a href="https://github.com/HexaCluster/pgdsat" target="_blank">pgdsat</a> - PostgreSQL Database Security Assessment Tool.</li>
<li><a href="https://github.com/anchore/grype" target="_blank">grype</a> - A vulnerability scanner for container images and filesystems.</li>
<li><a href="https://github.com/cisagov/parsnip" target="_blank">parsnip</a> - Parsnip is a program developed to assist in the parsing of protocols using the open source network security monitoring tool Zeek.</li>
<li><a href="https://github.com/cisagov/vulnrichment" target="_blank">vulnrichment</a> - A repo to conduct vulnerability enrichment.</li>
<li><a href="https://github.com/JanielDary/ImmoralFiber" target="_blank">ImmoralFiber</a> - Fibers are an optional and largely undocumented component of the Windows operating system, existing only in user mode.</li>
<li><a href="https://github.com/Diverto/IPPrintC2" target="_blank">IPPrintC2</a> - PoC for using MS Windows printers for persistence / command and control via Internet Printing.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.raspberrypi.com/news/raspberry-pi-connect/" target="_blank">Raspberry Pi Connect</a> - "...a secure and easy-to-use way to access your Raspberry Pi remotely, from anywhere on the planet, using just a web browser."</li>
<li><a href="https://github.com/theokwebb/C-from-Scratch" target="_blank">C-from-Scratch</a> - A roadmap to learn C from Scratch.</li>
<li><a href="https://github.com/cramppet/regulator" target="_blank">regulator</a> - Automated learning of regexes for DNS discovery.</li>
<li><a href="https://github.com/visma-prodsec/confused" target="_blank">confused</a> - Tool to check for dependency confusion vulnerabilities in multiple package management systems.</li>
<li><a href="https://github.com/ashirt-ops/ashirt-server" target="_blank">ashirt-server</a> - Adversary Simulators High-Fidelity Intelligence and Reporting Toolkit.</li>
<li><a href="https://github.com/HuskyHacks/bsides-nashville-identity-crisis" target="_blank">bsides-nashville-identity-crisis</a> - Identity Crisis: Combating M365 Account Takeovers at Scale (BSides Nashville 2024).</li>
<li><a href="https://bc-security.org/survivorship-bias-and-how-red-teams-can-handle-it/" target="_blank">Survivorship Bias and How Red Teams Can Handle It</a> - Not the first time I've heard this before.</li>
<li><a href="https://github.com/hac01/gcp-iam-brute" target="_blank">gcp-iam-brute</a> - GCP IAM Brute is a tool that leverages the testIamPermissions feature in Google Cloud Platform (GCP) to perform fuzz testing for different permissions within GCP.</li>
<li><a href="https://github.com/red-kite-solutions/stalker" target="_blank">stalker</a> - Stalker, the Extensible Attack Surface Management tool.</li>
<li><a href="https://github.com/duo-labs/cloudmapper" target="_blank">cloudmapper</a> - CloudMapper helps you analyze your Amazon Web Services (AWS) environments.</li>
<li><a href="https://github.com/xnl-h4ck3r/waymore" target="_blank">waymore</a> - Find way more from the Wayback Machine, Common Crawl, Alien Vault OTX, URLScan &amp; VirusTotal!.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 427 (+1)</p>
<p>Blogs monitored: 379 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
