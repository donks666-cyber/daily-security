Title: Last Week in Security (LWiS) - 2024-06-24
Date: 2024-06-24 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-06-24
Author: Erik
Summary: Electron security (<a href="https://x.com/khronokernel" target="_blank">@khronokernel</a>), snapshot fuzzing (<a href="https://x.com/h0mbre_" target="_blank">@h0mbre_</a>), macOS helpers LPE (<a href="https://x.com/L0Psec" target="_blank">@L0Psec</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-06-17 to 2024-06-24.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://x.com/i/bookmarks?post_id=1804918333231243704" target="_blank">[X/Twitter] CVE-2024-30078 (Windows Wi-Fi Driver RCE) details</a> - Looks like the bug is in handling VLAN (802.1Q) tags?</li>
<li><a href="https://learn.microsoft.com/en-us/windows/arm/arm64ec" target="_blank">Arm64EC - Build and port apps for native performance on Arm</a> - Microsoft is allowing developers to run both native ARM code and emulated x86_64 code in the same process at the same time on their new ARM builds of Windows. An impressive engineering feat, and probably a nightmare for EDR.</li>
<li><a href="https://www.reuters.com/technology/biden-ban-us-sales-kaspersky-software-over-ties-russia-source-says-2024-06-20/" target="_blank">Biden bans US sales of Kaspersky software over Russia ties</a> - The Russian affiliated EDR is soon to be completely banned in the US. It was previously banned from federal government networks in 2017.</li>
<li><a href="https://www.bleepingcomputer.com/news/security/advance-auto-parts-confirms-data-breach-exposed-employee-information/" target="_blank">Advance Auto Parts confirms data breach exposed employee information</a> - "...their data was stolen from a third-party cloud database environment". 3rd party risk FTW.</li>
<li><a href="https://poppopret.org/2024/06/24/google-stop-burning-counterterrorism-operations/" target="_blank">Google: Stop Burning Counterterrorism Operations</a> - Interesting read. National security vs Google.</li>
<li><a href="https://www.justice.gov/opa/pr/consulting-companies-pay-113m-failing-comply-cybersecurity-requirements-federally-funded" target="_blank">Consulting Companies to Pay $11.3M for Failing to Comply with Cybersecurity Requirements in Federally Funded Contract</a> - $11.3 million to settle claims of failing to meet security standards in a federal contract for New York's rental assistance program during the COVID-19 pandemic.</li>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations" target="_blank">Cloaked and Covert: Uncovering UNC3886 Espionage Operations</a> - Mandiant has uncovered operations by UNC3886, a suspected China-linked espionage group, targeting global strategic orgs with custom malware and exploiting 0-day vulnerabilities in FortiOS and VMware.</li>
<li><a href="https://krebsonsecurity.com/2024/06/krebsonsecurity-threatened-with-defamation-lawsuit-over-fake-radaris-ceo/" target="_blank">KrebsOnSecurity Threatened with Defamation Lawsuit Over Fake Radaris CEO</a> - KrebsOnSecurity faces a defamation lawsuit after exposing the dubious practices and fake CEO of the data broker Radaris, which has been involved in deceptive marketing and privacy concerns.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.guidepointsecurity.com/blog/sccm-exploitation-evading-defenses-and-moving-laterally-with-sccm-application-deployment/" target="_blank">SCCM Exploitation: Evading Defenses and Moving Laterally with SCCM Application Deployment</a> - Solid write-up on SCCM tradecraft using cobalt strike and open-source tooling.</li>
<li><a href="https://www.elttam.com/blog/plormbing-your-django-orm/#content" target="_blank">plORMber Your Django ORM</a> - "allowing un-validated user inputs into “safe” ORM methods could introduce a security risk." There are a few different ways to exploit ORM functions if the input isn't sanitized that allow for data theify (leaking password hashes, etc).</li>
<li><a href="https://googleprojectzero.blogspot.com/2024/06/project-naptime.html" target="_blank">Project Naptime: Evaluating Offensive Security Capabilities of Large Language Models</a> - Everyone is "doing AI," but can LLMs hack anything? Google Project Zero decided to find out. Answer: sort of, if the bugs are unambiguous and easly reachable. AI is not going to replace security researchers for a while.</li>
<li><a href="https://jprx.io/cve-2024-27815/" target="_blank">CVE-2024-27815</a> - Using _MSIZE instead of MLEN leads to a case where an attacker can write up to 255 bytes of data into a data field that is only 224 bytes long (and a kernel crash of course).</li>
<li><a href="https://www.elastic.co/security-labs/grimresource" target="_blank">GrimResource - Microsoft Management Console for initial access and evasion</a> - Initial access vectors continue to evolve. The latest use MSC files and execute code as mmc.exe. For an example see: <a href="https://gist.github.com/joe-desimone/2b0bbee382c9bdfcac53f2349a379fa4" target="_blank">grimresource.msc</a>.</li>
<li><a href="https://h0mbre.github.io/Lucid_Snapshots_Coverage/#" target="_blank">Fuzzer Development 4: Snapshots, Code-Coverage, and Fuzzing</a> - If you've been keeping up with this series you know what to expect. Detailed, technical fuzzing content.</li>
<li><a href="https://khronokernel.com/macos/2024/06/19/MDOYVR-2024.html" target="_blank">MacDevOpsYVR 2024 - Electron Security</a> - Electron has enabled many cross-platform applications (by shipping web browsers with them), but also can in some cases be hijacked for malicious purposes like TCC bypass. <a href="https://github.com/ripeda/lectricus" target="_blank">Lectricus</a> can detect these misconfigurations programatically.</li>
<li><a href="https://posts.specterops.io/feeding-the-phishes-276c3579bba7" target="_blank">Feeding the Phishes</a> - If you've done an engagement that involved phishing targets behind a secure email gateway, you know the issues presented in this post. Some good ideas for getting around email gateways are presented.</li>
<li><a href="https://blog.kandji.io/twitch-privileged-helper" target="_blank">How Twitch Helper Can Be Used for Privilege Escalation</a> - on macOS many applications install a "helper" which can do privileged actions, but if they aren't properly protected these helpers can lead to privilege escalation.</li>
<li><a href="https://blog.cloudflare.com/residential-proxy-bot-detection-using-machine-learning" target="_blank">Using machine learning to detect bot attacks that leverage residential proxies</a> - Residential proxies are a password spraying cheat code right now. Looks like Cloudflare is trying to combat this.</li>
<li><a href="https://evanconnelly.github.io/post/ios-oauth/" target="_blank">Mobile OAuth Attacks - iOS URL Scheme Hijacking Revamped</a> - Researchers identified a vulnerability in iOS where any app could hijack accounts via OAuth and Custom URL Schemes, potentially affecting numerous apps and a core iOS feature.</li>
<li><a href="https://css.ethz.ch/content/dam/ethz/special-interest/gess/cis/center-for-securities-studies/pdfs/CyberDefenseReport_%20From%20Vegas%20to%20Chengdu.pdf" target="_blank">[PDF] Hacking Contests, Bug Bounties, and China's Offensive Cyber Ecosystem</a> - A report on China's offensive ecosystem, detailing how vulnerability research works in China and its "hack for hire" culture.</li>
<li><a href="https://blog.pwnedlabs.io/blog.pwnedlabs.io/exploiting-gcp-cloud-build-for-privilege-escalation" target="_blank">Exploiting GCP Cloud Build for Privilege Escalation</a> - Exploit Google Cloud's Cloud Build service to escalate privileges and execute lateral movements within a GCP environment by manipulating the cloudbuild.yaml configuration file.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Addepar/RedFlag" target="_blank">RedFlag</a> - RedFlag uses AI to identify high-risk code changes. Run it in batch mode for release candidate testing or in CI pipelines to flag PRs and add reviewers. RedFlag's flexible configuration makes it valuable for any team.</li>
<li><a href="https://github.com/ZERODETECTION/MSC_Dropper" target="_blank">MSC_Dropper</a> - is a Python script designed to automate the creation of MSC (Microsoft Management Console) files with customizable payloads for arbitrary execution. This tool leverages a method discovered by Samir (@SBousseaden) from Elastic Security Labs, termed #GrimResource, which facilitates initial access and evasion through mmc.exe.</li>
<li><a href="https://github.com/pygrum/gimmick" target="_blank">gimmick</a> - Section-based payload obfuscation technique for x64.</li>
<li><a href="https://github.com/x86matthew/DOSVisor" target="_blank">DOSVisor</a> - x86 Real-Mode MS-DOS Emulator using Windows Hypervisor Platform.</li>
<li><a href="https://github.com/EvilBytecode/Lifetime-Amsi-EtwPatch" target="_blank">Lifetime-Amsi-EtwPatch</a> - Two in one, patch lifetime powershell console, no more etw and amsi!</li>
<li><a href="https://github.com/NUL0x4C/FetchPayloadFromDummyFile" target="_blank">FetchPayloadFromDummyFile</a> - Construct a payload at runtime using an array of offsets.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/tylerdotrar/SigmaPotato" target="_blank">SigmaPotato</a> - SeImpersonate privilege escalation tool for Windows 8 - 11 and Windows Server 2012 - 2022 with extensive PowerShell and .NET reflection support.</li>
<li><a href="https://github.com/ariary/volana" target="_blank">volana</a> - 🌒 Shell command obfuscation to avoid detection systems.</li>
<li><a href="https://github.com/1N3/Sn1per" target="_blank">Sn1per</a> - Attack Surface Management Platform.</li>
<li><a href="https://github.com/evilsocket/nerve" target="_blank">nerve</a> - Instrument any LLM to do actual stuff.</li>
<li><a href="https://github.com/tguard-soc-package/nusantara" target="_blank">nusantara</a> - T-Guard is an innovative security operations center (SOC) solution that leverages the strength of leading open-source tools to provide robust protection for your digital assets.</li>
<li><a href="https://github.com/allinurl/goaccess" target="_blank">goaccess</a> - GoAccess is a real-time web log analyzer and interactive viewer that runs in a terminal in *nix systems or through your browser.</li>
<li><a href="https://gist.github.com/tin-z/a469e996f8107a5ca8d3c858a2a4b65f" target="_blank">VR_roadmap.md</a> -  Becoming a Vulnerability Researcher roadmap</li>
<li><a href="https://github.com/flipt-io/reverst" target="_blank">reverst</a> - Reverse Tunnels in Go over HTTP/3 and QUIC.</li>
<li><a href="https://picarta.ai/" target="_blank">Image Location Search</a> - Could be cool for some OSINT practitioners out there.</li>
<li><a href="https://github.com/CICADA8-Research/LogHunter" target="_blank">LogHunter</a> - Opsec tool for finding user sessions by analyzing event log files through RPC (MS-EVEN).</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 427 (+0)</p>
<p>Blogs monitored: 382 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
