Title: Last Week in Security (LWiS) - 2022-06-27
Date: 2022-06-27 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-06-27
Author: Erik
Summary: Pre-auth RCE on Oracle Cloud (<a href="https://twitter.com/peterjson" target="_blank">@peterjson</a> + <a href="https://twitter.com/testanull" target="_blank">@testanull</a>), Global Jacuzzi hack (<a href="https://twitter.com/XeEaton" target="_blank">@XeEaton</a>), goodfaith scoping (<a href="https://twitter.com/ryanelkins" target="_blank">@ryanelkins</a>), Tailscale SSH (<a href="https://twitter.com/MayaKaczorowski" target="_blank">@MayaKaczorowski</a>), WerFault lsass dumper (<a href="https://twitter.com/asaf_gilboa" target="_blank">@asaf_gilboa</a> + <a href="https://twitter.com/s4ntiago_p" target="_blank">@s4ntiago_p</a>), ADFSRelay (<a href="https://twitter.com/praetorianlabs" target="_blank">@praetorianlabs</a>), modern C2 (<a href="https://twitter.com/preemptdev" target="_blank">@preemptdev</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-06-20 to 2022-06-27.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.cobaltstrike.com/blog/arsenal-kit-update-thread-stack-spoofing/" target="_blank">Arsenal Kit Update: Thread Stack Spoofing</a>. A new-ish (~6 months) EDR evasion technique comes to the most popular C2 framework out there.</li>
<li><a href="https://tailscale.com/blog/tailscale-ssh/" target="_blank">Introducing Tailscale SSH</a>. The ability to ssh to servers using Tailscale as an auth provider without changing SSH configs is pretty awesome.</li>
<li><a href="https://blogs.windows.com/windows-insider/2022/06/22/announcing-windows-11-insider-preview-build-25145/" target="_blank">The legacy Local Administrator Password Solution product (aka “LAPS”) is now a native part of Windows and includes many new features:</a>. Microsoft is taking real steps (finally) to lock down Windows (a little).</li>
<li><a href="https://mega-awry.io/pdf/mega-malleable-encryption-goes-awry.pdf" target="_blank">[PDF] MEGA: Malleable Encryption Goes Awry</a>. If you were counting on the mega.io encryption to protect your files, you're in for a bad time.</li>
<li><a href="https://www.splunk.com/en_us/product-security/announcements/svd-2022-0608.html" target="_blank">Splunk Enterprise deployment servers allow client publishing of forwarder bundles</a>. Imagine you land a phish on a workstation managed by the same Splunk forwarder as the Domain Controller and you can pull off a local privilege escalation. You can use Splunk to get a SYSTEM shell on the DC from the workstation. Pretty gnarly.</li>
<li><a href="https://www.youtube.com/watch?v=icBD5PiyoyI" target="_blank">Hacking a Samsung Galaxy for $6,000,000 in Bitcoin!?</a>. This video plays up the drama of the situation, but the hack is legit.</li>
<li><a href="https://blog.cloudflare.com/cloudflare-outage-on-june-21-2022/" target="_blank">Cloudflare outage on June 21, 2022</a>. Yes, cloudflare went down, but it had the root cause analysis published in six hours. In my view, an excellent PR move.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://mgeeky.tech/warcon-2022-modern-initial-access-and-evasion-tactics/" target="_blank">WarCon 2022 - Modern Initial Access and Evasion Tactics</a>. If you only read one post from this week as a red team, read this one and review the deck. Great modern red team tactics and techniques all in one spot.</li>
<li><a href="https://eaton-works.com/2022/06/20/hacking-into-the-worldwide-jacuzzi-smarttub-network/" target="_blank">Hacking into the worldwide Jacuzzi SmartTub network</a>. This is in the running for the best LWiS headline of 2022. Some impressively bad design (think my first web ctf challenge) was used to "secure" the global Jacuzzi network.</li>
<li><a href="https://labs.detectify.com/2022/06/21/hack-with-goodfaith-to-automate-and-scale-ethical-hacking/" target="_blank">Hack with 'goodfaith' - A tool to automate and scale good faith hacking</a>. The tough part about hacking is to stay in scope. Hacker and security researcher Ryan Elkins (<a href="https://twitter.com/ryanelkins" target="_blank">@ryanelkins</a>) revealed a new tool that is intended to help hackers and security researchers avoid generating traffic against out-of-scope targets.</li>
<li><a href="https://xorl.wordpress.com/2022/06/22/the-forgotten-suaveeyeful-freebsd-software-implant-of-the-equation-group/" target="_blank">The forgotten SUAVEEYEFUL FreeBSD software implant of the EQUATION GROUP</a>. Even the Equation Group used port 4444 at one point.</li>
<li><a href="https://peterjson.medium.com/miracle-one-vulnerability-to-rule-them-all-c3aed9edeea2" target="_blank">Miracle - One Vulnerability To Rule Them All</a>. "We successfully achieved pre-auth RCE on login.oracle.com" is a pretty crazy sentence to read. Even more crazy, they say they <a href="https://twitter.com/peterjson/status/1500755202382565377" target="_blank">have another pre-auth RCE</a>. If you have any interest in Java bugs, deserialization attacks, or massive pre-auth RCE on a cloud provider, don't skip this one.</li>
<li><a href="https://www.praetorian.com/blog/relaying-to-adfs-attacks/" target="_blank">Relaying to ADFS Attacks</a>. Relay that NTLM to the cloud! Tool <a href="https://github.com/praetorian-inc/ADFSRelay" target="_blank">here</a>.</li>
<li><a href="https://pre.empt.dev/posts/maelstrom-the-implant/" target="_blank">Maelstrom: Writing a C2 Implant</a>. These posts from pre.empt.dev have been a great resource for anyone starting to develop "modern" C2.</li>
<li><a href="https://blog.syss.com/posts/hacking-usb-flash-drives-part-2/" target="_blank">Hacking Some More Secure USB Flash Drives (Part II)</a>. This hardware hack has some extra fun, like emulating the "installer" of the USB drive to deliver malware.</li>
<li><a href="https://blog.bitsadmin.com/blog/dealing-with-large-bloodhound-datasets" target="_blank">Dealing with large BloodHound datasets</a>. This is a great overview of Bloodhound, collectors, and processors once the data is in the DB.</li>
<li><a href="https://mrd0x.com/attacking-with-webview2-applications/" target="_blank">Attacking With WebView2 Applications</a>. If you open a site in a "WebView2" application, you can inject all kinds of goodies into it. <a href="https://github.com/mrd0x/WebView2-Cookie-Stealer" target="_blank">WebView2-Cookie-Stealer</a> has the source.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/helpsystems/nanodump/commit/578116faea3d278d53d70ea932e2bbfe42569507" target="_blank">Add WerFault Silent Process Exit: --werfault to nanodump</a>. You can now force WerFault.exe to dump LSASS for you.</li>
<li><a href="https://www.mandiant.com/resources/floss-version-2" target="_blank">FLOSS Version 2.0</a>. "Over the last few months, we've added new functionality and improved the tool's performance. In this blog post we will share exciting new features and improvements including a new string deobfuscation technique, simplified tool usage, and much faster result output."</li>
<li><a href="https://github.com/edoardottt/awesome-hacker-search-engines" target="_blank">awesome-hacker-search-engines</a> -  A list of search engines useful during Penetration testing, vulnerability assessments, red team operations, bug bounty, and more.</li>
<li><a href="https://github.com/tijme/kernel-mii" target="_blank">kernel-mii</a> -  Cobalt Strike (CS) Beacon Object File (BOF) foundation for kernel exploitation using CVE-2021-21551.</li>
<li><a href="https://github.com/emredavut/Chrome-Android-and-Windows-0day-RCE-SBX" target="_blank">Chrome-Android-and-Windows-0day-RCE-SBX</a> -  Chrome Android and (patched) Windows 0day RCE+SBX... from the DPRK (in 2021).</li>
<li><a href="https://github.com/optiv/Mangle" target="_blank">Mangle</a> is a tool that manipulates aspects of compiled executables (.exe or DLL) to avoid detection from EDRs.</li>
<li><a href="https://github.com/0xsp-SRD/callback_injection-Csharp" target="_blank">callback_injection-Csharp</a> -  this repo is to cover the other undocumented or published / in different languages to achieve shellcode injection via windows callback functions.</li>
<li><a href="https://github.com/projectdiscovery/tlsx" target="_blank">tlsx</a> -  Fast and configurable TLS grabber focused on TLS based data collection.</li>
<li><a href="https://github.com/liamg/dismember" target="_blank">dismember</a> -  🔪 Scan memory for secrets and more (linux).</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.damnvulnerabledefi.xyz/" target="_blank">Damn Vulnerable DeFi</a> - The offensive security playground for decentralized finances. Learn up and get those massive bounties. Also check out <a href="https://github.com/Rivaill/CryptoVulhub" target="_blank">CryptoVulhub</a>.</li>
<li><a href="https://github.com/redhuntlabs/httploot" target="_blank">HTTPLoot</a> -  An automated tool which can simultaneously crawl, fill forms, trigger error/debug pages and "loot" secrets out of the client-facing code of sites.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 419 (+2)</p>
<p>Blogs monitored: 314 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
