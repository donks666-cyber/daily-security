Title: Last Week in Security (LWiS) - 2024-07-29
Date: 2024-07-29 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-07-29
Author: Erik
Summary: Specula (<a href="https://x.com/Oddvarmoe" target="_blank">@Oddvarmoe</a> + <a href="https://x.com/freefirex2" target="_blank">@freefirex2</a>), 🧵 namecalling (<a href="https://x.com/hasherezade" target="_blank">@hasherezade</a>), North Korean 🇰🇵 agents, Llama 3.1 (<a href="https://x.com/Meta" target="_blank">@Meta</a>), GraphSpy updates (<a href="https://x.com/RedByte1337" target="_blank">@RedByte1337</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-07-22 to 2024-07-29.</p>
<aside class="m-block m-success">
<h3>DEF CON</h3>
<p>LWiS will be taking a two week break for DEF CON. If you're attending, come say hi and get a <a href="https://ludus.cloud/" target="_blank">Ludus</a> sticker! We'll be running a workshop in the <a href="https://x.com/EmbeddedVillage" target="_blank">Embedded Systems Village</a> all weekend and presenting "Supercharge your vuln finding workflow with automated labs: How Ludus made it rain creds from SCCM" on Sunday at the <a href="https://redteamvillage.io/schedule.html" target="_blank">Red Team Village</a> on Sunday at 1100.</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://ai.meta.com/blog/meta-llama-3-1/" target="_blank">Introducing Llama 3.1: Our most capable models to date</a> - Zuck continues his redemption arc with the release of the most powerful LLM with open weights. It's <a href="https://blog.cloudflare.com/meta-llama-3-1-available-on-workers-ai" target="_blank">now available on Workers AI</a> as well. Is OpenAI holding back a larger model? Will this prompt them to make it available? A "jailbreak" prompt for Llama 3.1 is <a href="https://github.com/elder-plinius/L1B3RT45/blob/main/META.mkd" target="_blank">already available</a>.</li>
<li><a href="https://www.forbes.com/sites/johnkoetsier/2024/07/26/x-just-gave-itself-permission-to-use-all-your-data-to-train-grok/" target="_blank">Here's How To Stop X From Using Your Data To Train Its AI</a> - With the launch of the <a href="https://x.com/elonmusk/status/1815325410667749760" target="_blank">Memphis Supercluster training</a>, X is using your data to train their AI. Here's how to opt out if you're on X and don't want to be part of the training set.</li>
<li><a href="https://www.binarly.io/blog/pkfail-untrusted-platform-keys-undermine-secure-boot-on-uefi-ecosystem" target="_blank">PKfail: Untrusted Platform Keys Undermine Secure Boot on UEFI Ecosystem</a>  - Many manufacturers are shipping firmware with the default American Megatrends International (AMI) placeholder key. The AMI Secure Boot "master key", called the Platform Key (PK), was publicly exposed in a data leak of a downstream firmware vendor. Possession of this leaked key allows anyone to add EFI modules to the boot sequence even with Secure Boot enabled. <a href="https://youtu.be/SPl7zfC-CmQ" target="_blank">Windows PoC video</a> and <a href="https://www.youtube.com/watch?v=CveWt3gFQTE" target="_blank">Linux PoC video</a>.</li>
<li><a href="https://security.googleblog.com/2024/07/building-security-into-redesigned.html" target="_blank">Building security into the redesigned Chrome downloads experience</a> - Google will now upload and scan files for users opted into Enhanced Protection. Interestingly, if the download is password protected, Chome will even prompt for the password and send that off to Google to unpack and scan the file. Good for security, but potentially a privacy/compliance issue. The password prompt can be skipped and the whole process is opt-in.</li>
<li><a href="https://blog.knowbe4.com/how-a-north-korean-fake-it-worker-tried-to-infiltrate-us" target="_blank">How a North Korean Fake IT Worker Tried to Infiltrate Us</a> - A North Korean agent managed to get hired at the phishing testing company KnowBe4. Strange that the agent would conduct and pass 4 video interviews and a background check (using a stolen US identity) only to try to load malware on their workstation immediately after it was received. The North Korean team responsible for landing the job is probably really upset with the team that was in charge of "post exploitation" for burning the access so fast.</li>
<li><a href="https://www.cnbc.com/2024/07/23/google-wiz-deal-dead.html" target="_blank">Wiz walks away from $23 billion deal with Google, will pursue IPO</a> - It's got to take some serious conviction to walk away from a $23 billion deal.</li>
<li><a href="https://krebsonsecurity.com/2024/07/crooks-bypassed-googles-email-verification-to-create-workspace-accounts-access-3rd-party-services/" target="_blank">Crooks Bypassed Google's Email Verification to Create Workspace Accounts, Access 3rd-Party Services</a> - Single sign on is great, unless attackers can sign up for the SSO provider with your domain without proving ownership. This allows impersonation of a company on 3rd party sites that allow sign in with Google. Google has fixed the issue.</li>
<li><a href="https://www.dni.gov/files/documents/FOIA/DF-2018-00013-National-Intelligence-Council-Memorandum.pdf" target="_blank">[PDF] Kaspersky Laboratory Products Puts Networks and Data at Risk of Exploitation by Russian Intelligence Services</a> - A heavily redacted report from the National Intelligence Council that broadly addresses the risks of Kaspersky. The report is from 2017 but was publicly released 2024-07-19.</li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2024/07/29/ransomware-operators-exploit-esxi-hypervisor-vulnerability-for-mass-encryption/" target="_blank">Ransomware operators exploit ESXi hypervisor vulnerability for mass encryption</a> - If you have ESXi servers that are domain joined, read this ASAP. TLDR: Adding users to the "ESX Admins" group == ESXI compromise. 😬</li>
<li><a href="https://harfanglab.io/en/insidethelab/doppelganger-operations-europe-us/" target="_blank">Mid-year Doppelgänger information operations in Europe and the US</a> - Some Russian TTP light reading. A look at Russian campaigns against the French.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.synacktiv.com/en/publications/injecting-java-in-memory-payloads-for-post-exploitation" target="_blank">Injecting Java In-Memory Payloads for Post-Exploitation</a> - "This article will cover some tips and tricks that could be applied to inject such a payload, and to develop post-exploitation features that would allow altering the application behavior. This would be interesting to stay under the radar during post-exploitation, or to intercept plaintext credentials of privileged users authenticating to the compromised application."</li>
<li><a href="https://blog.ret2.io/2024/07/24/pwn2own-auto-2024-charx-exploit/" target="_blank">Pwn2Own Automotive: Popping the CHARX SEC-3100</a> - Part 2 of the blog introduced last week. This post covers exploit development for the CHARX SEC-3100, an AC charging controller, with an embedded Linux system.</li>
<li><a href="https://posts.specterops.io/deep-sea-phishing-pt-1-092a0637e2fd" target="_blank">Deep Sea Phishing Pt. 1</a> - With this much phishing content coming out of Specter Ops recently I am starting to suspect they are building up for a product or service announcement around phishing.</li>
<li><a href="https://tierzerosecurity.co.nz/2024/07/23/edr-telemetry-blocker.html" target="_blank">EDR Telemetry Blocking via Person-in-the-Middle Attacks</a> - Block EDR telemetry reaching its cloud servers by performing a Person-in-the-Middle (PitM) attack and filtering telemetry packets.</li>
<li><a href="https://trufflesecurity.com/blog/anyone-can-access-deleted-and-private-repo-data-github" target="_blank">Anyone can Access Deleted and Private Repository Data on GitHub</a> - You can access data from deleted forks, deleted repositories and even private repositories on GitHub. And it is available forever. This is known by GitHub, and intentionally designed that way.</li>
<li><a href="https://medium.com/@TalBeerySec/revealing-the-inner-structure-of-aws-session-tokens-a6c76469cba7" target="_blank">Revealing the Inner Structure of AWS Session Tokens</a> - Reverse engineering analysis of AWS Session Tokens.</li>
<li><a href="https://cti.monster/blog/2024/07/25/pdfdropper.html" target="_blank">Injecting Malicious Code into PDF Files and PDF Dropper Creation</a> - Something to look at for your initial access tradecraft. Injecting JavaScript into a PDF file to download a file from a specific URL and establish C2.</li>
<li><a href="https://www.thedfirspot.com/post/rdp-bitmap-cache-piece-s-of-the-puzzle" target="_blank">RDP Bitmap Cache - Piece(s) of the Puzzle</a> - Friendly reminder of some of the artifacts you are leaving behind. Defenders, anyone analyzing these at scale in your enterprise and baselining RDP activity by your syadmins yet?</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://trustedsec.com/blog/specula-turning-outlook-into-a-c2-with-one-registry-change" target="_blank">Specula - Turning Outlook Into a C2 With One Registry Change</a> - Did you know that Outlook has access to the entire system via COM/vbscript and that a custom homepage URL can use those features? Specula uses this to turn Outlook into a C2 - some solid <a href="https://www.youtube.com/watch?v=9qM2m1LZuVo" target="_blank">traitorware</a>!</li>
<li><a href="https://vulncheck.com/blog/vulncheck-goes-scanless" target="_blank">VulnCheck go-exploit Goes Scanless</a> - <a href="https://github.com/vulncheck-oss/go-exploit-cache" target="_blank">go-exploit-cache</a> can now ingest shodan data or pcap data to find vulnerabilities without active scanning.</li>
<li><a href="https://github.com/RedByte1337/GraphSpy" target="_blank">GraphSpy</a> - Initial Access and Post-Exploitation Tool for AAD and O365 with a browser-based GUI. Not new but just added the ability to list and modify MFA methods!</li>
<li><a href="https://github.com/Allevon412/SyscallTempering" target="_blank">SyscallTempering</a> improves upon the previous research and obtains a list of system calls that are not hooked by the currently running EDR solution (tested against sophos).</li>
<li><a href="https://github.com/hasherezade/thread_namecalling" target="_blank">thread_namecalling</a> - Process Injection using Thread Name. Full blogpost <a href="https://research.checkpoint.com/2024/thread-name-calling-using-thread-name-for-offense/" target="_blank">here</a>.</li>
<li><a href="https://github.com/TierZeroSecurity/edr_blocker" target="_blank">edr_blocker</a> - Blocks EDR Telemetry by performing Person-in-the-Middle attack where network filtering is applied using iptables. The blocked destination IP addresses are parsed based on the server name in TLS Client Hello packet and the provided blocked server name (or blocked string) list in the file.</li>
<li><a href="https://github.com/Leo4j/SessionExec" target="_blank">SessionExec</a> - Execute commands in other Sessions.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Leo4j/KeyCredentialLink" target="_blank">KeyCredentialLink</a> - Add Shadow Credentials to a target object by editing their msDS-KeyCredentialLink attribute.</li>
<li><a href="https://github.com/Leo4j/Invoke-ShareHunter" target="_blank">Invoke-ShareHunter</a> - Enumerate the Domain for Readable and Writable Shares.</li>
<li><a href="https://github.com/ricardojoserf/SharpSelfDelete" target="_blank">SharpSelfDelete</a> - PoC to self-delete a binary in C#.</li>
<li><a href="https://azurecharts.com/" target="_blank">Welcome to Azure Charts!</a> - Live visual exploration environment for Azure Cloud + ecosystem</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 432 (+1)</p>
<p>Blogs monitored: 386 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
