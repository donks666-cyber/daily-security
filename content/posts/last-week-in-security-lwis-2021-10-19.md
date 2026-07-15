Title: Last Week in Security (LWiS) - 2021-10-19
Date: 2021-10-19 15:25
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-10-19
Author: Erik
Summary: macOS ESF playground (<a href="https://twitter.com/jbradley89" target="_blank">@jbradley89</a>), Azure privesc via service principles (<a href="https://twitter.com/_wald0" target="_blank">@_wald0</a>), Java gadget finding (<a href="https://twitter.com/hugow_vincent" target="_blank">@hugow_vincent</a>), malicious Azure AD OAuth2 (<a href="https://twitter.com/nyxgeek" target="_blank">@nyxgeek</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-10-11 to 2021-10-19.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://portswigger.net/daily-swig/firefox-suggest-lands-in-the-us-bringing-ads-to-the-browser-search-bar" target="_blank">Firefox Suggest lands in the US, bringing ads to the browser search bar</a>. Add this to the list of check boxes to uncheck on new Firefox installs. Settings -&gt; Privacy &amp; Security -&gt; Address Bar — Firefox Suggest -&gt; Contextual suggestions.</li>
<li><a href="https://www.vice.com/en/article/z3xjqa/cheat-maker-is-so-far-not-afraid-of-call-of-dutys-new-kernel-level-anti-cheat" target="_blank">Cheat Maker Is Not Afraid of Call of Duty’s New Kernel-Level Anti-Cheat</a>. This is the second major video game maker to move to the kernel. As these drivers will be allow listed by AV, any vulnerability in them could prove valuable to red teamers.</li>
<li><a href="https://www.vice.com/en/article/jg8ynp/governor-wants-to-prosecute-journalist-who-clicked-view-source-on-government-site" target="_blank">Governor Wants to Prosecute Journalist Who Clicked ‘View Source’ on Government Site</a>. This is the level of computer literacy in government. <a href="https://github.com/SamPatt/RCVS-hack" target="_blank">RCVS-hack</a> contains this 31337 darkweb 0day. 🤦</li>
<li><a href="https://zerotrust.cyber.gov/federal-zero-trust-strategy/#identity" target="_blank">Moving the U.S. Government Towards Zero Trust Cybersecurity Principles</a>. The US government isn't totally hopeless and this push to use hardware tokens to prevent phishing from the White House is a great move!</li>
<li><a href="https://lockboxx.blogspot.com/2021/10/the-shenanigans-of-jonathan-villareal.html" target="_blank">The Shenanigans of Jonathan Villareal</a>. The fake iOS 0days were absent from this curated blog (you're welcome), but they show how easily manipulated the "infosec community" can be. This post breaks down the "RCE" and shows industry expert reactions.</li>
<li><a href="https://l0phtcrack.gitlab.io/" target="_blank">L0phtCrack is Now Open Source</a>. Perhaps the oldest password "audit" tool is now open source. The GPU supply shortage and other factors caused <a href="https://terahash.com/letter-from-ceo/" target="_blank">Terahash</a> to default on the terms of the sale of L0phtCrack and thus it was repossessed and open sourced.</li>
<li><a href="https://github.com/Sysinternals/SysmonForLinux" target="_blank">Sysmon For Linux</a>. Breaking: temperature in Hell nearing freezing, hogs show signs they may be capable of flight.</li>
<li><a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36970" target="_blank">Windows Print Spooler Spoofing Vulnerability - CVE-2021-36970</a>. This PrintNightmare may never end.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://maxwelldulin.com/BlogPost?post=6295828480" target="_blank">House of IO - Heap Reuse</a>. This new modification to the <a href="https://awaraucom.wordpress.com/2020/07/19/house-of-io-remastered/" target="_blank">House of Io</a> even has some <a href="https://github.com/mdulin2/house_of_io_many_more" target="_blank">example code</a> so you can follow along.</li>
<li><a href="https://posts.specterops.io/azure-privilege-escalation-via-service-principal-abuse-210ae2be2a5" target="_blank">Azure Privilege Escalation via Service Principal Abuse</a>. Despite well defined password policy safeguards, Application Administrators can often elevate to Global Administrators if the application has Global Admin service principle. "Azure admins can prevent this attack path by auditing roles held by service principals and comparing those roles to the other identities with control of apps."</li>
<li><a href="https://www.synacktiv.com/en/publications/finding-gadgets-like-its-2015-part-1.html" target="_blank">Finding gadgets like it's 2015: part 1</a>. This article explains the CommonCollection 1 and 7 gadget chains to help understand the new chain found in the Mojarra library.</li>
<li><a href="https://pentestlab.blog/2021/10/18/resource-based-constrained-delegation/" target="_blank">Resource Based Constrained Delegation</a>. RBCD is one of the more complicated Active Directory attack paths. This article shows practical, step-by-step exploitation of this path which should help drive home the process.</li>
<li><a href="https://blog.google/threat-analysis-group/countering-threats-iran/" target="_blank">Countering threats from Iran</a>. Interested in what an actual APT phishing campaign and infrastructure looks like? Look no further.</li>
<li><a href="https://www.trustedsec.com/blog/creating-a-malicious-azure-ad-oauth2-application/" target="_blank">Creating a Malicious Azure AD OAuth2 Application</a>. Emulate those OAuth2 APTs (see above) with this practical guide from trustedsec.</li>
<li><a href="https://infosecwriteups.com/exploiting-redis-through-ssrf-attack-be625682461b" target="_blank">Exploiting Redis Through SSRF Attack</a>. This post shows different ways the Redis key-value store can be exploited using SSRF.</li>
<li><a href="https://googleprojectzero.blogspot.com/2021/10/how-simple-linux-kernel-memory.html" target="_blank">How a simple Linux kernel memory corruption bug can lead to complete system compromise</a>. This post is unique in that the mitigations sections is three times as long as the vulnerability/PoC walk through.</li>
<li><a href="https://thalpius.com/2021/10/14/microsoft-windows-antimalware-scan-interface-bypasses/" target="_blank">Microsoft Windows Antimalware Scan Interface Bypasses</a>. AMSI bypasses have been around for a few years, and this post shows the internal workings of how the memory patches work.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://blog.cobaltstrike.com/2021/10/13/cobalt-strike-sleep-python-bridge/" target="_blank">Cobalt Strike Sleep Python Bridge</a>. Rejoice! You no longer need to write sleep (a Java/Perl hybrid) to interact with Cobalt Strike. Lots of cool examples of how it can be used in the post. It's only a matter of time before someone writes a nice web GUI for cobalt strike, or writes an integration for <a href="https://github.com/its-a-feature/Mythic" target="_blank">Mythic</a>. For prior art, check out <a href="https://github.com/dcsync/pycobalt" target="_blank">pycobalt</a>.</li>
<li><a href="https://themittenmac.com/the-esf-playground/" target="_blank">The ESF Playground</a> will let you view events from the Apple Endpoint Security Framework on your mac. This is particularly useful when trying to write detections and see how different processes are behaving.</li>
<li><a href="https://github.com/optiv/ScareCrow/releases/tag/v3.0" target="_blank">ScareCrow v3.0 released</a>. This popular shellcode loader has been updated with more EDR bypass tricks and some bug fixes.</li>
<li><a href="https://www.praetorian.com/blog/introducing-snowcat/" target="_blank">Introducing Snowcat: World’s First Dedicated Security Scanner for Istio</a>. Istio is a popular service mesh and Snowcat is a tool to audit it.</li>
<li><a href="https://github.com/kindtime/nosferatu" target="_blank">nosferatu</a> is an lsass NTLM authentication backdoor DLL that is injected into lsass and provides a skeleton key password for all accounts. On domain joined machines SMB, WinRM, and WMI are functional with the skeleton key password, on non-domain joined machines authentication via RDP, runas, and the lock screen also accepts the skeleton key password.</li>
<li><a href="https://labs.redyops.com/index.php/2021/10/18/anydesk-escalation-of-privilege-cve-2021-40854/?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=anydesk-escalation-of-privilege-cve-2021-40854" target="_blank">AnyDesk Escalation of Privilege (CVE-2021-40854)</a>. You've got love a privesc that involves a classic Open dialog -&gt; run cmd.exe path that results in SYSTEM in 2021.</li>
<li><a href="https://github.com/p0dalirius/LDAPmonitor" target="_blank">LDAPmonitor</a> monitors creation, deletion and changes to LDAP objects live during your pentest or system administration!</li>
<li><a href="https://github.com/aaaddress1/Skrull" target="_blank">Skrull</a> is a malware DRM, that prevents Automatic Sample Submission by AV/EDR and Signature Scanning from Kernel. It generates launchers that can run malware on the victim using the Process Ghosting technique. Also, launchers are totally anti-copy and naturally broken when got submitted. Probably want to review the <a href="https://github.com/aaaddress1/Skrull/blob/74040b45d23247b1bffd1ff0d2ce1493a4934cb4/src/armor.h#L122" target="_blank">code</a> before use (same goes for all tools).</li>
<li><a href="https://github.com/tandasat/WPBT-Builder" target="_blank">WPBT-Builder</a> is a simple UEFI application to create a Windows Platform Binary Table (WPBT) from the UEFI shell. This is a PoC for <a href="https://eclypsium.com/2021/09/23/everyone-gets-a-rootkit/" target="_blank">Everyone Gets a Rootkit</a>.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/FourCoreLabs/EDRHunt" target="_blank">EDRHunt</a> scans Windows services, drivers, processes, registry for installed EDRs (Endpoint Detection And Response). Read more about EDRHunt <a href="https://www.fourcore.vision/blogs/Red-Team-Adventure:-Digging-into-Windows-Endpoints-for-EDRs-and-profit-cUf" target="_blank">here</a>.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
