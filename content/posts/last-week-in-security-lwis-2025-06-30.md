Title: Last Week in Security (LWiS) - 2025-06-30
Date: 2025-06-30 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-06-30
Author: Erik
Summary: Linux sleep obfs (<a href="https://x.com/k0zmer" target="_blank">@k0zmer</a>), sudo vuln (<a href="https://x.com/0xm1rch" target="_blank">@0xm1rch</a>), self-xss trick (<a href="https://x.com/slonser_" target="_blank">@slonser_</a>), primitive injection (<a href="https://x.com/trickster012" target="_blank">@trickster012</a>), Sitecore RCE (<a href="https://x.com/chudyPB" target="_blank">@chudyPB</a> ), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-06-09 to 2025-06-30.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">Celebrate Hacker Summer with Altered Security</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p>Start your Red Team training with Altered Security! We offer multiple Red Team courses with affordable and enterprise-like hands-on labs.</p>
<p>Each course comes with an industry-recognized certification. We are the creators of the popular Red Team certifications like Certified Red Team Professional (CRTP), CRTE, CARTP and more.</p>
<p>We are celebrating July 2025 as 'Hacker Summer'. Enjoy 20% OFF on all the courses (on-demand and learning path) using <strong>'HACKERSUMMER20OFF'</strong> from July 1 to July31 2025. <strong><a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">Sign up now!</a></strong></p>
</aside><ul>
<li><a href="https://research.checkpoint.com/2025/ai-evasion-prompt-injection/" target="_blank">In the Wild: Malware Prototype With Embedded Prompt Injection</a> - Malware authors are now embedding prompts for AI systems into malware samples to try to defeat large language model (LLM) analysis. This specific sample's prompt injection doesn't work against modern LLMs.</li>
<li><a href="https://blog.cloudflare.com/cloudflare-service-outage-june-12-2025/" target="_blank">Cloudflare service outage June 12, 2025</a> - Even the largest cloud providers use other cloud providers for their core infrastructure. In this case, Cloudflare's key-value (KV) storage relied on Google Cloud, which itself had an outage.</li>
<li><a href="https://techcrunch.com/2025/06/24/us-bans-whatsapp-from-house-of-representatives-staff-devices/" target="_blank">US House bans WhatsApp from staff devices</a> - Probably related to 0-click exploits, and an effort to reduce attack surface? This is 6 days before <a href="https://krebsonsecurity.com/2025/06/senator-chides-fbi-for-weak-advice-on-mobile-security/" target="_blank">Senator Chides FBI for Weak Advice on Mobile Security</a>. Related?</li>
<li><a href="https://citizenlab.ca/2025/06/first-forensic-confirmation-of-paragons-ios-mercenary-spyware-finds-journalists-targeted/" target="_blank">Graphite Caught - First Forensic Confirmation of Paragon’s iOS Mercenary Spyware Finds Journalists Targeted</a> - Speaking of mobile security, if you are a potential target of these attacks you need to make sure you are fully up to date, enable lockdown mode, and reboot daily.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.watchtowr.com/is-b-for-backdoor-pre-auth-rce-chain-in-sitecore-experience-platform/" target="_blank">Is b For Backdoor? Pre-Auth RCE Chain In Sitecore Experience Platform</a> - Someone messed up and the ServicesAPI user password was changed to "b" for some reason in Sitecore 10.1+. Then watchTowr did their thing and turned it into full RCE.</li>
<li><a href="https://specterops.io/blog/2025/06/10/onelogin-many-issues-how-i-pivoted-from-a-trial-tenant-to-compromising-customer-signing-keys/" target="_blank">OneLogin, Many Issues: How I Pivoted from a Trial Tenant to Compromising Customer Signing Keys</a> - OneLogin flaws led its AD Connector service to expose authentication credentials and enable account impersonation tradecraft.</li>
<li><a href="https://www.aim.security/lp/aim-labs-echoleak-blogpost" target="_blank">Breaking down ‘EchoLeak’, the First Zero-Click AI Vulnerability Enabling Data Exfiltration from Microsoft 365 Copilot</a> - A vulnerability that exploits design flaws typical of RAG Copilots, allowing attackers to automatically exfiltrate any data from M365 Copilot’s context, without relying on specific user behavior.</li>
<li><a href="https://blog.redteam-pentesting.de/2025/reflective-kerberos-relay-attack/" target="_blank">A Look in the Mirror - The Reflective Kerberos Relay Attack</a> - If you can coerce any Windows host to authenticate back to you via SMB, you can relay the computer account’s Kerberos ticket back to the host and obtain NT AUTHORITY\SYSTEM privileges and thereby Remote Code Execution. Patched in <a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33073" target="_blank">CVE-2025-33073</a> . I can confirm a lot of people have known and abused this for some time now. We would urge defenders check past data sources to identify previous abuse. Various companies have now published their blogs on the topic as well such as <a href="https://www.synacktiv.com/publications/ntlm-reflection-is-dead-long-live-ntlm-reflection-an-in-depth-analysis-of-cve-2025" target="_blank">SynAckTiv</a>.</li>
<li><a href="https://darkmarc.substack.com/p/phishing-attack-uses-gmail-and-google" target="_blank">Phishing Attack Uses Gmail and Google Sites 'Living Off the Land' (Gmail Phishing)</a> - Love the tradecraft here. Companies like Google and Microsoft are defacto email service providers now. Leveraging their infrastructure to conduct your campaigns is a sure bet to hitting that inbox.</li>
<li><a href="https://mrd0x.com/filefix-clickfix-alternative/" target="_blank">FileFix - A ClickFix Alternative</a> - If you can socially engineer a victim to copy paste some some content File Explorer, you can get code execution and bypass Mark of the Web (MOTW).</li>
<li><a href="https://specterops.io/blog/2025/06/25/good-fences-make-good-neighbors-new-ad-trusts-attack-paths-in-bloodhound/" target="_blank">Good Fences Make Good Neighbors: New AD Trusts Attack Paths in BloodHound</a> - New changes to Bloodhound CE to improve coverage of Active Directory identities and improve trust relationships.</li>
<li><a href="https://cicada-8.medium.com/were-going-the-wrong-way-how-to-abuse-symlinks-and-get-lpe-in-windows-0c598b99125b" target="_blank">We’re going the wrong way! How to abuse symlinks and get LPE in Windows</a> - A write-up on using symlinks to escalate privileges on a Windows device. <a href="https://github.com/shubham0d/SymBlock" target="_blank">This project</a> never caught traction but serves as a reminder of the possibilities that exist still exist.</li>
<li><a href="https://specterops.io/blog/2025/06/25/untrustworthy-trust-builders-account-operators-replicating-trust-attack-aorta/" target="_blank">Untrustworthy Trust Builders: Account Operators Replicating Trust Attack (AORTA)</a> - There's a reason we recommend for system administrators to avoid using default groups in Active Directory. They just hold undocumented and unaccounted for risk. This new technique makes it so members of the Account Operators group can escalate to Domain Admin privileges by exploiting the Incoming Forest Trust Builders group.</li>
<li><a href="https://redheadsec.tech/phantom-boot-a-quick-look-at-windows-persistence-via-registerapplicationrestart/" target="_blank">Phantom Persistence - A quick look at Windows Persistence via RegisterApplicationRestart</a> - Use the RegisterApplicationRestart API to maintain persistence by having csrss.exe write registry entries during system shutdown when most monitoring processes have exited, avoiding detection by having the malicious application never directly touch the registry itself. A <a href="https://ludus.cloud/" target="_blank">Ludus</a> range is used to show the technique. 😊</li>
<li><a href="https://thegreycorner.com/2025/06/25/azure-service-c2-forwarding-part2.html" target="_blank">Azure Service Command and Control HTTP traffic forwarding part 2</a> - A few of these already exist but this is an updating walkthrough on using Azure to front implant traffic. As always, careful with burning your Microsoft Subscription.</li>
<li><a href="https://specterops.io/blog/2025/06/27/requesting-entra-id-tokens-with-entra-id-sso-cookies/" target="_blank">Requesting Entra ID Tokens with Entra ID SSO Cookies</a> - This post explains how to request OAuth tokens and enumerate an Entra ID tenant by using an SSO cookie from a non cloud-joined device.</li>
<li><a href="https://www.praetorian.com/blog/introducing-github-device-code-phishing/" target="_blank">Introducing: GitHub Device Code Phishing</a> - We will continue to see more of these tactics are attackers look to stay away from endpoints as much as possible. Sensitive data is behind an SSO portal. The blog release also came with a tool drop (<a href="https://github.com/praetorian-inc/GitPhish" target="_blank">GitPhish</a>) for you to use in your next red team.</li>
<li><a href="https://www.stratascale.com/vulnerability-alert-CVE-2025-32462-sudo-host" target="_blank">Vulnerability Advisory: Sudo Host Option Elevation of Privilege</a> - Sudo has had a vulnerability for over 12 years that allowed you to specify other hosts to check for sudo rules but applied them to the local host. I suspect this is a pretty rare to find in the wild but would be an easy win if you do.</li>
<li><a href="https://blog.talosintelligence.com/decrement-by-one-to-rule-them-all/" target="_blank">Decrement by one to rule them all: AsIO3.sys driver exploitation</a> - A nice use of hardlinks to bypass the image hash based security of an ASUS driver. Note that the exploitation technique used here won't work on Windows 11 24H2 where Virtualization-Based Security (VBS) or Hypervisor-protected Code Integrity (HVCI) are enabled.</li>
<li><a href="https://www.synacktiv.com/en/publications/exploiting-the-tesla-wall-connector-from-its-charge-port-connector" target="_blank">Exploiting the Tesla Wall Connector From Its Charge Port Connector</a> - Because of course you can update the Telsa Wall Connector via the charging cable!</li>
<li><a href="https://blog.slonser.info/posts/make-self-xss-great-again/" target="_blank">Make Self-XSS Great Again</a> - This one is for the web-app hackers tired of getting issues closed as Self-XSS.</li>
<li><a href="https://aff-wg.org/2025/06/26/beacon-object-files-five-years-on/" target="_blank">Beacon Object Files – Five Years On…</a> - Raphael Mudge reflects on the decisions and motivations behind the now ubiquitous Beacon Object Files (BOFs).</li>
<li><a href="https://www.outflank.nl/blog/2025/06/30/bof-linting-for-accelerated-development/" target="_blank">BOF Linting for Accelerated Development</a> - Speed up your Beacon Object File (BOF) development workflow! We know a few people that will start using this immediately.</li>
<li><a href="https://itm4n.github.io/offline-extraction-of-symantec-account-connectivity-credentials/" target="_blank">Offline Extraction of Symantec Account Connectivity Credentials (ACCs)</a> - A classic case of being "<a href="https://xkcd.com/356/" target="_blank">Nerd Sniped</a>", as itm4n's last blog ends with "<a href="https://itm4n.github.io/checking-symantec-account-credentials-privesccheck/" target="_blank">that’s the best I can do for now</a> ." In this post they dig into the guts of Symantec ACC to create a dumping and decryption tool that runs locally.</li>
<li><a href="https://mrbruh.com/asus_p2/" target="_blank">ASUSpicious Flaw - Millions of Users’ Information Exposed Since 2022</a> - ASUS still doesn't have any bug bounty program, which makes you wonder what else is out there not being reported. This is a nice C# reversing post that ended up with hardcoded API credentials and lots of data being exposed.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/NocteDefensor/SCCMDecryptor-BOF/tree/main" target="_blank">SCCMDecryptor-BOF</a> - A Beacon Object File (BOF) implementation of Adam Chester's(<a href="https://x.com/_xpn_" target="_blank">@_xpn_</a>) c# tool for decrypting SCCM encrypted password blobs retrieved from the site DB.</li>
<li><a href="https://github.com/rtecCyberSec/BitlockMove" target="_blank">BitlockMove</a> - Lateral Movement via Bitlocker DCOM interfaces &amp; COM Hijacking.</li>
<li><a href="https://github.com/temp43487580/EntraPassTheCert" target="_blank">EntraPassTheCert</a> - tool for requesting Entra ID's P2P certificate and authenticating remote Entra joinned devices with it.</li>
<li><a href="https://github.com/HullaBrian/COMmander" target="_blank">COMmander</a> - .NET tool used to enrich RPC telemetry.</li>
<li><a href="https://github.com/NeffIsBack/wsuks" target="_blank">wsuks</a> - Automating the MITM attack on WSUS.</li>
<li><a href="https://github.com/hdm/ctail" target="_blank">ctail</a> - Tail Certificate Transparency logs and extract hostnames.</li>
<li><a href="https://github.com/kozmer/silentpulse" target="_blank">silentpulse</a> - single-threaded event driven sleep obfuscation poc for linux.</li>
<li><a href="https://github.com/Teach2Breach/schtask" target="_blank">schtask</a> - Rust implementation, creating a scheduled task programmatically with user logon trigger.</li>
<li><a href="https://github.com/Ap3x/Panoptes" target="_blank">Panoptes</a> - Panoptes Endpoint Detection and Response Solution.</li>
<li><a href="https://github.com/itm4n/Pentest-Windows/tree/main/SMAStorageDump" target="_blank">SMAStorageDump</a> - Symantec Management Agent (a.k.a. "Altiris Agent") dumper and decryptor.</li>
<li><a href="https://github.com/quarkslab/wirego/" target="_blank">wirego</a> - A Wireshark plugin framework based on ZMQ, supporting Golang, Python and hopefully more languages soon. More info at <a href="https://blog.quarkslab.com/getting-started-with-wirego.html" target="_blank">Getting started with Wirego</a>.</li>
<li><a href="https://github.com/trickster0/PrimitiveInjection" target="_blank">PrimitiveInjection</a> - PrimitiveInjection by using Read, Write and Allocation Primitives. For more info see: <a href="https://trickster0.github.io/posts/Primitive-Injection/" target="_blank">Primitive Injection - Breaking the Status Quo</a>.</li>
<li><a href="https://github.com/hoodoer/DragonHash" target="_blank">DragonHash</a> - Demo code JavaScript POC that tricks user into sending Windows hash to responder. For more info see: <a href="https://trustedsec.com/blog/dragging-secrets-out-of-chrome-ntlm-hash-leaks-via-file-urls" target="_blank">Dragging Secrets Out of Chrome: NTLM Hash Leaks via File URLs</a>.</li>
<li><a href="https://github.com/ZephrFish/GoClipC2?ref=blog.zsec.uk" target="_blank">GoClipC2</a> - Clipboard for Command and Control between VDI, RDP and Others on Windows.</li>
<li><a href="https://github.com/SpecterOps/Nemesis" target="_blank">Nemesis</a> - 2.0 release of Nemesis! - An offensive data enrichment pipeline.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/adgaultier/caracal" target="_blank">caracal</a> - Make your (eBPF🐝) programs stealthier.</li>
<li><a href="https://github.com/sud0Ru/NauthNRPC" target="_blank">NauthNRPC</a> - Enumerate Domain Users Without Authentication.</li>
<li><a href="https://arxiv.org/abs/2506.14682" target="_blank">AIRTBench: Measuring Autonomous AI Red Teaming Capabilities in Language Models</a> - An AI red teaming benchmark for evaluating language models' ability to autonomously discover and exploit Artificial Intelligence and Machine Learning (AI/ML) security vulnerabilities.</li>
<li><a href="https://github.com/subat0mik/Misconfiguration-Manager/blob/main/presentations/Troopers%2025%20-%20Misconfiguration%20Manager.pdf" target="_blank">[PDF] Misconfiguration-Manager</a> - Recent talk from Troopers 2025 on SCCM Misconfigurations. Good to see <a href="https://ludus.cloud/" target="_blank">Ludus</a> in action!</li>
<li><a href="https://www.akamai.com/blog/security-research/botnets-flaw-mirai-spreads-through-wazuh-vulnerability" target="_blank">Two Botnets, One Flaw: Mirai Spreads Through Wazuh Vulnerability</a> - Wazuh used to spread malware? <a href="https://gitlab.com/badsectorlabs/iscariot-suite" target="_blank">Traitorware</a> in action!</li>
<li><a href="https://github.com/azunhsephiroth77/auto-ad-recon-netexec" target="_blank">auto-ad-recon-netexec</a> - Comprehensive Active Directory Enumeration tool using Netexec.</li>
<li><a href="https://www.cell.com/cell-reports-physical-science/fulltext/S2666-3864(25)00221-8" target="_blank">Manipulating trapped air bubbles in ice for message storage in cold regions</a> - "Manipulating the bubble layer by varying the freezing rate successfully utilizes Morse, binary, and ternary codes to store messages." 🤯</li>
<li><a href="https://github.com/TheManticoreProject/Manticore" target="_blank">Manticore</a> - A cross platform library to write offensive and defensive security tools in Go.</li>
<li><a href="https://github.com/c0nf1den71al/Lodestar-Forge" target="_blank">Lodestar-Forge</a> - Easy to use, open-source infrastructure management platform, crafted specifically for red team engagements.</li>
<li><a href="https://github.com/D4Vinci/Scrapling" target="_blank">Scrapling</a> - 🕷️ An undetectable, powerful, flexible, high-performance Python library to make Web Scraping Easy and Effortless as it should be!.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 454 (+0)</p>
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
