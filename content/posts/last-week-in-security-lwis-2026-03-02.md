Title: Last Week in Security (LWiS) - 2026-03-02
Date: 2026-03-02 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2026-03-02
Author: Erik
Summary: SolarWinds RCE (<a href="https://x.com/chudyPB" target="_blank">@chudyPB</a>), Windows 11 Recall-based LPE (<a href="https://x.com/filip_dragovic" target="_blank">@filip_dragovic</a>), Robot RCEs (<a href="https://x.com/olivier_boschko" target="_blank">@olivier_boschko</a> + <a href="https://x.com/ruikai" target="_blank">@ruikai</a>), EDR as a RAT (<a href="https://x.com/p0w1_" target="_blank">@p0w1_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2026-02-23 to 2026-03-02.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2026/02/cultivating-robust-and-efficient.html" target="_blank">Cultivating a robust and efficient quantum-safe HTTPS</a> - Google is pushing post-Quantum cryptography into Chrome. <a href="https://blog.cloudflare.com/bootstrap-mtc/" target="_blank">Cloudflare</a> is also on board.</li>
<li><a href="https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules" target="_blank">Google API Keys Weren't Secrets. But then Gemini Changed the Rules.</a> - Formally public API keys (used for things like Google Maps API) can now expose sensitive things like files uploaded to gemini if the Google Cloud project they came from has the Generative Language API enabled.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://github.com/wh1te4ever/super-tart-vphone-writeup" target="_blank">Building virtual iPhone using VPHONE600AP component of recently released PCC firmware</a> - It looks like it's possible to use the newly included "iPhone Research Environment Virtual Machine" of the <a href="https://security.apple.com/blog/private-cloud-compute/" target="_blank">Private Cloud Compute</a> to spin up a working iOS 26 virtual machine on an ARM based mac.</li>
<li><a href="https://labs.watchtowr.com/buy-a-help-desk-bundle-a-remote-access-solution-solarwinds-web-help-desk-pre-auth-rce-chain-s/" target="_blank">Buy A Help Desk, Bundle A Remote Access Solution? (SolarWinds Web Help Desk Pre-Auth RCE Chain(s))</a> - watchTowr researchers are scary. Piotr found a novel remote code execution vulnerability (bypassing prior patches), but it required authentication. So he found two authentication bypass 0days, but they were foiled by a "patch" that instructed admins to delete the jar file that contained the deserialization gadget used. Instead he found a different gadget that allows a connection to the local Postgres database and using that ran a malicious SQL to get SYSTEM level code execution. Code: <a href="https://github.com/watchtowrlabs/watchTowr-vs-SolarWinds-WebHelpDesk-CVE-2025-40552-CVE-2025-40553" target="_blank">watchTowr-vs-SolarWinds-WebHelpDesk-CVE-2025-40552-CVE-2025-40553</a>.</li>
<li><a href="https://www.mdsec.co.uk/2026/02/total-recall-retracing-your-steps-back-to-nt-authoritysystem/" target="_blank">Total Recall – Retracing Your Steps Back to NT AUTHORITYSYSTEM</a> - You know your red team is legit when your operators/devs are finding local privilege escalation vulnerabilities in Windows itself, and then bypassing the patches. The code at <a href="https://github.com/redpack-kr/CVE-2025-60710" target="_blank">CVE-2025-60710</a> (a copy of the accidentally released first PoC) looks legitimate but does include binaries (Msi_EoP.msi, 5eeabb3.rbs) that have not been vetted. Be careful.</li>
<li><a href="https://boschko.ca/unitree-go2-rce/" target="_blank">From DDS Packets to Robot Shells: Two RCEs in Unitree Robots (CVE-2026-27509 &amp; CVE-2026-27510)</a> - The journey from unboxing a robot to finding remote code execution vulnerabilities.</li>
<li><a href="https://itm4n.github.io/cve-2025-59201-ncsi-eop/" target="_blank">CVE-2025-59201 - Network Connection Status Indicator (NCSI) EoP</a> - Some neat tricks in the "Exploitation" section if you find yourself with a <cite>CreateSubKey</cite> right, although it ends without a full explanation of the code execution. I suspect that since WMI providers are loaded on-demand there is a missing step to explicitly invoke a WMI query against Win32_Tpm class once the registry key is overwritten.</li>
<li><a href="https://offsec.almond.consulting/bypassing-apache-fop-escaping-to-reach-ghostscript.html" target="_blank">Bypassing Apache FOP Postscript Escaping to reach GhostScript</a> - "According to Apache FOP, this bug will not be fixed. Instead, the documentation will be improved on what kind of security properties users can expect from Apache FOP." 🫠</li>
<li><a href="https://blog.amberwolf.com/blog/2026/february/delinea-protocol-handler---return-of-the-msi/" target="_blank">Delinea Protocol Handler - Return of the MSI: RCE via Custom Launcher</a> - More VPN client RCE this time via a protocol handler.</li>
<li><a href="https://decoder.cloud/2026/02/25/what-windows-server-2025-quietly-did-to-your-ntlm-relay/" target="_blank">What Windows Server 2025 Quietly Did to Your NTLM Relay</a> - Windows Server 2025 ignores the value of <cite>LmCompatibilityLevel</cite> and never generate NTLMv1 client traffic.</li>
<li><a href="https://labs.infoguard.ch/posts/abusing_cortex_xdr_live_response_as_c2/" target="_blank">Abusing Cortex XDR Live Terminal as a C2</a> - You know we love some <a href="https://www.youtube.com/watch?v=9qM2m1LZuVo" target="_blank">traitorware</a>!</li>
<li><a href="https://jakewnuk.com/posts/making-the-hashcracky-hashcat-rules/" target="_blank">Making the Hashcracky Hashcat Rules</a> - Some great tips and tools for password cracking rule generation in this post.</li>
<li><a href="https://ydinkin.substack.com/p/200-kernel-bugs-in-30-days" target="_blank">100+ Kernel Bugs in 30 Days</a> - What happens when you look at as many Windows drivers as you can get your hands on with AI assistance? Bugs. Lots of bugs.</li>
<li><a href="https://labs.reversec.com/posts/2026/02/building-an-ai-vishing-solution-in-7-days">Building an AI Vishing Solution in 7 Days</a> - I've warned about this <a href="https://blog.badsectorlabs.com/last-week-in-security-lwis-2021-06-21.html">many</a> <a href="https://blog.badsectorlabs.com/last-week-in-security-lwis-2023-02-13">times</a> <a href="https://blog.badsectorlabs.com/last-week-in-security-lwis-2024-03-25">before</a> . It's real now.</li>
<li><a href="https://openwall.com/lists/oss-security/2026/02/24/1" target="_blank">Telnetd Vulnerability Report</a> - After the CVE for passing a "-f root" value for the USER environment variable to telnetd, Justin Swartz took another look at telnetd and dug up another variant of a CVE from 1999 using environment variables to set the binary path telnetd uses to localize the prompt. This allows him to copy /bin/sh with the SUID bit set and gain root access to the local machine.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul><li><a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">PhantomSec | Advanced Offensive Capabilities Automated - EvadeX</a> <span class="m-label m-flat m-success">Sponsored</span> - EvadeX is an evasion-as-a-service platform for red teams and pentesters who want modern, continuously-updated evasive tradecraft without turning every engagement into an R&amp;D project. Generate highly customizable, low-signature payloads through a simple web workflow so you can tune to the target and stay focused on the engagement. Trusted by teams from small consultancies to the Fortune 10. <a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">Get callbacks past EDR today!</a></li></ul><ul>
<li><a href="https://github.com/vanhoefm/airsnitch" target="_blank">airsnitch</a> - A set of attacks that enable a guest user to bypass Wi-Fi client isolation. Or put differently, it allows an adversary who can connect to your network, either as a malicious insider or by connecting to a co-located open network, to 'bypass Wi-Fi encryption'. <a href="https://www.ndss-symposium.org/wp-content/uploads/2026-f1282-paper.pdf" target="_blank">[PDF] Paper</a>.</li>
<li><a href="https://0xv1n.github.io/posts/macnoise/" target="_blank">Introducing MacNoise!</a> - MacNoise is a modular macOS telemetry noise generator for EDR testing and security research. It generates real system events: network connections, file writes, process spawns, plist mutations, TCC permission probes, and more so security teams can validate that their EDR, SIEM, and firewall tooling detects what it is supposed to detect.</li>
<li><a href="https://github.com/BaddKharma/redStack" target="_blank">redStack</a> - Boot-to-Breach red team lab on AWS. Mythic, Sliver, and Havoc C2 behind a production-style Apache redirector. Deployed via Terraform.</li>
<li><a href="https://specterops.io/blog/2026/02/25/nemesis-2-2/" target="_blank">Nemesis 2.2</a> - "Nemesis 2.2 introduces a number of powerful new features focusing on large container processing, data processing agents, enhanced DPAPI support, and a host of performance improvements."</li>
<li><a href="https://github.com/m0x41nos/TimeAfterFree" target="_blank">TimeAfterFree</a> - PHP 8 sandbox escape PoC demonstrating a disable_functions bypass on Unix-like systems.</li>
<li><a href="https://github.com/knostic/OpenAnt/" target="_blank">OpenAnt</a> - An open source LLM-based vulnerability discovery product that helps defenders proactively find verified security flaws while minimizing both false positives and false negatives. Stage 1 detects. Stage 2 attacks. What survives is real.</li>
<li><a href="https://github.com/trailofbits/mquire" target="_blank">mquire</a> - <a href="https://blog.trailofbits.com/2026/02/25/mquire-linux-memory-forensics-without-external-dependencies/" target="_blank">Linux memory forensics without external dependencies</a></li>
<li><a href="https://github.com/0xbbuddha/notion" target="_blank">notion</a> - A Mythic C2 profile that uses Notion as a covert communication channel.</li>
<li><a href="https://github.com/praetorian-inc/nerva" target="_blank">nerva</a> - Fast service fingerprinting CLI for 120+ protocols (TCP/UDP/SCTP) - built by Praetorian</li>
<li><a href="https://github.com/HackingLZ/gibson" target="_blank">gibson</a> - Network monitoring tool that maps process-to-network connections, identifies cloud providers, and detects beaconing activity. Zero-flag agent binary for deployment, aggregation server, offline ASN lookup.</li>
<li><a href="https://github.com/dievus/ADPulse" target="_blank">ADPulse</a> is an open-source Active Directory security auditing tool that connects to a domain controller via LDAP(S), runs 35 automated security checks, and produces detailed reports in console, JSON, and HTML formats.</li>
<li><a href="https://github.com/Whispergate/Tyche" target="_blank">Tyche</a> is a Mythic HTTPX Profile Generator used to create Malleable C2 Profiles.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/senderend/azureBlob" target="_blank">azureBlob</a> - Azure Blob Storage C2 Profile for Mythic</li>
<li><a href="https://www.youtube.com/watch?v=YQEq5s4SRxY" target="_blank">The World's Hardest Hacking Competition - Pwn2Own Documentary</a> - A look into the Pwn2Own competitions and how Mozilla handles the 0day disclosures.</li>
<li><a href="https://www.youtube.com/watch?v=aoag03mSuXQ" target="_blank">The Internet Was Weeks Away From Disaster and No One Knew</a> - 8 millions views on a very popular YouTube channel goes over everything from Linux to the xz backdoor. If you want to play with xz you can with Ludus' <a href="https://docs.ludus.cloud/docs/environment-guides/malware-lab" target="_blank">Malware Lab</a> that includes the xz backdoor and an attacker machine.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 496 (+0)</p>
<p>Blogs monitored: 442 (+0)</p>
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
