Title: Last Week in Security (LWiS) - 2025-10-20
Date: 2025-10-20 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-10-20
Author: Erik
Summary: WhatchGuard RCE (<a href="https://x.com/_McCaulay" target="_blank">@_mccaulay</a>), BadSuccessor BOF (<a href="https://x.com/_logangoins" target="_blank">@_logangoins</a>), ClubWPT hack (<a href="https://x.com/samwcyo" target="_blank">@samwcyo</a>), MDE cloud vulns (<a href="https://x.com/p0w1_" target="_blank">@p0w1_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-10-06 to 2025-10-20.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://www.alteredsecurity.com/online-labs?utm_source=badsectorlabs&amp;utm_medium=email&amp;utm_campaign=diwali_offer" style="color: #3bd267;" target="_blank">Sharpen your Red Team skills with 20% OFF</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p style="text-indent: 0;">Start your Red Team training with Altered Security! We offer affordable Red Team courses with enterprise-like hands-on labs and lifetime access to course materials.</p>
<p style="text-indent: 0;">Each course comes with an industry-recognized certification. We are the creators of the Certified Red Team Professional (CRTP), CRTE, CARTP and more. Join more than 50,000 professionals from 130+ countries.</p>
<p style="text-indent: 0;">Enjoy 20% OFF on all courses and instructor-led bootcamps to be held in Q1 and Q2 2026. No coupon code required. Discount ends on November 1, 2025. <strong><a href="https://www.alteredsecurity.com/online-labs?utm_source=badsectorlabs&amp;utm_medium=email&amp;utm_campaign=diwali_offer" style="color: #3bd267;" target="_blank">Sign up now!</a></strong></p>
</aside><ul>
<li><a href="https://blog.ring.com/about-ring/ring-expands-community-requests-to-additional-community-safety-partners/" target="_blank">Ring Expands Community Requests to Additional Community Safety Partners</a> - The Amazon owned home security company is now integrating it's cameras with Flock Safety's "Nova" platform to enable <span class="strike">dystopian levels of surveillance</span>, sorry, a "public safety technology ecosystem." Security cameras are great, but not when they are used for mass surveillance. Norfolk Virginia has run <a href="https://www.documentcloud.org/documents/26101033-norfolk_flock/" target="_blank">over 200,000 searches in Flock Safety's system with no warrants or oversight</a>. Run your own closed systems with <a href="https://ui.com/us/en/physical-security" target="_blank">UniFi</a> or <a href="https://frigate.video/" target="_blank">Frigate</a>.</li>
<li><a href="https://mp.weixin.qq.com/s/XPjT0BVOJPJxSmASW0tXTA" target="_blank">[QQ] Technical Analysis Report on the Cyber Attack on the National Time Service Center by the U.S. National Security Agency</a> - "Throughout this incident, the NSA demonstrated world-leading capabilities in tactical concepts, operational techniques, encrypted communications, and anti-virus evasion." None of the "evidence" (screenshots of encrypted traffic or disassembled code) point directly to the NSA, and the smoking gun seems to be that this intrusion used an implant with modules and encryption, similar to the alleged leaked NSA tooling from 2016, but also many other advanced implants.</li>
<li><a href="https://security.apple.com/blog/apple-security-bounty-evolved" target="_blank">A major evolution of Apple Security Bounty, with the industry's top awards for the most advanced research</a> - Apple is doubling the rewards for their bug bounty program. Hopefully this gets more exploit chains to Apple, and fewer to morally questionable governments.</li>
<li><a href="https://endof10.org/" target="_blank">Support for Windows 10 ended on October 14, 2025.</a> - Time to explore Linux! Ironic that <a href="https://weee-forum.org/iewd-about/" target="_blank">International E-Waste Day</a> was also October 14th.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.watchtowr.com/yikes-watchguard-fireware-os-ikev2-out-of-bounds-write-cve-2025-9242/" target="_blank">yIKEs (WatchGuard Fireware OS IKEv2 Out-of-Bounds Write CVE-2025-9242)</a> - At what point should a company start over if their enterprise security products lack security protections from 25 years ago?</li>
<li><a href="https://specterops.io/blog/2025/10/20/the-near-return-of-the-king-account-takeover-using-the-badsuccessor-technique/" target="_blank">The (Near) Return of the King: Account Takeover Using the BadSuccessor Technique</a> - Props to Logan for emphasizing this new technique, creating a BOF for it, and of course using <a href="https://ludus.cloud" target="_blank">Ludus</a> to test and demonstrate it.</li>
<li><a href="https://samcurry.net/hacking-clubwpt-gold" target="_blank">Hacking the World Poker Tour: Inside ClubWPT Gold’s Back Office</a> - Love a good "huh what is that URL?" to "full access to all customer data" journey.</li>
<li><a href="https://www.synacktiv.com/en/publications/linkpro-ebpf-rootkit-analysis" target="_blank">LinkPro: Ebpf Rootkit Analysis</a> - Linux rootkits from threat actors are getting more advanced, but this one still uses LD_PRELOAD. Great analysis and diagrams of the complicated traffic flows by Théo.</li>
<li><a href="https://aff-wg.org/2025/10/13/weeding-the-tradecraft-garden/" target="_blank">Weeding the Tradecraft Garden</a> - Mudge is updating and expanding the Tradecraft Garden, which is now BSD licensed. The dynamic function resolution and optimizations along with <cite>mergelib</cite> make your position independent code easier to write. We're starting to see tooling based on the garden released by others!</li>
<li><a href="https://connormcgarr.github.io/windows-pac-arm64/" target="_blank">Exploit Development: Unveiling Windows ARM64 Pointer Authentication (PAC)</a> - Not sure how often Windows ARM64 is seen in the wild, but Connor is always pushing the envelope with his research.</li>
<li><a href="https://labs.infoguard.ch/posts/attacking_edr_part5_vulnerabilities_in_defender_for_endpoint_communication/" target="_blank">Analyzing and Breaking Defender for Endpoint's Cloud Communication</a> - Good insight into how Defender for Endpoint's cloud communication works, but it's going to be difficult to use operationally as getting to a point where you can modify the certificate validation of MsSense.exe probably would have caused some alarms. However, the ability to query the cloud for exclusions is very useful and unpatched.</li>
<li><a href="https://blog.quarkslab.com/exploiting-lenovo-driver-cve-2025-8061_part2.html" target="_blank">BYOVD to the next level (part 2) — rootkit like it's 2025</a> - "See how an attacker can abuse R/W primitives to manually map their own unsigned driver and completely bypass Driver Signature Enforcement (DSE)."</li>
<li><a href="https://medium.com/@dhiraj_mishra/macos-shortcuts-for-initial-access-c43ce7cf0e0c" target="_blank">macOS Shortcuts for Initial Access</a> - Not a lot of initial access techniques for macOS. This one has a lot of clicks, but get code execution.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/sadreck/Butler" target="_blank">Butler</a> - GitHub Actions Oversight.</li>
<li><a href="https://github.com/ofasgard/execute-assembly-pico" target="_blank">execute-assembly-pico</a> - A PICO for Crystal Palace that implements CLR hosting to execute a .NET assembly in memory.</li>
<li><a href="https://github.com/rasta-mouse/Crystal-Kit" target="_blank">Crystal-Kit</a> - This repo is a technical and social experiment to see if replacing Cobalt Strike's evasion primitives (Sleepmask/BeaconGate) with Crystal Palace PIC(O)s is feasible (or even desirable) for advanced evasion scenarios.</li>
<li><a href="https://github.com/rasta-mouse/LibTP" target="_blank">LibTP</a> - Crystal Palace library for proxying Nt API calls via the Threadpool.</li>
<li><a href="https://github.com/logangoins/BadTakeover-BOF" target="_blank">BadTakeover-BOF</a> - Beacon Object File (BOF) for Using the BadSuccessor Technique for Account Takeover.</li>
<li><a href="https://github.com/0xTriboulet/InlineExecuteEx" target="_blank">InlineExecuteEx</a> - A BOF that's a BOF Loader.</li>
<li><a href="https://github.com/andyrobbins/PingOneHound" target="_blank">PingOneHound</a> - Six Degrees of Organization Admin. See <a href="https://specterops.io/blog/2025/10/20/pingone-attack-paths/" target="_blank">PingOne Attack Paths</a> for all the details.</li>
<li><a href="https://github.com/dobin/DetonatorAgent" target="_blank">DetonatorAgent</a> - Detonate malware on VMs and get logs &amp; detection status.</li>
<li><a href="https://github.com/eSentire-Labs/surveyor" target="_blank">surveyor</a> - Advanced Windows kernel analysis and system profiling tool. Provides comprehensive visibility into kernel callbacks, ETW sessions, driver analysis, and system state through both userland APIs and optional kernel driver integration.</li>
<li><a href="https://github.com/ZerkerEOD/krakenhashes" target="_blank">krakenhashes</a> - KrakenHashes is a distributed password cracking system designed for security professionals and red teams.</li>
<li><a href="https://github.com/MatheuZSecurity/Singularity" target="_blank">Singularity</a> - Linux Kernel Rootkit for modern kernels (6x).</li>
<li><a href="https://github.com/moiz-2x/CVE-2025-24990_POC" target="_blank">CVE-2025-24990_POC</a> - Proof of Concept CVE-2025-24990 (Agere Systems's driver).</li>
<li><a href="https://github.com/0xf00sec/Aether" target="_blank">Aether</a> - Self-mutating macOS implant.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/lum8rjack/caddy-c2" target="_blank">caddy-c2</a> - Caddy v2 module to filter requests based on C2 profiles.</li>
<li><a href="https://github.com/vnt-dev/vnt" target="_blank">vnt</a> - A simple and efficient remote networking and intranet penetration tool. Use with <a href="https://github.com/vnt-dev/vnts" target="_blank">vnts</a>.</li>
<li><a href="https://github.com/zh54321/GraphPreConsentExplorer" target="_blank">GraphPreConsentExplorer</a> - A comprehensive list of usable Entra ID first-party clients with pre-consented Microsoft Graph scopes, in a simple YAML-file explorable with a simple HTML GUI.</li>
<li><a href="https://satcom.sysnet.ucsd.edu/docs/dontlookup_ccs25_fullpaper.pdf" target="_blank">[PDF] Don’t Look Up: There Are Sensitive Internal Links in the Clear on GEO Satellites</a> - "We observed unencrypted cellular backhaul traffic from several providers including cleartext call and text contents, job scheduling and industrial control systems for utility infrastructure, military asset tracking, inventory management for global retail stores, and in-flight wifi."</li>
<li><a href="https://kroon.email/site/en/posts/wireguard-wstunnel/" target="_blank">Tunneling WireGuard over HTTPS using Wstunnel</a> - I could see this being useful for bypassing firewalls or deep packet inspection.</li>
<li><a href="https://github.com/encodeous/nylon" target="_blank">nylon</a> - Dynamic Routing on WireGuard for everyone.</li>
<li><a href="https://www.youtube.com/watch?v=hksVvXONrIo" target="_blank">[YouTube] It's Not Just You - The iOS Keyboard is Broken</a> - Something strange is going on with input/animation vs output. Another theory is the swipe to type feature, but disabling that also doesn't fix the issue.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 462 (+3)</p>
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
