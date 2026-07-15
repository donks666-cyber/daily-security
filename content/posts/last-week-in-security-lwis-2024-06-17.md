Title: Last Week in Security (LWiS) - 2024-06-17
Date: 2024-06-17 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-06-17
Author: Erik
Summary: Nighthawk 0.3 (<a href="https://x.com/MDSecLabs" target="_blank">@MDSecLabs</a>), Musl heap exploit (<a href="https://x.com/NCCsecurityUS" target="_blank">@NCCsecurityUS</a>), Copilot chat 💉 (<a href="https://x.com/wunderwuzzi23" target="_blank">@wunderwuzzi23</a>), allowPrivilegeEscalation in K8s (<a href="https://x.com/christophetd" target="_blank">@christophetd</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-06-10 to 2024-06-17.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.apple.com/blog/private-cloud-compute" target="_blank">Private Cloud Compute: A new frontier for AI privacy in the cloud</a> - Apple has entered the AI arena, but unlike others is focused on user privacy. While "private cloud compute" isn't perfect (they are open sourcing "a subset of the security-critical PCC source code," not everything), it's clear they spent a lot of time considering how to do cloud compute in the most private way possible.</li>
<li><a href="https://techcommunity.microsoft.com/t5/sysinternals-blog/process-monitor-v4-0-and-sysmon-1-3-3-for-linux/ba-p/4169957" target="_blank">Process Monitor v4.0 and Sysmon 1.3.3 for Linux</a> - ProcMon 4.0 is here and has dark mode!</li>
<li><a href="https://services.google.com/fh/files/misc/snowflake-threat-hunting-guide.pdf" target="_blank">[PDF] Mandiant Threat Hunting Guide: Snowflake</a> - 64 pages. Threat hunting guidance and queries for detecting abnormal and malicious activity across Snowflake customer database instances.</li>
<li><a href="https://security.googleblog.com/2024/06/time-to-challenge-yourself-in-2024.html" target="_blank">Time to challenge yourself in the 2024 Google CTF</a> - Google's annual CTF runs this weekend.</li>
<li><a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-30078" target="_blank">Windows Wi-Fi Driver Remote Code Execution Vulnerability: CVE-2024-30078</a> - "An unauthenticated attacker could send a malicious networking packet to an adjacent system that is employing a Wi-Fi networking adapter, which could enable remote code execution." We have yet to see any legitimate PoCs.</li>
<li><a href="https://www.propublica.org/article/microsoft-solarwinds-golden-saml-data-breach-russian-hackers" target="_blank">Microsoft Chose Profit Over Security and Left U.S. Government Vulnerable to Russian Hack, Whistleblower Says</a> - An account of a SAML flaw in Active Directory Federation Services that was used by the SolarWinds hackers, and the response (or lack there of) from Microsoft. Interesting insider perspective in light of the US government moving nearly everything into Microsoft's cloud.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.mdsec.co.uk/2024/06/nighthawk-0-3-automate-all-the-things/" target="_blank">Nighthawk 0.3 - Automate All the Things</a> - The MDSec team has basically rewritten the Nighthawk C2 framework with a focus on automation and interoperability. We haven't gotten our hands on Nighthawk yet, but it looks like a serious C2 for high level red teams without the development resources to create and maintain their own C2.</li>
<li><a href="https://research.nccgroup.com/2024/06/11/pumping-iron-on-the-musl-heap-real-world-cve-2022-24834-exploitation-on-an-alpine-mallocng-heap/" target="_blank">Pumping Iron on the Musl Heap - Real World CVE-2022-24834 Exploitation on an Alpine mallocng Heap</a> - You may not need to exploit Redis with an integer overflow with 350MiB of data, but this write up goes in depth about the exploitation of the musl heap, which is used in Apline Linux - the basis of many Docker containers.</li>
<li><a href="https://embracethered.com/blog/posts/2024/github-copilot-chat-prompt-injection-data-exfiltration/" target="_blank">GitHub Copilot Chat: From Prompt Injection to Data Exfiltration</a> - Careful what code you are running your AI assistants on, and what capabilities (i.e. web browsing) the assistants have.</li>
<li><a href="https://blog.christophetd.fr/stop-worrying-about-allowprivilegeescalation/" target="_blank">Stop worrying about 'allowPrivilegeEscalation'</a> - This Kubernetes option is unfortunately named, but this post explains what it actually does.</li>
<li><a href="https://mrd0x.com/progressive-web-apps-pwa-phishing/" target="_blank">Progressive Web Apps (PWAs) Phishing</a> - The usual social engineering wizardry from <a href="https://x.com/mrd0x" target="_blank">@mrd0x</a>. This time phishing with Progressive Web Apps and UI manipulation.</li>
<li><a href="https://rootsecdev.medium.com/introduction-to-azure-cloud-token-theft-mindmap-v1-22d015cb5ee8" target="_blank">Introduction to Azure Cloud Token Theft MindMap V1</a> - Who doesn't love a good mindmap?</li>
<li><a href="https://anvbis.au/posts/code-execution-in-chromiums-v8-heap-sandbox/" target="_blank">Code Execution in Chromium's V8 Heap Sandbox</a> - A JSArray builtin allows you to change the length of an array to any arbitrary value which provides you with out-of-bounds access to that array.</li>
<li><a href="https://0reg.dev/blog/tenda-ac8-rop" target="_blank">ROPing Routers from scratch: Step-by-step Tenda Ac8v4 Mips 0day Flow-control ROP -&gt; RCE</a> - Even if this Tenda router is not a current target, the MIPS emulation/exploitation is well done.</li>
<li><a href="https://bc-security.org/scriptblock-smuggling/" target="_blank">ScriptBlock Smuggling: Spoofing PowerShell Security Logs and Bypassing AMSI Without Reflection or Patching</a> - Still using PowerShell in your ops? "...This issue was disclosed to Microsoft but was closed with no further action."</li>
<li><a href="https://frereit.de/aes_gcm/" target="_blank">AES-GCM and breaking it on nonce reuse</a> - This is an extremely technical cryptography blog post. The interactive components are really neat - you can change the examples live on the site!</li>
<li><a href="https://posts.specterops.io/lateral-movement-with-the-net-profiler-8772c86f9523" target="_blank">Lateral Movement with the .NET Profiler</a> - The common language runtime is full of neat tricks that can be abused. Example code is in the tools and exploits section.</li>
<li><a href="https://sector7.computest.nl/post/2024-06-cve-2024-20693-windows-cached-code-signature-manipulation/" target="_blank">CVE-2024-20693: Windows cached code signature manipulation</a> - Manipulating the cached signature signing level of an executable or DLL could lead to a local privilege escalation. In this case they created a PoC that elevates from a low privilege user to SYSTEM.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/vxCrypt0r/Voidgate" target="_blank">Voidgate</a> - A technique that can be used to bypass AV/EDR memory scanners. This can be used to hide well-known and detected shellcodes (such as msfvenom) by performing on-the-fly decryption of individual encrypted assembly instructions, thus rendering memory scanners useless for that specific memory page.</li>
<li><a href="https://github.com/thefLink/Hunt-Sleeping-Beacons" target="_blank">Hunt-Sleeping-Beacons</a> - Aims to identify sleeping beacons.</li>
<li><a href="https://github.com/Leo4j/Invoke-ADEnum" target="_blank">Invoke-ADEnum</a> - Automate Active Directory Enumeration.</li>
<li><a href="https://github.com/Flangvik/QRucible" target="_blank">QRucible</a> - Python utility that generates "imageless" QR codes in various formats.</li>
<li><a href="https://github.com/0xEr3bus/RdpStrike" target="_blank">RdpStrike</a> - Positional Independent Code to extract clear text password from mstsc.exe using API Hooking via HWBP.</li>
<li><a href="https://github.com/cod3nym/Deobfuscar" target="_blank">Deobfuscar</a> - A simple commandline application to automatically decrypt strings from Obfuscator protected binaries.</li>
<li><a href="https://github.com/NetSPI/gcpwn" target="_blank">gcpwn</a> - Enumeration/exploit/analysis/download/etc pentesting framework for GCP; modeled like Pacu for AWS; a product of numerous hours via @WebbinRoot.</li>
<li><a href="https://github.com/BreakingMhet/honeyzure" target="_blank">honeyzure</a> - HoneyZure is a honeypot tool specifically designed for Azure environments, fully provisioned through Terraform. It leverages a Log Analytics Workspace to ingest logs from various Azure resources, generating alerts whenever the deceptive Azure resources are accessed.</li>
<li><a href="https://github.com/nccgroup/SteppingStones" target="_blank">SteppingStones</a> - A Red Team Activity Hub.</li>
<li><a href="https://github.com/varwara/CVE-2024-26229" target="_blank">CVE-2024-26229</a> - CWE-781: Improper Address Validation in IOCTL with METHOD_NEITHER I/O Control Code.</li>
<li><a href="https://github.com/NVISOsecurity/CVE-2024-26229-BOF" target="_blank">CVE-2024-26229-BOF</a> - BOF implementations of CVE-2024-26229 for Cobalt Strike and BruteRatel.</li>
<li><a href="https://github.com/MayerDaniel/profiler-lateral-movement" target="_blank">profiler-lateral-movement</a> - Lateral Movement via the .NET Profiler.</li>
<li><a href="https://github.com/Wh1t3Rh1n0/SlackEnum" target="_blank">SlackEnum</a> - A user enumeration tool for Slack.</li>
<li><a href="https://github.com/BC-SECURITY/ScriptBlock-Smuggling" target="_blank">ScriptBlock-Smuggling</a> - Example code samples from our ScriptBlock Smuggling Blog post.</li>
<li><a href="https://github.com/ricardojoserf/NativeDump" target="_blank">NativeDump</a> - Dump lsass using only Native APIs by hand-crafting Minidump files (without MinidumpWriteDump!).</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/assetnote/nowafpls" target="_blank">nowafpls</a> - Burp Plugin to Bypass WAFs through the insertion of Junk Data.</li>
<li><a href="https://github.com/schooldropout1337/lazyegg" target="_blank">lazyegg</a> - LazyEgg is a powerful tool for extracting various types of data from a target URL. It can extract links, images, cookies, forms, JavaScript URLs, localStorage, Host, IP, and leaked credentials.</li>
<li><a href="https://github.com/Anze/KeyCluCask" target="_blank">KeyCluCask</a> - Simple and handy overview of applications shortcuts.</li>
<li><a href="https://github.com/awslabs/security-hub-compliance-analyzer" target="_blank">security-hub-compliance-analyzer</a> - A compliance analysis tool which enables organizations to more quickly articulate their compliance posture and also generate supporting evidence artifacts.</li>
<li><a href="https://github.com/YiikerGiiker/Nemesis-Ansible" target="_blank">Nemesis-Ansible</a> - Automatically deploy Nemesis.</li>
<li><a href="https://github.com/rtecCyberSec/Packer_Development" target="_blank">Packer_Development</a> - Slides &amp; Code snippets for a workshop held @ x33fcon 2024.</li>
<li><a href="https://github.com/DebugPrivilege/InsightEngineering" target="_blank">InsightEngineering</a> - Hardcore Debugging.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 427 (+0)</p>
<p>Blogs monitored: 382 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
