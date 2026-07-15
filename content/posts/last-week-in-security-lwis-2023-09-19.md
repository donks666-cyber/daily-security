Title: Last Week in Security (LWiS) - 2023-09-19
Date: 2023-09-19 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-09-19
Author: Erik
Summary: Cobalt Strike 4.9, 38TB of internal MS data, a crazy phish, an Okta toolkit, macOS LPE, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-09-11 to 2023-09-19.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://techcommunity.microsoft.com/t5/storage-at-microsoft/smb-ntlm-blocking-now-supported-in-windows-insider/ba-p/3916206" target="_blank">SMB NTLM blocking now supported in Windows Insider</a>. The beginning of the end for NTLM relay attacks, but you know enterprise will still have it enabled for "legacy" support for 20 years.</li>
<li><a href="https://go.dev/blog/wasi" target="_blank">WASI support in Go</a>. The Sliver crew is already looking at doing fun things with this.</li>
<li><a href="https://retool.com/blog/mfa-isnt-mfa/" target="_blank">When MFA isn't actually MFA</a>. "The caller claimed to be one of the members of the IT team, and deepfaked our employee'≈s actual voice." It finally happened. It's time to buy hardware keys for all your employees. There is no better defense against this type of advanced attack.</li>
<li><a href="https://www.wiz.io/blog/38-terabytes-of-private-data-accidentally-exposed-by-microsoft-ai-researchers" target="_blank">38TB of data accidentally exposed by Microsoft AI researchers</a>. In the cloud, a signed URL can become a single factor that exposes a lot of data.</li>
<li><a href="https://vulncheck.com/blog/juniper-cve-2023-36845" target="_blank">Fileless Remote Code Execution on Juniper Firewalls</a>. I can't decide if we should laugh or cry. Firewalls, do your one job!</li>
<li><a href="https://www.cobaltstrike.com/blog/cobalt-strike-49-take-me-to-your-loader" target="_blank">Cobalt Strike 4.9: Take Me To Your Loader</a>. The Forta team is working hard to make Cobalt Strike even more modular as well as a bunch of other great enhancements.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.mandiant.com/resources/blog/arbitrary-file-deletion-vulnerabilities" target="_blank">Deleting Your Way Into SYSTEM: Why Arbitrary File Deletion Vulnerabilities Matter</a>. Detailed write up of how to use a file delete for much more than denial of service.</li>
<li><a href="https://www.secureworks.com/research/azure-active-directory-domain-services-escalation-of-privilege" target="_blank">Azure Active Directory Domain Services Escalation of Privilege</a>. Curious if the patch was just the PetitPotam patch...</li>
<li><a href="https://splintercod3.blogspot.com/p/bypassing-uac-with-sspi-datagram.html" target="_blank">Bypassing UAC with SSPI Datagram Contexts</a>. It's messy in the PoC state (creates a service) but a nice UAC bypass.</li>
<li><a href="https://her0ness.github.io/2023-09-14-Attacking-an-EDR-Part-2/" target="_blank">Attacking an EDR - Part 2</a>. With EDR going to the cloud for the heavy lifting in detection, if you can tamper with that network traffic, you can often blind the EDR.</li>
<li><a href="https://www.dutchosintguy.com/post/using-ai-for-extracting-usernames-emails-phone-numbers-and-personal-names-from-large-datasets" target="_blank">Using AI for extracting Usernames, Emails, Phone Numbers, and Personal Names from large datasets</a>. Neat, but you'll need a local model to operate on any sensitive data.</li>
<li><a href="https://medium.com/@matterpreter/hypervisor-detection-with-systemhypervisordetailinformation-26e44a57f80e" target="_blank">Hypervisor Detection with SystemHypervisorDetailInformation</a>. Detect those sandboxes a little easier with <a href="https://github.com/matterpreter/cpuid/" target="_blank">cpuid</a> - A class to emulate the behavior of NtQuerySystemInformation when passed the SystemHypervisorDetailInformation information class.</li>
<li><a href="https://www.trustedsec.com/blog/okta-for-red-teamers/" target="_blank">Okta for Red Teamers</a> - This is fuego 🔥. The addition of a SAML authentication endpoint has been used by threat actors recently.</li>
<li><a href="https://exploits.forsale/themebleed/" target="_blank">CVE-2023-38146: Arbitrary Code Execution via Windows Themes</a>. Looks like the fix might be incomplete - more research needed here! The PoC is: <a href="https://github.com/gabe-k/themebleed" target="_blank">themebleed</a>.</li>
<li><a href="https://www.elastic.co/security-labs/peeling-back-the-curtain-with-call-stacks" target="_blank">Peeling back the curtain with call stacks</a>. The elastic team has been on a good run recently with very technical posts.</li>
<li><a href="https://asahilina.net/agx-exploit/" target="_blank">I hacked macOS!!! CVE-2022-32947 - With Lina✨ &amp; Cyan💎</a>. Very creative site to explain an extremely technical exploit. The final "demo" is impressive. Some people are truly wizards and Lina is one of them.</li>
<li><a href="https://www.g1a55er.net/Android-14-Still-Allows-Modification-of-System-Certificates" target="_blank">Android 14 Still Allows Modification of System Certificates</a>. Lots of claims stating Android 14 would break TLS interception, turns out, its still possible.</li>
<li><a href="https://www.mdsec.co.uk/2023/09/the-not-so-pleasant-password-manager/" target="_blank">The Not So Pleasant Password Manager</a>. Some tough restrictions on XXS were bypassed to successfully leak credentials.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/YOLOP0wn/EchoDrv" target="_blank">EchoDrv</a> - Exploitation of echo_driver.sys.</li>
<li><a href="https://github.com/S3cur3Th1sSh1t/Caro-Kann" target="_blank">Caro-Kann</a> - Encrypted shellcode Injection to avoid Kernel triggered memory scans</li>
<li><a href="https://github.com/redskal/malrdp-deploy" target="_blank">malrdp-deploy</a> -  Automated (kinda) deployment of MalRDP infrastructure with Terraform &amp; Ansible</li>
<li><a href="https://github.com/malcomvetter/Periscope" target="_blank">Periscope</a> - Fully Integrated Adversarial Operations Toolkit (C2, stagers, agents, ephemeral infrastructure, phishing engine, and automation). Note: purposely broken by the author.</li>
<li><a href="https://github.com/Pennyw0rth/NetExec" target="_blank">NetExec</a> - Crack Map Exec fork with different maintainers. Queue the drama.</li>
<li><a href="https://github.com/YOLOP0wn/POSTDump" target="_blank">POSTDump</a> is the C# / .NET implementation of the ReactOS minidump function (like nanodump), thus avoiding call to the Windows API MiniDumpWriteDump function.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/volexity/donut-decryptor" target="_blank">donut-decryptor</a> -  Retrieve inner payloads from Donut samples</li>
<li><a href="https://github.com/SpecterOps/TierZeroTable" target="_blank">TierZeroTable</a> -  About Table of AD and Azure assets and whether they belong to Tier Zero</li>
<li><a href="https://github.com/simplerhacking/Evilginx3-Phishlets" target="_blank">Evilginx3-Phishlets</a> -  This repository provides penetration testers and red teams with an extensive collection of dynamic phishing templates designed specifically for use with Evilginx3.</li>
<li><a href="https://github.com/duckduckgo/tracker-radar" target="_blank">tracker-radar</a> - Good for OSINT.</li>
<li><a href="https://github.com/EvotecIT/GPOZaurr" target="_blank">GPOZaurr</a> - Group Policy Eater is a PowerShell module that aims to gather information about Group Policies but also allows fixing issues that you may find in them.</li>
<li><a href="https://github.com/r3ggi/electroniz3r" target="_blank">electroniz3r</a> - Take over macOS Electron apps' TCC permissions.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 354 (+0)</p>
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
