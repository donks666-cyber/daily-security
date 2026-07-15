Title: Last Week in Security (LWiS) - 2025-01-27
Date: 2025-01-27 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-01-27
Author: Erik
Summary: 0-click deanonymization (<a href="https://x.com/hackermondev" target="_blank">@hackermondev</a>), Subaru hacks (<a href="https://x.com/samwcyo" target="_blank">@samwcyo</a> + <a href="https://x.com/infosec_au" target="_blank">@infosec_au</a>), 🍪 sandwitch (<a href="https://x.com/d4d89704243" target="_blank">@d4d89704243</a>), Entra Connect attacks (<a href="https://x.com/hotnops" target="_blank">@hotnops</a>), Kerberos relaying via HTTP (<a href="https://x.com/croco_byte" target="_blank">@croco_byte</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-01-20 to 2025-01-27.</p>
<aside class="m-note m-success">
Last Week in Security will be off next week as we work on enhancements to <a href="https://ludus.cloud" target="_blank">Ludus</a>.</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.securityweek.com/dhs-disbands-cyber-safety-review-board-ending-one-of-cisas-few-bright-spots/" target="_blank">DHS Disbands Cyber Safety Review Board, Ending One of CISA's Few Bright Spots</a> - Their <a href="https://www.cisa.gov/sites/default/files/2024-04/CSRB_Review_of_the_Summer_2023_MEO_Intrusion_Final_508c.pdf" target="_blank">Review of the Summer 2023 Microsoft Exchange Online Intrusion</a> was not only thorough but also pretty scathing and led to <a href="https://www.securityweek.com/microsoft-overhauls-cybersecurity-strategy-after-scathing-csrb-report/" target="_blank">real change</a>. This disbanding comes as the board was in the middle of the <a href="https://en.wikipedia.org/wiki/Salt_Typhoon" target="_blank">Salt Typhoon</a> telecom hack investigation.</li>
<li><a href="https://openai.com/index/announcing-the-stargate-project/" target="_blank">Announcing The Stargate Project</a> - $500B promised and $100B "deploying immediately" for building new AI infrastructure for OpenAI in the United States. If only OpenAI was actually Open. A world where Oracle, whose founder said <a href="https://arstechnica.com/information-technology/2024/09/omnipresent-ai-cameras-will-ensure-good-behavior-says-larry-ellison/" target="_blank">"omnipresent AI cameras will ensure good behavior"</a>, controls artificial general intelligence is a nightmare. Oracle's old headquarters were even used as Cyberdyne's headquarters (the creators of Skynet) in Terminator Genisys.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://samcurry.net/hacking-subaru" target="_blank">Hacking Subaru: Tracking and Controlling Cars via the STARLINK Admin Panel</a> - A must read this week. The 2FA bypass was particularly egregious (just delete the popup 🤣). Really makes you want to by a 2006-vintage vehicle with none of this remote-management. Note that STARLINK is the Subaru internet connected car service, and is in no way related to the SpaceX satellite internet service.</li>
<li><a href="https://labs.watchtowr.com/get-fortirekt-i-am-the-super_admin-now-fortios-authentication-bypass-cve-2024-55591/" target="_blank">Get FortiRekt, I Am The Super_Admin Now - Fortinet FortiOS Authentication Bypass CVE-2024-55591</a> - I mean, at this point, shame on you if you're still running an SSL VPN? Just tear it out and use Tailscale? The risk of keeping an SSL VPN isn't worth that CISO salary (and will cause it to abruptly end). Another slam dunk by watchTowr, that comes with a PoC: <a href="https://github.com/watchtowrlabs/fortios-auth-bypass-poc-CVE-2024-55591" target="_blank">fortios-auth-bypass-poc-CVE-2024-55591</a>.</li>
<li><a href="https://bryce.co/undebuggable/" target="_blank">Debugging An Undebuggable App</a> - How to use lldb and a dissassembler to get around some debug protections, including a force crash, in an iOS app. The <a href="https://www.youtube.com/watch?v=ih6gWZDuNME" target="_blank">video walkthrough</a> is expertly done and worth a watch even if you don't have much interest in iOS.</li>
<li><a href="https://portswigger.net/research/stealing-httponly-cookies-with-the-cookie-sandwich-technique" target="_blank">Stealing HttpOnly cookies with the cookie sandwich technique</a> - A combination of vulnerabilties (including XSS) allows Zakhar to leak the PHPSESSID of any visitor to a site.</li>
<li><a href="https://blog.lumen.com/the-j-magic-show-magic-packets-and-where-to-find-them/" target="_blank">The J-Magic Show: Magic Packets And Where To Find Them</a> - The addition of a challenge-response to the cd00r backdoor is interesting, but the self-signed certificates and lack of replay-protection indicates it's use by a mid tier threat actor.</li>
<li><a href="https://gist.github.com/hackermondev/45a3cdfa52246f1d1201c1e8cdef6117" target="_blank">Unique 0-click deanonymization attack targeting Signal, Discord and hundreds of platform</a> - Using a global CDN's cache to narrow down a user's physical location as they load content is brilliant.</li>
<li><a href="https://krebsonsecurity.com/2025/01/mastercard-dns-error-went-unnoticed-for-years/" target="_blank">MasterCard DNS Error Went Unnoticed for Years</a> - A one-letter mistake (<cite>akam.ne</cite> vs <cite>akam.net</cite>) could have led to serious issues. The Bugcrowd response was strange, as this wasn't even reported via Bugcrowd.</li>
<li><a href="https://posts.specterops.io/entra-connect-attacker-tradecraft-part-2-672df0147abc" target="_blank">Entra Connect Attacker Tradecraft: Part 2</a> - Hybrid environments (on-prem AD + Entra AD) present a lot of complicated connections, ripe for exploitation. This post explores how to add credentials to a user in another domain within the same Entra tenant given a sync account.</li>
<li><a href="https://starlabs.sg/blog/2025/cve-2024-26230-windows-telephony-service-its-got-some-call-ing-issues/" target="_blank">CVE-2024-26230: Windows Telephony Service - It's Got Some Call-ing Issues (Elevation of Privilege)</a> - While the vulnerabilies were patched in April and November of 2024, the post walks through exploitation and provides a <a href="https://github.com/star-sg/CVE/tree/master/CVE-2024-26230" target="_blank">PoC</a>.</li>
<li><a href="https://jprx.io/cve-2024-54507/" target="_blank">SUSCTL (CVE-2024-54507)</a> - "This bug is a neat example of how difficult kernel programming can be. Even the most seemingly innocuous loads can be deadly. Even though the authors were careful to prevent integer overflows, information leakage was still possible due to the initial 4-byte load." PoC: <a href="https://github.com/jprx/CVE-2024-54507" target="_blank">CVE-2024-54507</a> - An integer type confusion in XNU.</li>
<li><a href="https://jm33.me/offensive-cgo-an-elf-loader.html" target="_blank">Offensive CGO - An ELF Loader</a> - A mostly working ELF loader for Go (fails to capture output).</li>
<li><a href="https://www.synacktiv.com/en/publications/abusing-multicast-poisoning-for-pre-authenticated-kerberos-relay-over-http-with">Abusing Multicast Poisoning for Pre-Authenticated Kerberos Relay Over HTTP With Responder and Krbrelayx</a> - If you in the multicast domain of a target that does not support signing and sealing for Kerberos authentication over HTTP (i.e. ADCS Web Enrollment, SCCM Management Point, or SCCM Distribution Point), you can now spoof an LLMNR response to achieve Kerberos relaying via HTTP. This was discovered by <a href="https://googleprojectzero.blogspot.com/2021/10/using-kerberos-for-authentication-relay.html">James Forshaw</a> and reported in <a href="https://blog.badsectorlabs.com/last-week-in-security-lwis-2021-10-27.html">LWiS 2021-10-27</a>, but <a href="https://x.com/croco_byte">@croco_byte</a> has add supported to <a href="https://github.com/lgandx/Responder/pull/301">Responder</a> and <a href="https://github.com/dirkjanm/krbrelayx/pull/51">Krbrelayx</a>.</li>
<li><a href="https://flatt.tech/research/posts/clone2leak-your-git-credentials-belong-to-us/" target="_blank">Clone2Leak: Your Git Credentials Belong To Us</a> - A number of issues with Git and Git tools related to text parsing and newline injection.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/x86matthew/WinVisor" target="_blank">WinVisor</a> - WinVisor - A hypervisor-based emulator for Windows x64 user-mode executables using Windows Hypervisor Platform API. Full here <a href="https://www.elastic.co/security-labs/winvisor-hypervisor-based-emulator" target="_blank">WinVisor</a>.</li>
<li><a href="https://github.com/dhmosfunk/7-Zip-CVE-2025-0411-POC" target="_blank">7-Zip-CVE-2025-0411-POC</a> - This repository contains POC scenarios as part of CVE-2025-0411 MotW bypass.</li>
<li><a href="https://github.com/NtDallas/Draugr" target="_blank">Draugr</a> - BOF with Synthetic Stackframe.</li>
<li><a href="https://github.com/offalltn/gitC2" target="_blank">gitC2</a> is a simple C2 POC that leverages a GitHub repository for executing commands through issues.</li>
<li><a href="https://github.com/NtDallas/OdinLdr" target="_blank">OdinLdr</a> - Cobaltstrike Reflective Loader with Synthetic Stackframe.</li>
<li><a href="https://github.com/NoahKirchner/speedloader" target="_blank">speedloader</a> - Rust template/library for implementing your own COFF loader.</li>
<li><a href="https://github.com/ghost-ng/slinger" target="_blank">slinger</a> - An impacket-lite cli tool that combines many useful impacket functions using a single session.</li>
<li><a href="https://github.com/Teach2Breach/rpeloader" target="_blank">rpeloader</a> - use python on windows with full submodule support without installation.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://infosecwriteups.com/reversing-discovering-and-exploiting-a-tp-link-router-vulnerability-cve-2024-54887-341552c4b104" target="_blank">Reversing, Discovering, And Exploiting A TP-Link Router Vulnerability — CVE-2024-54887</a> - A nice MIPS buffer overflow with ROP.</li>
<li><a href="https://jhalon.github.io/breaking-into-cyber-security/" target="_blank">So You Want To Work in Cyber Security?</a> - The most complete write-up on how to get into cybersecurity I've seen in a long time.</li>
<li><a href="https://github.com/HulkOperator/AuthStager" target="_blank">AuthStager</a> is a proof-of-concept tool that generates a custom stager shellcode that authenticates to the stager server using an authentication token. The server validates client requests before sending the second stage, enhancing security in the staging process. The detailed information regarding this project is explained in this blog post: <a href="https://hulkops.gitbook.io/blog/red-team/stage-but-verify" target="_blank">Stage, But Verify</a>.</li>
<li><a href="https://github.com/LuemmelSec/APEX" target="_blank">APEX</a> - Azure Post Exploitation Framework.</li>
<li><a href="https://github.com/nickvourd/CS-Aggressor-Kit" target="_blank">CS-Aggressor-Kit</a> - Homemade Aggressor scripts kit for Cobalt Strike.</li>
<li><a href="https://www.dsinternals.com/en/smb-signing-windows-server-2025-client-11-24h2-defaults/" target="_blank">Changes to SMB Signing Enforcement Defaults in Windows 24H2</a> - Are you still profiting from NTLM-based attacks? Yeah same here. But apparently things will change? Eventually?</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 444 (+1)</p>
<p>Blogs monitored: 403 (+2)</p>
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
