Title: Last Week in Security (LWiS) - 2025-03-10
Date: 2025-03-10 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-03-10
Author: Erik
Summary: Detection Studio (<a href="https://x.com/sifex" target="_blank">@sifex</a>), SCCM discovery account decryption (<a href="https://x.com/unsigned_sh0rt" target="_blank">@unsigned_sh0rt</a>), FindProcessesWithNamedPipes (<a href="https://x.com/podalirius_" target="_blank">@podalirius_</a>), Windows LPE (<a href="https://x.com/MrAle_98" target="_blank">@MrAle_98</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-03-03 to 2025-03-10.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://x.com/Frichette_n/status/1897694172619870401" target="_blank">[X] Bybit hackers lacked OPSEC</a> - Some amateur mistakes, but when you walk away with $1.5B, I suppose it doesn't matter how you did it.</li>
<li><a href="https://www.cobaltstrike.com/blog/update-stopping-cybercriminals-from-abusing-cobalt-strike?utm_source=Securitylabru" target="_blank">Update: Stopping Cybercriminals from Abusing Cobalt Strike</a> - Interesting to read about a company working with Microsoft to stop the illicit use of its own products.</li>
<li><a href="https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25390" target="_blank">VMSA-2025-0004: VMware ESXi, Workstation, and Fusion updates address multiple vulnerabilities (CVE-2025-22224, CVE-2025-22225, CVE-2025-22226)</a> - We don't typically post every CVE that pops up, but these are VM escapes for ESXi and <a href="https://github.com/vmware/vcf-security-and-compliance-guidelines/tree/main/security-advisories/vmsa-2025-0004#are-the-vulnerabilities-being-exploited-in-the-wild" target="_blank">Broadcom has information to suggest that exploitation of these issues has occurred “in the wild.”</a>.</li>
<li><a href="https://techcommunity.microsoft.com/blog/windowsservernewsandbestpractices/removal-of-des-in-kerberos-for-windows-server-and-client/4386903" target="_blank">Removal of DES in Kerberos for Windows Server and Client</a> - Windows is known for its backwards compatibility, and this is proof. DES was disabled by default in 2009, but still available until 2025.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.doyensec.com/2025/03/04/exploitable-sshd.html" target="_blank">!exploitable Episode Two - Enter the Matrix</a> - Love this blast from the past - SSHNuke, a real exploit used in The Matrix Reloaded.</li>
<li><a href="https://www.elttam.com/blog/rails-sqlite-gadget-rce/" target="_blank">New Method to Leverage Unsafe Reflection and Deserialisation to Rce on Rails</a> - Deserialization bugs aren't new, but this post explores a new technique to leverage them for remote code execution on a default Rails install by using the sqlite3 gem.</li>
<li><a href="https://www.synacktiv.com/en/publications/exploiting-neverwinter-nights" target="_blank">Exploiting Neverwinter Nights</a> - The 2002 RPG game gets exploited to allow remote code execution on a client that connects to a malicious server. While the specific exploit is unlikely to be useful to you, the process of finding and creating the exploit is well documented.</li>
<li><a href="https://www.atredis.com/blog/2025/3/7/node-is-a-loader" target="_blank">Node is a loader</a> - The suggestion of using Logitech Hub as an initial access hijacked app is interesting.</li>
<li><a href="https://rastamouse.me/kerberoasting-without-tgs-reqs/" target="_blank">Kerberoasting w/o the TGS-REQ</a> - If your compromised user has an appropriate service ticket cached in their logon session, you can just <cite>describe</cite> it out and try to crack it.</li>
<li><a href="https://posts.specterops.io/decrypting-the-forest-from-the-trees-661694ed1616" target="_blank">Decrypting the Forest From the Trees</a> - "SCCM forest discovery accounts can be decrypted including accounts used for managing untrusted forests. If the site server is a managed client, service account credentials can be decrypted via the Administration Service API." There was an update to <a href="https://github.com/garrettfoster13/sccmhunter" target="_blank">sccmhunter</a> to add the <a href="https://github.com/garrettfoster13/sccmhunter/releases/tag/v.1.0.8" target="_blank">get_forestkey</a> command as well.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://detection.studio/" target="_blank">Detection Studio</a> - A new tool to help detection engineers get the most out of Sigma. Learn more <a href="https://sinn.io/detection-studio/" target="_blank">here</a>.</li>
<li><a href="https://github.com/yehia-mamdouh/ZeroProbe" target="_blank">ZeroProbe</a> - ZeroProbe is an advanced enumeration and analysis framework designed for exploit developers, security researchers, and red teamers. It provides a set of enumeration tools to identify security vulnerabilities, analyze system protections, and facilitate exploit development.</li>
<li><a href="https://www.eff.org/deeplinks/2025/03/meet-rayhunter-new-open-source-tool-eff-detect-cellular-spying" target="_blank">Meet Rayhunter: A New Open Source Tool from EFF to Detect Cellular Spying</a> - <a href="https://github.com/EFForg/rayhunter" target="_blank">rayhunter</a> turns an orbic mobile hotspot into a <a href="https://en.wikipedia.org/wiki/Stingray_phone_tracker" target="_blank">Stingray</a> detector.,</li>
<li><a href="https://github.com/MrAle98/CVE-2025-21333-POC" target="_blank">CVE-2025-21333-POC</a> - POC exploit for CVE-2025-21333 heap-based buffer overflow privilege escalation exploit for Windows 11 23H2. It leverages WNF state data and I/O ring IOP_MC_BUFFER_ENTRY. Read more <a href="https://medium.com/@ale18109800/cve-2025-21333-windows-heap-based-buffer-overflow-analysis-d1b597ae4bae" target="_blank">here</a>.</li>
<li><a href="https://github.com/p0dalirius/FindProcessesWithNamedPipes" target="_blank">FindProcessesWithNamedPipes</a> - A simple C++ Windows tool to get information about processes exposing named pipes.</li>
<li><a href="https://github.com/WildByDesign/ACLViewer" target="_blank">ACLViewer</a> - ACL Viewer for Windows.</li>
<li><a href="https://github.com/Orange-Cyberdefense/ocd-mindmaps" target="_blank">ocd-mindmaps</a> - Orange Cyberdefense mindmaps. <a href="https://github.com/Orange-Cyberdefense/ocd-mindmaps/blob/main/img/mindmap_ad_dark_classic_2025.03.excalidraw.svg" target="_blank">mindmap_ad_dark_classic_2025.03.excalidraw.svg</a> is new/updated.</li>
<li><a href="https://github.com/DarkSpaceSecurity/RunAs-Stealer" target="_blank">RunAs-Stealer</a> - RunAs Utility Credential Stealer implementing 3 techniques : Hooking CreateProcessWithLogonW, Smart Keylogging, Remote Debugging.</li>
<li><a href="https://github.com/ZephrFish/RepoMan" target="_blank">RepoMan</a> - Repoman is a command-line tool designed to automate the creation, modification, and management of Git repositories.</li>
<li><a href="https://github.com/Kryp7os/SharpRBCD" target="_blank">SharpRBCD</a> - An executable that simplifies adding the msds-AllowedToActOnBehalfOfOtherIdentity attribute for RBCD.</li>
<li><a href="https://github.com/jfmaes/phisherman" target="_blank">phisherman</a> - A real fake social engineering app.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/mk6i/retro-aim-server" target="_blank">retro-aim-server</a> - Open-source instant messaging server that makes classic AIM and ICQ clients work again. Pair it with <a href="https://github.com/mk6i/aim-for-macos" target="_blank">aim-for-macos</a> - Run classic Windows AIM on modern MacOS.</li>
<li><a href="https://github.com/som3canadian/Cloudflare-Redirector" target="_blank">Cloudflare-Redirector</a> - Just another C2 Redirector using CloudFlare.</li>
<li><a href="https://github.com/certsocietegenerale/FIR" target="_blank">FIR</a> - Fast Incident Response.</li>
<li><a href="https://github.com/R41N3RZUF477/QuickAssist_UAC_Bypass" target="_blank">QuickAssist_UAC_Bypass</a> - UAC Bypass using UIAccess program QuickAssist.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 444 (+0)</p>
<p>Blogs monitored: 406 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
