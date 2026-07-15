Title: Last Week in Security (LWiS) - 2024-06-10
Date: 2024-06-10 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-06-10
Author: Erik
Summary: SCCM ansible role (<a href="https://x.com/synzack21" target="_blank">@synzack21</a>), Hacking millions of modems (<a href="https://x.com/samwcyo" target="_blank">@samwcyo</a>), F5 Secure Vault (<a href="https://x.com/myst404_" target="_blank">@myst404_</a>), Secure Kerrnel (<a href="https://x.com/33y0re" target="_blank">@33y0re</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-06-03 to 2024-06-10.</p>
<aside class="m-note m-success">
<h3>SCCM Ludus Role</h3>
<p>Get hands on with SCCM using the new <a href="https://github.com/badsectorlabs/ludus_xz_backdoor" target="_blank">SCCM role</a> for <a href="https://ludus.cloud/" target="_blank">Ludus</a>.</p>
<p>Read the blog post <a href="https://posts.specterops.io/automating-sccm-with-ludus-a-configuration-manager-for-your-configuration-manager-c8f4d8e40473" target="_blank">Automating SCCM with Ludus: A Configuration Manager for Your Configuration Manager</a>.</p>
<p>This is the most complex role yet for Ludus, and it was great working with Zach.</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><p><a href="https://x.com/vxunderground/status/1799254734018134195" target="_blank">[X/Twitter] CSS injection in GitHub profiles</a> - Not a lot of detail on this but apparently using LaTeX you can include external CSS in your GitHub profile.</p>
</li>
<li><p><a href="https://learn.microsoft.com/en-us/windows-server/get-started/removed-deprecated-features-windows-server-2025" target="_blank">Features removed or no longer developed starting with Windows Server 2025 (preview)</a> - "All versions of NTLM, including LANMAN, NTLMv1, and NTLMv2, are no longer under active feature development and are deprecated." Backwards compatibility will keep NTLM relaying alive for at least another decade.</p>
</li>
<li><p>Microsoft Recall</p>
<blockquote>
<ul>
<li><a href="https://blogs.windows.com/windowsexperience/2024/06/07/update-on-the-recall-preview-feature-for-copilot-pcs/" target="_blank">Update on the Recall preview feature for Copilot+ PCs</a> - Microsoft says Recall will now be opt-in. For how long one wonders, until they flip it back to opt-out.</li>
<li><a href="https://github.com/Pennyw0rth/NetExec/pull/335" target="_blank">Add Recall module for dumping all users Microsoft Recall DBs &amp; screenshots #335</a> - Recall extraction feature added to netexec.</li>
<li><a href="https://github.com/xaitax/TotalRecall" target="_blank">TotalRecall</a> - This tool extracts and displays data from the Recall feature in Windows 11, providing an easy way to access information about your PC's activity snapshots.</li>
</ul>
</blockquote>
</li>
<li><p><a href="https://www.bleepingcomputer.com/news/security/fbi-recovers-7-000-lockbit-keys-urges-ransomware-victims-to-reach-out/" target="_blank">FBI recovers 7,000 LockBit keys, urges ransomware victims to reach out</a> - A lot of keys! Pretty cool!</p>
</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.watchtowr.com/no-way-php-strikes-again-cve-2024-4577/" target="_blank">No Way, PHP Strikes Again! (CVE-2024-4577)</a> - On Windows (specifically the Chinese and Japanese locales), a '<cite>%AD</cite>' in a URL gets interpreted as '<cite>-</cite>' which can lead to remote code execution depending on how PHP is configured. By default, the XAMPP project is vulnerable.</li>
<li><a href="https://www.atredis.com/blog/2024/6/3/how-to-train-your-large-language-model" target="_blank">How to Train Your Large Language Model</a> - Ever wondered how people 'fine tune' large language models for specific tasks? This post walks through training a local model and GPT-4 to assist with making sense of the pseudo-code output in the IDA Pro disassembler. The model and plugin code can be found at <a href="https://github.com/atredispartners/aidapal" target="_blank">aidapal</a>.</li>
<li><a href="https://www.synacktiv.com/en/publications/whfb-and-entra-id-say-hello-to-your-new-cache-flow" target="_blank">WHFB and Entra ID: Say Hello to Your New Cache Flow</a> - With Windows Hello for Business and Entra ID, there still needs to be a way to authenticate the user on the device if the device is offline. This cache can be used by attackers to bruteforce passwords. The use of a trusted platform module (TPM), or better yet a TPM v2, will slow down this bruteforce considerably.</li>
<li><a href="https://www.matteomalvica.com/blog/2024/06/05/intro-v8-exploitation-maglev/" target="_blank">An Introduction to Chrome Exploitation - Maglev Edition</a> - Besides mobile devices, Chrome is probably the next hardest target. This post covers Chromium Security Architecture and the V8 Pipeline, with a focus on the Maglev Compiler. It also covers the root cause analysis of CVE-2023-4069 and how to exploit it with JIT-spraying shellcode.</li>
<li><a href="https://research.checkpoint.com/2024/inside-the-box-malwares-new-playground/" target="_blank">Inside the Box: Malware's New Playground</a> - Malware groups are using the <a href="https://www.boxedapp.com/" target="_blank">BoxedApp</a> product to evade detection. This mirrors earlier efforts that used VMprotect. If you can pay a modest price for a commercial packer that will help you evade EDR, many financially motivated actors will do so. Are you using commercial packers in your adversary simulations?</li>
<li><a href="https://samcurry.net/hacking-millions-of-modems" target="_blank">Hacking Millions of Modems (and Investigating Who Hacked My Modem)</a> - A hacker discovers his modem is compromised, and through the course of investigating finds a way to hack any Cox customer's modem.</li>
<li><a href="https://rtx.meta.security/exploitation/2024/06/03/Android-Zygote-injection.html" target="_blank">Becoming any Android app via Zygote command injection</a> - Meta's red team discovered a vulnerability in Android (now patched) that allows an attacker with the WRITE_SECURE_SETTINGS permission, which is held by the ADB shell and certain privileged apps, to execute arbitrary code as any app on a device. By doing so, they could read and write any app's data, make use of per-app secrets and login tokens, change most system configuration, unenroll or bypass Mobile Device Management, and more. The exploit involves no memory corruption, meaning it worked unmodified on virtually any device running Android 9 or later, and persists across reboots. This feels like a vulnerability that will make some advanced actors very upset to see patched.</li>
<li><a href="https://offsec.almond.consulting/deep-diving-f5-secure-vault.html" target="_blank">Deep diving into F5 Secure Vault</a> - After <a href="https://offsec.almond.consulting/post-exploiting-f5-BIG-IP.html" target="_blank">Exploiting an F5 Big-IP</a>, <a href="https://x.com/myst404_" target="_blank">@myst404_</a> set their sights on the "Secure Vault." Spoiler: it isn't all that secure.</li>
<li><a href="https://connormcgarr.github.io/secure-images/" target="_blank">Windows Internals: Dissecting Secure Image Objects - Part 1</a> - The king of technical deep dives is back! Funny that this is actually a third order blog post spawned from research originally into the Kernel Control Flow Guard (Kernel CFG) feature. As always, Connor delivers a great, highly technical post.</li>
<li><a href="https://summoning.team/blog/veeam-enterprise-manager-cve-2024-29849-auth-bypass/" target="_blank">Bypassing Veeam Authentication CVE-2024-29849</a> - "This vulnerability in Veeam Backup Enterprise Manager allows an unauthenticated attacker to log in to the Veeam Backup Enterprise Manager web interface as any user. - Critical"</li>
<li><a href="https://pagedout.institute/download/PagedOut_004_beta1.pdf" target="_blank">[PDF] Paged Out! #4 (14MB, beta1 build)</a> - A great modern <a href="https://en.wikipedia.org/wiki/Zine" target="_blank">zine</a>.</li>
<li><a href="https://en.hackndo.com/password-spraying-lockout/" target="_blank">Spray passwords, avoid lockouts</a> - A very compreshensive look at Windows password policy. <a href="https://github.com/login-securite/conpass" target="_blank">conpass</a> is the new tool dropped to implement the ideas presented in the post.</li>
<li><a href="https://www.ribbiting-sec.info/posts/2024-06-05_csharp_obfuscator/" target="_blank">Develop your own C# Obfuscator</a> - Sure, you've used ConfuserEx, but what if you wrote your own C# obfuscator?</li>
<li><a href="https://medium.com/@0xcc00/bypassing-edr-ntds-dit-protection-using-blueteam-tools-1d161a554f9f" target="_blank">Bypassing EDR NTDS.dit protection using BlueTeam tools.</a> - Love to see <a href="https://gitlab.com/badsectorlabs/iscariot-suite" target="_blank">traitorware</a> in the wild.</li>
<li><a href="https://posts.specterops.io/one-phish-two-phish-red-teams-spew-phish-1a2f02010ed7" target="_blank">One Phish Two Phish, Red Teams Spew Phish</a> - How to give your phishing domains a reputation boost.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/SySS-Research/MAT" target="_blank">MAT</a> - This tool, programmed in C#, allows for the fast discovery and exploitation of vulnerabilities in MSSQL servers.</li>
<li><a href="https://github.com/thebookisclosed/AmperageKit" target="_blank">AmperageKit</a> - One stop shop for enabling Recall in Windows 11 version 24H2 on unsupported devices.</li>
<li><a href="https://github.com/basecamp/omakub" target="_blank">omakub</a> - Opinionated Ubuntu Setup.</li>
<li><a href="https://github.com/noperator/chromedb" target="_blank">chromedb</a> - Read Chromium data (namely, cookies and local storage) straight from disk, without spinning up the browser.</li>
<li><a href="https://github.com/trustedsec/The_Shelf" target="_blank">The_Shelf</a> - Retired TrustedSec Capabilities. See <a href="https://trustedsec.com/blog/introducing-the-shelf" target="_blank">Introducing The Shelf</a>  for more.</li>
<li><a href="https://github.com/oldboy21/RflDllOb" target="_blank">RflDllOb</a> - Reflective DLL Injection Made Bella.</li>
<li><a href="https://github.com/sinsinology/CVE-2024-29849" target="_blank">CVE-2024-29849</a> - Veeam Backup Enterprise Manager Authentication Bypass (CVE-2024-29849).</li>
<li><a href="https://github.com/shdwpwn/rsescan" target="_blank">rsescan</a> - RSEScan is a command-line utility for interacting with the RSECloud. It allows you to fetch subdomains and IPs from certificates for a given domain or organization.</li>
<li><a href="https://github.com/0xsp-SRD/MDE_Enum" target="_blank">MDE_Enum</a> - comprehensive .NET tool designed to extract and display detailed information about Windows Defender exclusions and Attack Surface Reduction (ASR) rules without Admin privileges.</li>
<li><a href="https://github.com/AlteredSecurity/Disable-TamperProtection" target="_blank">Disable-TamperProtection</a> - A POC to disable TamperProtection and other Defender / MDE components.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://blog.kandji.io/malware-bypass-tcc" target="_blank">How Malware Can Bypass Transparency Consent and Control (CVE-2023-40424)</a> - CVE-2023-40424 is a vulnerability that allows a root-level user to create a new user with a custom Transparency Consent and Control (TCC) database in macOS, which can then be used to access other users' private data. It was fixed in 2023 in macOs Sonoma (but not backported to older versions!).</li>
<li><a href="https://github.com/The-Viper-One/PsMapExec" target="_blank">PsMapExec</a> - A PowerShell tool that takes strong inspiration from CrackMapExec / NetExec.</li>
<li><a href="https://github.com/An0nUD4Y/Evilginx-Phishing-Infra-Setup" target="_blank">Evilginx-Phishing-Infra-Setup</a> - Evilginx Phishing Engagement Infrastructure Setup Guide.</li>
<li><a href="https://github.com/fiddyschmitt/File-Tunnel?ref=selfh.st" target="_blank">File-Tunnel</a> - Tunnel TCP connections through a file.</li>
<li><a href="https://github.com/TupleType/awesome-cicd-attacks" target="_blank">awesome-cicd-attacks</a> - Practical resources for offensive CI/CD security research. Curated the best resources I've seen since 2021.</li>
<li><a href="https://ja4db.com/" target="_blank">JA4+ Database</a> -  Download, read, learn about, and contribute to augment your organization's JA4+ network security efforts</li>
<li><a href="https://github.com/elastic/detection-rules" target="_blank">detection-rules</a> is the home for rules used by Elastic Security. This repository is used for the development, maintenance, testing, validation, and release of rules for Elastic Security's Detection Engine.</li>
<li><a href="https://github.com/openrecall/openrecall" target="_blank">openrecall</a> - OpenRecall is a fully open-source, privacy-first alternative to proprietary solutions like Microsoft's Windows Recall. With OpenRecall, you can easily access your digital history, enhancing your memory and productivity without compromising your privacy.</li>
<li><a href="https://github.com/guelfoweb/knock" target="_blank">knock</a> - Knock Subdomain Scan.</li>
<li><a href="https://github.com/soxrok2212/ubiquity-toolkit" target="_blank">ubiquity-toolkit</a> - A collection of statically-linked tools targeted to run on almost any linux system.</li>
<li><a href="https://github.com/whokilleddb/SOAPHound" target="_blank">SOAPHound</a> - A fork of SOAPHound that uses an external server to exfiltrate the results vs dropping them on disk for improved OPSEC.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 427 (+0)</p>
<p>Blogs monitored: 381 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
