Title: Last Week in Security (LWiS) - 2025-08-25
Date: 2025-08-25 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-08-25
Author: Erik
Summary: WebClient deep dive (<a href="https://x.com/0xthirteen" target="_blank">@0xthirteen</a>), 2x RCE chains in Commvault (<a href="https://x.com/chudyPB" target="_blank">@chudyPB</a>), how to rob a hotel (<a href="https://x.com/dmcxblue" target="_blank">@dmcxblue</a>), MSI patch/protocol handler RCE (<a href="https://x.com/johnnyspandex" target="_blank">@johnnyspandex</a>), self-relaying (<a href="https://x.com/_logangoins" target="_blank">@_logangoins</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-08-18 to 2025-08-25.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://marektoth.com/blog/dom-based-extension-clickjacking/" target="_blank">DOM-based Extension Clickjacking: Your Password Manager Data at Risk</a> - As password manager adoption grows, so does the value in finding ways to trick them into giving up credentials. Hardware tokens are the best defense, followed by a password manager and a separate 2nd factor app on your mobile device. Much less convenient, much more secure.</li>
<li><a href="https://www.reuters.com/business/meta-signs-over-10-billion-cloud-deal-with-google-source-says-2025-08-21/" target="_blank">Meta signs over $10 billion cloud deal with Google, source says</a> - Are Google's in-house AI chips (Tensor Processing Units - TPUs) the shovels of the AI era?</li>
<li><a href="https://www.intc.com/news-events/press-releases/detail/1748/intel-and-trump-administration-reach-historic-agreement-to" target="_blank">Intel and Trump Administration Reach Historic Agreement to Accelerate American Technology and Manufacturing Leadership</a> - The $10 billion USD deal is roughly equivalent to the cost to the US government of the General Motors bailout (2009-2013), except there is no (current) global economic crisis and this deal is not to save 100,000+ jobs. Is the only US company with a hope of creating advanced semiconductor manufacturing domestically "too big to fail?"</li>
<li><a href="https://www.reuters.com/technology/russia-orders-state-backed-max-messenger-app-whatsapp-rival-pre-installed-phones-2025-08-21/" target="_blank">Russia orders state-backed MAX messenger app, a WhatsApp rival, pre-installed on phones and tablets</a> - WhatsApp calls are experiencing extreme packet loss in Russia, likely in an effort to push users to MAX.</li>
<li><a href="https://www.rrauction.com/jim-sanborn-kryptos-k4-solution-auction/" target="_blank">Kryptos K4: The Solution Auction</a> - If you are unfamiliar with Kryptos, <a href="https://youtube.com/watch?v=jVpsLMCIB0Y" target="_blank">this documentary</a> is a must watch and the channel for the past 8 years has been exceptional. Now you can be the 2nd person ever to know the solution of Kryptos K4, for the right price that is.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://specterops.io/blog/2025/08/19/will-webclient-start/" target="_blank">Will WebClient Start</a> - Everyone's favorite service to use in an NTLM relay, but can you start it as a low privileged user? No is the answer, but the investigation into the WebClient service was very well done. The signature red background of a <a href="https://ludus.cloud" target="_blank">Ludus</a> lab can be seen in the EFS properties screenshot. 😊</li>
<li><a href="https://specterops.io/blog/2025/08/22/operating-outside-the-box-ntlm-relaying-low-privilege-http-auth-to-ldap/" target="_blank">Operating Outside the Box: NTLM Relaying Low-Privilege HTTP Auth to LDAP</a> - Speaking of relaying, this is a neat trick to "self-relay" in order to get an authenticated LDAP session with a domain controller. Again, love to see <a href="https://ludus.cloud" target="_blank">Ludus</a> empowering researchers. 😊</li>
<li><a href="https://securitylabs.datadoghq.com/articles/enumerating-aws-the-quiet-way-cloudtrail-free-discovery-with-resource-explorer/" target="_blank">Enumerating AWS the quiet way: CloudTrail-free discovery with Resource Explorer</a> - Attackers always take a risk when enumerating permissions of AWS tokens if those actions log in CloudTrail, as the simple act of enumeration may trigger a detection. Thus, if there is a way to enumerate permissions without any CloudTrail logs, attackers can gain information without notifying defenders. As of July 2025, <cite>resource-explorer-2:ListResources</cite> now logs to CloudTrail by default.</li>
<li><a href="https://labs.watchtowr.com/guess-who-would-be-stupid-enough-to-rob-the-same-vault-twice-pre-auth-rce-chains-in-commvault/" target="_blank">Guess Who Would Be Stupid Enough To Rob The Same Vault Twice? Pre-Auth RCE Chains in Commvault</a> - Four CVEs across two pre-auth RCE chains for a Data Protection or Cyber Resilience solution. Ouch.</li>
<li><a href="https://dmcxblue.net/2025/08/23/how-to-rob-a-hotel/" target="_blank">How to Rob a Hotel</a> - These end-to-end walkthroughs are rare, and make me yearn for the write ups of <a href="https://theanarchistlibrary.org/category/author/phineas-fisher" target="_blank">Phineas Fisher</a>.</li>
<li><a href="https://blog.amberwolf.com/blog/2025/august/delinea-protocol-handler---msi-strikes-back/" target="_blank">Delinea Protocol Handler - MSI Strikes Back</a> - These protocol handler attacks could be an amazing initial access vector if you were confident your target organization uses the software. The patch trick for misexec is evergreen, stash that away.</li>
<li><a href="https://www.hexacorn.com/blog/2025/08/19/dll-forwardsideloading/" target="_blank">DLL ForwardSideloading</a> - You've gotta love when built in Windows binaries are susceptible to a form of DLL sideloading. I could see this being used in both droppers and persistence mechanisms to obfuscate the execution trace of a tool.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/NetPenguins/ludus_k3s" target="_blank">ludus_k3s</a> - Role for creating a k3s cluster in <a href="https://ludus.cloud" target="_blank">Ludus</a>.</li>
<li><a href="https://github.com/professor-moody/ludus_litterbox_role" target="_blank">ludus_litterbox_role</a> - A role for deploying <a href="https://github.com/BlackSnufkin/LitterBox" target="_blank">LitterBox</a> - a comprehensive malware analysis sandbox - on Windows systems within <a href="https://ludus.cloud" target="_blank">Ludus</a> lab environments.</li>
<li><a href="https://github.com/chompie1337/PhrackCTF" target="_blank">PhrackCTF</a> - Binary Exploitation Phrack CTF Challenge.</li>
<li><a href="https://github.com/clearbluejar/pyghidra-mcp" target="_blank">pyghidra-mcp</a> - Python Command-Line Ghidra MCP.</li>
<li><a href="https://github.com/evilsocket/legba/releases/tag/1.1.0" target="_blank">legba 1.1.0</a> - A multiprotocol credentials bruteforcer / password sprayer and enumerator. 🥷. The 1.1.0 release brings a ton of improvements!</li>
<li><a href="https://github.com/MorDavid/vCenterHound" target="_blank">vCenterHound</a> - Collect infrastructure and permissions data from vCenter and export it as a BloodHound‑compatible graph using Custom Nodes/Edges.</li>
<li><a href="https://github.com/print3M/dllshimmer" target="_blank">DllShimmer</a> - Weaponize DLL hijacking easily. Backdoor any function in any DLL.</li>
<li><a href="https://github.com/2x7EQ13/CreateProcessAsPPL" target="_blank">CreateProcessAsPPL</a> - This is the loader that supports running a program with Protected Process Light (PPL) protection functionality.</li>
<li><a href="https://github.com/kleiton0x00/RtlHijack" target="_blank">RtlHijack</a> - Alternative Read and Write primitives using Rtl* functions the unintended way.</li>
<li><a href="https://github.com/dirkjanm/DeviceToken" target="_blank">DeviceToken</a> - Request device ticket/token using the device's MSA.</li>
<li><a href="https://github.com/p0dalirius/bhopengraph" target="_blank">bhopengraph</a> - A python library to create BloodHound OpenGraphs.</li>
<li><a href="https://github.com/0xJs/BlockEDRTraffic" target="_blank">BlockEDRTraffic</a> - Two tools written in C that block network traffic for blacklisted EDR processes, using either Windows Defender Firewall (WDF) or Windows Filtering Platform (WFP).</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/MorDavid/BruteForceai" target="_blank">BruteForceAI</a> - Advanced LLM-powered brute-force tool combining AI intelligence with automated login attacks.</li>
<li><a href="https://github.com/netspi/ateam" target="_blank">ATEAM</a> - A Python reconnaissance tool designed to discover Azure services and attribute tenant ownership information based on their responses.</li>
<li><a href="https://lock.cmpxchg8b.com/anubis.html" target="_blank">Hey… quick question, why are anime catgirls blocking my access to the Linux kernel?</a> - In the cat and mouse game of bot defense, Anubis is but a minor annoyance for bot operators.</li>
<li><a href="https://github.com/google/facade" target="_blank">facade</a> is an enterprise-security anomaly detection system developed by Google. It is a high-precision deep-learning-based machine learning system used in a number of applications across Google. It is used as a last line of defense against insider threats, as an ACL recommendation system, and as a way to detect account compromise.</li>
<li><a href="https://github.com/arosenmund/defcon33_silence_kill_edr" target="_blank">defcon33_silence_kill_edr</a> - A workshop from DEF CON 33 on how to silence and kill EDRs.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 456 (+1)</p>
<p>Blogs monitored: 424 (+0)</p>
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
