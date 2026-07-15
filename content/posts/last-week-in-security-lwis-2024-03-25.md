Title: Last Week in Security (LWiS) - 2024-03-25
Date: 2024-03-25 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-03-25
Author: Erik
Summary: CI/CD attacks (<a href="https://twitter.com/bishopfox" target="_blank">@bishopfox</a>), IdP pwnage (<a href="https://twitter.com/_xpn_" target="_blank">@_xpn_</a>), on-prem exchange attacks (<a href="https://twitter.com/Jonas_B_K" target="_blank">@Jonas_B_K</a>), Windows privesc (<a href="https://twitter.com/p1k4l4" target="_blank">@p1k4l4</a>), SCCM in GOAD (<a href="https://twitter.com/M4yFly" target="_blank">@M4yFly</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-03-18 to 2024-03-25.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.elastic.co/security-labs/unveiling-malware-behavior-trends" target="_blank">Unveiling malware behavior trends</a> - Analyzing a Windows dataset of over 100,000 malicious files by Elastic Security Labs.</li>
<li><a href="https://www.mdsec.co.uk/2024/03/introducing-star-fs/" target="_blank">Introducing STAR-FS</a> The Bank of England announced the introduction of a new regulatory framework, STAR-FS, to support the financial sector in its cyber resilience operations.</li>
<li><a href="https://gofetch.fail/" target="_blank">GoFetch</a> - A new vulnerability baked into Apple's M-series of chips that allows attackers (and/or userspace applications) to extract secret keys from Macs. It looks like there are mitigation flags that can be set to mitigate this for sensitive cryptographic calls. Time will tell if they are effective/implemented.</li>
<li><a href="https://www.theverge.com/2024/3/21/24107659/apple-doj-lawsuit-antitrust-documents-suing?ref=selfh.st" target="_blank">The US Department of Justice is suing Apple — read the full lawsuit here</a> - Will this lead to a more open iOS? Maybe, but it will be years before anything (if anything) changes.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://eversinc33.com/posts/anti-anti-rootkit-part-i/" target="_blank">(Anti-)Anti-Rootkit Techniques - Part I: UnKovering mapped rootkits</a> - Part I of a series, that will showcase various anti-rootkit techniques, known through anti-rootkits or anti-cheats, and their implementations in <a href="https://github.com/eversinc33/unKover" target="_blank">unKover</a>.</li>
<li><a href="https://sillywa.re/posts/flower-da-flowin-shc/" target="_blank">naively bypassing new memory scanning POCs</a> - This blog focuses on in-memory evasion from both offensive and defensive angles, and introduces a simple but effective method to avoid detection by leveraging behaviors similar to legitimate JIT (Just-In-Time) compilation processes</li>
<li><a href="https://bishopfox.com/blog/poisoned-pipeline-attack-execution-a-look-at-ci-cd-environments" target="_blank">Poisoned Pipeline Execution Attacks: A Look at CI-CD Environments</a> - This attack vector is 🔥. Internal red teams: Add supply chain to your existing red team roadmap if you haven't already.</li>
<li><a href="https://blog.xpnsec.com/identity-providers-redteamers/" target="_blank">Identity Providers for RedTeamers</a> - A look at popular cloud-based Identify Providers and their attack primitives. Awesome work by Adam Chester of (now) SpecterOps. Very practical to modern operations against SaaS/Remote friendly companies.</li>
<li><a href="https://fin3ss3g0d.net/index.php/2024/03/18/weaponizing-windows-thread-pool-apis-proxying-dll-loads/" target="_blank">Weaponizing Windows Thread Pool APIs: Proxying DLL Loads Using I/O Completion Callbacks</a> - Proxying DLL loads using the Windows thread pool API with C++/assembly.</li>
<li><a href="https://rhinosecuritylabs.com/research/cve-2024-1212unauthenticated-command-injection-in-progress-kemp-loadmaster/" target="_blank">CVE-2024-1212: Unauthenticated Command Injection - In Progress Kemp LoadMaster</a> - Write-up on the Progress Kemp LoadMaster load balancer Unauthenticated command injection vulnerability. A bash script that calls a binary that runs shell commands with <cite>system</cite>, what could go wrong?</li>
<li><a href="https://www.wiz.io/blog/introducing-namespacehound-for-cross-tenant-violation-assessments" target="_blank">NamespaceHound: protecting multi-tenant K8s clusters</a> - Open-source tool for detecting the risk of potential namespace crossing violations and anonymous access opportunities in multi-tenant clusters. <a href="https://github.com/wiz-sec-public/namespacehound/" target="_blank">NamespaceHound</a> is the tool.</li>
<li><a href="https://labs.lares.com/fear-kerberos-pt1/" target="_blank">Kerberos I - Overview</a> - Every attackers friend, kerberos. This start of a series on the topic.</li>
<li><a href="https://trustedsec.com/blog/from-error-to-entry-cracking-the-code-of-password-spraying-tools" target="_blank">From Error to Entry: Cracking the Code of Password-Spraying Tools</a> - An analysis of the current password spraying tooling and limitations in the error codes they handle. Good reminder for tool authors!</li>
<li><a href="https://www.akamai.com/blog/security-research/abusing-dhcp-administrators-group-for-privilege-escalation-in-windows-domains" target="_blank">Abusing the DHCP Administrators Group to Escalate Privileges in Windows Domains</a> - DHCP Administrator to DA under certain conditions.</li>
<li><a href="https://badoption.eu/blog/2024/03/23/cortex.html" target="_blank">Deactivating Cortex XDR via repair function</a> - Without tamper protection its trivial to deactivate Cortex.</li>
<li><a href="https://mayfly277.github.io/posts/SCCM-LAB-part0x0/" target="_blank">SCCM / MECM LAB - Part 0x0</a> - An SCCM lab lands in the GOAD universe. A great resource, but you are locked into the rigid setup of GOAD.</li>
<li><a href="https://raesene.github.io/blog/2024/03/24/Using-Tailscale-for-persistence/" target="_blank">Using Tailscale for persistence</a> - Some great <a href="https://www.youtube.com/watch?v=9qM2m1LZuVo" target="_blank">traitorware</a>!</li>
<li><a href="https://blog.trailofbits.com/2024/03/19/read-code-like-a-pro-with-our-weaudit-vscode-extension/" target="_blank">Read code like a pro with our weAudit VSCode extension</a> - <a href="https://github.com/trailofbits/vscode-weaudit" target="_blank">vscode-weaudit</a> is the new VSCode extension from the code auditing pros at Trial of Bits.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/MzHmO/WhoIsWho" target="_blank">WhoIsWho</a> - Alternatives to the command whoami</li>
<li><a href="https://github.com/SaadAhla/dropper" target="_blank">dropper</a>-  Project that generates Malicious Office Macro Enabled Dropper for DLL SideLoading and Embed it in Lnk file to bypass MOTW</li>
<li><a href="https://github.com/mrexodia/perfect-dll-proxy" target="_blank">Perfect DLL Proxy</a> -  Perfect DLL Proxying using forwards with absolute paths. [I'm partial to <a href="https://github.com/sadreck/Spartacus" target="_blank">Spartacus</a>]</li>
<li><a href="https://github.com/RedSiege/Jigsaw" target="_blank">Jigsaw</a> - Hide shellcode by shuffling bytes into a random array and reconstruct at runtime</li>
<li><a href="https://github.com/fin3ss3g0d/IoDllProxyLoad" target="_blank">IoDllProxyLoad</a> - DLL proxy load example using the Windows thread pool API, I/O completion callback with named pipes, and C++/assembly</li>
<li><a href="https://code.europa.eu/ec-digit-s2/opentide" target="_blank">OpenTIDE</a> - Open Threat Informed Detection Engineering is the European Commission DIGIT.S2 (Security Operations) open source initiative to build a rich ecosystem of tooling and data supporting Cyber Threat Detections.</li>
<li><a href="https://github.com/codewhitesec/HttpRemotingObjRefLeak" target="_blank">HttpRemotingObjRefLeak</a> - Additional resources for leaking and exploiting ObjRefs via HTTP .NET Remoting <a href="https://code-white.com/blog/leaking-objrefs-to-exploit-http-dotnet-remoting/" target="_blank">CVE-2024-29059</a>.</li>
<li><a href="https://posts.specterops.io/pwned-by-the-mail-carrier-0750edfad43b" target="_blank">Pwned by the Mail Carrier</a> - Compromising exchange with some defensive guidance on adjusting ACEs to limit Exchange's AD permissions and establishing security boundaries for Tier Zero assets. Jonas is on a tear lately.</li>
<li><a href="https://github.com/Kudaes/ADPT" target="_blank">Another Dll Proxying Tool</a> - DLL proxying for lazy people</li>
<li><a href="https://github.com/nbaertsch/nimvoke" target="_blank">nimvoke</a> - Indirect syscalls + DInvoke made simple.</li>
<li><a href="https://github.com/AdnaneKhan/ActionsCacheBlasting" target="_blank">ActionsCacheBlasting</a> - Proof-of-concept code for research into GitHub Actions Cache poisoning.</li>
<li><a href="https://github.com/Nassim-Asrir/CVE-2023-36424" target="_blank">CVE-2023-36424</a> - Windows Kernel Pool (clfs.sys) Corruption Privilege Escalation.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/SpecterOps/presentations/tree/master/SO-CON%202024" target="_blank">SO-CON 2024</a> - SO-CON 2024 presentations released. Videos coming soon!</li>
<li><a href="https://stackshare.io/posts/top-developer-tools-2023" target="_blank">The Top 100+ Developer Tools 2023</a> - Looking for a research target inspiration? "This year we analyzed well over 12 million data points shared by you - the StackShare community - to bring you these rankings."</li>
<li><a href="https://github.com/stitionai/devika" target="_blank">Devika</a> - Devika is an Agentic AI Software Engineer that can understand high-level human instructions, break them down into steps, research relevant information, and write code to achieve the given objective. Devika aims to be a competitive open-source alternative to Devin by Cognition AI.</li>
<li><a href="https://jasonppy.github.io/VoiceCraft_web/" target="_blank">VoiceCraft: Zero-Shot Speech Editing and Text-to-Speech in the Wild</a> - VoiceCraft is a token infilling neural codec language model, that achieves state-of-the-art performance on both speech editing and zero-shot text-to-speech (TTS) on in-the-wild data including audiobooks, internet videos, and podcasts. The model weights aren't out yet but should be by the end of the month. This is going to make vishing deadly.</li>
<li><a href="https://github.com/hrishioa/lumentis" target="_blank">lumentis</a> - AI powered one-click comprehensive docs from transcripts and text.</li>
<li><a href="https://github.com/RedefiningReality/Cobalt-Strike" target="_blank">Cobalt Strike Resources</a> - Various resources to enhance Cobalt Strike's functionality and its ability to evade antivirus/EDR detection.</li>
<li><a href="https://github.com/chainguard-dev/bincapz" target="_blank">bincapz</a> - Enumerate binary capabilities, including malicious behaviors.</li>
<li><a href="https://victoronsoftware.com/posts/mtls-go-client-windows-certificate-store/" target="_blank">Mutual TLS (mTLS) Go client</a> - How to build an mTLS Go client that uses the Windows certificate store.</li>
<li><a href="https://github.com/ElliotKillick/windows-vs-linux-loader-architecture" target="_blank">Windows vs Linux Loader Architecture</a> - Side-by-side comparison of the Windows and Linux (GNU) Loaders.</li>
<li><a href="https://github.com/d60/twikit" target="_blank">Twikit</a> - Simple API wrapper to interact with twitter's unofficial API. You can log in to Twitter using your account username, email address and password and use most features on Twitter, such as posting and retrieving tweets, liking and following users. Curious on how long this will last.</li>
<li><a href="https://github.com/TracecatHQ/tracecat?tab=readme-ov-file" target="_blank">tracecat</a> - 😼 The AI-native, open source alternative to Tines / Splunk SOAR.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 374 (+3)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
