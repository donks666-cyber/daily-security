Title: Last Week in Security (LWiS) - 2025-04-21
Date: 2025-04-21 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-04-21
Author: Erik
Summary: CVE drama (<a href="https://x.com/mitrecorp" target="_blank">@MITREcorp</a>), Control Flow Hijacking w/Data Pointers (<a href="https://x.com/0xLegacyy" target="_blank">@0xLegacyy</a>), Copilot in notepad (<a href="https://x.com/zux0x3a" target="_blank">@zux0x3a</a>), .NET AOT in Ghidra (<a href="https://x.com/washi_dev" target="_blank">@washi_dev</a>), CSWSH in 2025 (<a href="https://x.com/includesecurity" target="_blank">@IncludeSecurity</a>), 300ms to Admin (<a href="https://x.com/compasssecurity" target="_blank">@compasssecurity</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-04-14 to 2025-04-21.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://whistlebloweraid.org/wp-content/uploads/2025/04/2025_0414_Berulis-Disclosure-HELP-and-Oversight-with-Exhibits.pdf" target="_blank">[PDF] Disclosure of Cyber Security Breach and Data Exfiltration through DOGE Systems and Whistleblower/Witness Intimidation</a> - A senior DevSecOps Engineer at the National Labor Relations Board ("NLRB") details what he saw as DOGE was granted access to NLRB systems. The evidence looks damning, whomever did these actions had high privileges, was exfiltrating a lot of data, and besides disabling logging, was pretty sloppy (smash and grab vs stealth). The use of correct credentials of a DOGE account from Russia (blocked by Geo-rules) just 15 minutes after the account was created is very strange. If we assume Russia had/has an active implant that pulled the credentials from a DOGE employee that created the account or was sent the credentials, why would they attempt to use them <em>from Russia</em>? The mix of high-level and amateur tradecraft doesn't make sense, but it wouldn't be the first time a Russian cyber actor <a href="https://www.wired.com/story/guccifer-elite-hackers-mistakes/" target="_blank">forgot to turn on their VPN</a>; it does happen. For a more editorialized version of the story, see: <a href="https://www.npr.org/2025/04/15/nx-s1-5355896/doge-nlrb-elon-musk-spacex-security" target="_blank">A whistleblower's disclosure details how DOGE may have taken sensitive labor data</a>.</li>
<li><a href="https://www.bleepingcomputer.com/news/security/cisa-extends-funding-to-ensure-no-lapse-in-critical-cve-services/" target="_blank">CISA extends funding to ensure 'no lapse in critical CVE services'</a> - MITRE, a non-profit federally funded research and development center, created and has maintained the Common Vulnerability and Exposures (CVE) database for 25 years. They sent a letter on 2025-04-15 that stated their funding would expire the next day. This is highly unusual, as government contracts not set to have their "option periods" (additional years) funded are notified well in advance. As the letter was making headlines, late the night of the 15th CISA apparently "executed the option period" (funded at least one additional year). While technically you can wait until midnight of the day the contract expires to extend it, it's highly unusual. If MITRE hadn't sent the letter that caused headlines, would the funding have come? Either way, there is now a new <a href="https://www.thecvefoundation.org/" target="_blank">CVE Foundation</a> that may be able to take over if MITRE does lose funding.</li>
<li><a href="https://cybersecurityadvisors.network/2025/04/15/la-liga-blocking-of-cloudflare-ips-in-spain/" target="_blank">La Liga: Blocking of Cloudflare IPs in Spain</a> - The Spanish La Liga football league blocked Cloudflare IPs to prevent Spanish citizen from streaming football matches. The issue is, over 20% of the internet sits behind Cloudflare, so blocking all of Cloudflare's IPs took down a good chunk of the internet for Spain during football matches. This is a good reminder of why technically competent advisors are needed for government agencies and enforcement. Cloudflare is <a href="https://www.broadbandtvnews.com/2025/02/19/cloudflare-takes-legal-action-over-laligas-disproportionate-blocking-efforts/" target="_blank">taking legal action</a> to stop the blocking.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://x.com/nicksdjohnson/status/1912439023982834120" target="_blank">[X] A thread on "extremely sophisticated phishing"</a> - The use of Oauth application grants to spoof a subpoena notice from Google is genius. The email reads "Google Legal Support was granted access to your Google Account" where "Google Legal Support" is the name of the attacker's Oauth app. This is 10/10 out of the box thinking. The attacker actually re-used a legitimate email Google sent, and just re-sent it via a few intermediaries to the victims. How does it work? Short answer: Email is hard. Long answer: see this <a href="https://easydmarc.com/blog/google-spoofed-via-dkim-replay-attack-a-technical-breakdown/" target="_blank">technical breakdown</a>.</li>
<li><a href="https://research.checkpoint.com/2025/cve-2025-24054-ntlm-exploit-in-the-wild/" target="_blank">CVE-2025-24054, NTLM Exploit In The Wild</a> - An NTLM leak was seen emailed to multiple targets. While SMB traffic <em>should</em> be blocked at the enterprise firewall from leaving an organization, it isn't always. <a href="https://github.com/0x6rss/CVE-2025-24071_PoC" target="_blank">CVE-2025-24071_PoC</a> is a tool to create a PoC.</li>
<li><a href="https://0xsp.com/offensive/the-hidden-risk-compromising-notepad-cowriters-bearer-tokens/?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=the-hidden-risk-compromising-notepad-cowriters-bearer-tokens" target="_blank">The Hidden Risk: Compromising Notepad Cowriter’s Bearer Tokens</a> - With Microsoft shoving Copilot into everything, not even notepad is safe.</li>
<li><a href="https://blog.includesecurity.com/2025/04/cross-site-websocket-hijacking-exploitation-in-2025/" target="_blank">Cross-Site WebSocket Hijacking Exploitation in 2025</a> - Same origin policy (SOP) doesn't apply to websockets, so browsers have to implement their own defenses. This post looks at what is possible today with WebSocket hijacking in different browsers.</li>
<li><a href="https://www.legacyy.xyz/defenseevasion/windows/2025/04/16/control-flow-hijacking-via-data-pointers.html" target="_blank">Control Flow Hijacking via Data Pointers</a> - Write better loaders with fewer calls to VirtualProtect using data pointers to get start the execution of your loaded shellcode. It was also released as a BOF: - <a href="https://github.com/iilegacyyii/DataInject-BOF" target="_blank">DataInject-BOF</a>.</li>
<li><a href="https://www.netspi.com/blog/technical-blog/adversary-simulation/cve-2025-21299-cve-2025-29809-unguarding-microsoft-credential-guard/" target="_blank">CVE-2025-21299 and CVE-2025-29809: Unguarding Microsoft Credential Guard</a> - "Insufficient validation of the Kerberos krbtgt service name within the TGT can lead to a bypass of credential guard, and therefore extraction of a primary TGT from the host that should otherwise be prevented."</li>
<li><a href="https://shells.systems/watch-your-ai-using-replit-ai-to-mask-your-c2-traffic/" target="_blank">Watch Your AI! Using Replit AI to Mask Your C2 Traffic</a> - "3rd Party C2" is the best kind of C2.</li>
<li><a href="https://blog.washi.dev/posts/recovering-nativeaot-metadata/" target="_blank">Recovering Metadata from .NET Native AOT Binaries</a> - Native AOT binaries are C# binaries that are pre-compiled to machine code vs the standard just-in-time (JIT) compilation of C# binaries. This makes them difficult to reverse engineer (i.e. all the normal tools don't work). This post explores the problem and introduces <a href="https://github.com/Washi1337/ghidra-nativeaot" target="_blank">ghidra-nativeaot</a> - Ghidra .NET Native AOT Analyzer Plugin.</li>
<li><a href="https://archie-osu.github.io/2025/04/13/powerhook.html" target="_blank">Code execution inside PID 0</a> - If you've ever wanted code execution inside of <cite>System Idle Process</cite>, this post is for you.</li>
<li><a href="https://blog.compass-security.com/2025/04/3-milliseconds-to-admin-mastering-dll-hijacking-and-hooking-to-win-the-race-cve-2025-24076-and-cve-2025-24994/" target="_blank">300 Milliseconds to Admin: Mastering DLL Hijacking and Hooking to Win the Race (CVE-2025-24076 and CVE-2025-24994)</a> - A low privilege user can trigger the install of the "Mobile devices" webcam functionality in Windows 11, which causes a DLL the user has write permissions on to be loaded by a SYSTEM process. It gets tricky because the DLL is loaded first as the user, and then as SYSTEM immediately after, making it a bit of a race condition. Clever use of WinAPI hooks with <a href="https://github.com/microsoft/Detours" target="_blank">Detours</a> solved that and made it reliable.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/MythicAgents/VECTR" target="_blank">VECTR</a> - A service container for Mythic C2 for interacting with SRA's VECTR.</li>
<li><a href="https://github.com/hasherezade/waiting_thread_hijacking" target="_blank">waiting_thread_hijacking</a> - Waiting Thread Hijacking - injection by overwriting the return address of a waiting thread.</li>
<li><a href="https://github.com/Meowmycks/koneko" target="_blank">koneko</a> - Robust Cobalt Strike shellcode loader with multiple advanced evasion features.</li>
<li><a href="https://github.com/ibaiC/FriendlyFireBOF" target="_blank">FriendlyFireBOF</a> - A BOF that suspends non-GUI threads for a target process or resumes them resulting in stealthy process silencing.</li>
<li><a href="https://github.com/Tylous/SourcePoint/releases/tag/v4.0" target="_blank">SourcePoint v4.0</a> - The popular C2 profile generator for Cobalt Strike has been updated to support the latest Cobalt Strike features.</li>
<li><a href="https://github.com/hackerschoice/bincrypter" target="_blank">bincrypter</a> - Pack/Encrypt/Obfuscate ELF + SHELL scripts.</li>
<li><a href="https://momo5502.github.io/emulator/" target="_blank">After days of struggle, my emulator now runs in the browser</a> - 🤯 web assembly is getting wild. Source: <a href="https://github.com/momo5502/emulator" target="_blank">emulator</a>.</li>
<li><a href="https://github.com/almounah/go-buena-clr" target="_blank">go-buena-clr</a> - Good CLR Host with Native patchless AMSI Bypass.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/GONZOsint/trufflehog-explorer" target="_blank">trufflehog-explorer</a> - a user-friendly web-based tool to visualize and analyze data extracted using TruffleHog.</li>
<li><a href="https://github.com/FalconForceTeam/dAWShund" target="_blank">dAWShund</a> - Putting a leash on naughty AWS permissions.</li>
<li><a href="https://github.com/ccbrown/cloud-snitch" target="_blank">cloud-snitch</a> - Easy-to-use map visualization for AWS activity, inspired by Little Snitch for macOS.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 450 (+3)</p>
<p>Blogs monitored: 409 (+1)</p>
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
