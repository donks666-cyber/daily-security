Title: Last Week in Security (LWiS) - 2025-02-10
Date: 2025-02-10 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-02-10
Author: Erik
Summary: Mythic C#/BOF support (<a href="https://x.com/its_a_feature_" target="_blank">@its_a_feature_</a>), Ludus guide (<a href="https://x.com/sherif_ninja" target="_blank">@sherif_ninja</a>), Window shadow stacks (<a href="https://x.com/33y0re" target="_blank">@33y0re</a>), Orbit scanner (<a href="https://x.com/BHinfoSecurity" target="_blank">@BHinfoSecurity</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-01-27 to 2025-02-10.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.techdirt.com/2025/02/05/a-25-year-old-is-writing-backdoors-into-the-treasurys-6-trillion-payment-system-what-could-possibly-go-wrong/" target="_blank">A 25-Year-Old Is Writing Backdoors Into The Treasury’s $6 Trillion Payment System. What Could Possibly Go Wrong?</a> - After spending years complying with strict government cybersecurity regulations as a contractor, this feels like a slap in the face. It has been <a href="https://storage.courtlistener.com/recap/gov.uscourts.dcd.277055/gov.uscourts.dcd.277055.13.0_1.pdf" target="_blank">ordered to stop</a> by a court, but <a href="https://talkingpointsmemo.com/edblog/heres-what-treasury-and-doj-mean-by-read-only-access" target="_blank">what Treasury and DOJ mean by ‘read-only’ access</a> is in question. Good thing Marko Elez has the <a href="https://github.com/markoelez?achievement=yolo&amp;tab=achievements" target="_blank">YOLO badge on GitHub</a>. Another DOGE employee seemingly has a <a href="https://krebsonsecurity.com/2025/02/teen-on-musks-doge-team-graduated-from-the-com/" target="_blank">history of cybercrime</a>.</li>
<li><a href="https://www.theverge.com/news/608145/apple-uk-icloud-encrypted-backups-spying-snoopers-charter" target="_blank">Apple ordered to open encrypted user accounts globally to UK spying</a> - While it's not unusual for a country to force tech companies to hand over information on their citizens (i.e. USA, China, etc), the UK is demanding data on <strong>anyone</strong> that has an Apple/iCloud account. It will be interesting to see Apple's reaction, although there are gag orders so it may take another leak to find out what happens. Now is just as good a time as any to turn on <a href="https://support.apple.com/en-us/108756" target="_blank">Advanced Data Protection for iCloud</a>.</li>
<li><a href="https://socket.dev/blog/malicious-package-exploits-go-module-proxy-caching-for-persistence" target="_blank">Go Supply Chain Attack: Malicious Package Exploits Go Module Proxy Caching for Persistence</a> - The issue with easy to use package systems is... the malware. The difference between <cite>boltdb-go/bolt</cite> and <cite>boltdb/bolt</cite> is an infected machine. The unique structure of the Go package cache made this really difficult to spot unless you downloaded the package from the proxy - the backing GitHub repo was clean.</li>
<li><a href="https://blog.cloudflare.com/cloudflare-incident-on-february-6-2025/" target="_blank">Cloudflare incident on February 6, 2025</a> - A simple abuse report led to the accidental takedown of the global R2 (file storage) gateway for an hour. Oops. All major tech companies have these outages, but Cloudflare has a great history of transparency.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://posts.specterops.io/forging-a-better-operator-quality-of-life-e8bf24fc2aba" target="_blank">Forging a Better Operator Quality of Life</a> - The Mythic C2 platform has introduced a way to easily use C# assemblies and Cobalt Strike Beacon Object Files (BOFs) with Mythic agents. If you're building a custom C2, consider only writing an agent and letting Mythic handle all the backend C2 for you.</li>
<li><a href="https://retr0.blog/blog/llama-rpc-rce" target="_blank">Llama's Paradox - Delving deep into Llama.cpp and exploiting Llama.cpp's Heap Maze, from Heap-Overflow to Remote-Code Execution.</a> - Ever wondered what a modern heap overflow to RCE exploit looks like on Linux? Well, here is the best example I have seen!</li>
<li><a href="https://xphantom.nl/posts/Offensive-Security-Lab/" target="_blank">Build Your Own Offensive Security Lab A Step-by-Step Guide with Ludus</a> - A great write up that covers not only the basics of <a href="https://ludus.cloud/" target="_blank">Ludus</a> but also some advanced tricks!</li>
<li><a href="https://connormcgarr.github.io/km-shadow-stacks/" target="_blank">Exploit Development: Investigating Kernel Mode Shadow Stacks on Windows</a> - The king of long form technical articles is back! In this one, Connor explores the low level Intel's Control-Flow Enforcement Technology (CET) in Window's secure kernel. Side note, Prelude has made some interesting hires recently - first Matt Hand, now Connor McGarr... what are they cooking?</li>
<li><a href="https://labs.watchtowr.com/8-million-requests-later-we-made-the-solarwinds-supply-chain-attack-look-amateur/" target="_blank">8 Million Requests Later, We Made The SolarWinds Supply Chain Attack Look Amateur</a> - The gang and watchTowr do it again. Registering abandoned S3 buckets leds to epic amounts of potential compromise. Imagine if a ransomware crew did this instead of a well-natured cybersecurity company.</li>
<li><a href="https://starlabs.sg/blog/2025/12-mali-cious-intent-exploiting-gpu-vulnerabilities-cve-2022-22706/" target="_blank">Mali-cious Intent: Exploiting GPU Vulnerabilities (CVE-2022-22706 / CVE-2021-39793)</a> - I don't have the stats to back this up, but it feels like the Mali GPUs of Android phones are the source of a lot of serious Android exploits.</li>
<li><a href="https://jhftss.github.io/Endless-Exploits/" target="_blank">Endless Exploits: The Saga of a macOS Vulnerability Struck Nine Times</a> - Security is hard. It took 9 patches to finally stop the exploitation of PackageKit bugs (some patches introduced new bugs!).</li>
<li><a href="https://neodyme.io/en/blog/com_hijacking_2/#recap" target="_blank">The Key to COMpromise - Abusing a TOCTOU race to gain SYSTEM, Part 2</a> - Some advanced COM hijacking against AVG Internet Security to gain SYSTEM privileges.</li>
<li><a href="https://posts.specterops.io/further-adventures-with-cmpivot-client-coercion-38b878b740ac" target="_blank">Further Adventures With CMPivot — Client Coercion</a> - How CMPivot, a component of Microsoft Configuration Manager, can be exploited to coerce SMB authentication from client machines. This could equate to privilege escalation opportunities in an SCCM/ConfigMgr environment.</li>
<li><a href="https://labs.jumpsec.com/bring-your-own-trusted-binary-byotb-bsides-edition/" target="_blank">Bring Your Own Trusted Binary (BYOTB) – BSides Edition</a> - Basically sprinkle some signed alternatives to <a href="https://github.com/nicocha30/ligolo-ng" target="_blank">ligolo-ng</a> on your next engagement.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://gist.github.com/S3cur3Th1sSh1t/8294ec59d1ef38cba661697edcfacb9b" target="_blank">tspatch.c</a> - "Tired of using ts::multirdp, because Mimikatz is a nogo nowadays and get's flagged anyway most of the time? Well, here is a standalone patching implementation with Win11 support"</li>
<li><a href="https://github.com/lolc2/lolc2.github.io" target="_blank">lolc2.github.io</a> is a collection of C2 frameworks that leverage legitimate services to evade detection.</li>
<li><a href="https://github.com/Teach2Breach/pool_party_rs" target="_blank">pool_party_rs</a> - This tool is a remote process injection uses techniques described in <a href="https://www.safebreach.com/blog/process-injection-using-windows-thread-pools/" target="_blank">The Pool Party You Will Never Forget</a> and found in <a href="https://github.com/SafeBreach-Labs/PoolParty" target="_blank">PoolParty</a>.</li>
<li><a href="https://github.com/johnjhacking/bloudstrike" target="_blank">bloudstrike</a> - Linux CS bypass technique.</li>
<li><a href="https://github.com/nettitude/raccoon" target="_blank">raccoon</a> - a C# tool for extending the screenshot functionality of Command and Control (C2) frameworks. The tool was developed to take targeted screenshots of processes even if their window is minimised. Check out the <a href="https://www.lrqa.com/en/cyber-labs/introducing-raccoon/" target="_blank">original blog</a> .</li>
<li><a href="https://github.com/logangoins/Stifle" target="_blank">Stifle</a> - .NET Post-Exploitation Utility for Abusing Explicit Certificate Mappings in ADCS.</li>
<li><a href="https://github.com/boku7/StringReaper" target="_blank">StringReaper</a> - Reaping treasures from strings in remote processes memory.</li>
<li><a href="https://github.com/CodeXTF2/ScreenshotBOF" target="_blank">ScreenshotBOF</a> - An alternative screenshot capability for Cobalt Strike that uses WinAPI and does not perform a fork &amp; run. Screenshot downloaded in memory.</li>
<li><a href="https://github.com/johnjhacking/CVE-2024-38143" target="_blank">CVE-2024-38143</a> - Windows WLAN AutoConfig Service Elevation of Privilege Vulnerability.</li>
<li><a href="https://github.com/orbitscanner/orbit" target="_blank">orbit</a> - Orbit is a powerful platform designed to facilitate large-scale Nuclei scans, enabling teams to efficiently manage and analyze scan results.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/MorDavid/BloodHoundViewer" target="_blank">BloodHoundViewer</a> - BloodHound CE Enhancement Extension - A Chrome extension that enhances BloodHound Community Edition with additional features including query history navigation, improved layout controls, and Neo4j button.</li>
<li><a href="https://github.com/frack113/ludus_caldera_server" target="_blank">ludus_caldera_server</a> - Ansible role to install a CALDERA server for LUDUS.</li>
<li><a href="https://github.com/frack113/ludus_caldera_agent" target="_blank">ludus_caldera_agent</a> - Ansible role to install a CALDERA agent for LUDUS.</li>
<li><a href="https://github.com/frack113/ludus_aurora_agent" target="_blank">ludus_aurora_agent</a> - Ludus role to install Free windows EDR Aurora.</li>
<li><a href="https://github.com/Primusinterp/ludus-ad-vulns" target="_blank">ludus-ad-vulns</a> - Ludus role that adds vulnerabilities in an Active Directory.</li>
<li><a href="https://github.com/dmcxblue/AzureRedirector" target="_blank">AzureRedirector</a> - A C# project that builds a Web Applciation which redirects all HTTPS.</li>
<li><a href="https://github.com/luchina-gabriel/OSX-PROXMOX" target="_blank">OSX-PROXMOX</a> - Voilà, install macOS on ANY Computer! This is really and magic easiest way!.</li>
<li><a href="https://github.com/uniQuk/caReports" target="_blank">caReports</a> - Conditional Access Reporting.</li>
<li><a href="https://github.com/rauchg/doom-captcha" target="_blank">doom-captcha</a> - A DOOM®-based CAPTCHA for the web.</li>
<li><a href="https://github.com/aws-samples/well-architected-iac-analyzer" target="_blank">well-architected-iac-analyzer</a> - Well-Architected Infrastructure as Code (IaC) Analyzer is a project that demonstrates how generative AI can be used to evaluate infrastructure code for alignment with best practices.</li>
<li><a href="https://www.vergiliusproject.com/" target="_blank">Vergilius</a> - Take a look into the depths of Windows kernels and reveal more than 60,000 undocumented structures.</li>
<li><a href="https://msendpointmgr.com/2025/02/09/company-portal-app-deep-dive/" target="_blank">The Company Portal app – A deep dive into bridges</a> - Thorough explanation on how Microsoft's Company Portal app uses two bridge components - ConfigMgr Bridge and Intune Management Extension Bridge - to handle application installations and device management functions in Windows.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 444 (+1)</p>
<p>Blogs monitored: 404 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
