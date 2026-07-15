Title: Last Week in Security (LWiS) - 2024-10-28
Date: 2024-10-28 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-10-28
Author: Erik
Summary: Delta Sues Crowdstrike (<a href="https://x.com/CrowdStrike" target="_blank">@CrowdStrike</a>), Jenkins Post-Exploitation (<a href="https://x.com/TrustedSec" target="_blank">@TrustedSec</a>), PE embedded within a PNG (<a href="https://x.com/MalDevAcademy" target="_blank">@MalDevAcademy</a>), Prompt Injection to C2 (<a href="https://x.com/wunderwuzzi23" target="_blank">@wunderwuzzi23</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-10-21 to 2024-10-28.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.reuters.com/legal/delta-sues-crowdstrike-over-software-update-that-prompted-mass-flight-2024-10-25/" target="_blank">Delta sues CrowdStrike over software update that prompted mass flight disruptions</a> - Let the games begin. Do we see in the future of companies like Fortinet/Avanti? "...after a global outage in July caused mass flight cancellations, disrupted travel plans of 1.3 million customers and cost the carrier more than $500 million."</li>
<li><a href="https://security.apple.com/blog/pcc-security-research/" target="_blank">Security research on Private Cloud Compute</a> - Apples new bounty program has a ton of $ possibilities!</li>
<li><a href="https://www.theregister.com/2024/10/23/linus_torvalds_affirms_expulsion_of/" target="_blank">Linus Torvalds affirms expulsion of Russian maintainers</a> - Some maintainers of the Linux kernel have been removed due to their associate with Russia.</li>
<li><a href="https://www.kali.org/blog/end-of-i386-kernel-and-images/" target="_blank">The end of the i386 kernel and images</a> - The i386 architecture has long been obsolete, and from this week, support for i386 in Kali Linux is going to shrink significantly: i386 kernel and images are going away. Images and releases will no longer be created for this platform.</li>
<li><a href="https://www.recordedfuture.com/research/operation-overload-impersonates-media-influence-2024-us-election" target="_blank">Operation Overload Impersonates Media to Influence 2024 US Election</a> - "...Using fake news, fact-checking sites, and AI-generated audio, it seeks to manipulate public opinion by impersonating trusted media organizations."</li>
<li><a href="https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/" target="_blank">Embargo ransomware: Rock’n’Rust</a> - Ransomware group Embargo is testing and deploying a new Rust-based toolkit. The interesting observation here is that differences in deployed versions, bugs, and leftover artifacts suggest that these tools are under active development.</li>
<li><a href="https://mullvad.net/en/blog/introducing-shadowsocks-obfuscation-for-wireguard" target="_blank">Introducing Shadowsocks Obfuscation for WireGuard</a> - Mullvad VPN has introduced Shadowsocks. Shadowsocks is a protocol that obfuscates traffic which aims to make it harder for firewalls to detect and block VPN traffic.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://embracethered.com/blog/posts/2024/claude-computer-use-c2-the-zombais-are-coming/" target="_blank">ZombAIs: From Prompt Injection to C2 with Claude Computer Use</a> - Anthropic released "Claude Computer Use" and this researcher got to work! TLDR - They code execution by asking the prompt to run their sliver agent. Worth noting it's still in BETA as of the day of this LWiS post.</li>
<li><a href="https://blog.smithsecurity.biz/systematic-destruction-hacking-the-scammers-pt.-2" target="_blank">💰Systematic Destruction (Hacking the Scammers pt. 2)</a> - Security researcher is targetting and exploiting those pesky holiday scammers. They were able to find a vulnerability in the scammers custom application.</li>
<li><a href="https://medium.com/@moblig/how-i-accessed-microsofts-servicenow-exposing-all-microsoft-employee-emails-chat-support-5f8d535eb63b" target="_blank">How I Accessed Microsoft’s ServiceNow — Exposing ALL Microsoft Employee emails, Chat Support Transcripts &amp; Attachments</a> - Fun read on how a researcher found a way to access Microsoft's ServiceNow instance, which exposed all Microsoft employee internal email requests, support ticket transcripts, incidents &amp; live agent support chats. No bounty for the researcher though!</li>
<li><a href="https://www.aquasec.com/blog/aws-cdk-risk-exploiting-a-missing-s3-bucket-allowed-account-takeover/" target="_blank">AWS CDK Risk: Exploiting a Missing S3 Bucket Allowed Account Takeover</a> - Wild finding by the Aqua team that affected 1% of the AWS Cloud Development Kit (CDK) users. Disclosure to remediation took around 5 weeks.</li>
<li><a href="https://www.trendmicro.com/en_us/research/24/j/using-grpc-http-2-for-cryptominer-deployment.html" target="_blank">Using gRPC and HTTP/2 for Cryptominer Deployment: An Unconventional Approach</a> - Blog post on how malicious actors are exploiting Docker remote API servers via gRPC/h2c to deploy the cryptominer SRBMiner to facilitate their mining of XRP on Docker hosts.</li>
<li><a href="https://trustedsec.com/blog/offensively-groovy" target="_blank">Offensively Groovy</a> - If you compromise a Jenkins server during one of your engagements, this read is for you. This blog is a good primer into post-exploitation after you've compromised a Jenkins server.</li>
<li><a href="https://doublepulsar.com/burning-zero-days-fortijump-fortimanager-vulnerability-used-by-nation-state-in-espionage-via-msps-c79abec59773" target="_blank">Burning Zero Days: FortiJump FortiManager vulnerability used by nation state in espionage via MSPs</a> - At what point do we stop accepting the risk of exposing these SSL VPNs to the public? At what point do we switch vendors?</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Maldev-Academy/ExecutePeFromPngViaLNK" target="_blank">ExecutePeFromPngViaLNK</a> - Extract and execute a PE embedded within a PNG file using an LNK file.</li>
<li><a href="https://github.com/xaitax/Chrome-App-Bound-Encryption-Decryption" target="_blank">Chrome-App-Bound-Encryption-Decryption</a> - Tool to decrypt App-Bound encrypted keys in Chrome 127+, using the IElevator COM interface with path validation and encryption protections.</li>
<li><a href="https://github.com/FalconOps-Cybersecurity/udpz" target="_blank">udpz</a> - Speedy probe-based UDP service scanner.</li>
<li><a href="https://github.com/deletehead/OctoC2t" target="_blank">OctoC2t</a> - Simple C2 using GitHub repository as comms channel.</li>
<li><a href="https://github.com/0xHossam/KernelCallbackTable-Injection-PoC" target="_blank">KernelCallbackTable-Injection-PoC</a> - Proof of Concept for manipulating the Kernel Callback Table in the Process Environment Block (PEB) to perform process injection and hijack execution flow.</li>
<li><a href="https://github.com/Permiso-io-tools/SkyScalpel" target="_blank">SkyScalpel</a> - SkyScalpel is an open-source framework for JSON policy parsing, obfuscation, deobfuscation, and detection in cloud environments. It provides flexible and highly configurable mechanisms to handle JSON-level obfuscation, IAM policy transformations, and the detection of evasive obfuscation techniques in cloud security contexts.</li>
<li><a href="https://github.com/HulkOperator/AuthStager" target="_blank">AuthStager</a> - AuthStager is a proof-of-concept tool that generates a custom stager shellcode that authenticates to the stager server using an authentication token.</li>
<li><a href="https://github.com/OtterHacker/ShareFouine" target="_blank">ShareFouine</a> - This python script allows you to easily navigate into Sharepoint using UNIX like commands.</li>
<li><a href="https://github.com/CICADA8-Research/TypeLibWalker" target="_blank">TypeLibWalker</a> - This is a new way of persistence on Windows machines using TypeLib. TypeLib persistence technique.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/OpenBAS-Platform/openbas" target="_blank">openbas</a> - Open Breach and Attack Simulation Platform.</li>
<li><a href="https://github.com/p0dalirius/pyLootApacheServerStatus" target="_blank">pyLootApacheServerStatus</a> - A script to automatically dump all URLs present in /server-status to a file locally.</li>
<li><a href="https://github.com/ZephrFish/LOLSearches?ref=blog.zsec.uk" target="_blank">LOLSearches</a> - Living off the land searches for explorer and sharepoint.</li>
<li><a href="https://github.com/p0dalirius/goopts" target="_blank">goopts</a> - goopts, a Go library to parse arguments given in command line to a program.</li>
<li><a href="https://github.com/CCob/DGPOEdit" target="_blank">DGPOEdit</a> - Disconnected GPO Editor - A Group Policy Manager launcher to allow editing of domain GPOs from non-domain joined machines.</li>
<li><a href="https://github.com/marticliment/UniGetUI" target="_blank">UniGetUI</a> - UniGetUI: The Graphical Interface for your package managers. Could be terribly described as a package manager manager to manage your package managers.</li>
<li><a href="https://github.com/Skyvern-AI/skyvern" target="_blank">skyvern</a> - Automate browser-based workflows with LLMs and Computer Vision.</li>
<li><a href="https://starbasedb.com/blog/bindable-microservices-with-cloudflare-workers/" target="_blank">Bindable Microservices with Cloudflare Workers</a> - three files, one command, boom - you have a backend. Cloudflare is magic!</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 439 (+0)</p>
<p>Blogs monitored: 396 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
