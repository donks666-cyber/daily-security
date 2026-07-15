Title: Last Week in Security (LWiS) - 2024-09-30
Date: 2024-09-30 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-09-30
Author: Erik
Summary: CUPS RCE (<a href="https://x.com/evilsocket" target="_blank">@evilsocket</a>), driver vulns (<a href="https://x.com/vinopaljiri" target="_blank">@vinopaljiri</a>), NamelessC2 release (<a href="https://x.com/trickster012" target="_blank">@trickster012</a>), liveness detection bypass (<a href="https://x.com/CaptMeelo" target="_blank">@CaptMeelo</a>), Windows LPE (<a href="https://x.com/ricnar456" target="_blank">@ricnar456</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-09-23 to 2024-09-30.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://specterops.io/specter-bash/" style="color: #3bd267;" target="_blank">Specter Bash 2024</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p>Dare to join us for the ultimate SpecterOps experience! From October 7-10 in Denver, dive into spine-tingling offensive and defensive trainings like our renowned Red Team Operations course and the all-new Identity-driven Offensive Tradecraft course. When night falls, gear up for thrilling evening events with Specters and fellow training participants; it'll be scary-fun!</p>
<p><b>Save 25% on in-person tickets with code</b> <code>LWIS</code>. <a href="https://specterops.io/specter-bash/" style="color: #3bd267;" target="_blank">Secure your spot now!</a></p>
</aside><ul>
<li><a href="https://www.theverge.com/2024/9/30/24258333/hurricane-helene-quartz-chip-mining-north-carolina-spruce-pine" target="_blank">Hurricane Helene barreled through a crucial chip mining area in North Carolina</a> - If you want to make small die chips, it takes ultra-pure quartz, and that primarily comes from just two mines in western North Carolina that were hit hard by Hurricane Helene. Time will tell if the supply chain for quartz is disrupted. The storm also led to <a href="https://bsidesaugusta.org/" target="_blank">BSides Augusta being cancelled</a>.</li>
<li><a href="https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html" target="_blank">Eliminating Memory Safety Vulnerabilities at the Source</a> - Google says memory-safe languages prevent vulnerabilities, and now they have the data to prove it. Better start learning Rust!</li>
<li><a href="https://pages.nist.gov/800-63-4/sp800-63b.html" target="_blank">NIST's second draft of "SP 800-63-4"</a> - "Verifiers and CSPs SHALL NOT require users to change passwords periodically. However, verifiers SHALL force a change if there is evidence of compromise of the authenticator." 🥳</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.evilsocket.net/2024/09/26/Attacking-UNIX-systems-via-CUPS-Part-I/" target="_blank">Attacking UNIX Systems via CUPS, Part I</a> - A CVSS 9.9 caused quite a stir last week. Impressive that this service that listens globally hasn't gotten more attention before now. As it stands the many <a href="https://gist.github.com/stong/c8847ef27910ae344a7b5408d9840ee1" target="_blank">PoCs</a> require the user to print from a malicious printer, but <a href="https://x.com/evilsocket/status/1840437569831481581" target="_blank">there may be ways to exploit this without user interaction</a>. <a href="https://x.com/QuinnyPig/status/1839404608055390634" target="_blank">Ubuntu EC2 instances are affected thanks to snap.</a>. There is a <a href="https://cloud.projectdiscovery.io/?template=CVE-2024-47176" target="_blank">Nuclei template</a> for it as well. The CUPS CVSS 9.9 story is not over yet.</li>
<li><a href="https://research.checkpoint.com/2024/breaking-boundaries-investigating-vulnerable-drivers-and-mitigating-risks/" target="_blank">Breaking Boundaries: Investigating Vulnerable Drivers and Mitigating Risks</a> - Using YARA and VirusTotal's Retrohunt feature, Check Point Research found 1,900 unique signed Windows drivers that probably have a local privilege escalation vulnerability. They checked one by hand an PoC'd the exploit. If you're in need of a CVE, it would seem there are 1,899 drivers just waiting to be exploited.</li>
<li><a href="https://www.synacktiv.com/en/publications/fuzzing-confused-dependencies-with-depfuzzer" target="_blank">Fuzzing confused dependencies with Depfuzzer</a> - "This article explores package registries, the CLI tools used to interact with them, and their underlying mechanisms. We will then introduce <a href="https://github.com/synacktiv/DepFuzzer" target="_blank">DepFuzzer</a>, a tool designed to automate the detection of dependency confusion vulnerabilities in package files."</li>
<li><a href="https://billdemirkapi.me/leveraging-big-data-for-vulnerability-discovery-at-scale/" target="_blank">Secrets and Shadows: Leveraging Big Data for Vulnerability Discovery at Scale</a> - Dangling DNS records and hardcoded secrets are the results of fast-moving cloud service providers and, perhaps, a lack of accountability by the cloud service providers. This post also uses VirusTotal's Rerohunt feature to find secrets over the course of a few years. An impressive amount of domains and secrets were found.</li>
<li><a href="https://bishopfox.com/blog/brokenhill-attack-tool-largelanguagemodels-llm" target="_blank">Broken Hill: A Productionized Greedy Coordinate Gradient Attack Tool for Use Against Large Language Models</a> - More attacks on LLMs from Bishop Fox.</li>
<li><a href="https://www.romainthomas.fr/post/24-09-apple-lockdown-dbi-lifting/#fn:1" target="_blank">Instrumenting an Apple Vision Pro Library with QBDI</a> - Some advanced VisionOS reversing to get a library from the hedset to work on an M-series mac.</li>
<li><a href="https://github.com/google/security-research/blob/master/pocs/linux/kernelctf/CVE-2024-26808_cos/docs/exploit.md" target="_blank">Linux kernel Netfilter Use-After-Free leads to LPE</a> - A Use-After-Free (UAF) in the netfilter component of Linux leads to a privilage escalation. PoC is <a href="https://github.com/google/security-research/tree/master/pocs/linux/kernelctf/CVE-2024-26808_cos/exploit/cos-105-17412.294.36" target="_blank">here</a>.</li>
<li><a href="https://captmeelo.com//talks/research/2024/09/26/rootcon18.html" target="_blank">[ROOTCON 18] Seeing is Not Believing: Bypassing Facial Liveness Detection by Fooling the Sensor</a> - Most facial liveness detection is easily bypassed. With AI on the rise, this will only get easier.</li>
<li><a href="https://labs.lares.com/fear-kerberos-pt4/" target="_blank">Kerberos IV - Delegations</a>  - Fourth part of a Kerberos series. This time, Lares touches on some delegation attacks.</li>
<li><a href="https://media.defense.gov/2024/Sep/25/2003553985/-1/-1/0/CTR-DETECTING-AND-MITIGATING-AD-COMPROMISES.PDF#page8" target="_blank">Detecting and Mitigating Active Directory Compromises</a> - A list of some common exploitation vectors, how to detect them, and how to prevent them. Good write up!</li>
<li><a href="https://0xsultan.github.io/dfir/Xintra-Crash-Dump-Analysis/" target="_blank">Xintra - .NET Crash Dump Analysis</a> - Good walkthrough on DFIR analysis on a .NET crash dump. This is a write-up from Xintra.org training.</li>
<li><a href="https://research.checkpoint.com/2024/10-years-of-dll-hijacking-and-what-we-can-do-to-prevent-10-more/" target="_blank">10 Years of DLL Hijacking, and What We Can Do to Prevent 10 More</a> - References of threat actors abusing DLL hijacks from products of the following vendors: NVIDIA, Microsoft, Oracle, and Citrix. Who's still abusing DLL hijacks on ops?</li>
<li><a href="https://blog.fox-it.com/2024/09/25/red-teaming-in-the-age-of-edr-evasion-of-endpoint-detection-through-malware-virtualisation/" target="_blank">Red Teaming in the age of EDR: Evasion of Endpoint Detection Through Malware Virtualisation</a> - Some say it's the near future of maldev - using a virtualization layer that executes encrypted bytecode sequentially.</li>
<li><a href="https://papermtn.co.uk/probing-slack-workspaces-for-authentication-information-and-other-treats/" target="_blank">Probing Slack Workspaces for Authentication Information and other Treats</a> - Some cool slack tradecraft. Check out the information leaked via unauthenticated means.</li>
<li><a href="https://www.coresecurity.com/core-labs/articles/cve-2024-6769-poisoning-activation-cache-elevate-medium-high-integrity" target="_blank">CVE-2024-6769: Poisoning the Activation Cache to Elevate From Medium to High Integrity</a> - Very detailed write-up on a local privilege escalation in Windows in two parts, from medium integrity to limited high integrity, and then from limited high to full Administrator. <a href="https://github.com/fortra/CVE-2024-6769" target="_blank">CVE-2024-6769</a> is the PoC.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/passtheticket/CVE-2024-38200" target="_blank">CVE-2024-38200</a> - CVE-2024-38200 - Microsoft Office NTLMv2 Disclosure Vulnerability.</li>
<li><a href="https://github.com/Evi1Grey5/Recursive-Loader" target="_blank">Recursive-Loader</a> - Code that was written about a year for a project for vx-underground. However, due to various reasons, the code is being publicly released. tl;dr recursive loader, painful to reverse engineer.</li>
<li><a href="https://github.com/Tylous/FaceDancer" target="_blank">FaceDancer</a> - FaceDancer is an exploitation tool aimed at creating hijackable, proxy-based DLLs by taking advantage of COM-based system DLL image loading.</li>
<li><a href="https://github.com/ChaitanyaHaritash/IllusiveFog" target="_blank">IllusiveFog</a> - Windows Administrator level Implant. (Code looks rough and in PoC format so careful)</li>
<li><a href="https://github.com/trickster0/NamelessC2" target="_blank">NamelessC2</a> - A C2 with all its components written in Rust.</li>
<li><a href="https://posts.specterops.io/ghostwriter-v4-3-sso-json-fields-and-reporting-with-bloodhound-976835a7edba" target="_blank">Ghostwriter v4.3: SSO, JSON Fields, and Reporting with BloodHound</a> - Always nice to see updates to a solid tool.</li>
<li><a href="https://gist.github.com/snovvcrash/caded55a318bbefcb6cc9ee30e82f824" target="_blank">elevator_decrypt_key.cpp</a> - Unprotect the App-Bound Encryption Key via an RPC call to Google Chrome Elevation Service (PoC).</li>
<li><a href="https://lolesxi-project.github.io/LOLESXi/#" target="_blank">Living Off The Land ESXi</a> - List of binaries/scripts natively available in VMware ESXi that adversaries have utilized in their operations.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://androidoffsec.withgoogle.com/posts/binder-internals/" target="_blank">Binder Internals</a> - Solid primer. The post discusses the inner workings of Android's Binder IPC system.</li>
<li><a href="https://samcurry.net/hacking-kia" target="_blank">Hacking Kia: Remotely Controlling Cars With Just a License Plate</a> - "...allowed remote control over key functions using only a license plate." 🤯</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 438 (+0)</p>
<p>Blogs monitored: 395 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
