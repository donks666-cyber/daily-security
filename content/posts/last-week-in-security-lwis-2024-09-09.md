Title: Last Week in Security (LWiS) - 2024-09-09
Date: 2024-09-09 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-09-09
Author: Erik
Summary: Windows heap overflow (<a href="https://x.com/esj4y" target="_blank">@esj4y</a>), Linux TCP UAF (<a href="https://x.com/v4bel" target="_blank">@v4bel</a>), Goffloader (<a href="https://x.com/BouncyHat" target="_blank">@BouncyHat</a>), Intune lat-movement (<a href="https://x.com/h4wkst3r" target="_blank">@h4wkst3r</a>), browser attack detection (<a href="https://x.com/mega_spl0it" target="_blank">@mega_spl0it</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-09-03 to 2024-09-09.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://specterops.io/specter-bash/" style="color: #3bd267;" target="_blank">Specter Bash 2024</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p>Dare to join us for the ultimate SpecterOps experience! From October 7-10 in Denver, dive into spine-tingling offensive and defensive trainings like our renowned Red Team Operations course and the all-new Identity-driven Offensive Tradecraft course. When night falls, gear up for thrilling evening events with Specters and fellow training participants; it'll be scary-fun!</p>
<p><b>Save 25% on in-person tickets with code</b> <code>LWIS</code>. <a href="https://specterops.io/specter-bash/" style="color: #3bd267;" target="_blank">Secure your spot now!</a></p>
</aside><ul>
<li><a href="https://rewardsforjustice.net/rewards/gru-officers-unit-29155/" target="_blank">$10 million for information about malicious cyber activities against U.S. critical infrastructure</a> - Get $10 million for snitching on the GRU. What's the price of looking over your shoulder for the rest of your life?</li>
<li><a href="https://therecord.media/ransomware-hackers-threaten-planned-parenthood-montana" target="_blank">Ransomware hackers threaten Montana branch of Planned Parenthood</a> - It seems nothing is off limits anymore. 93 GB of data allegedly. They're looking to leak all of it if not paid.</li>
<li><a href="https://jfrog.com/blog/revival-hijack-pypi-hijack-technique-exploited-22k-packages-at-risk/" target="_blank">Revival Hijack - PyPI hijack technique exploited in the wild, puts 22K packages at risk</a> - Another week, another PyPI hijack. Are your developers protected from this threat?</li>
<li><a href="https://security.googleblog.com/2024/09/deploying-rust-in-existing-firmware.html" target="_blank">Deploying Rust in Existing Firmware Codebases</a> - Rust in firmware, Android, and Chrome. Memory unsafety vulnerabilities are going to be harder to find in the future.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.guidepointsecurity.com/blog/building-a-hardware-hacking-arsenal-the-right-bits-for-every-byte" target="_blank">Building a Hardware Hacking Arsenal: The Right Bits for Every Byte</a> - An overview of some tool recommendations if you're looking to get into IoT testing.</li>
<li><a href="https://gatari.dev/posts/the-art-of-exploiting-ad-from-linux/" target="_blank">The Art of Exploiting Active Directory from Linux</a> - A lot of impacket and proxychains. Worth noting some red teams are also moving away from dropping tooling on target and proxying everything over.</li>
<li><a href="https://labs.watchtowr.com/veeam-backup-response-rce-with-auth-but-mostly-without-auth-cve-2024-40711-2/" target="_blank">Veeam Backup &amp; Response - RCE With Auth, But Mostly Without Auth (CVE-2024-40711)</a> - Watchtowr shows restraint and breaks tradition by not releasing the full exploit code. This post is a good walkthrough of .NET patch diffing.</li>
<li><a href="https://blog.zsec.uk/homelab-clustering-pt1/" target="_blank">(Re)Building the Ultimate Homelab NUC Cluster - Part 1</a> - A few Intel NUCs make for a great homelab. Excited to read part two where <a href="https://ludus.cloud" target="_blank">Ludus</a> is set up!</li>
<li><a href="https://3sjay.github.io/2024/09/08/Windows-Kernel-Pool-Exploitation-CVE-2021-31956-Part1.html" target="_blank">Windows Kernel Pool Exploitation CVE-2021-31956 - Part 1</a> - The first in a series about exploiting a Windows kernel heap overflow from low integrity.</li>
<li><a href="https://www.darknavy.org/blog/cve_2024_5274_a_minor_flaw_in_v8_parser_leading_to_catastrophes/" target="_blank">CVE-2024-5274: A Minor Flaw in V8 Parser Leading to Catastrophes</a> - A Chrome V8 vulnerability in the javascript parser led to an out of bounds read/write. The interplay between javascript and C++ in browsers and the exploitation of the later from the former is always impressive to me.</li>
<li><a href="https://blog.theori.io/deep-dive-into-rcu-race-condition-analysis-of-tcp-ao-uaf-cve-2024-27394-f40508b84c42" target="_blank">Deep Dive into RCU Race Condition: Analysis of TCP-AO UAF (CVE-2024–27394)</a> - This Linux use-after-free (UAF) vulnerability was patched in April of 2024, but the detailed walk through and PoC are available in this post.</li>
<li><a href="https://trustedsec.com/blog/when-on-workstation-do-as-the-local-browsers-do" target="_blank">When on Workstation, Do as the Local Browsers Do!</a> - As host-based solutions get better, attackers move to the path of least resistance. Those browsers are looking good! Creds, cookies, access tokens, etc.</li>
<li><a href="https://securityintelligence.com/x-force/detecting-intune-lateral-movement/" target="_blank">Getting “in tune” with an enterprise: Detecting Intune lateral movement</a> - How Microsoft Intune, a cloud-based device management solution, can be abused for lateral movement in hybrid identity environments.</li>
<li><a href="https://www.cobaltstrike.com/blog/revisiting-the-udrl-part-3-beacon-user-data" target="_blank">Revisiting the UDRL Part 3: Beacon User Data</a> - The CobaltStrike team explains how Beacon User Data (BUD) can track memory allocations to improve masking of Beacon and additional components like External C2 DLLs. Their example demonstrates loading and masking both Beacon and an External C2 DLL simultaneously using these methods.</li>
<li><a href="https://blog.reveng.ai/physmem-e-when-kernel-drivers-peek-into-memory/" target="_blank">PhysMem(e): When Kernel Drivers Peek into Memory CVE-2024-41498</a> - A Windows vulnerability in the IOMap64.sys driver allows unauthorized read/write access to physical memory. Daniele explains the driver's structure, the vulnerable functions that use MmMapIoSpace to map physical addresses, and how these can be exploited. Proof of concept and yara rule in the post as well.</li>
<li><a href="https://malwaremaloney.blogspot.com/2024/09/cracking-onedrives-personal-vault.html" target="_blank">Cracking OneDrive's Personal Vault</a> - "Personal Vault" uses a BitLocker-encrypted VHDX file stored locally. By unlocking the vault through OneDrive and using administrative access, one can extract the BitLocker External Key (BEK) file. This BEK file can then unlock the VHDX, allowing access to the vault's contents even when locked. The process requires admin privileges and the vault to be unlocked once. <a href="https://github.com/Beercow/Personal-Vault-BEK" target="_blank">Personal-Vault-BEK</a> is the script to automate it all.</li>
<li><a href="https://edermi.github.io/post/2024/mfa_bypass_mtls/" target="_blank">When Certificates Fail: A Story of Bypassed MFA in Remote Access</a> - mTLS in a custom setup for Citrix would effectively disable MFA. Any valid mTLS certificate for the company would allow single factor authentication for any user.</li>
<li><a href="https://unit42.paloaltonetworks.com/stately-taurus-abuses-vscode-southeast-asian-espionage/" target="_blank">Chinese APT Abuses VSCode to Target Government in Asia</a> - Credit to <a href="https://x.com/PfiatDe" target="_blank">@pfiatde</a> for writing this up <a href="https://badoption.eu/blog/2023/01/31/code_c2.html" target="_blank">last year</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/deh00ni/NtDumpBOF" target="_blank">NtDumpBOF</a> - BOF port of the tool <a href="https://github.com/ricardojoserf/NativeDump" target="_blank">NativeDump</a>  by <a href="https://x.com/ricardojoserf" target="_blank">@RicardoJoseRF</a>.</li>
<li><a href="https://github.com/stivenhacker/GhostStrike" target="_blank">GhostStrike</a> - A basic XOR and process hollowing loader.</li>
<li><a href="https://github.com/CICADA8-Research/COMThanasia" target="_blank">COMThanasia</a> - A set of programs for analyzing common vulnerabilities in COM.</li>
<li><a href="https://github.com/praetorian-inc/goffloader" target="_blank">goffloader</a> - A Go implementation of Cobalt Strike style BOF/COFF loaders. Full blog post introduction <a href="https://www.praetorian.com/blog/introducing-goffloader-a-pure-go-implementation-of-an-in-memory-coffloader-and-pe-loader/" target="_blank">here</a>.</li>
<li><a href="https://frida.re/news/2024/09/06/frida-16-5-0-released/" target="_blank">Frida 16.5.0 Released</a> - New hardware breakpoint and watchpoint APIs, Windows ARM support, and other goodies.</li>
<li><a href="https://github.com/Flangvik/remote_wrapper" target="_blank">remote_wrapper</a> - Extensible Mythic Wrapper that allows payload wrapping to occur on a remote host.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/dadevel/impacket-zsh-integration" target="_blank">impacket-zsh-integration</a> - ZSH integration for Impacket.</li>
<li><a href="https://github.com/zeze-zeze/NamedPipeMaster" target="_blank">NamedPipeMaster</a> - a tool used to analyze and monitor in named pipes.</li>
<li><a href="https://github.com/Malcrove/SeamlessPass" target="_blank">SeamlessPass</a> - A tool leveraging Kerberos tickets to get Microsoft 365 access tokens using Seamless SSO.</li>
<li><a href="https://projectblack.io/blog/cve-hunting-at-scale/" target="_blank">CVE Hunting Made Easy</a> - How mass downloading of Wordpress Plugins + running a SAST on those led to 14 CVEs. Can along with <a href="https://github.com/prjblk/wordpress-audit-automation" target="_blank">wordpress-audit-automation</a> - which are the scripts to download every Wordpress plugin (updated in the last 2 years) and run Semgrep over the lot of it while storing output in a database.</li>
<li><a href="https://cicada-8.medium.com/evil-msi-a-long-story-about-vulnerabilities-in-msi-files-1a2a1acaf01c" target="_blank">Evil MSI. A story about vulnerabilities in MSI Files</a> - Detailed blog post on MSI abuse and the file format itself.</li>
<li><a href="https://socket.dev/blog/github-users-targeted-by-new-wave-of-spambots-promoting-malicious-downloads" target="_blank">GitHub Users Targeted by New Wave of Spambots Promoting Malicious Downloads</a> - Attackers are targetting your developers and your CICD pipelines!</li>
<li><a href="https://plowsec.github.io/angr-introspection-2024.html" target="_blank">angr for real-world use cases</a> - Angr is a binary analysis platform with features like symbolic execution. It's popular in the CTF and crackme scene, but this post focuses on how it can be used against real targets.</li>
<li><a href="https://github.com/cbecks2/edr-artifacts" target="_blank">edr-artifacts</a> - This repository is meant to catalog network and host artifacts associated with various EDR products "shell" and response functionalities.</li>
<li><a href="https://hackingthe.cloud/aws/exploitation/Misconfigured_Resource-Based_Policies/exploiting_misconfigured_gitlab_oidc_aws_iam_roles/" target="_blank">Exploiting Misconfigured GitLab OIDC AWS IAM Roles</a> - This would be sick to exploit on a red team.</li>
<li><a href="https://github.com/sz3/libcimbar" target="_blank">libcimbar</a> - Optimized implementation for color-icon-matrix barcodes.</li>
<li><a href="https://www.coresecurity.com/core-labs/articles/windows-dwm-core-library-elevation-privilege-vulnerability-cve-2024-30051" target="_blank">Windows DWM Core Library Elevation of Privilege Vulnerability (CVE-2024-30051)</a> - "In this blog post, I will explain a vulnerability in the Microsoft Windows DWM Core library that I analyzed when the exploit for Core Impact was being developed. Allows an unprivileged attacker to execute code as a DWM user with Integrity System privileges (CVE-2024-30051)."</li>
<li><a href="https://github.com/mrexodia/phnt-single-header" target="_blank">phnt-single-header</a> - Single header version of System Informer's phnt library.</li>
<li><a href="https://github.com/ii4gsp/CVE-2020-27786" target="_blank">CVE-2020-27786</a> - Exploit for a a use-after-free vulnerability due to a race condition in MIDI devices in Linux Kernel 5.6.13. Check out the full <a href="https://ii4gsp.github.io/cve-2020-27786/#full-exploit" target="_blank">blog post</a> as well.</li>
<li><a href="https://github.com/Wa1nut4/CVE-2024-26230" target="_blank">CVE-2024-26230</a> - Windows LPE in tapisrv.dll - CVE-2024-26230.</li>
<li><a href="https://minder-security.ghost.io/ludus-build-a-purple-teaming-test-environment/" target="_blank">Building a Purple Teaming Test Environment with Ludus</a> - Always cool to see folks blogging about <a href="https://ludus.cloud/" target="_blank">Ludus!</a></li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 436 (+3)</p>
<p>Blogs monitored: 389 (+3)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
