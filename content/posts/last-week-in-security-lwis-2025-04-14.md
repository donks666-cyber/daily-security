Title: Last Week in Security (LWiS) - 2025-04-14
Date: 2025-04-14 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-04-14
Author: Erik
Summary: WinRMS relay (<a href="https://x.com/Defte_" target="_blank">@Defte_</a>), plaintext Zip attacks (<a href="https://x.com/PfiatDe" target="_blank">@pfiatde</a>), SQL Server Crypto deep dive (<a href="https://x.com/_xpn_" target="_blank">@_xpn_</a>), FindUnusualSessions (<a href="https://x.com/podalirius_" target="_blank">@podalirius_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-04-07 to 2025-04-14.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/ssl-tls-certificate-lifespans-reduced-to-47-days-by-2029/" target="_blank">SSL/TLS certificate lifespans reduced to 47 days by 2029</a> - The CA/Browser Forum agreed unanimously to reduce certificate lifespans aggressively. Currently Domain Control Validation (DCV) certificates lifespan is 398 days.</li>
<li><a href="https://www.servethehome.com/broadcom-vmware-esxi-8-0u3e-now-has-a-free-version/" target="_blank">VMware ESXi 8.0U3e Now Has a Free Version How to Get It</a> - ESXi used to have a free version, then <a href="https://investors.broadcom.com/news-releases/news-release-details/broadcom-completes-acquisition-vmware" target="_blank">Broadcom bought VMware</a> and well, <a href="https://www.reddit.com/r/vmware/search/?q=broadcom&amp;restrict_sr=on&amp;t=year" target="_blank">everything kind of fell apart</a>. Looks like a free ESXi is back (no API or cluster support). For a better and more automated experience, try the free and open source <a href="https://ludus.cloud/" target="_blank">Ludus</a> built on KVM/QEMU/Proxmox.</li>
<li><a href="https://krebsonsecurity.com/2025/04/china-based-sms-phishing-triad-pivots-to-banks/" target="_blank">China-based SMS Phishing Triad Pivots to Banks</a> - Phishing crews are using mobile OS's built in wallet features to convince victims to send them bank verification codes to add their cards to the scammer's mobile wallet, where they can then spend money from the cards until they are shut down.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.whiteflag.io/blog/is-tls-more-secured-the-winrms-case/" target="_blank">Is TLS more secure, the WinRMS case.</a> - "WinRM is protected against NTLMRrelay as communications are encrypted. However WinRMS (the one communicating over HTTPS) is not." 🤯</li>
<li><a href="https://www.horizon3.ai/attack-research/disclosures/unsafe-at-any-speed-abusing-python-exec-for-unauth-rce-in-langflow-ai/" target="_blank">Unsafe at Any Speed: Abusing Python Exec for Unauth RCE in Langflow AI</a> - I wonder if this unauthenticated endpoint was "vibe coded" by AI?</li>
<li><a href="https://embracethered.com/blog/posts/2025/github-custom-copilot-instructions/" target="_blank">GitHub Copilot Custom Instructions and Risks</a> - More AI risks, the old trick of unicode zero width characters is back to instruct AI to add backdoors or "telemetry" to projects silently. More at <a href="https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents" target="_blank">Pillar Security</a>.</li>
<li><a href="https://badoption.eu/blog/2025/04/07/zipcrack.html" target="_blank">Practical Known Plaintext Attack Against ZIP Files</a> - After nearly a year, PfiatDe is back! The fact that zip file names and sizes are by default not encrypted is what allows this to work.</li>
<li><a href="https://posts.specterops.io/the-sql-server-crypto-detour-5ff9ac7033de" target="_blank">The SQL Server Crypto Detour</a> - A great journey into the depths of MSSQL encryption. Remember: "Always lab your target product before spending so much time in a disassembler." We couldn't <a href="https://ludus.cloud/" target="_blank">agree more</a>.</li>
<li><a href="https://unsigned-sh0rt.net/posts/pdq_credentials/" target="_blank">Decrypting PDQ credentials</a> - More encryption/decryption fun from the Specter Ops crew with a <a href="https://gist.github.com/garrettfoster13/ed0c6edf77e96430ea6a0c361b8f8b6c" target="_blank">tool</a> release and <a href="https://github.com/dru1d-foofus/pdq-bof" target="_blank">bof</a>.</li>
<li><a href="https://trustedsec.com/blog/kubernetes-for-pentesters-part-1" target="_blank">Kubernetes for Pentesters: Part 1</a> - A basic first introduction to Kubernetes (k8s).</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/tdeerenberg/InlineWhispers3" target="_blank">InlineWhispers3</a> - Tool for working with Indirect System Calls in Cobalt Strike's Beacon Object Files (BOF) using SysWhispers3 for EDR evasion.</li>
<li><a href="https://github.com/m417z/thread-call-stack-scanner" target="_blank">thread-call-stack-scanner</a> - Safely manage the unloading of DLLs that have been hooked into a process. <a href="https://github.com/KNSoft/KNSoft.SlimDetours/discussions/15" target="_blank">Context</a>.</li>
<li><a href="https://github.com/MatheuZSecurity/ElfDoor-gcc" target="_blank">ElfDoor-gcc</a> is an LD_PRELOAD that hijacks gcc to inject malicious code into binaries during linking, without touching the source code.</li>
<li><a href="https://github.com/zimnyaa/go-internalmonologue" target="_blank">go-internalmonologue</a> - Get NetNTLMv2 in Go.</li>
<li><a href="https://github.com/p0dalirius/FindUnusualSessions" target="_blank">FindUnusualSessions</a> - A tool to remotely detect unusual sessions opened on windows machines using RPC.</li>
<li><a href="https://github.com/3lp4tr0n/RemoteMonologue" target="_blank">RemoteMonologue</a> - Weaponizing DCOM for NTLM Authentication Coercions. See: <a href="https://www.ibm.com/think/x-force/remotemonologue-weaponizing-dcom-ntlm-authentication-coercions" target="_blank">RemoteMonologue: Weaponizing DCOM for NTLM authentication coercions</a>.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/joaoviictorti/shadow-rs" target="_blank">shadow-rs</a> - Windows Kernel Rootkit in Rust.</li>
<li><a href="https://github.com/bot984397/eepy" target="_blank">eepy</a> - sleep obfuscation via rop.</li>
<li><a href="https://github.com/ahkeur/WriteProcessMemoryAPC" target="_blank">WriteProcessMemoryAPC</a> - Nim reimplementation of WriteProcessMemoryAPC.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 447 (+1)</p>
<p>Blogs monitored: 408 (+1)</p>
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
