Title: Last Week in Security (LWiS) - 2026-03-09
Date: 2026-03-09 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2026-03-09
Author: Erik
Summary: Ludus 2 (<a href="https://x.com/badsectorlabs" target="_blank">@badsectorlabs</a>), new GOAD lab (<a href="https://x.com/M4yFly" target="_blank">@M4yFly</a>), 🍪 hack (<a href="https://x.com/XeEaton" target="_blank">@XeEaton</a>), DPAPI + Nemesis (<a href="https://x.com/harmj0y" target="_blank">@harmj0y</a> + <a href="https://x.com/tifkin_" target="_blank">@tifkin_</a>), iOS exploit kit found (<a href="https://x.com/Mandiant" target="_blank">@Mandiant</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2026-03-02 to 2026-03-09.</p>
<aside class="m-block m-success">
<h3>Ludus 2!</h3>
<p>Our open source cyber range platform <a href="https://ludus.cloud" target="_blank">Ludus</a> has become the go-to tool for cybersecurity professionals (red and blue teams) since its release two years ago. We're excited to launch version 2 today, with tons of new features (cluster support, web ui, group management, SSO, and more!). Check out the updated site <a href="https://ludus.cloud/" target="_blank">here</a> and the <a href="https://docs.ludus.cloud/docs/upgrading-from-v1" target="_blank">upgrade docs</a>!</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/coruna-powerful-ios-exploit-kit" target="_blank">Coruna: The Mysterious Journey of a Powerful iOS Exploit Kit</a> - The kit only works on iOS 13-17.2.1 (from 2023), so as always having an up to date device makes you much harder to exploit (and moreso if you have the latest hardware with additional hardware based protections like <a href="https://security.apple.com/blog/memory-integrity-enforcement/" target="_blank">Memory Integrity Enforcement (MIE)</a>). Pretty impressive there is a kit out there with 23 separate iOS exploits (5 full chains) that all work together nicely. This kit was likely caught as it was being used rather recklessly (a pop up telling users to visit the site on iOS and targeting any user who landed on the page is bold), but consider how many of these kits work on iOS 26 and are currently being used more carefully in targeted attacks. If you may be a target, consider enabling <a href="https://support.apple.com/en-us/105120" target="_blank">Lockdown Mode</a>. What are the odds this was was the kit <a href="https://cyberscoop.com/l3harris-executive-peter-williams-sentenced-zero-day-exploits-russia/" target="_blank">sold by the L3Harris executive to Russia?</a>.</li>
<li><a href="https://health.aws.amazon.com/health/status" target="_blank">Operational issue - Multiple services (UAE)</a> - Does your disaster recovery plan include drones targeting your datacenter? AWS' ME-CENTRAL-1 took direct hits causing massive outages.</li>
<li><a href="https://www.reuters.com/business/ziff-davis-sell-connectivity-division-accenture-12-billion-2026-03-03/" target="_blank">Ziff Davis to sell Ookla and Downdetector to Accenture as part of $1.2 billion deal</a> - $1.2B USD for the speedtest.net company?!</li>
<li><a href="https://www.whitehouse.gov/wp-content/uploads/2026/03/President-Trumps-Cyber-Strategy-for-America.pdf" target="_blank">[PDF] President Trump’s CYBER STRATEGY for America</a> - A few interesting points in this short document. "We will unleash the private sector by creating incentives to identify and disrupt adversary networks and scale our national capabilities." Sounds like contractors are about to get in on some offensive operations. <a href="https://www.defenseone.com/threats/2024/06/china-turning-private-firms-offensive-cyber-operations/397767/" target="_blank">China</a> has been doing this for years. Russia tacitly approves of ransomware groups as long as they don't target Russian speaking countries. I'm not sure why the government is involved in, "supporting the security of cryptocurrencies and blockchain technologies." Wasn't the original point of cryptocurrency to break from government and institutional control? Perhaps Trump wants to <a href="https://www.reuters.com/investigations/inside-trump-familys-global-crypto-cash-machine-2025-10-28/" target="_blank">secure his own bag</a>. It also states, "America’s cyber workforce... is an asset worthy of great investment and essential to our nation’s economic prosperity and security." And yet <a href="https://cyberscoop.com/cisa-personnel-cuts-trump-second-term-analysis/" target="_blank">across party lines and industry, the verdict is the same: CISA is in trouble</a>.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.watchtowr.com/sometimes-you-can-just-feel-the-security-in-the-design-junos-os-evolved-cve-2026-21902-rce/" target="_blank">Sometimes, You Can Just Feel The Security In The Design (Juniper Junos Evolved CVE-2026-21902 Pre-Auth RCE)</a> - This might be the simplest watchTowr post I've ever read. A service running as root and listening on all interfaces will just execute commands without authentication. There are two extra requests to schedule the command but really that's it. PoC: <a href="https://github.com/watchtowrlabs/watchTowr-vs-JunosEvolved-CVE-2026-21902" target="_blank">watchTowr-vs-JunosEvolved-CVE-2026-21902</a>.</li>
<li><a href="https://aff-wg.org/2026/03/03/a-scalpel-a-hammer-and-a-foot-gun/" target="_blank">A scalpel, a hammer, and a foot gun</a> - "What would change in red teaming (or cybersecurity even), if there was no fear of “burning a tool” because of its content tells and behavior was the only meaningful battleground?" Mudge drops the coolest tool so far in the Tradecraft Garden (personal opinion). This ability to on the fly edit compiled binaries has existed in custom tooling on advanced red teams before, but having it built into the flow of PICOs and atomic capability building is awesome. That being said, I'm sure people will start using <cite>ised</cite> against their own tooling as well. It's that awesome. The video walk through at the end of the post is worth the watch. Rasta (the most prolific poster of Crystal Palace material outside of Mudge himself?) also put out a post: <a href="https://rastamouse.me/islands-of-invariance/" target="_blank">Islands of Invariance</a>.</li>
<li><a href="https://bishopfox.com/blog/beyond-electron-attacking-alternative-desktop-application-frameworks" target="_blank">Beyond Electron: Attacking Alternative Desktop Application Frameworks</a> - You've seen all the XSS to RCE attacks on Electron apps, but how about the newer web-framework-to-app builder, Tauri. While more difficult (and disabled by default), under the right circumstances XSS can be RCE in Tauri as well.</li>
<li><a href="https://www.codeant.ai/security-research/pac4j-jwt-authentication-bypass-public-key" target="_blank">CVE-2026-29000: Critical Authentication Bypass in pac4j-jwt - Using Only a Public Key (CVSS 10)</a> - A simple null check ended up bypassing all auth. These are the kinds of vulnerabilities that the current generation of AI models excel at finding (keeping track of state, tracing flows, checking logic).</li>
<li><a href="https://specterops.io/blog/2026/03/04/offensive-dpapi-with-nemesis/" target="_blank">Offensive DPAPI With Nemesis</a> - Something to be said for the developers behind DPAPI and Chrome that it takes a 3,000+ word post to explain how to dump credentials from a Browser on Windows in 2026. A few years ago this was all in a SQLite database, unencrypted.</li>
<li><a href="https://bishopfox.com/blog/cve-2026-21643-pre-authentication-sql-injection-in-forticlient-ems-7-4-4" target="_blank">Pre-Authentication SQL Injection in FortiClient EMS 7.4.4 - CVE-2026-21643</a> - This feels like a vulnerability that static source code scanners would find easily; user controlled data into a format string that is used as a SQL query. Classic SQLi.</li>
<li><a href="https://eaton-works.com/2026/03/09/skcet-hack/" target="_blank">Using cookies to hack into a tech college’s admission system</a> - Speaking of classic vulnerabilities... this is another blast from the past (early 2000s?).</li>
<li><a href="https://jakobfriedl.github.io/blog/conquest-profiles/" target="_blank">Customizing C2 Traffic using Advanced Malleable Network Profiles</a> - Conquest is the best open source C2 since Adaptix?</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul><li><a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">PhantomSec | Advanced Offensive Capabilities Automated - EvadeX</a> <span class="m-label m-flat m-success">Sponsored</span> - EvadeX is an evasion-as-a-service platform for red teams and pentesters who want modern, continuously-updated evasive tradecraft without turning every engagement into an R&amp;D project. Generate highly customizable, low-signature payloads through a simple web workflow so you can tune to the target and stay focused on the engagement. Trusted by teams from small consultancies to the Fortune 10. <a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">Get callbacks past EDR today!</a></li></ul><ul>
<li><a href="https://mayfly277.github.io/posts/Dracarys-lab/" target="_blank">Dracarys</a> - New GOAD lab from Mayfly!</li>
<li><a href="https://github.com/Macmod/sopa" target="_blank">sopa</a> - A practical client for ADWS in Golang.</li>
<li><a href="https://github.com/ZephrFish/ludus-defender-lab" target="_blank">ludus-defender-lab</a> - Ludus range configs and Ansible roles for a Windows security lab pre-staged for MDE and MDI, with a fully misconfigured ADCS installation for detection coverage testing.</li>
<li><a href="https://github.com/ChiChou/vscode-frida" target="_blank">vscode-frida</a> - Unofficial frida extension for VSCode.</li>
<li><a href="https://github.com/ghostvectoracademy/DLLHijackHunter" target="_blank">DLLHijackHunter</a> - Automated DLL Hijacking Detection with Zero False Positives.</li>
<li><a href="https://github.com/Whispergate/ludus_nginx_redirector" target="_blank">ludus_nginx_redirector</a> - This role is designed for use in Ludus ranges to proxy C2 traffic with extensive customization options for routing, rate limiting, and operational security.</li>
<li><a href="https://github.com/zerozenxlabs/CVE-2026-20127---Cisco-SD-WAN-Preauth-RCE" target="_blank">CVE-2026-20127---Cisco-SD-WAN-Preauth-RCE</a> - This repository contains a working proof-of-concept exploit for CVE-2026-20127, a critical pre-authentication vulnerability in Cisco Catalyst SD-WAN Controller (formerly vSmart) and Catalyst SD-WAN Manager (formerly vManage) that has been actively exploited in the wild since 2023.</li>
<li><a href="https://github.com/mandiant/speakeasy/releases/tag/v2.0.0b1" target="_blank">Speakeasy v2.0.0b1</a> - The Windows malware emulation framework that executes binaries, drivers, and shellcode in a modeled Windows runtime instead of a full VM got a major update!</li>
<li><a href="https://github.com/vulhunt-re/vulhunt" target="_blank">vulhunt</a> - Vulnerability detection framework by Binarly's REsearch team</li>
<li><a href="https://github.com/dazzyddos/PrivHound" target="_blank">PrivHound</a> - A BloodHound OpenGraph collector that models Windows local privilege escalation as interconnected attack paths.</li>
<li><a href="https://github.com/BlackSnufkin/Maverick" target="_blank">Maverick</a> - Adaptix C2 agent using Crystal Palace PIC linker and PICO module system</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/GreatScott/enject" target="_blank">enject</a> - Hide .env secrets from prAIng eyes: secrets live in local encrypted stores (per project) and are injected directly into apps at runtime, never touching disk as plaintext.</li>
<li><a href="https://github.com/Cobalt-Strike/eden" target="_blank">eden</a> - A PoC UDRL for Cobalt Strike built with Crystal Palace that combines Raphael Mudge's page streaming technique with a modular call gate (Draugr)</li>
<li><a href="https://github.com/Alex-Gilbert/unredact" target="_blank">unredact</a> - Unredact uses computer vision, font-aware constraint solving, and LLM reasoning to figure out what text is hiding under those black bars. Upload a PDF, and it will detect redactions, calculate exactly which strings could fit based on pixel-width constraints, and let you visually verify guesses with a live overlay.</li>
<li><a href="https://blog.zsec.uk/ltr101-getting-into-industry-in-2026/" target="_blank">LTR101 - Getting into Industry in 2026</a> - Andy updates his "breaking into cybersecurity" post for 2026. Guess what made it in the Resources section this year? <a href="https://ludus.cloud/" target="_blank">Ludus</a> 😎.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 496 (+0)</p>
<p>Blogs monitored: 442 (+0)</p>
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
