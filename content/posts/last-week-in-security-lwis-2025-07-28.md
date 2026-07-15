Title: Last Week in Security (LWiS) - 2025-07-28
Date: 2025-07-28 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-07-28
Author: Erik
Summary: VMware Tools LPE (<a href="https://x.com/justbronzebee" target="_blank">@justbronzebee</a>), Adaptix C2 0.7 (<a href="https://x.com/hacker_ralf" target="_blank">@hacker_ralf</a>), Ludus MCP (<a href="https://x.com/__Mastadon" target="_blank">@__Mastadon</a>), SOAP(y) (<a href="https://x.com/_logangoins" target="_blank">@_logangoins</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-07-21 to 2025-07-28.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://aws.amazon.com/security/security-bulletins/rss/aws-2025-015/" target="_blank">Security Update for Amazon Q Developer Extension for Visual Studio Code (Version #1.84)</a> - The Amazon Q extension for Visual Studio Code was hacked, sorry, had a "potentially unapproved code modification" that attempted to use a large langue model prompt to run a kind of AI-generated wiper. While Amazon said no end users were affected, it did attempt to run on at least <a href="https://bsky.app/profile/quinnypig.com/post/3luogum3g6s2i" target="_blank">one end users machine</a>.</li>
<li><a href="https://githubnext.com/projects/github-spark" target="_blank">GitHub Spark</a> - Are "micro apps" coded with natural language and AI going to be the next big "app?" Google has an "experiment" called <a href="https://opal.withgoogle.com/landing/" target="_blank">Opal</a> that is very similar. It's also interesting that both Google's Opal announcement and Amazon's <a href="https://kiro.dev/blog/introducing-kiro/" target="_blank">Kiro</a> introduction blog post both pushed Discord as the place to get help and provide feedback. To me, this shows these tools are aimed at a younger audience.</li>
<li><a href="https://www.theguardian.com/technology/2025/jul/24/what-are-the-new-uk-online-safety-rules-and-how-will-they-be-enforced" target="_blank">What are the new UK online safety rules and how will age checks on adult content be enforced?</a> - The UK is now enforcing age verification with the familiar cry of "protect the children." Pressure against this may work, as the <a href="https://www.theverge.com/news/710504/uk-apple-encryption-back-door-icloud-adp-backing-down" target="_blank">UK wants to weasel out of demand for Apple encryption back door</a> following backlash. The "online safety rules" will impact large platforms like Facebook, TikTok, and even <a href="https://www.telegraph.co.uk/business/2025/07/23/wikipedia-threatens-limit-access-website-britain/" target="_blank">Wikipedia</a>. It's not like having every site implement its own age verification system could lead to serious privacy breaches...</li>
<li><a href="https://techcrunch.com/2025/07/26/dating-safety-app-tea-breached-exposing-72000-user-images/" target="_blank">Dating safety app Tea breached, exposing 72,000 user images</a> - An app that required users to verify their identity left their Firebase database publicly exposed. Calling this a "hack" or "breach" is a bit of an exaggeration as it's more like putting all the data in a pile in the woods hoping no one would find it; no security, just a location they thought would be hard to find.</li>
<li><a href="https://www.theregister.com/2025/07/23/vmware_patch_download_problems/" target="_blank">VMware prevents some perpetual license holders from downloading patches</a> - Broadcom continues to trash the VMware brand, focused on only the largest customers, to the determent of all others.</li>
<li><a href="https://arxiv.org/html/2507.12869v1" target="_blank">WhoFi: Deep Person Re-Identification via Wi-Fi Channel Signal Encoding</a> - You can now track individuals via Wi-Fi signal reflections from human bodies which create unique biometric signatures. Spooky! 👻</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://specterops.io/blog/2025/07/24/escaping-the-confines-of-port-445-ntlm-relay/" target="_blank">Escaping the Confines of Port 445</a> - Using Service Control Manager (SCM) to start Webclient service can provide operators with some lateral movement techniques. Don't forget to keep this in your opnotes as you're introducing a configuration change into the clients environment.</li>
<li><a href="https://swarm.ptsecurity.com/the-guest-who-could-exploiting-lpe-in-vmware-tools/" target="_blank">The Guest Who Could: Exploiting LPE in VMWare Tools</a> - The use of predictable pipe names and the lack of <cite>FILE_FLAG_FIRST_PIPE_INSTANCE</cite> which will fail if the pipe already exists means an attacker can create the vmware tools pipe with their own permission set before the SYSTEM level service. This eventually leads to local privilege escalation via arbitrary file write.</li>
<li><a href="https://rastamouse.me/debugging-the-tradecraft-garden/" target="_blank">Debugging the Tradecraft Garden</a> - Rasta Mouse continues his exploration of the Tradecraft Garden, this time making it a little easier to write and debug on Windows.</li>
<li><a href="https://specterops.io/blog/2025/07/25/make-sure-to-use-soapy-an-operators-guide-to-stealthy-ad-collection-using-adws/" target="_blank">Make Sure to Use SOAP(y) – An Operators Guide to Stealthy AD Collection Using ADWS</a> - Microsoft introduced Active Directory Web Services (ADWS) is a web interface enabled by default on domain controllers. <a href="https://github.com/logangoins/soapy" target="_blank">SoaPy</a> - can be used to interact with and dump ADWS from a Linux host. This post has another <a href="https://ludus.cloud" target="_blank">Ludus</a> domain spotted in the wild! 😊</li>
<li><a href="https://labs.watchtowr.com/stack-overflows-heap-overflows-and-existential-dread-sonicwall-sma100-cve-2025-40596-cve-2025-40597-and-cve-2025-40598/" target="_blank">Stack Overflows, Heap Overflows, and Existential Dread (SonicWall SMA100 CVE-2025-40596, CVE-2025-40597 and CVE-2025-40598)</a> - "It’s 2025, and at this point, we’re convinced there’s a secret industry-wide pledge: every network appliance must include at least one trivially avoidable HTTP header parsing bug - preferably pre-auth. Bonus points if it involves sscanf."</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/NocteDefensor/LudusMCP" target="_blank">LudusMCP</a> - Model Context Protocol server for managing <a href="https://ludus.cloud" target="_blank">Ludus</a> lab environments through natural language commands.</li>
<li><a href="https://github.com/rehosting/penguin" target="_blank">penguin</a> - PENGUIN (Personalized EmulatioN Generated Using Instrumented Analysis) takes a target centric approach to rehosting using a precise and tailored specification of the rehosting process. [The description is underselling this tool, you can take arbitrary embedded firmware and get it up and running in an emulator with two commands.]</li>
<li><a href="https://x.com/SkelSec/status/1946218349324603774" target="_blank">[X] Any domain user can BSOD a 2025 Domain Controller</a> - "This does not meet Microsoft's bar for immediate servicing." 🫠</li>
<li><a href="https://adaptix-framework.gitbook.io/adaptix-framework/changelog-and-updates/v0.6-greater-than-v0.7" target="_blank">AdaptixC2 v0.7</a> - My current favorite open-source C2 got a new release, and v0.7 brings a scripting language to allow programatic control of the C2!</li>
<li><a href="https://github.com/hybryx/mistwalker" target="_blank">Mistwalker</a> - Create Entra Global Admin accounts from On-Prem.</li>
<li><a href="https://github.com/klezVirus/RAIWhateverTrigger" target="_blank">RAIWhateverTrigger</a> - Local SYSTEM auth trigger for relaying - X.</li>
<li><a href="https://github.com/grayhatkiller/wambam-bof" target="_blank">wambam-bof</a> - A Cobalt Strike BOF that extracts access tokens from .tbres files. This BOF locates DPAPI-encrypted blobs stored in .tbres files, decrypts them in the current user context using CryptUnprotectData, and extracts the access token. This BOF is opsec safe and could be used as an alternate to office_tokens BOF.</li>
<li><a href="https://github.com/awgh/ratnet-rs" target="_blank">ratnet-rs</a> - Rust port of RatNet, an anonymity network designed for mesh routing and embedded scenarios.</li>
<li><a href="https://github.com/rasta-mouse/Crystal-Loaders" target="_blank">Crystal-Loaders</a> - A small collection of Crystal Palace PIC loaders designed for use with Cobalt Strike.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/whokilleddb/sinister-vsix" target="_blank">sinister-vsix</a> - Blog/Journal on how to backdoor VSCode extensions.</li>
<li><a href="https://github.com/wariv/DarkLnk" target="_blank">DarkLnk</a> - Build sneaky &amp; malicious LNK files.</li>
<li><a href="https://github.com/fastrepl/hyprnote" target="_blank">hyprnote</a> - Local-first AI Notepad for Private Meetings.</li>
<li><a href="https://github.com/czhu12/canine" target="_blank">canine</a> - Power of Kubernetes, Simplicity of Heroku.</li>
<li><a href="https://github.com/9001/copyparty" target="_blank">copyparty</a> - Portable file server with accelerated resumable uploads, dedup, WebDAV, FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file, no deps.</li>
<li><a href="https://github.com/dacort/s3grep" target="_blank">s3grep</a> - CLI tool for searching logs and unstructured content in Amazon S3 buckets.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 455 (+0)</p>
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
