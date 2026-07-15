Title: Last Week in Security (LWiS) - 2022-11-14
Date: 2022-11-14 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-11-14
Author: Erik
Summary: ROADtools Token eXchange (<a href="https://twitter.com/_dirkjan" target="_blank">@_dirkjan</a>), Certified pre-owned followup (<a href="https://twitter.com/harmj0y" target="_blank">@harmj0y</a> + <a href="https://twitter.com/tifkin_" target="_blank">@tifkin_</a>), AAD Privileged Access (<a href="https://twitter.com/0xcsandker" target="_blank">@0xcsandker</a>), FindEmptySystem (<a href="https://twitter.com/christruncer" target="_blank">@christruncer</a>), TelemetrySource (<a href="https://twitter.com/jsecurity101" target="_blank">@jsecurity101</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-11-07 to 2022-11-14.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.vice.com/en/article/5d3435/russian-hackers-abortion-records-dark-web" target="_blank">Russian Hackers Are Publishing Stolen Abortion Records on the Dark Web</a>. Much like the <a href="https://www.politico.eu/article/cybercriminal-extorts-finnish-therapy-patients-in-shocking-attack-ransomware-blackmail-vastaamo/" target="_blank">Finnish mental health</a> breach and hospital attacks this shows that no targets are off limits for criminals. Putting a <a href="https://www.wsj.com/articles/red-cross-wants-digital-symbols-to-deter-hackers-from-healthcare-institutions-11667571607" target="_blank">digital red cross</a> probably won't help.</li>
<li><a href="https://twitter.com/BillDemirkapi/status/1590062146486140928" target="_blank">ISOs from the internet will have MotW</a>. It was fun while it lasted. On to the next one.</li>
<li><a href="https://support.apple.com/en-us/HT213505" target="_blank">About the security content of iOS 16.1.1 and iPadOS 16.1.1</a>. XML parsing bugs could lead to RCE. The bug details are <a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2336" target="_blank">here</a> and <a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2335" target="_blank">here</a>. The update also <a href="https://techcrunch.com/2022/11/09/apple-limits-airdrop-everyone-option-to-10-minutes-in-china/" target="_blank">limits AirDrop 'Everyone' option to 10 minutes in China</a> with the speculation being that censors can't monitor airdropped content.</li>
<li><a href="https://research.securitum.com/amazon-once-again-lost-control-for-3-hours-over-the-ip-pool-in-a-bgp-hijacking-attack/" target="_blank">Amazon once again lost control (for 3 hours) over the IP pool in a BGP Hijacking attack</a>. It is a little wild to me that in 2022 we still use protocols developed for use among friendly research institutions as the underlying infrastructure for cryptocurrencies whose original goal was to survive in a network of adversarial participants.</li>
<li><a href="https://www.washingtonpost.com/technology/2022/11/08/trustcor-internet-addresses-government-connections/" target="_blank">Mysterious company with government ties plays key internet role</a>. I said last week, "your OS is just a bootloader for your browser." Perhaps we should take a look at who gets trusted by default in our browsers...</li>
<li><a href="https://petapixel.com/2022/11/09/a-russian-missile-crew-was-geolocated-from-just-this-photo/" target="_blank">A Russian Missile Crew Was Geolocated From Just This Photo</a>. OSINT is wild.</li>
<li><a href="https://finance.yahoo.com/news/intel-471-acquires-spiderfoot-090000155.html" target="_blank">Intel 471 Acquires SpiderFoot</a>. Attack surface monitoring is hot right now.</li>
<li><a href="https://twitter.com/MaximeDeGreve/status/1590415616921698305" target="_blank">Github code search launches</a>. I've been impressed with GitHub since the Microsoft acquisition. Let's see how long it lasts but so far so good.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://dirkjanm.io/introducing-roadtools-token-exchange-roadtx/" target="_blank">Introducing ROADtools Token eXchange (roadtx) - Automating Azure AD authentication, Primary Refresh Token (ab)use and device registration</a>. Dirk-jan is in the pantheon of researchers where every post is a must read. When it comes with a tool release... oh baby..</li>
<li><a href="https://posts.specterops.io/certificates-and-pwnage-and-patches-oh-my-8ae0f4304c1d" target="_blank">Certificates and Pwnage and Patches, Oh My!</a>. After a year, AD CS attacks have proven more pervasive than I thought they would be, led to more discoveries, and even patches from Microsoft to the way certs were mapped to identities. I guess you could say releasing their tooling really... imposed cost... as opposed to keeping it closed source.</li>
<li><a href="https://bugs.xdavidhu.me/google/2022/11/10/accidental-70k-google-pixel-lock-screen-bypass/" target="_blank">Accidental $70k Google Pixel Lock Screen Bypass</a>. This would be a perfect "bugdoor" (intentional bug used as a backdoor), but it looks like an honest mistake with a complex system of overlapping lockscreen.</li>
<li><a href="https://www.archcloudlabs.com/projects/loadlibrary-analysis/" target="_blank">Analysis of a LoadLibraryA Stack String Obfuscation Technique with Radare2 &amp; x86dbg</a>. Well laid out post on malware analysis.</li>
<li><a href="https://csandker.io//2022/11/10/Untangling-Azure-II-Privileged-Access.html" target="_blank">Untangling Azure Active Directory Permissions II: Privileged Access</a>. Building on <a href="https://csandker.io/2022/10/19/Untangling-Azure-Permissions.html" target="_blank">part 1</a>, this post explores more Azure Active Directory access concepts.</li>
<li><a href="https://thalpius.com/2022/11/08/microsoft-defender-for-identity-recent-bypasses-comments/" target="_blank">Microsoft Defender for Identity Recent Bypasses Comments</a>. Some good tips for defenders.</li>
<li><a href="https://research.nccgroup.com/2022/11/09/tales-of-windows-detection-opportunities-for-an-implant-framework/" target="_blank">Tales of Windows detection opportunities for an implant framework</a>. Some interesting detection techniques in here with code samples.</li>
<li><a href="https://unit42.paloaltonetworks.com/openlitespeed-vulnerabilities/" target="_blank">Unit 42 Finds Three Vulnerabilities in OpenLiteSpeed Web Server</a>. RCE, privilege escalation, and directory traversal - the holy trinity.</li>
<li><a href="https://www.trendmicro.com/en_us/research/22/k/cve-2019-8561-a-hard-to-banish-packagekit-framework-vulnerabilit.html" target="_blank">CVE-2019-8561: A Hard-to-Banish PackageKit Framework Vulnerability in macOS</a>. A good post that also shows the Apple commitment to "old" OSs isn't there. Monterey's latest release (12.6.1) does not include the fix...</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/FortyNorthSecurity/EDD/blob/master/EDD/Functions/FindEmptySystem.cs" target="_blank">EDD - FindEmptySystem</a>. More details <a href="https://fortynorthsecurity.com/blog/finding-empty-systems/" target="_blank">here</a></li>
<li><a href="https://github.com/capt-meelo/laZzzy" target="_blank">laZzzy</a> is a shellcode loader, developed using different open-source libraries, that demonstrates different execution techniques.</li>
<li><a href="https://research.nccgroup.com/2022/11/10/tool-release-web3-decoder-burp-suite-extension/" target="_blank">Tool Release - Web3 Decoder Burp Suite Extension</a>. Get those obnoxious cryptocurrency bounties!</li>
<li><a href="https://github.com/jsecurity101/TelemetrySource" target="_blank">TelemetrySource</a> - Project created to map functions responsible for triggering events from various telemetry sources. Details <a href="https://posts.specterops.io/uncovering-window-security-events-ab72e1ec745c" target="_blank">here</a>.</li>
<li><a href="https://blog.mondoo.com/cnquery-cnspec" target="_blank">Introducing cnquery and cnspec</a>. Imagine osquery but with GraphQL. Very cool.</li>
<li><a href="https://github.com/ccdescipline/CInject" target="_blank">CInject</a> Windows Kernel inject (no module no thread).</li>
<li><a href="https://github.com/reveng007/SharpGmailC2" target="_blank">SharpGmailC2</a> Our Friendly Gmail will act as Server and implant will exfiltrate data via smtp and will read commands from C2 (Gmail) via imap protocol.</li>
<li><a href="https://github.com/Cr4ckC4t/cve-2022-41352-zimbra-rce" target="_blank">cve-2022-41352-zimbra-rce</a> Zimbra &lt;9.0.0.p27 RCE.</li>
<li><a href="https://github.com/Mr-Un1k0d3r/AMSI-ETW-Patch" target="_blank">AMSI-ETW-Patch</a> Patch AMSI and ETW using a single byte patch for both.</li>
<li><a href="https://github.com/alfarom256/CVE-2022-3699" target="_blank">CVE-2022-3699</a> Lenovo Diagnostics Driver EoP - Arbitrary R/W.</li>
<li><a href="https://github.com/riesha/drv-vuln-scanner" target="_blank">drv-vuln-scanner</a> Finds imports that could be exploited, still requires manual analysis.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/secureworks/squarephish" target="_blank">squarephish</a> is an advanced phishing tool that uses a technique combining the OAuth Device code authentication flow and QR codes.</li>
<li><a href="https://lcamtuf.substack.com/p/digital-detritus" target="_blank">Digital detritus</a>. As a digital hoarder (look at me right now trying to collect and label all the relevant security stuff from last week) this post resinated with me.</li>
<li><a href="https://thealgorithmicbridge.substack.com/p/gpt-4-rumors-from-silicon-valley" target="_blank">GPT-4 Rumors From Silicon Valley</a>. AI is getting scary.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 421 (+0)</p>
<p>Blogs monitored: 327 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
