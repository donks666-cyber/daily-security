Title: Last Week in Security (LWiS) - 2023-05-09
Date: 2023-05-09 20:00
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-05-09
Author: Erik
Summary: Windows DHCPv6 RCE (<a href="https://twitter.com/thezdi" target="_blank">@thezdi</a>), hashcat rule process (<a href="https://infosec.exchange/@JakeWnuk" target="_blank">@JakeWnuk@infosec.exchange</a>), 🐍 FSB implant (<a href="https://twitter.com/NSAcyber" target="_blank">@NSACyber</a>), x64dbg XFG plugin (<a href="https://twitter.com/m417z" target="_blank">@m417z</a>), Freeze.rs (<a href="https://twitter.com/Tyl0us" target="_blank">@Tyl0us</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-05-01 to 2023-05-09.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2023/05/so-long-passwords-thanks-for-all-phish.html" target="_blank">So long passwords, thanks for all the phish</a>. The passwordless future is much like the year of the Linux desktop - long promised, yet to be delivered. Google's adoption of passkeys is a huge step however, and this kind of authentication "raw material" is much more scoped and secure than the name of your dog your mom uses as a password for every online account.</li>
<li><a href="https://news.bloomberglaw.com/ip-law/apple-fails-to-revive-copyright-case-over-iphone-ios-simulator" target="_blank">Apple Fails to Revive Copyright Case Over iPhone iOS Simulator</a>. "The US Court of Appeals for the Eleventh Circuit on Monday ruled that Corellium's CORSEC simulator is protected by copyright law's fair use doctrine, which allows the duplication of copyrighted work under certain circumstances." With this, the 2019 case should finally be fully settled.</li>
<li><a href="https://www.vice.com/en/article/n7enqd/senator-asks-banks-stop-ai-cloned-voices" target="_blank">Senator Asks Big Banks How They're Going to Stop AI Cloned Voices From Breaking Into Accounts</a>. How voice as authentication was ever greenlight will continue to amaze me.</li>
<li><a href="https://docs.modular.com/mojo/" target="_blank">Mojo🔥</a>. Mojo is a new programming language that bridges the gap between research and production by combining the best of Python syntax with systems programming and metaprogramming. With Mojo, you can write portable code that's faster than C and seamlessly inter-op with the Python ecosystem. Mojo is currently in closed beta.</li>
<li><a href="https://www.theregister.com/2023/05/09/intel_oem_private_keys_leaked/?td=keepreading" target="_blank">FYI: Intel BootGuard OEM private keys leak from MSI cyber heist</a>. BootGuard isn't so secure any more. Check the <a href="https://github.com/binarly-io/SupplyChainAttacks/tree/main/MSI" target="_blank">impacted devices</a>.</li>
<li><a href="https://angle.ankura.com/post/102icqx/russian-linked-malware-targets-u-s-critical-infrastructure" target="_blank">Russian-Linked Malware Targets U.S. Critical Infrastructure</a>. "Since being discovered in March 2022, no known disruptive or destructive attacks leveraging PIPEDREAM have been carried out on ICSs in the U.S."</li>
<li><a href="https://www.wired.com/story/solarwinds-hack-public-disclosure/" target="_blank">The DOJ Detected the SolarWinds Hack 6 Months Earlier Than First Disclosed</a>. Sophisticated attacks are hard to put together from the blue side.</li>
<li><a href="https://www.youtube.com/watch?v=XEM5qz__HOU" target="_blank">Palantir AIP | Defense and Military</a>. "Alexa, destroy that enemy tank for me using the best available asset."</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://media.defense.gov/2023/May/09/2003218554/-1/-1/1/JOINT_CSA_HUNTING_RU_INTEL_SNAKE_MALWARE_20230509.PDF" target="_blank">[PDF] Hunting Russian Intelligence “Snake” Malware</a>. A very detailed write up from American intelligence on the FSB's "Snake" Windows implant.</li>
<li><a href="https://blog.stratumsecurity.com/2023/05/04/integration-fails/" target="_blank">Privilege Escalations through Integrations</a>. Some good "modern" web app testing. And by that I mean YOLOing between auth providers that don't do proper session handoff.</li>
<li><a href="https://www.zerodayinitiative.com/blog/2023/5/1/cve-2023-28231-rce-in-the-microsoft-windows-dhcpv6-service" target="_blank">CVE-2023-28231: RCE in the Microsoft Windows DHCPv6 Service</a>. Good news is that DHCP is limited to a broadcast domain?</li>
<li><a href="https://jakewnuk.com/posts/brewing-hash-cracking-rules-w-the-twin-cats/" target="_blank">Brewing Hash Cracking Rules with The Twin Cats</a>. Some great hashcat rule analysis and generation. Lots of good tools linked in the post as well.</li>
<li><a href="https://jub0bs.com/posts/2023-05-05-smorgasbord-of-a-bug-chain/" target="_blank">A smorgasbord of a bug chain: postMessage, JSONP, WAF bypass, DOM-based XSS, CORS, CSRF…</a>. Quite the web app bug chain, which did require user interaction, but is impressive none the less.</li>
<li><a href="https://m417z.com/Leveraging-XFG-to-help-with-reverse-engineering/" target="_blank">Leveraging XFG to help with reverse engineering</a>. If you reverse engineer on Windows with extended flow guard, this x64dbg plugin is a must!</li>
<li><a href="https://labs.nettitude.com/blog/etwhash-he-who-listens-shall-receive/" target="_blank">ETWHash - “He who listens, shall receive”</a>. Extract NetNTLMv2 hashes of incoming authentications via SMB, by consuming ETW events from the Microsoft-Windows-SMBServer provider.</li>
<li><a href="https://blog.scrt.ch/2023/05/01/solr-rce-from-exposed-administration-interface/" target="_blank">Apache Solr 8.3.1 RCE from exposed administration interface</a>. A good write up on exploring a web app to find RCE.</li>
<li><a href="https://posts.specterops.io/exploring-impersonation-through-the-named-pipe-filesystem-driver-15f324dfbaf2" target="_blank">Exploring Impersonation through the Named Pipe Filesystem Driver</a>. This post covers file system drivers, specifically the named pipe driver (npfs.sys), as well as shows a proof of concept for calling NtFsControlFile directly to perform named pipe impersonation instead of calling the Win32 API, ImpersonateNamedPipeClient.</li>
<li><a href="https://www.securesystems.de/blog/building-a-red-team-infrastructure-in-2023/" target="_blank">Building a Red Team Infrastructure in 2023</a>. The phishing setup is interesting - specifically the use of postfix to clean mail headers.</li>
<li><a href="https://www.cyberark.com/resources/threat-research-blog/fantastic-rootkits-and-where-to-find-them-part-2" target="_blank">Fantastic Rootkits and Where to Find Them (Part 2)</a>. Not much is written about rootkits these days, especially for Windows.</li>
<li><a href="https://danrevah.github.io/2023/05/03/CVE-2023-25394-VideoStream-LPE/" target="_blank">CVE-2023-25394 - VideoStream Local Privilege Escalation</a>. A great writeup about finding a privesc in a common 3rd party macOS app. The process is well documented from start to finish.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/garrettfoster13/sccmhunter" target="_blank">sccmhunter</a> is a post-ex tool built to streamline identifying, profiling, and attacking SCCM related assets in an Active Directory domain. The basic function of the tool is to query LDAP with the find module for potential SCCM related assets.</li>
<li><a href="https://github.com/Binject/exec2shell" target="_blank">exec2shell</a> - Extracts TEXT section of a PE, ELF, or Mach-O executable to shellcode.</li>
<li><a href="https://github.com/cyn8/chophound" target="_blank">chophound</a> - Some scripts to support with importing large datasets into BloodHound.</li>
<li><a href="https://github.com/DataDog/hash" target="_blank">HASH</a> - HASH (HTTP Agnostic Software Honeypot).</li>
<li><a href="https://github.com/404tk/cloudtoolkit" target="_blank">cloudtoolkit</a> - Cloud Penetration Testing Toolkit.</li>
<li><a href="https://github.com/xkaneiki/CVE-2023-0386" target="_blank">CVE-2023-0386</a> - Privilege escalation exploit for Ubuntu 22.04.</li>
<li><a href="https://github.com/Wh1t3Rh1n0/PECheck" target="_blank">PECheck</a> - A tool to verify and create PE Checksums for Portable Executable (PE) files.</li>
<li><a href="https://github.com/Kudaes/CustomEntryPoint" target="_blank">CustomEntryPoint</a> - Select any exported function in a dll as the new dll's entry point.</li>
<li><a href="https://github.com/RedTeamPentesting/resocks" target="_blank">resocks</a> - mTLS-Encrypted Back-Connect SOCKS5 Proxy.</li>
<li><a href="https://github.com/TheKevinWang/stealthscraper" target="_blank">stealthscraper</a> - A social media scraper that attempts to be stealthy by simulating a user using gui automation.</li>
<li><a href="https://github.com/optiv/Freeze.rs" target="_blank">Freeze.rs</a> - Freeze.rs is a payload toolkit for bypassing EDRs using suspended processes, direct syscalls written in RUST.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.walmart.com/ip/Gateway-14-1-Ultra-Slim-Notebook-FHD-Intel-Core-i5-1135G7-Quad-Core-Iris-Xe-Graphics-16GB-RAM-512GB-SSD-Tuned-THX-Fingerprint-Scanner-1MP-Webcam-HDMI/654399212" target="_blank">The best laptop deal I have ever seen</a>. If you need a DEF CON burner, this is it ($279 and free shipping at the time of publishing).</li>
<li><a href="https://github.com/nadermx/backgroundremover" target="_blank">backgroundremover</a> - Background Remover lets you Remove Background from images and video using AI with a simple command line interface that is free and open source.</li>
<li><a href="https://lockboxx.blogspot.com/2023/05/course-review-practical-web-application.html" target="_blank">Course Review: "Practical Web Application Security and Testing"</a>. The course is $1 during May if you are interested.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 341 (+2)</p>
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
