Title: Last Week in Security (LWiS) - 2026-01-12
Date: 2026-01-12 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2026-01-12
Author: Erik
Summary: SmarterMail Pre-auth RCE (<a href="https://x.com/chudyPB" target="_blank">@chudyPB</a> + <a href="https://x.com/sinsinology" target="_blank">@SinSinology</a>), Claude Code code execution (<a href="https://x.com/ryotkak" target="_blank">@ryotkak</a>), VSS create (<a href="https://x.com/ricardojoserf" target="_blank">@RicardoJoseRF</a> ), EDRStartupHinder (<a href="https://x.com/TwoSevenOneT" target="_blank">@TwoSevenOneT</a>), and more!

<aside class="m-block m-success">
<h3>LWiS Break</h3>
<p>We launched <a href="https://ludus.cloud/" target="_blank">Ludus</a> on 2024-02-06. Since they we have been hard at work on new features driven by user feedback, releasing 71 versions. Over the next two weeks we will be hard at work on finalizing the next major release of Ludus and will take a break from LWiS during that time.</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2026-01-05 to 2026-01-12.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://x.com/CloudflareRadar/status/2010773830172627347" target="_blank">[X] Iran's disconnection from the Internet is now in its 5th day</a> - Even Starlink is reportedly being jammed by the government of Iran. <a href="https://www.reddit.com/r/Starlink/comments/1q9toxo/as_iranian_regime_shuts_down_internet_even/nz1zski/" target="_blank">Reddit users</a> are reporting issues with Starlink but still have connectivity.</li>
<li><a href="https://www.bnd.bund.de/SharedDocs/Stellenangebote/DE/Stellenangebote/AS-2025-901-enterbnd-hacking-hd.html" target="_blank">Germany's foreign intelligence agency (BND) is looking to hire CTF players</a> - "Experience in penetration testing, red team engagements or capture the flags (CTF)."</li>
<li><a href="https://fox11online.com/news/crime/menasha-police-officer-accused-of-using-license-plate-recognition-system-to-track-his-ex-girlfriend-cristian-morales-misconduct-in-office-flock-domestic-abuse-restraining-order-cash-bond" target="_blank">Menasha police officer accused of using license plate recognition system to track his ex</a> - Don't build systems that can easily be abused and this won't be a problem.</li>
<li><a href="https://www.aol.com/articles/popular-grocery-store-chain-uses-130056099.html?_guc_consent_skip=1767738511" target="_blank">Popular grocery store chain uses biometric surveillance on shoppers, raising privacy concerns</a> - "A person does not surrender all Fourth Amendment protection by venturing into the public sphere." (<a href="https://www.law.cornell.edu/supremecourt/text/16-402" target="_blank">CARPENTER v. UNITED STATES</a>)</li>
<li><a href="https://github.com/torvalds/AudioNoise/commit/93a72563cba609a414297b558cb46ddd3ce9d6b5" target="_blank">Merge branch 'antigravity'</a> - Linus Torvalds, the maintainer of the Linux kernel, "vibe-coded" a visualization tool. The truth is Linus has been "vibe coding" for a long time. He rarely authors code for Linux, instead directing changes and reviewing code from others before merging. He just replaced "others" with Gemini for this case but people are making a big deal about it.</li>
<li><a href="https://www.theverge.com/tech/856149/microsoft-365-office-rebrand-copilot?ref=selfh.st" target="_blank">No, Microsoft didn’t rebrand Office to Microsoft 365 Copilot</a> - Can't really blame people for thinking the rebrand happened. “In November 2022, we renamed only the Office ‘hub’ app for web and mobile to the Microsoft 365 app. In January 2025, we updated it to the Microsoft 365 Copilot app to reflect its role in bringing Copilot and Microsoft 365 productivity experiences together in one place.”</li>
<li><a href="https://phrack.org/issues/7/3" target="_blank">The Conscience of a Hacker</a> - The "Hacker Manifesto" turned 40 years old last week. A classic part of hacker history and culture.</li>
<li><a href="https://blog.thinkst.com/2026/01/thinkst-canary-acquires-uk-based-deceptiq.html">Thinkst Canary acquires UK-based DeceptIQ</a> - Wow. That was fast. We reported on the launch of DeceptIQ in <a href="https://blog.badsectorlabs.com/last-week-in-security-lwis-2025-11-10.html">LWiS 2025-11-10</a>. Congrats to Rad and the team at Thinkst!</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.watchtowr.com/do-smart-people-ever-say-theyre-smart-smartertools-smartermail-pre-auth-rce-cve-2025-52691/" target="_blank">Do Smart People Ever Say They’re Smart? (SmarterTools SmarterMail Pre-Auth RCE CVE-2025-52691)</a> - When <a href="https://x.com/chudyPB" target="_blank">@chudyPB</a> and <a href="https://x.com/sinsinology" target="_blank">@SinSinology</a> team up, shells are all but guaranteed. The timing of the patch vs the advisory (3 month gap) is interesting. With the rise of AI, will the patch-diff-to-exploit pipeline become commoditized? Will the AI powered EDR save us from the AI generated exploits?</li>
<li><a href="https://flatt.tech/research/posts/pwning-claude-code-in-8-different-ways/" target="_blank">Pwning Claude Code in 8 Different Ways</a> - Some "read only" commands were allowlisted by default, and of course they could be abused to execute arbitrary code.</li>
<li><a href="https://www.outflank.nl/blog/2026/01/07/patchguard-peekaboo-hiding-processes-on-systems-with-patchguard-in-2026/" target="_blank">PatchGuard Peekaboo: Hiding Processes on Systems with PatchGuard in 2026</a> - This may be the most technical post I've read that also has clear AI generated parts like, "HVCI didn’t just raise the bar – it fundamentally changed the game by moving enforcement to a layer that kernel code simply cannot reach," and "the cat-and-mouse game isn’t dead – it’s just moved to a much smaller playing field." The "not x but y" pattern is appearing everywhere these days...</li>
<li><a href="https://blog.quarkslab.com/clang-hardening-cheat-sheet-ten-years-later.html" target="_blank">Clang Hardening Cheat Sheet - Ten Years Later</a> - A recommended set of options for compiling C and C++ with Clang to improve security of the resulting binaries.</li>
<li><a href="https://ricardojoserf.github.io/w11shadowcopies/" target="_blank">Creating Shadow Copies with VSS API</a> - With Microsoft removing the vssadmin command to create shadow copies, you now have to use the VSS API to create them.</li>
<li><a href="https://arxiv.org/pdf/2512.09742" target="_blank">[PDF] Weird Generalization and Inductive Backdoors: New Ways to Corrupt LLMs</a> - A small amount of data poisoning can cause dramatic shifts in model's behavior (i.e. from good to bad terminator based on the "current year").</li>
<li><a href="https://www.cyera.com/research-labs/ni8mare-unauthenticated-remote-code-execution-in-n8n-cve-2026-21858" target="_blank">Ni8mare  -  Unauthenticated Remote Code Execution in n8n (CVE-2026-21858)</a> - It's really unauthenticated file access, which you can then use for token forgery and n8n has remote code execution as a feature. Patched in 1.121.0 and the 2.x versions of n8n are not affected.</li>
<li><a href="https://trustedsec.com/blog/updating-the-sysmon-community-guide-lessons-learned-from-the-front-lines" target="_blank">Updating the Sysmon Community Guide: Lessons Learned from the Front Lines</a> - A great resource for defenders just got a big update.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul><li><a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">PhantomSec | Advanced Offensive Capabilities Automated - EvadeX</a> <span class="m-label m-flat m-success">Sponsored</span> - EvadeX is an evasion-as-a-service platform for red teams and pentesters who want modern, continuously-updated evasive tradecraft without turning every engagement into an R&amp;D project. Generate highly customizable, low-signature payloads through a simple web workflow so you can tune to the target and stay focused on the engagement. Trusted by teams from small consultancies to the Fortune 10. <a href="https://phantomsec.tools/?utm_source=LWIS" style="color: #3bd267;" target="_blank">Get callbacks past EDR today!</a></li></ul><ul>
<li><a href="https://github.com/Pennyw0rth/NetExec-Lab/tree/main/Barbhack-2025" target="_blank">Barbhack CTF 2025 (Pirates - Active Directory Lab)</a> - Originally featured in the Barbhack 2025 CTF, this lab is now available for free to everyone! In this lab, you'll explore how to use the powerful tool NetExec to efficiently compromise an Active Directory domain during an internal pentest. Build on VMware, VirtualBox, or <a href="https://ludus.cloud" target="_blank">Ludus</a>.</li>
<li><a href="https://github.com/watchtowrlabs/watchTowr-vs-SmarterMail-CVE-2025-52691" target="_blank">watchTowr-vs-SmarterMail-CVE-2025-52691</a> - SmarterMail Pre-Auth RCE 1day Detection Artifact Generator Tool</li>
<li><a href="https://github.com/c0rdyc3ps/ScrappyDoo" target="_blank">ScrappyDoo</a> - Opengraph-Compatible JSON Generator for BloodHound.</li>
<li><a href="https://github.com/ricardojoserf/w11_shadow_copies" target="_blank">w11_shadow_copies</a> - Create, delete or list Shadows Copies using the VSS API using C++, C# or Python.</li>
<li><a href="https://github.com/TwoSevenOneT/EDRStartupHinder" target="_blank">EDRStartupHinder</a> - A red team tool to prevent Antivirus and EDR from running (Check the <a href="https://www.zerosalarium.com/2026/01/edrstartuphinder-edr-startup-process-blocker.html" target="_blank">blog post</a> for more details.)</li>
<li><a href="https://github.com/0x4D31/santamon" target="_blank">santamon</a> - Lightweight macOS detection agent built on Santa’s Endpoint Security telemetry.</li>
<li><a href="https://github.com/Macmod/flashingestor" target="_blank">flashingestor</a> - A TUI for Active Directory collection.</li>
<li><a href="https://github.com/0xedh/dumpguard_bof" target="_blank">dumpguard_bof</a> - Beacon Object File (BOF) port of DumpGuard for extracting NTLMv1 hashes from sessions on modern Windows systems.</li>
<li><a href="https://github.com/incursi0n/ClipboardStealBOF" target="_blank">ClipboardStealBOF</a> - An alternative to the builtin clipboard feature in Cobalt Strike that adds the capability to enable/disable and dump the clipboard history.</li>
<li><a href="https://github.com/Logisek/AfterShell" target="_blank">AfterShell</a> - Fast Windows post-exploitation wins after initial access.</li>
<li><a href="https://github.com/zoicware/RemoveWindowsAI" target="_blank">RemoveWindowsAI</a> - Force Remove Copilot, Recall and More in Windows 11.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.youtube.com/watch?v=vVI7atoAeoo" target="_blank">I Built a 1 Petabyte Server From Scratch</a> - A great video of a JBOD built from scratch. The highlight is all the testing done at each step of the build. Remember what Mythbusters tought you, "the only difference between screwing around and science is writing it down."</li>
<li><a href="https://blog.tobyjackson.io/blog/what-makes-a-senior-pentester/" target="_blank">Climbing The Ladder: What Non-Technical Attributes Make a Senior Pentester?</a> - Underapreciated "soft skills" that make you valuable to companies.</li>
<li><a href="https://github.com/JeanBonBeurre34/cc-agent" target="_blank">cc-agent</a> - Another command and control agent.</li>
<li><a href="https://github.com/kreuzberg-dev/kreuzberg" target="_blank">kreuzberg</a> - A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Java, Go, PHP, Elixir, C#, TypeScript (Node/Bun/Wasm/Deno) — or use via CLI, REST API, or MCP server.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 495 (+2)</p>
<p>Blogs monitored: 439 (+0)</p>
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
