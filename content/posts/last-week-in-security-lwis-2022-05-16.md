Title: Last Week in Security (LWiS) - 2022-05-16
Date: 2022-05-16 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-05-16
Author: Erik
Summary: 

<aside class="m-note m-warning">
<h3>Catching up</h3>
<p>This is a rapid-fire 2 week recap - most entries will have no commentary. Regularly scheduled LWiS will return next week!</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous 2 weeks. This post covers 2022-05-02 to 2022-05-16.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2022/05/taking-on-next-generation-of-phishing.html" target="_blank">Taking on the Next Generation of Phishing Scams</a>. Phishing is going to get more difficult, but backwards compatibility will be there for a while longer.</li>
<li><a href="https://blog.cloudflare.com/wildcard-proxy-for-everyone/" target="_blank">Wildcard proxy for everyone</a>. Wildcard certificates are useful to hide your specific domains from certificate transparency logs, and wildcard DNS entries do the same for DNS aggregators/change monitors.</li>
<li><a href="https://krebsonsecurity.com/2022/05/microsoft-patch-tuesday-may-2022-edition/" target="_blank">Microsoft Patch Tuesday, May 2022 Edition</a>. Maybe hold off on your <a href="https://www.cisa.gov/uscert/ncas/current-activity/2022/05/13/cisa-temporarily-removes-cve-2022-26925-known-exploited" target="_blank">domain controllers</a>?</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.f-secure.com/blog/scheduled-task-tampering/" target="_blank">Scheduled Task Tampering</a>. It's possible to add scheduled tasks without logging using the registry and some tricks. However, task execution will still log unless you tamper with ETW in the scheduler process itself. Some cool options to increase red team opsec in this post as well as a nice Sigma rule for defenders.</li>
<li><a href="https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/" target="_blank">Cloudflare Pages, part 1: The fellowship of the secret</a></li>
<li><a href="https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt2/" target="_blank">Cloudflare Pages, part 2: The two privescs</a></li>
<li><a href="https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt3/" target="_blank">Cloudflare Pages, part 3: The return of the secrets</a></li>
<li><a href="https://offsec.almond.consulting/authenticating-with-certificates-when-pkinit-is-not-supported.html" target="_blank">Authenticating with certificates when PKINIT is not supported</a></li>
<li><a href="https://starlabs.sg/blog/2022/05/new-wine-in-old-bottle-microsoft-sharepoint-post-auth-deserialization-rce-cve-2022-29108/" target="_blank">New Wine in Old Bottle - Microsoft Sharepoint Post-Auth Deserialization RCE (CVE-2022-29108)</a></li>
<li><a href="https://www.horizon3.ai/f5-icontrol-rest-endpoint-authentication-bypass-technical-deep-dive/" target="_blank">F5 iControl REST Endpoint Authentication Bypass Technical Deep Dive</a></li>
<li><a href="https://www.varonis.com/blog/url-spoofing" target="_blank">Spoofing SaaS Vanity URLs for Social Engineering Attacks</a>. Some good lure techniques in here.</li>
<li><a href="https://exploit.ph/defending-the-three-headed-relay.html" target="_blank">Defending the Three Headed Relay</a></li>
<li><a href="https://hausec.com/2022/05/04/azure-virtual-machine-execution-techniques/" target="_blank">Azure Virtual Machine Execution Techniques</a>. All major clouds have this "feature."</li>
<li><a href="https://www.mdsec.co.uk/2022/04/resolving-system-service-numbers-using-the-exception-directory/" target="_blank">Resolving System Service Numbers using the Exception Directory</a></li>
<li><a href="https://labs.nettitude.com/blog/introducing-sharpwsus/" target="_blank">Introducing SharpWSUS</a></li>
<li><a href="https://labs.nettitude.com/blog/introducing-malsccm/" target="_blank">Introducing MalSCCM</a></li>
<li><a href="https://blog.nviso.eu/2022/05/09/introducing-pycobalthound/" target="_blank">Introducing pyCobaltHound – Let Cobalt Strike unleash the Hound</a></li>
<li><a href="https://offensivedefence.co.uk/posts/ntcreateuserprocess/" target="_blank">PPID Spoofing &amp; BlockDLLs with NtCreateUserProcess</a></li>
<li><a href="https://malicious.link/post/2022/ldapsearch-reference/" target="_blank">LDAPSearch Reference</a></li>
<li><a href="https://posts.specterops.io/learning-machine-learning-part-3-attacking-black-box-models-3efffc256909" target="_blank">Learning Machine Learning Part 3: Attacking Black Box Models</a></li>
<li><a href="https://suspicious.actor/2022/05/05/mdsec-nighthawk-study.html" target="_blank">Studying “Next Generation Malware” - NightHawk’s Attempt At Obfuscate and Sleep</a></li>
<li><a href="https://www.trustedsec.com/blog/diving-into-pre-created-computer-accounts/" target="_blank">Diving into pre-created computer accounts</a></li>
<li><a href="https://whynotsecurity.com/blog/o365fedenum/" target="_blank">Office365 User Enumeration</a></li>
<li><a href="https://barbellsandrootshells.com/electron-shellcode-loader" target="_blank">Electron Shellcode Loader</a></li>
<li><a href="https://www.fortalicesolutions.com/posts/bofhound-granularize-your-active-directory-reconnaissance-game" target="_blank">Fortalice BOFHound Release - Granularize Your Active Directory Reconnaissance Game</a></li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/trustedsec/ELFLoader" target="_blank">ELFLoader</a>. Be sure to read the <a href="https://www.trustedsec.com/blog/elfloader-another-in-memory-loader-post/" target="_blank">blog post</a>.</li>
<li><a href="https://github.com/hakluke/hakoriginfinder" target="_blank">hakoriginfinder</a> is a tool for discovering the origin host behind a reverse proxy. Useful for bypassing cloud WAFs.</li>
<li><a href="https://github.com/sailay1996/SpoolTrigger" target="_blank">SpoolTrigger</a> - Weaponizing for privileged file writes bugs with windows problem reporting</li>
<li><a href="https://github.com/Octoberfest7/XLL_Phishing" target="_blank">XLL_Phishing</a> - XLL Phishing Tradecraft</li>
<li><a href="https://github.com/alufers/mitmproxy2swagger" target="_blank">mitmproxy2swagger</a> - Automagically reverse-engineer REST APIs via capturing traffic</li>
<li><a href="https://github.com/guervild/uru" target="_blank">uru</a> is a payload generation tool that enables you to create payload based on a configuration file.</li>
<li><a href="https://github.com/fortalice/pyldapsearch" target="_blank">pyldapsearch</a> - Tool for issuing manual LDAP queries which offers bofhound compatible output</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://markdoc.io/" target="_blank">Markdoc</a></li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 416 (+0)</p>
<p>Blogs monitored: 304 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
