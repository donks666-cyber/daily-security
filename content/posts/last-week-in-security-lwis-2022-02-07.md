Title: Last Week in Security (LWiS) - 2022-02-07
Date: 2022-02-07 20:57
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-02-07
Author: Erik
Summary: EXE in LNK embeds (<a href="https://twitter.com/x86matthew" target="_blank">@x86matthew</a>), LinkedIn Slink phishers (<a href="https://twitter.com/briankrebs" target="_blank">@briankrebs</a>), Apollo 2.0 (<a href="https://twitter.com/djhohnstein" target="_blank">@djhohnstein</a>), modern relaying (<a href="https://twitter.com/Jean_Maes_1994" target="_blank">@Jean_Maes_1994</a>), exfil with Power Automate (<a href="https://twitter.com/varonis" target="_blank">@varonis</a>), sandboxing defender (<a href="https://twitter.com/GabrielLandau" target="_blank">@GabrielLandau</a>), SysWhispers rundown (<a href="https://twitter.com/KlezVirus" target="_blank">@KlezVirus</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-01-31 to 2022-02-07.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://portswigger.net/daily-swig/vulnerabilities-in-cisco-small-business-routers-could-allow-unauthenticated-attackers-persistent-access-to-internal-networks" target="_blank">Vulnerabilities in Cisco Small Business routers could allow unauthenticated attackers persistent access to internal networks</a>. This was the CVE of last week, a full 10.0 on the CVSS scale (RCE as root). SSL VPN gateways continue to be a juicy target for attackers.</li>
<li><a href="https://www.samba.org/samba/security/CVE-2021-44142.html" target="_blank">Out-of-bounds heap read/write vulnerability in VFS module vfs_fruit allows code execution</a>. This takes the #2 spot for most hyped CVE of last week. The vfs_fruit module is used for macOS compatibility, and is enabled on many prosumer NAS devices by default. No PoC yet, technical details <a href="https://www.zerodayinitiative.com/blog/2022/2/1/cve-2021-44142-details-on-a-samba-code-execution-bug-demonstrated-at-pwn2own-austin" target="_blank">here</a>.</li>
<li><a href="https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805" target="_blank">Helping users stay safe: Blocking internet macros by default in Office</a>. It's about time! While there are certainly valid use cases for macros, they should be a bigger challenge to enable than a simple click given the damage they can do. Here's to hoping organizations patch. I'll be pouring one out for this old red team favorite in April.</li>
<li><a href="https://openssf.org/community/alpha-omega/" target="_blank">Alpha-Omega Project</a>. This project aims to attack open source software vulnerability from both ends, maintainers and end users. Specifics are light, but if it means more fuzzing or code analysis on popular open source projects, that's a good thing.</li>
<li><a href="https://www.eff.org/deeplinks/2022/02/its-back-senators-want-earn-it-bill-scan-all-online-messages" target="_blank">It’s Back: Senators Want EARN IT Bill to Scan All Online Messages</a>. US Senate again tries to open up the path for widespread surveillance by making private companies scan all content and report "violations" to law enforcement. I'm sure they will use the line "protect the children" in their push to get it passed.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.x86matthew.com/view_post?id=embed_exe_lnk" target="_blank">EmbedExeLnk - Embedding an EXE inside a LNK with automatic execution</a>. This is a really neat multi-layered payload. It's a LNK that runs powershell to extract an EXE from itself, drop, and run that exe. This way LNK based attacks can be totally self contained.</li>
<li><a href="https://krebsonsecurity.com/2022/02/how-phishers-are-slinking-their-links-into-linkedin/" target="_blank">How Phishers Are Slinking Their Links Into LinkedIn</a>. LinkedIn has marketing "feature" that is proving to be useful for phishers to hide their links. LinkedIn is (for now) a pretty high reputation site.</li>
<li><a href="https://research.nccgroup.com/2022/02/07/a-deeper-dive-into-cve-2021-39137-a-golang-security-bug-that-rust-would-have-prevented/" target="_blank">A deeper dive into CVE-2021-39137 – a Golang security bug that Rust would have prevented</a>. A headline sure to start a holy war. If you're interested in low level language details you'll enjoy this post.</li>
<li><a href="https://research.nccgroup.com/2022/02/02/testing-infrastructure-as-code-using-dynamic-tooling/" target="_blank">Testing Infrastructure-as-Code Using Dynamic Tooling</a>. The <a href="https://github.com/ncc-erik-steringer/Aerides" target="_blank">Aerides</a> tool is capable of mocking the appropriate AWS API endpoints to allow "normal" tools to run (terraform, etc). This allows infrastructure as code to be tested in CI pipelines with automated tooling easily.</li>
<li><a href="https://shells.systems/dnsstager-v1-0-stable-stealthier-code-dll-agent-much-more/" target="_blank">DNSStager v1.0 stable: Stealthier code, DLL agent &amp; much more</a>. DNS has always been a gamble for me. Either the SOC never sees it because they aren't monitoring DNS, or it gets instantly caught because it sticks out so badly. There isn't really a middle ground. This new version looks like it does well against MS365 (ATP) which is no small feat.</li>
<li><a href="https://posts.specterops.io/apollo-2-0-new-year-new-features-48acdf4898d3" target="_blank">Apollo 2.0 — New Year, New Features</a>. Hot on the heals of the Mythic update, the Apollo agent gets a massive update! Props to Dwight for such an amazing changelog! Dynamic content loading, P2P over SMB or TCP, SOCK5 proxying, in-process assembly execution, PE execution, and smaller file size. Apollo has arrived!</li>
<li><a href="https://www.trustedsec.com/blog/a-comprehensive-guide-on-relaying-anno-2022/" target="_blank">I’m bringing relaying back: A comprehensive guide on relaying anno 2022</a>. Appropriate title. If you have missed the developments in relaying over the past few years, this will get you up to speed.</li>
<li><a href="https://www.varonis.com/blog/power-automate-data-exfiltration" target="_blank">Using Power Automate for Covert Data Exfiltration in Microsoft 365</a>. Creating "flows" between Microsoft apps can also allow attackers to create "flows" of your data off to OneDrive. Best/worst part? It's enabled by default for any M365 user.</li>
<li><a href="https://elastic.github.io/security-research/whitepapers/2022/02/02.sandboxing-antimalware-products-for-fun-and-profit/article/#" target="_blank">Sandboxing Antimalware Products for Fun and Profit</a>. This was the original post (and original <a href="https://github.com/MartinIngesen/TokenStomp" target="_blank">PoC</a>) that set off a string of researchers implementing the technique in <a href="https://github.com/byt3bl33d3r/OffensiveNim/blob/master/src/sandbox_process_bin.nim" target="_blank">Nim</a>, <a href="https://github.com/pwn1sher/KillDefender" target="_blank">C++</a>, <a href="https://github.com/plackyhacker/SandboxDefender" target="_blank">C#</a>, and even a <a href="https://github.com/Cerbersec/KillDefenderBOF" target="_blank">BOF</a>.</li>
<li><a href="https://klezvirus.github.io/RedTeaming/AV_Evasion/NoSysWhisper/" target="_blank">SysWhispers is dead, long live SysWhispers!</a>. This post is a one-stop-shop for your SysWhispers knowledge.</li>
<li><a href="https://github.com/tyranid/infosec-presentations/blob/master/OffensiveCon/2022/This%20are%20my%20principals.pdf" target="_blank">This are my principals.pdf [PDF]</a>. This is James Forshaw's deck from OffensiveCon 2022. My rule is to read anything James publishes, but this deck would benefit from the recorded talk to give context.</li>
<li><a href="https://github.com/RedTeamOperations/Advanced-Process-Injection-Workshop" target="_blank">Advanced-Process-Injection-Workshop</a>. This is a full workshop, on GitHub, for free! Looks like most of the recent injection methods are here.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/hahwul/authz0" target="_blank">authz0</a> is an automated authorization test tool. Unauthorized access can be identified based on URLs and Roles &amp; Credentials.</li>
<li><a href="https://github.com/bugch3ck/SharpLdapWhoami" target="_blank">SharpLdapWhoami</a> is a "WhoAmI" that functions by asking the LDAP service on a domain controller. I'm not 100% sure what this would be useful for without testing it.</li>
<li><a href="https://github.com/mrd0x/EvilSelenium" target="_blank">EvilSelenium</a> is a new project that weaponizes Selenium to abuse Chrome - steal cookies, dump creds, take screenshots, add SSH keys to GitHub, etc.</li>
<li><a href="https://github.com/magisterquis/shelloverreversessh" target="_blank">shelloverreversessh</a> is a simple implant which connects back to an OpenSSH server, requests a port be forwarded to it from the server, and serves up SOCKS4a or a shell to forwarded connections.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Psmths/reave" target="_blank">reave</a> is a post-exploitation framework tailored for hypervisor endpoints. Interesting concept, I'll be following it.</li>
<li><a href="https://github.com/idnahacks/GoodHound" target="_blank">GoodHound</a> uses Sharphound, Bloodhound and Neo4j to produce an actionable list of attack paths for targeted remediation.</li>
<li><a href="https://github.com/ShutdownRepo/ShadowCoerce" target="_blank">ShadowCoerce</a> is an  MS-FSRVP coercion abuse PoC. Not sure how I missed this one.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
