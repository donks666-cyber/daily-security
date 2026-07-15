Title: Last Week in Security (LWiS) - 2022-05-31
Date: 2022-05-31 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-05-31
Author: Erik
Summary: Follina Word RCE (<a href="https://twitter.com/_JohnHammond" target="_blank">@_JohnHammond</a> + <a href="https://twitter.com/BillDemirkapi" target="_blank">@BillDemirkapi</a>), PyPI CTX and PHPass compromise (<a href="https://twitter.com/aydinnyunuss" target="_blank">@aydinnyunuss</a>), Gargoyle w/ROP (<a href="https://twitter.com/thefLinkk" target="_blank">@thefLinkk</a>), Fuchsia OS kernel hacking (<a href="https://twitter.com/a13xp0p0v" target="_blank">@a13xp0p0v</a>), custom Cypher (<a href="https://twitter.com/simondotsh" target="_blank">@simondotsh</a>), code audit process (<a href="https://twitter.com/frycos" target="_blank">@frycos</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-05-23 to 2022-05-31.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.huntress.com/blog/microsoft-office-remote-code-execution-follina-msdt-bug" target="_blank">Rapid Response: Microsoft Office RCE - “Follina” MSDT Attack</a>. Follina aka CVE-2022-30190 is an RCE vector that uses the Microsoft Support Diagnostic Tool via a URL handler in a Word document (no macro) to execute code. There is more analysis <a href="https://billdemirkapi.me/unpacking-cve-2021-40444-microsoft-office-rce/" target="_blank">here</a> as well as <a href="https://msrc-blog.microsoft.com/2022/05/30/guidance-for-cve-2022-30190-microsoft-support-diagnostic-tool-vulnerability/" target="_blank">official guidance</a>. <a href="https://github.com/chvancooten/follina.py" target="_blank">follina.py</a> is the PoC.</li>
<li><a href="https://ngrok.com/next-generation" target="_blank">Welcome to the next generation of ngrok</a>. The popular tunneling utility used to exposed local ports to the public internet released version 3 with some cool new features. Oauth and OpenID support with a few command line switches make authentication easy. Ngrok has been used to host short lived phishing pages by threat actors in the past.</li>
<li><a href="https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/company/vmware-broadcom.pdf" target="_blank">Broadcom to Acquire VMware for Approximately $61 Billion in Cash and Stock</a>. If anyone witnessed the Symantec acquisition br Broadcom this is scary if you use any VMware products (vCenter, Carbon Black, etc). For what it's worth I've been using <a href="https://www.proxmox.com/en/" target="_blank">Proxmox</a> at home and in production for a while and it's pretty great.</li>
<li><a href="https://sockpuppets.medium.com/how-i-hacked-ctx-and-phpass-modules-656638c6ec5e" target="_blank">How I hacked CTX and PHPass Modules</a>. This is a great example of how <em>NOT</em> to conduct "security research." By deploying malicious packages that actively harvested sensitive environment variables, this crosses the line and I would not consider it "good faith" research. However, the automated techniques used to target package registries are relatively low effort for an extremely high impact. The next attacker will not claim "research" and will use this access for ransomware or worse.</li>
<li><a href="https://www.bleepingcomputer.com/news/technology/ftc-fines-twitter-150m-for-using-2fa-info-for-targeted-advertising/" target="_blank">FTC fines Twitter $150M for using 2FA info for targeted advertising</a>. Twitter used its 2FA phone numbers for advertising and got caught. I suppose when you loose 221 million USD a year you get desperate and every piece of data is up for sale.</li>
<li><a href="https://tails.boum.org/security/prototype_pollution/index.en.html" target="_blank">Serious security vulnerability in Tails 5.0</a>. Tor Browser in Tails 5.0 and earlier is unsafe to use for sensitive information. 5.1 will be released 2022-05-31.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.blackhillsinfosec.com/spoofing-microsoft-365-like-its-1995/" target="_blank">Spoofing Microsoft 365 Like It's 1995</a>. What if you wanted a scanner to send emails to your internal users but you use O365 email? How about an MS mail server that listens on port 25, has no auth, and delivers mail straight to your users from any email even if it doesn't exist in your domain? What could go wrong?</li>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2254" target="_blank">Issue 2254: Zoom: Remote Code Execution with XMPP Stanza Smuggling</a>. XML being parsed differently by two different libraries ends ups in RCE. Impressive research.</li>
<li><a href="https://a13xp0p0v.github.io/2022/05/24/pwn-fuchsia.html" target="_blank">A Kernel Hacker Meets Fuchsia OS</a>. This is a long post that goes from "download the src" to "plant a rootkit."</li>
<li><a href="https://www.synacktiv.com/en/publications/the-printer-goes-brrrrr.html" target="_blank">The printer goes brrrrr!!!</a>. The ability to exploit an implant a network printer could give you network access for years. No one watches their printers, and the often have access to many subnets.</li>
<li><a href="https://csandker.io//2022/05/29/Debugging-And-Reversing-ALPC.html" target="_blank">Debugging and Reversing ALPC</a>. No big reveal at the end of the post, but it does give good instructions on setting up a Windows VM for local or remote kernel debugging. For a more detailed post check out <a href="https://csandker.io//2022/05/24/Offensive-Windows-IPC-3-ALPC.html" target="_blank">Offensive Windows IPC Internals 3: ALPC</a>.</li>
<li><a href="https://labs.detectify.com/2022/05/30/leveraging-aws-quicksight-dashboards-to-visualize-recon-data/" target="_blank">Leveraging AWS QuickSight dashboards to visualize recon data</a>. Use the AWS "business intelligence" tool to visualize all your "business intelligence" or make sense of some very verbose command line output.</li>
<li><a href="https://simondotsh.com/infosec/2022/05/24/bloodhound.html" target="_blank">Capitalizing on BloodHound's Data: Cypher, Object Ownerships and Trusts</a>. Investigate object ownerships across domains using custom Cypher queries.</li>
<li><a href="https://cedowens.medium.com/taking-esf-for-a-nother-spin-6e1e6acd1b74" target="_blank">Taking ESF For A(nother) Spin</a>. ESF is the macOS ETW.</li>
<li><a href="https://frycos.github.io/vulns4free/2022/05/24/security-code-audit-fails.html" target="_blank">Security Code Audit - For Fun and Fails</a>. While there is no epic RCE to end this post, there is tons of good knowledge and process described throughout.</li>
<li><a href="https://www.trustedsec.com/blog/intro-to-web-app-security-testing-burp-suite-tips-tricks/" target="_blank">Intro to Web App Security Testing: Burp Suite Tips &amp; Tricks</a>. Some basic Burp Suite usage to get you started poking at web apps.</li>
<li><a href="https://posts.specterops.io/automating-azure-abuse-research-part-1-30b0eca33418" target="_blank">Automating Azure Abuse Research — Part 1</a>. Every website has an API, some just make you work harder to automate their usage than others. In this case Andy automates the "Run Command Script" function of Azure via Powershell, but the technique is generally applicable.</li>
<li><a href="https://www.horizon3.ai/vmware-authentication-bypass-vulnerability-cve-2022-22972-technical-deep-dive/" target="_blank">VMware Authentication Bypass Vulnerability (CVE-2022-22972) Technical Deep Dive</a>. Host header manipulation and a custom "logon server" allow you to bypass authentication on multiple VMware products. PoC <a href="https://github.com/horizon3ai/CVE-2022-22972" target="_blank">here</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/thefLink/DeepSleep" target="_blank">DeepSleep</a> is a variant of Gargoyle for x64 to hide memory artifacts using ROP only and PIC.</li>
<li><a href="https://github.com/necreas1ng/VLANPWN" target="_blank">VLANPWN</a> is a VLAN attack toolkit (double tagging and DTP hijacking).</li>
<li><a href="https://github.com/gamozolabs/mempeek" target="_blank">mempeek</a> is a command line tool that resembles a debugger as well as Cheat Engine, to search for values in memory.</li>
<li><a href="https://github.com/Cracked5pider/KaynStrike" target="_blank">KaynStrike</a> is a User Defined Reflective Loader for Cobalt Strike Beacon that spoofs the thread start address and frees itself after entry point was executed.</li>
<li><a href="https://github.com/S4ntiagoP/freeBokuLoader" target="_blank">freeBokuLoader</a> is a simple BOF that tries to free the memory region where the User Defined Reflective Loader is stored.</li>
<li><a href="https://github.com/kleiton0x00/Shelltropy" target="_blank">Shelltropy</a> - A technique of hiding malicious shellcode via Shannon encoding.</li>
<li><a href="https://github.com/asaurusrex/MachoBins" target="_blank">MachoBins</a> is designed to provide information on Mac lolbins, similar to <a class="m-link-wrap" href="https://gtfobins.github.io/" target="_blank">https://gtfobins.github.io/</a> or <a class="m-link-wrap" href="https://lolbas-project.github.io/" target="_blank">https://lolbas-project.github.io/</a>, but specifically for Mac!</li>
<li><a href="https://github.com/klezVirus/NimlineWhispers3" target="_blank">NimlineWhispers3</a> - A tool for converting SysWhispers3 syscalls for use with Nim projects.</li>
<li><a href="https://github.com/sailay1996/CdpSvcLPE" target="_blank">CdpSvcLPE</a> - Windows Local Privilege Escalation via CdpSvc service (Writeable SYSTEM path Dll Hijacking).</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/cube0x0/BofRoast" target="_blank">BofRoast</a> - Beacon Object Files for roasting Active Directory.</li>
<li><a href="https://github.com/ch2sh/BatchGuard" target="_blank">BatchGuard</a> - Batch file AV evasion and obfuscation solution.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 416 (+0)</p>
<p>Blogs monitored: 308 (+3)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
