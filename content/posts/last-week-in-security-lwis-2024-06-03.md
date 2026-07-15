Title: Last Week in Security (LWiS) - 2024-06-03
Date: 2024-06-03 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-06-03
Author: Erik
Summary: F5 TLS MITM (<a href="https://x.com/lowercase_drm" target="_blank">@lowercase_drm</a> + <a href="https://x.com/myst404_" target="_blank">@myst404_</a>), WASM phishing tool (<a href="https://x.com/JumpsecLabs" target="_blank">@JumpsecLabs</a>), MS Recall info (<a href="https://x.com/GossiTheDog" target="_blank">@GossiTheDog</a>), Checkpoint path traversal (<a href="https://x.com/watchtowrcyber" target="_blank">@watchtowrcyber</a>), smbclient-ng (<a href="https://x.com/podalirius_" target="_blank">@podalirius_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-05-29 to 2024-06-03.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://community.snowflake.com/s/question/0D5VI00000Emyl00AB/detecting-and-preventing-unauthorized-user-access" target="_blank">Detecting and Preventing Unauthorized User Access</a> - Snowflake, CrowdStrike, and Mandiant, are providing a joint statement related to their ongoing investigation involving a targeted threat campaign against some Snowflake customer accounts. It was previously reported that Snowflake itself had a breach. It looks like its just a bunch of Snowflake customers that are getting breached.</li>
<li><a href="https://go.recordedfuture.com/hubfs/reports/CTA-RU-2024-0530.pdf" target="_blank">[PDF] GRU's BlueDelta Targets Key Networks in Europe with Multi-Phase Espionage Campaigns</a> - A detailed report on how an APT operates. While the malware itself is not impressive (batch scripts), it likely was somewhat effective. Take a look at the phishing lures for inspiration on your next red team operation.</li>
<li><a href="https://www.cs.umd.edu/~dml/papers/wifi-surveillance-sp24.pdf" target="_blank">[PDF] Surveilling the Masses with Wi-Fi-Based Positioning Systems</a> - Apple's database of WiFi router locations aids Apple devices in locating themselves, but having a fairly accurate location of every WiFi router every Apple device has ever seen is a pretty powerful intelligence tool if queried correctly and the data presented well.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://doublepulsar.com/recall-stealing-everything-youve-ever-typed-or-viewed-on-your-own-windows-pc-is-now-possible-da3e12e9465e" target="_blank">Stealing everything you've ever typed or viewed on your own Windows PC is now possible with two lines of code — inside the Copilot+ Recall disaster.</a> - Security implications of Recall. Microsoft capturing and storing screenshots? What could go wrong? This is the best keylogger/screenshot tool for a red-teamer, built right into the OS.</li>
<li><a href="https://posts.specterops.io/to-infinity-and-beyond-feab2d8ff93c" target="_blank">To Infinity and Beyond!</a> - A perspective around EDR limitations and purple teams.</li>
<li><a href="https://www.sonatype.com/blog/pypi-crypto-stealer-targets-windows-users-revives-malware-campaign" target="_blank">PyPI crypto-stealer targets Windows users, revives malware campaign</a> - Another day, another malicious PyPI package! This does some recon, persistence and crypto-theft.</li>
<li><a href="https://decoder.cloud/2024/05/30/abusing-the-serelabelprivilege/" target="_blank">Abusing the SeRelabelPrivilege</a> - How SeRelabelPrivilege allows you to take ownership of a resource which opens up privilege escalation opportunities. A <a href="https://github.com/decoder-it/RelabelAbuse" target="_blank">PoC</a> is available.</li>
<li><a href="https://labs.jumpsec.com/wasm-smuggling-for-initial-access-and-w-a-l-k-tool-release/" target="_blank">WASM Smuggling for Initial Access and W.A.L.K. Tool Release</a> - Initial access with (currently working) evasion via WASM (HTML smuggling). <a href="https://github.com/JumpsecLabs/WALK_WebAssembly_Lure_Krafter" target="_blank">PoC</a> dropped as well!</li>
<li><a href="https://labs.watchtowr.com/check-point-wrong-check-point-cve-2024-24919/" target="_blank">Check Point - Wrong Check Point (CVE-2024-24919)</a> - A simple POST request and you've got a nasty path traversal.</li>
<li><a href="https://www.elastic.co/security-labs/protecting-your-devices-from-information-theft-keylogger-protection" target="_blank">Protecting your devices from information theft: Keylogger detection using Windows API behaviors</a> Elastic EDR released enhanced features for detecting keyloggers by monitoring windows APIs and utilizing some "new behavioral" detection rules. Worth testing in your <a href="https://ludus.cloud/" target="_blank">Ludus</a> instance with our <a href="https://github.com/badsectorlabs/ludus_elastic_container" target="_blank">ludus_elastic_container</a> role.</li>
<li><a href="https://blog.plerion.com/things-you-wish-you-didnt-need-to-know-about-s3/" target="_blank">Things you wish you didn't need to know about S3</a> - If you manage or protect AWS resources, this one is for you. Some S3 misconfigurations you should be aware of.</li>
<li><a href="https://scorpiosoftware.net/2024/06/01/building-a-verifier-dll/" target="_blank">Building a Verifier DLL</a> - A method for injecting DLLs into processes to monitor and modify their behavior by Pavel Yosifovich.</li>
<li><a href="https://www.landh.tech/blog/20240603-npm-cache-poisoning/" target="_blank">How a Single Vulnerability Can Bring Down the JavaScript Ecosystem</a> - A cache poisoning DoS on the NPM registry. Pretty cool!</li>
<li><a href="https://blog.openthreatresearch.com/rise-of-the-planet-of-the-agents/" target="_blank">Rise of the Planet of the Agents 🤖: Creating an LLM-Based AI Agent from Scratch!</a> - The journey of creating a LLM-based AI agent.</li>
<li><a href="https://www.outflank.nl/blog/2024/06/03/edr-internals-macos-linux/" target="_blank">EDR Internals for macOS and Linux</a> - Good read on EDR evasion for macOS and linux. The blog highlights capabilities and weaknesses of EDR against macOS and linux platforms.</li>
<li><a href="https://offsec.almond.consulting/post-exploiting-f5-BIG-IP.html" target="_blank">Post-Exploiting an F5 Big-IP: root, and now what?</a> - Load balancers can often seen valuable traffic. This blog shows how to set up a Machine-in-the-middle (MITM) attack and compromise sensitive information from the applications being load-balanced.</li>
<li><a href="https://khronokernel.com/macos/2024/06/03/CVE-2024-27822.html" target="_blank">CVE-2024-27822: macOS PackageKit Privilege Escalation</a> - A little bit tricky, as you have to poison the user's .zshenv file and wait for a .pkg install for the exploit to work, but if you are on a macOS system with some time, it's a valid technique!</li>
<li><a href="https://medium.com/@enki-techblog/ios-16-5-1-safari-rce-analysis-cve-2023-37450-89bb8583bebc" target="_blank">iOS 16.5.1 safari RCE Analysis (CVE-2023-37450)</a> - We've seen lots of write-ups on V8 javascript engine bugs, but not many on Apple's AbstractInterpreter in WebKit. It's an old bug, but good information.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/rbmm/RtlClone" target="_blank">RtlClone</a> - Implementing RtlCloneUserProcess using NtCreateUserProcess, detailing undocumented APIs for process cloning.</li>
<li><a href="https://github.com/decoder-it/RelabelAbuse" target="_blank">RelabelAbuse</a> - Simple POC for exploiting SeRelabelPrivilege</li>
<li><a href="https://github.com/JumpsecLabs/WALK_WebAssembly_Lure_Krafter" target="_blank">WALK_WebAssembly_Lure_Krafter</a> - A web assembly (WASM) phishing lure generator based on pre-built templates and written in Rust with some GenAI assistance. W.A.L.K. aims at aiding with initial access during red teams and phishing exercises leveraging WASM smuggling techniques.</li>
<li><a href="https://github.com/smokeme/ansible-havoc" target="_blank">ansible-havoc</a> - Scripts to deploy Havoc on Linode and setup categorization and SSL.</li>
<li><a href="https://github.com/tjnull/pentest-arsenal/tree/main/Cadiclus" target="_blank">Cadiclus</a> - Privilege Escalation Tool for Linux Systems that use PowerShell.</li>
<li><a href="https://github.com/kaist-hacking/CVE-2023-6702" target="_blank">CVE-2023-6702</a> - Chrome Renderer 1day RCE via Type Confusion in Async Stack Trace (v8ctf submission).</li>
<li><a href="https://github.com/p0dalirius/smbclient-ng" target="_blank">smbclient-ng</a> - is a fast and user friendly way to interact with SMB shares.</li>
<li><a href="https://github.com/sinsinology/CVE-2024-4358" target="_blank">CVE-2024-4358</a> - Progress Telerik Report Server pre-authenticated RCE chain (CVE-2024-4358/CVE-2024-1800).</li>
<li><a href="https://github.com/felmoltor/goLAPS" target="_blank">goLAPS</a> - Retrieve LAPS passwords from a domain. The tools is inspired in pyLAPS.</li>
<li><a href="https://browser.lol/" target="_blank">browser.lol</a> - This free service launches a browser inside your browser. They are certainly logging activity, but a nice service for opening suspect links without sensitive information. Tip: use the <a href="https://v6.browser.lol/create" target="_blank">v6</a> link to get a better experience. You can self host your own version with <a href="https://kasmweb.com/community-edition" target="_blank">kasm workspaces</a>.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://techcommunity.microsoft.com/t5/microsoft-security-experts-blog/recover-an-adcs-platform-from-compromise/ba-p/4120889" target="_blank">Recover an ADCS platform from compromise</a> - Microsoft guidance on recovering your AD CS environment after it's been compromised. We all know you popped ESC# today... Give it a read and then add this to your finding resources!</li>
<li><a href="https://github.com/CrowdStrike/VirtualGHOST" target="_blank">VirtualGHOST</a> - This repository contains a PowerShell script leveraging VMWare PowerCLI to identify unregistered VMWare Virtual Machines (VMs) that are powered on by comparing the list of VMs registered in the inventory (vCenter or ESXi) vs. those that are powered on.</li>
<li><a href="https://github.com/Edd13Mora/NetWrapper" target="_blank">NetWrapper</a> - Simple netexec wraper with html repport.</li>
<li><a href="https://medium.com/@flytechoriginal/state-of-wifi-security-in-2024-b88091015cc2" target="_blank">State of WiFi Security in 2024</a> - Doing oWireless pentesting? Must read!</li>
<li><a href="https://github.com/julep-ai/julep" target="_blank">julep</a> - Open-source alternative to Assistant's API with a managed backend for memory, RAG, tools and tasks. ~Supabase for building AI agents.</li>
<li><a href="https://github.com/alphasoc/flightsim" target="_blank">flightsim</a> - A utility to safely generate malicious network traffic patterns and evaluate controls.</li>
<li><a href="https://github.com/Leo4j/Invoke-SessionHunter" target="_blank">Invoke-SessionHunter</a> - Retrieve and display information about active user sessions on remote computers. No admin privileges required.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 427 (+0)</p>
<p>Blogs monitored: 381 (+2)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
