Title: Last Week in Security (LWiS) - 2021-05-17
Date: 2021-05-18 19:45
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-05-17
Author: Erik
Summary: Exim RCE (<a href="https://twitter.com/lockedbyte" target="_blank">@lockedbyte</a>), Windows kernel exploit writeup (<a href="https://twitter.com/33y0re" target="_blank">@33y0re</a>), plaintext RDP creds from memory (<a href="https://twitter.com/jonasLyk" target="_blank">@jonasLyk</a>, <a href="https://twitter.com/n00py1" target="_blank">@n00py1</a>), MS Defender ATP bypasses (<a href="https://twitter.com/Tyl0us" target="_blank">@Tyl0us</a>), hashcat 6.2.0 (<a href="https://twitter.com/hashcat" target="_blank">@hashcat</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-05-10 to 2021-05-17.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://blog.cloudflare.com/introducing-cryptographic-attestation-of-personhood/" target="_blank">Humanity wastes about 500 years per day on CAPTCHAs. It’s time to end this madness</a>. Cloudflare sets out to end CAPTCHAs and replace them with hardware tokens - which are increasingly built into modern computing devices.</li>
<li><a href="https://fingerprintjs.com/blog/external-protocol-flooding/" target="_blank">Exploiting custom protocol handlers for cross-browser tracking in Tor, Safari, Chrome and Firefox</a>. "Scheme flooding" is a new technique that uses custom URL schemes to fingerprint your computer across browsers (even Tor browser). Check out the <a href="https://github.com/fingerprintjs/external-protocol-flooding" target="_blank">code</a> and <a href="https://schemeflood.com/" target="_blank">demo site</a>.</li>
<li><a href="https://posts.specterops.io/bloodhound-enterprise-vs-bloodhound-open-sourc-e4fe55594359" target="_blank">BloodHound Enterprise vs. BloodHound Open-Source</a>. The upcoming Enterprise release of BloodHound shouldn't change anything for the open source version, and will provide lots of new features. What are the odds that a signed BloodHound Enterprise binary is allowed by major EDR vendors?</li>
<li><a href="https://hashcat.net/forum/thread-10103.html" target="_blank">Hashcat v6.2.0 Released</a>. The latest hashcat adds 26 new hash modes, a new attack mode for single GPUs, new features and bug fixes.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://www.blackarrow.net/leveraging-microsoft-teams-to-persist-and-cover-up-cobalt-strike-traffic/" target="_blank">Leveraging Microsoft Teams to persist and cover up Cobalt Strike traffic</a>. In the age of remote work, your target is likely running Teams. This post shows how to leverage a DLL hijack for persistence when Teams runs as well as the creation of a C2 profile to mimic Teams traffic. Despite Microsoft saying <a href="https://www.microsoft.com/security/blog/2021/03/26/securing-our-approach-to-domain-fronting-within-azure/" target="_blank">domain fronting is dead</a>, it hasn't been shut off on Azure quite yet, which allows your "Teams" traffic to front behind legitimate Microsoft domains.</li>
<li><a href="https://connormcgarr.github.io/cve-2020-21551-sploit/" target="_blank">Exploit Development: CVE-2021-21551 - Dell ‘dbutil_2_3.sys’ Kernel Exploit Writeup</a>. Posts like this are incredibly valuable for anyone looking to learn as they walk through the entire process from initial analysis to final PoC. Get the code <a href="https://github.com/connormcgarr/Kernel-Exploits/tree/master/CVE-2021-21551" target="_blank">here</a>. <a href="https://github.com/waldo-irc/CVE-2021-21551" target="_blank">Other PoCs</a> are starting to pop up as well.</li>
<li><a href="https://luemmelsec.github.io/Building-An-Evil-USB-Cable/" target="_blank">Evil Logitech - erm I ment USB cable</a>. Build your own hardware BadUSB cable with cheap parts and open source code.</li>
<li><a href="https://www.n00py.io/2021/05/dumping-plaintext-rdp-credentials-from-svchost-exe/" target="_blank">Dumping Plaintext RDP credentials from svchost.exe</a>. In some (inconsistent) cases, the svchost.exe that has rdpcorets.dll loaded stores the user's RDP password in memory in plain text. This post shows you what to dump, and what to search for to possibly get credentials. It looks like this will <a href="https://twitter.com/gentilkiwi/status/1393986751501307906" target="_blank">soon be a feature in mimikatz</a>.</li>
<li><a href="https://blog.whtaguy.com/2021/05/d-link-router-cve-2021-27342.html" target="_blank">D-Link Router CVE-2021-27342 Timing Side-Channel Attack Vulnerability Writeup</a>. By realizing that successful logins and incorrect logins varied wildly in the response time, credentials can be brute forced at high speed. Just because there is a delay for failure doesn't mean you can already try the next credential!</li>
<li><a href="https://www.mcafee.com/enterprise/en-us/assets/reports/rp-access-token-theft-manipulation-attacks.pdf" target="_blank">Technical Analysis of Access Token Theft and Manipulation</a>. This deck from McAfee's Advanced Threat Research group covers a lot of access token techniques.</li>
<li><a href="https://web.archive.org/web/20210511125449/https://taha.run/posts/1" target="_blank">Hacking a company and accessing the back-end files leading to RCE and a 4-digit bounty</a>. Note: original site down at the time of publishing. Inadvertent .git folders accessible lead to full compromise.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/lockedbyte/CVE-Exploits/tree/master/CVE-2020-28018" target="_blank">CVE-2020-28018</a> is one of the <a href="https://www.qualys.com/2021/05/04/21nails/21nails.txt" target="_blank">21Nails</a> Exim mail server vulnerabilities that combines a memory leak, arbitrary read primitive, and a write-what-where primitive to achieve arbitrary code execution. For details see <a href="https://adepts.of0x.cc/exim-cve-2020-28018/" target="_blank">From theory to practice: analysis and PoC development for CVE-2020-28018 (Use-After-Free in Exim)</a>.</li>
<li><a href="https://github.com/redcode-labs/Solaris" target="_blank">Solaris</a> is a LKM rootkit loader/dropper that lists available security mechanisms.</li>
<li><a href="https://github.com/jfmaes/SharpNukeEventLog" target="_blank">SharpNukeEventLog</a> nukes the event log using some epic dinvoke fu to suspend the threads of the event log process.</li>
<li><a href="https://github.com/mgeeky/RedWarden" target="_blank">RedWarden</a> is a Cobalt Strike C2 Reverse proxy that fends off Blue Teams, AVs, EDRs, scanners through packet inspection and malleable profile correlation.</li>
<li><a href="https://github.com/optiv/Dent" target="_blank">Dent</a> is a framework for creating COM-based bypasses utilizing vulnerabilities in Microsoft's Window's Defender Advanced Threat Protection (called Microsoft Defender for Endpoint this week) sensors. All the details are in <a href="https://www.optiv.com/insights/source-zero/blog/breaking-wdapt-rules-com" target="_blank">Breaking the (WDAPT) Rules with COM</a>.</li>
<li><a href="https://github.com/Unit221B/Russian" target="_blank">Russian</a> is a registry file that changes two keys that are checked by some malware to determine if you are using a Russian language keyboard. This should be an absolute last resort defense against ransomware, but is very easy to deploy.</li>
<li><a href="https://github.com/dsnezhkov/exclave" target="_blank">exclave</a> helps offload wrapping/unwrapping of offensive payloads with Intel SGX technology assist. This is an interesting project to protect C2 secrets using protected processor memory and Intel's secure enclave technology.</li>
<li><a href="https://github.com/CCob/dnMerge" target="_blank">dnMerge</a> is a lightweight .NET assembly dependency merger that uses dnLib and 7zip's LZMA SDK for compressing dependant assemblies.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/dandavison/delta#installation" target="_blank">delta</a> aims to make time studying diffs both efficient and enjoyable: it allows you to make extensive changes to the layout and styling of diffs, as well as allowing you to stay arbitrarily close to the default git/diff output.</li>
<li><a href="https://github.com/Accenture/jenkins-attack-framework" target="_blank">jenkins-attack-framework</a> is a project to help assess the popular CI/CD product Jenkins.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
<p>This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
