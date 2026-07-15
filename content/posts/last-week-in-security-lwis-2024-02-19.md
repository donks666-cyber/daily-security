Title: Last Week in Security (LWiS) - 2024-02-19
Date: 2024-02-19 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-02-19
Author: Erik
Summary: ESC13 (<a href="https://twitter.com/Jonas_B_K" target="_blank">@Jonas_B_K</a>), Sandboxing syscalls (<a href="https://twitter.com/h0mbre_" target="_blank">@h0mbre_</a>), Cross Window Forgery (<a href="https://twitter.com/PaulosYibelo" target="_blank">@PaulosYibelo</a>), new Windows callback method (<a href="https://twitter.com/daaximus" target="_blank">@daaximus</a>), dangerous EntraID role (<a href="https://twitter.com/_wald0?lang=en" target="_blank">@_wald0</a>), github-secrets (Tobias Madl of <a href="https://twitter.com/Neodyme" target="_blank">@Neodyme</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-02-12 to 2024-02-19.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://freenginx.org/en/" target="_blank">Free Nginx</a> - It seems the maintainer of nginx is forking. Limited details at <a href="https://freenginx.org/pipermail/nginx/2024-February/000000.html" target="_blank">announcing freenginx.org</a> - This seems to have stemmed over F5/Nginx issuing CVEs for experiemental QUIC code and Maxim not liking that. <a href="https://my.f5.com/manage/s/article/K000138444" target="_blank">Here is the advisory</a>, you be the judge.</li>
<li><a href="https://www.aquasec.com/blog/snap-trap-the-hidden-dangers-within-ubuntus-package-suggestion-system/" target="_blank">Snap Trap: The Hidden Dangers Within Ubuntu's Package Suggestion System</a>  - "We've examined the command-not-found package that is installed by default in Ubuntu, which suggests packages to install for unrecognized commands. Our findings reveal that besides searching for apt packages, it also queries the Snap Store for snap packages. Given that any user can upload to the Snap Store, an attacker could potentially manipulate the command-not-found package to recommend their own malicious package. This blog discusses the suggestion mechanism, how an attacker might exploit it, the risks associated with installing a malicious snap package, and our discovery that an attacker could impersonate 26% of the commands from apt packages."</li>
<li><a href="https://twitter.com/AzakaSekai_/status/1759326049262019025" target="_blank">[UNVERIFIED] someone just leaked a bunch of internal Chinese government documents on GitHub</a> - This could be spicy. No code, but lots of docs.</li>
<li><a href="https://arstechnica.com/tech-policy/2024/02/human-rights-court-takes-stand-against-weakening-of-end-to-end-encryption/" target="_blank">Backdoors that let cops decrypt messages violate human rights, EU court says</a> - The "confidentiality of communications is an essential element of the right to respect for private life and correspondence," and requiring messages to be decrypted by law enforcement "cannot be regarded as necessary in a democratic society."</li>
<li><a href="https://cvecrowd.com/" target="_blank">CVE Crowd</a> - Picks up where cvetrends left off (killed by twitter API limits). CVE trends uses the "fediverse" (mastodon) for its data.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://malwaretech.com/2024/02/bypassing-edrs-with-edr-preload.html" target="_blank">Bypassing EDRs With EDR-Preloading</a> - A nice technique to block EDR DLL loading. No good if your EDR is using a kernel driver however... Code <a href="https://github.com/MalwareTech/EDR-Preloader" target="_blank">here</a>.</li>
<li><a href="https://posts.specterops.io/adcs-esc13-abuse-technique-fda4272fbd53" target="_blank">ADCS ESC13 Abuse Technique</a> - ADCS is now up to 13 different attack paths!</li>
</ul>
<aside class="m-note m-success">
<h3>Easy ESC13 Setup in Ludus</h3>
<p>Want to test out ESC13 easily? Using <a href="https://ludus.cloud" target="_blank">ludus.cloud</a> it's as easy as adding our <a href="https://github.com/bad-sector-labs/ludus_adcs" target="_blank">ansible role</a> to the server, assigning it to a VM, and deploying it! Full guide <a href="https://docs.ludus.cloud/docs/Environment%20Guides/adcs" target="_blank">here</a>.</p>
</aside>
<ul>
<li><a href="https://www.legitsecurity.com/blog/azure-devops-zero-click-ci/cd-vulnerability" target="_blank">Azure Devops Zero-Click CI/CD Vulnerability</a> - Pipeline triggers confused Azure to think that the pipeline was run from the project and not a fork, allowing access to secrets.</li>
<li><a href="https://h0mbre.github.io/Lucid_Context_Switching/#" target="_blank">Fuzzer Development: Sandboxing Syscalls</a> - The fuzzer/emulator being built in this blog is interesting and its fun to watch its progress. This installment is all about sandboxing the Bochs emulator to prevent it from accessing anything outside of its environment.</li>
<li><a href="https://modexp.wordpress.com/2024/02/13/delegated-nt-dll/" target="_blank">Delegated NT DLL</a> - "Like the WOW64 table, the NT delegate table provides a simple way to intercept a variety of callbacks in 32-bit mode without the need to overwrite code with inline hooking." Code <a href="https://gist.github.com/odzhan/d677d9d5b6b31d8cabf9277bc14a3856" target="_blank">here</a>.</li>
<li><a href="https://www.paulosyibelo.com/2024/02/cross-window-forgery-web-attack-vector.html" target="_blank">Cross Window Forgery: A Web Attack Vector</a> - I'd say this isn't a vulnerability but certianly a neat hack. Convincing a user to agree to a SSO prompt without them realizing it is classic social engineering. This paired with a phish could be an interesting intial access method to online services.</li>
<li><a href="https://revers.engineering/beyond-process-and-object-callbacks-an-unconventional-method/" target="_blank">Beyond Process And Object Callbacks: An Unconventional Method</a>. A technical post on a previously undocumented method for creating callbacks without registering with the object manager in Windows.</li>
<li><a href="https://posts.specterops.io/the-most-dangerous-entra-role-youve-probably-never-heard-of-e00ea08b8661" target="_blank">The Most Dangerous Entra Role You've (Probably) Never Heard Of</a> - TLDR: "Entra ID has a built-in role called “Partner Tier2 Support” that enables escalation to Global Admin, but this role is hidden from view in the Azure portal GUI." I'm not a hacker, I'm an "unathorized remote partner tier2 support engineer."</li>
<li><a href="https://www.trendmicro.com/en_us/research/24/b/cve-2024-21412-facts-and-fixes.html" target="_blank">SmartScreen Vulnerability: CVE-2024-21412 Facts and Fixes</a> - The post text is light on details, but it looks like an ms-application handler and then an SMB hosted LNK. See <a href="https://youtube.com/watch?v=xR0dbM9oe70&amp;t=80" target="_blank">this YouTube Video</a>.</li>
<li><a href="https://blog.projectdiscovery.io/hello-lucee-let-us-hack-apple-again/" target="_blank">Hello Lucee! Let us hack Apple again?</a> - The PD team find some critical vulnerabilities within Lucee, a CFML server, with RCE capabilities. Decent payout $$$.</li>
<li><a href="https://aceresponder.com/blog/exploiting-empire-c2-framework?1" target="_blank">Exploiting Empire C2 Framework</a> - <a href="https://github.com/ACE-Responder/Empire-C2-RCE-PoC" target="_blank">RCE</a>  in Empire C2 framework &lt;5.9.3!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-21410" target="_blank">Microsoft Exchange Server Elevation of Privilege Vulnerability</a> - "An attacker who successfully exploited this vulnerability could relay a user's leaked Net-NTLMv2 hash against a vulnerable Exchange Server and authenticate as the user." Sounds like fun.</li>
<li><a href="https://www.zoom.com/en/trust/security-bulletin/ZSB-24008/" target="_blank">Zoom Desktop Client for Windows, Zoom VDI Client for Windows, and Zoom Meeting SDK for Windows - Improper Input Validation</a> "Improper input validation in Zoom... may allow an unauthenticated user to conduct an escalation of privilege via network access." Via network access!?</li>
<li><a href="https://github.com/neodyme-labs/github-secrets" target="_blank">github-secrets</a> - This tool analyzes a given Github repository and searches for dangling or force-pushed commits containing potential secret or interesting information. Check out the blog post: <a href="https://neodyme.io/en/blog/github_secrets/" target="_blank">Hidden GitHub Commits and How to Reveal Them</a>.</li>
<li><a href="https://github.com/knqyf263/CVE-2023-50387" target="_blank">CVE-2023-50387</a> - KeyTrap (DNSSEC) [DoS]. See: <a href="https://www.athene-center.de/en/keytrap" target="_blank">KeyTrap: Serious Vulnerability in the Internet Infrastructure</a>.</li>
<li><a href="https://github.com/Sh3lldon/FullBypass" target="_blank">FullBypass</a> - A tool which bypasses AMSI (AntiMalware Scan Interface) and PowerShell CLM (Constrained Language Mode) and gives you a FullLanguage PowerShell reverse shell.</li>
<li><a href="https://github.com/senzee1984/InflativeLoading" target="_blank">InflativeLoading</a> - Dynamically convert a native EXE to PIC shellcode by appending a shellcode stub.</li>
<li><a href="https://github.com/xaitax/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability" target="_blank">CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability</a> - PoC for the NTLM leak from last week. <a href="https://github.com/duy-31/CVE-2024-21413" target="_blank">Another one</a>.</li>
<li><a href="https://github.com/icyguider/UAC-BOF-Bonanza" target="_blank">UAC-BOF-Bonanza</a> - Collection of UAC Bypass Techniques Weaponized as BOFs.</li>
<li><a href="https://github.com/rbmm/SDD" target="_blank">SDD1</a> <a href="https://github.com/rbmm/SDD2" target="_blank">and SSD2</a> - Self delete DLLs PoCs.</li>
<li><a href="https://medium.com/@mitrecaldera/announcing-mitre-caldera-v5-06798b928adf" target="_blank">Announcing MITRE Caldera™ v5!</a> - Cool update! Purple teamers will appreciate this.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/MatheuZSecurity/NullSection" target="_blank">NullSection</a> - NullSection is an Anti-Reversing tool that applies a technique that overwrites the section header with nullbytes.</li>
<li><a href="https://github.com/d0ge/sessionless" target="_blank">sessionless</a> - TokenSigner is a Burp Suite extension for editing, signing, verifying various signed web tokens.</li>
<li><a href="https://forgejo.org/2024-02-forking-forward/?ref=selfh.st" target="_blank">Forgejo forks its own path forward</a> - Forgejo was a soft-fork of Gitea, but is now a fully independent hard-fork.</li>
<li><a href="https://github.com/justakazh/sicat" target="_blank">sicat</a> - The useful exploit finder.</li>
<li><a href="https://raesene.github.io/blog/2024/02/17/a-final-kubernetes-censys/" target="_blank">A final Kubernetes census</a> - Cool data analysis of exposed kubernetes nodes has come to an end.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 368 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
