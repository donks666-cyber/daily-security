Title: Last Week in Security (LWiS) - 2024-10-07
Date: 2024-10-07 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-10-07
Author: Erik
Summary: I-XRAY doxxing 🕶️ (<a href="https://x.com/AnhPhuNguyen1" target="_blank">@AnhPhuNguyen1</a> + <a href="https://x.com/CaineArdayfio" target="_blank">@CaineArdayfio</a>), TeamViewer LPE (<a href="https://x.com/PedroGabaldon" target="_blank">@PedroGabaldon</a>), C# source generators (<a href="https://x.com/DragoQcc" target="_blank">@DragoQcc</a>), ⏲️-based user enum (<a href="https://x.com/nyxgeek" target="_blank">@nyxgeek</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-09-30 to 2024-10-07.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://docs.google.com/document/d/1iWCqmaOUKhKjcKSktIwC3NNANoFP7vPsRvcbOIup_BA/preview" target="_blank">[Google Doc] I-XRAY: The AI Glasses That Reveal Anyone's Personal Details—Home Address, Name, Phone Number, and More—Just from Looking at Them</a> - Meta's smart glasses live stream their view to Insagram, where the feed is scraped for faces, those are reverse image searched and enhanced with web searches and fed back to an app. Near instant, automatic doxxing. <a href="https://www.youtube.com/watch?v=gHrSXe1cElI" target="_blank">Video demo</a>. At least COVID normalized wearing masks in public?</li>
<li><a href="https://blog.cloudflare.com/how-cloudflare-auto-mitigated-world-record-3-8-tbps-ddos-attack/" target="_blank">How Cloudflare auto-mitigated world record 3.8 Tbps DDoS attack</a> - A recent authentication bypass vulnerability in ASUS routers likely led to the record setting distributed denial of service attack.</li>
<li><a href="https://arstechnica.com/ai/2024/09/california-governor-vetoes-controversial-ai-safety-bill/" target="_blank">California governor vetoes controversial AI safety bill</a> - The governor claims the bill did not take into account "smaller, specialized models," thus potentially giving a win to both sides. Those who think the bill didn't go far enough can try again, and those who want less regulation have it for now. Perhaps the governor just knows where his state's <a href="https://laist.com/news/a-mystery-surge-in-california-tax-revenue-points-to-tech-companies-like-nvidia-heres-why" target="_blank">dollars come from</a>...</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.lexfo.fr/StealC_malware_analysis_part1.html" target="_blank">StealC Malware Analysis</a> - A three part series on reverse engineering a Windows malware sample from the StealC family, starting with the packed sample all the way to the recovery of all stages of the C2.</li>
<li><a href="https://pgj11.com/posts/Finding-TeamViewer-0days-Part-1/" target="_blank">Finding TeamViewer 0days</a> - Another three part series on finding a local priviledge escalation vulnerability in TeamView for Windows. <a href="https://pgj11.com/posts/Finding-TeamViewer-0days-Part-2/" target="_blank">Part II</a>, <a href="https://pgj11.com/posts/Finding-TeamViewer-0days-Part-3/" target="_blank">Part III</a>, and <a href="https://github.com/PeterGabaldon/CVE-2024-7479_CVE-2024-7481" target="_blank">the PoC</a>, are up as well.</li>
<li><a href="https://www.elttam.com/blog/monocle-on-chronicles/" target="_blank">A Monocle On Chronicles - Using Talkback Chronicles, and introducing a new Newsletter.</a> - If you're reading LWiS you might enjoy this infosec news aggregator. While LWiS is 100% human curated and written, talkback is fully automated.</li>
<li><a href="https://itm4n.github.io/printnightmare-not-over/" target="_blank">The PrintNightmare is not Over Yet</a> - Many "mitigations" to PrintNightmare are not enough to stop attackers who can use techniques like DNS spoofing to accomplish attacks. “There is no combination of mitigations that is equivalent to setting Restrict Driver Installation To Administrators to 1.”</li>
<li><a href="https://posts.specterops.io/dotnet-source-generators-in-2024-part-1-getting-started-76d619b633f5" target="_blank">Dotnet Source Generators in 2024 Part 1: Getting Started</a> - "Source generators in .NET enable you to inspect user code and generate additional code on the fly based on that analysis. [...] you can generate hundreds of lines of code, helping to reduce boilerplate and repetitive code across your projects.""</li>
<li><a href="https://www.elastic.co/pdf/elastic-global-threat-report-2024" target="_blank">Global Threat Report</a> - Elastic security labs gives their take and visibility into modern attacks. A lot of linux tradecraft explained which isn't very common in similar reports. Pretty cool.</li>
<li><a href="https://trustedsec.com/blog/kicking-it-old-school-with-time-based-enumeration-in-azure" target="_blank">Kicking it Old-School with Time-Based Enumeration in Azure</a> - <a href="https://x.com/nyxgeek" target="_blank">@nyxgeek</a> is rolling back the clock with this one. Another user-enumeration method via the Basic Authentication time-based abuse.</li>
<li><a href="https://permiso.io/blog/exploiting-hosted-models" target="_blank">When AI Gets Hijacked: Exploiting Hosted Models for Dark Roleplaying</a> - It's always the fundamentals. How hijacked access keys can lead to the demise of your fancy AI application.</li>
<li><a href="https://www.huntress.com/blog/hunting-for-m365-password-spraying" target="_blank">Hunting for M365 Password Spraying</a> - For the defenders, this is almost a baseline tier detection at this point. Using AWS API Gateway, Github, and other third-parties is becoming standard password spraying tradecraft. Once you identify it, what are your next steps?</li>
<li><a href="https://www.r-tec.net/r-tec-blog-axis-camera-app-takeover.html" target="_blank">Axis Camera APP takeover</a> - The r-tec team saw this on a pentest and the PoC was no bueno so they decided to make it better and showcase impact to the client. Love to see it. Persisting in cameras/printers could be fruitful in most environments.</li>
<li><a href="https://www.fitretech.com/blog/paranoia" target="_blank">PARAnoia</a> - How physical compromise can lead to compromising a domain-joined machine. Not 100% sure the conditions are easy to replicate but you decide as the reader. "Physical Access is Root Access".</li>
<li><a href="https://blog.projectdiscovery.io/ruby-saml-gitlab-auth-bypass/" target="_blank">Ruby-SAML / GitLab Authentication Bypass (CVE-2024-45409)</a> - PD with the Nuclei template for this 10.0. An unauthenticated attacker with access to any signed saml document (by the IdP) can thus forge a SAML Response/Assertion with arbitrary contents.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/gergelykalman/fs_usage_ng" target="_blank">fs_usage_ng</a> - An attempt to make the fs_usage tool from Apple work better for my filesystem research.</li>
<li><a href="https://github.com/mbog14/CVE-2024-44193" target="_blank">CVE-2024-44193</a> - Hacking Windows through iTunes - Local Privilege Escalation 0-day.</li>
<li><a href="https://github.com/vectra-ai-research/Halberd" target="_blank">Halberd</a> - Halberd : Multi-Cloud Security Testing Tool to execute a comprehensive array of attack techniques across multiple surfaces via a simple web interface.</li>
<li><a href="https://github.com/attacksurge/ax" target="_blank">ax</a> - AXIOM is out. AX is in. Control Your Infrastructure, Scale Your Scanning—On Your Terms. Easily distribute arbitrary binaries and scripts using any of our seven supported cloud providers.</li>
<li><a href="https://github.com/googleprojectzero/SockFuzzer" target="_blank">SockFuzzer</a> - SockFuzzer, originally designed as a networking-focused fuzzer for the XNU kernel (used in macOS and iOS), has evolved into a comprehensive kernel fuzzing framework.</li>
<li><a href="https://github.com/safedv/RustiveDump" target="_blank">RustiveDump</a> - LSASS memory dumper using only NTAPIs, creating a minimal minidump, built in Rust with no_std and independent of the C runtime (CRT). It supports XOR encryption and remote file transmission.</li>
<li><a href="https://github.com/Friends-Security/SharpExclusionFinder" target="_blank">SharpExclusionFinder</a> - Tool designed to find folder exclusions using Windows Defender using command line utility MpCmdRun.exe as a low privileged user, without relying on event logs.</li>
<li><a href="https://github.com/mlcsec/EDRenum-BOF" target="_blank">EDRenum-BOF</a> - Identify common EDR processes, directories, and services. Simple BOF of Invoke-EDRChecker.</li>
<li><a href="https://github.com/decoder-it/KrbRelay-SMBServer" target="_blank">KrbRelay-SMBServer</a> - This krbrelay version acts as an SMB server (instead of DCOM) to relay Kerberos AP-REQ to CIFS or HTTP. It's 90% based on @cube0x0's KrbRelay</li>
<li><a href="https://github.com/SpecterOps/cred1py" target="_blank">cred1py</a> - A Python POC for CRED1 over SOCKS5. Test it out in your <a href="https://docs.ludus.cloud/docs/environment-guides/sccm" target="_blank">Ludus SCCM Lab</a>.</li>
<li><a href="https://github.com/H4NM/WhoYouCalling" target="_blank">WhoYouCalling</a> - Records an executable's network activity into a Full Packet Capture file (.pcap) and much more.</li>
<li><a href="https://github.com/Teach2Breach/noldr" target="_blank">noldr</a> - Dynamically resolve API function addresses at runtime in a secure manner.</li>
<li><a href="https://www.netexec.wiki/nfs-protocol/enumeration" target="_blank">Netexec gain NFS support</a> - A whole new world of share enumeration and looting just opened up.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/synacktiv/AADOutsider-py" target="_blank">AADOutsider-py</a> - Python3 rewrite of AsOutsider features of AADInternals.</li>
<li><a href="https://github.com/MrGlockenspiel/activate-linux" target="_blank">activate-linux</a> - The "Activate Windows" watermark ported to Linux.</li>
<li><a href="https://github.com/freedomofpress/dangerzone" target="_blank">dangerzone</a> - Take potentially dangerous PDFs, office documents, or images and convert them to safe PDFs.</li>
<li><a href="https://www.merklemap.com/" target="_blank">Merklemap</a> - Subdomain Search Engine: Uncover and Explore Subdomains with Ease.</li>
<li><a href="https://github.com/evild3ad/MemProcFS-Analyzer" target="_blank">MemProcFS-Analyzer</a> - MemProcFS-Analyzer - Automated Forensic Analysis of Windows Memory Dumps for DFIR.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 439 (+1)</p>
<p>Blogs monitored: 396 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
