Title: Last Week in Security (LWiS) - 2025-08-18
Date: 2025-08-18 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-08-18
Author: Erik
Summary: DEF CON releases, PDQ SmartDeploy creds (<a href="https://x.com/unsigned_sh0rt" target="_blank">@unsigned_sh0rt</a>), FortiSIEM root command injection (<a href="https://x.com/SinSinology" target="_blank">@SinSinology</a>), a cat themed loader (<a href="https://x.com/vxunderground" target="_blank">@vxunderground</a>), fine-tune LLMs for offsec (<a href="https://x.com/kyleavery_" target="_blank">@kyleavery_</a>), juicing NTDS.DIT (<a href="https://x.com/mgrafnetter" target="_blank">@MGrafnetter</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-08-04 to 2025-08-18.</p>
<aside class="m-note m-success">
This is a big post with lots of links from Black Hat and DEF CON releases! We certainly didn't cover everything, but we did our best. Let us know if we missed your favorite tool/technique/write-up!</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://x.com/0xzak/status/1955265807807545763" target="_blank">[X] Malicious Cursor extension drains wallet</a> - Editor extensions are still the wild west, and this is not the first and will not be the last malicious extension uploaded to OpenVSX and promoted as legitimate.</li>
<li><a href="https://data.ddosecrets.com/APT%20Down%20-%20The%20North%20Korea%20Files/article.txt" target="_blank">APT Down - The North Korea Files</a> - Someone got access to an alleged North Korean APT's workstation and Virtual Private Sever (VPS). They were kind enough to dump the files and write it up. This data is a gold mine for threat intel analysts.</li>
<li><a href="https://www.theregister.com/2025/08/12/hyundai_want_secure_locks_on/" target="_blank">Hyundai: Want cyber-secure car locks? That'll be £49, please</a> - Charging customers for security updates on high end physical products is a new one.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.ndss-symposium.org/wp-content/uploads/2025-2065-paper.pdf" target="_blank">[PDF] GhostShot: Manipulating the Image of CCD Cameras with Electromagnetic Interference</a> - The maximum demonstrated distance was 1 meter, but very cool research on how you can trick a digital camera to show detailed images with specialized electromagnetic interference.</li>
<li><a href="https://specterops.io/blog/2025/08/12/hklmsystemsetupsmartdeploy-the-static-keys-to-abusing-pdq-smartdeploy/" target="_blank">HKLMSYSTEMSetupsMarTdEpLoY –  The (Static) Keys to Abusing PDQ SmartDeploy</a> - Static, hardcoded, universal encryption keys just add a step for attackers, they don't actually protect anything. This is another research article and tool release enabled by <a href="https://ludus.cloud" target="_blank">Ludus</a>.</li>
<li><a href="https://exploits.forsale/pwn2own-2024/" target="_blank">CVE-2024-30088 Pwning Windows Kernel @ Pwn2Own Vancouver 2024 (Plus Xbox)</a> - New drivers == new vulnerabilities.</li>
<li><a href="https://blog.talosintelligence.com/revault-when-your-soc-turns-against-you-2/" target="_blank">ReVault! When your SoC turns against you… deep dive edition</a> - What if the security chip in your laptop was actually a backdoor? This research into the Dell ControlVault shows what is possible when the dedicated security hardware is compromised.</li>
<li><a href="https://labs.watchtowr.com/should-security-solutions-be-secure-maybe-were-all-wrong-fortinet-fortisiem-pre-auth-command-injection-cve-2025-25256/" target="_blank">Should Security Solutions Be Secure? Maybe We're All Wrong - Fortinet FortiSIEM Pre-Auth Command Injection (CVE-2025-25256)</a> - A simple command injection, as root, in "the backbone of your security operations team and is your ultimate defense against attacks." I wish it was surprising.</li>
<li><a href="https://pentest.party/posts/2025/ksetup-machine-password/" target="_blank">Machine Account Takeover with LsaStorePrivateData()</a> - A good alternative to getting machine account credentials when you're a local administrator but don't/can't dump LSA.</li>
<li><a href="https://specterops.io/blog/2025/08/14/juicing-ntds-dit-files-last-drop-dsinternals-powershell-active-directory-offline-attacks/" target="_blank">Juicing ntds.dit Files to the Last Drop</a> - The Golden dMSA Attack, full support for Local Administrator Password Solution (LAPS), and the ability to extract trust passwords and BitLocker recovery keys have been added to <a href="https://www.powershellgallery.com/packages/DSInternals/6.1" target="_blank">DSInternals</a>.</li>
<li><a href="https://specterops.io/blog/2025/08/15/pantheon-introduction-a-guide-and-script-collection-for-mythic-eventing/" target="_blank">Pantheon Introduction: A Guide and Script Collection for Mythic Eventing</a> - A repository containing eventing automation which include reconnaissance, persistence location, and credential preparation scripts</li>
<li><a href="https://specterops.io/blog/2025/08/13/going-for-brokering-offensive-walkthrough-for-nested-app-authentication/" target="_blank">Going for Broke(ring) – Offensive Walkthrough for Nested App Authentication</a> - Microsoft uses nested app authentication (NAA) for many applications. Access and refresh tokens for select applications, such as administrator portals, can be exchanged for tokens to other applications with a brokered request to authentication endpoints.</li>
<li><a href="https://cicada-8.medium.com/impacket-developer-guide-part-1-rpc-4df4fe6d79d7" target="_blank">Impacket Developer Guide. Part 1. RPC Deep Dive</a> - Ever feel overwhelmed about contributing or modifying the impacket project? Start here!</li>
<li><a href="https://www.outflank.nl/blog/2025/08/07/training-specialist-models/" target="_blank">Training Specialist Models: Automating Malware Development</a> - The future is here. Payload development now includes LLM that make decisions and modifications when going up against certain EDRs at a specific point in time. Imagine a pipeline where <a href="https://ludus.cloud/" target="_blank">Ludus</a>, LLMs, automation, Multiple VMs/OS types, and multiple EDR technologies are all working together to generate a payload that works when you need it to.</li>
<li><a href="https://portswigger.net/research/http1-must-die" target="_blank">HTTP/1.1 must die: the desync endgame</a> - This paper introduces several novel classes of HTTP desync attack capable of mass compromise of user credentials. Biggest takeaway here: <a href="https://http1mustdie.com/" target="_blank">HTTP/1.1 is insecure</a>. Here is an example of <a href="https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn#paypal" target="_blank">PayPal</a> learning this lesson.</li>
<li><a href="https://blog.amberwolf.com/blog/2025/august/breaking-into-your-network-zer0-effort/" target="_blank">Breaking Into Your Network? Zer0 Effort. - DEF CON 33 Overview</a> - Teased in the last edition of LWiS, this post covers the bugs disclosed at DEF CON in popular zero trust network solutions. It includes a <a href="https://vimeo.com/1109180896" target="_blank">link to the full talk</a> given at DEF CON as well!</li>
<li><a href="https://www.youtube.com/watch?v=z6GJqrkL0S0" target="_blank">DEFCON33 - Turning Microsoft's Login Page into our Phishing Infrastructure - Keanu Nys</a> - Phish using the legitimate Microsoft Login page? Say less. Awesome DEFCON33 Talk. Highly practical is todays landscape.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://hashcat.net/forum/thread-13330.html" target="_blank">hashcat v7.0.0</a> - Lots of updates including hash-mode autodetection, docker build support, Apple Metal GPU support, AMD HIP support, Argon2 and Summary algorithm support, and much more.</li>
<li><a href="https://github.com/m3rcer/IRvana" target="_blank">IRvana</a> - Slaying multi-language LLVM IR with obfuscation passes to achieve JIT execution.</li>
<li><a href="https://github.com/Fudgedotdotdot/dump_kerberos_tickets" target="_blank">dump_kerberos_tickets</a> - Dump Kerberos tickets.</li>
<li><a href="https://github.com/Fudgedotdotdot/nimpersonate" target="_blank">nimpersonate</a> - Impersonate Windows tokens in Nim.</li>
<li><a href="https://vx-api.gitbook.io/vx-api/my-projects/meow-meow-kitty-cat-meow-meow" target="_blank">Meow Meow Kitty Cat Meow Meow</a> - A new project from <a href="https://x.com/vxunderground" target="_blank">@vxunderground</a>. "Insert" will hide your payload in a BMP, "Pspsps" extracts payloads from BMPs, and "Loader" is a loader with dynamic syscall resolution that extracts a payload from a BMP and executes it in memory.</li>
<li><a href="https://github.com/curi0usJack/ludus_badblood" target="_blank">ludus_badblood</a> - Outfits your ludus AD domain with BadBlood info.</li>
<li><a href="https://github.com/jumpycastle/rre-burp" target="_blank">rre-burp</a> - Burp extension for Recursive Request Exploits (RRE) — DEF CON 2025.</li>
<li><a href="https://github.com/8ales/Azure-AppHunter" target="_blank">Azure-AppHunter</a> - Azure AppHunter is an open-source tool created for security researchers, red teamers and defenders to help them identify excessive privileges assigned to Service Principals.</li>
<li><a href="https://github.com/praetorian-inc/turnt" target="_blank">turnt</a> - A tool designed for smuggling interactive command and control traffic through legitimate TURN servers hosted by reputable providers such as Zoom.</li>
<li><a href="https://github.com/praetorian-inc/oauthseeker" target="_blank">oauthseeker</a> - A malicious OAuth application that can be leveraged for both internal and external phishing attacks targeting Microsoft Azure and Office365 users.</li>
<li><a href="https://github.com/praetorian-inc/glato" target="_blank">glato</a> - GitLab Attack TOolkit. [Not to be confused with <a href="https://github.com/praetorian-inc/gato" target="_blank">gato</a> - GitHub Actions Pipeline Enumeration and Attack Tool.]</li>
<li><a href="https://github.com/praetorian-inc/ChromeAlone" target="_blank">ChromeAlone</a> - A tool to transform Chromium browsers into a C2 Implant.</li>
<li><a href="https://github.com/praetorian-inc/janus-framework" target="_blank">janus-framework</a> is a powerful Go library for chaining security tools together to create complex, reusable workflows that can run at scale. It provides a uniform interface for connecting disparate security tools, enabling automation of multi-step security processes.</li>
<li><a href="https://github.com/synacktiv/gpoParser" target="_blank">gpoParser</a> - gpoParser is a tool designed to extract and analyze configurations applied through Group Policy Objects (GPOs) in an Active Directory environment.</li>
<li><a href="https://github.com/rubenformation/CVE-2025-50154" target="_blank">CVE-2025-50154</a> - POC for CVE-2025-50154, a zero day vulnerability on windows file explorer disclosing NTLMv2-SSP without user interaction. It is a bypass for the CVE-2025-24054 Security Patch.</li>
<li><a href="https://github.com/kidtronnix/restless-guest" target="_blank">restless-guest</a> - An offensive toolkit for restless guests #DEFCON33.</li>
<li><a href="https://github.com/Semperis/EntraGoat" target="_blank">EntraGoat</a> - A deliberately vulnerable Microsoft Entra ID environment. Learn identity security through hands-on, realistic attack challenges.</li>
<li><a href="https://github.com/SafeBreach-Labs/RPC-Racer" target="_blank">RPC-Racer</a> - Toolset to manipulate RPC clients by finding delayed services and masquerading as them.</li>
<li><a href="https://github.com/m8sec/dispatch" target="_blank">Dispatch</a> - Evasive Payload Delivery Server &amp; C2 Redirector.</li>
<li><a href="https://github.com/olafhartong/BamboozlEDR" target="_blank">BamboozlEDR</a> - A comprehensive ETW (Event Tracing for Windows) event generation tool designed for testing and research purposes.</li>
<li><a href="https://github.com/SpecterOps/JamfHound" target="_blank">JamfHound</a> - JamfHound is a python3 project designed to collect and identify attack paths in Jamf Pro tenants based on existing object permissions by outputting data as JSON for ingestion into BloodHound.</li>
<li><a href="https://github.com/garrettfoster13/NotSoSmartDeploy" target="_blank">NotSoSmartDeploy</a> - POC to decrypt SmartDeploy encrypted credentials.</li>
<li><a href="https://github.com/dmcxblue/AzureStrike" target="_blank">AzureStrike</a> - An HTA Application which builds Azure (Entra) Scenarios for Red Team Simulations.</li>
<li><a href="https://github.com/sikumy/sauron" target="_blank">sauron</a> - Fast context enumeration for newly obtained Active Directory credentials.</li>
<li><a href="https://github.com/sikumy/spearspray" target="_blank">spearspray</a> - Enhance Your Active Directory Password Spraying with User Intelligence.</li>
<li><a href="https://github.com/123ojp/GREtunnel-scanner" target="_blank">GREtunnel-scanner</a> - This is a GRE PoC code for Talks: From Spoofing to Tunneling: New Red Team's Networking Techniques for Initial Access and Evasion.</li>
<li><a href="https://github.com/scottctaylor12/C4" target="_blank">C4</a> - Cross Compatible Command and Control.</li>
<li><a href="https://github.com/arosenmund/defcon33_silence_kill_edr" target="_blank">defcon33_silence_kill_edr</a> - DC33 workshop: "Putting EDRs in Their place"</li>
<li><a href="https://github.com/knight0x07/WinRAR-CVE-2025-8088-PoC-RAR" target="_blank">WinRAR-CVE-2025-8088-PoC-RAR</a> - WinRAR 0day CVE-2025-8088 PoC RAR Archive.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/cisagov/thorium" target="_blank">thorium</a> - A scalable file analysis and data generation platform that allows users to easily orchestrate arbitrary docker/vm/shell tools at scale.</li>
<li><a href="https://github.com/123ojp/VxLAN-Scanner" target="_blank">VxLAN-Scanner</a> - This is a VxLAN PoC code for Talks: From Spoofing to Tunneling: New Red Team's Networking Techniques for Initial Access and Evasion.</li>
<li><a href="https://github.com/MythicMeta/Pantheon" target="_blank">Pantheon</a> - Community Eventing and Scripting examples.</li>
<li><a href="https://specterops.io/blog/2025/08/11/certify-2-0/" target="_blank">Certify 2.0</a> Certify has been updated to 2.0 and it includes a much needed update. Nearly twice the amount of ADCS tradecraft has been introduced since the initial release.</li>
<li><a href="https://github.com/Sleepw4lker/TameMyCerts" target="_blank">TameMyCerts</a> - Policy Module for Microsoft Active Directory Certificate Services.</li>
<li><a href="https://github.com/sensepost/bloatware-pwn" target="_blank">bloatware-pwn</a> - LPE / RCE Exploits for various vulnerable "Bloatware" products.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 455 (+0)</p>
<p>Blogs monitored: 424 (+0)</p>
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
