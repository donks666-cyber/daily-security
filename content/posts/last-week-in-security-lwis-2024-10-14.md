Title: Last Week in Security (LWiS) - 2024-10-14
Date: 2024-10-14 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-10-14
Author: Erik
Summary: FortiGate exploit (<a href="https://x.com/watchtowrcyber" target="_blank">@watchtowrcyber</a>), Azure admin approval bypass (<a href="https://x.com/PedroGabaldon" target="_blank">@PedroGabaldon</a>), dylib 💉 in Teams (<a href="https://x.com/Coiffeur0x90" target="_blank">@Coiffeur0x90</a>), Ivanti Connect Secure vuln (<a href="https://x.com/buffaloverflow" target="_blank">@buffaloverflow</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-10-07 to 2024-10-14.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.wsj.com/tech/cybersecurity/u-s-wiretap-systems-targeted-in-china-linked-hack-327fc63b" target="_blank">U.S. Wiretap Systems Targeted in China-Linked Hack</a> - Adversaries using "lawful" backdoors for access. Remember this story the next time a <a href="https://www.europol.europa.eu/media-press/newsroom/news/european-police-chiefs-call-for-industry-and-governments-to-take-action-against-end-to-end-encryption-roll-out" target="_blank">politician demands a backdoor on end-to-end encryption</a> to "protect the children" or whatever the rallying cry of the day is.</li>
<li><a href="https://research.checkpoint.com/2024/disinformation-campaign-moldova/" target="_blank">Operation Middlefloor: Disinformation Campaign Targets Moldova Ahead of Presidential Elections and Eu Membership Referendum</a> - Current events are used to initiate cyber attacks. The use of "feedback forms" to gather detailed information about victims for further targeting is an interesting move and shows a level of sophistication and persistence above the standard cybercriminal.</li>
<li><a href="https://krebsonsecurity.com/2024/10/lamborghini-carjackers-lured-by-243m-cyberheist/" target="_blank">Lamborghini Carjackers Lured by $243M Cyberheist</a> - Some impressively poor OPSEC on display here. The lack of any tact in using the stolen funds also didn't help the criminals/now-victims. Cryptocurrency remains the wild west.</li>
<li><a href="https://www.securityweek.com/collapse-of-national-security-elites-cyber-firm-leaves-bitter-wake/" target="_blank">Collapse of National Security Elites' Cyber Firm Leaves Bitter Wake</a> - IronNet was once valued at $3 billion when it IPO'd in 2021 despite never being profitable, relying on the name of its founder former NSA head Keith Alexander. Is IronNet the <a href="https://en.wikipedia.org/wiki/Theranos" target="_blank">Theranos</a> of cybersecurity?</li>
<li><a href="https://www.abc.net.au/news/2024-10-05/robot-vacuum-deebot-ecovacs-photos-ai/104416632" target="_blank">Insecure Deebot robot vacuums collect photos and audio to train AI</a> - Hopefully there will be a market of fully-offline capable IoT devices as consumers become aware of the risks of these internet connected sensor platforms in their homes, but based on the rise of social media, the average consumer cares little for privacy.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.quarkslab.com/exploiting-microsoft-teams-on-macos-during-a-purple-team-engagement.html" target="_blank">Exploiting Microsoft Teams on macOS during a Purple Team engagement</a> - macOS tradecraft posts are rare, and tradecraft that works on the latest Microsoft Teams and macOS 14.4 (Sonoma) is even more rare. This post covers post-exploitation actions on macOS using Teams to bypass macOS TCC (Transparency, Consent, and Control) as well as persistence.</li>
<li><a href="https://theevilbit.github.io/beyond/beyond_0034/" target="_blank">Beyond the good ol' LaunchAgents - 34 - launchd boot tasks</a> - More macOS tradecraft, but this one requires a TCC bypass or root and a SIP (System Integrity Protection) bypass.</li>
<li><a href="https://pgj11.com/posts/Bypass-Azure-Admin-Approval-Mode-Enumeration/" target="_blank">Bypass Azure Admin Approval Mode for User Consent Workflow When Enumerating</a> - Skip the admin approval workflow by issuing yourself a token for an existing application with the entitlements you need, like <cite>SharePoint Online Web Client Extensibility</cite>.</li>
<li><a href="https://labs.watchtowr.com/fortinet-fortigate-cve-2024-23113-a-super-complex-vulnerability-in-a-super-secure-appliance-in-2024/" target="_blank">Fortinet FortiGate CVE-2024-23113 - A Super Complex Vulnerability In A Super Secure Appliance In 2024</a> - The watchtowr labs researchers find yet another vulnerability in an SSL VPN.</li>
<li><a href="https://blog.amberwolf.com/blog/2024/october/cve-2024-37404-ivanti-connect-secure-authenticated-rce-via-openssl-crlf-injection/" target="_blank">Ivanti Connect Secure - Authenticated RCE via OpenSSL CRLF Injection (CVE-2024-37404)</a> - Another SSLVPN vulnerability, this time authenticated arbitrary code execution as root.</li>
<li><a href="https://trustedsec.com/blog/ekuwu-not-just-another-ad-cs-esc" target="_blank">EKUwu: Not just another AD CS ESC</a> ESC15 coming in hot! <a href="https://github.com/ly4k/Certipy/pull/228/commits/b9e87bbf09345d1364b6ff5108130bf9ee80fa47" target="_blank">Certipy PR</a> has been submitted.</li>
<li><a href="https://goodworkaround.com/2024/10/14/issuing-custom-security-attributes-in-entra-id-tokens/?linkedin" target="_blank">Issuing Custom Security Attributes in Entra ID tokens</a> - In this blogpost, the author demonstrates how to use the custom claims provider functionality of Entra ID custom authentication extensions in order to issue Custom Security Attributes as claims.</li>
<li><a href="https://medmahmoudi.com/projects/how-i-found-a-p2-misrouting-issue-affecting-all-google-cloud-load-balancers" target="_blank">How I found a P2 Misrouting issue affecting all Google Cloud Load Balancers</a> - "...By crafting unconventional HTTP requests, I stumbled upon a flaw that reveals sensitive bucket names and opens the door for attackers to exploit load balancers in unexpected ways.". Always fun to read about cloud vulnerabilities.</li>
<li><a href="https://securitymaven.medium.com/when-usbs-attack-exploring-the-underbelly-of-malicious-lnk-files-f536d5dbc753" target="_blank">When USBs Attack: Exploring the Underbelly of Malicious LNK Files</a> - If you're still doing physicals and wanted to know a little bit more about how USBs can be used as initial access payloads, give this a read!</li>
<li><a href="https://harfanglab.io/insidethelab/hijackloader-abusing-genuine-certificates/" target="_blank">HijackLoader evolution: abusing genuine signing certificates</a> - CTI read on how tools like <a href="https://github.com/JohnHammond/recaptcha-phish" target="_blank">recaptcha-phish</a> - were weaponized by attackers.</li>
<li><a href="https://www.r-tec.net/r-tec-blog-dll-sideloading.html" target="_blank">DLL Sideloading</a> - Good writeup on the topic. Summarizes the differences between hijacking, sideloading, proxying, etc. Good read if you need a good intro to these concepts.</li>
<li><a href="https://blog.apnic.net/2024/10/14/how-to-inspect-tls-encrypted-traffic/" target="_blank">How to inspect TLS encrypted traffic</a> - Good walkthrough for attackers and defenders.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/vxCrypt0r/Voidmaw" target="_blank">Voidmaw</a> - A new technique that can be used to bypass memory scanners. This can be useful in hiding problematic code (such as reflective loaders implemented by C2 beacons) or other problematic executables that will be flagged by the antimalware programs(such as mimikatz).</li>
<li><a href="https://github.com/Krypteria/Proxll" target="_blank">Proxll</a> - Tool designed to simplify the generation of proxy DLLs while addressing common conflicts related to windows.h.</li>
<li><a href="https://github.com/NocteDefensor/Sharelord" target="_blank">Sharelord</a> - .NET Assembly that creates network shares, sets ACE entries for directories, sets share perms, and deletes shares. Learning project for C#.</li>
<li><a href="https://github.com/adanalvarez/TrailDiscover" target="_blank">TrailDiscover</a> - An evolving repository of CloudTrail events with detailed descriptions, MITRE ATT&amp;CK insights, real-world incidents, references and security implications.</li>
<li><a href="https://github.com/ANSSI-FR/orc2timeline" target="_blank">orc2timeline</a> - orc2timeline extracts and analyzes artifacts contained in archives generated with DFIR-ORC.exe to create a timeline from them.</li>
<li><a href="https://github.com/horizon3ai/CVE-2024-9465" target="_blank">CVE-2024-9465</a> - Proof of Concept Exploit for CVE-2024-9465 (Palo Alto Expedition unauthenticated SQL injection).</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/slygoo/pssrecon" target="_blank">pssrecon</a> - Small tool to perform SCCM recon and enumerate a Primary Site Server (PSS) or Distribution Point (DP) over winreg. This can enumerate useful information such as the Site Database, whether a DP allows anonymous access, if a DP is PXE enabled and the location of Management Points (MP) in the site.</li>
<li><a href="https://github.com/intigriti/misconfig-mapper" target="_blank">misconfig-mapper</a> - Misconfig Mapper is a fast tool to help you uncover security misconfigurations on popular third-party services used by your company and/or bug bounty targets!</li>
<li><a href="https://github.com/AaLl86/MiniKvm_public" target="_blank">MiniKvm_public</a> - This repo contains all the code and documentation for the MiniKvm project and the CH9329 controller.</li>
<li><a href="https://github.com/sudonoodle/Aggressor-Aggregator" target="_blank">Aggressor-Aggregator</a> - A helper script for consolidating Aggressor and BOF repositories into a single CNA for Cobalt Strike.</li>
<li><a href="https://github.com/CobblePot59/ADcheck" target="_blank">ADcheck</a> - Assess the security of your Active Directory with few or all privileges.</li>
<li><a href="https://github.com/mandiant/gocrack" target="_blank">gocrack</a> - GoCrack is a management frontend for password cracking tools written in Go.</li>
<li><a href="https://0xanalyst.github.io/Project-Lost/" target="_blank">Living Off Security Tools</a> - It was only a matter of time. Let's not forget <a href="https://gitlab.com/badsectorlabs/iscariot-suite" target="_blank">Iscariot Suite</a>. Not sure if this project will take off or not but we will track it.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 439 (+0)</p>
<p>Blogs monitored: 396 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing. 4</p>
</section>
