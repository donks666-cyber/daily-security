Title: Last Week in Security (LWiS) - 2022-10-31
Date: 2022-10-31 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-10-31
Author: Erik
Summary: 🎃 Spooky (forthcoming) OpenSSL 3 critical vuln, RC4 fun (<a href="https://twitter.com/tiraniddo" target="_blank">@tiraniddo</a>), Autodial DLL techniques (<a href="https://twitter.com/TheXC3LL" target="_blank">@TheXC3LL</a>), token leak abuse via webshell (<a href="https://twitter.com/_Kudaes_" target="_blank">@_Kudaes_</a>), Open-Obfuscator (<a href="https://twitter.com/rh0main" target="_blank">@rh0main</a>), more exchange pwnage from 🍊 (<a href="https://twitter.com/orange_8361" target="_blank">@orange_8361</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-10-17 to 2022-10-31.</p>
<p>This week I reviewed 368 blog posts and 2213 tweets to find only the best and most relevant items to include here.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://mta.openssl.org/pipermail/openssl-announce/2022-October/000238.html" target="_blank">Forthcoming OpenSSL Releases</a>. Behind this simple title is a spooky Halloween statement: "OpenSSL 3.0.7 is a security-fix release. The highest severity issue fixed in this release is CRITICAL." OpenSSL 3+ isn't that widespread yet, but this might be an interesting bug.</li>
<li><a href="https://blog.cloudflare.com/building-privacy-into-internet-standards-and-how-to-make-your-app-more-private-today/" target="_blank">Privacy Gateway: a privacy preserving proxy built on Internet standards</a>. Domain fronting/hiding just went legit. Currently the relay domains are unique to the applications (and thus not useful for censor evasion) but there is no technical reason that has to remain the case. Check out the first implementation <a href="https://www.documentcloud.org/documents/22349375-flo-white-paper" target="_blank">here</a>. Keep in mind with this Cloudflare positions itself to collect that delicious metadata (although they seem to be actively trying to actually "don't be evil" - hopefully that continues).</li>
<li><a href="https://research.nccgroup.com/2022/10/31/check-out-our-new-microcorruption-challenges/" target="_blank">Check out our new Microcorruption challenges!</a>. Excellent embedded security CTF!</li>
<li><a href="https://chromereleases.googleblog.com/2022/10/stable-channel-update-for-desktop_27.html" target="_blank">Stable Channel Update for Desktop</a>. A good reminder to stay on top of your Chrome updates. Or use Firefox developer edition to break all the ROP gadgets.</li>
<li><a href="https://arstechnica.com/gadgets/2022/10/apple-clarifies-security-update-policy-only-the-latest-oses-are-fully-patched/" target="_blank">Apple clarifies security update policy: Only the latest OSes are fully patched</a>. Apple going full opposite of the "still supports 16 bit DOS applications from 1993" stance of Microsoft and only fully patching the latest OS they release. Enterprises that use macOS can't be pleased by this, as even with developer betas there may be issues with production workflows on the latest OS version for some time after release. Hardware than can't be upgrade is now forever vulnerable? 2017 MacBook Pros are unable to be updated and aren't <em>that</em> old...</li>
<li><a href="https://twitter.com/markrussinovich/status/1585415828979462144" target="_blank">It's here: Dark Mode Process Explorer!</a></li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://red.0xbad53c.com/red-team-operations/initial-access/macro-attacks/binary-file-write-via-microsoft-speech-api" target="_blank">Binary File Write via Microsoft Speech API</a>. It's tricky to write files from macros in 2022 without Defender or other AV getting unhappy. This lesser known API has the ability to write binaries, which is a very useful primitive for a maldoc.</li>
<li><a href="https://googleprojectzero.blogspot.com/2022/10/rc4-is-still-considered-harmful.html" target="_blank">RC4 Is Still Considered Harmful</a>. Kerberos continues to be an issue for enterprises, and "just turn off X" is never that simple. Consider turning on <a href="https://syfuhs.net/kerberos-fast-armoring" target="_blank">FAST</a> though (and disable RC4 if you can).</li>
<li><a href="https://www.mdsec.co.uk/2022/10/autodialdlling-your-way/" target="_blank">Autodial(DLL)ing Your Way</a>. The Winsock2 registry is used by anything that makes a network connection and thus is a good spot for persistence, lateral movement, and even credential dumping via SSP loads. Code <a href="https://github.com/mdsecactivebreach/DragonCastle" target="_blank">here</a>.</li>
<li><a href="https://www.praetorian.com/blog/self-hosted-github-runners-are-backdoors/" target="_blank">From Self-Hosted GitHub Runner to Self-Hosted Backdoor</a>. CI/CD compromise is scary because it not only affects your organization but potentially everyone who uses the product being build by that CI/CD pipeline.</li>
<li><a href="https://www.tarlogic.com/blog/token-handles-abuse-one-shell-to-handle-them-all/" target="_blank">One shell to HANDLE them all</a>. A webshell that can abuse leaked user token handles? Sign me up.</li>
<li><a href="https://octagon.net/blog/2022/10/28/juniper-sslvpn-junos-rce-and-multiple-vulnerabilities/" target="_blank">Juniper SSLVPN / JunOS RCE and Multiple Vulnerabilities</a>. Can we please go more than a week without an unauth RCE in a major SSL VPN? Zero trust can't come fast enough. Or things like <a href="https://srcincite.io/blog/2022/10/25/eat-what-you-kill-pre-authenticated-rce-in-vmware-nsx-manager.html" target="_blank">Pre-authenticated Remote Code Execution in VMWare NSX Manager</a>?</li>
<li><a href="https://h0mbre.github.io/PAWNYABLE_UAF_Walkthrough/#" target="_blank">PAWNYABLE UAF Walkthrough (Holstein v3)</a>. Some good technical binary exploitation content.</li>
<li><a href="https://blog.nviso.eu/2022/10/25/the-dangers-of-trust-policies-in-aws/" target="_blank">The dangers of trust policies in AWS</a>. The cloud is built on trust, so understanding best policies for trust policies is critical.</li>
<li><a href="https://blog.orange.tw/2022/10/proxyrelay-a-new-attack-surface-on-ms-exchange-part-4.html" target="_blank">A New Attack Surface on MS Exchange Part 4 - ProxyRelay!</a>. If you're still running on-prem exchange... stop it. If you email is too sensitive to trust to a cloud provider, it certainly shouldn't be in the swiss cheese that is Exchange.</li>
<li><a href="https://www.zscaler.com/blogs/security-research/technical-analysis-windows-clfs-zero-day-vulnerability-cve-2022-37969-part2-exploit-analysis" target="_blank">Technical Analysis of Windows CLFS Zero-Day Vulnerability CVE-2022-37969 - Part 2: Exploit Analysis</a>. More details on the Windows local privilege escalation vulnerability.</li>
<li><a href="https://rastamouse.me/getdomain-vs-getcomputerdomain-vs-getcurrentdomain/" target="_blank">GetDomain vs GetComputerDomain vs GetCurrentDomain</a>. If you're in a network with complicated trust relationships or multiple forests, its a good idea to test your tools to make sure they are acting on the objects you expect!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/guacsec/guac" target="_blank">guac</a> aggregates software security metadata into a high fidelity graph database.</li>
<li><a href="https://www.romainthomas.fr/post/22-10-open-obfuscator/" target="_blank">Open-Obfuscator: A free and open-source obfuscator for mobile applications</a>. A free and open-source solution for obfuscating mobile applications. Also some of the best looking docs I've seen in a long time.</li>
<li><a href="https://portswigger.net/blog/free-dastardly-from-burp-suite" target="_blank">Free: Dastardly from Burp Suite</a> is a free, lightweight web application security scanner for your CI/CD pipeline, from the makers of Burp Suite.</li>
<li><a href="https://github.com/ORCx41/TerraLdr" target="_blank">TerraLdr</a> - Payload Loader Designed With Advanced Evasion Features.</li>
<li><a href="https://github.com/MrAle98/BOF-herpaderping" target="_blank">BOF-herpaderping</a> - Beacon Object File partial implementation of process herpaderping technique.</li>
<li><a href="https://github.com/Accenture/Spartacus" target="_blank">Spartacus</a>  - DLL Hijacking Discovery Tool.</li>
<li><a href="https://github.com/liamg/siphon" target="_blank">siphon</a> ⚗️ Intercept stdin/stdout/stderr for any process.</li>
<li><a href="https://github.com/rasta-mouse/SharpC2" target="_blank">SharpC2</a>. This looks to be a rewrite/less featured version of Rastamouse's collab with xpn that was also called SharpC2 (now pulled from GitHub)?</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/jsa2/caOptics" target="_blank">caOptics</a> - Azure AD Conditional Access gap analyzer</li>
<li><a href="https://github.com/Idov31/Sandman" target="_blank">Sandman</a> is a NTP based backdoor for red team engagements in hardened networks.</li>
<li><a href="https://github.com/tishion/potto" target="_blank">potto</a> A minimum cross-platform implementation of COM (Component Object Model), DI/IOC framework.</li>
<li><a href="https://github.com/charmbracelet/vhs" target="_blank">vhs</a> Your CLI home video recorder 📼</li>
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
