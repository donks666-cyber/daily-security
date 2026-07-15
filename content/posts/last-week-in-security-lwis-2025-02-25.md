Title: Last Week in Security (LWiS) - 2025-02-25
Date: 2025-02-25 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-02-25
Author: Erik
Summary: ADIDNS Parser (<a href="https://x.com/the_bit_diddler" target="_blank">@the_bit_diddler</a>), Parallels LPE (<a href="https://x.com/patch1t" target="_blank">@patch1t</a>), PowerChell (<a href="https://x.com/itm4n" target="_blank">@itm4n</a>), SACL Scanner (Alexander DeMine of <a href="https://x.com/SpecterOps" target="_blank">@SpecterOps</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-02-17 to 2025-02-25.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.bbc.com/news/articles/cgj54eq4vejo" target="_blank">Apple pulls data protection tool after UK government security row</a> - There were leaks, but now it's official. Apple is, “gravely disappointed” to have to remove <a href="https://support.apple.com/en-us/108756" target="_blank">Advanced Data Protection</a> (ADP) from UK users. While the orders are still secret, having to disable fully end-to-end encryption for data gives you can idea of what the UK government is after - the ability to collect data on any UK iCloud user whenever they want. Critically, iOS backups are not end-to-end encrypted under "standard protection," allowing those with access to the keys on Apple's servers to pull a full backup of all data on an iOS device that has been backed up to the cloud.</li>
<li><a href="https://www.theblock.co/post/342667/crypto-exchange-bybit-hacked-as-over-1-billion-worth-of-eth-leaves-wallets" target="_blank">Crypto exchange Bybit confirms hack as over $1.4 billion worth of ETH leaves wallets</a> - We will likely never get a detailed post-mortem, but it looks like an extremely well done attack that involved malware infection and <a href="https://research.checkpoint.com/2025/the-bybit-incident-when-research-meets-reality/" target="_blank">UI manipulation</a>.</li>
<li><a href="https://taleliyahu.medium.com/top-20-cyber-security-newsletters-d675e53d7ef4" target="_blank">Top 25 Cyber Security Newsletters — 2025</a> - LWiS made the list!</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.inversecos.com/2025/02/an-inside-look-at-nsa-equation-group.html" target="_blank">An inside look at NSA (Equation Group) TTPs from China’s lense</a> - Research by <a href="https://x.com/inversecos?lang=en&amp;mx=2" target="_blank">@inversecos</a>  on why China has attributed Northwestern Polytechnical University (Chinese University) breach to the U.S. National Security Agency (NSA). "It is important to note that the authenticity and extent of these allegations remain unverified by independent sources." A key observation from the Chinese case notes was the extensive use of big data analysis, particularly in tracking “hands-on keyboard” activity.</li>
<li><a href="https://thegreycorner.com/2025/02/12/containerd-socket-exploitation-part-1.html" target="_blank">containerd socket exploitation part 1</a> and <a href="https://thegreycorner.com/2025/02/19/containerd-socket-exploitation-part-2.html" target="_blank">part 2</a> - Part 1 explains how to exploit the containerd socket using the ctr command-line tool for lateral movement or privilege escalation in containerized environments, while Part 2 delves into more complex techniques using curl when the ctr tool isn't available.</li>
<li><a href="https://blog.chebuya.com/posts/server-side-request-forgery-on-sliver-c2/" target="_blank">SSRF on Sliver C2 teamserver via spoofed implant callback (CVE-2025-27090)</a> - Cool find. The <a href="https://github.com/chebuya/exploits/tree/main/CVE-2025-27090%3A%20Sliver%20C2%20SSRF" target="_blank">POC</a> can be found here. Don't expose those teamservers!</li>
<li><a href="https://posts.specterops.io/dont-touch-that-object-finding-sacl-tripwires-during-red-team-ops-248269883559" target="_blank">Don’t Touch That Object! Finding SACL Tripwires During Red Team Ops</a> - With deception technologies becoming pretty standard in mature environments, red teamers are incorporating them into their SOPs. New tool drop as well (<a href="https://github.com/ToweringDragoon/SACL_Scanner" target="_blank">SACL_Scanner</a>)!</li>
<li><a href="https://www.synacktiv.com/publications/lsa-secrets-revisiting-secretsdump" target="_blank">LSA Secrets: revisiting secretsdump</a> - If the old faithful secretsdump.py is getting caught, give <a href="https://github.com/fortra/impacket/pull/1898" target="_blank">regsecrets and dpapidump</a> a shot!</li>
<li><a href="https://www.kandji.io/blog/macos-audit-story-part3" target="_blank">Uncovering Apple Vulnerabilities: diskarbitrationd and storagekitd Audit Part 3</a> - The final post of a 3-part series on how attackers can weaponize mount based vulnerabilities.</li>
<li><a href="https://jhftss.github.io/Parallels-0-day/" target="_blank">Dropping a 0 day: Parallels Desktop Repack Root Privilege Escalation</a> - Unfortunate that despite good faith disclosure this has to be dropped as an 0day.</li>
<li><a href="https://blog.sshh.io/p/how-to-backdoor-large-language-models" target="_blank">How to Backdoor Large Language Models</a> - "In this article, I want to explain why relying on “untrusted” models can still be risky, and why open-source won’t always guarantee safety. To illustrate, I built my own backdoored LLM called 'BadSeek.'"</li>
<li><a href="https://blog.scrt.ch/2025/02/18/reinventing-powershell-in-c-c/" target="_blank">Reinventing PowerShell in C/C++</a> - Some really great research into writing a custom powershell console that evades pretty much every protection around powershell. Check out <a href="https://github.com/scrt/PowerChell" target="_blank">PowerChell</a> - A PowerShell console in C/C++ with all the security features disabled.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/EspressoCake/ADIDNS_Parser" target="_blank">ADIDNS_Parser</a> - Parser and reconciliation tooling for large Active Directory environments.</li>
<li><a href="https://github.com/trustedsec/DitExplorer" target="_blank">DitExplorer</a> - Tool for viewing NTDS.dit. Read more: <a href="https://trustedsec.com/blog/exploring-ntds-dit-part-1-cracking-the-surface-with-dit-explorer" target="_blank">Exploring NTDS.dit – Part 1: Cracking the Surface with DIT Explorer</a>.</li>
<li><a href="https://github.com/0xjessie21/CVE-2025-24016" target="_blank">CVE-2025-24016</a> - CVE-2025-24016: Wazuh Unsafe Deserialization Remote Code Execution (RCE).</li>
<li><a href="https://github.com/ToweringDragoon/SACL_Scanner" target="_blank">SACL_Scanner</a> - SACL Scanner is a tool designed to scan and analyze SACLs.</li>
<li><a href="https://github.com/captainGeech42/implant.js" target="_blank">implant.js</a> - Proof-of-concept modular implant platform leveraging v8.</li>
<li><a href="https://github.com/Arcanum-Sec/msftrecon" target="_blank">msftrecon</a> - MSFTRecon is a reconnaissance tool designed for red teamers and security professionals to map Microsoft 365 and Azure tenant infrastructure. It performs comprehensive enumeration without requiring authentication, helping identify potential security misconfigurations and attack vectors.</li>
<li><a href="https://github.com/0xRedpoll/SignalKeyBOF" target="_blank">SignalKeyBOF</a> - BOF to decrypt Signal Desktop chat logs.</li>
<li><a href="https://github.com/xforcered/SoaPy" target="_blank">SoaPy</a> - SoaPy is a Proof of Concept (PoC) tool for conducting offensive interaction with Active Directory Web Services (ADWS) from Linux hosts.</li>
<li><a href="https://github.com/RedTeamPentesting/keycred" target="_blank">keycred</a> - Generate and Manage KeyCredentialLinks.</li>
<li><a href="https://github.com/BishopFox/sonicrack" target="_blank">sonicrack</a> - Decrypt encrypted SonicOSX firmware images.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/sensepost/susinternals" target="_blank">susinternals</a> - psexecsvc - a python implementation of PSExec's native service implementation.</li>
<li><a href="https://nucleiprompts.com/" target="_blank">Nuclei AI Prompts</a> - "Enhance your security testing with AI-powered Nuclei prompts."</li>
<li><a href="https://github.com/H4NM/WhoYouCalling" target="_blank">WhoYouCalling</a> - Records an executable's network activity into a Full Packet Capture file (.pcap) and much more.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 444 (+0)</p>
<p>Blogs monitored: 405 (+0)</p>
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
