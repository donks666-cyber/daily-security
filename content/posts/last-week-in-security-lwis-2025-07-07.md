Title: Last Week in Security (LWiS) - 2025-07-07
Date: 2025-07-07 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-07-07
Author: Erik
Summary: Lenovo Applocker bypass (<a href="https://x.com/oddvarmoe" target="_blank">@Oddvarmoe</a>), Citrix Bleed 2 (<a href="https://x.com/SinSinology" target="_blank">@SinSinology</a>, <a href="https://x.com/inkmoro" target="_blank">@inkmoro</a>, Aliz Hammond), A+ adversary simulation (<a href="https://x.com/quarkslab" target="_blank">@quarkslab</a>), DreamWalkers loader (<a href="https://x.com/max2cbx" target="_blank">@max2cbx</a>), SigStrike (<a href="https://x.com/rushter" target="_blank">@rushter</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-06-30 to 2025-07-07.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">Celebrate Hacker Summer with Altered Security</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p>Start your Red Team training with Altered Security! We offer multiple Red Team courses with affordable and enterprise-like hands-on labs.</p>
<p>Each course comes with an industry-recognized certification. We are the creators of the popular Red Team certifications like Certified Red Team Professional (CRTP), CRTE, CARTP and more.</p>
<p>We are celebrating July 2025 as 'Hacker Summer'. Enjoy 20% OFF on all the courses (on-demand and learning path) using <strong>'HACKERSUMMER20OFF'</strong> from July 1 to July 31 2025. <strong><a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">Sign up now!</a></strong></p>
</aside><ul>
<li><a href="https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/" target="_blank">Content Independence Day: no AI crawl without compensation!</a> - Cloudflare is blocking AI crawlers by default on sites it hosts/protects. Is this giving power back to publishers, or a move to become the marketplace for content and thus make a handsome middleman fee? Perhaps both. Of note, I learned that <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/402" target="_blank">402 Payment Required</a> is a real HTTP status.</li>
<li><a href="https://blogs.windows.com/windows-insider/2025/07/03/announcing-windows-11-insider-preview-build-27891-canary-channel/" target="_blank">Announcing Windows 11 Insider Preview Build 27891 (Canary Channel)</a> - Powershell 2.0 is not long for this world on Windows 11. Update your powershell tooling if you still have any left over from 2015.</li>
<li><a href="https://spycloud.com/blog/state-secrets-for-sale-chinese-hacking/" target="_blank">State Secrets for Sale: More Leaks from the Chinese Hack-for-Hire Industry</a> - After the <a href="https://unit42.paloaltonetworks.com/i-soon-data-leaks/" target="_blank">i-Soon leaks</a> in 2024, there was no doubt about how Chinese tech companies were working for the state, but these leaks add even more evidence.</li>
<li><a href="https://oig.justice.gov/sites/default/files/reports/25-065_t.pdf" target="_blank">[PDF] Audit of the Federal Bureau of Investigation's Efforts to Mitigate the Effects of Ubiquitous Technical Surveillance</a> - Ubiquitous surveillance is an issue for law enforcement too. Page 2 (pdf page 7) details how a Cartel in Mexico used phone data and the city's cameras to kill informants.</li>
<li><a href="https://bugs.launchpad.net/ubuntu/+source/intel-compute-runtime/+bug/2110131" target="_blank">[SRU] NEO_DISABLE_MITIGATIONS flag default should be true</a> - In 2018 <a href="https://meltdownattack.com/" target="_blank">Meltdown and Spectre</a> were the first speculative execution vulnerabilities that led to many mitigations. Unfortunately those mitigations led to real performance impacts. Now, Ubuntu is rethinking the tradeoff.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.guidepointsecurity.com/blog/the-birth-and-death-of-loopyticket/" target="_blank">The Birth and Death of “LoopyTicket” – Our Story on CVE-2025-33073</a> - How curiosity leads to finding CVEs in plain sight. Also a bonus to see <a href="https://ludus.cloud/" target="_blank">Ludus</a> continue to help the security community.</li>
<li><a href="https://oblivion-malware.xyz/posts/kharon-agent/" target="_blank">Kharon Agent: Demonstration of Advanced Post-Exploitation</a> - Kharon is a fully Position-Independent Code (PIC) implant for Mythic with advanced evasion capabilities, dotnet/powershell/shellcode/bof memory executions, lateral movements, pivot and more.</li>
<li><a href="https://www.netspi.com/blog/technical-blog/cloud-pentesting/extracting-sensitive-information-azure-load-testing/" target="_blank">Extracting Sensitive Information from Azure Load Testing</a> - Code execution and sensitive information extraction by injecting malicious code into JMeter JMX files or Python Locust files.</li>
<li><a href="https://trustedsec.com/blog/abusing-chrome-remote-desktop-on-red-team-operations-a-practical-guide" target="_blank">Abusing Chrome Remote Desktop on Red Team Operations: A Practical Guide</a> - Someone push a PR to <a href="https://lolrmm.io/" target="_blank">LOLRMM</a>! Surprised is not in here already. We brought this one up in <a href="https://youtu.be/9qM2m1LZuVo?si=_M4lr9jpMZBy1pJC&amp;t=581" target="_blank">2022</a>.</li>
<li><a href="https://www.elastic.co/security-labs/taking-shellter" target="_blank">Taking SHELLTER: a commercial evasion framework abused in- the- wild</a> - A leaked SHELLTER payload ends up in the hands of Elastic, they do a full work up on it and now <a href="https://www.shellterproject.com/statement-regarding-recent-misuse-of-shellter-elite-and-elastic-security-labs-handling/" target="_blank">Shellter has released a statement on how they feel about it</a>. Safe to say the upcoming Shellter release will have extra love for Elastic EDR?</li>
<li><a href="https://labs.watchtowr.com/how-much-more-must-we-bleed-citrix-netscaler-memory-disclosure-citrixbleed-2-cve-2025-5777/" target="_blank">How Much More Must We Bleed? - Citrix NetScaler Memory Disclosure (CitrixBleed 2 CVE-2025-5777)</a> - A simple unauthenticated GET request leaks memory from an enterprise security gateway.</li>
<li><a href="https://msrc.microsoft.com/blog/2025/06/redirectionguard-mitigating-unsafe-junction-traversal-in-windows/" target="_blank">RedirectionGuard: Mitigating unsafe junction traversal in Windows</a> - Going after entire vulnerability classes is the most effective way to secure Windows. This requires developers to opt in however, so adoption will likely be slow outside of first party Microsoft code.</li>
<li><a href="https://oddvar.moe/2025/07/03/applocker-bypass-on-lenovo-machines-the-curious-case-of-mfgstat-zip/" target="_blank">Applocker Bypass on Lenovo Machines – the Curious Case of MFGSTAT.zip</a> - Vendors are known to add "bloatware" to operating systems, but this zip file in the windows system directory that is writeable by all users is a strange one.</li>
<li><a href="https://blog.quarkslab.com/a-story-about-confluence-and-tokens.html" target="_blank">When too much access is not enough: a story about Confluence and tokens</a> - This is a great post showcasing the thought process of adversary simulation. The author surveys the access they have along with constraints of the environment, sets up a representative test network (using <a href="https://ludus.cloud/" target="_blank">Ludus</a> perhaps?), then explores different avenues with pros and cons, creating and testing tooling before actioning the target.</li>
<li><a href="https://ricardojoserf.github.io/memorysnitcher/" target="_blank">MemorySnitcher and the power of NtReadVirtualMemory</a> - Intentionally leak function addresses to use them later. "So… is this useful? I am not sure, but it was fun to write about it :)" See <a href="https://github.com/ricardojoserf/MemorySnitcher" target="_blank">MemorySnitcher</a> for the code.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/TheManticoreProject/LDAPWordlistHarvester" target="_blank">LDAPWordlistHarvester</a> - A tool that allows you to extract a client-specific wordlist from the LDAP of an Active Directory.</li>
<li><a href="https://github.com/cybersectroll/TrollBlacklistDLL" target="_blank">TrollBlacklistDLL</a> - Reads blacklist.txt and blocks dlls from loading with option to unblock subsequently. Patches LdrLoadDll in local/remote process to return dll not found.</li>
<li><a href="https://github.com/rushter/SigStrike" target="_blank">SigStrike</a> - Cobalt Strike beacon parser and crawler.</li>
<li><a href="https://github.com/mongodb/kingfisher" target="_blank">kingfisher</a> - Kingfisher is a blazingly fast secret‑scanning and validation tool built in Rust.</li>
<li><a href="https://github.com/trufflesecurity/force-push-scanner" target="_blank">force-push-scanner</a> - Scan for secrets in dangling commits on GitHub using GH Archive data.</li>
<li><a href="https://github.com/maxDcb/DreamWalkers" target="_blank">DreamWalkers</a> - Reflective shellcode loader with advanced call stack spoofing and .NET support.</li>
<li><a href="https://github.com/MazX0p/PhantomInjector" target="_blank">PhantomInjector</a> - Advanced In-Memory PowerShell Process Injection Framework.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Yeeb1/SockTail" target="_blank">SockTail</a> - Lightweight binary that joins a device to a Tailscale network and exposes a local SOCKS5 proxy. Designed for red team operations and ephemeral access into restricted environments using Tailscale’s embedded client (tsnet). Zero config, no daemon, no persistence - just a fast way in.</li>
<li><a href="https://github.com/humanascode/terraform-azapi-nsgator" target="_blank">terraform-azapi-nsgator</a> - Terraform module for intelligent Azure Network Security Group (NSG) rule management.</li>
<li><a href="https://modzero.com/en/blog/when-backups-open-backdoors-synology-active-backup-m365/" target="_blank">When Backups Open Backdoors: Accessing Sensitive Cloud Data via "Synology Active Backup for Microsoft 365"</a> - If you're on Reddit, you might have noticed some users reporting that they Synology NAS was popped. Read more about <a href="https://modzero.com/en/blog/when-backups-open-backdoors-synology-active-backup-m365/" target="_blank">CVE-2025-4679.</a> here.</li>
<li><a href="https://github.com/MHaggis/ASRGEN" target="_blank">ASRGEN</a> - ASR Configurator, Essentials and Atomic Testing.</li>
<li><a href="https://github.com/LowOrbitSecurity/gubble" target="_blank">gubble</a> - gubble is a tool designed to audit Google Workspace group settings. It analyzes settings such as who can join, view membership, post messages, view conversations, and more to help identify potential security risks associated with group configurations.</li>
<li><a href="https://github.com/NikhilPanwar/secrets-ninja" target="_blank">secrets-ninja</a> - Secrets Ninja is an GUI tool for validating &amp; investigating API keys discovered during pentesting &amp; bug bounty hunting.</li>
<li><a href="https://github.com/RWXstoned/LdrShuffle" target="_blank">LdrShuffle</a> - Code execution/injection technique using DLL PEB module structure manipulation.</li>
<li><a href="https://github.com/Macmod/godap" target="_blank">godap</a> - A complete terminal user interface (TUI) for LDAP.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 455 (+1)</p>
<p>Blogs monitored: 423 (+0)</p>
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
