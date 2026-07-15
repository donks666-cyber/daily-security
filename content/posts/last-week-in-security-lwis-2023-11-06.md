Title: Last Week in Security (LWiS) - 2023-11-06
Date: 2023-11-06 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-11-06
Author: Erik
Summary: In-line PE runner (<a href="https://twitter.com/s4ntiago_p" target="_blank">@s4ntiago_p</a>), Citrix Bleed (<a href="https://twitter.com/assetnote" target="_blank">@assetnote</a> ), Cisco IOS XE PoC (<a href="https://twitter.com/JamesHorseman2" target="_blank">@JamesHorseman2</a>), LDAP auth (<a href="https://twitter.com/lowercase_drm" target="_blank">@lowercase_drm</a>), fuzzer fundamentals (<a href="https://twitter.com/h0mbre_" target="_blank">@h0mbre_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-10-24 to 2023-11-06.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2023/10/joint-industry-statement-of-support-for.html" target="_blank">Joint Industry statement of support for Consumer IoT Security Principles</a>. A good idea, but without teeth, what is there to keep these labels honest?</li>
<li><a href="https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/" target="_blank">Post Mortem on Cloudflare Control Plane and Analytics Outage</a>. Perhaps the worst outage in Cloudflare history. Big props for such a timely and technical Post Mortem. It's going to be a busy end of the year for their reliability engineers.</li>
<li><a href="https://blog.cloudflare.com/introducing-har-sanitizer-secure-har-sharing/" target="_blank">Introducing HAR Sanitizer: secure HAR sharing</a> - In response to the latest Okta breach, Cloudflare is recommending folks to sanitize their HAR files to minimize attack surface. We wouldn't recommend sending anyone your HAR files but this is a good response and idea for all using HAR files in your debugging workflow. I think think of a couple infosec vendors asking for HAR files for debugging. This was an interesting turn of events.</li>
<li><a href="https://www.sec.gov/news/press-release/2023-227?utm_source=danielmiessler.com&amp;utm_medium=newsletter&amp;utm_campaign=ul-no-405-my-ai-bill-deep-dive-ai-poisoning-an-ir-prep-checklist-and-discovery" target="_blank">SEC Charges SolarWinds and Chief Information Security Officer with Fraud, Internal Control Failures</a>. I guess you should actually implement the controls you tell investors you have - allegedly.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.coresecurity.com/core-labs/articles/running-pes-inline-without-console" target="_blank">Running PEs Inline Without a Console</a>. Woah. It can even run powershell without any process creation.</li>
<li><a href="https://posts.specterops.io/lateral-movement-abuse-the-power-of-dcom-excel-application-3c016d0d9922" target="_blank">Lateral Movement: Abuse the Power of DCOM Excel Application</a> - <cite>ActivateMicrosoftApp()</cite> method within the DCOM Excel application for lateral movement.</li>
<li><a href="https://medium.com/@xploiterd/ec2-user-data-to-rce-f601264a75c2" target="_blank">EC2 User-data to RCE</a> - Instance Metadata Service v1 strikes again. Migrate to SSRF -&gt; Creds -&gt; User-Data -&gt; RCE. Migrate to IMDSv2!</li>
<li><a href="https://wiki.offsecml.com/Welcome+to+the+Offensive+ML+Framework" target="_blank">Welcome to the Offensive ML Framework</a> - Excited to see if this project gets some traction. They're keeping tabs of ML use cases in offsec.</li>
<li><a href="https://medium.com/@fakasler/phishing-with-dynamite-7d33d8fac038" target="_blank">Phishing With Dynamite</a> - Pretty nifty implementation of phishing users in accessing an environment you control via the browser. Similar to phishing with <a href="https://mrd0x.com/bypass-2fa-using-novnc/" target="_blank">noVNC by Mr.d0x</a>.</li>
<li><a href="https://twitter.com/0gtweet/status/1720419490519752955" target="_blank">By-design AV bypass with "dev drive"</a> - Probably good for a few weeks. Interesting feature by MSFT. <a href="https://learn.microsoft.com/en-us/windows/dev-drive/" target="_blank">Walkthrough of Dev Drive on Windows 11</a>.</li>
<li><a href="https://thecontractor.io/data-bouncing/" target="_blank">Data-Bouncing - The art of indirect exfiltration.</a> - "....by directing web requests to certain domains that process hostnames in headers, you can relay small pieces of data to your DNS listener, allowing you to collect and reconstruct data, be it strings, files, or anything else." Using web requests to "font" a DNS request. Good to get data out of restrictive network - slowly.</li>
<li><a href="https://offsec.almond.consulting/ldap-authentication-in-active-directory-environments.html" target="_blank">LDAP authentication in Active Directory environments</a>. Great low level detail on how LDAP works and can be protected, and how to patch your tools to incorporate the new protections and continue working.</li>
<li><a href="https://www.archcloudlabs.com/projects/trendnet-731br/" target="_blank">Old CVEs Leading to New Vulns - Reverse Engineering TrendNet-731BRv1</a>. Always educational to see someone else's though process as the take a known vulnerability and recreate an exploit for it.</li>
<li><a href="https://www.assetnote.io/resources/research/citrix-bleed-leaking-session-tokens-with-cve-2023-4966" target="_blank">Citrix Bleed: Leaking Session Tokens with CVE-2023-4966</a>. From patch diff to exploit.</li>
<li><a href="https://bishopfox.com/blog/building-exploit-fortigate-vulnerability-cve-2023-27997" target="_blank">Building an Exploit for FortiGate Vulnerability CVE-2023-27997</a>. Exploit development content for the FortiGate pre-authentication remote code injection vulnerability.</li>
<li><a href="https://decoder.cloud/2023/11/03/localpotato-http-edition/" target="_blank">LocalPotato HTTP edition</a>. Another potato LPE. I really appreciate the lab setup section.</li>
<li><a href="https://www.horizon3.ai/cisco-ios-xe-cve-2023-20198-deep-dive-and-poc/" target="_blank">Cisco IOS XE CVE-2023-20198: Deep Dive and POC</a>. Not much of a deep dive as the exploit is simple.</li>
<li><a href="https://h0mbre.github.io/New_Fuzzer_Project/#" target="_blank">Fuzzer Development: The Soul of a New Machine</a>. Develop a fuzzer from scratch? Impressive.</li>
<li><a href="https://blog.nviso.eu/2023/10/26/introducing-cs2br-pt-iii-knees-deep-in-binary/" target="_blank">Introducing CS2BR pt. III - Knees deep in Binary</a>. I love authors that post their process even when it does not end in success. We learn a lot from failure!</li>
<li><a href="https://pentestlab.blog/2023/11/06/persistence-windows-telemetry/" target="_blank">Persistence - Windows Telemetry</a>. Another LOLBin and persistence mechanism.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/EspressoCake/Defender-Exclusions-Creator-BOF" target="_blank">Defender-Exclusions-Creator-BOF</a> - A BOF to add or remove Windows Defender exclusions.</li>
<li><a href="https://github.com/KingOfTheNOPs/cookie-monster" target="_blank">cookie-monster</a> - BOF to steal browser cookies.</li>
<li><a href="https://github.com/netero1010/GhostTask" target="_blank">GhostTask</a> - Create/modify scheduled tasks directly in the registry to avoid event logs and alerts.</li>
<li><a href="https://github.com/ElliotKillick/LdrLockLiberator" target="_blank">LdrLockLiberator</a> - A collection of techniques for escaping or otherwise forgoing Loader Lock while executing your code from DllMain.</li>
<li><a href="https://github.com/exotikcheat/Kernel_VADInjector" target="_blank">Kernel_VADInjector</a> - Windows 10 DLL Injector via Driver utilizing VAD and hiding the loaded driver.</li>
<li><a href="https://github.com/scriptchildie/maliciousCodeMatchingMFA" target="_blank">maliciousCodeMatchingMFA</a> - A small executable to trick a user to authenticate using code matching MFA.</li>
<li><a href="https://github.com/The-Viper-One/PsMapExec" target="_blank">PsMapExec</a> - The cme saga continues. This project is in powershell and inspired by CrackMapExec.</li>
<li><a href="https://github.com/fkasler/cuddlephish" target="_blank">cuddlephish</a> -  Weaponized Browser-in-the-Middle (BitM) for Penetration Testers.</li>
<li><a href="https://github.com/efchatz/pandora" target="_blank">pandora</a> - A red team tool that assists into extracting/dumping master credentials and/or entries from different password managers.</li>
<li><a href="https://github.com/ewby/Mockingjay_BOF" target="_blank">WIP Mockingjay BOF Conversion</a> -  Cobalt Strike Beacon Object File (BOF) Conversion of the Mockingjay Process Injection Technique.</li>
<li><a href="https://github.com/Cracked5pider/LdrLibraryEx" target="_blank">LdrLibraryEx</a> - A small x64 library to load dll's into memory.</li>
<li><a href="https://github.com/deletehead/ReleaseTheHounds" target="_blank">ReleaseTheHounds</a> -  Tool to upload large datasets and interact with BloodHound CE API.</li>
<li><a href="https://sshx.io/" target="_blank">sshx</a> - A secure web-based, collaborative terminal.</li>
<li><a href="https://github.com/G0ldenGunSec/DayBird" target="_blank">DayBird</a> - Extension functionality for the NightHawk operator client.</li>
<li><a href="https://github.com/MandConsultingGroup/porch-pirate" target="_blank">porch-pirate</a> - Porch Pirate is the most comprehensive recon / OSINT client and framework for Postman that facilitates the automated discovery and exploitation of API endpoints and secrets committed to workspaces, collections, requests, users and teams. Porch Pirate can be used as a client or be incorporated into your own applications.</li>
<li><a href="https://github.com/HaydoW/NerfDefender" target="_blank">NerfDefender</a> - BOF and C++ implementation of the Windows Defender sandboxing technique described by Elastic Security Labs/Gabriel Landau.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/SySS-Research/hashcathelper" target="_blank">hashcathelper</a> - Got some creds? Has a couple different modules. One allows operators to insert new relationships into an existing BloodHound database such as when users have the same password. Improve those screenshots!</li>
<li><a href="https://github.com/cosad3s/postleaks" target="_blank">postleaks</a> -  Search for sensitive data in Postman public library.</li>
<li><a href="https://github.com/Enelg52/OffensiveGo" target="_blank">OffensiveGo</a> - Looking to do some offensive dev in go? Start here. Notable golang tools at the bottom such as sliver and merlin.</li>
<li><a href="https://nullg0re.com/2023/09/hijacking-someone-else-dcsync/" target="_blank">Hijacking Someone Else's DCSync</a> - Friendly reminder that your AADConnect server are tier 0 assets. Pwn the AADConnect server -&gt; wait for cloud takeoff -&gt; catch hashes in flight.</li>
<li><a href="https://github.com/ElliotKillick/Mido" target="_blank">Mido</a> - The Secure Microsoft Windows Downloader.</li>
<li><a href="https://blog.xpnsec.com/unobfuscating-network-access-accounts/" target="_blank">Exploring SCCM by Unobfuscating Network Access Accounts</a> - These Network Access Accounts (NAA) accounts have been very fruitful lately...</li>
<li><a href="https://github.com/m8sec/pymeta#pymeta" target="_blank">PyMeta</a> - Pymeta will search the web for files on a domain to download and extract metadata. This technique can be used to identify: domains, usernames, software/version numbers and naming conventions.</li>
<li><a href="https://github.com/cisagov/LME" target="_blank">LME</a> -  Logging Made Easy (LME) is a free and open logging and protective monitoring solution serving all organizations. Good resource for a detection lab (<a href="https://www.detectionlab.network/" target="_blank">RIP</a>), but very manual setup.</li>
<li><a href="https://gist.github.com/GeisericII/6849bc86620c7a764d88502df5187bd0" target="_blank">Get-LoggedOn.py</a> - Lookup logged in users using itm4n's session enum via registry.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 359 (+1)</p>
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
