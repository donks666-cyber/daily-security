Title: Last Week in Security (LWiS) - 2025-11-18
Date: 2025-11-18 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-11-18
Author: Erik
Summary: Cloudflare takes down the internet, IDA Pro gets a TUI, Rust in Android, AI-orchestrated cyber espionage, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-11-10 to 2025-11-18.</p>
<p>Last Week in Security will be off next week.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://www.alteredsecurity.com/online-labs?utm_source=badsectorlabs&amp;utm_medium=email&amp;utm_campaign=diwali_offer" style="color: #3bd267;" target="_blank">Sharpen your Red Team skills with 20% OFF</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p style="text-indent: 0;">Start your Red Team training with Altered Security! We offer affordable Red Team courses with enterprise-like hands-on labs and lifetime access to course materials.</p>
<p style="text-indent: 0;">Each course comes with an industry-recognized certification. We are the creators of the Certified Red Team Professional (CRTP), CRTE, CARTP and more. Join more than 50,000 professionals from 130+ countries.</p>
<p style="text-indent: 0;">Get 20% OFF on all courses and instructor-led bootcamps to be held in Q1 and Q2 2026 in our Black Friday deals until December 17, 2025. No coupon code required. <strong><a href="https://www.alteredsecurity.com/online-labs?utm_source=badsectorlabs&amp;utm_medium=email&amp;utm_campaign=diwali_offer" style="color: #3bd267;" target="_blank">Sign up now!</a></strong></p>
</aside><ul>
<li><a href="https://blogs.windows.com/windowsexperience/2025/11/18/preparing-for-whats-next-windows-security-and-resiliency-innovations-help-organizations-mitigate-risks-recover-faster-and-prepare-for-the-era-of-ai/" target="_blank">Preparing for what’s next: Windows security and resiliency innovations help organizations mitigate risks, recover faster and prepare for the era of AI</a> - A real word salad of a title but some interesting content like, "Sysmon functionality will soon be available in Windows."</li>
<li><a href="https://blog.cloudflare.com/18-november-2025-outage/" target="_blank">Cloudflare outage on November 18, 2025</a> - Pretty wild when your outage report contains the phrase, "I would like to apologize for the pain we caused the Internet today." Kudos to Cloudflare for timely and transparent reporting.</li>
<li><a href="https://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html" target="_blank">Rust in Android: move fast and fix things</a> - Google is writing more Rust than C/C++ in Android as of this year, and the number of memory safety bugs is decreasing rapidly because of it. Exploitation is going to look very different in just a few years. But don't worry if you're an exploit developer/researcher, just read about the FortiWeb vulnerability below.</li>
<li><a href="https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf" target="_blank">[PDF] Disrupting the first reported AI-orchestrated cyber espionage campaign</a> - This feels like marketing more than an actual threat intel report. No indicators of compromise, and very light on technical details. Now consider, how many campaigns are using models that are either designed for cyber espionage, or are not going to report on Chinese use of them for cyber espionage?</li>
<li><a href="https://arstechnica.com/gadgets/2025/11/google-will-let-android-power-users-bypass-upcoming-sideloading-restrictions/" target="_blank">Google will let Android power users bypass upcoming sideloading restrictions</a> - Was this the plan all along? Announce an unpopular change, then walk it back to the change you wanted in the first place, but now it's seen as a win vs the worse version you initially announced.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.watchtowr.com/when-the-impersonation-function-gets-used-to-impersonate-users-fortinet-fortiweb-auth-bypass/" target="_blank">When The Impersonation Function Gets Used To Impersonate Users (Fortinet FortiWeb Auth. Bypass CVE-2025-64446)</a> - A path traversal and an authentication bypass in a security appliance? Standard fare sadly.</li>
<li><a href="https://github.com/google/security-research/security/advisories/GHSA-9p78-p5g6-gcj8" target="_blank">"Astral-tokio-tar" / "uv" Arbitrary Write Path Traversal Vulnerability</a> - Not your typical path traversal vulnerability. Some creative use of symlinks to write to arbitrary files.</li>
<li><a href="https://www.atredis.com/blog/2025/9/30/drawbot-lets-hack-something-cute" target="_blank">Drawbot: Let’s Hack Something Cute!</a> - A good order-from-amazon to hacked journey.</li>
<li><a href="https://modzero.com/en/blog/no-leak-no-problem/" target="_blank">No Leak, No Problem - Bypassing ASLR with a ROP Chain to Gain RCE</a> - More solid Internet-of-Things hacking.</li>
<li><a href="https://www.hacktron.ai/blog/supapwn" target="_blank">SupaPwn: Hacking Our Way into Lovable's Office and Helping Secure Supabase</a> - A nice foil to the Anthropic PDF. Here is a model/tool with some very talented hackers doing some legitimate hacking.</li>
<li><a href="https://whiteknightlabs.com/2025/11/11/understanding-cloud-persistence-how-attackers-maintain-access-using-google-cloud-functions/" target="_blank">Understanding Cloud Persistence: How Attackers Maintain Access Using Google Cloud Functions</a> - The major cloud providers have so many different services there are lots of ways to maintain access. This one is using Google Cloud Functions to recreate a backdoor account every time it's deleted.</li>
<li><a href="https://pberba.github.io/security/2025/11/11/macos-infection-vector-applescript-bypass-gatekeeper/" target="_blank">MacOS Infection Vector: Using AppleScripts to bypass Gatekeeper</a> - A rare post on macOS initial access.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://hex-rays.com/blog/introducing-hcli" target="_blank">Introducing HCLI: The Modern Command-Line Interface for IDA</a> - IDA pro gets a new terminal interface. Feels like the first step towards AI-assisted IDA Pro.</li>
<li><a href="https://github.com/ricardojoserf/SAMDump" target="_blank">SAMDump</a> - Extract SAM and SYSTEM using Volume Shadow Copy (VSS) API. With multiple exfiltration options and XOR obfuscation. For details see <a href="https://ricardojoserf.github.io/samdump/" target="_blank">SAMDump - Stealthy SAM Dumping Using VSS and NTAPIs</a>.</li>
<li><a href="https://github.com/AppOmni-Labs/heisenberg-ssc-health-check?utm_source=tldrsec.com&amp;utm_medium=referral&amp;utm_campaign=tl-dr-sec-305-ai-sast-awesome-annual-security-reports-block-risky-dependencies" target="_blank">heisenberg-ssc-health-check</a> - Analyzes software dependencies across GitHub repositories to identify security vulnerabilities and health risks in your supply chain.</li>
<li><a href="https://github.com/keowu/Ryujin" target="_blank">Ryujin</a> - Ryūjin Protector - Is a Intel Arch - BIN2BIN - PE Obfuscation/Protection/DRM tool.</li>
<li><a href="https://github.com/preludeorg/Regstoration" target="_blank">Regstoration</a> - A rust proof of concept to demonstrate registry overwriting via RegRestoreKey using the Offline Registry Library. For more information see: <a href="https://www.preludesecurity.com/blog/rehabilitating-registry-tradecraft-with-regrestorekey" target="_blank">Rehabilitating Registry Tradecraft with RegRestoreKey</a>.</li>
<li><a href="https://github.com/leftp/RegPersist" target="_blank">RegPersist</a> - a BOF implementation of various registry persistence methods.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/solst-ice/itoa" target="_blank">itoa</a> - Converts an image to ASCII art.</li>
<li><a href="https://github.com/karlvbiron/MAD-CAT" target="_blank">MAD-CAT</a> - MAD-CAT (Meow Attack Data Corruption Automation Tool) is a comprehensive security tool designed to simulate data corruption attacks against multiple database systems. The tool supports both single-target attacks and bulk CSV-based attack campaigns, with support for both credentialed and non-credentialed attack scenarios.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 490 (+0)</p>
<p>Blogs monitored: 436 (+1)</p>
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
