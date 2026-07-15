Title: Last Week in Security (LWiS) - 2025-05-27
Date: 2025-05-27 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-05-27
Author: Erik
Summary: BadSuccessor (<a href="https://x.com/YuG0rd" target="_blank">@YuG0rd</a>), o3 finds SMB 0day (<a href="https://x.com/seanhn" target="_blank">@seanhn</a>), crashing defender (<a href="https://x.com/InfoGuard_Labs" target="_blank">@InfoGuard_Labs</a>), MDT looting (<a href="https://x.com/oddvarmoe" target="_blank">@Oddvarmoe</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-05-19 to 2025-05-27.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2025/05/tracking-cost-of-quantum-factori.html" target="_blank">Tracking the Cost of Quantum Factoring</a> - It could take 20x less qubits (1 million running for 1 week) than previously thought to factor Rivest–Shamir–Adleman (RSA) keys. The largest public functioning general-purpose quantum computer (IBM <a href="https://www.spinquanta.com/news-detail/discover-the-worlds-largest-quantum-computer-in20250106092507" target="_blank">Condor</a>) has 1,121 qubits. The national institute of standards says systems without post-quantum cryptography should be deprecated in 2030 and disallowed after 2035.</li>
<li><a href="https://arstechnica.com/security/2025/05/signal-resorts-to-weird-trick-to-block-windows-recall-in-desktop-app/" target="_blank">“Microsoft has simply given us no other option,” Signal says as it blocks Windows Recall</a> - Windows Recall will screenshot nearly anything, including payment details, health records, and until this update, Signal desktop messages. Users who want to take legitimate screenshots or use a screen-reader have to toggle a setting in Signal which is off by default.</li>
<li><a href="https://arstechnica.com/gadgets/2025/05/self-hosting-is-having-a-moment-ethan-sholly-knows-why/?ref=selfh.st" target="_blank">Self-hosting is having a moment. Ethan Sholly knows why.</a> - We couldn't agree more. The price-per-dollar of "compute" (CPU+RAM+Disk) is so good right now you can self host <a href="https://ludus.cloud" target="_blank">entire networks easily</a>.</li>
<li><a href="https://old.reddit.com/r/Tailscale/comments/1ksy3xy/someone_just_randomly_joined_my_tailnet/mtphcm9/?context=3" target="_blank">[reddit] Someone just randomly joined my Tailnet</a> - Tailscale has to manually input a list of shared email providers, otherwise the first person to sign up is the tailnet admin. Sounds like there is a change coming to make this a non-issue, and tailnet approvals is now on by default, but it's tech-debt coming back to bite Tailscale.</li>
<li><a href="https://www.zetter-zeroday.com/uae-recruiting-us-personnel-displaced-by-doge-to-work-on-ai-for-its-military/?ref=zero-day-newsletter" target="_blank">UAE Recruiting US Personnel Displaced by DOGE to Work on AI for its Military</a> - "A UAE brigadier general received permission from the Pentagon to recruit former members of the Defense Digital Service to work on artificial intelligence for the UAE military — despite past warnings from US spy agencies and federal lawmakers that UAE could share AI technologies with China."</li>
<li><a href="https://blogs.windows.com/windowsdeveloper/2025/05/19/the-windows-subsystem-for-linux-is-now-open-source/" target="_blank">The Windows Subsystem for Linux is now open source</a> - WSL2 is open source, WSL1 (Lxcore.sys) is not yet open source.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.akamai.com/blog/security-research/abusing-dmsa-for-privilege-escalation-in-active-directory" target="_blank">BadSuccessor: Abusing dMSA to Escalate Privileges in Active Directory</a> - If there is a Windows Server 2025 domain controller, and you have any low-priv user in the network with the ability to create a delegated Managed Service Account (dMSA), or control an OU where it can be created, congrats! You've got Domain Admin! With all the press this has gotten, I wonder if it will be elevated from "won't fix" by the Microsoft Security Response Center. <a href="https://pastebin.com/raw/wrn4vqce" target="_blank">[Pastebin] This cypher query</a> may be your best bet for detection right now (credit to <a href="https://x.com/sekurlsa_pw" target="_blank">@sekurlsa_pw</a>).</li>
<li><a href="https://sean.heelan.io/2025/05/22/how-i-used-o3-to-find-cve-2025-37899-a-remote-zeroday-vulnerability-in-the-linux-kernels-smb-implementation/" target="_blank">How I used o3 to find CVE-2025-37899, a remote zeroday vulnerability in the Linux kernel’s SMB implementation</a> - "No scaffolding, no agentic frameworks, no tool use... With o3 LLMs have made a leap forward in their ability to reason about code, and if you work in vulnerability research you should start paying close attention."</li>
<li><a href="https://www.darknavy.org/blog/argusee_a_multi_agent_collaborative_architecture_for_automated_vulnerability_discovery/" target="_blank">Argusee: A Multi-Agent Collaborative Architecture for Automated Vulnerability Discovery</a> - The framework managed to find a vulnerability in the Linux USB protocol stack (CVE-2025-37891), and scored 100% on buffer overflow test cases from META CyberSecEval.</li>
<li><a href="https://labs.infoguard.ch/posts/attacking_edr_part4_fuzzing_defender_scanning_and_emulation_engine/" target="_blank">Attacking EDRs Part 4: Fuzzing Defender's Scanning and Emulation Engine (mpengine.dll)</a> - The ability to crash Windows Defender is powerful, as a file that causes a crash can be packaged with an initial access or lateral movement payload to prevent scanning and detection.</li>
<li><a href="https://jellevergeer.com/red-team-revelations-exposing-and-addressing-vulnerabilities-in-ivanti-workspace-control/" target="_blank">Red Team Revelations: Exposing and Addressing Vulnerabilities in Ivanti Workspace Control</a> - C# programs and static keys are a timeless classic. <a href="https://github.com/jellever/InvatiWorkspaceControlDecrypter" target="_blank">InvatiWorkspaceControlDecrypter</a> is the tool.</li>
<li><a href="https://neodyme.io/en/blog/pwn2own-2024_canon_rce/" target="_blank">Pwn2Own Ireland 2024: Canon imageCLASS MF656Cdw</a> - Some embedded hacking, and a fun description on how they set up a remote exploitation lab.</li>
<li><a href="https://trustedsec.com/blog/red-team-gold-extracting-credentials-from-mdt-shares" target="_blank">Red Team Gold: Extracting Credentials from MDT Shares</a> - Find creds and other goodies on Microsoft Deployment Toolkit (MDT) shares. Only thing this post is missing is a role for <a href="https://ludus.cloud/" target="_blank">Ludus</a> to setup MDT in a lab.</li>
<li><a href="https://whiteknightlabs.com/2025/05/27/understanding-integer-overflow-in-windows-kernel-exploitation/" target="_blank">Understanding Integer Overflow in Windows Kernel Exploitation</a> - Get your feet wet with Windows Kernel exploitation by triggering some blue screens with integer overflows.</li>
<li><a href="https://blog.zsec.uk/offensive-cti/" target="_blank">Offensive Threat Intelligence</a> - "It’s not about knowing threats, it’s about becoming them long enough to help others beat them." I would argue LWiS is "Offensive Threat Intelligence." You should be taking ideas and tools from this blog to improve your red/blue team.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/logangoins/SharpSuccessor" target="_blank">SharpSuccessor</a> - SharpSuccessor is a .NET Proof of Concept (POC) for fully weaponizing Yuval Gordon’s (<a href="https://x.com/YuG0rd" target="_blank">@YuG0rd</a>) BadSuccessor attack from Akamai.</li>
<li><a href="https://github.com/LuemmelSec/Pentest-Tools-Collection/blob/main/tools/ActiveDirectory/BadSuccessor.ps1" target="_blank">BadSuccessor.ps1</a> - BadSuccessor checks for prerequisites and attack abuse.</li>
<li><a href="https://github.com/zarkones/OnionC2" target="_blank">OnionC2</a> - C2 written in Rust &amp; Go powered by Tor network.</li>
<li><a href="https://github.com/microsoft/AI-Red-Teaming-Playground-Labs" target="_blank">AI-Red-Teaming-Playground-Labs</a> - AI Red Teaming playground labs to run AI Red Teaming trainings including infrastructure.</li>
<li><a href="https://github.com/cyndicatelabs/brc4_profile_maker" target="_blank">brc4_profile_maker</a> - An interactive TUI tool to create Brute Ratel C4 profiles based on BURP browsing data.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/kunai-project/kunai" target="_blank">kunai</a> - Threat-hunting tool for Linux.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 452 (+0)</p>
<p>Blogs monitored: 420 (+2)</p>
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
