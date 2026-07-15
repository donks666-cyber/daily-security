Title: Last Week in Security (LWiS) - 2021-11-16
Date: 2021-11-16 20:45
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-11-16
Author: Erik
Summary: The future of NTLM relaying (<a href="https://twitter.com/_EthicalChaos_" target="_blank">@_EthicalChaos_</a>), Windows updates for hackers (<a href="https://twitter.com/bitsadmin" target="_blank">@bitsadmin</a>), Syscall malware analysis (<a href="https://twitter.com/m0rv4i" target="_blank">@m0rv4i</a>), fighting EDRs in the kernel (<a href="https://twitter.com/cerbersec" target="_blank">@cerbersec</a>), Living Off Trusted Sites (LOTS) Project (<a href="https://twitter.com/mrd0x" target="_blank">@mrd0x</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-11-08 to 2021-11-16.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://krebsonsecurity.com/2021/11/hoax-email-blast-abused-poor-coding-in-fbi-website/" target="_blank">Hoax Email Blast Abused Poor Coding in FBI Website</a>. A series of blunders allowed a hacker to send tens of thousands of emails from an FBI mail server to arbitrary addresses with arbitrary content. Not a good look for the FBI.</li>
<li><a href="https://security.paloaltonetworks.com/CVE-2021-3064" target="_blank">CVE-2021-3064 PAN-OS: Memory Corruption Vulnerability in GlobalProtect Portal and Gateway Interfaces</a>. Another unauthenticated RCE as root in a gateway device. Thankfully this "only" affects older PAN-OS 8.1-8.1.17 devices. The interesting bit is how this was found by a red team and used privately for ~8 months before disclosure. Their rationale is <a href="https://www.randori.com/blog/why-zero-days-are-essential-to-security/" target="_blank">here (official)</a> and <a href="https://www.reddit.com/r/netsec/comments/qqzrsr/cve20213064_cvss_98_rce_in_palo_alto_networks/hk42xa9/" target="_blank">here (reddit)</a>. Technical details will be released 2021-12-10.</li>
<li><a href="https://security.googleblog.com/2021/11/clusterfuzzlite-continuous-fuzzing-for.html" target="_blank">ClusterFuzzLite: Continuous fuzzing for all</a>. After the success of OSS-fuzz, Google is releasing an "easy to use" fuzzing workflow: "ClusterFuzzLite is a continuous fuzzing solution that runs as part of Continuous Integration (CI) workflows to find vulnerabilities faster than ever before. With just a few lines of code, GitHub users can integrate ClusterFuzzLite into their workflow and fuzz pull requests to catch bugs before they are committed."</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://bitsadm.in/blog/windows-security-updates-for-hackers" target="_blank">Windows Security Updates for Hackers</a>. This is the one stop shop for all information related to Windows releases, updates, and tools to find missing patches. Bookmark it.</li>
<li><a href="https://secreltyhiddenwriteups.blogspot.com/2021/11/becoming-super-admin-in-someone-elses.html" target="_blank">Becoming A Super Admin In Someone Else's Gsuite Organization And Taking It Over</a> With a few edited requests in Google Domains you could add yourself to arbitrary GSuite customers as a Super Admin. Great find! PoC video <a href="https://www.youtube.com/watch?v=-DX0CurwwUs" target="_blank">here</a>.</li>
<li><a href="https://blog.google/threat-analysis-group/analyzing-watering-hole-campaign-using-macos-exploits/" target="_blank">Analyzing a watering hole campaign using macOS exploits</a>. macOS is making gains in the consumer market, and thus is getting attention from threat actors. The targets and geography leave little to imagination in terms of attributions. More and more 0days are being used to target activists these days, how dystopian. For more details check out SentielOne's analysis of <a href="https://www.sentinelone.com/labs/infect-if-needed-a-deeper-dive-into-targeted-backdoor-macos-macma/" target="_blank">macOS.Macma</a>.</li>
<li><a href="https://jmpesp.me/malware-analysis-syscalls-example/" target="_blank">Malware Analysis: Syscalls</a>. These malware analysis posts should serve to enlighten the reader as to how their own tools may look from the "other side."</li>
<li><a href="https://blog.nviso.eu/2021/11/16/kernel-karnage-part-3-challenge-accepted/" target="_blank">Kernel Karnage – Part 3 (Challenge Accepted)</a>. To fight kernel driver EDR, you must be come kernel driver EDR?</li>
<li><a href="https://pentestlab.blog/2021/11/15/golden-certificate/" target="_blank">Golden Certificate</a>. DCShadow and Golden Tickets getting too popular/detectable? If the environment is running Active Directory Certification Services (AD CS) you can mint a "Golden Certificate" instead.</li>
<li><a href="https://posts.specterops.io/capability-abstraction-case-study-detecting-malicious-boot-configuration-modifications-1852e2098a65" target="_blank">Capability Abstraction Case Study: Detecting Malicious Boot Configuration Modifications</a>. This post is an exemplar of how to think more about a technique is uses and design detections around it vs an easily bypassed signature.</li>
<li><a href="https://blog.zsec.uk/honeypoc-ultimate/" target="_blank">AutoPoC - Validating the Lack of Validation in PoCs</a>. From HoneyPoC to AutoPoC, Andy has exposed more "threat intelligence" <span class="strike">scripts</span> "products" and "professionals" than anyone. It's pretty crazy to see the amount of trust some people have in random GitHub projects.</li>
<li><a href="https://klezvirus.github.io/RedTeaming/Development/ImplementingShellcodeRetrieval/" target="_blank">Implementing Shellcode Retrieval</a>. The <a href="https://github.com/klezVirus/inceptor" target="_blank">inceptor</a> framework can now abstract how shellcode is delivered to the loader so it can be store in arbitrary formats like UUIDs.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/CCob/lsarelayx" target="_blank">lsarelayx</a> is system wide NTLM relay tool designed to relay incoming NTLM based authentication to the host it is running on. lsarelayx will relay any incoming authentication request which includes SMB. The original application still gets its authentication and there are no errors for the user. This is the next generation of NTLM relaying - with the important caveat of loading into lsass.</li>
<li><a href="https://github.com/rasta-mouse/ExternalC2.NET" target="_blank">ExternalC2.NET</a> is a .NET implementation of Cobalt Strike's External C2 Spec. This could be the basis for your own C2 channel written in C# that uses any medium you can interface with via C# - think services like Slack, Google Drive, Twitter, etc.</li>
<li><a href="https://lots-project.com/" target="_blank">Living Off Trusted Sites (LOTS) Project</a>. Attackers are using popular legitimate domains when conducting phishing, C&amp;C, exfiltration and downloading tools to evade detection. This is a list of websites that allow attackers to use their domain or subdomain to host content that may be used as a C2 channel, phishing site, file host, or data exfiltration destination.</li>
<li><a href="https://github.com/comsec-group/blacksmith" target="_blank">blacksmith</a> is a next-gen Rowhammer fuzzer that uses non-uniform, frequency-based patterns. Read <a href="https://comsec.ethz.ch/research/dram/blacksmith/" target="_blank">this blog post</a> for more information. Bypassing password logic for sudo in ~5-30 minutes is pretty impressive.</li>
<li><a href="https://github.com/zeronetworks/rpcfirewall" target="_blank">rpcfirewall</a> is a firewall for Windows RPC that can be used for research, attack detection, and attack prevention.</li>
<li><a href="https://github.com/MarkoH17/Spray365" target="_blank">Spray365</a> makes spraying Microsoft accounts (Office 365 / Azure AD) easy through its customizable two-step password spraying approach. The built-in execution plan features options that attempt to bypass Azure Smart Lockout and insecure conditional access policies.</li>
<li><a href="https://github.com/CravateRouge/bloodyAD" target="_blank">bloodyAD</a> is an Active Directory Privilege Escalation Framework that can perform specific LDAP/SAMR calls to a domain controller in order to perform AD privesc. It supports authentication using password, NTLM hashes or Kerberos.</li>
<li><a href="https://github.com/edermi/skweez" target="_blank">skweez</a> spiders web pages and extracts words for wordlist generation.</li>
<li><a href="https://github.com/N4kedTurtle/LocalDllParse" target="_blank">LocalDllParse</a> checks all loaded Dlls in the current process for a version resource. Useful for identifying EDRs on a system without making calls out of the current process and avoids all commonly monitored API calls.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Retrospected/kerbmon" target="_blank">kerbmon</a> pulls the current state of the Service Principal Name (SPN) records and sAMAccounts that have the property 'Do not require Kerberos pre-authentication' set (UF_DONT_REQUIRE_PREAUTH). It stores these results in a SQLite3 database.</li>
<li><a href="https://github.com/t3hbb/NSGenCS" target="_blank">NSGenCS</a> is an extremely simple, yet extensible framework to evade AV with obfuscated payloads under Windows.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
