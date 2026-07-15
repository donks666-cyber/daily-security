Title: Last Week in Security (LWiS) - 2021-08-09
Date: 2021-08-09 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-08-09
Author: Erik
Summary: Cobalt Strike Updates (<a href="https://twitter.com/joevest" target="_blank">@joevest</a>, <a href="https://twitter.com/adamsvoboda" target="_blank">@adamsvoboda</a>), ProxyShell [another exchange RCE] (<a href="https://twitter.com/orange_8361" target="_blank">@orange_8361</a>). DeployPrinterNightmare (<a href="https://twitter.com/Flangvik" target="_blank">@Flangvik</a>), Pulse Connect patch bypass (<a href="https://twitter.com/buffaloverflow" target="_blank">@buffaloverflow</a>), Snapcraft App exploitation (<a href="https://twitter.com/itszn13" target="_blank">@itszn13</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-08-02 to 2021-08-09.</p>
<aside class="m-note m-warning">
<h3>BlackHat/DEF CON</h3>
<p>With everything that was released last week, I no doubt have missed a lot. Look for it in the coming weeks as I sift through everything! Be sure to check out PortSwigger's <a href="https://portswigger.net/daily-swig/top-hacks-from-black-hat-and-def-con-2021" target="_blank">Top Hacks from Black Hat and DEF CON 2021</a>. If you notice some DEF CON videos missing from YouTube, check out <a href="https://htp.live/videos/recently-added" target="_blank">HTP.live</a> to see if they were mirrored before being taken down.</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://lists.zx2c4.com/pipermail/wireguard/2021-August/006887.html" target="_blank">WireGuardNT, a high-performance WireGuard implementation for the Windows kernel</a>. The WireGuard team continues to impress with a Windows kernel driver to increase speed (up to 5x speedup) and decrease battery usage. It's currently experimental and can be enabled with <cite>reg add HKLMSoftwareWireGuard /v ExperimentalKernelDriver /t REG_DWORD /d 1 /f</cite>.</li>
<li><a href="https://www.eff.org/deeplinks/2021/08/apples-plan-think-different-about-encryption-opens-backdoor-your-private-life" target="_blank">Apple's Plan to "Think Different" About Encryption Opens a Backdoor to Your Private Life</a>. The company that once said, <a href="https://9to5mac.com/wp-content/uploads/sites/6/2019/01/DwGoq2uV4AA_Aov.jpg-large.jpeg" target="_blank">"What happens on your iPhone stays on your iPhone,"</a> and famously <a href="https://www.documentcloud.org/documents/2722199-5-15-MJ-00451-SP-USA-v-Black-Lexus-IS300.html" target="_blank">refused to unlock a terrorist's iPhone</a> is rolling out software that will scan images on an iPhone. This type of client-side scanning breaks end to end encryption, and while it is being used initially to combat child exploitation, how difficult would it be to use the same system to censor or report on iPhone users that share images such as <a href="https://www.vice.com/en/article/8qq5x5/the-rebel-physicist-and-the-tank-man" target="_blank">"tank man?"</a></li>
<li><dl>
<dt>Cobalt Strike News</dt>
<dd><ul>
<li><a href="https://blog.cobaltstrike.com/2021/08/04/cobalt-strike-4-4-the-one-with-the-reconnect-button/" target="_blank">Cobalt Strike 4.4: The One with the Reconnect Button</a>. In addition to some nice to have features, 4.4 comes with some major OPSEC changes. Users can now define their own reflective loader and sleep obfuscation technique. This should make it much more difficult to statically signature Cobalt Strike in memory. A good primer for the sleep mask functionality is <a href="https://adamsvoboda.net/sleeping-with-a-mask-on-cobaltstrike/" target="_blank">Sleeping with a Mask On</a>. For the customer loader <a href="https://x64sec.sh/custom-dll-injection-with-cobalt-strike/" target="_blank">this blog post</a> is a good starting place for creating a DLL injector BOF.</li>
<li><a href="https://blog.cobaltstrike.com/2021/08/04/cobalt-strike-dos-vulnerability-cve-2021-36798/" target="_blank">Cobalt Strike DoS Vulnerability (CVE-2021-36798)</a>. "Hotcobalt" was an issue with screenshot processing on the Cobalt Strike teamserver that allowed a "malicious" beacon to crash the teamserver. More details on the <a href="https://labs.sentinelone.com/hotcobalt-new-cobalt-strike-dos-vulnerability-that-lets-you-halt-operations/" target="_blank">SentinelOne blog</a>.</li>
<li><a href="https://blog.cobaltstrike.com/2021/08/06/introducing-cobalt-strike-community-kit/" target="_blank">Introducing Cobalt Strike Community Kit</a>. The <a href="https://cobalt-strike.github.io/community_kit/" target="_blank">Community Kit</a> is a great place to find community additions to the popular C2 framework. Be sure to vet anything before using it live!</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://media.defense.gov/2021/Aug/03/2002820425/-1/-1/1/CTR_KUBERNETES%20HARDENING%20GUIDANCE.PDF" target="_blank">Kubernetes Hardening Guidance</a>. The NSA and CISA drop 59 pages of Kubernetes hardening guidance. Just because you can push code to a cluster in one command doesn't mean you can forget about the security implications of doing so.</li>
<li>The Conti ransomware gang (aka Hermes aka Ryuk) had some of their "affilaite" training material leak last week. <a href="https://github.com/silence-is-best/files/blob/main/translate_f.pdf" target="_blank">Here</a> is a roughly translated PDF if you are interested in their tradecraft.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://labs.bishopfox.com/tech-blog/youre-doing-iot-rng" target="_blank">You're Doing IoT RNG</a>. "Basically, every IoT device with a hardware random number generator (RNG) contains a serious vulnerability whereby it fails to properly generate random numbers, which undermines security for any upstream use."</li>
<li><a href="https://blog.orange.tw/2021/08/proxylogon-a-new-attack-surface-on-ms-exchange-part-1.html" target="_blank">A New Attack Surface on MS Exchange Part 1 - ProxyLogon!</a> and <a href="https://blog.orange.tw/2021/08/proxyoracle-a-new-attack-surface-on-ms-exchange-part-2.html" target="_blank">A New Attack Surface on MS Exchange Part 2 - ProxyOracle!</a>. The master Orange Tsai is back to shell Exchange some more. This variant is dubbed "ProxyShell" and despite being patched in April a good number of Exchange servers on the internet appear to be vulnerable. Double check those patches and grab the <a href="https://github.com/SigmaHQ/sigma/blob/master/rules/web/web_exchange_proxyshell.yml" target="_blank">web_exchange_proxyshell.yml</a> Sigma rule.</li>
<li><a href="https://portswigger.net/research/http2" target="_blank">HTTP/2: The Sequel is Always Worse</a>. There are some tricky issues with HTTP/2, especially in an environment of load balancers, front and back end request processors, and the like. Web app assessors or bug bounty folks should pay special attention to this one.</li>
<li><a href="https://research.nccgroup.com/2021/08/05/technical-advisory-pulse-connect-secure-rce-via-uncontrolled-archive-extraction-cve-2021-22937-patch-bypass/" target="_blank">Technical Advisory: Pulse Connect Secure – RCE via Uncontrolled Archive Extraction – CVE-2021-22937 (Patch Bypass)</a>. Some bugs don't die on the first patch. NCC Group takes a swing at Pulse Secure and develops a patch bypass for an authenticated remote code execution vulnerability.</li>
<li><a href="https://blog.ret2.io/2021/08/04/snapcraft-injection/" target="_blank">Snapcraft Packages Come With Extra Baggage: Exploiting Ubuntu's Snapcraft Apps with CVE-2020-27348</a>. A crash while launching docker led to a "DLL sideloading" type issue against the snap container engine in Ubuntu. While the bug was patched in March of 2021, this is a great writeup.</li>
<li><a href="https://www.cyberark.com/resources/threat-research-blog/bypassing-windows-hello-without-masks-or-plastic-surgery?wvideo=dfzonzhind" target="_blank">Bypassing Windows Hello Without Masks or Plastic Surgery</a>. By spoofing an external USB camera, researchers were able to bypass Windows Hello authentication. It does require an IR photo of the victim, but otherwise becomes a quick USB skeleton key to the targeted Windows computer.</li>
<li><a href="https://blog.kyleavery.com/posts/multi-stage-mythic/" target="_blank">Multi-Stage Offensive Operations with Mythic</a>. Modular toolkits, varied C2 mechanisims, but a unified back end are the future of offensive operations.</li>
<li><a href="https://www.blackhillsinfosec.com/admins-nightmare-combining-hivenightmare-serioussam-and-ad-cs-attack-paths-for-profit/" target="_blank">Admin’s Nightmare: Combining HiveNightmare/SeriousSAM and AD CS Attack Path’s for Profit</a>. With all the Windows issues recently, it was only a matter of time until someone made a combo attack walkthrough.</li>
<li><a href="https://blog.compass-security.com/2021/08/relaying-ntlm-authentication-over-rpc-again/" target="_blank">Relaying NTLM authentication over RPC again…</a>. "Due to the absence of global integrity verification requirements for the RPC protocol, a man-in-the-middle attacker can relay his victim’s NTLM authentication to a target of his choice over the RPC protocol." No code released yet.</li>
<li><a href="https://bohops.com/2021/08/07/cve-2021-0090-intel-driver-support-assistant-dsa-elevation-of-privilege-eop/" target="_blank">CVE-2021-0090: Intel Driver &amp; Support Assistant (DSA) Elevation of Privilege (EoP)</a>. "Intel Driver &amp; Support Assistant (DSA) is a driver and software update utility for Intel components. DSA version 20.8.30.6 (and likely prior) is vulnerable to a local privilege escalation reparse point bug. An unprivileged user has nominal control over configuration settings within the web-based interface.  This includes the ability to configure the folder location for downloads and data (e.g. installers and log files). An unprivileged user can change the folder location, coerce a privileged file copy operation to a “protected” directory through a reparse point, and deliver a payload such as a DLL loading technique to execute unintended code."</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Flangvik/DeployPrinterNightmare" target="_blank">DeployPrinterNightmare</a> is a C# tool for installing a shared network printer abusing the PrinterNightmare bug to allow other network machines easy privesc!</li>
<li><a href="https://github.com/twistlock/whoc" target="_blank">whoc</a> is a container image that extracts the underlying container runtime and sends it to a remote server. Poke at the underlying container runtime of your favorite CSP container platform!</li>
<li><a href="https://github.com/GhostPack/Certify" target="_blank">Certify</a> is a C# tool to enumerate and abuse misconfigurations in Active Directory Certificate Services (AD CS). This is the toolset promised with the release of <a href="https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf" target="_blank">Certified Pre-Owned: Abusing Active Directory Certificate Services</a> in June of 2021. A <a href="https://http418infosec.com/ad-cs-the-certified-pre-owned-attacks" target="_blank">recent post</a> covered the attacks in more practical terms.</li>
<li><a href="https://github.com/knavesec/EyeWitnessTheFitness" target="_blank">EyeWitnessTheFitness</a> is a combination of <a href="https://github.com/FortyNorthSecurity/EyeWitness" target="_blank">EyeWitness</a> (web screenshot OSINT tool) and <a href="https://github.com/ustayready/fireprox" target="_blank">fireprox</a> (IP rotation proxy via AWS API gateway) that only uses one fireprox API for all EyeWitness targets.</li>
<li><a href="https://github.com/med0x2e/SigFlip" target="_blank">SigFlip</a> is a tool for patching authenticode signed PE files (exe, dll, sys, etc) without invalidating or breaking the existing signature. This looks particularly nasty and is used by APT 10.</li>
<li><a href="https://github.com/Tylous/SourcePoint" target="_blank">SourcePoint</a> is a C2 profile generator for Cobalt Strike command and control servers designed to ensure evasion. This tool was released along side the talk <a href="https://www.youtube.com/watch?v=JXKNdWUs77w" target="_blank">Operation Bypass Catch My Payload If You Can</a>.</li>
<li><a href="https://github.com/CCob/BeaconEye" target="_blank">BeaconEye</a> scans running processes for active CobaltStrike beacons. When processes are found to be running beacon, BeaconEye will monitor each process for C2 activity. Check out <a href="https://github.com/CCob/BeaconEye/blob/ed905c8b677a4e01f82737fc5545dbfc381e6c1c/BeaconEye.cs#L118" target="_blank">IsBeaconProcess</a> to make sure your beacon wouldn't get picked up.</li>
<li><a href="https://github.com/jacob-baines/concealed_position" target="_blank">concealed_position</a> is a local privilege escalation attack against Windows using the concept of "Bring Your Own Vulnerability". Specifically, Concealed Position (CP) uses the as designed package point and print logic in Windows that allows a low privilege user to stage and install printer drivers. CP specifically installs drivers with known vulnerabilities which are then exploited to escalate to SYSTEM. Concealed Position was first presented at <a href="https://www.youtube.com/watch?v=vdesswZYz-8" target="_blank">DEF CON 29</a>.</li>
<li><a href="https://github.com/hakluke/haklistgen" target="_blank">haklistgen</a> is a tool that turns any junk text into a usable wordlist for brute-forcing (subdomains, words in HTTP response, etc).</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/zodiacon/RegExp" target="_blank">RegExp</a> is a replacement for the Windows built-in Regedit.exe tool. Improvements over that tool includes many enhanced features.</li>
<li><a href="https://github.com/Fahrj/reverse-ssh#requirements" target="_blank">reverse-ssh</a> is a A statically-linked ssh server with a reverse connection feature for simple yet powerful remote access.</li>
<li><a href="https://github.com/mosajjal/dnsmonster" target="_blank">dnsmonster</a> is a passive DNS collection and monitoring built with Golang, Clickhouse and Grafana. This is a scalable solution to do enterprise DNS monitoring.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
