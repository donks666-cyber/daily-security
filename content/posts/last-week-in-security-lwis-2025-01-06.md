Title: Last Week in Security (LWiS) - 2025-01-06
Date: 2025-01-06 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-01-06
Author: Erik
Summary: Kick off 2025 with, fresh news, new exploits, techniques, tools, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past few weeks. This post covers 2024-12-16 to 2025-01-06.</p>
<aside class="m-note m-success">
<h3>Happy New Year!</h3>
<p>This is a three week edition of Last Week in Security. A lot has been released, so let us know what we missed!</p>
<p>Sponsor slots for 2025 are filling up! Email blog (at) badsectorlabs.com for more information.</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://s3.documentcloud.org/documents/25472740/letter-to-chairman-brown-and-ranking-member-scott.pdf" target="_blank">[PDF] BeyondTrust RMM breach leads to US Treasury breach</a> - The best example of <a href="https://gitlab.com/badsectorlabs/iscariot-suite" target="_blank">traitorware</a>  yet? This is too recent to be related to the <a href="https://home.treasury.gov/news/press-releases/jy2769" target="_blank">sanctions</a> for Integrity Tech, a Beijing-based cybersecurity company.</li>
<li><a href="https://storage.courtlistener.com/recap/gov.uscourts.cand.350613/gov.uscourts.cand.350613.494.0_1.pdf" target="_blank">[PDF] Summary Judgment in WhatsApp vs NSO Group case</a> - The court held NSO Group liable for breaching WhatsApp’s terms of service, which prohibit malicious or illegal use, such as reverse engineering, decompiling software, or sending harmful code.</li>
<li><a href="https://letsencrypt.org/2024/12/05/ending-ocsp/?ref=scotthelme.co.uk" target="_blank">Ending OCSP Support in 2025</a> - Online Certificate Status Protocol has always been pretty broken (leaks your domain requests, soft-fails when unreachable anyway), so this is a step forward.</li>
<li><a href="https://apnews.com/article/united-states-china-hacking-espionage-c5351ef7c2207785b76c8c62cde6c513" target="_blank">A 9th telecoms firm has been hit by a massive Chinese espionage campaign, the White House says</a> - Phone and SMS should be considered fully compromised at this point. Use <a href="https://signal.org/" target="_blank">Signal</a> or <a href="https://simplex.chat/" target="_blank">SimpleX</a>.</li>
</ul>
<ul><li><a href="https://app.presspool.ai/engage/9" style="color: #3bd267;" target="_blank">Fortified’s Central Command Platform Named "Healthcare Cybersecurity Solution of the Year"</a> <span class="m-label m-flat m-success">Sponsored</span> - The MSSP platform integrates Advisory Services and Threat Defense (SOC) Managed Services into a single, cohesive application, offering a comprehensive suite of tools that enable healthcare providers, payors, and other healthcare clients to monitor threats, manage risk registers, gain insights from analytics, and react to real-time alerts through desktop and mobile applications. <a href="https://app.presspool.ai/engage/9/" style="color: #3bd267;" target="_blank">Learn more and see it in action today!</a></li></ul></section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.jumpsec.com/tokensmith-bypassing-intune-compliant-device-conditional-access/" target="_blank">TokenSmith – Bypassing Intune Compliant Device Conditional Access</a> - Entra ID conditional access is a complex system, and the need to allow devices to go from non-compliant to compliant allows for attackers to get full MSGraph tokens even on non-intune compliant devices. Note that cookies and the user's password/MFA are still required.</li>
<li><a href="https://github.blog/security/vulnerability-research/uncovering-gstreamer-secrets/" target="_blank">Uncovering GStreamer secrets</a> - 29 vulnerabilities discovered thanks to a custom input corpus generator for the MP4 format.</li>
<li><a href="https://starlabs.sg/blog/2024/all-i-want-for-christmas-is-a-cve-2024-30085-exploit/" target="_blank">All I Want for Christmas is a CVE-2024-30085 Exploit</a> - A really great breakdown of a heap-based buffer overflow vulnerability affecting the Windows Cloud Files Mini Filter Driver. There are actually two separate overflows and some head-fu to pull this exploit off. Code here: <a href="https://github.com/star-sg/CVE/tree/master/CVE-2024-30085" target="_blank">CVE-2024-30085</a>.</li>
<li><a href="https://www.wiz.io/blog/the-many-ways-to-obtain-credentials-in-aws" target="_blank">The many ways to obtain credentials in AWS</a> - A summary of the various ways computer services on AWS obtain their credentials. This is knowledge that btoh attackers and defenders can gain to get an upper hand on the side that doesn't have this knowledge.</li>
<li><a href="https://benkofman.com/2024/12/23/pwspraying.html" target="_blank">Password Spraying with Selenium and Fireprox</a> - A little manual unlike tools like  <a href="https://github.com/knavesec/CredMaster" target="_blank">CredMaster</a> but this seems like a good exercise for those looking to understand modern password spraying tradecraft. TLDR - You almost always have to cycle your IP address and worry about those source IP addresses. Many identify API GW in their audit logs. AWS API GW alternatives are pretty hot right now.</li>
<li><a href="https://www.hvs-consulting.de/en/nfs-security-identifying-and-exploiting-misconfigurations/" target="_blank">NFS Security: Identifying and Exploiting Misconfigurations</a> - There aren't many blog posts around abusing NFS. This is a great introduction to those interested. NFS is still a popular protocol to come across on internal pentests. ALso came with a tool drop:<a href="https://github.com/hvs-consulting/nfs-security-tooling" target="_blank">nfs-security-tooling</a>.</li>
<li><a href="https://www.safebreach.com/blog/ldapnightmare-safebreach-labs-publishes-first-proof-of-concept-exploit-for-cve-2024-49113/" target="_blank">LDAPNightmare: SafeBreach Labs Publishes First Proof-of-Concept Exploit for CVE-2024-49113</a> - The LDAP vulnerability patched last month has a crash proof of concept available. The race to remote code execution is on! PoC: <a href="https://github.com/SafeBreach-Labs/CVE-2024-49113" target="_blank">CVE-2024-49113</a>.</li>
<li><a href="https://www.x86matthew.com/view_post?id=ntsockets" target="_blank">NTSockets - Downloading a file via HTTP using the NtCreateFile and NtDeviceIoControlFile syscalls</a> - This post demonstrates how to create TCP sockets and transmit/receive data using only ntdll exports.</li>
<li><a href="https://www.wiz.io/blog/nuclei-signature-verification-bypass" target="_blank">Breaking the Chain: Wiz Uncovers a Signature Verification Bypass in Nuclei, the Popular Vulnerability Scanner (CVE-2024-43405)</a> - Ooof. This one hits the impact box hard. Imagine distributing a malicious template and getting RCE on many hackers assessment devices. Great find!</li>
<li><a href="https://cicada-8.medium.com/im-watching-you-how-to-spy-windows-users-via-ms-uia-c9acd30f94c4" target="_blank">I’m watching you! How to spy Windows users via MS UIA</a> - Exploiting Windows accessibility framework to stealthily monitor user activity, including password managers and messaging apps.</li>
<li><a href="https://medium.com/@frsfaisall/mastering-modern-red-teaming-infrastructure-part-2-building-stealthy-c2-infrastructure-with-312aec7e1e48" target="_blank">Mastering Modern Red Teaming Infrastructure — Part 2: Building Stealthy C2 Infrastructure with Sliver and Re-director</a> - Surprise: Using Cloudflare to proxy your traffic. Cloudflare is cracking down on abuse so I'm curious how long this will last. Good walkthrough to anyone looking for a step-by-step guide.</li>
<li><a href="https://adnanthekhan.com/2024/12/21/cacheract-the-monster-in-your-build-cache/" target="_blank">Cacheract: The Monster in your Build Cache</a> - A GitHub actions post-exploitation technique that abuses the cache. The scary part is once it has permissions, it adds itself to the cache, and as long as the action runs once every 7 days, it could persist forever. Code: <a href="https://github.com/adnaneKhan/cacheract" target="_blank">Cacheract</a>.</li>
<li><a href="https://ssd-disclosure.com/ssd-advisory-cldflt-heap-based-overflow-pe/" target="_blank">SSD Advisory – cldflt Heap-Based Overflow (PE)</a> - A nice Windows local privilege escalation that took third place in TyphoonPWN 2024.</li>
<li><a href="https://fin3ss3g0d.net/index.php/2024/12/27/static-keys-shattered-security-dreams-a-cve-2024-5764-story/" target="_blank">Static Keys, Shattered Security Dreams: A CVE-2024–5764 Story</a> - A writeup of multiple issues in the Sonotype Nexus Cache including path traversal and issues with the older OrientDB system.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/kozmer/aad-bofs" target="_blank">aad-bofs</a> - AzureAD beacon object files.</li>
<li><a href="https://github.com/Fitretech-Security/dylight" target="_blank">dylight</a> is a project that loads macOS dynamic libraries (dylibs) from the internet over HTTP and injects within the local process.</li>
<li><a href="https://github.com/kapellos/VladimiRED/" target="_blank">VladimiRED</a> - is a C# port of <a href="https://github.com/caueb/Mockingjay" target="_blank">Mockingjay injection technique</a> to be used with AppDomainManager Injection Method.</li>
<li><a href="https://github.com/CrowdStrike/sccmhound" target="_blank">sccmhound</a> - A BloodHound collector for Microsoft Configuration Manager.</li>
<li><a href="https://github.com/kozmer/aad-bofs" target="_blank">aad-bofs</a> - This repository contains a collection of BOFs for various Azure AD attacks.</li>
<li><a href="https://github.com/JumpsecLabs/TokenSmith" target="_blank">TokenSmith</a> generates Entra ID access &amp; refresh tokens on offensive engagements. It is suitable for both covert adversary simulations and penetration tests with the tokens generated working out of the box with many popular Azure post exploitation tools.</li>
<li><a href="https://github.com/BlackSnufkin/LitterBox" target="_blank">LitterBox</a> - A sandbox environment designed specifically for malware development and payload testing.</li>
<li><a href="https://github.com/NtDallas/sharp-execute" target="_blank">sharp-execute</a> - Executing .NET Files from an Unmanaged Process with Manual CLR Loading.</li>
<li><a href="https://github.com/hardenedlinux/userland-exec" target="_blank">userland-exec</a> - Userland exec replaces the existing process image within the current address space with a new one. It mimics the behavior of the system call execve, but the process structures describing the process image remain unchanged. In other words, the process name reported by system utilities will retain the old process name.</li>
<li><a href="https://github.com/t3hbb/PanGP_Extractor/tree/PanGPA-v6.2.6-838" target="_blank">PanGP_Extractor</a> - Tool to extract username and password of current user from PanGPA in plaintext.</li>
<li><a href="https://github.com/jonescyber-ai/Blackfyre" target="_blank">Blackfyre</a> - Blackfyre is an open-source platform designed to standardize and streamline binary analysis. It provides tools and APIs for extracting, analyzing, and storing binary data in a disassembler-agnostic and architecture-agnostic format. This enables consistent workflows for advanced reverse engineering tasks powered by AI/ML, NLP, and LLMs.</li>
<li><a href="https://github.com/logangoins/Krueger" target="_blank">Krueger</a> - Proof of Concept (PoC) .NET tool for remotely killing EDR with WDAC.</li>
<li><a href="https://github.com/BlackSnufkin/LitterBox" target="_blank">LitterBox</a> - Sandbox approach for malware developers and red teamers to test payloads against detection mechanisms before deployment.</li>
<li><a href="https://github.com/k3nundrum/hashcrack-ai" target="_blank">hashcrack-ai</a> - Hashcrack-AI is an automated python script that is designed to use GPU instances provided by <a class="m-link-wrap" href="https://vast.ai" target="_blank">https://vast.ai</a>, to deploy a Dockerized Hashcat CUDA instance <a class="m-link-wrap" href="https://github.com/dizcza/docker-hashcat" target="_blank">https://github.com/dizcza/docker-hashcat</a>.</li>
<li><a href="https://github.com/nullenc0de/trust-validator" target="_blank">trust-validator</a> - Validates priv escalation of AD trusts.</li>
<li><a href="https://github.com/ajm4n/DLLHound" target="_blank">DLLHound</a> - Find potential DLL Sideloads on your windows computer.</li>
<li><a href="https://github.com/lasersharkkiller/Know-Normal-S1" target="_blank">Know-Normal-S1</a> - Helps to "Know Normal" by comparing artifacts from an alert against the enterprise. Based on SANS 508 concept.</li>
<li><a href="https://github.com/zh54321/PoCEntraDeviceComplianceBypass" target="_blank">PoCEntraDeviceComplianceBypass</a> - Simple pure PowerShell POC to bypass Entra / Intune Compliance Conditional Access Policy.</li>
<li><a href="https://github.com/CCob/DRSAT" target="_blank">DRSAT</a> - Disconnected RSAT - A method of running Group Policy Manager, Certificate Authority and Certificate Templates MMC snap-ins from non-domain joined machines.</li>
<li><a href="https://github.com/AdnaneKhan/Cacheract" target="_blank">Cacheract</a> - GitHub Actions Cache Native Malware - for Educational and Research Purposes only.</li>
<li><a href="https://github.com/GitHubSecurityLab/CodeQL-Community-Packs/" target="_blank">CodeQL-Community-Packs</a> - Collection of community-driven CodeQL query, library and extension packs. More info: <a href="https://github.blog/security/vulnerability-research/announcing-codeql-community-packs/" target="_blank">Announcing CodeQL Community Packs</a>.</li>
<li><a href="https://github.com/ZephrFish/SCCMSiteCodeHunter?ref=blog.zsec.uk" target="_blank">SCCMSiteCodeHunter</a> - A utility for querying SCCM (System Center Configuration Manager) management points and site servers using LDAP.</li>
<li><a href="https://github.com/SafeBreach-Labs/CVE-2024-49112" target="_blank">CVE-2024-49112</a> - LdapNightmare is a PoC tool that tests a vulnerable Windows Server against CVE-2024-49112.</li>
<li><a href="https://github.com/djackreuter/btexec" target="_blank">btexec</a> - Execute shellcode via Bluetooth device authentication.</li>
<li><a href="https://github.com/CICADA8-Research/Spyndicapped" target="_blank">Spyndicapped</a> - COM ViewLogger — new malware keylogging technique.</li>
<li><a href="https://github.com/GangGreenTemperTatum/DOMspy" target="_blank">DOMspy</a> - A web security research tool for DOM testing. A chrome extension now.</li>
<li><a href="https://github.com/xforcered/MLOKit" target="_blank">MLOKit</a> is a toolkit that can be used to attack MLOps platforms by taking advantage of the available REST API. This tool allows the user to specify an attack module, along with specifying valid credentials (API key or stolen access token) for the respective MLOps platform. Read the full report here: <a href="https://www.ibm.com/downloads/documents/us-en/11630e2cbc302316" target="_blank">[PDF] Disrupting the Model: Abusing MLOps Platforms to Compromise ML Models and Enterprise Data Lakes</a>.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/grayhatkiller/SharpExShell" target="_blank">SharpExShell</a> automates the DCOM lateral movement technique which abuses ActivateMicrosoftApp method of Excel application.</li>
<li><a href="https://github.com/NocteDefensor/InstaTools" target="_blank">InstaTools</a> - Ansible Script to install my favorite Tools.</li>
<li><a href="https://github.com/AmberWolfCyber/NachoVPN" target="_blank">NachoVPN</a> - A delicious, but malicious SSL-VPN server 🌮.</li>
<li><a href="https://github.com/SpiralBL0CK/CVE-2024-35176" target="_blank">CVE-2024-35176</a> - CVE-2024-35176 poc full.</li>
<li><a href="https://github.com/justinmeiners/lc3-vm" target="_blank">lc3-vm</a> - Write your own virtual machine for the LC-3 computer!.</li>
<li><a href="https://github.com/grayhatkiller/SharpExShell" target="_blank">SharpExShell</a> - SharpExShell automates the DCOM lateral movement technique which abuses ActivateMicrosoftApp method of Excel application.</li>
<li><a href="https://github.com/aniqfakhrul/powerview.py" target="_blank">powerview.py</a> - Just another Powerview alternative.</li>
<li><a href="https://github.com/OWASP/OFFAT" target="_blank">OFFAT</a> - The OWASP OFFAT tool autonomously assesses your API for prevalent vulnerabilities, though full compatibility with OAS v3 is pending. The project remains a work in progress, continuously evolving towards completion.</li>
<li><a href="https://github.com/bohops/SharpRDPHijack" target="_blank">SharpRDPHijack</a> - A proof-of-concept Remote Desktop (RDP) session hijack utility.</li>
<li><a class="m-text m-dim" href="https://attackrulemap.netlify.app/" target="_blank">AttackRuleMap</a> - Mapping of open-source detection rules and atomic tests.</li>
<li><a href="https://github.com/NHAS/egressinator" target="_blank">egressinator</a> - Find what egress ports are allowed.</li>
<li><a href="https://github.com/LuemmelSec/Pentest-Tools-Collection/blob/main/tools/Azure/AzurePwn.ps1" target="_blank">Azurepwn.ps1</a> - Azure post-exploitation work</li>
</ul>
<p>Resources</p>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 442 (+0)</p>
<p>Blogs monitored: 401 (+0)</p>
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
