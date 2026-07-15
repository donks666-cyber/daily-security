Title: Last Week in Security (LWiS) - 2025-12-02
Date: 2025-12-02 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-12-02
Author: Erik
Summary: Two weeks of news, techniques, tools, exploits, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-11-18 to 2025-12-02.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://www.alteredsecurity.com/online-labs?utm_source=badsectorlabs&amp;utm_medium=email&amp;utm_campaign=diwali_offer" style="color: #3bd267;" target="_blank">Sharpen your Red Team skills with 20% OFF</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p style="text-indent: 0;">Start your Red Team training with Altered Security! We offer affordable Red Team courses with enterprise-like hands-on labs and lifetime access to course materials.</p>
<p style="text-indent: 0;">Each course comes with an industry-recognized certification. We are the creators of the Certified Red Team Professional (CRTP), CRTE, CARTP and more. Join more than 50,000 professionals from 130+ countries.</p>
<p style="text-indent: 0;">Get 20% OFF on all courses and instructor-led bootcamps to be held in Q1 and Q2 2026 in our Black Friday deals until December 17, 2025. No coupon code required. <strong><a href="https://www.alteredsecurity.com/online-labs?utm_source=badsectorlabs&amp;utm_medium=email&amp;utm_campaign=diwali_offer" style="color: #3bd267;" target="_blank">Sign up now!</a></strong></p>
</aside><ul>
<li><a href="https://archive.is/20251124130917/https://www.bloomberg.com/news/articles/2025-11-20/cyber-warfare-startup-nabs-contracts-to-give-us-military-hackers-ai-tools#selection-1229.0-1234.0" target="_blank">US Military Hackers Go on Offense With Help From Cyber Startup</a> - The US has always had a private/public partnership for all things military, and now it's looking like it will have it for offensive cyber operations as well. I hope the CISO at Twenty is ready for the nation state attacks that will inevitably follow this publication.</li>
<li><a href="https://peaches.cloud/events/hacking-cmmc-ctf-with-cybertalents" target="_blank">Hacking CMMC CTF with CyberTalents</a> - A CTF focused on a cybersecurity standard that is currently being implemented by the US government is novel.</li>
<li><a href="https://security.googleblog.com/2025/11/android-quick-share-support-for-airdrop-security.html" target="_blank">Android Quick Share Support for AirDrop: A Secure Approach to Cross-Platform File Sharing</a> - Cross-platform file sharing for the mobile OSs. What's next, world peace?!</li>
<li><a href="https://krebsonsecurity.com/2025/11/meet-rey-the-admin-of-scattered-lapsus-hunters/" target="_blank">Meet Rey, the Admin of ‘Scattered Lapsus$ Hunters’</a> - Quite a journey of OSINT breadcrumbs to uncover the identity of an admin of the Scattered Lapsus$ Hunters Telegram group.</li>
<li><a href="https://www.eff.org/deeplinks/2025/11/lawmakers-want-ban-vpns-and-they-have-no-idea-what-theyre-doing" target="_blank">Lawmakers Want to Ban VPNs—And They Have No Idea What They're Doing</a> - Wisconsin joins Michigan in attempting to ban VPNs, except Wisconsin's bill has passed the State Assembly is is moving through the State Senate. "This battle is being fought by people who clearly have no idea how any of this technology actually works."</li>
<li><a href="https://www.schneier.com/blog/archives/2025/11/huawei-and-chinese-surveillance.html" target="_blank">Huawei and Chinese Surveillance</a> - Interesting anecdote from the Stone Group founder about how the Ministry of State Security told him they would were going to "send agents to work undercover at his company in positions dealing with international relations." Nothing that ties this to Huawei, but interesting nonetheless.</li>
<li><a href="https://www.privacyguides.org/news/2025/11/22/grapheneos-migrates-server-infrastructure-from-france-amid-police-intimidation-claims/" target="_blank">GrapheneOS migrates server infrastructure from France amid police intimidation claims</a> - Speaking of government intimidation...</li>
<li><a href="https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack" target="_blank">Shai-Hulud 2.0 Supply Chain Attack: 25K+ Repos Exposing Secrets</a>  - The JavaScript Node Package Manager (npm) ecosystem was under attack yet again. This worm-like campaign is impressive in its scope and the fact it was registering infected developer machines as GitHub Actions runners and then using GitHub Actions for command and control is pretty clever.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.watchtowr.com/stop-putting-your-passwords-into-random-websites-yes-seriously-you-are-the-problem/" target="_blank">Stop Putting Your Passwords Into Random Websites (Yes, Seriously, You Are The Problem)</a> - It's so easy to <a href="https://github.com/CorentinTh/it-tools" target="_blank">self-host</a> these kinds of formatters there is no excuse for using random websites, and then to "save" them is just something else.</li>
<li><a href="https://aff-wg.org/2025/12/01/tradecraft-orchestration-in-the-garden/" target="_blank">Tradecraft Orchestration in the Garden</a> - The addition of variables and callable labels makes Tradecraft Garden projects truly modular. For more see <a href="https://rastamouse.me/pic-symphony/" target="_blank">PIC Symphony</a> by Rasta Mouse. I have a feeling there is a Tradecraft Garden/Crystal Palace training course in the works 😉.</li>
<li><a href="https://decoder.cloud/2025/11/24/reflecting-your-authentication-when-windows-ends-up-talking-to-itself/" target="_blank">Reflecting Your Authentication: When Windows Ends Up Talking to Itself</a> - Kerberos, NTLM, SMB, HTTP and DCE/RPC, Ghost SPNs, the CredMarshalTargetInfo (CMTI) trick, and more covered in this post. Authentication coercion and reflection is an issue in basically every Windows environment. The fact that until June 2025 any domain user could reflect authentication back to a domain controller and compromise a domain is crazy. "There are a couple of other reflection attacks I've already submitted to MSRC" 🤯</li>
<li><a href="https://fluxsec.red/creating-implant-dll-exports-wyrm-c2" target="_blank">Creating a framework in Wyrm C2 to easily configure custom exports of an implant</a> - This rust based C2 framework is expanding quickly.</li>
<li><a href="https://specterops.io/blog/2025/11/25/less-praying-more-relaying-enumerating-epa-enforcement-for-mssql-and-https/" target="_blank">Less Praying More Relaying – Enumerating EPA Enforcement for MSSQL and HTTPS</a> - A great low level investigation into what Enhanced Protection for Authentication (EPA) actually does in practice, and some nice tooling to enumerate it. While I can't prove it, the IPs used in the screenshots look like this was developed in a GOAD lab on <a href="https://ludus.cloud" target="_blank">Ludus</a>.</li>
<li><a href="https://specterops.io/blog/2025/11/21/an-evening-with-claude-code/" target="_blank">An Evening with Claude (Code)</a> - Using regex and an LLM to determine if a command is safe seems like an impossible task. There are simply too many edge cases and strange utilities that can execute commands or write to files. Always a good idea to use containers, sandboxes, VMs for AI work. You know, in case <a href="https://www.reddit.com/r/google_antigravity/comments/1p82or6/google_antigravity_just_deleted_the_contents_of/" target="_blank">Google Antigravity deletes the contents of your whole drive</a>.</li>
<li><a href="https://specterops.io/blog/2025/11/19/sccm-hierarchy-takeover-via-entra-integrationbecause-of-the-implication/" target="_blank">SCCM Hierarchy Takeover via Entra Integration…Because of the Implication</a> - Three posts from Specter Ops in one LWiS? Yep. That what happens when you publish good content. At this point Garrett Foster may be the world's leading expert on SCCM attacks. While this is a somewhat niche attack (you have to be able to manipulate UPNs), getting SCCM administrator is usually game over for the domain. Another CVE powered by <a href="https://ludus.cloud" target="_blank">Ludus</a> 😊.</li>
<li><a href="https://whiteknightlabs.com/2025/11/25/discreet-driver-loading-in-windows/" target="_blank">Discreet Driver Loading in Windows</a> - You can modify a driver's checksum, and therefore it's hash, which keeps the digital signature valid while breaking any hash based detections. Note that Microsoft’s list of blocked drivers cannot be bypassed using this technique, since that list includes the <a href="https://docs.virustotal.com/reference/authentihash" target="_blank">authentihash</a> of the drivers.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/HackingLZ/push_matrix_tool" target="_blank">push_matrix_tool</a> - A self-hosted web push notification demo server for testing and training purposes. Built with FastAPI and vanilla JavaScript.</li>
<li><a href="https://github.com/zyn3rgy/relayinformer" target="_blank">RelayInformer</a> - Python and BOF utilities to the determine EPA enforcement levels of popular NTLM relay targets from the offensive perspective.</li>
<li><a href="https://github.com/Orange-Cyberdefense/moxpack" target="_blank">moxpack</a> - A Qemu Proxmox Template builder project using Packer.</li>
<li><a href="https://github.com/Cobalt-Strike/sleepmask-vs" target="_blank">sleepmask-vs</a> - A simple Sleepmask BOF example.</li>
<li><a href="https://github.com/Cobalt-Strike/icmp-udc2" target="_blank">icmp-udc2</a> - UDC2 implementation that provides an ICMP C2 channel.</li>
<li><a href="https://github.com/monsieurPale/RSA-Backdoor" target="_blank">RSA-Backdoor</a> - This repo contains code to reproduce the Secretly Embedded Trapdoor with Universal Protection (SETUP) attack on RSA key generation proposed by Young &amp; Yung, 1996. Considering the potential of this attack, never trust black box key generation systems. I am also planning on providing a small utility to hook ssh-keygen on compromised host to automatically backdoor further keys... TBC</li>
<li><a href="https://github.com/entropy-z/Kharon-Agent" target="_blank">Kharon-Agent</a> - Agent for AdaptixC2 containing lateral movement capabilities ( WMI, SCM, WinRM, DCOM), bof/dotnet/shellocde in memory executions, postex modules with shellcode and bof with possibilities of fork executions (spawn/explicit).</li>
<li><a href="https://github.com/NtDallas/BOF_RunPe" target="_blank">BOF_RunPe</a> - BOF to run PE in Cobalt Strike Beacon without console creation.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/rustmailer/bichon" target="_blank">bichon</a> - A lightweight, high-performance Rust email archiver with WebUI.</li>
<li><a href="https://github.com/ckane/CS7038-Malware-Analysis" target="_blank">CS7038-Malware-Analysis</a> - Course Repository for University of Cincinnati Malware Analysis Class (CS[567]038).</li>
<li><a href="https://github.com/p-e-w/heretic" target="_blank">heretic</a> - Fully automatic censorship removal for language models.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 490 (+0)</p>
<p>Blogs monitored: 436 (+0)</p>
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
