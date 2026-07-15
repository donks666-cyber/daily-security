Title: Last Week in Security (LWiS) - 2023-10-09
Date: 2023-10-09 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-10-09
Author: Erik
Summary: Looney Tunables Linux LPE (<a href="https://twitter.com/QUALYS" target="_blank">@qualys</a>), Impending curl issue (<a href="https://twitter.com/bagder" target="_blank">@bagder</a>), macOS gatekeeper bypass 0day (<a href="https://twitter.com/_xpn_" target="_blank">@_xpn_</a>), firewall unauth RCE (<a href="https://twitter.com/watchtowrcyber" target="_blank">@watchtowrcyber</a>), sccmhunter update (<a href="https://twitter.com/garrfoster" target="_blank">@garrfoster</a>), loaders (<a href="https://twitter.com/mcbroom_evan" target="_blank">@mcbroom_evan</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-10-02 to 2023-10-09.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.coresecurity.com/core-labs/articles/impacket-we-love-playing-tickets" target="_blank">Impacket Updates: We Love Playing With Tickets</a> - Impacket is starting to crank out some kerberos improvements. You can create a <a href="https://unit42.paloaltonetworks.com/next-gen-kerberos-attacks/" target="_blank">Sapphire Ticket</a> a bit easier now with Impacket without having to use a fork.</li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2023/10/03/defending-new-vectors-threat-actors-attempt-sql-server-to-cloud-lateral-movement/" target="_blank">Defending new vectors: Threat actors attempt SQL Server to cloud lateral movement</a> - The instance metadata service (IMDS) was the target. The cloud metadata service has been a popular target for AWS attacks in the past, and Azure is no different now.</li>
<li><a href="https://labs.watchtowr.com/exim-0days-90s-vulns-in-90s-software/" target="_blank">90s Vulns In 90s Software (Exim) - Is the Sky Falling?</a> - "So, our advice is the usual - patch when you can, once patches are available (Exim have stated they will release patches at 12:00 UTC today, Monday 2nd October). But in the meantime, don't panic - this one is more of a damp squib than a world-ending catastrophe." Unless you have a <a href="https://www.sophos.com/en-us/security-advisories/sophos-sa-20231005-exim-vuln" target="_blank">Sophos Firewall</a>, in which case you should patch ASAP.</li>
<li><a href="https://security.googleblog.com/2023/10/expanding-our-exploit-reward-program-to.html" target="_blank">Expanding our exploit reward program to Chrome and Cloud</a> - It's neat they pay for n-day PoCs not just 0days.</li>
<li><a href="https://github.com/curl/curl/discussions/12026" target="_blank">Severity HIGH security problem to be announced with curl 8.4.0 on Oct 11</a> - This is drectly from the curl author, unlike other reported "high severity" curl issues in the past that turned out to be nothing.</li>
<li><a href="https://www.reuters.com/technology/russia-plans-try-block-vpn-services-2024-senator-2023-10-03/" target="_blank">Russia plans to try to block VPN services in 2024</a> - Good luck!</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.qualys.com/2023/10/03/cve-2023-4911/looney-tunables-local-privilege-escalation-glibc-ld-so.txt" target="_blank">Looney Tunables: Local Privilege Escalation in the glibc's ld.so (CVE-2023-4911)</a> - Is this the <a href="https://dirtycow.ninja/" target="_blank">Dirty COW</a> of 2023? Perhaps not quite as ubiquitous as it relies on a range of glibc versions (glibc 2.34+). Props to Qualys for keeping the old school phrack-esqe disclosures alive. <a href="https://github.com/RickdeJager/CVE-2023-4911" target="_blank">PoC 1</a>. <a href="https://github.com/leesh3288/CVE-2023-4911" target="_blank">PoC 2</a>. <a href="https://haxx.in/files/gnu-acme.py" target="_blank">[Direct Download] PoC 3</a>. <a href="https://github.com/Green-Avocado/CVE-2023-4911" target="_blank">PoC 4</a>.</li>
<li><a href="https://blog.xpnsec.com/dirtynib/" target="_blank">MacOS "DirtyNIB" Vulnerability</a> - It's possible to hijack the entitlements of Apple apps by swapping out the interface (NIB) file. This is currently unpatched, even on macOS 14.0. Weaponize this for camera/mic/keychain/file access once you get code execution. Or maybe even bundle it in with your dropper.</li>
<li><a href="https://theevilbit.github.io/posts/launch_constraints_deep_dive/" target="_blank">Launch and Environment Constraints Deep Dive</a>. A great companion to the previous post that details what Launch and Environment Constraints are and what kind of bugs they hamper.</li>
<li><a href="https://outflank.nl/blog/2023/10/05/solving-the-unhooking-problem/" target="_blank">Solving The “Unhooking” Problem</a> - Unhooking gets complicated when the user can run arbitrary code (BOF/C#) that may load libraries without the protection of the C2 agent. Outflank presents their solution to this issue - visibility, automation, and on-demand unhooking.</li>
<li><a href="https://securityintelligence.com/x-force/reflective-call-stack-detections-evasions/" target="_blank">Reflective call stack detections and evasions</a> - An updated <a href="https://github.com/boku7/BokuLoader" target="_blank">BokuLoader</a> has some new methods to avoid call stack spoofing detection.</li>
<li><a href="https://dev.to/living_syn/sliver-and-cursed-chrome-for-post-exploitation-4gnk" target="_blank">Sliver and Cursed Chrome for Post Exploitation</a> - With sensitive information moving to SaaS and other browser based apps, being able to operate as a compromised user in the context of their browser is essential for modern red teams.</li>
<li><a href="https://labs.watchtowr.com/yet-more-unauth-remote-command-execution-vulns-in-firewalls-sangfor-edition/" target="_blank">Yet More Unauth Remote Command Execution Vulns in Firewalls - Sangfor Edition</a>. I will always be impressed with unauth RCE on a firewall. 🤦</li>
<li><a href="https://www.synacktiv.com/en/publications/behind-the-shield-unmasking-scudos-defenses" target="_blank">Behind the Shield: Unmasking Scudo's Defenses</a> - Scudo is LLVM's hardened allocator. This post is a dense exploration of how exploitation of scudo may be possible.</li>
</ul>
<p><a href="https://www.elttam.com/blog/stsafe-a110/#content" target="_blank">Exploring the STSAFE-A110 Analysing I2C communications between host and the secure element</a> - Some physical device hacking with a logic analyzer to read I2C of a secure element.</p>
<ul>
<li><a href="https://rastamouse.me/cobalt-strike-aggressor-callbacks/" target="_blank">Cobalt Strike Aggressor Callbacks</a> - Shows how to use the new callbacks feature of Cobalt Strike 4.9. Much better than setting global flags and parsing all beacon output in a timer function which is what we had to do before.</li>
<li><a href="https://skylightcyber.com/2023/10/04/trends-from-the-trenches-social-engineering/" target="_blank">Trends From the Trenches: Social Engineering</a> - Some really solid examples in this post. I've used similar pretexts to great effect.</li>
<li><a href="https://gist.github.com/EvanMcBroom/0f45c1bdb55b4d5f43c7bcf336e0663e" target="_blank">Perfect Loader Implementations</a> - Some good Linux and Windows loader work, see <a href="https://github.com/EvanMcBroom/fuse-loader" target="_blank">fuse-loader</a> and <a href="https://github.com/EvanMcBroom/perfect-loader" target="_blank">perfect-loader</a> for PoCs. These are great raw material for custom C2s.</li>
<li><a href="https://github.blog/2023-10-09-coordinated-disclosure-1-click-rce-on-gnome-cve-2023-43641/" target="_blank">Coordinated Disclosure: 1-Click RCE on GNOME (CVE-2023-43641)</a> - Lots of protections bypassed to get RCE - excited for the follow up post.</li>
<li><a href="https://certitude.consulting/blog/en/using-cloudflare-to-bypass-cloudflare/" target="_blank">Using Cloudflare to bypass Cloudflare</a> - Defaults can be dangerous. Be sure to validate the host headers!</li>
<li><a href="https://binarly.io/posts/Binarly_REsearch_Uncovers_Major_Vulnerabilities_in_Supermicro_BMCs/index.html" target="_blank">Binarly REsearch Uncovers Major Vulnerabilities in Supermicro BMCs</a> - Authenticated command injection and a slew of XSS. Theoretically you could chain these to be unauth remote RCE, but you'd need a click from a logged in admin.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/lefayjey/linWinPwn" target="_blank">linWinPwn</a> - Bash script that automates a number of Active Directory Enumeration and Vulnerability checks. Will be interesting if they keep up with this project. Interesting new project since it's using the new <a href="https://github.com/Pennyw0rth/NetExec" target="_blank">NetExec</a> . Will other tools do the same?</li>
<li><a href="https://github.com/icyguider/LatLoader" target="_blank">LatLoader</a> - PoC module to demonstrate automated lateral movement with the Havoc C2 framework.</li>
<li><a href="https://github.com/garrettfoster13/sccmhunter/releases/tag/v0.0.2" target="_blank">sccmhunter v.0.0.2 - Updated Admin Module</a> - SCCM is the gift that keeps on giving. This is a new easy way to execute commands on managed machines (Administration Service API).</li>
<li><a href="https://github.com/pentagridsec/archive_pwn" target="_blank">archive_pwn</a> - A Python-based tool to create zip, tar and cpio archives to exploit common archive library issues and developer mistakes. <a href="https://www.pentagrid.ch/de/blog/archive-pwn-tool-release/" target="_blank">Blog Post</a>.</li>
<li><a href="https://github.com/Cr4sh/SmmBackdoorNg" target="_blank">SmmBackdoorNg</a> - Updated version of System Management Mode backdoor for UEFI based platforms: old dog, new tricks.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://blog.whiteflag.io/blog/browser-cache-smuggling/" target="_blank">Browser cache smuggling</a> - Interesting payload delivery technique.</li>
<li><a href="https://redteamrecipe.com/Registry-Attack-Vectors/" target="_blank">Registry Attack Vectors(RTC0018)</a> - A big list of interesting reg keys.</li>
<li><a href="https://www.chudamax.com/posts/kerberos-102-overview/" target="_blank">Kerberos 102 - Overview</a> Three part blog series on kerberos, delegation, and cross-realm. You can never read enough about kerberos.</li>
<li><a href="https://github.com/codereversing/ted_api" target="_blank">ted_api</a> - TED is a limited general purpose reverse engineering API, and hybrid debugger, that allows for inspection and modification of a program's inner workings. TED carries out its functionality by being injected into a target process and starting a gRPC server, which clients can then connect to.</li>
<li><a href="https://github.com/sshlog/agent" target="_blank">agent</a> - SSH Session Monitoring Daemon.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 358 (+2)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
