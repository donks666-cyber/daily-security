Title: Last Week in Security (LWiS) - 2025-11-03
Date: 2025-11-03 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-11-03
Author: Erik
Summary: ShareHound (<a href="https://x.com/podalirius_" target="_blank">@podalirius_</a>), Conquest C2 (<a href="https://x.com/virtualloc" target="_blank">@virtualloc</a>), Docker Compose path traversal (<a href="https://x.com/RonMasas" target="_blank">@RonMasas</a>), dead domain discovery (<a href="https://x.com/_lauritz_" target="_blank">@_lauritz_</a>), Narrator persistence/lat movement (<a href="https://x.com/Oddvarmoe" target="_blank">@Oddvarmoe</a> ), Windows 11 LPE (<a href="https://x.com/d4m0n_8" target="_blank">@d4m0n_8</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-10-27 to 2025-11-03.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.dotcom.press/history-of-domains" target="_blank">A Brief History of Domains</a> - <cite>.com</cite> is 40 years old!</li>
<li><a href="https://tailscale.com/blog/peer-relays-beta" target="_blank">Introducing Tailscale Peer Relays</a> - Tailscale brings self-hostable relay servers, and they're built into the tailscale client. All customers can use two peer relays, for free, forever.</li>
<li><a href="https://www.chinalawtranslate.com/en/online-presenter-code-of-conduct/#gsc.tab=0" target="_blank">Code of Conduct for Online Presenters</a> - China is requiring real names, identity verification, and adherence "to the correct political orientation," for "online presenters" (streamers). "For livestream content that requires a higher professional level (such as medical care, finance, law, education) presenters should obtain the corresponding practice qualifications and report them to the livestream platform."</li>
<li><a href="https://archive.is/20251030160126/https://www.404media.co/ice-and-cbp-agents-are-scanning-peoples-faces-on-the-street-to-verify-citizenship/#selection-529.0-536.1" target="_blank">ICE and CBP Agents Are Scanning Peoples’ Faces on the Street To Verify Citizenship</a> - Are you ready to bet your freedom on a "lowest price technically acceptable" facial recognition system? "An apparent biometric match by Mobile Fortify is a ‘definitive’ determination of a person’s status and that an ICE officer may ignore evidence of American citizenship—including a birth certificate—if the app says the person is an alien."</li>
<li><a href="https://www.linkedin.com/help/linkedin/answer/a8059228" target="_blank">Update to our Terms and data use</a> - LinkedIn has opted you in to using your data to train AI models. To opt out, go to Settings -&gt; Data Privacy -&gt; Data for Generative AI Improvement and turn it off.</li>
<li><a href="https://tee.fail/" target="_blank">TEE.fail: Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition</a> - The DDR5 DRAM bus can be used to break the security guarantees of modern "Trusted Execution Environments" (TEEs). The portable version of the attack fits in a briefcase and "even has a cup holder for your coffee." If your favorite <a href="https://scrt.network/" target="_blank">blockchain</a> depends on TEEs for security, you may want to consider something <a href="https://www.getmonero.org/library/Zero-to-Monero-2-0-0.pdf" target="_blank">[PDF] based on math</a>.</li>
<li><a href="https://security.googleblog.com/2025/10/https-by-default.html" target="_blank">HTTPS by default</a> - In a year Chrome will first try to use HTTPS for all requests by default and warn the user before trying HTTP. You can enable this now in Settings -&gt; Privacy and security -&gt; Always use secure connections. I'm old enough to remember <a href="https://codebutler.com/2010/10/24/firesheep/" target="_blank">Firesheep</a>.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.imperva.com/blog/cve-2025-62725-from-docker-compose-ps-to-system-compromise/" target="_blank">CVE-2025-62725: From “docker compose ps” to System Compromise</a> - Even "read only" commands like <cite>docker compose ps</cite> could lead to path traversal and therefore system compromise if the attacker targets a binary or SSH keys for overwriting.</li>
<li><a href="https://googleprojectzero.blogspot.com/2025/11/defeating-kaslr-by-doing-nothing-at-all.html" target="_blank">Defeating KASLR by Doing Nothing at All</a> - It's interesting to see one Google team (Project Zero) publicly beefing with another Google team (Pixel/Linux Kernel team) about a security feature.</li>
<li><a href="https://security.lauritz-holtmann.de/tools/dead-domain-discovery/#dead-domain-discovery-dns---dns-forwarder" target="_blank">Dead Domain Discovery: Discover Expired or Unregistered Domains</a> - Two tools to help discovery expired or unregistered domains as you browse target domains: <a href="https://github.com/lauritzh/dead-domain-discovery-dns" target="_blank">dead-domain-discovery-dns</a> and <a href="https://github.com/lauritzh/dead-domain-discovery" target="_blank">dead-domain-discovery</a>.</li>
<li><a href="https://www.synacktiv.com/en/publications/creating-a-two-face-rust-binary-on-linux" target="_blank">Creating a "Two-Face" Rust Binary on Linux</a> - This could also be considered advanced "environmental keying" for malware.</li>
<li><a href="https://code-white.com/blog/wsus-cve-2025-59287-analysis/" target="_blank">A Retrospective Analysis of CVE-2025-59287 in Microsoft WSUS</a> - The patch for the WSUS vulnerability last month actually contained a new vulnerability?!</li>
<li><a href="https://specterops.io/blog/2025/10/30/epic-pentest-fail/" target="_blank">Epic Pentest Fail</a> - Almost no one shares their failures, and that's a shame. Good on Forrest (and Specter Ops) for publishing this post.</li>
<li><a href="https://specterops.io/blog/2025/10/30/sharehound-an-opengraph-collector-for-network-shares/" target="_blank">ShareHound: An OpenGraph Collector for Network Shares</a> - Network shares, especially on larger and older networks, are often full of useful data for red teamers. ShareHound, along with <a href="https://github.com/p0dalirius/shareql" target="_blank">shareql</a> allows for precise targeting and enumeration of network shares, and then using OpenGraph, the exploration of them in BloodHound.</li>
<li><a href="https://rastamouse.me/arranging-the-pic-parterre/" target="_blank">Arranging the PIC Parterre</a> - A look at the recent updates to Crystal Palace from a third party perspective.</li>
<li><a href="https://specterops.io/blog/2025/10/31/adminsdholder-misconceptions-misconfigurations-and-myths/" target="_blank">AdminSDHolder: Misconceptions, Misconfigurations, and Myths</a> - Be sure to check out the <a href="https://specterops.io/wp-content/uploads/sites/3/2025/10/AdminSDHolder_-Misconceptions-Misconfigurations.pdf" target="_blank">[PDF] 150 page white paper</a> on AdminSDHolder.</li>
<li><a href="https://trustedsec.com/blog/hack-cessibility-when-dll-hijacks-meet-windows-helpers" target="_blank">Hack-cessibility: When DLL Hijacks Meet Windows Helpers</a> - Always fun when a technique can be both persistence and lateral movement. Also a good reminder that there are lots of techniques that are "published" but not "publicized."</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/EvilBytecode/Ebyte-Syscalls" target="_blank">Ebyte-Syscalls</a> - Obfuscating function calls using Vectored Exception Handlers by redirecting execution through exception-based control flow. Uses byte swapping without memory or assembly allocation.</li>
<li><a href="https://github.com/kfallahi/UnderlayCopy" target="_blank">UnderlayCopy</a> - PowerShell toolkit that extracts locked Windows files (SAM, SYSTEM, NTDS, ...) using MFT parsing and raw disk reads.</li>
<li><a href="https://github.com/rasta-mouse/LibGate" target="_blank">LibGate</a> - A Crystal Palace shared library to resolve &amp; perform syscalls.</li>
<li><a href="https://github.com/warpnet/COM-Fuzzer" target="_blank">COM-Fuzzer</a> - Gain insights into COM/DCOM implementations that may be vulnerable using an automated approach and make it easy to visualize the data. By following this approach, a security researcher will hopefully identify interesting (D)COM classes/implementations in such a time that would take a manual approach significantly more.</li>
<li><a href="https://github.com/synacktiv/twoface" target="_blank">twoface</a> - "Two-Face" Rust binary on Linux.</li>
<li><a href="https://github.com/TierZeroSecurity/teams-cookies-bof" target="_blank">teams-cookies-bof</a> - BOF to steal Teams cookies.</li>
<li><a href="https://github.com/pard0p/LibIPC" target="_blank">LibIPC</a> - LibIPC is a simple Crystal Palace shared library for inter-process communication, based on Named Pipes.</li>
<li><a href="https://tradecraftgarden.org/references.html" target="_blank">Community Pavilion</a> - A collection of projects that build on the Tradecraft Garden (position-independent development framework from Mudge).</li>
<li><a href="https://github.com/loosehose/SilentButDeadly" target="_blank">SilentButDeadly</a> is a network communication blocker specifically designed to neutralize EDR/AV software by preventing their cloud connectivity using Windows Filtering Platform (WFP). This version focuses solely on network isolation without process termination.</li>
<li><a href="https://github.com/D4m0n/CVE-2025-50168-pwn2own-berlin-2025" target="_blank">CVE-2025-50168-pwn2own-berlin-2025</a> - Pwn2Own Berlin 2025 - LPE (Windows 11) winning bug.</li>
<li><a href="https://github.com/NtDallas/BOF_Spawn/" target="_blank">BOF_Spawn</a> - Cobalt Strike BOF for beacon/shellcode injection using fork &amp; run technique with Draugr synthetic stack frames.</li>
<li><a href="https://github.com/jakobfriedl/conquest" target="_blank">conquest</a> - Conquest is a feature-rich and malleable command &amp; control/post-exploitation framework developed in Nim.</li>
<li><a href="https://github.com/7hePr0fess0r/ADCSDevilCOM" target="_blank">ADCSDevilCOM</a> - A C# tool for requesting certificates from ADCS using DCOM over SMB. This tool allows you to remotely request X.509 certificates from CA server using the MS-WCCE protocol over DCOM and It bypasses the traditional endpoint mapper requirement by using SMB directly.</li>
<li><a href="https://github.com/Skeletal-Group/Hermes" target="_blank">Hermes</a> - Fast covert timing channel communication for inter-process and inter-processor communication on Windows systems</li>
<li><a href="https://github.com/mwnickerson/COMHijackBOF" target="_blank">COMHijackBOF</a> - Automates COM hijacking of msedgewebview2.exe for persistence and code execution.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Sam0rai/guilty-as-yara" target="_blank">guilty-as-yara</a> - A Rust-based tool that generates Windows PE executables containing data patterns designed to trigger YARA rule matches. This is invaluable for validating YARA rules and ensuring your malware detection signatures work as expected.</li>
<li><a href="https://www.youtube.com/watch?v=fa8-mB79gaI" target="_blank">Easy Cyber Ranges with Ludus</a> - If you've struggled with building complex cyber ranges to practice your red team or pentest skills, Ludus will make scaffolding your lab much easier on a variety of platforms including Microsoft Azure, Google GCP, Proxmox and mini-pcs. Create ranges such as Game of Active Directory (GOAD) easily.</li>
<li><a href="https://github.com/Techlm77/LinuxPlay" target="_blank">LinuxPlay</a> - An open-source, ultra-low-latency remote desktop for Linux hosts and Windows clients.</li>
<li><a href="https://github.com/drwscefn/AxHound" target="_blank">AxHound</a> - Grab yer ldapsearch logs from AdaptixC2 a little easier.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 465 (+0)</p>
<p>Blogs monitored: 434 (+3)</p>
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
