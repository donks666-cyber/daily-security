Title: Last Week in Security (LWiS) - 2024-10-21
Date: 2024-10-21 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-10-21
Author: Erik
Summary: VNC-Like over SCCM (<a href="https://twitter.com/netero_1010" target="_blank">@netero_1010</a>), Use LLMs to find CVEs (<a href="https://x.com/ProtectAICorp" target="_blank">@ProtectAICorp</a>), New process 💉 technique (<a href="https://x.com/OutflankNL" target="_blank">@OutflankNL</a>), 💰 Big acquisition (<a href="https://x.com/Sophos" target="_blank">@Sophos</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-10-14 to 2024-10-21.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.secureworks.com/about/press/sophos-to-acquire-secureworks" target="_blank">Sophos to Acquire Secureworks to Accelerate Cybersecurity Services and Technology for Organizations Worldwide</a> - "...The all-cash transaction is valued at approximately $859 million". Congrats to those that cashed out!</li>
<li><a href="https://www.prnewswire.com/news-releases/leeds-equity-partners-acquires-offsec-302275836.html" target="_blank">Leeds Equity Partners Acquires OffSec</a> - Offsec has been acquired by Leeds Equity Partners. News coming shortly after the OSCP+ vs OSCP announcement.</li>
<li><a href="https://sec.cloudapps.cisco.com/security/center/resources/october_15_2024" target="_blank">Cisco Event Response: Reports of Security Incident</a> - "...Based on our investigations, we are confident that there has been no breach of our systems. "</li>
<li><a href="https://www.edr-telemetry.com/" target="_blank">Welcome to the EDR Telemetry Project</a> - Just released! Certainly do not use this data as the sole source of truth for your EDR telemetry, but it's a good starting point for understanding what data is being collected by various EDR solutions.</li>
<li><a href="https://www.bbc.com/news/articles/ce8vedz4yk7o" target="_blank">Firm hacked after accidentally hiring North Korean cyber criminal</a> - North Koreans continue to get jobs as an initial access vector. Anyone else establish initial access from just applying to a job posting? #SorryHR</li>
<li><a href="https://www.wired.com/story/anonymous-sudan-ddos-indictment-takedown/" target="_blank">Hacker Charged With Seeking to Kill Using Cyberattacks on Hospitals</a> - The US has accused two brothers of being part of the hacker group Anonymous Sudan, which allegedly went on a wild cyber attack spree that hit hundreds of targets—and, for one of the two men, even put lives at risk.</li>
<li><a href="https://techcrunch.com/2024/10/17/microsoft-said-it-lost-weeks-of-security-logs-for-its-customers-cloud-products/?guccounter=1" target="_blank">Microsoft said it lost weeks of security logs for its customers’ cloud products</a> - Not only do you have to pay to play but you might also lose your logs in the process. Ouch!</li>
<li><a href="https://www.bleepingcomputer.com/news/security/internet-archive-breached-again-through-stolen-access-tokens/" target="_blank">Internet Archive breached again through stolen access tokens</a> - They can't catch a break right now. Second in a row. Leave the Internet Archive alone!</li>
<li><a href="https://www.defense.gov/News/News-Stories/Article/Article/3937053/army-announces-effort-to-help-small-business-meet-cybersecurity-requirements/" target="_blank">Army Announces Effort to Help Small Business Meet Cybersecurity Requirements</a> - "...The Army is setting aside about $26 million in both fiscal year 2025 and fiscal year 2026 for the pilot NCODE program"</li>
<li><a href="https://cointelegraph.com/news/monero-transactions-japanese-authorities-arrest-18-scammers" target="_blank">Japanese authorities trace Monero, arrest 18 in $670K laundering case</a> - Unsure how this "tracing" took place. "The flow was traced" is what article linked (written in Japanese) says. This was the first time (as reported by Japanese authorities) that Monero was used to identify a suspect.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.outflank.nl/blog/2024/10/15/introducing-early-cascade-injection-from-windows-process-creation-to-stealthy-injection/" target="_blank">Introducing Early Cascade Injection: From Windows Process Creation to Stealthy Injection</a> - A process injection technique that avoids queuing cross-process Asynchronous Procedure Calls (APCs), while having minimal remote process interaction.</li>
<li><a href="https://www.spatial-sec.com/blog/post/22/index.html" target="_blank">The Black Team Ops honeypot</a> - Your weekly humor/troll post. Title says it all.</li>
<li><a href="https://trustedsec.com/blog/spec-tac-ula-deserialization-deploying-specula-with-net" target="_blank">Spec-tac-ula Deserialization: Deploying Specula with .NET</a> - Exploiting .NET deserialization to persist on a workstation. Some updates have been made to ysoserial.net as well.</li>
<li><a href="https://kknowl.es/posts/stratus-contributor/" target="_blank">Becoming a Stratus Red Team Contributor</a> - A step-by-step walkthrough of contributing to this project and how the project is structured.</li>
<li><a href="https://www.elastic.co/security-labs/elevate-your-threat-hunting" target="_blank">Elevate Your Threat Hunting with Elastic</a> - A threat hunting package designed to aid defenders with proactive detection queries to identify actor-agnostic intrusions.</li>
<li><a href="https://sabotagesec.com/i-hate-you-com-pitfalls-of-com-object-activation/" target="_blank">I hate you COM - Pitfalls of COM object activation</a> - Some documented lessons learned from someone performing some tool development using COM objects and the <cite>ICorPublish</cite> interface.</li>
<li><a href="https://www.akamai.com/blog/security-research/winreg-relay-vulnerability" target="_blank">Call and Register — Relay Attack on WinReg RPC Client</a> - The write-up of CVE-2024-43532. The vulnerability abuses a fallback mechanism in the WinReg client implementation that uses obsolete transport protocols insecurely if the SMB transport is unavailable.</li>
<li><a href="https://global.ptsecurity.com/analytics/pt-esc-threat-intelligence/fake-attachment-roundcube-mail-server-attacks-exploit-cve-2024-37383-vulnerability" target="_blank">Fake attachment. Roundcube mail server attacks exploit CVE-2024-37383 vulnerability.</a> - This blog post showcases how to exploit CVE-2024-37383 which is a Roundcube Webmail vulnerability. This is a stored XSS vulnerability that allows an attacker to execute JavaScript code on the user's page.</li>
<li><a href="https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/how-threat-actors-conduct-election-interference-operations-an-overview/" target="_blank">How Threat Actors Conduct Election Interference Operations: An Overview</a> - Elections in the US are around the corner which means these headlines are SEO goldmines. TLDR - Check your new sources!</li>
<li><a href="https://www.infernux.no/EntraID-GeneralHardening/" target="_blank">Hardening Entra ID</a> - Food baseline read for anyone performing engagements (offense or defense) against Entra ID.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/netero1010/SCCMVNC" target="_blank">SCCMVNC</a> -  A tool to modify SCCM remote control settings on the client machine, enabling remote control without permission prompts or notifications. This can be done without requiring access to SCCM server.</li>
<li><a href="https://github.com/Octoberfest7/Secure_Stager" target="_blank">Secure_Stager</a> - An x64 position-independent shellcode stager that verifies the stage it retrieves prior to execution.</li>
<li><a href="https://github.com/ctrlsam/rigour" target="_blank">rigour</a> -  A rigorous IoT scanner based on Shodan.io</li>
<li><a href="https://github.com/protectai/vulnhuntr" target="_blank">vulnhuntr</a> - Vulnhuntr leverages the power of LLMs to automatically create and analyze entire code call chains starting from remote user input and ending at server output for detection of complex, multi-step, security-bypassing vulnerabilities that go far beyond what traditional static code analysis tools are capable of performing.</li>
<li><a href="https://github.com/ngalongc/AuthzAI" target="_blank">AuthzAI</a> - An automated tool to test and analyze API endpoints for potential permission model violations using OpenAI structured outputs.</li>
<li><a href="https://github.com/samyk/rflasermic" target="_blank">rflasermic</a> - From DEFCON32 - RF-modulated high fidelity laser microphone and keystroke sniffer</li>
<li><a href="https://github.com/Offensive-Panda/LsassReflectDumping" target="_blank">LsassReflectDumping</a> - This tool leverages the Process Forking technique using the RtlCreateProcessReflection API to clone the lsass.exe process. Once the clone is created, it utilizes MINIDUMP_CALLBACK_INFORMATION callbacks to generate a memory dump of the cloned process.</li>
<li><a href="https://github.com/akamai/akamai-security-research/tree/main/PoCs/cve-2024-43532" target="_blank">CVE-2024-43532</a> - PoC of CVE-2024-43532 by Akamai Security Research</li>
<li><a href="https://github.com/reveng007/DarkWidow" target="_blank">DarkWidow</a> -  Indirect Dynamic Syscall, SSN + Syscall address sorting via Modified TartarusGate approach + Remote Process Injection via APC Early Bird + Spawns a sacrificial Process as target process + (ACG+BlockDll) mitigation policy on spawned process + PPID spoofing + Api resolving from TIB + API hashing.</li>
<li><a href="https://github.com/momo5502/emulator" target="_blank">emulator</a> -  🪅 Windows User Space Emulator. A high-performance Windows process emulator that operates at the syscall level, providing full control over process execution through comprehensive hooking capabilities.</li>
<li><a href="https://github.com/nullenc0de/servicelens" target="_blank">servicelens</a> - ServiceLens is a Python tool for analyzing services linked to Microsoft 365 domains. It scans DNS records like SPF and DMARC to identify services, categorizing them into Email, Cloud, Security, and more.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/vxfemboy/ghostport" target="_blank">ghostport</a> - A high-performance port spoofing tool built in Rust. Confuse port scanners with dynamic service emulation across all ports. Features customizable signatures, efficient async handling, and easy traffic redirection.</li>
<li><a href="https://github.com/nianticlabs/venator" target="_blank">venator</a> - A flexible threat detection platform that simplifies rule management and deployment using K8s CronJob and Helm, but can also run standalone or with other job schedulers like Nomad.</li>
<li><a href="https://github.com/microsoft/openvmm" target="_blank">openvmm</a> - Home of OpenVMM and OpenHCL.</li>
<li><a href="https://github.com/getomni-ai/zerox" target="_blank">zerox</a> - A dead simple way of OCR-ing a document for AI ingestion. Documents are meant to be a visual representation after all. With weird layouts, tables, charts, etc.</li>
<li><a href="https://powershellisfun.com/2024/10/17/query-winget-software-installer-data-with-powershell/" target="_blank">Query WinGet software installer data with PowerShell</a> - Don't sleep on WinGet! It's a great way to install software on Windows.</li>
<li><a href="https://github.com/Versent/saml2aws" target="_blank">saml2aws</a> - CLI tool which enables you to login and retrieve AWS temporary credentials using a SAML IDP</li>
<li><a href="https://github.com/mandiant/GoReSym" target="_blank">GoReSym</a> - Go symbol recovery tool</li>
<li><a href="https://github.com/microsoft/BitNet" target="_blank">BitNet</a> -  Official inference framework for 1-bit LLMs</li>
<li><a href="https://github.com/Nuitka/Nuitka" target="_blank">Nuitka</a> - Nuitka is a Python compiler written in Python. It's fully compatible with Python 2.6, 2.7, 3.4-3.12. You feed it your Python app, it does a lot of clever things, and spits out an executable or extension module.</li>
<li><a href="https://github.com/g0h4n/RustHound-CE" target="_blank">RustHound-CE</a> - Active Directory data ingestor for BloodHound Community Edition written in Rust. 🦀</li>
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
