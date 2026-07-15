Title: Last Week in Security (LWiS) - 2024-03-18
Date: 2024-03-18 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-03-18
Author: Erik
Summary: Windows patch diffing (<a href="https://twitter.com/clearbluejar" target="_blank">@clearbluejar</a>), FileCatalyst RCE (<a href="https://twitter.com/Nettitude_Labs" target="_blank">@Nettitude_Labs</a>), Windows/Frida course (<a href="https://twitter.com/FuzzySec" target="_blank">@FuzzySec</a>), Tor WebTunnel bridges (<a href="https://twitter.com/torproject" target="_blank">@torproject</a>, Pixel 7/8 Pro exploit (<a href="https://twitter.com/_simo36" target="_blank">@_simo36</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-03-11 to 2024-03-18.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://devblogs.microsoft.com/microsoft365dev/stay-ahead-of-the-game-with-the-latest-updates-to-the-microsoft-365-developer-program/" target="_blank">Stay ahead of the game with the latest updates to the Microsoft 365 Developer Program</a> - Changes in M365 Developer program. What used to be a free M365 developer subscription is now a pay walled service; it requires an active subscription to Visual Studio Enterprise.</li>
<li><a href="https://blog.projectdiscovery.io/nuclei-3-2/" target="_blank">Nuclei v3.2 Release with Authenticated Scanning, Advanced Fuzzing &amp; more</a> - Authenticated scanning support is great. Nuclei is a great example of the power of open-source.</li>
<li><a href="https://x.ai/blog/grok-os" target="_blank">Open Release of Grok-1</a> - This is the raw base model checkpoint from the Grok-1 pre-training phase, which concluded in October 2023. This means that the model is not fine-tuned for any specific application, such as dialogue. It's up to you to determine if this is a PR play as Grok isn't useful for much that other smaller open source models can't do.</li>
<li><a href="https://cofense.com/blog/svg-files-abused-in-emerging-campaigns/" target="_blank">SVG Files Abused in Emerging Campaigns</a> - How TAs are using SVGs for HTML smuggling.</li>
<li><a href="https://www.bleepingcomputer.com/news/security/tors-new-webtunnel-bridges-mimic-https-traffic-to-evade-censorship/?ref=selfh.st#google_vignette" target="_blank">Tor's new WebTunnel bridges mimic HTTPS traffic to evade censorship</a> - A new censorship resistant method to connect to the Tor network!</li>
<li><a href="https://www.linkedin.com/pulse/using-socially-responsible-marketing-fund-non-commercial-kfa7f/" target="_blank">Using socially responsible marketing to fund non-commercial open source security tools</a> - I dig this and it's working since they are getting "free" marketing out of it right now.</li>
<li><a href="https://twitter.com/FuzzySec/status/1767902907750625646" target="_blank">New course: "Windows Instrumentation with Frida"</a> - <a href="https://twitter.com/FuzzySec" target="_blank">@FuzzySec</a> is a well know researcher who has put out great content and tools. Excited to dig into this offering.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://rezaduty-1685945445294.hashnode.dev/attacking-android" target="_blank">Attacking Android</a> - Blog post some common attack vectors if you're assessing Android environments.</li>
<li><a href="https://posts.specterops.io/summoning-ragnarok-with-your-nemesis-7c4f0577c93b" target="_blank">Summoning RAGnarok With Your Nemesis</a> - A Nemesis powered Retrieval-Augmented Generation (RAG) chatbot.</li>
<li><a href="https://salt.security/blog/security-flaws-within-chatgpt-extensions-allowed-access-to-accounts-on-third-party-websites-and-sensitive-data" target="_blank">Security Flaws within ChatGPT Ecosystem Allowed Access to Accounts On Third-Party Websites and Sensitive Data</a> - Write-up on vulnerabilities found during this research on ChatGPT ecosystem including 0-click attacks. Note these flaws are in the earlier "plugins" not the custom "GPTs" feature commonly seen today.</li>
<li><a href="https://redcanary.com/threat-detection-report/" target="_blank">2024 Threat Detection Report</a> - Red Canary's 2024 Threat Detection Report. Emphasis on "Detection". Take a look at their most commonly identify tools. If you're a red teamer using unmodified versions of those tools, consider yourself caught. Another interesting comment in this report: "Our new industry analysis showcases how adversaries reliably leverage the same small set of 10-20 techniques against organizations, regardless of their sector or industry.". Red teamers don't need a bunch of fancy techniques. Stick to a few OPSEC friendly/effective techniques and focus on your objectives.</li>
<li><a href="https://blog.includesecurity.com/2024/03/discovering-deserialization-gadget-chains-in-rubyland/" target="_blank">Discovering Deserialization Gadget Chains in Rubyland</a> - Write-up that details the process and insights gained from creating a Ruby deserialization gadget chain from scratch, utilizing libraries such as action_view, active_record, dry-types, and eventmachine, to demonstrate deserialization exploitation in Ruby apps.</li>
<li><a href="https://www.horizon3.ai/attack-research/attack-blogs/fortiwlm-the-almost-story-for-the-forti-forty/" target="_blank">Fortinet FortiWLM Deep-Dive, IOCs, and the Almost Story of the “Forti Forty”</a> - Technical analysis of some recent patched and unpatched (sigh) Fortinet vulnerabilities. Of course there is unauthenticated RCE as root...</li>
<li><a href="https://www.netspi.com/blog/technical/cloud-penetration-testing/azure-user-assigned-managed-identities-via-deployment-scripts/" target="_blank">Azure Deployment Scripts: Assuming User-Assigned Managed Identities</a> - Over-permissioned deployment Scripts and User-Assigned Managed Identities enables privilege escalation.</li>
<li><a href="https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#pivoting-on-ip-addresses-discovering-a-phishing-campaign" target="_blank">Tales from the cloud trenches: Using malicious AWS activity to spot phishing campaigns</a> - How poor OPSEC by threat actors against AWS burned them. IoCs at the end for all defenders.</li>
<li><a href="https://research.nccgroup.com/2024/03/14/ltair-the-lte-air-interface-tool/" target="_blank">LTair: The LTE Air Interface Tool</a> - LTair, a tool that allows NCC Group to perform different attacks on the LTE Control Plane via the air interface. Niche assessment type. Looks neat but the tool isn't actually released yet?</li>
<li><a href="https://clearbluejar.github.io/posts/patch-tuesday-diffing-cve-2024-20696-windows-libarchive-rce/" target="_blank">Patch Tuesday Diffing: CVE-2024-20696 - Windows Libarchive RCE</a> - A nice post on patch diffing Windows DLLs.</li>
<li><a href="https://labs.nettitude.com/blog/cve-2024-25153-remote-code-execution-in-fortra-filecatalyst/" target="_blank">CVE-2024-25153: Remote Code Execution in Fortra FileCatalyst</a> - String obfuscation will not save you from logic bugs like path traversal.</li>
<li><a href="https://download.vusec.net/papers/ghostrace_sec24.pdf" target="_blank">[PDF] GhostRace: Exploiting and Mitigating Speculative Race Conditions</a> - These speculative execution style bugs have seemingly no end.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/TarlogicSecurity/BlueSpy" target="_blank">BlueSpy</a> - Proof of concept to record and replay audio from a bluetooth device without the legitimate user's awareness.</li>
<li><a href="https://blog.syss.com/posts/introducing-azurenum/" target="_blank">Introducing AzurEnum</a> - The latest Azure tool - Intended to give pentesters/red teamers a good idea of the main security issues of an azure tenant and its permission structure. The code is <a href="https://github.com/SySS-Research/azurenum" target="_blank">here</a>.</li>
<li><a href="https://github.com/g0ldencybersec/gungnir" target="_blank">Gungnir</a> - Gungnir is a command-line tool written in Go that continuously monitors certificate transparency (CT) logs for newly issued SSL/TLS certificates.</li>
<li><a href="https://github.com/MzHmO/SymProcAddress" target="_blank">SymProcAddress</a> - Zero EAT touch way to retrieve function addresses (GetProcAddress on steroids)</li>
<li><a href="https://github.com/skelsec/anfs" target="_blank">anfs</a> - Asynchronous NFSv3 client in pure Python</li>
<li><a href="https://github.com/0x36/Pixel_GPU_Exploit" target="_blank">Pixel_GPU_Exploit</a> - Android 14 kernel exploit for Pixel7/8 Pro.</li>
<li><a href="https://github.com/Wh04m1001/GamingServiceEoP" target="_blank">GamingServiceEoP</a> - Exploit for arbitrary folder move in GamingService component of Xbox. GamingService is not default service. If service is installed on system it allows low privilege users to escalate to system.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://mythicmeta.github.io/overview/" target="_blank">Mythic Community Overview</a> - Mythic agent capability matrix. Cool project for those that develop their own agents for Mythic.</li>
<li><a href="https://github.com/localsend/localsend" target="_blank">localsend</a> -  An open-source cross-platform alternative to AirDrop</li>
<li><a href="https://github.com/absolomb/FindMeAccess" target="_blank">FindMeAccess</a> - Finding gaps in Azure/M365 MFA requirements for different resources, client ids, and user agents. The tool is mostly based off Spray365's auditing logic.</li>
<li><a href="https://github.com/Krook9d/PurpleLab" target="_blank">PurpleLab</a> -  PurpleLab is an efficient and readily deployable lab solution, providing a swift setup for cybersecurity professionals to test detection rules, simulate logs, and undertake various security tasks, all accessible through a user-friendly web interface</li>
<li><a href="https://github.com/piaolin/DetectDee" target="_blank">DetectDee</a> -  Hunt down social media accounts by username, email or phone across social networks.</li>
<li><a href="https://github.com/BC-SECURITY/Moriarty" target="_blank">Moriarty</a> -  Moriarty is designed to enumerate missing KBs, detect various vulnerabilities, and suggest potential exploits for Privilege Escalation in Windows environments.</li>
<li><a href="https://github.com/SecureHats/miaow/" target="_blank">Miaow</a> -  Project Miaow is a prove of concept to escalate privileges in Microsoft Azure using an ARM template deployment</li>
<li><a href="https://payload-wizard.vercel.app/" target="_blank">Payload Wizard</a> -  AI assistant that utilizes GPT language models to interpret and generate cybersecurity payloads 🪄. Github repo is <a href="https://github.com/ANG13T/payload-wizard" target="_blank">here</a>.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 371 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
