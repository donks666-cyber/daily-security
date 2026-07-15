Title: Last Week in Security (LWiS) - 2024-04-01
Date: 2024-04-01 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-04-01
Author: Erik
Summary: XZ backdoor (<a href="https://twitter.com/fr0gger_" target="_blank">@fr0gger_</a> + <a href="https://twitter.com/amlweems" target="_blank">@amlweems</a>), best LPE since DirtyCOW (<a href="https://twitter.com/notselwyn" target="_blank">@notselwyn</a>), SCCM pwnage (<a href="https://twitter.com/AndrewOliveau" target="_blank">@AndrewOliveau</a> + <a href="https://twitter.com/__Mastadon" target="_blank">@__Mastadon</a>), kernel fuzzing (<a href="https://twitter.com/R00tkitSMM" target="_blank">@R00tkitSMM</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-03-25 to 2024-04-01.</p>
<aside class="m-note m-success">
<h3>Ludus 1.3.0 Release</h3>
<p>The biggest update to Ludus since 1.0.0 is out now! Share ranges, limit deploys, run specific roles and more. Plus a bunch of bug fixes!</p>
<p>Get 1.3.0 <a href="https://gitlab.com/badsectorlabs/ludus/-/releases" target="_blank">here</a>.</p>
<p>Learn more about Ludus at <a href="https://ludus.cloud" target="_blank">ludus.cloud</a>.</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><p>XZ Backdoor</p>
<blockquote>
<ul>
<li><a href="https://twitter.com/badsectorlabs/status/1773759444486177023" target="_blank">Our (viral?!) breakdown thread</a> - This thread took off on friday as it was posted pretty quickly after the news broke.</li>
<li><a href="https://github.com/amlweems/xzbot" target="_blank">xzbot</a> - notes, honeypot, and exploit demo for the xz backdoor (CVE-2024-3094).</li>
<li><a href="https://twitter.com/fr0gger_/status/1774342248437813525" target="_blank">XZ backdoor infographic</a> - A nice one page summary of the backdoor</li>
<li><a href="https://x.com/julianor/status/1774130812721488205" target="_blank">More potential malicious commits from Jia Tan</a>.</li>
</ul>
</blockquote>
</li>
<li><p><a href="https://storage.courtlistener.com/recap/gov.uscourts.cand.369872/gov.uscourts.cand.369872.735.0.pdf" target="_blank">[PDF] Court documents show Facebook owned VPN was using HTTPS interception to decrypt Snapchat, YouTube, and Amazon traffic</a> - See the bottom of page 2 and top of page 3. At least they paid the VPN "users?" Remember, this from <a href="https://www.businessinsider.com/well-these-new-zuckerberg-ims-wont-help-facebooks-privacy-problems-2010-5" target="_blank">they "trust me"</a> Zuck. Just as Meta was gaining reputation back with their open LLMs...</p>
</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><p><a href="https://pwning.tech/nftables/" target="_blank">Flipping Pages: An analysis of a new Linux vulnerability in nf_tables and hardened exploitation techniques</a> - This got overshadowed by the xz backdoor but it's epic. A tale about exploiting KernelCTF Mitigation, Debian, and Ubuntu instances with a double-free in nf_tables in the Linux kernel, using novel techniques like Dirty Pagedirectory. All without even having to recompile the exploit for different kernel targets once.</p>
</li>
<li><p><a href="https://blog.exodusintel.com/2024/03/27/mind-the-patch-gap-exploiting-an-io_uring-vulnerability-in-ubuntu/" target="_blank">Mind the Patch Gap: Exploiting an io_uring Vulnerability in Ubuntu</a> - More great Linux exploitation content.</p>
</li>
<li><p>SCCM</p>
<blockquote>
<ul>
<li><a href="https://www.guidepointsecurity.com/blog/sccm-exploitation-account-compromise-through-automatic-client-push-amp-ad-system-discovery/" target="_blank">SCCM Exploitation: Account Compromise Through Automatic Client Push &amp; AD System Discovery</a> - The SCCM train continues! A way to go from low priv user -&gt; SCCM client push account and SCCM machine account. Great work Marshall!</li>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/windows-session-hijacking-via-ccmexec" target="_blank">SeeSeeYouExec: Windows Session Hijacking via CcmExec</a> - A blog on how the CcmExec service can be utilized for session hijacking. Came with a tool drop: <a href="https://github.com/mandiant/CcmPwn" target="_blank">CcmPwn</a> . A tool designed to facilitate this technique.</li>
<li><a href="https://mayfly277.github.io/posts/SCCM-LAB-part0x1/" target="_blank">SCCM / MECM LAB - Part 0x1 - Recon and PXE</a> - A walkthrough of the new SCCM lab in GOAD.</li>
</ul>
</blockquote>
</li>
<li><p><a href="https://www.elastic.co/security-labs/itw-windows-lpe-0days-insights-and-detection-strategies" target="_blank">In-the-Wild Windows LPE 0-days: Insights &amp; Detection Strategies</a> - Detection methods for Windows local privilege escalation techniques based on dynamic behaviors analysis. Not really 0-days since they're older vulns but still cool read.</p>
</li>
<li><p><a href="https://r00tkitsmm.github.io/fuzzing/2024/03/27/libffuzzerkernel.html" target="_blank">Structure-Aware linux kernel Fuzzing with libFuzzer</a> - Enhancing Linux kernel fuzzing by integrating KCOV with libFuzzer, aiming to boot the kernel efficiently without a complex root filesystem setup.</p>
</li>
<li><p><a href="https://www.oligo.security/blog/shadowray-attack-ai-workloads-actively-exploited-in-the-wild" target="_blank">ShadowRay: First Known Attack Campaign Targeting AI Workloads Actively Exploited In The Wild</a> - I thought AI was supposed to replace security, not add to it!</p>
</li>
<li><p><a href="https://www.humansecurity.com/learn/blog/satori-threat-intelligence-alert-proxylib-and-lumiapps-transform-mobile-devices-into-proxy-nodes" target="_blank">Satori Threat Intelligence Alert: PROXYLIB and LumiApps Transform Mobile Devices into Proxy Nodes</a> - Have you used residential proxies for your red teams yet? Threat actors are using them...</p>
</li>
<li><p><a href="https://www.secureworks.com/research/azure-redirect-uri-takeover-vulnerability" target="_blank">Azure Redirect URI Takeover Vulnerability</a> - A vulnerability in Azure's OAuth 2.0 flow where unregistered subdomains in application redirect URIs could be exploited by TAs to steal authorization codes and impersonate users.</p>
</li>
<li><p><a href="https://scorpiosoftware.net/2024/03/26/the-power-of-ui-automation/" target="_blank">The Power of UI Automation</a> - UI Automation provides a tree of UI automation elements representing various aspects of a user interface. Could be useful to automate certain testing or other tasks.</p>
</li>
<li><p><a href="https://labs.lares.com/fear-kerberos-pt2/" target="_blank">Kerberos II - Credential Access</a> Part two of the <a href="https://labs.lares.com/fear-kerberos-pt1/" target="_blank">series</a>.</p>
</li>
<li><p><a href="https://danaepp.com/improving-port-scans-against-api-servers" target="_blank">Improving port scans against API servers</a> - Friendly reminder to explore new tools because you might end up liking them. Like replacing your ESXi host with <a href="https://ludus.cloud/" target="_blank">Ludus</a> 😜! This blog discusses some of the reasons they moved away from Nmap and into naabu (from the projectdiscovery team).</p>
</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/soufianetahiri/TeamsNTLMLeak" target="_blank">TeamsNTLMLeak</a> - Leak NTLM via Website tab in teams via MS Office.</li>
<li><a href="https://github.com/Ridter/atexec-pro" target="_blank">Atexec-pro</a> - Fileless atexec, no more need for port 445.</li>
<li><a href="https://github.com/nettitude/SharpConflux/" target="_blank">SharpConflux</a> - SharpConflux is a .NET application built to facilitate Confluence exploration. It allows Red Team operators to easily investigate Confluence instances with the goal of finding credential material and documentation relating to objectives without having to rely on SOCKS proxying. <a href="https://labs.nettitude.com/blog/introducing-sharpconflux/" target="_blank">Here is the related blog.</a></li>
<li><a href="https://github.com/Tw1sm/SQL-BOF" target="_blank">SQL-BOF</a> - A library of beacon object files to interact with remote SQL servers and data.</li>
<li><a href="https://github.com/jhaddix/CSPReconGO" target="_blank">CspReconGo</a> - It automates the extraction and analysis of domains from Content Security Policy (CSP) headers and JavaScript files on websites.</li>
<li><a href="https://github.com/Notselwyn/CVE-2024-1086" target="_blank">CVE-2024-1086</a> - Universal local privilege escalation Proof-of-Concept exploit for CVE-2024-1086, working on most Linux kernels between v5.14 and v6.6, including Debian, Ubuntu, and KernelCTF. The success rate is 99.4% in KernelCTF images.</li>
<li><a href="https://github.com/mandiant/CcmPwn" target="_blank">CcmPwn</a> - Lateral movement script that leverages the CcmExec service to remotely hijack user sessions.</li>
<li><a href="https://github.com/Cipher7/ChaiLdr" target="_blank">ChaiLdr</a> - AV bypass while you sip your Chai!.</li>
<li><a href="https://github.com/magisterquis/curlrevshell" target="_blank">curlrevshell</a> - Kooky cURL-powered replacement for reverse shell via /dev/tcp.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Meckazin/ChromeKatz" target="_blank">Cookie dumper for Chrome and Edge</a> -  Dump cookies directly from Chrome process memory</li>
<li><a href="https://github.com/joaoviictorti/RustRedOps" target="_blank">RustRedOps</a> - 🦀 | RustRedOps is a repository dedicated to gathering and sharing advanced techniques and offensive malware for Red Team, with a specific focus on the Rust programming language.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 375 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
