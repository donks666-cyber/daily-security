Title: Last Week in Security (LWiS) - 2025-03-17
Date: 2025-03-17 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-03-17
Author: Erik
Summary: Evilginx Pro (<a href="https://x.com/mrgretzky" target="_blank">@mrgretzky</a>), Pre-auth RCE in a CMS (<a href="https://x.com/chudyPB" target="_blank">@chudyPB</a>), GOAD ADCS (<a href="https://x.com/M4yFly" target="_blank">@M4yFly</a>), YouTube email disclosure (<a href="https://x.com/brutecat" target="_blank">@brutecat</a>), SAML parser bug (@ulldma.bsky.social/@ulldma@infosec.exchange), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-03-10 to 2025-03-17.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://breakdev.org/evilginx-pro-release/" target="_blank">Evilginx Pro is finally here!</a> - The best credential phishing kit introduces a Pro version. If you're a professional red team, this should be part of your tooling.</li>
<li><a href="https://www.cobaltstrike.com/blog/cobalt-strike-411-shh-beacon-is-sleeping" target="_blank">Cobalt Strike 4.11: Shhhhhh, Beacon is Sleeping....</a> - A novel sleepmask, novel process injection technique, new out-of-the-box obfuscation options for Beacon, asynchronous BOFs, and a DNS over HTTPS (DoH) Beacon. The option to disable auto scrolling in the console window may be the most welcome addition though.</li>
<li><a href="https://blog.cloudflare.com/password-reuse-rampant-half-user-logins-compromised/" target="_blank">Password reuse is rampant: nearly half of observed user logins are compromised</a> - No surprise here. The odds of your universal password being "stuffed" is much higher than a hacker exfiltrating your password manager database which is why we continue to push password managers and multi-factor authentication (hardware tokens are best).</li>
<li><a href="https://www.trendmicro.com/en_us/research/25/c/ai-assisted-fake-github-repositories.html" target="_blank">AI-Assisted Fake GitHub Repositories Fuel SmartLoader and LummaStealer Distribution</a> - Fake GitHub repositories are looking more and more legitimate thanks to "AI." This campaign was using game cheats and cracked software, but are your assessors checking their latest tools/exploits from GitHub for malware (or worse)? Testing in a safe but representative environment (using <a href="https://ludus.cloud/" target="_blank">Ludus</a>) before your customer's production network should be mandatory.</li>
<li><a href="https://www.gsma.com/solutions-and-impact/technologies/networks/gsma_resources/gsma-rcs-universal-profile-3-0-specifications/" target="_blank">GSMA RCS Universal Profile 3.0 specifications</a> - End to end encryption is coming to cross-platform messaging (Android &lt;-&gt; Apple) by default soon. More encryption is always a good thing.</li>
<li><a href="https://www.androidauthority.com/android-linux-terminal-app-available-3532999/?ref=selfh.st" target="_blank">Android's Linux Terminal app is now widely available on Pixels, and here's how to get it</a> - You can now run a Debian virtual machine on your Pixel smartphone as a built in feature of Android.</li>
<li><a href="https://www.rippling.com/blog/lawsuit-alleges-12-billion-unicorn-deel-cultivated-spy-orchestrated-long-running-trade-secret-theft-corporate-espionage-against-competitor" target="_blank">Lawsuit Alleges $12 Billion "Unicorn" Deel Cultivated Spy, Orchestrated Long-Running Trade-Secret Theft &amp; Corporate Espionage Against Competitor</a> - Some serious insider threat allegations. The <a href="https://rippling2.imgix.net/Complaint.pdf" target="_blank">[PDF] complaint</a> is worth a read, bravo to the Rippling General Counsel for signing off on this and the security team for pulling it off (see paragraph #93+).</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://github.blog/security/sign-in-as-anyone-bypassing-saml-sso-authentication-with-parser-differentials/" target="_blank">Sign in as anyone: Bypassing SAML SSO authentication with parser differentials</a> - SAML has always been a difficult protocol. ruby-saml (used in popular Ruby based projects like GitLab) uses two different XML parsers and by exploiting differences in how they process XML an attacker in possession of a valid signed assertion for any user can fabricate assertions and impersonate any other user.</li>
<li><a href="https://blog.quarkslab.com/technical-dive-into-modern-phishing.html" target="_blank">Beyond the Hook: A Technical Deep Dive into Modern Phishing Methodologies</a> - From Evilginx to Modlishka, to browser-in-the-browser, to noVNC, and webRTC, this is probably the most comprehensive post on modern phishing techniques I've seen.</li>
<li><a href="https://certitude.consulting/blog/en/bolt-cms/" target="_blank">CVE-2025-25599: A Cautionary Tale of Insecure Temporary Files</a> - A classic insecure use of temporary files. Time it right, and you can read any file the webserver has access to - think configs with passwords, etc.</li>
<li><a href="https://www.stepsecurity.io/blog/harden-runner-detection-tj-actions-changed-files-action-is-compromised" target="_blank">Harden-Runner detection: tj-actions/changed-files action is compromised</a> - GitHub actions are now part of the software supply chain and are being targeted.</li>
<li><a href="https://mayfly277.github.io/posts/ADCS-part14/" target="_blank">GOAD - part 14 - ADCS 5/7/9/10/11/13/14/15</a> - Get hands on an exploit 8 more Active Directory Certificate Services vulnerabilities. You can set up a vulnerable environment with <a href="https://github.com/Orange-Cyberdefense/GOAD" target="_blank">GOAD</a> or in <a href="https://ludus.cloud/" target="_blank">Ludus</a> with <a href="https://github.com/badsectorlabs/ludus_adcs/" target="_blank">ludus_adcs</a>. <a href="https://mayfly277.github.io/posts/Exchange-part1/" target="_blank">Exchange - Part 1 - no creds</a> just dropped today as well.</li>
<li><a href="https://brutecat.com/articles/youtube-creator-emails" target="_blank">Disclosing YouTube Creator Emails for a $20k Bounty</a> - A creative path to leak the notification email of any YouTube partner with some protobuff tricks and deep knowledge of the Youtube API.</li>
<li><a href="https://labs.watchtowr.com/bypassing-authentication-like-its-the-90s-pre-auth-rce-chain-s-in-kentico-xperience-cms/" target="_blank">Bypassing Authentication Like It’s The ‘90s - Pre-Auth RCE Chain(s) in Kentico Xperience CMS</a> - A content management system built on Microsoft Web Services Enhancement 3.0 has many flaws. Since this is watchTowr, you know the post is going to be both entertaining and ruthless.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/MythicAgents/Xenon" target="_blank">Xenon</a> - A Mythic agent for Windows written in C. Read about the development <a href="https://c0rnbread.com/creating-mythic-c2-agent-part1/" target="_blank">here</a>.</li>
<li><a href="https://github.com/0xRedpoll/ludus_mythic_teamserver" target="_blank">ludus_mythic_teamserver</a> - Ludus role for deploying a Mythic Teamserver onto Linux servers.</li>
<li><a href="https://github.com/alioguzhan/truffleshow" target="_blank">truffleshow</a> - A simple web viewer for TruffleHog JSON output.</li>
<li><a href="https://github.com/3itch/checkm8" target="_blank">checkm8</a> - bypassing intel txt's tboot integrity checks via coreboot shim.</li>
<li><a href="https://github.com/DarkSpaceSecurity/SSH-Stealer" target="_blank">SSH-Stealer</a> - Smart keylogging capability to steal SSH Credentials including password &amp; Private Key.</li>
<li><a href="https://github.com/dagowda/DSViper" target="_blank">DSViper</a> is a powerful tool designed to bypass Windows Defender's security mechanisms, enabling seamless execution of payloads on Windows systems without triggering security alerts. [Debatable - methods seem pretty simple and it's pretty sketchy to download the C++ files from github instead of package them in the repo]</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://aff-wg.org/" target="_blank">The Security Conversation</a> - Mudge, the creator of Cobalt Strike, is back! This non-technical post is about the importance of offensive security research and tooling, even if you don't like it. A more "raw" thread from Mudge is on <a href="https://bsky.app/profile/raphaelmudge.bsky.social/post/3lkfaavjyhs2a" target="_blank">bluesky</a>.</li>
<li><a href="https://github.com/prodaft/cradle/" target="_blank">cradle</a> - CRADLE is a collaborative platform for Cyber Threat Intelligence analysts. It streamlines threat investigations with integrated note-taking, automated data linking, interactive visualizations, and robust access control. Enhance your CTI workflow from analysis to reporting—all in one secure space.</li>
<li><a href="https://github.com/Karmaz95/Snake_Apple" target="_blank">Snake_Apple</a> - Articles and tools related to research in the Apple environment (mainly macOS).</li>
<li><a href="https://github.com/jkramarz/TheTick" target="_blank">TheTick</a> - The Tick is the next evolution in covert access control system implants for simulating adversary-in-the-middle attacks.</li>
<li><a href="https://github.com/macos-fuse-t/scorpi" target="_blank">scorpi</a>  - A Modern Hypervisor (for macOS).</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 445 (+1)</p>
<p>Blogs monitored: 407 (+1)</p>
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
