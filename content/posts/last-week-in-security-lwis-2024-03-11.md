Title: Last Week in Security (LWiS) - 2024-03-11
Date: 2024-03-11 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-03-11
Author: Erik
Summary: Midnight Blizzard vs Microsoft, Fuzzer dev (<a href="https://twitter.com/h0mbre_" target="_blank">@h0mbre_</a>), Browserless Entra flow (<a href="https://twitter.com/_wald0" target="_blank">@_wald0</a>), SCCM one-stop-shop (<a href="https://twitter.com/subat0mik" target="_blank">@subat0mik</a> + <a href="https://twitter.com/_Mayyhem" target="_blank">@_Mayyhem</a> + <a href="https://twitter.com/garrfoster" target="_blank">@garrfoster</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-03-04 to 2024-03-11.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://krebsonsecurity.com/2024/03/incognito-darknet-market-mass-extorts-buyers-sellers/" target="_blank">Incognito Darknet Market Mass-Extorts Buyers, Sellers</a> - Getting your darknet market shutdown is the worst thing that can happen right? What if the market operators then extort both the buyers and sellers? We'll see if this becomes the largest darknet market data dump ever on April 1st.</li>
<li><a href="https://msrc.microsoft.com/blog/2024/03/update-on-microsoft-actions-following-attack-by-nation-state-actor-midnight-blizzard/" target="_blank">Update on Microsoft Actions Following Attack by Nation State Actor Midnight Blizzard</a> - Russian actors are still all up in Microsoft, this time using "secrets of different types" to gain access to source code and "internal systems."</li>
<li><a href="https://www.justice.gov/opa/pr/chinese-national-residing-california-arrested-theft-artificial-intelligence-related-trade" target="_blank">Chinese National Residing in California Arrested for Theft of Artificial Intelligence-Related Trade Secrets from Google</a> - Defendant allegedly pilfered technology from Google while secretly working for two PRC-based technology companies.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://alephsecurity.com/2024/03/07/kontrol-lux-lock-2/" target="_blank">Say Friend and Enter: Digitally lockpicking an advanced smart lock (Part 2: discovered vulnerabilities)</a> - Digital locks are vulnerable to a variety of attacks, but for most threat models a brick is a bigger threat than an exposed debug port.</li>
<li><a href="https://h0mbre.github.io/Loading_Bochs/" target="_blank">Fuzzer Development 3: Building Bochs, MMU, and File I/0</a> - Must read series if you are at all interested in fuzzers.</li>
<li><a href="https://rastamouse.me/yarp-as-a-c2-redirector/" target="_blank">YARP as a C2 Redirector</a> - C2 redirectors via the <a href="https://github.com/microsoft/reverse-proxy" target="_blank">YARP project</a>. This was the solution built my microsoft for internal engineers to use as a reverse proxy. Potential option for your team to explore if you're migrating away from apache/nginx rewrite rules.</li>
<li><a href="https://0xf00sec.github.io/2024/03/09/MacOs-X.html" target="_blank">MacOS Malware Dev</a> - This article explores macOS malware development, covering the architecture, security features, and coding practices. Good read!</li>
<li><a href="https://www.akamai.com/blog/security-research/2024/mar/leaking-ntlm-credentials-through-windows-themes" target="_blank">Leaking NTLM Credentials Through Windows Themes</a> - This was patched in January (CVE-2024-21320) but serves as a reminder that NTLM will continue to be a pain point until eliminated.</li>
<li><a href="https://research.aurainfosec.io/pentest/git-rotate/" target="_blank">Git-Rotate: Leveraging GitHub Actions for Password Spraying</a> - Good way to burn your github account but this outside the box thinking is awesome.</li>
<li><a href="https://posts.redteamtacticsacademy.com/powerquery-for-red-teamers-unleashing-the-potential-of-m-language-and-macros-fc74a72edd5b" target="_blank">Power Query for Red Teamers: Unleashing the Potential of M Language and Macros</a> - This blog post explores Power Query's potential for red teamers, emphasizing the M language for data manipulation and macros for actionable insights.</li>
<li><a href="https://securelist.com/network-tunneling-with-qemu/111803/" target="_blank">Network tunneling with… QEMU?</a> - Creative way of using QEMU for internal access.</li>
<li><a href="https://fin3ss3g0d.net/index.php/2024/03/04/smishing-with-evilgophish/" target="_blank">Smishing with EvilGophish</a> - Using EvilGophish to send those pesky texts. I wonder how many red teams are actually simulating/emulating this attack vector.</li>
<li><a href="https://posts.specterops.io/browserless-entra-device-code-flow-0802f3bbb91a" target="_blank">Browserless Entra Device Code Flow</a> - Performing every step in Entra's OAuth 2.0 Device Code flow — including the user authentication steps — without a browser!</li>
<li><a href="https://mrd0x.com/sentinelone-persistence-via-menu-context/" target="_blank">Hijacking &amp; Spoofing Context Menu Options</a> - Hijacking SentinelOne's “Scan For Threats” context menu option and creating your own option for persistence.</li>
<li><a href="https://trustedsec.com/blog/unwelcome-guest-abusing-azure-guest-access-to-dump-users-groups-and-more" target="_blank">Unwelcome Guest: Abusing Azure Guest Access to Dump Users, Groups, and more</a> - Friendly reminder of what guest access can do for your organization. <a href="https://aadinternals.com/post/quest_for_guest/" target="_blank">Guest access</a> enumeration and attack vectors have been around for quite some time.</li>
<li><a href="https://www.preludesecurity.com/blog/event-tracing-for-windows-etw-your-friendly-neighborhood-ipc-mechanism" target="_blank">Event Tracing for Windows (ETW): Your Friendly Neighborhood IPC Mechanism</a> - Using ETW as your C2 communication channel? Wicked. No PoC was released but does spark some discussions and thoughts on how lateral movement traffic should look like to avoid detection.</li>
<li><a href="https://posts.specterops.io/misconfiguration-manager-overlooked-and-overprivileged-70983b8f350d" target="_blank">Misconfiguration Manager: Overlooked and Overprivileged</a> - :fire: The Specterops team is crushing it. This introduces an SCCM Attack matrix and standardizes SCCM attack naming.</li>
<li><a href="https://zolder.io/aitm-attacks-using-cloudflare-workers/" target="_blank">Building a AITM attack tool in Cloudflare Workers (174 LOC)</a> - The research on MITM detection and attacks keeps ramping up. This <a href="https://gist.github.com/douglarek/33d653cf09cd6d80df2e9dc561b19079" target="_blank">gist (cloudflare-worker-proxy.js)</a> contains the PoC. Very powerful attack.</li>
<li><a href="https://www.netspi.com/blog/technical/red-team-operations/microsoft-outlook-remote-code-execution-cve-2024-21378/" target="_blank">CVE-2024-21378 — Remote Code Execution in Microsoft Outlook</a> - NetSPIs write-up on how they discovered CVE-2024-21378 which is an authenticated RCE vulnerability via synced form objects.</li>
<li><a href="https://www.horizon3.ai/attack-research/attack-blogs/nextchat-an-ai-chatbot-that-lets-you-talk-to-anyone-you-want-to/" target="_blank">NextChat: An AI Chatbot That Lets You Talk to Anyone You Want To</a> - Unpatched SSRF details disclosed for <a href="https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web" target="_blank">ChatGPT-Next-Web</a> . Seems like a popular open-source project for those wanting to get a chatGPT UI.</li>
<li><a href="https://blog.delivr.to/webassembly-smuggling-it-wasmt-me-648a62547ff4" target="_blank">WebAssembly Smuggling: It WASM't me</a> - Take your HTML smuggling to the next level with web assembly. Now your smuggling can <a href="https://www.whitehouse.gov/oncd/briefing-room/2024/02/26/press-release-technical-report/" target="_blank">make the whitehouse happy</a> since you can write it in Rust.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/MzHmO/Parasite-Invoke" target="_blank">Parasite-Invoke</a> - Hide your P/Invoke signatures through other people's signed assemblies</li>
<li><a href="https://github.com/techspence/ADeleginator" target="_blank">ADeleginator</a> - A companion tool that uses ADeleg to find insecure trustee and resource delegations in Active Directory</li>
<li><a href="https://github.com/subat0mik/Misconfiguration-Manager" target="_blank">Misconfiguration Manager</a> - Misconfiguration Manager is a central knowledge base for all known Microsoft Configuration Manager tradecraft and associated defensive and hardening guidance.</li>
<li><a href="https://github.com/nettitude/yasha" target="_blank">yasha</a> - Yet another security header analyzer.</li>
<li><a href="https://github.com/MythicAgents/nemesis" target="_blank">nemesis</a> - Nemesis agent for Mythic.</li>
<li><a href="https://github.com/chvancooten/NimPlant/releases/tag/v1.3" target="_blank">NimPlant v1.3</a> - "a lot of code refactoring and various enhancements."</li>
<li><a href="https://github.com/gergelykalman/brew-lpe-via-periodic" target="_blank">brew-lpe-via-periodic</a> - Brew Local Privilege Escalation exploit on Intel macOS.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://jackson-t.com/are-we-helping/" target="_blank">Are We Helping?</a> Interesting perspective. Thought provoking notes about the current state of infosec.</li>
<li><a href="https://github.com/MythicAgents/freyja" target="_blank">Freyja Purple Team Agent</a> -  Freyja is a Golang, Purple Team agent that compiles into Windows, Linux and macOS x64 executables.</li>
<li><a href="https://permiso.io/blog/cloudgrappler-a-powerful-open-source-threat-detection-tool-for-cloud-environments" target="_blank">Introducing CloudGrappler: A Powerful Open-Source Threat Detection Tool for Cloud Environments</a> - Potential framework for those smaller teams that need a solution to look for known evil in their cloud environments. The question is, where do you get those indicators while they're still relevant?</li>
<li><a href="https://github.com/RichardoC/gitlab-secrets/" target="_blank">gitlab-secrets</a> - This tool analyzes a given Gitlab repository and searches for dangling or force-pushed commits containing potential secret or interesting information.</li>
<li><a href="https://github.com/NilsIrl/dockerc" target="_blank">dockerc</a> - container image to single executable compiler.</li>
<li><a href="https://github.com/SafeBreach-Labs/PoolParty" target="_blank">PoolParty</a> - A set of fully-undetectable process injection techniques abusing Windows Thread Pools.</li>
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
