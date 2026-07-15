Title: Last Week in Security (LWiS) - 2023-02-13
Date: 2023-02-13 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-02-13
Author: Erik
Summary: Phishing in 2023 (<a href="https://twitter.com/0xcsandker" target="_blank">@0xcsandker</a>), SaltStack A-Salt (Alex Hill - <a href="https://twitter.com/SkylightCyber" target="_blank">@SkylightCyber</a>), LocalPotato (<a href="https://twitter.com/decoder_it" target="_blank">@decoder_it</a> + <a href="https://twitter.com/elad_shamir" target="_blank">@elad_shamir</a>), install4j XXE (<a href="https://twitter.com/frycos" target="_blank">@frycos</a>), LPE in Avast (<a href="https://twitter.com/Denis_Skvortcov" target="_blank">@Denis_Skvortcov</a>), learning Semgrep (<a href="https://twitter.com/jrozner/" target="_blank">@jrozner</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-02-06 to 2023-02-13.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://valle-demo.github.io/" target="_blank">VALL-E - Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers</a>. New research from Mircosoft shows how the new model can clone a voice to a high degree of accuracy with only 3 seconds of sample audio from the target. Previous techniques required at least 30 minutes of audio and had worse results. Think how easy it will soon be to call some, record their voice, and then have "them" say things generated in real time. This will be used for vishing, and it will be extremely effective.</li>
<li><a href="https://twitter.com/MrTuxracer/status/1623374059655335959" target="_blank">Truffle Security revealed data collection in XSS Hunster</a>. Infosec Twitter was quick to denounce the data collection and suggest running your own instance.</li>
<li><a href="https://support.apple.com/en-us/HT213635" target="_blank">About the security content of iOS 16.3.1 and iPadOS 16.3.1</a>. WebKit exploit and "Apple is aware of a report that this issue may have been actively exploited."</li>
<li><a href="https://twitter.com/lemogbenga/status/1624881422640062470" target="_blank">Namcheap/Namecheap's SendGrid account compromised to send phishing emails</a>. Namecheap <a href="https://www.namecheap.com/status-updates/archives/74848" target="_blank">says its SendGrid</a>, SendGrid hasn't said anything (that I can find).</li>
<li><a href="https://blog.thinkst.com/2023/02/canarytokens-org-welcomes-azure-login-certificate-token.html" target="_blank">Canarytokens.org welcomes Azure Login Certificate Token</a>. Canarytokens are still the best free security tool you aren't using.</li>
<li><a href="https://www.reddit.com/r/reddit/comments/10y427y/we_had_a_security_incident_heres_what_we_know/" target="_blank">We had a security incident. Here's what we know.</a>. Phish to cloned internal gateway gives an attacker valid credentials and second-factor token. FIDO2/U2F would have made this impossible. Props to the user for self-reporting.</li>
<li><a href="https://blog.projectdiscovery.io/announcing-nuclei-cloud/" target="_blank">Announcing Nuclei Cloud</a>. The undisputed champions of the open source attack surface management tooling game are here with their hosted solution. This is not one to dismiss given their incredible history of high quality tool releases.</li>
<li><a href="https://blogs.microsoft.com/blog/2023/02/07/reinventing-search-with-a-new-ai-powered-microsoft-bing-and-edge-your-copilot-for-the-web/" target="_blank">Reinventing search with a new AI-powered Microsoft Bing and Edge, your copilot for the web</a>. ChatGPT++ comes to Bing. This actually made me create a Microsoft account and sign up for the waitlist. Well done Microsoft.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.cobaltstrike.com/blog/behind-the-mask-spoofing-call-stacks-dynamically-with-timers/" target="_blank">Behind the Mask: Spoofing Call Stacks Dynamically with Timers</a>. The Cobalt Strike team is hard at work pushing the boundries of call stack spoofing.</li>
<li><a href="https://decoder.cloud/2023/02/13/localpotato-when-swapping-the-context-leads-you-to-system/" target="_blank">LocalPotato - When Swapping The Context Leads You To SYSTEM</a>. The Potatos never die! This is the 21st potato in my collection. Patching in 2023-01 (as <a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21746" target="_blank">CVE-2023-21746</a> ), this potato allows for local privilege escaltion through some tricky SPN manipulation.</li>
<li><a href="https://jub0bs.com/posts/2023-02-08-fearless-cors/" target="_blank">Fearless CORS: a design philosophy for CORS middleware libraries (and a Go implementation)</a>. This is the best post on CORS on the internet. DM me anything better. I dare you.</li>
<li><a href="https://www.securesystems.de/blog/offphish-phishing-revisited-in-2023/" target="_blank">Offphish - Phishing revisited in 2023</a>. This is a great rundown of modern phishing techniques. Keep in mind the ISO MOTW bypass was <a href="https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-zero-day-bug-exploited-to-push-malware/" target="_blank">patched by Microsoft in November</a>.</li>
<li><a href="https://gts3.org/assets/papers/2022/gupta:popkorn.pdf" target="_blank">[PDF] POPKORN: Popping Windows Kernel Drivers At Scale</a>. Some interesting work on "large scale" (212 unique singed Windows kernel drivers) driver fuzzing. Unlike seemingly every other interesting paper, they actually <a href="https://github.com/ucsb-seclab/popkorn-artifact" target="_blank">published the code!</a>.</li>
<li><a href="https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/" target="_blank">A-Salt: attacking SaltStack</a>. SaltStack is a desired state configruation platform and less popular member of the Ansible, Puppet, SaltStack triad. Unlike Ansible, which is agentless, SaltStack uses an agent-server model and is basically a remote access tool (and potential traitorware!).</li>
<li><a href="https://research.nccgroup.com/2023/02/09/security-code-review-with-chatgpt/" target="_blank">Security Code Review With ChatGPT</a>. The ChatGPT craze is still with us. Stop feeding it your code. I almost daily have it write me things in languages I'm not fully familair with and it does a decent job at getting me started.</li>
<li><a href="https://frycos.github.io/vulns4free/2023/02/12/install4j-xxe.html" target="_blank">XXE with Auto-Update in install4j</a>. Update attacks are great since they are usually 0-click. This is a great walkthrough of a Java installer XML External Entity (XXE) attack that reads arbitrary file contents in the PoC.</li>
<li><a href="https://theevilbit.github.io/posts/cve-2022-22655/" target="_blank">CVE-2022-22655 - TCC - Location Services Bypass</a>. I had no idea that location access wasn't part of TCC directly, but rather locationd's responsibility.</li>
<li><a href="https://swarm.ptsecurity.com/binance-smart-chain-token-bridge-hack/" target="_blank">Binance Smart Chain Token Bridge Hack</a>. Ever wanted to steal ~$500,000,000 from the comfort of your own home? Thanks to the magic of smart contracts, you can!</li>
<li><a href="https://www.synacktiv.com/en/publications/exploiting-a-remote-heap-overflow-with-a-custom-tcp-stack.html" target="_blank">Exploiting a remote heap overflow with a custom TCP stack</a>. "The funkiest part was undoubtedly implementing a custom TCP stack to trigger the bug. This is quite uncommon for an user land and real life (as not in a CTF) exploit, and we hope that was entertaining for the reader." It was!</li>
<li><a href="https://the-deniss.github.io/posts/2023/02/09/elevation-of-privileges-from-everyone-through-avast-av-sandbox-to-system-amppl.html" target="_blank">Elevation of privileges from Everyone through Avast Sandbox to System AmPPL (CVE-2021-45335, CVE-2021-45336 and CVE-2021-45337)</a>. Someting about a local privilege escaltion via an anti-virus sandbox just warms my heart. It's red teaming schadenfreude.</li>
<li><a href="https://www.trustedsec.com/blog/azure-ad-kerberos-tickets-pivoting-to-the-cloud/" target="_blank">Azure AD Kerberos Tickets: Pivoting to the Cloud</a>. Domain Admin is cool, but impersonation of any non-MFA account via Azure SSO is cooler.</li>
<li><a href="https://badoption.eu/blog/2023/02/12/S4B_Teams.html" target="_blank">How your messenger used for internal communication might compromise your company</a>. Skype for business. Teams. Lync. Take your pick, get your access.</li>
<li><a href="https://goingbeyondgrep.com/posts/learning-semgrep/" target="_blank">Learning Semgrep</a>. You've seen the power of Semgrep on this blog before, so why not learn it?</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://www.trustedsec.com/blog/teamfiltration-v3-5-0-improve-all-the-things/" target="_blank">TeamFiltration V3.5.0 - Improve All the Things!</a>. Lots of new features and improvements to this cross-platform framework for enumerating, spraying, exfiltrating, and backdooring Office 365 Azure AD accounts.</li>
<li><a href="https://github.com/CCob/ThreadlessInject" target="_blank">ThreadlessInject</a> - Threadless Process Injection using remote function hooking.</li>
<li><a href="https://github.com/blackarrowsec/redteam-research/tree/master/LPE%20via%20StorSvc" target="_blank">LPE via StorSvc</a> - Windows Local Privilege Escalation via StorSvc service (writable SYSTEM path DLL Hijacking).</li>
<li><a href="https://github.com/TheD1rkMtr/FilelessPELoader" target="_blank">FilelessPELoader</a> - Loading Remote AES Encrypted PE in memory, decrypt and run it.</li>
<li><a href="https://github.com/TheD1rkMtr/D1rkSleep" target="_blank">D1rkSleep</a> - Improved version of EKKO by @5pider that Encrypts only Image Sections.</li>
<li><a href="https://github.com/Dec0ne/HWSyscalls" target="_blank">HWSyscalls</a> is a new method to execute indirect syscalls using HWBP, HalosGate and a synthetic trampoline on kernel32 with HWBP.</li>
<li><a href="https://github.com/Brum3ns/firefly" target="_blank">firefly</a> is an advanced black-box fuzzer and not just a standard asset discovery tool. Firefly provides the advantage of testing a target with a large number of built-in checks to detect behaviors in the target.</li>
<li><a href="https://github.com/TheD1rkMtr/UnhookingPatch" target="_blank">UnhookingPatch</a> - Bypass EDR Hooks by patching NT API stub, and resolving SSNs and syscall instructions at runtime.</li>
<li><a href="https://github.com/REDMED-X/OperatorsKit" target="_blank">OperatorsKit</a> - Collection of Beacon Object Files (BOF) for Cobalt Strike.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/cloudflare/wildebeest" target="_blank">wildebeest</a> is an ActivityPub and Mastodon-compatible server.</li>
<li><a href="https://github.com/Orange-Cyberdefense/grepmarx" target="_blank">grepmarx</a> - A source code static analysis platform for AppSec enthusiasts.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 337 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
