Title: Last Week in Security (LWiS) - 2023-11-29
Date: 2023-11-29 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-11-29
Author: Erik
Summary: 2x macOS TCC bypasses (<a href="https://twitter.com/gergely_kalman" target="_blank">@gergely_kalman</a>), Okta 🥷 (<a href="https://twitter.com/nickvangilder" target="_blank">@nickvangilder</a>), pcap analysis helper (<a href="https://twitter.com/bartavelle" target="_blank">@bartavelle</a>), Mythic and Merlin C2 updates (<a href="https://twitter.com/its_a_feature_" target="_blank">@its_a_feature_</a> + <a href="https://twitter.com/Ne0nd0g" target="_blank">@Ne0nd0g</a>) and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-11-13 to 2023-11-29.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.microsoft.com/en-us/security/blog/2023/11/22/diamond-sleet-supply-chain-compromise-distributes-a-modified-cyberlink-installer/" target="_blank">Diamond Sleet supply chain compromise distributes a modified CyberLink installer</a> - Supply chain attack by North Korea-based group. Thus far, the malicious activity has impacted over 100 devices in multiple countries, including Japan, Taiwan, Canada, and the United States.</li>
<li><a href="https://www.datadoghq.com/state-of-cloud-security/" target="_blank">State of Cloud Security</a> - Datadog summarizes what cloud security looks like in 2023. Nothing groundbreaking.</li>
<li><a href="https://www.wired.com/story/hemisphere-das-white-house-surveillance-trillions-us-call-records/" target="_blank">Secretive White House Surveillance Program Gives Cops Access to Trillions of US Phone Records</a>. Signal calls are free.</li>
<li><a href="https://posts.specterops.io/mythic-v3-2-highlights-interactive-tasking-push-c2-and-dynamic-file-browser-7035065e2b3d" target="_blank">Mythic v3.2 Highlights: Interactive Tasking, Push C2, and Dynamic File Browser</a>. The most flexible open source C2 gets some new features.</li>
<li><a href="https://posts.specterops.io/merlins-evolution-multi-operator-cli-and-peer-to-peer-magic-c7d2f29e192f" target="_blank">Merlin's Evolution: Multi-Operator CLI and Peer-to-Peer Magic</a>. Merlin also gets an update!</li>
<li><a href="https://owncloud.com/security-advisories/disclosure-of-sensitive-credentials-and-configuration-in-containerized-deployments/" target="_blank">Disclosure of sensitive credentials and configuration in containerized deployments</a>. A 10.0 CVSS vulnerability. A bit awkward as the same day <a href="https://owncloud.com/news/owncloud-becomes-part-of-kiteworks" target="_blank">ownCloud becomes part of Kiteworks</a>.</li>
<li><a href="https://blogs.eclipse.org/post/mike-milinkovich/introducing-eclipse-threadx" target="_blank">Introducing Eclipse ThreadX</a>. Azure RTOS becomes part of Eclipse ThreadX</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://gergelykalman.com/lateralus-CVE-2023-32407-a-macos-tcc-bypass.html" target="_blank">lateralus (CVE-2023-32407) - a macOS TCC bypass</a> - A macOS TCC bypass by exploiting a bug in the Metal framework's handling of the MTL_DUMP_PIPELINES_TO_JSON_FILE environment variable, allowing attackers to control file paths and potentially overwrite sensitive files, leading to a $30,500 bounty from Apple, who promptly addressed the issue and removed the problematic environment variable. <a href="https://github.com/gergelykalman/CVE-2023-32407-a-macOS-TCC-bypass-in-Metal" target="_blank">POC</a>. Want more TCC bypasses? <a href="https://gergelykalman.com/sqlol-CVE-2023-32422-a-macos-tcc-bypass.html" target="_blank">sqlol (CVE-2023-32422) - a macOS TCC bypass</a> also dropped last week.</li>
<li><a href="https://vulncheck.com/blog/cve-2023-44604-activemq-in-memory" target="_blank">Executing from Memory Using ActiveMQ CVE-2023-46604</a> - Bypass current detections of existing PoCs. This post discusses the exploitation of the ActiveMQ CVE-2023-46604 by executing Nashorn JavaScript from memory.</li>
<li><a href="https://themittenmac.com/low-level-process-hunting-on-macos/" target="_blank">Low-Level Process Hunting on macos</a> - This post discusses low-level process hunting on macOS, emphasizing the importance of understanding parent/child relationships and the nuances of process creation using fork, exec, and their combination. Decent read for those starting out macOS development.</li>
<li><a href="https://medium.com/nickvangilder/okta-for-red-teamers-perimeter-edition-c60cb8d53f23" target="_blank">Okta for Red Teamers — Perimeter Edition</a> - Identifying Okta portals, phishing infrastructure, hosting considerations, Evilginx phishlet setup, distributing phishing links, replaying captured session cookies, and evading Okta's behavioral detection policies. So much fuego in this one 🔥</li>
<li><a href="https://www.naksyn.com/edr%20evasion/2023/11/18/mockingjay-revisited-process-stomping-srdi-beacon.html" target="_blank">Mockingjay revisited - Process stomping and loading beacon with sRDI</a> - "...a variation of hasherezade's Process Overwriting and it has the advantage of writing a shellcode payload on a targeted section instead of writing a whole PE payload over the hosting process address space."</li>
<li><a href="https://decoder.cloud/2023/11/20/a-deep-dive-in-cert-publishers-group/" target="_blank">A “deep dive” in Cert Publishers Group</a> - Members of Cert Publishers can add a malicious Certification Authority, potentially leading to trusted certificates for various malicious activities.</li>
<li><a href="https://blackwinghq.com/blog/posts/a-touch-of-pwn-part-i/" target="_blank">A Touch of Pwn - Part I</a> - Vulnerabilities in the fingerprint sensors of Dell Inspiron 15, Lenovo ThinkPad T14, and Microsoft Surface Pro X/8 leading to auth bypass. Surprisingly, the Microsoft Surface was the worst of the bunch, despite the research being funded by Microsoft!</li>
<li><a href="https://revers.engineering/fun-with-pg-compliant-hook/" target="_blank">Fun with another PG-compliant Hook</a> - The article describes a technique for hooking SYSCALL in a PG-compliant manner using Event Tracing for Windows (ETW) and the HalPrivateDispatchTable. Useful for your next Windows rootkit.</li>
<li><a href="https://about.gitlab.com/blog/2023/11/20/stealth-operations-the-evolution-of-gitlabs-red-team/" target="_blank">Stealth operations: The evolution of GitLab's Red Team</a> - Solid write-up about building an internal red team. Some good content here about what a Red Team's goals should be and how to handle "deconfliction."</li>
<li><a href="https://blog.dfsec.com/ios/2023/11/19/thats-far-out-man/" target="_blank">That's FAR-out, Man</a>. A detailed look into finding a Linux kernel infoleak.</li>
<li><a href="https://www.synacktiv.com/en/publications/how-to-voltage-fault-injection" target="_blank">How to voltage fault injection</a>. Some very detailed physical hacking content. Need something a little more beginner friendly? Start with <a href="https://www.archcloudlabs.com/projects/trendnet-731br-spi-flash-dump/" target="_blank">Hardware Hacking - Dumping Flash Memory of a TrendNet-731BRv1 Router</a> also released last week.</li>
<li><a href="https://blog.checkymander.com/red%20team/tools/operations/Nemesis-Zero-To-Hero/" target="_blank">Nemesis: Zero to Hero</a>. The only thing better would have been an Ansible role.</li>
<li><a href="https://ruler-project.github.io/ruler-project/" target="_blank">Really Useful Logging and Event Repository (RULER) Project</a>. Good places to look during incident response, or post-compromise 😈.</li>
<li><a href="https://labs.nettitude.com/blog/creating-an-opsec-safe-loader-for-red-team-operations/" target="_blank">Creating an OPSEC safe loader for Red Team Operations</a>. Everyone could use a better loader.</li>
<li><a href="https://www.r-tec.net/r-tec-blog-process-injection-avoiding-kernel-triggered-memory-scans.html" target="_blank">Process Injection - Avoiding Kernel Triggered Memory Scans</a>. Speaking of better loaders...</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/RalfHacker/Kerbeus-BOF" target="_blank">Kerbeus-BOF</a>  - BOF for Kerberos abuse (an implementation of some important features of the Rubeus).</li>
<li><a href="https://github.com/antroguy/LocklessBof" target="_blank">LocklessBof</a> - A Beacon Object File (BOF) implementation of Lockless by HarmJ0y, designed to enumerate open file handles and facilitate the fileless download of locked files.</li>
<li><a href="https://github.com/MrDomainAdmin/LyinEagle" target="_blank">LyinEagle</a> - BETA C2 server that uses the legitimate FIN7 Griffon JScript as its implant.</li>
<li><a href="https://github.com/johnjhacking/badgerDAPS" target="_blank">badgerDAPS</a> -  Brute Ratel LDAP filtering and sorting tool. Easily take BR log output and pull hostnames for ease of use with other red team tooling. Supports OU filtering and removes disabled hosts.</li>
<li><a href="https://github.com/protectai/ai-exploits" target="_blank">AI Exploits</a> -  A collection of real world AI/ML exploits for responsibly disclosed vulnerabilities.</li>
<li><a href="https://github.com/naksyn/ProcessStomping" target="_blank">ProcessStomping</a> -  A variation of ProcessOverwriting to execute shellcode on an executable's section.</li>
<li><a href="https://gist.github.com/adamsvoboda/8e248c6b7fb812af5d04daba141c867e" target="_blank">DumpS1.ps1</a> - Uses a CoSetProxyBlanket to call the dump function in SentinelAgent.exe to dump a PID to disk. Requires local admin. Love the traitorware aspect here.</li>
<li><a href="https://github.com/nathan31337/Splunk-RCE-poc" target="_blank">Proof of concept exploit for CVE-2023-46214</a> - Authenticated RCE. Comes with a <a href="https://blog.hrncirik.net/cve-2023-46214-analysis" target="_blank">blog</a>.</li>
<li><a href="https://github.com/sokaRepo/CoercedPotatoRDLL" target="_blank">CoercedPotatoRDLL</a> -  Reflective DLL to privesc from NT Service to SYSTEM using SeImpersonateToken privilege</li>
<li><a href="https://www.synacktiv.com/en/publications/pcapan-a-pcap-analysis-helper" target="_blank">Pcapan: a PCAP analysis helper</a> - Filter out known good and find suspicious connections in pcaps.</li>
<li><a href="https://github.com/wavetermdev/waveterm" target="_blank">waveterm</a>  - An open-source, cross-platform terminal for seamless workflows. Reminds me of an open source <a href="https://www.warp.dev/" target="_blank">warp</a>.</li>
<li><a href="https://github.com/sterrasec/genpatch" target="_blank">genpatch</a>  - genpatch is IDA plugin that generates a python script for patching binary.</li>
<li><a href="https://github.com/factionsecurity/faction" target="_blank">faction</a> -  Pen Test Report Generation and Assessment Collaboration.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/assume-breach/Home-Grown-Red-Team" target="_blank">Home-Grown-Red-Team</a> - Some cool tradecraft write-ups.</li>
<li><a href="https://github.com/Xacone/BestEdrOfTheMarket" target="_blank">Best EDR Of The Market (BEOTM) 🐲</a> -  AV/EDR bypassing lab for training &amp; learning purposes.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 362 (+3)</p>
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
