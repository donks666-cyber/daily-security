Title: Last Week in Security (LWiS) - 2022-04-18
Date: 2022-04-18 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-04-18
Author: Erik
Summary: .NET execution with docx (<a href="https://twitter.com/danonit" target="_blank">@danonit</a>), AV evasion masterclass (<a href="https://twitter.com/_vivami" target="_blank">@_vivami</a>), Phisher's errors (<a href="https://twitter.com/Marco_Ramilli" target="_blank">@Marco_Ramilli</a>), global injection and hooking (<a href="https://twitter.com/m417z" target="_blank">@m417z</a>), custom transport protocols in Burp(<a href="https://twitter.com/pentagridsec" target="_blank">@pentagridsec</a>), advanced fuzzing (<a href="https://twitter.com/kasifdekel" target="_blank">@kasifdekel</a>), coercing NTLM authentication from SCCM (<a href="https://twitter.com/_Mayyhem" target="_blank">@_Mayyhem</a>), xss iframe traps (<a href="https://twitter.com/hoodoer" target="_blank">@hoodoer</a>), patchless AMSI bypass (<a href="https://twitter.com/_EthicalChaos_" target="_blank">@_EthicalChaos_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-04-11 to 2022-04-18.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://krebsonsecurity.com/2022/04/microsoft-patch-tuesday-april-2022-edition/" target="_blank">Microsoft Patch Tuesday, April 2022 Edition</a>. This was a big one: 120 security vulnerabilities in Windows, including a "wormable" RPC RCE <a href="https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-26809" target="_blank">CVE-2022-26809</a>.</li>
<li><a href="https://www.cisa.gov/uscert/ncas/alerts/aa22-103a" target="_blank">APT Cyber Tools Targeting ICS/SCADA Devices</a>. Some significant ICS/SCADA malware is on the loose. The use of a known-vulnerable driver for kernel code execution is a known tactic, but paired with the ICS capabilities described in this report can have serious physical world consequences. As always, vx-underground has the <a href="https://samples.vx-underground.org/APTs/2022/2022.04.13/Samples/" target="_blank">samples</a></li>
<li><a href="https://techcrunch.com/2022/04/18/web-scraping-legal-court/" target="_blank">Web scraping is legal, US appeals court reaffirms</a>. LinkedIn looses another round against scrapers. Public data is public, no matter how mad you get when someone accesses it in a way you don't like.</li>
<li><a href="https://github.blog/2022-04-12-git-security-vulnerability-announced/" target="_blank">Git security vulnerability announced</a>. On Windows, for example, an attacker could create <cite>C:.gitconfig</cite>, which would cause all git invocations that occur outside of a repository to read its configured values. The Git uninstaller for Windows also had an privilege escalation vulnerability (DLL hijack in <cite>C:WindowsTemp</cite>).</li>
<li><a href="https://blog.lightspin.io/aws-rds-critical-security-vulnerability" target="_blank">AWS RDS Vulnerability Leads to AWS Internal Service Credentials</a>. The cloud is just someone else's computer, and they don't always lock it down as much as they should (but probably much better than most IT departments could). Official AWS publication <a href="https://aws.amazon.com/security/security-bulletins/AWS-2022-004/" target="_blank">here</a>.</li>
<li><a href="https://www.vice.com/en/article/dyp9nk/fbi-doj-law-enforcement-seize-raidforums" target="_blank">Law Enforcement Seizes RaidForums, One of the Most Important Hacking Sites</a>. One of the most important hacking sites? That might be a reach.</li>
<li><a href="https://www.zerodayinitiative.com/blog/2022/4/14/p2omiami-2022-schedule" target="_blank">Pwn2Own Miami 2022 Schedule</a>. Looks like some good stuff on the docket if you are into ICS pwnage.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://vanmieghem.io/blueprint-for-evading-edr-in-2022/" target="_blank">A blueprint for evading industry leading endpoint protection in 2022</a>. Tons of gold in this post. Do not skip.</li>
<li><a href="https://marcoramilli.com/2022/04/14/from-a-phishing-page-to-a-possible-threat-actor/" target="_blank">From a Phishing Page to a Possible Threat Actor</a>. "Cyber attackers are humans. Humans make mistakes or let behind actions details that could be used to trace them." The phishing site to  creator's mirror selfie trip proves that nicely.</li>
<li><a href="https://m417z.com/Implementing-Global-Injection-and-Hooking-in-Windows/" target="_blank">Implementing Global Injection and Hooking in Windows</a>. The technical bits to this are very cool, and the code for the injection can be found <a href="https://github.com/m417z/global-inject-demo" target="_blank">here</a>. Want to be able to hook any function of any process? Why not just inject a DLL into <em>every</em> process? Bold.</li>
<li><a href="https://www.pentagrid.ch/de/blog/teaching_burp_a_new_http_transport_encoding/" target="_blank">Teaching Burp a new HTTP Transport Encoding</a>. If you ever need to implement a custom transport encoding scheme for a Burp extension, this blog will save you a lot of time. Code <a href="https://github.com/pentagridsec/PentagridBurpTransportEncoding" target="_blank">here</a>.</li>
<li><a href="https://googleprojectzero.blogspot.com/2022/04/cve-2021-1782-ios-in-wild-vulnerability.html" target="_blank">CVE-2021-1782, an iOS in-the-wild vulnerability in vouchers</a>. If you're hungry for deeply technical iOS vulnerability write ups, Ian Beer has you covered.</li>
<li><a href="https://www.sentinelone.com/labs/inside-the-black-box-how-we-fuzzed-microsoft-defender-for-iot-and-found-multiple-vulnerabilities/" target="_blank">Inside the Black Box | How We Fuzzed Microsoft Defender for IoT and Found Multiple Vulnerabilities</a>. Some cool advanced fuzzing techniques in play in this post.</li>
<li><a href="https://posts.specterops.io/coercing-ntlm-authentication-from-sccm-e6e23ea8260a" target="_blank">Coercing NTLM Authentication from SCCM</a>. Authentication coercion attacks are all the rage, and now you can get some sweet hashes from SCCM. <a href="https://github.com/Mayyhem/SharpSCCM" target="_blank">SharpSCCM</a> will help you get what you need.</li>
<li><a href="https://www.trustedsec.com/blog/persisting-xss-with-iframe-traps/" target="_blank">Persisting XSS With IFrame Traps</a>. Users navigate away from your XSS payload too quickly? Using an "iframe trap" you can manipulate the address bar and get your victim to stick around long enough for your payload to complete, or even enter credentials on your xss-loaded site!</li>
<li><a href="https://ethicalchaos.dev/2022/04/17/in-process-patchless-amsi-bypass/" target="_blank">In-Process Patchless AMSI Bypass</a>. Using exceptions to patch amsi.dll's AmsiScanBuffer function. Very cleaver. This will make one of my favorite tools (<a href="https://github.com/CCob/BOF.NET" target="_blank">BOF.NET</a>) even more powerful. Example C code <a href="https://gist.github.com/CCob/fe3b63d80890fafeca982f76c8a3efdf" target="_blank">here</a>.</li>
<li><a href="https://rhinosecuritylabs.com/aws/cve-2022-25165-aws-vpn-client/" target="_blank">CVE-2022-25165: Privilege Escalation to SYSTEM in AWS VPN Client</a>. Time-of-check-time-of-use (TOCTOU) hits the AWS VPN client (patched in 3.0.0) and allows for arbitrary file overwrite as SYSTEM.</li>
<li><a href="https://blog.assetnote.io/2022/04/13/watchguard-firebox-rce/" target="_blank">Diving Deeper into WatchGuard Pre-Auth RCE - CVE-2022-26318</a>. This is a cool look at a leaked exploit and the work needed to really understand how it works and how it can be modified.</li>
<li><a href="https://medium.com/@airlockdigital/make-phishing-great-again-vsto-office-files-are-the-new-macro-nightmare-e09fcadef010" target="_blank">Make phishing great again. VSTO office files are the new macro nightmare?</a>. There are some caveats, but executing .NET code from the internet with just a docx is crazy. Microsoft Office truly has way too many features that 99.9% of people never use, but attackers will happily leverage for shells.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/pwn1sher/frostbyte" target="_blank">frostbyte</a> is a POC project that combines different defense evasion techniques to build better redteam payloads.</li>
<li><a href="https://github.com/puzzlepeaches/msprobe" target="_blank">msprobe</a> is a tool for finding all things on-prem Microsoft products for password spraying and enumeration.</li>
<li><a href="https://github.com/grigoritchy/pocs/tree/main/windows/spooler-splenumforms-iov" target="_blank">spooler-splenumforms-iov</a> is a memory corruption vulnerability in windows spooler service that was patched on most recent Microsoft Patch Tuesday, 2022-04-12.</li>
<li><a href="https://github.com/daem0nc0re/SharpWnfSuite#sharpwnfscan" target="_blank">SharpWnfScan</a> dumps Windows Notification Facility subscription information from process.</li>
<li><a href="https://github.com/firefart/stunner/" target="_blank">stunner</a> is a tool to test and exploit STUN, TURN and TURN over TCP servers.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/RyanJarv/cdn-proxy" target="_blank">cdn-proxy</a> is a tool that can be used by web app pentesters to create a copy of a targeted website with CDN and WAF restrictions disabled.</li>
<li><a href="https://github.com/soteria-security/ADInspect" target="_blank">ADInspect</a> is a PowerShell script that automates the security assessment of Microsoft Active Directory environments.</li>
<li><a href="https://github.com/trailofbits/maat" target="_blank">maat</a> is an open-source symbolic execution framework. Bonus, the <a href="https://maat.re/" target="_blank">project's site</a> uses m.css like this blog!</li>
<li><a href="https://github.com/kazet/wpgarlic" target="_blank">wpgarlic</a> is a proof-of-concept WordPress plugin fuzzer.</li>
<li><a href="https://github.com/fyoorer/ShadowClone" target="_blank">ShadowClone</a> - Unleash the power of cloud. Distribute your long running tasks dynamically across thousands of serverless functions and gives you the results within seconds where it would have taken hours to complete.</li>
<li><a href="https://github.com/optionalCTF/SSOh-No" target="_blank">SSOh-No</a> is a tool for user enumeration and password spraying tool for testing Azure AD.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 415 (+0)</p>
<p>Blogs monitored: 304 (+2)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
