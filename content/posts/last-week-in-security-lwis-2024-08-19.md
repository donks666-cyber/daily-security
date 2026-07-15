Title: Last Week in Security (LWiS) - 2024-08-19
Date: 2024-08-19 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-08-19
Author: Erik
Summary: DEF CON 32 Tools and Talks, Apache confusion (<a href="https://x.com/orange_8361" target="_blank">Orange Tsai</a>), private TLDs (<a href="https://x.com/n7wera" target="_blank">@N7WEra</a>), UDL 🎣 (<a href="https://x.com/Oddvarmoe" target="_blank">@Oddvarmoe</a>), crash analysis (<a href="https://x.com/patrickwardle" target="_blank">@patrickwardle</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-07-29 to 2024-08-19.</p>
<aside class="m-block m-success">
<h3>DEF CON Recap</h3>
<p>We had a great time at DEF CON, introducing over 700 people to <a href="https://ludus.cloud/" target="_blank">Ludus</a> with a self-paced IP camera hacking workshop in the Embedded Systems Village. We also dropped <a href="https://github.com/badsectorlabs/sccm-http-looter" target="_blank">sccm-http-looter</a> at our talk in the Red Team Village. Slides from the talk are in the repo.</p>
<p>Did we miss your favorite talk or tool? Let us know!</p>
<p>Interested in sponsoring LWiS? Email us at blog (at) badsectorlabs.com</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards" target="_blank">NIST Releases First 3 Finalized Post-Quantum Encryption Standards</a> -- One encryption and two signature algorithms have been standardized with one more signature algorithm on the way. This is good news as quantum computing slowly builds up steam.</li>
<li><a href="https://www.sec.gov/Archives/edgar/data/1740742/000182912624005571/unicoin_8k.htm" target="_blank">Unicoin Inc.</a> - Nightmare scenario? "...threat actor had gained access to the Company's Google G-Suite account and changed passwords of all users of the Company's G-Suite products". The question is, should red teams emulate these scenarios, or how should they prove that level of access non-destructively?</li>
<li><a href="https://blog.cloudflare.com/ja4-signals" target="_blank">Advancing Threat Intelligence: JA4 fingerprints and inter-request signals</a> - Cloudflare clients are getting some improved detection capabilities.</li>
<li><a href="https://www.justice.gov/opa/pr/justice-department-disrupts-north-korean-remote-it-worker-fraud-schemes-through-charges-and?is=3bf4c01caca61e2c18827898761fda68b574b79086fbdb1c8a12f66a5527e845" target="_blank">Justice Department Disrupts North Korean Remote IT Worker Fraud Schemes Through Charges and Arrest of Nashville Facilitator</a> - Have you added this to your threat profile? Insider threat has become more of a reality over time. Assumed breach engagements should almost be a requirement at this point. Also, if someone wants to host a laptop farm in your house, just say no.</li>
<li><a href="https://x.com/f4rmpoet/status/1825472703223992323" target="_blank">[X] Closer look at CVE-2024-38063 (Windows TCPIP RCE).</a> - There was lots of chatter about a 9.8 CVSS unauthenticated, pre-firewall, RCE vulnerability in Windows TCP/IP driver. It looks like it <em>may</em> not be as bad as it sounds.</li>
<li><a href="http://phrack.org/issues/71/1.html" target="_blank">Phrak 71</a> - The legendary zine is still going strong 40 years later.</li>
<li><a href="https://x.com/mattkorda/status/1823376298997162151" target="_blank">[X] PSA: don't share workout pics on Instagram, otherwise a big nerd (me) might use them to learn things about your nuclear weapons.</a> - Never underestimate the power of OSINT.</li>
<li><a href="https://krebsonsecurity.com/2024/08/nationalpublicdata-com-hack-exposes-a-nations-data/" target="_blank">NationalPublicData.com Hack Exposes a Nation's Data</a> - If you live in the US, your social security number, address, and more is likely exposed. Freeze your credit. Welcome to the boring dystopia. How did this happen? Well, <a href="https://krebsonsecurity.com/2024/08/national-public-data-published-its-own-passwords/" target="_blank">National Public Data Published Its Own Passwords</a>. 🤦‍♂️</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.orange.tw/2024/08/confusion-attacks-en.html?m=1" target="_blank">[EN] Confusion Attacks: Exploiting Hidden Semantic Ambiguity in Apache HTTP Server!</a> - <a href="https://x.com/orange_8361" target="_blank">Orange Tsai</a> with their annual wizardry. The talk can be found <a href="https://i.blackhat.com/BH-US-24/Presentations/US24-Orange-Confusion-Attacks-Exploiting-Hidden-Semantic-Thursday.pdf" target="_blank">here [PDF]</a>.</li>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/enumerating-private-tlds/" target="_blank">Hacking Beyond .com — Enumerating Private TLDs</a> - Add TLDs to your recon checklist. Tool now available.</li>
<li><a href="https://blog.chebuya.com/posts/unauthenticated-remote-command-execution-on-byob/" target="_blank">Unauthenticated remote code execution on BYOB via spoofed file exfiltration+command injection</a> - Working code released as well. This exploit in BYOB (Build Your Own Botnet) [an open-source post-exploitation framework for students, researchers and developers] works by spoofing an agent exfiltrating a file to overwrite the sqlite database and bypass authentication. After authentication is bypassed, a command injection vulnerability is exploited in the payload builder page.</li>
<li><a href="https://blog.projectdiscovery.io/introducing-httpx-dashboard-2/" target="_blank">Introducing the httpx dashboard</a> - Get your httpx results in the PD dashboard now!</li>
<li><a href="https://www.fullspectrum.dev/catching-shells-without-infrastructure-using-open-tor-relays/" target="_blank">Catching Shells Without Infrastructure Using "Open" Tor Relays.</a> - By leveraging "open" Tor relays as entry points and Tor hidden services as listeners, attackers could potentially run small, stealthy implants that connect back through the Tor network. I'd bet most enterprise FW would block this outbound traffic though? Maybe a good measurable event to have as part of your red/purple teams.</li>
<li><a href="https://decoder.cloud/2024/08/02/the-fake-potato/" target="_blank">The “Fake” Potato</a> - There are never enough potatoes!</li>
<li><a href="https://ghostwriteattack.com/" target="_blank">GhostWrite</a> - The GhostWrite vulnerability affects the T-Head XuanTie C910 and C920 RISC-V CPUs. This vulnerability allows unprivileged attackers, even those with limited access, to read and write any part of the computer's memory and to control peripheral devices like network cards. Worst part? It's a hardware bug that can't be patched.</li>
<li><a href="https://habr.com/ru/companies/ru_mts/articles/832892/" target="_blank">The quarantine! Infecting .NET-assembly as a real APT</a> -  This article is a deep dive into how hackers can mess with .NET assemblies in Windows to sneak in malicious code, with examples of different techniques they might use. Google translate is your friend.</li>
<li><a href="https://flatt.tech/research/posts/beyond-the-limit-expanding-single-packet-race-condition-with-first-sequence-sync/" target="_blank">Beyond the Limit: Expanding single-packet race condition with a first sequence sync for breaking the 65,535 byte limit</a> - To overcome the limitation of a single packet attack, use IP fragmentation and TCP sequence number reordering.</li>
<li><a href="https://www.pentestpartners.com/security-blog/knowbe4-rce-and-lpe/" target="_blank">KnowBe4 RCE and LPE</a> - Couple vulns from KnowBe4 applications. Good write-ups!</li>
<li><a href="https://trustedsec.com/blog/oops-i-udld-it-again" target="_blank">Oops I UDL'd it Again</a> - New phishing technique! Universal Data Link Configuration (UDL) files to leak NTLM or even plaintext creds (if the user enters them).</li>
<li><a href="https://cymulate.com/blog/exploiting-pta-credential-validation-in-azure-ad/" target="_blank">Double Agent: Exploiting Pass-through Authentication Credential Validation in Azure AD</a> - Remember your Entra Connect servers are Tier 0 assets. "...the issue is not an immediate threat and is of moderate severity."</li>
<li><a href="https://objective-see.org/blog/blog_0x7B.html" target="_blank">The Hidden Treasures of Crash Reports</a> - This post discusses how crash reports can reveal malware, bugs, and system vulnerabilities, providing examples from major security incidents. I like the idea of using crash reports as recon as well.</li>
<li><a href="https://hacktodef.com/addressed-aws-defaults-risks-oidc-terraform-and-anonymous-to-administratoraccess" target="_blank">Addressed AWS defaults risks: OIDC, Terraform and Anonymous to AdministratorAccess</a> - If you know the AWS account ID and the name of a role that doesn't have the "subject" condition, then you can compromise that AWS account from the internet. These types of flaws are wild. Like likely affects other OIDC-based roles.</li>
<li><a href="https://www.synacktiv.com/publications/sccmsecretspy-exploiting-sccm-policies-distribution-for-credentials-harvesting-initial" target="_blank">SCCMSecrets.py: exploiting SCCM policies distribution for credentials harvesting, initial access and lateral movement</a> - The team at Synacktiv was also scoping out the SSCM DP HTTP service for looting. They gave us a shoutout in the footnote as well. Great work guys!</li>
<li><a href="https://labs.jumpsec.com/ssh-tunnelling-to-punch-through-corporate-firewalls-updated-take-on-one-of-the-oldest-lolbins/" target="_blank">SSH Tunnelling to Punch Through Corporate Firewalls - Updated take on one of the oldest LOLBINs</a> - Some tradecraft on using the SSH client in windows environments. More talked about the past year or so but it's been around windows by default for a few years (2017)</li>
<li><a href="https://blacktop.github.io/ipsw/blog/kernel-symbolication/" target="_blank">Kernel Symbolication</a> - The article explains how the symbolication process works, describes the signature format, and discusses the importance of this capability for reverse engineers and security researchers analyzing Apple's kernel internals.</li>
<li><a href="https://www.akamai.com/blog/security-research/2024-august-kubernetes-gitsync-command-injection-defcon" target="_blank">Git-Syncing into Trouble: Exploring Command Injection Flaws in Kubernetes</a> - DEF CON talk: Akamai researcher Tomer Peled found a design flaw in Kubernetes' sidecar project git-sync that allows for potential command injection. This vulnerability can be exploited on default installations of Kubernetes on all platforms (including Amazon Elastic Kubernetes Service (EKS), Azure Kubernetes Service (AKS), and Google Kubernetes Engine (GKE), and  Linode) and is no considered a vulnerability by the Kubernetes team.</li>
<li><a href="https://blog.syss.com/posts/hacking-a-secure-industrial-remote-access-gateway/" target="_blank">Hacking a Secure Industrial Remote Access Gateway</a> - XSS + command injection as root in the Cosy+ gateway allow unauthenticated attackers to gain root access to the device. Syss went deep on this device, and its a great post on how you can tear apart an embedded system.</li>
<li><a href="https://www.semperis.com/blog/unoauthorized-privilege-elevation-through-microsoft-applications/" target="_blank">UnOAuthorized: Privilege Elevation Through Microsoft Applications</a> - Cloud based (Entra ID) privilege escalation. Already patched but cool read. Detection for prior abuse is provided.</li>
<li><a href="https://dirkjanm.io/persisting-with-federated-credentials-entra-apps-managed-identities/" target="_blank">Persisting on Entra ID applications and User Managed Identities with Federated Credentials</a> - More Entra ID based work. Dirk-jan shows an alternative approach attackers can use to configure credentials on Entra ID applications and Azure User Managed Identities. It can help them persist in environments or even elevate privileges if they can compromise a service principal with high privileges.</li>
<li><a href="https://chesterlebron.blogspot.com/2024/08/my-methodology-to-aws-detection-engineering-part-1.html" target="_blank">My Methodology to AWS Detection Engineering (Part 1: Object Selection)</a> - The start of a detection engineering series in AWS using Splunk.</li>
<li><a href="https://securityintelligence.com/x-force/little-bug-that-could/" target="_blank">Racing Round and Round: The Little Bug That Could</a> - The write-up of CVE-2024-30089 which is an use-after-free vuln in Windows 11 Kernel streaming service. Valentina also outlines her approach to bug hunting - "picking a target and sticking to it might be one of the most difficult steps of the research process."</li>
<li><a href="https://www.outflank.nl/blog/2024/08/13/will-the-real-grimresource-please-stand-up-abusing-the-msc-file-format" target="_blank">Will the real #GrimResource please stand up? - Abusing the MSC file format</a> - There was some chatter about MSC files for phishing not too long ago. Turns out elastic caught a sample from a red team that was an Outflank customer. A real <a href="https://en.wikipedia.org/wiki/Ouroboros" target="_blank">ouroboros</a> situation. Outflank just added cross-platform support to <a href="https://www.outflank.nl/blog/2024/08/07/introducing-outflank-c2-with-implant-support-for-windows-macos-and-linux/" target="_blank">Outflank C2</a> as well.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/badsectorlabs/sccm-http-looter" target="_blank">sccm-http-looter</a> - Find interesting files stored on (System Center) Configuration Manager (SCCM/CM) shares via HTTP(s).</li>
<li><a href="https://github.com/projectdiscovery/tldfinder" target="_blank">tldfinder</a> - A streamlined tool for discovering TLDs, associated domains, and related domain names.</li>
<li><a href="https://github.com/Teach2Breach/Tempest" target="_blank">Tempest</a> - A command and control framework written in rust.</li>
<li><a href="https://github.com/cado-security/cloudgrep" target="_blank">cloudgrep</a> - cloudgrep is grep for cloud storage.</li>
<li><a href="https://github.com/klezVirus/DriverJack" target="_blank">DriverJack</a> - Hijacking valid driver services to load arbitrary (signed) drivers abusing native symbolic links and NT paths.</li>
<li><a href="https://github.com/klezVirus/RpcProxyInvoke" target="_blank">RpcProxyInvoke</a> - Simple POC library to execute arbitrary calls proxying them via NdrServerCall2 or similar.</li>
<li><a href="https://github.com/hacksider/Deep-Live-Cam" target="_blank">Deep-Live-Cam</a> - real time face swap and one-click video deepfake with only a single image.</li>
<li><a href="https://github.com/tehstoni/tryharder" target="_blank">tryharder</a> - C++ Staged Shellcode Loader with Evasion capabilities.</li>
<li><a href="https://github.com/plonxyz/4n6pi" target="_blank">4n6pi</a> - 4n6pi is a forensic imager for disks, designed to run on a Raspberry Pi powered by libewf. It provides a simple and portable solution for creating disk images in forensic investigations.</li>
<li><a href="https://github.com/SafeBreach-Labs/QuickShell" target="_blank">QuickShell</a> - A library and a set of tools for exploiting and communicating with Google's Quick Share devices.</li>
<li><a href="https://github.com/happycakefriends/certainly" target="_blank">certainly</a> - Certainly is a offensive security toolkit to capture large amounts of traffic in various network protocols in bitflip and typosquat scenarios.</li>
<li><a href="https://github.com/Azure/PyRIT" target="_blank">PyRIT</a> - The Python Risk Identification Tool for generative AI (PyRIT) is an open access automation framework to empower security professionals and machine learning engineers to proactively find risks in their generative AI systems.</li>
<li><a href="https://github.com/CCob/Shwmae" target="_blank">Shwmae</a> - Shwmae (shuh-my) is a Windows Hello abuse tool that was released during DEF CON 32 as part of the Abusing Windows Hello Without a Severed Hand talk. The purpose of the tool is to abuse Windows Hello from a privileged user context.</li>
<li><a href="https://github.com/qi4L/CVE-2024-38077" target="_blank">CVE-2024-38077</a> - MadLicense Windows RCE CVE-2024-38077: A Simple Heap Overflow Vulnerability for the terminal licensing server. [As always verify the code before use.]</li>
<li><a href="https://github.com/deepinstinct/ShimMe" target="_blank">ShimMe</a> - Tools from the DEFCON 32 talk "SHIM me what you got - Manipulating Shim and Office for Code Injection". "Office Injector" and "Shim Injector"</li>
<li><a href="https://github.com/klezVirus/koppeling-p" target="_blank">koppeling-p</a> - Adaptive DLL hijacking / dynamic export forwarding - EAT preserve.</li>
<li><a href="https://github.com/mattzajork/httpxui" target="_blank">httpxui</a> - HTTP flyover tool based on the httpx library by ProjectDiscovery.</li>
<li><a href="https://github.com/Offensive-Panda/.NET_PROFILER_DLL_LOADING" target="_blank">.NET_PROFILER_DLL_LOADING</a> - .NET profiler DLL loading can be abused to make a legit .NET application load a malicious DLL using environment variables. This exploit is loading a malicious DLL using Task Scheduler (MMC) to bypass UAC and getting admin privileges.</li>
<li><a href="https://github.com/UndeadSec/DockerSpy" target="_blank">DockerSpy</a> - DockerSpy searches for images on Docker Hub and extracts sensitive information such as authentication secrets, private keys, and more.</li>
<li><a href="https://github.com/jborean93/LocalKdc" target="_blank">LocalKdc</a> - Info on how to use Kerberos KDC on a non-domain joined host.</li>
<li><a href="https://github.com/Chocapikk/CVE-2024-36401" target="_blank">CVE-2024-36401</a> - GeoServer Remote Code Execution.</li>
<li><a href="https://github.com/zyn3rgy/smbtakeover" target="_blank">smbtakeover</a> - BOF and Python3 implementation of technique to unbind 445/tcp on Windows via SCM interactions.</li>
<li><a href="https://github.com/MzHmO/LeakedWallpaper" target="_blank">LeakedWallpaper</a> - Leak of any user's NetNTLM hash. Fixed in KB5040434.</li>
<li><a href="https://github.com/lypd0/DeadPotato" target="_blank">DeadPotato</a> - DeadPotato is a windows privilege escalation utility from the Potato family of exploits, leveraging the SeImpersonate right to obtain SYSTEM privileges. This script has been customized from the original GodPotato source code by BeichenDream.</li>
<li><a href="https://github.com/synacktiv/SCCMSecrets" target="_blank">SCCMSecrets</a> - SCCMSecrets.py aims at exploiting SCCM policies distribution for credentials harvesting, initial access and lateral movement.</li>
<li><a href="https://github.com/EspressoCake/BOF_NativeAPI_Definitions-VSCode" target="_blank">BOF_NativeAPI_Definitions-VSCode</a> - A VSCode plugin to assist with BOF development.</li>
<li><a href="https://github.com/huntresslabs/rogueapps" target="_blank">rogueapps</a> - When good OAuth apps go rogue. Documents observed OAuth application tradecraft.</li>
<li><a href="https://github.com/runZeroInc/sshamble" target="_blank">sshamble</a> - SSHamble: Unexpected Exposures in SSH.</li>
<li><a href="https://github.com/Mayyhem/Maestro" target="_blank">Maestro</a> - Maestro is a post-exploitation tool designed to interact with Intune/EntraID from a C2 agent on a user's workstation without requiring knowledge of the user's password or Azure authentication flows, token manipulation, and web-based administration console.</li>
<li><a href="https://github.com/MaLDAPtive/Invoke-Maldaptive" target="_blank">Invoke-Maldaptive</a> - MaLDAPtive is a framework for LDAP SearchFilter parsing, obfuscation, deobfuscation and detection.</li>
<li><a href="https://github.com/helviojunior/hookchain" target="_blank">hookchain</a> - HookChain: A new perspective for Bypassing EDR Solutions.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/emiliensocchi/azure-tiering" target="_blank">azure-tiering</a> - Azure administrative tiering based on known attack paths.</li>
<li><a href="https://github.com/Yaxxine7/ASRepCatcher" target="_blank">ASRepCatcher</a> - Make everyone in your VLAN ASRep roastable.</li>
<li><a href="https://github.com/ricardojoserf/TrickDump" target="_blank">TrickDump</a> - Dump lsass using only NTAPIS running 3 programs to create 3 JSON and 1 ZIP file... and generate the Minidump later!.</li>
<li><a href="https://github.com/Neuvik/neuvik-terraform-workshop" target="_blank">neuvik-terraform-workshop</a> - Neuviks Terraform Red Team Workshop.</li>
<li><a href="https://github.com/chaitin/SafeLine/tree/main" target="_blank">SafeLine</a> - serve as a reverse proxy to protect your web services from attacks and exploits.</li>
<li><a href="https://github.com/0xv1n/RemoteSessionEnum" target="_blank">RemoteSessionEnum</a> - Remotely Enumerate sessions using undocumented Windows Station APIs.</li>
<li><a href="https://github.com/xvzc/SpoofDPI" target="_blank">SpoofDPI</a> - A simple and fast anti-censorship tool written in Go.</li>
<li><a href="https://github.com/yamadashy/repopack" target="_blank">repopack</a> - 📦 Repopack is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, and Gemini.</li>
<li><a href="https://github.com/AdnaneKhan/Gato-X" target="_blank">Gato-X</a> - GitHub Attack Toolkit - Extreme Edition.</li>
<li><a href="https://github.com/hotnops/apeman" target="_blank">apeman</a> - AWS Attack Path Management Tool - Walking on the Moon.</li>
<li><a href="https://screenshotone.com/blog/cloudflare-workers/" target="_blank">Cloudflare Workers as an API gateway</a> - From the sofware engineering community but infosec can learn from some of this 🙂.</li>
<li><a href="https://github.com/sevagas/Advanced_Initial_access_in_2024_OffensiveX" target="_blank">Advanced_Initial_access_in_2024_OffensiveX</a> - Resources linked to my presentation at OffensiveX in Athens in June 2024 on the topic "Breach the Gat, Advanced Initial Access in 2024".</li>
<li><a href="https://awssecuritydigest.com/articles/opinionated-ramp-up-guide-to-aws-pentesting" target="_blank">An Opinionated Ramp Up Guide to AWS Pentesting</a> - Hot takes on cloud pentesting. Does this resonate with anyone?</li>
<li><a href="https://github.com/Devolutions/MsRdpEx" target="_blank">MsRdpEx</a> - Microsoft RDP Client Extensions.</li>
<li><a href="https://github.com/jokob-sk/NetAlertX" target="_blank">NetAlertX</a> - 🔍 WIFI / LAN intruder detector. Scans for devices connected to your network and alerts you if new and unknown devices are found.</li>
<li><a href="https://github.com/timelinize/timelinize" target="_blank">timelinize</a> - Store your data from all your accounts and devices in a single cohesive timeline on your own computer.</li>
<li><a href="https://icode4.coffee/?p=954" target="_blank">TONY HAWK'S PRO STRCPY</a> - Exploit game consoles with a bad strcpy in the custom park load function of Tony Hawk's Pro Skater.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 431 (+0)</p>
<p>Blogs monitored: 386 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
