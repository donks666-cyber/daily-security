Title: Last Week in Security (LWiS) - 2024-04-16
Date: 2024-04-16 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-04-16
Author: Erik
Summary: Dev tunnels for C2 (<a href="https://twitter.com/RedSiege" target="_blank">@RedSiege</a>), UAF Windows LPE (<a href="https://twitter.com/KeyZ3r0" target="_blank">@KeyZ3r0</a>), SCCM enum script (<a href="https://twitter.com/_Mayyhem" target="_blank">@_Mayyhem</a>), ETW patching (<a href="https://twitter.com/jsecurity101" target="_blank">@jsecurity101</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-04-08 to 2024-04-16.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://cloud.google.com/blog/topics/public-sector/google-public-sector-achieves-top-secret-and-secret-cloud-authorization" target="_blank">Google Public Sector achieves Top Secret and Secret cloud authorization</a> - Google has entered the chat. With Microsoft's recent APT issues, I wonder if any any orgs will consider Google.</li>
<li><a href="https://unit42.paloaltonetworks.com/muddled-libra-evolution-to-cloud/" target="_blank">Muddled Libra's Evolution to the Cloud</a> - Unit 42 researchers discovered that the Muddled Libra group now actively targets software-as-a-service (SaaS) applications and cloud service provider (CSP) environments.</li>
<li><a href="https://msrc.microsoft.com/blog/2024/04/toward-greater-transparency-adopting-the-cwe-standard-for-microsoft-cves/" target="_blank">Toward greater transparency: Adopting the CWE standard for Microsoft CVEs</a> - "...we will now publish root cause data for Microsoft CVEs using the Common Weakness Enumeration (CWE™) industry standard."</li>
<li><a href="https://opentofu.org/blog/our-response-to-hashicorps-cease-and-desist/" target="_blank">Our Response to Hashicorp's Cease and Desist Letter</a> - Some turmoil in the IaC world. "The OpenTofu team vehemently disagrees with any suggestion that it misappropriated, mis-sourced, or otherwise misused HashiCorp's BSL code. All such statements have zero basis in facts."</li>
<li><a href="https://aws.amazon.com/about-aws/whats-new/2024/04/amazon-cloudfront-oac-lambda-function-url-origins/" target="_blank">Amazon CloudFront now supports Origin Access Control (OAC) for Lambda function URL origins</a> - Let your cloud teams know!</li>
<li><a href="https://www.aaro.mil/Portals/136/PDFs/UAP_RECORDS_RESEARCH/AARO_DHS_Kona_Blue.pdf" target="_blank">[PDF] KONA BLU</a> - Declassified DHS project - KONA BLUE - A special access program for recovering materials user for inter dimensional, time, and space travel. While the project only was a SAP for 6 months and seems like it <a href="https://www.aaro.mil/Portals/136/PDFs/UAP_RECORDS_RESEARCH/History_and_Origin_of_KONA_BLUE_FINAL_508.pdf?ver=VWt5t7KtzTZzZ3bZoEAGqA%3d%3d" target="_blank">[PDF] never really did anything</a> a look into what goes into a SAP is interesting and the first example being declassified we are aware of.</li>
<li><a href="https://www.neowin.net/news/microsoft-will-add-external-recipient-rate-email-limits-to-exchange-online-in-january-2025/" target="_blank">Microsoft will add External Recipient Rate email limits to Exchange Online in January 2025</a> - The paywalls continue, this is a push for more revenue from the Azure email service. This could impact your bulk phishing engagements if you're using exchange as your mail sender and send to more than 2,000 recipients a day.</li>
<li><a href="https://krebsonsecurity.com/2024/04/twitters-clumsy-pivot-to-x-com-is-a-gift-to-phishers/" target="_blank">Twitter's Clumsy Pivot to X.com Is a Gift to Phishers</a> - Rewriting URLs is a dangerous game.</li>
<li><a href="https://labs.watchtowr.com/palo-alto-putting-the-protecc-in-globalprotect-cve-2024-3400/" target="_blank">Palo Alto - Putting The Protecc In GlobalProtect (CVE-2024-3400)</a> - This is being actively exploited in the wild, and is this month's SSLVPN RCE...</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://redsiege.com/blog/2024/04/using-microsoft-dev-tunnels-for-c2-redirection/" target="_blank">Using Microsoft Dev Tunnels for C2 Redirection</a> - Using <a href="https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/overview" target="_blank">dev tunnels</a> as your C2. Careful with burning your Microsoft account.</li>
<li><a href="https://medium.com/heck-the-packet/cs-technologies-evolution-vulnerabilities-e3e8c8bd4a4c" target="_blank">CS Technologies — Evolution Vulnerabilities</a> - A set of vulnerabilities within software used to administer the EVO2 and EVO4 door access controllers. Chained together, this leads to unauthenticated access to add a user with access to every door in the building, control doors, etc.</li>
<li><a href="https://whereisk0shl.top/post/a-trick-the-story-of-cve-2024-26230" target="_blank">A trick, the story of CVE-2024-26230</a> - A step-by-step walkthrough of CVE-2024-26230 (use-after-free vulnerability in the telephony service)</li>
<li><a href="https://www.stedi.com/blog/stedi-discovered-an-aws-access-vulnerability" target="_blank">We discovered an AWS access vulnerability</a> - A vulnerability in AWS STS allowed users to gain unauthorized account access due to incorrect role trust policy evaluations. It's been patched! Cool to read that this SaaS has a different AWS account per customer as a security boundary.</li>
<li><a href="https://www.0ffset.net/reverse-engineering/capstone-resolving-stack-strings/" target="_blank">Resolving Stack Strings with Capstone Disassembler &amp; Unicorn in Python</a> - Walkthrough on how to resolve stack strings in malware using Capstone Disassembler and Unicorn Emulator in Python. They used Conti Ransomware to showcase it.</li>
<li><a href="https://blog.theori.io/chaining-n-days-to-compromise-all-part-3-windows-driver-lpe-medium-to-system-12f7821d97bb" target="_blank">Chaining N-days to Compromise All: Part 3 — Windows Driver LPE: Medium to System</a> - This post discusses the exploitation of a logic bug in the Windows kernel driver mskssrv.sys (CVE-2023-29360), which was demonstrated in Pwn2Own 2023. The exploit allows priv-esc from user to SYSTEM by manipulating the Memory Descriptor List (MDL) to map physical memory addresses incorrectly, effectively bypassing security checks. It was part of <a href="https://twitter.com/theori_io/status/1764544922005430576" target="_blank">this crazy VM escape chain</a>.</li>
<li><a href="https://posts.specterops.io/rooting-out-risky-sccm-configs-with-misconfiguration-manager-0beecaab1af3" target="_blank">Rooting out Risky SCCM Configs with Misconfiguration Manager</a> - The SpecterOps team has published a <a href="https://github.com/subat0mik/Misconfiguration-Manager/blob/main/MisconfigurationManager.ps1" target="_blank">script</a> for sysadmins and infosec practitioners to identify every TAKEOVER and ELEVATE attack in <a href="https://github.com/subat0mik/Misconfiguration-Manager" target="_blank">Misconfiguration-Manager</a>. SCCM is an overlooked attack surface that usually holds a privileged position in the AD network.</li>
<li><a href="https://jsecurity101.medium.com/understanding-etw-patching-9f5af87f9d7b" target="_blank">Understanding ETW Patching</a> - A quick summary from <a href="https://twitter.com/jsecurity101" target="_blank">@jsecurity101</a> on how function patching can be applied to ETW providers to alter or inhibit their standard behavior, potentially evading detection by modifying or bypassing function execution in both user-mode and kernel-mode operations.</li>
<li><a href="https://www.akamai.com/blog/security-research/critical-vulnerability-create-uri-remote-code-execution" target="_blank">CreateRCE — Yet Another Vulnerability in CreateUri</a> In another episode of Akamai vs Outlook clients... "An attacker on the internet can trigger the vulnerability against Outlook clients without any user interaction (zero-click)". The technical write-up of <a href="https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2023-35628" target="_blank">CVE-2023-35628</a> which was patched December 2023.</li>
<li><a href="https://dfir.ch/posts/sysrv/" target="_blank">Sysrv Infection (Linux Edition)</a> - Write up of the Sysrv botnet, which deployed a crypto miner on a Linux system using a payload pulled down from a specified URL. Sometimes detecting these can be as easy as checking those DNS logs for known mining pools.</li>
<li><a href="https://github.com/MythicAgents/sliver/blob/main/blog/blog.md" target="_blank">My Journey on Integrating Sliver into Mythic</a> - Mythic agents that use Mythic's API and Sliver's API to remotely control Sliver agents from within Mythic!</li>
<li><a href="https://0xsp.com/uncategorized/how-i-leveraged-wmi-to-enumerate-a-process-modules-and-their-base-addresses/" target="_blank">How I Leveraged WMI to Enumerate a Process Modules and Their Base Addresses</a> - "Leverage Windows Management Instrumentation (WMI) to extract the loaded modules of a specific process and understand how to get each module base address, show the advantages and the ability to perform ShellCode injection in .text section directly."</li>
<li><a href="https://gergelykalman.com/why-you-shouldnt-use-a-commercial-vpn-amateur-hour-with-windscribe.html" target="_blank">Why you shouldn't use a commercial VPN: Amateur hour with Windscribe</a> - If you are going to use a commercial VPN, at least generate standard WireGuard or OpenVPN configs and use the industry standard apps. This is why.</li>
<li><a href="https://labs.nettitude.com/blog/flaw-in-putty-p-521-ecdsa-signature-generation-leaks-ssh-private-keys/" target="_blank">Flaw in PuTTY P-521 ECDSA signature generation leaks SSH private keys</a> - "An attacker who compromises an SSH server may be able to leverage this vulnerability to compromise the user's private key. Attackers may also be able to compromise the SSH private keys of anyone who used git+ssh with commit signing and a P-521 SSH key, simply by collecting public commit signatures." Cryptography is hard!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Wh04m1001/UserManagerEoP" target="_blank">UserManagerEoP</a> - PoC for CVE-2023-36047. Patched last week. Should still be viable if you're on an engagement right now!</li>
<li><a href="https://github.com/klarna-incubator/gram" target="_blank">Gram</a> - Klarna's own threat model diagramming tool</li>
<li><a href="https://github.com/frkngksl/Shoggoth" target="_blank">Shoggoth</a> - Shoggoth is an open-source project based on C++ and asmjit library used to encrypt given shellcode, PE, and COFF files polymorphically.</li>
<li><a href="https://github.com/YuriiCrimson/ExploitGSM" target="_blank">ExploitGSM</a> - Exploit for 6.4 - 6.5 Linux kernels and another exploit for 5.15 - 6.5. Zero days when published.</li>
<li><a href="https://github.com/Azure/Copilot-For-Security" target="_blank">Copilot-For-Security</a> - Microsoft Copilot for Security is a generative AI-powered security solution that helps increase the efficiency and capabilities of defenders to improve security outcomes at machine speed and scale, while remaining compliant to responsible AI principles</li>
<li><a href="https://gist.github.com/Homer28/7f3559ff993e2598d0ceefbaece1f97f" target="_blank">CVE-2024-21378</a> -  DLL code for testing CVE-2024-21378 in MS Outlook. Using this with <a href="https://github.com/NetSPI/ruler/tree/com-forms" target="_blank">Ruler</a>.</li>
<li><a href="https://github.com/AdnaneKhan/ActionsTOCTOU" target="_blank">ActionsTOCTOU</a> - Example repository for GitHub Actions Time of Check to Time of Use (TOCTOU vulnerabilities).</li>
<li><a href="https://github.com/DosX-dev/obfus.h" target="_blank">obfus.h</a> - obfus.h is a macro-only library for compile-time obfuscating C applications, designed specifically for the Tiny C (tcc). It is tailored for Windows x86 and x64 platforms and supports almost all versions of the compiler.</li>
<li><a href="https://github.com/Faisal-P27/WAREED-DNS-C2" target="_blank">Wareed DNS C2</a> is a Command and Control (C2) that utilizes the DNS protocol for secure communications between the server and the target. Designed to minimize communication and limit data exchange, it is intended to be a first-stage C2 to persist in machines that don't have access to the internet via HTTP/HTTPS, but where DNS is allowed.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/cablej/hack-your-government" target="_blank">Can you hack your government?</a> -  A list of governments with Vulnerability Disclosure Policies.</li>
<li><a href="https://github.com/target/goalert" target="_blank">GoAlert</a> - Open source on-call scheduling, automated escalations, and notifications so you never miss a critical alert</li>
<li><a href="https://github.com/mrrootsec/AssetViz" target="_blank">AssetViz</a> -  AssetViz simplifies the visualization of subdomains from input files, presenting them as a coherent mind map. Ideal for penetration testers and bug bounty hunters conducting reconnaissance, AssetViz provides intuitive insights into domain structures for informed decision-making.</li>
<li><a href="https://artemonsecurity.blogspot.com/2024/04/gmer-art-of-exposing-windows-rootkits.html" target="_blank">GMER - the art of exposing Windows rootkits in kernel mode</a> - GMER is an anti-rootkit tool used to detect and combat rootkits, specifically focusing on the prevalent kernel mode rootkits, and remains effective despite many anti-rootkits losing relevance with advancements in Windows security.</li>
<li><a href="https://nicolasuter.medium.com/aitm-phishing-with-azure-functions-a1530b52df05" target="_blank">AiTM Phishing with Azure Functions</a> - The deployment of a serverless AiTM phishing toolkit using Azure Functions to phish Entra ID credentials and cookies</li>
<li><a href="https://github.com/cloudflare/orange" target="_blank">orange</a> - Orange Meets is a demo application built using Cloudflare Calls. To build your own WebRTC application using Cloudflare Calls. Combine this with some <a href="https://github.com/myshell-ai/OpenVoice" target="_blank">OpenVoice</a> or <a href="https://github.com/CorentinJ/Real-Time-Voice-Cloning" target="_blank">Real-Time-Voice-Cloning</a>. Scary.</li>
<li><a href="https://github.com/tldrsec/awesome-secure-defaults" target="_blank">awesome-secure-defaults</a> - Share this with your development teams and friends or use it in your own tools. "Awesome secure by default libraries to help you eliminate bug classes!"</li>
<li><a href="https://gist.github.com/mistymntncop/f6853ffe9492a049e03f2ee3c53d1d26" target="_blank">NtWaitForDebugEvent + WaitForMultipleObjects</a> - Using these two together to wait for debug events from multiple debugees at once.</li>
<li><a href="https://github.com/taranis-ai/taranis-ai" target="_blank">taranis-ai</a> - Taranis AI is an advanced Open-Source Intelligence (OSINT) tool, leveraging Artificial Intelligence to revolutionize information gathering and situational analysis.</li>
<li><a href="https://github.com/jsecurity101/MSFT_DriverBlockList" target="_blank">MSFT_DriverBlockList</a> - Repository of Microsoft Driver Block Lists based off of OS-builds.</li>
<li><a href="https://github.com/dazzyddos/HSC24RedTeamInfra" target="_blank">HSC24RedTeamInfra</a> - Slides and Codes used for the workshop Red Team Infrastructure Automation at HackSpanCon2024.</li>
<li><a href="https://github.com/Dhravya/supermemory" target="_blank">SuperMemory</a> - Build your own second brain with supermemory. It's a ChatGPT for your bookmarks. Import tweets or save websites and content using the chrome extension.</li>
<li><a href="https://kubenomicon.com/" target="_blank">Kubenomicon</a> - An open source offensive security focused threat matrix for kubernetes with an emphasis on walking through how to exploit each attack.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 376 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
