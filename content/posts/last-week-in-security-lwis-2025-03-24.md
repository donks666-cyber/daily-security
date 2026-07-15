Title: Last Week in Security (LWiS) - 2025-03-24
Date: 2025-03-24 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-03-24
Author: Erik
Summary: Next.js auth bypass (<a href="https://x.com/zhero___" target="_blank">@zhero___</a> + <a href="https://x.com/inzo____" target="_blank">@inzo____</a>), ServiceNow for red teamers (<a href="https://x.com/__invictus_" target="_blank">@__invictus_</a>), Veeam RCE - again! (<a href="https://x.com/chudyPB" target="_blank">@chudyPB</a>), ArgFuscator (<a href="https://x.com/wietze" target="_blank">@Wietze</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-03-17 to 2025-03-24.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://cloud.google.com/blog/products/identity-security/google-announces-agreement-acquire-wiz" target="_blank">Google + Wiz: Strengthening Multicloud Security</a> - $32 billion... Google is positioning itself to be the "security" cloud provider after the Mandiant and Wiz acquisitions.</li>
<li><a href="https://trustedsec.com/blog/trimarc-joins-trustedsec-strengthening-our-commitment-to-security" target="_blank">Trimarc Joins TrustedSec: Strengthening Our Commitment to Security</a> - TrustedSec snatches Sean Metcalf and his team! Good luck guys!</li>
<li><a href="https://www.bleepingcomputer.com/news/security/microsoft-trusted-signing-service-abused-to-code-sign-malware/" target="_blank">Microsoft Trusted Signing service abused to code-sign malware</a> - The Microsoft hosted signing service is being abused to sign malware. Why not use the Azure service when it's cheap and easy?</li>
<li><a href="https://www.theatlantic.com/politics/archive/2025/03/trump-administration-accidentally-texted-me-its-war-plans/682151/?gift=kPTlqn0J1iP9IBZcsdI5IVJpB2t9BYyxpzU4sooa69M" target="_blank">The Trump Administration Accidentally Texted Me Its War Plans</a> - Politics aside, the planning and dissemination of national security information via Signal is wild. This is why iOS 0days are so valuable; with access to the phone all the end-to-end encryption isn't worth anything and an adversary can just read the messages out of Signal's database. One wonders what would happen to an Army soldier who shared operational details via Signal and if that same punishment will befall any members of this group chat. The US Director of National Intelligence, who was in the Signal group where the information was shared, <a href="https://x.com/DNIGabbard/status/1900525561786646903" target="_blank">tweeted</a> on 2025-03-14 (10 days ago) "Any unauthorized release of classified information is a violation of the law and will be treated as such." We shall see.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://zhero-web-sec.github.io/research-and-things/nextjs-and-the-corrupt-middleware" target="_blank">Next.js and the corrupt middleware: the authorizing artifact</a> - Adding a header can bypass any middleware (i.e. authentication) of unpatched Next.js applications.</li>
<li><a href="https://blog.cloudflare.com/browser-based-rdp/" target="_blank">RDP without the risk: Cloudflare's browser-based solution for secure third-party access</a> - Put RDP behind the secured Cloudflare Zero Trust platform (i.e. hardware 2FA) without any configuration changes to Windows endpoint. If you can get over the fact that Cloudflare is a TLS Man-in-the-middle for all your traffic, it's an amazing solution to many security issues.</li>
<li><a href="https://www.mdsec.co.uk/2025/03/red-teaming-with-servicenow/" target="_blank">Red Teaming with ServiceNow</a> - This is adversary simulation at its finest. Any "red team" can phish and deploy some beacons, but the true pros are understanding the network better than the defenders and using their own tools against them. This is how the <a href="https://youtube.com/watch?v=bDJb8WOJYdA&amp;t=96" target="_blank">pros</a> do it.</li>
<li><a href="https://blog.lexfo.fr/glpi-sql-to-rce.html" target="_blank">Pre-authentication SQL injection to RCE in GLPI (CVE-2025-24799/CVE-2025-24801)</a> - GLPI SQLI (pre-auth) and authenticated RCE. Happy hunting!</li>
<li><a href="https://securityintelligence.com/x-force/bypassing-windows-defender-application-control-loki-c2/" target="_blank">Bypassing Windows Defender Application Control with Loki C2</a> - <a href="https://x.com/0xBoku" target="_blank">0xBoku</a> keeps cooking Loki C2. This time he is bypassing Windows Defender Application Control (WDAC) by exploiting trusted Microsoft Electron applications. While Loki C2 hasn't been released yet, the community is already creating POCs like <a href="https://github.com/smokeme/asar-backdoor" target="_blank">asar-backdoor</a>.</li>
<li><a href="https://labs.watchtowr.com/by-executive-order-we-are-banning-blacklists-domain-level-rce-in-veeam-backup-replication-cve-2025-23120/" target="_blank">By Executive Order, We Are Banning Blacklists - Domain-Level RCE in Veeam Backup &amp; Replication (CVE-2025-23120)</a> - You patched that Veeam RCE? Oops, it's vulnerable again! Another entry in the "just because it's patched doesn't mean it's not vulnerable" file.</li>
<li><a href="https://portswigger.net/research/saml-roulette-the-hacker-always-wins" target="_blank">SAML roulette: the hacker always wins</a> - The SAML bug from last week written up in detail for Gitlab.</li>
<li><a href="https://blog.doyensec.com/2025/03/18/exploitable-gitlab.html" target="_blank">!exploitable Episode Three - Devfile Adventures</a> - A nice write up of the 2024 Gitlab path traversal bug in devfiles. Comes complete with an exploit: <a href="https://github.com/doyensec/malicious-devfile-registry" target="_blank">malicious-devfile-registry</a> - Exploit for CVE-2024-0402 in Gitlab.</li>
<li><a href="https://www.wietzebeukema.nl/blog/bypassing-detections-with-command-line-obfuscation" target="_blank">Bypassing Detections with Command-Line Obfuscation</a> - The regex you cooked up to detected "malicious" command line args? Probably not considering all the edge cases! Check out the tool: <a href="https://argfuscator.net/" target="_blank">ArgFuscator</a>.</li>
<li><a href="https://gosecure.ai/blog/2025/03/21/talk-to-your-malware-integrating-ai-capability-in-an-open-source-c2-agent/" target="_blank">Talk To Your Malware – Integrating AI Capability in an Open-Source C2 Agent</a> - This isn't another <a href="https://www.anthropic.com/news/model-context-protocol" target="_blank">Model Context Protocol</a> for Mythic, it's a <cite>prompt</cite> command you can use to trust (i.e. YOLO) an LLM to do actions you describe in plain english.</li>
<li><a href="https://www.netspi.com/blog/technical-blog/adversary-simulation/the-future-of-beacon-object-files/" target="_blank">The Things We Think and Do Not Say: The Future of Our Beacon Object Files (BOFs)</a> - Beacon Object Files (BOFs) came to Cobalt Strike, and soon many C2s, in 2020. Five years later, it's worth discussing how BOFs can be improved. This post even comes with <a href="https://github.com/NetSPI/BOF-PE" target="_blank">BOF-PE</a> - An example reference design for a proposed BOF PE.</li>
<li><a href="https://bishopfox.com/blog/rust-for-malware-development" target="_blank">Rust for Malware Development</a> - "Rewrite it in rust" comes for malware.</li>
<li><a href="https://whiteknightlabs.com/2025/03/24/understanding-windows-kernel-pool-memory/" target="_blank">Understanding Windows Kernel Pool Memory</a> - Some low level investigation of the Windows Kernel including memory types, debugging in WinDbg, and analyzing pool tags.</li>
<li><a href="https://therealunicornsecurity.github.io/What-not-to-do-with-vms/" target="_blank">What not to do with on prem virtualization</a> - Don't underestimate the value of .vmdk disk files - they contain everything!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/orlyjamie/spinningcat/" target="_blank">spinningcat</a> - A program to "demonstrate impact" by filling the target's screen with a cat gif and playing techno music (based on: <a href="https://github.com/orlyjamie/spinningcat/" target="_blank">spinningcat</a>).</li>
<li><a href="https://github.com/carlospolop/cloudpeass" target="_blank">CloudPEASS</a> - The current goal of Cloud PEASS is simple: Once you manage to get some credentials to access Azure, GCP or AWS, use different techniques to get the permissions the principal has and highlight all the potential attacks (privilege escalation, read sensitive information, etc) it's possible to do. [Note: this is the first tool I've seen to ship data to an LLM by default (that isn't explicitly an AI based tool). Be careful with sensitive data]</li>
<li><a href="https://github.com/0x6rss/CVE-2025-24071_PoC" target="_blank">CVE-2025-24071_PoC</a> - NTLM Hash Leak via RAR/ZIP Extraction and .library-ms File.</li>
<li><a href="https://github.com/Verizon/verizon_burp_extensions_ai" target="_blank">verizon_burp_extensions_ai</a> - Verizon Burp Extensions: AI Suite.</li>
<li><a href="https://github.com/aydinnyunus/CVE-2025-29927" target="_blank">CVE-2025-29927</a> - Vulnerability in Next.js where the internal header x-middleware-subrequest can be used to bypass middleware checks like authentication.</li>
<li><a href="https://github.com/frack113/ludus_ghosts_server" target="_blank">ludus_ghosts_server</a> - Ansible GHOSTS server role for <a href="https://ludus.cloud/" target="_blank">Ludus</a>.</li>
<li><a href="https://github.com/thinkst/defending-off-the-land" target="_blank">defending-off-the-land</a> - Assortment of scripts and tools for our Blackhat EU 2024 talk. [The <cite>file_access_token</cite> is so cool!]</li>
<li><a href="https://github.com/V-i-x-x/kernel-callback-removal" target="_blank">kernel-callback-removal</a> - kernel callback removal (Bypassing EDR Detections).</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/jfmaes/phisherman" target="_blank">phisherman</a> - A real fake social engineering app.</li>
<li><a href="https://iis-blogs.azurewebsites.net/brian-murphy-booth/the-biggest-mistake-serviceprincipalname-s" target="_blank">The biggest mistake: ServicePrincipalName’s</a> - Old blog but still valuable. Must read for all kerberos enthusiast or anyone confused about what SPNs are.</li>
<li><a href="https://github.com/projectdiscovery/nuclei-templates-labs" target="_blank">nuclei-templates-labs</a> - Vulnerable environments paired with ready-to-use Nuclei templates for security testing and learning! 🚀.</li>
<li><a href="https://github.com/Zouuup/landrun" target="_blank">landrun</a> - Run any Linux process in a secure, unprivileged sandbox using Landlock LSM. Think firejail, but lightweight, user-friendly, and baked into the kernel.</li>
<li><a href="https://github.com/MichaelGrafnetter/active-directory-firewall" target="_blank">active-directory-firewall</a> - Active Directory Firewall.</li>
<li><a href="https://github.com/Cryakl/Ultimate-RAT-Collection" target="_blank">Ultimate-RAT-Collection</a> - For educational purposes only, exhaustive samples of 450+ classic/modern trojan builders including screenshots.</li>
<li><a href="https://cascii.app/" target="_blank">cascii</a> is a web-based ASCII and Unicode diagram builder written in vanilla Javascript.</li>
<li><a href="https://en.wikipedia.org/wiki/Time_crystal" target="_blank">Time crystal</a> - 🤯</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 446 (+1)</p>
<p>Blogs monitored: 407 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>X: <a href="https://x.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
