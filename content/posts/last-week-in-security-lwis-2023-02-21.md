Title: Last Week in Security (LWiS) - 2023-02-21
Date: 2023-02-21 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-02-21
Author: Erik
Summary: FortiNAC RCE, NimPlant (<a href="https://twitter.com/chvancooten" target="_blank">@chvancooten</a>), LPE via GPO (<a href="https://twitter.com/decoder_it" target="_blank">@decoder_it</a>), bypassing Okta MFA (<a href="https://twitter.com/n00py1" target="_blank">@n00py1</a>), injection with NtQueueApcThreadEx (<a href="https://twitter.com/LloydLabs" target="_blank">@LloydLabs</a>), DKOM attacks on ETW providers (<a href="https://twitter.com/FuzzySec" target="_blank">@FuzzySec</a>), PCIe on Windows (<a href="https://twitter.com/4lpine" target="_blank">@4lpine</a>), and more!

<aside class="m-note m-warning">
<h3>3 years of LWiS!</h3>
<p>To celebrate 3 years of weekly posts, I'll be taking next week off.</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-02-13 to 2023-02-21.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://ccb.belgium.be/en/news/new-legal-framework-reporting-it-vulnerabilities" target="_blank">New legal framework for reporting IT vulnerabilities</a>. Belgium's CSIRT can give researchers legal protection granted they meet some conditions when reporting (ethics stuff like acting without intent to harm, no public disclosure without consent, etc). To see this codified in law is awesome. Hack the planet!</li>
<li><a href="https://blog.clamav.net/2023/02/clamav-01038-01052-and-101-patch.html" target="_blank">ClamAV 0.103.8, 0.105.2 and 1.0.1 patch versions published</a>. HFS+ file parsing could lead to remote code execution. As ClamAV is used in many mail gateways, the potential to get code execution by emailing an HFS+ file is exiting/terrifying.</li>
<li><a href="https://github.com/GoogleChromeLabs/telnet-client" target="_blank">telnet-client</a>. The Google Chrome team put a telnet client into Chrome. Your scientists were so preoccupied with whether or not they could, they didn't stop to think if they should.</li>
<li><a href="https://twitter.com/vxunderground/status/1627477748359872513" target="_blank">[Twitter] Activision was breached December 4th, 2022.</a>. How'd they do it? SMS phishing, and you can see the screenshots in the tweet. All it takes is one, however, the attackers appear to have their access from a different location (i.e. no code running on the user's system). Would your systems catch this (impossible travel, etc)?</li>
<li><a href="https://arstechnica.com/information-technology/2023/02/godaddy-says-a-multi-year-breach-hijacked-customer-websites-and-accounts/" target="_blank">GoDaddy says a multi-year breach hijacked customer websites and accounts</a>. Ever since GoDaddy bought and then tried to resell me a domain I searched for on their site in 2012 I have sworn to never touch them. Intuition was right on.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.archcloudlabs.com/projects/disabling-clamav-as-unprivileged-user/" target="_blank">Disabling ClamAV as an Unprivileged User</a>. Socketfile permissions claim another victim. With write access to kick off scans comes the ability to shut down the AV altogether.</li>
<li><a href="https://decoder.cloud/2023/02/16/eop-via-arbitrary-file-write-overwite-in-group-policy-client-gpsvc-cve-2022-37955/" target="_blank">EoP via Arbitrary File Write/Overwite in Group Policy Client “gpsvc” - CVE-2022-37955</a>. Symbolic links on Windows have led to lots of LPEs over the past few years. This one uses a GPO's "Files" windows setting to write arbitrary files as SYSTEM.</li>
<li><a href="https://www.n00py.io/2023/02/bypassing-okta-mfa-credential-provider-for-windows/" target="_blank">Bypassing Okta MFA Credential Provider for Windows</a>. A little walkthrough on how to flip off MFA for RDP once you have admin on the machine.</li>
<li><a href="https://securityintelligence.com/posts/direct-kernel-object-manipulation-attacks-etw-providers/" target="_blank">Direct Kernel Object Manipulation (DKOM) Attacks on ETW Providers</a>. Attackers in your kernel is a certified "bad thing." How bad? This post shows a few ways to blind ETW from the kernel. Not just theory, there is an example from Lazarus in the post as well.</li>
<li><a href="https://bishopfox.com/blog/what-the-vuln-zimbra" target="_blank">What the Vuln: Zimbra</a>. This new post series looks fun! First up: a web app with a path traversal vulnerability.</li>
<li><a href="https://www.horizon3.ai/fortinet-fortinac-cve-2022-39952-deep-dive-and-iocs/" target="_blank">Fortinet FortiNAC CVE-2022-39952 Deep-Dive and IOCs</a>. How did this get past the internal security team, static analysis, and external audits? Amazing. <a href="https://github.com/horizon3ai/CVE-2022-39952/blob/master/CVE-2022-39952.py" target="_blank">Are you kidding me?</a></li>
<li><a href="https://ctf.re//windows/kernel/pcie/tutorial/2023/02/14/pcie-part-1/" target="_blank">A Practical Tutorial on PCIe for Total Beginners on Windows (Part 1)</a>. The amount of high quality free learning on the internet is amazing, and the people that put it together are awesome.</li>
<li><a href="https://posts.specterops.io/abusing-azure-app-service-managed-identity-assignments-c3adefccff95" target="_blank">Abusing Azure App Service Managed Identity Assignments</a>. Azure is a scary place, and fully understanding the connections of services, apps, principles, etc is a constant struggle.</li>
<li><a href="https://antoinevastel.com/bot%20detection/2023/02/19/new-headless-chrome.html?mc_cid=006a7961cd&amp;mc_eid=ad8c97ece0" target="_blank">New headless Chrome has been released and has a near-perfect browser fingerprint</a>. TLDR: --headless=new will make your headless browser look nearly the same as regular chrome.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/j00sean/CVE-2022-44666" target="_blank">CVE-2022-44666</a> - Write-up for another forgotten Windows vulnerability (0day): Microsoft Windows Contacts (VCF/Contact/LDAP) syslink control href attribute escape, which was not fully fixed as CVE-2022-44666 in the patches released on December, 2022.</li>
<li><a href="https://github.com/LloydLabs/ntqueueapcthreadex-ntdll-gadget-injection" target="_blank">ntqueueapcthreadex-ntdll-gadget-injection</a> - This novel way of using NtQueueApcThreadEx by abusing the ApcRoutine and SystemArgument[0-3] parameters by passing a random pop r32; ret gadget can be used for stealthy code injection.</li>
<li><a href="https://github.com/Kudaes/Split" target="_blank">Split</a> - Apply a divide and conquer approach to bypass EDRs.</li>
<li><a href="https://gist.github.com/freefirex/8b202c94fc6c1036aed1402a4dd28db1" target="_blank">COFF_With_Exception_handler.c</a>. Make your BOFs safer.</li>
<li><a href="https://github.com/Cracked5pider/LsaParser" target="_blank">LsaParser</a> - A shitty (and old) lsass parser. [authors original description]</li>
<li><a href="https://github.com/chvancooten/NimPlant" target="_blank">NimPlant</a> - A light-weight first-stage C2 implant written in Nim.</li>
<li><a href="https://github.com/iilegacyyii/ThreadlessInject-BOF" target="_blank">ThreadlessInject-BOF</a> - BOF implementation of <a href="https://twitter.com/_EthicalChaos_" target="_blank">@_EthicalChaos_</a>'s ThreadlessInject project. A novel process injection technique with no thread creation, released at BSides Cymru 2023.</li>
<li><a href="https://github.com/Orange-Cyberdefense/graphcat" target="_blank">graphcat</a> - Generate graphs and charts based on password cracking result.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.cryptool.org/en/cto/openssl" target="_blank">OpenSSL Ported to the web browser with WebAssembly</a>. WebAssembly is coming for everything. Chrome/Firefox/Safari are the OSs of the future.</li>
<li><a href="https://github.com/CoolerVoid/heap_detective" target="_blank">heap_detective</a> - The simple way to detect heap memory pitfalls in C++ and C. Beta.</li>
<li><a href="https://pbom.dev/" target="_blank">Open Software Supply Chain Attack Reference (OSC&amp;R)</a>. Its ATT&amp;CK for releasing software.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 337 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
