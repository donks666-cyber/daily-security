Title: Last Week in Security (LWiS) - 2025-09-29
Date: 2025-09-29 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-09-29
Author: Erik
Summary: OmniProx (<a href="https://x.com/ZephrFish" target="_blank">@ZephrFish</a>), Phantom Chrome Extensions (<a href="https://x.com/Synacktiv" target="_blank">Riadh Bouchahoua (@Synacktiv)</a>), FIDO phishing (<a href="https://x.com/dennis_kniep" target="_blank">@dennis_kniep</a>), VMWare Tools LPE (<a href="https://x.com/0xThiebaut" target="_blank">@0xThiebaut</a>), MSI lateral movement (<a href="https://x.com/werdhaihai" target="_blank">@werdhaihai</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-09-22 to 2025-09-29.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.secretservice.gov/newsroom/releases/2025/09/us-secret-service-dismantles-imminent-telecommunications-threat-new-york" target="_blank">U.S. Secret Service dismantles imminent telecommunications threat in New York tristate area</a> - A "nation-state threat actor" set up, "more than 300 co-located SIM servers and 100,000 SIM cards across multiple sites." The Secret Service claims this was to disrupt the United Nations general assembly happening in New York City. However, "within 35 miles" puts them <a href="https://www.mapdevelopers.com/draw-circle-tool.php?circles=%5B%5B56326.9%2C40.7505339%2C-73.9676469%2C%22%23AAAAAA%22%2C%22%23000000%22%2C0.4%5D%5D" target="_blank">really far away</a> from the UN headquarters in NYC. It's probably just a standard SMS spam farm.</li>
<li><a href="https://www.linkedin.com/posts/brentmuir_gtig-vulnerabilities-gti-activity-7376823949587906561-GSM3/" target="_blank">[LinkedIn] In 2024, we observed a Time-to-exploit of -1</a> - A paywalled report from Google Threat Intelligence shows that in 2024 vulnerabilities are being exploited before they are publicly known more often than after disclosure. Since the report is for customers only, it's not possible to know the methodology or sampling bias for this data unfortunately. Engagement bait?</li>
<li><a href="https://aff-wg.org/2025/09/26/analysis-of-a-ransomware-breach/" target="_blank">Analysis of a Ransomware Breach</a> - Mudge reflects on Kerberosting, the security conversation, and Senator Wyden's letter to the FTC (covered last week). If Microsoft had decided that Active Directory privilege escalation was a core issue in 2011, what would the cybersecurity industry look like today?</li>
<li><a href="https://www.huntress.com/cybersecurity-education/cybersecurity-awareness/capture-the-flag" target="_blank">Join the Huntress Annual Capture the Flag</a> - "Every October for Cybersecurity Awareness Month, thousands of defenders join our month-long Capture the Flag competition. Whether you’re new to cybersecurity or a seasoned pro, you’ll face daily puzzles and real-world attack simulations that sharpen your skills and keep you on your toes."</li>
<li><a href="https://flare-on.com/" target="_blank">FlareOnOS v12.2</a> - "The Flare-On Challenge is the <a href="https://cloud.google.com/security/flare?hl=en" target="_blank">FLARE</a> team's annual Capture-the-Flag (CTF) contest. It is a single-player series of Reverse Engineering puzzles that runs for every fall."</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.watchtowr.com/is-this-bad-this-feels-bad-goanywhere-cve-2025-10035/" target="_blank">Is This Bad? This Feels Bad. (Fortra GoAnywhere CVE-2025-10035)</a> - Spoiler: <a href="https://labs.watchtowr.com/it-is-bad-exploitation-of-fortra-goanywhere-mft-cve-2025-10035-part-2/" target="_blank">It Is Bad (Part 2)</a>.</li>
<li><a href="https://www.synacktiv.com/en/publications/the-phantom-extension-backdooring-chrome-through-uncharted-pathways" target="_blank">The Phantom Extension: Backdooring Chrome Through Uncharted Pathways</a> - Browser access may be the only thing you need to accomplish operational objectives, and therefore getting a Chrome extension installed without tripping defenses is paramount. This post shows exactly that as well as three techniques to bypass enhanced developer mode security. The Synacktiv private Chrome C2 "Cheef" looks pretty sweet as well.</li>
<li><a href="https://denniskniep.github.io/posts/14-fido-cross-device-phishing/" target="_blank">FIDO Cross Device Phishing</a> - "This works ONLY if attacker has placed device(s) in BLE range (~150m) near the victim(s)." Physical Fast IDentity Online (FIDO) tokens, are still the gold standard of authentication.</li>
<li><a href="https://blog.nviso.eu/2025/09/29/you-name-it-vmware-elevates-it-cve-2025-41244/" target="_blank">You name it, VMware elevates it (CVE-2025-41244)</a> - A trivial local privilege escalation for Linux guests running VMware Tools.</li>
<li><a href="https://blog.quarkslab.com/exploiting-lenovo-driver-cve-2025-8061.html" target="_blank">BYOVD to the next level (part 1) — exploiting a vulnerable driver (CVE-2025-8061)</a> - A Windows local privilege escalation using a Lenovo driver (<cite>LnvMSRIO.sys</cite>, patched 2025-09-09). Also note that Hypervisor-Enforced Code Integrity (HVCI) was disabled for this exploit.</li>
<li><a href="https://specterops.io/blog/2025/09/29/dcom-again-installing-trouble-lateral-movement-bof/" target="_blank">DCOM Again: Installing Trouble</a> - Use the Windows Installer Custom Action server to install a driver remotely for lateral movement. I think it's funny that the Microsoft Installer internal name is Darwin, the same name Apple uses for the core Unix-like operating system that power macOS, iOS, watchOS, etc. <a href="https://www.xkcd.com/910/" target="_blank">Naming things is hard</a>.</li>
<li><a href="https://www.x41-dsec.de/security/research/news/2025/09/25/mouse-entropy/" target="_blank">Is Mouse Input Random Enough for Generating Secret Keys?</a> - Short answer: it depends on how many points you collect and if you enforce a minimum travel distance between point collection, but it's probably good enough to be a source of randomness for generating a secure cryptographic key.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Antonlovesdnb/ConstructingDefenseLab" target="_blank">ConstructingDefenseLab</a> - <a href="https://ludus.cloud" target="_blank">Ludus</a> range for the Constructing Defense Lab.</li>
<li><a href="https://github.com/werdhaihai/msi_lateral_mv" target="_blank">msi_lateral_mv</a> - Lateral Movement Bof with MSI ODBC Driver Install.</li>
<li><a href="https://github.com/hackerhouse-opensource/SetupHijack" target="_blank">SetupHijack</a> - SetupHijack is a security research tool that exploits race conditions and insecure file handling in Windows applications installer and update processes.</li>
<li><a href="https://www.synacktiv.com/en/publications/appledbrs-a-research-support-tool-for-apple-platforms" target="_blank">Appledb_rs, a Research Support Tool for Apple Platforms</a> - This is the <a href="https://winbindex.m417z.com/" target="_blank">Windows Binaries Index</a> for macOS/iOS. Code is: <a href="https://github.com/synacktiv/appledb_rs" target="_blank">appledb_rs</a>.</li>
<li><a href="https://blog.zsec.uk/omniprox/" target="_blank">OmniProx: Multi-Cloud IP Rotation Made Simple</a> - AWS changed their terms of service which technically made using AWS for IP rotation (a la <a href="https://github.com/ustayready/fireprox" target="_blank">fireprox</a>) a violation of the terms (but <a href="https://www.eff.org/deeplinks/2010/07/court-violating-terms-service-not-crime-bypassing" target="_blank">not</a> <a href="https://www.findlaw.com/legalblogs/ninth-circuit/violation-of-a-websites-terms-of-service-is-not-criminal/" target="_blank">criminal</a>). Code is: <a href="https://github.com/ZephrFish/OmniProx" target="_blank">OmniProx</a>.</li>
<li><a href="https://github.com/LeighlinRamsay/GunnerC2" target="_blank">GunnerC2</a> - A modern, operator-friendly Command-and-Control framework for authorized red-team operations and research.</li>
<li><a href="https://adaptix-framework.gitbook.io/adaptix-framework/changelog-and-updates/v0.8-greater-than-v0.9" target="_blank">AdaptixC2 v0.9</a> - Another update to the great open source C2.</li>
<li><a href="https://github.com/Octoberfest7/ThreadCPUAssignment_POC" target="_blank">ThreadCPUAssignment_POC</a> - A small experiment on assigning a processes threads a specific CPU and then blocking it with a high priority thread.</li>
<li><a href="https://github.com/M1ndo/WerDump" target="_blank">WerDump</a> - A Beacon Object File (BOF) for Havoc/CS to Bypass PPL and Dump Lsass.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.youtube.com/watch?v=UVD0fbiNbnM" target="_blank">[YouTube] Is the iPhone 17 the First Un-Breakable Phone?</a> - A good video breakdown of the Memory Tagging Extension released in iOS 26 for the new iPhone 17 series (covered two weeks ago).</li>
<li><a href="https://www.youtube.com/watch?v=1bBVQaAD_jI" target="_blank">[YouTube] I build a machine that turns you into a criminal</a> - Interesting technical art piece.</li>
<li><a href="https://github.com/vulncheck-oss/0day.today.archive" target="_blank">0day.today.archive</a> - An archive of 0day.today exploits.</li>
<li><a href="https://github.com/EasyTier/EasyTier" target="_blank">EasyTier</a> - A simple, decentralized mesh VPN with WireGuard support.</li>
<li><a href="https://github.com/styx-emulator/styx-emulator" target="_blank">styx-emulator</a> - Multi-architecture emulation for the modern era.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 459 (+1)</p>
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
