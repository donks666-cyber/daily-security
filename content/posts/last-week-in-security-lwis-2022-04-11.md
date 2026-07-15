Title: Last Week in Security (LWiS) - 2022-04-11
Date: 2022-04-11 23:54
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-04-11
Author: Erik
Summary: Full Edge exploit (<a href="https://twitter.com/33y0re" target="_blank">@33y0re</a>), dynamic P/Invoke (<a href="https://twitter.com/bohops" target="_blank">@bohops</a>), Veeam exploits (<a href="https://twitter.com/SinSinology" target="_blank">@SinSinology</a>), macOS LPE (<a href="https://twitter.com/patch1t" target="_blank">@patch1t</a>), AV debugger (<a href="https://twitter.com/plowsec" target="_blank">@PlowSec</a>), SMB over QUIC (<a href="https://twitter.com/_xpn_/" target="_blank">@_xpn_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-04-04 to 2022-04-11.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2022/04/improving-software-supply-chain.html" target="_blank">Improving software supply chain security with tamper-proof builds</a>. As there is more pressure to secure the software supply chain, solutions like this will hopefully become more popular. Having to rely on GitHub's hosted runner is a downside I hope can be addressed.</li>
<li><a href="https://content.vectra.ai/rs/748-MCE-447/images/EBook_Security_Leaders_Research.pdf" target="_blank">[PDF] Breaking Point: Is mounting pressure creating a ticking time bomb for a health crisis in cybersecurity?</a>. Sample size of only 200, but perhaps some insight here. I wonder if the kind of people drawn to information security are pre-disposed to mental health issues or if the job is more to blame (a bit of nature vs nurture I suppose).</li>
<li><a href="https://success.trendmicro.com/dcx/s/solution/000290678?language=en_US" target="_blank">IMPORTANT SECURITY BULLETIN: Trend Micro Apex Central Arbitrary File Upload Remote Code Execution (RCE) Vulnerability</a>. Not that noteworthy except that remote, unauthenticated RCE in a security product is always rough. The active in-the-wild exploitation is the cherry on top.</li>
<li><a href="https://www.state.gov/establishment-of-the-bureau-of-cyberspace-and-digital-policy/" target="_blank">Establishment of the Bureau of Cyberspace and Digital Policy</a>. Light on details, but a "Digital Freedom Coordinator" at least <em>sounds</em> good?</li>
<li><a href="https://www.microsoft.com/security/blog/2022/04/05/new-security-features-for-windows-11-will-help-protect-hybrid-work/" target="_blank">New security features for Windows 11 will help protect hybrid work</a>. Some interesting new defaults coming to Windows 11 that will make the OS more secure by default, but also feed more data into the "AI model for application trust within the Microsoft cloud."</li>
<li><a href="https://github.com/AgainstTheWest/NginxDay" target="_blank">NginxDay</a> - Nginx 18.1 04/09/22 zero-day repo (no code). I'll hold judgement until code is released. This could be a ruse.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://connormcgarr.github.io/type-confusion-part-3/" target="_blank">Exploit Development: Browser Exploitation on Windows - CVE-2019-0567, A Microsoft Edge Type Confusion Vulnerability (Part 3)</a>. This series has been a treat. No one else I know of is putting together, detailed, well written, fully documented, modern exploit walk-throughs with DEP, ASLR, CFG, ACG, CIG, and no-child process mitigation bypasses. This is a SANS SEC760 course for free. Great work Connor!</li>
<li><a href="https://googleprojectzero.blogspot.com/2022/04/cve-2021-30737-xerubs-2021-ios-asn1.html" target="_blank">CVE-2021-30737, @xerub's 2021 iOS ASN.1 Vulnerability</a>. This post explores the bug that was exploited to unlock the San Bernadino iPhone.</li>
<li><a href="https://bohops.com/2022/04/02/unmanaged-code-execution-with-net-dynamic-pinvoke/" target="_blank">Unmanaged Code Execution with .NET Dynamic PInvoke</a>. C# and P/Invoke have been the go-to solution after Powershell's advanced logging as introduced. This "dynamic" P/Invoke (note: not <a href="https://github.com/TheWover/DInvoke" target="_blank">DInvoke</a>) adds some stealth and different signatures to P/Invoke code.</li>
<li><a href="https://www.mdsec.co.uk/2022/03/abc-code-execution-for-veeam/" target="_blank">ABC-Code Execution for Veeam</a>. Veeam is a widely used enterprise backup solution, and recently patch a few bad bugs. We've detailed the remote RCE in LWiS-2022-03-14 and LWiS-2022-03-21, but this covers two additional vulnerabilities. This post is from 2022-03-29, but the MDSec scraper I have only just updated with it. MDSec please include an RSS/Atom feed with your blog!</li>
<li><a href="https://labs.nettitude.com/blog/repurposing-real-ttps-for-use-on-red-team-engagements/" target="_blank">Repurposing Real TTPs for use on Red Team Engagements</a>. The job of a good Adversary Simulation offering is to take real TTPs and expand/adapt them to give customers a realistic but unique look at an adversary. This post explains exactly how that was done for a Bleeding Bear attack. Code here: <a href="https://github.com/Allevon412/BreadBear" target="_blank">BreadBear</a>.</li>
<li><a href="https://www.trendmicro.com/en_us/research/22/d/macos-suhelper-root-privilege-escalation-vulnerability-a-deep-di.html" target="_blank">MacOS SUHelper Root Privilege Escalation Vulnerability: A Deep Dive Into CVE-2022-22639</a>. A nice LPE for macOS (patched in 12.3). Code here: <a href="https://github.com/jhftss/CVE-2022-22639" target="_blank">CVE-2022-22639</a>.</li>
<li><a href="https://blog.scrt.ch/2022/04/05/automatically-extracting-static-antivirus-signatures/" target="_blank">Automatically extracting static antivirus signatures</a>. The idea of an automated "AV debugger" isn't 100% novel (see: <a href="https://github.com/rasta-mouse/ThreatCheck" target="_blank">ThreatCheck</a>), but this certainly goes a step further. <a href="https://github.com/scrt/avdebugger" target="_blank">avdebugger</a> has the code.</li>
<li><a href="https://www.trustedsec.com/blog/making-smb-accessible-with-ntlmquic/" target="_blank">Making SMB Accessible with NTLMquic</a>. SMB over QUIC support is included in Windows 11 and Server 2022. On Windows 11, it's enabled by default and will be attempted if normal TCP/445 fails. This might allow some authentication elicitation from restricted networks that allow QUIC out. <a href="https://youtu.be/rgGgFloZbJ0" target="_blank">Demo</a> and <a href="https://github.com/xpn/ntlmquic" target="_blank">code</a> are up.</li>
<li><a href="https://www.x86matthew.com/view_post?id=import_dll_injection" target="_blank">ImportDLLInjection - An alternative method of injecting DLLs by modifying PE headers in memory</a>. What if you simply replace the entire IMAGE_NT_HEADERS structure in a spawned process to include your DLL in the import descriptor list? This post does that and the spawned process will import the DLL!</li>
<li><a href="https://vollragm.github.io/posts/abusing-large-page-drivers/" target="_blank">Abusing LargePageDrivers to copy shellcode into valid kernel modules</a>. Once again the game cheat community is leading the charge with kernel exploit development.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Wra7h/ARCInject" target="_blank">ARCInject</a> can overwrite a process's recovery callback and execute with WER.</li>
<li><a href="https://github.com/ferreiraklet/Jeeves" target="_blank">Jeeves</a> is made for looking to Time-Based Blind SQLInjection through recon.</li>
<li><a href="https://github.com/ekzhang/bore" target="_blank">bore</a> is a simple CLI tool for making tunnels to localhost.</li>
<li><a href="https://github.com/NextronSystems/ransomware-simulator" target="_blank">ransomware-simulator</a> is a ransomware simulator written in Golang.</li>
<li><a href="https://github.com/slyd0g/SwiftInMemoryLoading" target="_blank">SwiftInMemoryLoading</a> is a Swift implementation of in-memory Mach-O loading on macOS. Blog post soon?</li>
<li><a href="https://github.com/nayjones/inflate.py" target="_blank">inflate.py</a> artificially inflate a given binary to exceed common EDR file size limits. Can be used to bypass common EDR.</li>
<li><a href="https://github.com/mdsecactivebreach/com_inject" target="_blank">com_inject</a> performs process injection via Component Object Model (COM) IRundown::DoCallback(). Blog post <a href="https://www.mdsec.co.uk/2022/04/process-injection-via-component-object-model-com-irundowndocallback/" target="_blank">here</a>.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/shellfarmer/WeakestLink" target="_blank">WeakestLink</a> is a browser extension that extracts users from LinkedIn company pages.</li>
<li><a href="https://github.com/projectdiscovery/uncover" target="_blank">uncover</a> quickly discovers exposed hosts on the internet using multiple search engines.</li>
<li><a href="https://github.com/3nock/sub3suite" target="_blank">sub3suite</a> is a research-grade suite of tools for Subdomain Enumeration, OSINT Information gathering &amp; Attack Surface Mapping that supports both manual and automated analysis on variety of target types with many available features &amp; tools.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 415 (+2)</p>
<p>Blogs monitored: 302 (+5)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
