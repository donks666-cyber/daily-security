Title: Last Week in Security (LWiS) - 2025-09-02
Date: 2025-09-02 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-09-02
Author: Erik
Summary: Azure AD via weak ACLS (<a href="https://x.com/xybytes" target="_blank">@xybytes</a>), HTTP stealth proxy (<a href="https://x.com/IAmMandatory" target="_blank">@IAmMandatory</a>), Dll sideloading for initial access (<a href="https://x.com/Print3M_" target="_blank">@Print3M_</a>), kernel-hack-drill (<a href="https://x.com/a13xp0p0v" target="_blank">@a13xp0p0v</a>), Sitecore RCE (<a href="https://x.com/chudyPB" target="_blank">@chudyPB</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-08-25 to 2025-09-02.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift" target="_blank">Widespread Data Theft Targets Salesforce Instances via Salesloft Drift</a> - The third party Salesloft chatbot "Drfit" had their OAuth tokens used to compromise all (?) Salesloft customer's Salesforce accounts. <a href="https://blog.cloudflare.com/response-to-salesloft-drift-incident/" target="_blank">Cloudflare</a> has a detailed write up of their investigation.</li>
<li><a href="https://www.newsweek.com/hackers-issue-ultimatum-data-breach-2122489" target="_blank">Hackers Issue Ultimatum to Google After Data Breach Warning</a> - Being called out by name to be fired by a threat actor has to be a crowning achievement of a threat intel specialist right?</li>
<li><a href="https://android-developers.googleblog.com/2025/08/elevating-android-security.html" target="_blank">A new layer of security for certified Android devices</a> - Android does away with sideloading, requiring all apps to be from "verified developers." Android becomes a walled garden, much like iOS? <a href="https://www.youtube.com/watch?v=8WfRcnF4iZI" target="_blank">"You either die a hero, or you live long enough to see yourself become the villain."</a></li>
<li><a href="https://fastcode.io/2025/08/30/the-69-billion-domino-effect-how-vmwares-debt-fueled-acquisition-is-killing-open-source-one-repository-at-a-time/" target="_blank">The $69 Billion Domino Effect: How VMware’s Debt-Fueled Acquisition Is Killing Open Source, One Repository at a Time</a> - Bitnami had 18 years of providing a trustworthy free service profitably, but like all things acquired by Broadcom, it now must be squeezed for every last cent.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://specterops.io/blog/2025/08/27/dough-no-revisiting-cookie-theft/" target="_blank">Dough No! Revisiting Cookie Theft</a> - Chromium based browsers have moved to protect cookies using Window's Data Protection API (DPAPI) and more recently Application Bound encryption primitives. That's just another hurdle for attackers, as is exposed in this post. With more and more data moving to Software as a Service (SaaS) applications, browser cookie compromise is becoming a bigger target. The use of our free and open source <a href="https://ludus.cloud" target="_blank">Ludus</a> to setup a safe environment to test browser extensions is the always great to see. 😊</li>
<li><a href="https://xybytes.com/azure/When-Azure-Dynamic-Groups-Meet-Weak-ACLS/" target="_blank">When Azure Dynamic Groups Meet Weak ACLs</a> - Entra ID's "dynamic groups" can enable some interesting attack paths. GenericWrite over a user on-prem can allow an attacker to add them to a department that gets Azure permissions based on a dynamic group filter. Look for attributed based rules in Entra ID on your next hybrid assessment.</li>
<li><a href="https://print3m.github.io/blog/dll-sideloading-for-initial-access" target="_blank">DLL Sideloading for Initial Access – Red Team Operator's Guide</a> - A new tool and some guidance for picking DLLs to sideload for initial access.</li>
<li><a href="https://swarm.ptsecurity.com/kernel-hack-drill-and-a-new-approach-to-exploiting-cve-2024-50264-in-the-linux-kernel/" target="_blank">Kernel-hack-drill and a new approach to exploiting CVE-2024-50264 in the Linux kernel</a> - A very technical post on the 2025 Pwnie Award for the Best Privilege Escalation, a Use-After-Free in the Linux kernel.</li>
<li><a href="https://embracethered.com/blog/posts/2025/agenthopper-a-poc-ai-virus/" target="_blank">AgentHopper: An AI Virus</a> - New tools, same problems. The next generation needs to read Ken Thompson's classic <a href="https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf" target="_blank">[PDF] Reflections on Trusting Trust</a>.</li>
<li><a href="https://blog.amberwolf.com/blog/2025/august/advisory---netskope-client-for-windows---local-privilege-escalation-via-rogue-server/" target="_blank">Advisory - Netskope Client for Windows - Local Privilege Escalation via Rogue Server (CVE-2025-0309)</a> - "In Netskope Windows client versions prior to R129, It was possible to escalate privileges by forcing the client into enrolling into a rogue Netskope server. This could be abused by a low-privileged, local user in order to escalate their privileges on the client host to that of the stAgentSvc service, which runs with SYSTEM privileges."</li>
<li><a href="https://labs.watchtowr.com/cache-me-if-you-can-sitecore-experience-platform-cache-poisoning-to-rce/" target="_blank">Cache Me If You Can (Sitecore Experience Platform Cache Poisoning to RCE)</a> - Move over Adobe Experience Manager (AEM), another enterprise content management system has some remote code execution vulnerabilities!</li>
<li><a href="https://labs.watchtowr.com/the-one-where-we-just-steal-the-vulnerabilities-crushftp-cve-2025-54309/" target="_blank">The One Where We Just Steal The Vulnerabilities (CrushFTP CVE-2025-54309)</a> - The CrushFTP is slightly older news, but the mention of a, "universal in-memory kernel backdoor that we can inject into virtualized appliances, allowing us to universally jailbreak appliances and deploy EDR-tier capabilities onto the device itself to capture network, disk, and memory artifacts when exploitation occurs" is very interesting.</li>
<li><a href="https://wilgibbs.com/blog/defcon-finals-mcp/" target="_blank">All You Need Is MCP - LLMs Solving a DEF CON CTF Finals Challenge</a> - An MCP server hooked up to IDA Pro solves and then patches a DEF CON CTF challenge with minimal prompting.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Paradoxis/ADSyncDump-BOF" target="_blank">ADSyncDump-BOF</a> - The ADSyncDump BOF is a port of Dirk-Jan Mollema's adconnectdump.py / ADSyncDecrypt into a Beacon Object File (BOF) with zero dependencies.</li>
<li><a href="https://github.com/mandatoryprogrammer/thermoptic/" target="_blank">thermoptic</a> - A next-generation HTTP stealth proxy which perfectly cloaks requests as the Chrome browser across all layers of the stack.</li>
<li><a href="https://github.com/Print3M/DllShimmer" target="_blank">DllShimmer</a> - Weaponize DLL hijacking easily. Backdoor any function in any DLL.</li>
<li><a href="https://github.com/AmberWolfCyber/UpSkope" target="_blank">UpSkope</a> - Custom IPC Client and Proof of Concept exploit for CVE-2025-0309 (Netskope Windows Client LPE).</li>
<li><a href="https://github.com/xaitax/NTSleuth" target="_blank">NTSleuth</a> - Comprehensive Windows Syscall Extraction &amp; Analysis Framework.</li>
<li><a href="https://github.com/alex3O/BYOVD-DriverKiller/blob/master/README.en.md" target="_blank">BYOVD-DriverKiller</a> - Driver Reversing &amp; Exploitation.</li>
<li><a href="https://github.com/poppopjmp/VMDragonSlayer" target="_blank">VMDragonSlayer</a> - Automated multi-engine framework for unpacking, analyzing, and devirtualizing binaries protected by commercial and custom Virtual Machine based protectors. Combines Dynamic Taint Tracking, Symbolic Execution, Pattern &amp; Semantic Classification, and Machine Learning–driven prioritization to dramatically reduce manual reverse engineering time.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Semperis/SAMLSmith" target="_blank">SAMLSmith</a> is a C# tool for generating custom SAML responses and implementing Silver SAML and Golden SAML attacks. It provides comprehensive functionality for security researchers and penetration testers working with SAML-based authentication systems.</li>
<li><a href="https://lyra.horse/blog/2025/08/you-dont-need-js/" target="_blank">You no longer need JavaScript</a> - I agree. LWiS uses no JavaScript except for the search bar.</li>
<li><a href="https://www.helpnetsecurity.com/2025/08/27/plex-media-server-cve-2025-34158-attack/?ref=selfh.st" target="_blank">300k+ Plex Media Server instances still vulnerable to attack via CVE-2025-34158</a> - The popular media streaming software was the initial access vector for the <a href="https://thehackernews.com/2023/03/lastpass-hack-engineers-failure-to.html" target="_blank">LastPass Hack</a>. Update!</li>
<li><a href="https://github.com/gabriel-sztejnworcel/pipe-intercept" target="_blank">pipe-intercept</a> - Intercept Windows Named Pipes communication using Burp or similar HTTP proxy tools.</li>
<li><a href="https://github.com/basecamp/omarchy" target="_blank">omarchy</a> - Opinionated Arch/Hyprland Setup.</li>
<li><a href="https://github.com/DarkCoderSc/OptixGate" target="_blank">OptixGate</a> - Open-source multi-purpose remote access tool for Microsoft Windows.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 458 (+2)</p>
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
