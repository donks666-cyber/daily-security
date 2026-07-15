Title: Last Week in Security (LWiS) - 2026-01-05
Date: 2026-01-05 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2026-01-05
Author: Erik
Summary: Windows ARM64 internals (<a href="https://x.com/33y0re" target="_blank">@33y0re</a>), VEH^2 PoC (<a href="https://x.com/0xfluxsec" target="_blank">@0xfluxsec</a>), macOS 26 TCC bypass (<a href="https://x.com/patch1t" target="_blank">@patch1t</a>), BOFs with Crystal Palace (<a href="https://x.com/_RastaMouse" target="_blank">@_RastaMouse</a>), Flare-On 2025 write-ups (<a href="https://x.com/washi_dev" target="_blank">@washi_dev</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-12-15 to 2026-01-05.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/north-korean-infiltrator-caught-working-in-amazon-it-department-thanks-to-lag-110ms-keystroke-input-raises-red-flags-over-true-location" target="_blank">North Korean infiltrator caught working in Amazon IT department thanks to lag — 110ms keystroke input raises red flags over true location</a> - 110ms is really not all that much. <a href="https://aresluna.org/keyboard-secrets/typing-delay/" target="_blank">Try it yourself</a>. Maybe the "more than" in "more than 110ms" is doing heavy lifting to not give away the threshold? 800ms+ is where something like <a href="https://mosh.org/" target="_blank">Mosh</a> really helps.</li>
<li><a href="https://www.youtube.com/watch?v=vU1-uiUlHTo" target="_blank">This Flock Camera Leak is like Netflix For Stalkers</a> - The easy pivot from camera to personal details shows the power of mass surveillance, and this was a private citizen. Using an exposed Flock camera to stream Flock's response was a nice touch.</li>
<li><a href="https://www.politico.com/news/2026/01/03/trump-venezuela-cyber-operation-maduro-00709816" target="_blank">Trump suggests US used cyberattacks to turn off lights in Venezuela during strikes</a> - Cyber is a domain of warfare and it's being used to support actions in the physical world. While <a href="https://en.wikipedia.org/wiki/Stuxnet" target="_blank">Stuxnet</a> may have been the first cyber-physical attack to get media attention, expect every modern military operation to have a cyber component going forward.</li>
<li><a href="https://ca.news.yahoo.com/man-boards-heathrow-flight-without-081243825.html" target="_blank">Man boards Heathrow flight without ticket, boarding pass or passport in major security breach</a> - Get this man a job as a physical penetration tester!</li>
<li><a href="https://www.wiz.io/blog/mongobleed-cve-2025-14847-exploited-in-the-wild-mongodb" target="_blank">MongoBleed (CVE-2025-14847) exploited in the wild: everything you need to know</a> - An information leak in nearly every version of MongoDB reminiscent of <a href="https://en.wikipedia.org/wiki/Heartbleed" target="_blank">Heartbleed</a> could leak sensitive information including credentials. The decision to drop a proof of concept on <a href="https://github.com/joe-desimone/mongobleed/commits/main/" target="_blank">Christmas Day</a>  has been met with backlash.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://arxiv.org/pdf/2510.09272" target="_blank">[PDF] Modern iOS Security Features – A Deep Dive into SPTM, TXM, and Exclaves</a> - 174 pages of detailed technical analysis of iOS security.</li>
<li><a href="https://kibty.town/blog/mintlify/" target="_blank">how to hack discord, vercel and more with one easy trick</a> - The B2B SaaS documentation platform (with AI of course) led to cross site scripting across many major platforms.</li>
<li><a href="https://www.archcloudlabs.com/projects/kernel_of_doom/" target="_blank">Kernel of Doom - A Tiny Linux Kernel to Boot into Doom</a> - An awesome little experiment that will certainly help get DOOM running on even more devices.</li>
<li><a href="https://www.evilsocket.net/2025/12/18/TP-Link-Tapo-C200-Hardcoded-Keys-Buffer-Overflows-and-Privacy-in-the-Era-of-AI-Assisted-Reverse-Engineering/" target="_blank">TP-Link Tapo C200: Hardcoded Keys, Buffer Overflows and Privacy in the Era of AI Assisted Reverse Engineering</a> - Using AI and <a href="https://github.com/LaurieWired/GhidraMCP" target="_blank">GhidraMCP</a> three vulnerabilities were found in a TP Link camera.</li>
<li><a href="https://sud0ru.ghost.io/yet-another-dcom-object-for-command-execution-part-2/" target="_blank">Yet Another DCOM Object for Command Execution Part 2</a> - CPLs were a go to for phishing payloads a while ago as the user could double click them and they would execute and email filters didn't realize they were executable. Now you can use them for lateral movement!</li>
<li><a href="https://www.elttam.com/blog/leaking-more-than-you-joined-for/" target="_blank">ORM Leaking More Than You Joined For</a> - With SQL injections becoming more rare, object-relational mapping (ORM) middleware allowing users to search and filter sensitive data can inadvertently leak that data.</li>
<li><a href="https://connormcgarr.github.io/windows-arm64-interrupts/" target="_blank">Windows ARM64 Internals: Pardon The Interruption! Interrupts on Windows for ARM</a> - Start your new year with some deep technical Windows ARM64 internals.</li>
<li><a href="https://fluxsec.red/vectored-exception-handling-squared-rust" target="_blank">Vectored Exception Handling Squared</a> - A writeup and proof of concept for some research from last June by Crowdstrike on how to modfiy the CONTEXT struct in Windows to set hardware breakpoints without calling SetThreadContext and thus avoiding event tracing for Windows (ETW) logging.</li>
<li><a href="https://jhftss.github.io/CVE-2025-43530/" target="_blank">CVE-2025-43530: Exploiting a private API for VoiceOver</a> - A macOS Transparency, Consent, and Control (TCC) bypass that injects a library into an Apple signed binary (in this case SSH) to bypass security checks and run arbitrary AppleScript that uses Finder for actions. This completely bypasses TCC.</li>
<li><a href="https://rastamouse.me/bof-cocktails/" target="_blank">BOF Cocktails</a> - Using Crystal Palace, Rasta Mouse shows how to implement hooks into existing BOFs with some Aggressor script kung-fu.</li>
<li><a href="https://washi1337.github.io/ctf-writeups/writeups/flare-on/2025/" target="_blank">Flare-On 2025</a> - Write ups for all the Flare-On 2025 challenges.</li>
<li><a href="https://whiteknightlabs.com/2026/01/06/the-new-chapter-of-egress-communication-with-cobalt-strike-user-defined-c2/" target="_blank">The New Chapter of Egress Communication with Cobalt Strike User-Defined C2</a> - No longer must you proxy your agent communication to a local process on the victim machine, with User-Defined C2 (UDC2) you can create a Beacon Object File (BOF) that integrates into the agent itself.</li>
<li><a href="https://blog.zsec.uk/capd/" target="_blank">Making CloudFlare Workers Work for Red Teams</a> - Conditional Access Payload Delivery (CAPD) is a great term for this category. Cloudflare excells at bot protection and fine grained access policy, so why not use it for payload delivery protection?</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul><li><a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">PhantomSec | Advanced Offensive Capabilities Automated - EvadeX</a> <span class="m-label m-flat m-success">Sponsored</span> - EvadeX is an evasion-as-a-service platform for red teams and pentesters who want modern, continuously-updated evasive tradecraft without turning every engagement into an R&amp;D project. Generate highly customizable, low-signature payloads through a simple web workflow so you can tune to the target and stay focused on the engagement. Trusted by teams from small consultancies to the Fortune 10. <a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">Get callbacks past EDR today!</a></li></ul><ul>
<li><a href="https://github.com/almounah/silph" target="_blank">silph</a> - Stealthy In-Memory Local Password Harvester (SILPH) tool: dump LSA, SAM and DCC2 with indirect syscall.</li>
<li><a href="https://github.com/5tuk0v/ludus_ghostwriter" target="_blank">ludus_ghostwriter</a> - An Ansible Role that installs Ghostwriter on a Linux-based host using ghostwriter-cli and Docker Compose.</li>
<li><a href="https://github.com/professor-moody/ludus_scorch" target="_blank">ludus_scorch</a> - An Ansible collection that installs System Center Orchestrator (SCORCH) deployments with optional configurations for security testing.</li>
<li><a href="https://github.com/professor-moody/scorch" target="_blank">scorch</a> - Offensive security toolkit for Microsoft System Center Orchestrator (SCORCH). Single binary, cross-platform, works from non-domain joined systems.</li>
<li><a href="https://github.com/CyberSecurityUP/NeuroSploit" target="_blank">NeuroSploit</a> - NeuroSploitv2 is an advanced, AI-powered penetration testing framework designed to automate and augment various aspects of offensive security operations. Leveraging the capabilities of large language models (LLMs). [Untested, appears vibe coded]</li>
<li><a href="https://github.com/zero2504/EDR-GhostLocker" target="_blank">EDR-GhostLocker</a> - AppLocker-Based EDR Neutralization.</li>
<li><a href="https://github.com/mellow-hype/mt7622-qemu-vm" target="_blank">mt7622-qemu-vm</a> - QEMU emulation of MediaTek MT7622 PCI driver.</li>
<li><a href="https://www.cve.org/CVERecord?id=CVE-2025-14728" target="_blank">Rapid7 Velociraptor Directory Traversal Vulnerability</a> - We discussed using Velociraptor as a red team tool in our <a href="https://github.com/badsectorlabs/iscariot-suite" target="_blank">iscariot-suite</a>, but this exploit potentially allows the takeover of the Velociraptor server, which would then allow an attacker to use Velociraptor as a command and control service across your network.</li>
<li><a href="https://github.com/rasta-mouse/crystal-palace-vsc" target="_blank">crystal-palace-vsc</a> - Language extension for Crystal Palace Specification files. On the VSCode Marketplace here: <a href="https://marketplace.visualstudio.com/items?itemName=rastamouse.crystal-palace" target="_blank">crystal-palace-vsc</a></li>
<li><a href="https://github.com/pard0p/Remote-BOF-Runner" target="_blank">Remote-BOF-Runner</a> - Remote BOF Runner is a Havoc extension framework for remote execution of Beacon Object Files (BOFs) using a PIC loader made with Crystal Palace.</li>
<li><a href="https://github.com/BishopFox/sliver/releases/tag/v1.6.0" target="_blank">Sliver v1.6.0</a> - The best Go C2 framework gets an update. The new memfd features and the total CLI rewrite look interesting.</li>
<li><a href="https://github.com/0xflux/Vectored-Exception-Handling-Squared" target="_blank">Vectored-Exception-Handling-Squared</a> - Vectored Exception Handling Squared.</li>
<li><a href="https://github.com/mhaskar/FsquirtCPLPoC" target="_blank">FsquirtCPLPoC</a> - PoC for generating bthprops.cpl module designed to be loaded by Fsquirt.exe LOLBin.</li>
<li><a href="https://github.com/WKL-Sec/slack-udc2" target="_blank">slack-udc2</a> - Cobalt Strike UDC2 implementation that provides an Slack C2 channel.</li>
<li><a href="https://github.com/joe-desimone/mongobleed" target="_blank">mongobleed</a> - A proof-of-concept exploit for the MongoDB zlib decompression vulnerability that allows unauthenticated attackers to leak sensitive server memory.</li>
<li><a href="https://github.com/Print3M/Google-Hack-Search" target="_blank">Google-Hack-Search</a> - Custom Google search engine dedicated to IT security &amp; hacking stuff. Over 230 high-quality sources.</li>
<li><a href="https://github.com/Adversis/tailsnitch" target="_blank">tailsnitch</a> - A security auditor for Tailscale configurations. Scans your tailnet for misconfigurations, overly permissive access controls, and security best practice violations.</li>
<li><a href="https://github.com/lsecqt/SessionView" target="_blank">SessionView</a> - A portable C# utility for enumerating local and remote windows sessions.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.jack.bio/blog/licenseplate" target="_blank">Using TypeScript to Obtain One of the Rarest License Plates</a> - Burp suite and the lack of rate limits combine for this niche "hack" (<a href="https://en.wikipedia.org/wiki/Hacker" target="_blank">original definition</a>).</li>
<li><a href="https://github.com/cjpais/Handy" target="_blank">Handy</a> - A free, open source, and extensible speech-to-text application that works completely offline.</li>
<li><a href="https://github.com/BlessedRebuS/Krawl" target="_blank">Krawl</a> - Krawl is a lightweight cloud native deception server and anti-crawler that creates fake web applications with low-hanging vulnerabilities and realistic, randomly generated decoy data.</li>
<li><a href="https://www.youtube.com/watch?v=xYfiOnufBSk" target="_blank">How Passkeys Work - Computerphile</a> - A decent high level overview of passkeys you can send to your parents.</li>
<li><a href="https://simondotsh.com/infosec/2026/01/04/what-i-seek-pentester.html" target="_blank">What I Seek Out of a Pentester</a> - Good overview on how to set your self up for success when looking for jobs in offensive security. The base of knowledge is really important in order to make connections quickly.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 493 (+0)</p>
<p>Blogs monitored: 439 (+1)</p>
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
