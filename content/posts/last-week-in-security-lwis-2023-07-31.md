Title: Last Week in Security (LWiS) - 2023-07-31
Date: 2023-07-31 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-07-31
Author: Erik
Summary: Citrix ADC RCE (<a href="https://twitter.com/assetnote" target="_blank">@assetnote</a> + <a href="https://twitter.com/bishopfox" target="_blank">@bishopfox</a>), Zenbleed (<a href="https://twitter.com/taviso" target="_blank">@taviso</a>), coolest hack of the year [CVE-2023-38408] (<a href="https://twitter.com/qualys" target="_blank">@qualys</a>), AWS CNI for k8s abuse (<a href="https://twitter.com/BerneCampbell" target="_blank">@BerneCampbell</a>), WebKit exploitation (<a href="https://twitter.com/typeconfuser" target="_blank">@typeconfuser</a> + <a href="https://twitter.com/sherl0ck__" target="_blank">@sherl0ck__</a>), CS2BR (<a href="https://twitter.com/MoritzLThomas" target="_blank">@MoritzLThomas</a>), Mockingjay PoC (<a href="https://twitter.com/dottor_morte" target="_blank">@dottor_morte</a>), LPE via installers (<a href="https://twitter.com/AndrewOliveau" target="_blank">@AndrewOliveau</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-07-17 to 2023-07-31.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><p>Citrix ADC and NetScaler Gateway RCE (CVE-2023-3519)</p>
<blockquote>
<ul>
<li><a href="https://blog.assetnote.io/2023/07/21/citrix-CVE-2023-3519-analysis/" target="_blank">Analysis of CVE-2023-3519 in Citrix ADC and NetScaler Gateway</a>  and <a href="https://blog.assetnote.io/2023/07/24/citrix-rce-part-2-cve-2023-3519/" target="_blank">Part 2</a>.</li>
<li><a href="https://bishopfox.com/blog/citrix-adc-gateway-rce-cve-2023-3519" target="_blank">53% of them are unpatched</a>. Bishop Fox has the best breakdown of the vulnerability landscape.</li>
</ul>
</blockquote>
</li>
<li><p><a href="https://www.cobaltstrike.com/blog/cobalt-strike-and-outflank-friends-evasive-places/" target="_blank">Cobalt Strike and Outflank Security Tooling: Friends in Evasive Places</a>. I like the idea of a base, stable tool and then a service to make it more useful (i.e. less detectable). However, if this service is as popular as Cobalt Strike itself, won't it be a target for EDR? I wonder if OST subscriptions will be more limited than Cobalt Strike licenses.</p>
</li>
<li><p><a href="https://www.vice.com/en/article/4a3n3j/backdoor-in-police-radios-tetra-burst" target="_blank">Researchers Find 'Backdoor' in Encrypted Police and Military Radios</a>. Who would have thought a closed source encryption scheme from the 90's was vulnerable?</p>
</li>
<li><p><a href="https://www.sentinelone.com/labs/jumpcloud-intrusion-attacker-infrastructure-links-compromise-to-north-korean-apt-activity/" target="_blank">JumpCloud Intrusion | Attacker Infrastructure Links Compromise to North Korean APT Activity</a>. Bad day when your SSO/Identity provider is hacked. As we move to the cloud the companies are usually more secure then on-prem, but the blast radius of a succssful hack is huge.</p>
</li>
<li><p><a href="https://krebsonsecurity.com/2023/07/russia-sends-cybersecurity-ceo-to-jail-for-14-years/" target="_blank">Russia Sends Cybersecurity CEO to Jail for 14 Years</a>. In Soviet Russia, anti-crime sends you to jail. Not the first case of defenders being jailed in Russia with no public evidence either.</p>
</li>
<li><p><a href="https://cyble.com/blog/threat-actor-targeting-developers-via-trojanized-ms-visual-studio/" target="_blank">Threat Actor Targeting Developers via Trojanized MS Visual Studio</a>. Reminds me of <a href="https://en.wikipedia.org/wiki/XcodeGhost" target="_blank">XcodeGhost</a>.</p>
</li>
<li><p><a href="https://blog.isosceles.com/the-legacy-of-stagefright/" target="_blank">The Legacy of Stagefright</a>. Not often do we look back at the legacy of a bug.</p>
</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.elttam.com/blog/amazon-vpc-cni/#content" target="_blank">Abusing Amazon VPC CNI plugin for Kubernetes</a>. "By abusing the privileges of the Amazon VPC CNI plugin, it's possible for workloads to manipulate the networking of other unrelated EC2 instances. This can be leveraged by an attacker with a foothold in an EKS cluster to access and attack other instances living in other VPCs."</li>
<li><a href="https://blog.exodusintel.com/2023/07/20/shifting-boundaries-exploiting-an-integer-overflow-in-apple-safari/" target="_blank">Shifting boundaries: Exploiting an Integer Overflow in Apple Safari</a>. A detailed look at a 2020 WebKit vulnerability and exploitation.</li>
<li><a href="https://maia.crimew.gay/posts/fuckstalkerware-2/" target="_blank">#FuckStalkerware pt. 2 - SpyHide couldnt hide forever</a>. It's not often people write about their actual hacks (not bug bounty). Makes me miss <a href="https://www.vice.com/en/article/3k9zzk/hacking-team-hacker-phineas-fisher-has-gotten-away-with-it" target="_blank">Phineas Fisher</a>.</li>
<li><a href="https://blog.nviso.eu/2023/07/17/introducing-cs2br-pt-ii-one-tool-to-port-them-all/" target="_blank">Introducing CS2BR pt. II - One tool to port them all</a>. I still don't get why you would create a C2 that doesn't just have BOF compatibility out of the box, but here we are.</li>
<li><a href="https://lock.cmpxchg8b.com/zenbleed.html" target="_blank">Zenbleed</a>. You should get nervous if Tavis hasn't posted anything in a while, because you know he's cooking up a banger. Use-after-free in a CPU, pretty awesome research.</li>
<li><a href="https://www.qualys.com/2023/07/19/cve-2023-38408/rce-openssh-forwarded-ssh-agent.txt" target="_blank">CVE-2023-38408: Remote Code Execution in OpenSSH's forwarded ssh-agent</a>. A very "meh" bug but an epic exploit. From cannot "control anything except the order in which we load (and immediately unload) shared libraries from /usr/lib* in ssh-agent" to RCE is just the kind of creative hacking that gets me excited. This has my vote for coolest hack of the year so far.</li>
<li><a href="https://blog.assetnote.io/2023/07/22/pre-auth-rce-metabase/" target="_blank">Chaining our way to Pre-Auth RCE in Metabase (CVE-2023-38646)</a>. The assetnote guys really know how to pwn a webapp.</li>
<li><a href="https://jakewnuk.com/posts/an-approach-to-a9/" target="_blank">An Approach to A9</a>. Did you know hashcat had an <cite>-a9</cite> attach mode?</li>
<li><a href="https://h0mbre.github.io/kCTF_Data_Only_Exploit/#" target="_blank">Escaping the Google kCTF Container with a Data-Only Exploit</a>. Some great Linux kernel exploitation content.</li>
<li><a href="https://riccardoancarani.github.io/2023-07-31-mockingjay-what-is-old-is-new-again/" target="_blank">Mockingjay - What is old is new again</a>. "Riding the hype train to see if we can get something useful out of it." That's like 90% of what I do.</li>
<li><a href="https://posts.specterops.io/on-structured-data-707b7d9876c6" target="_blank">On (Structured) Data</a>. Yes. Please someone with authority (CISA? MITRE?) or commonly used tools (Forta? Specter Ops?) define the schema that all C2 and post-ex tools can use so we can standardize all this mess! In the meantime people will write adaptors (think Extract, transform, and load [ETL] pipelines) for tools that lag behind. If there is a good enough aggregator, people will be compelled to conform.</li>
<li><a href="https://www.trustedsec.com/blog/prefetch-the-little-snitch-that-tells-on-you/" target="_blank">Prefetch: The Little Snitch That Tells on You</a>. Make sure to clean up after yourself.</li>
<li><a href="https://www.wiz.io/blog/ubuntu-overlayfs-vulnerability" target="_blank">GameOver(lay): Easy-to-exploit local privilege escalation vulnerabilities in Ubuntu Linux affect 40% of Ubuntu cloud workloads</a>. Ubuntu moves fast, and sometimes breaks things.</li>
<li><a href="https://github.com/0xe7/Talks/blob/main/Andrew_Charlie_Ive_Got_A_Forged_Twinkle_In_My_Eye.pdf" target="_blank">[PDF] Andrew_Charlie_Ive_Got_A_Forged_Twinkle_In_My_Eye.pdf</a>. Some creative, unique slides on ticket forging attacks and detections.</li>
<li><a href="https://appsec.guide/" target="_blank">Automated Testing Handbook</a>. When some of the masters of app testing (Trail of Bits) write a book, you might want to give it a read.</li>
<li><a href="https://www.politoinc.com/post/playing-with-bubbles-an-introduction-to-dll-sideloading" target="_blank">Playing with Bubbles: An Introduction to DLL-Sideloading</a>. A good intro, and uses my favorite DLL sideloading tool: <a href="https://github.com/Accenture/Spartacus" target="_blank">Spartacus</a>.</li>
<li><a href="https://labs.cognisys.group/posts/Advanced-Module-Stomping-and-Heap-Stack-Encryption/" target="_blank">Advanced Module Stomping &amp; Heap/Stack Encryption</a>. These days you best be doing some type of heap/stack encryption or any advanced EDR will detect all your unobfuscated strings in memory. Grab the code <a href="https://github.com/CognisysGroup/SweetDreams" target="_blank">here</a> .</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://redhuntlabs.com/blog/introducing-bucketloot-an-automated-cloud-bucket-inspector/" target="_blank">Introducing BucketLoot</a> - An Automated Cloud Bucket Inspector.</li>
<li><a href="https://github.com/wh0amitz/KRBUACBypass" target="_blank">KRBUACBypass</a> - UAC Bypass By Abusing Kerberos Tickets.</li>
<li><a href="https://github.com/vchan-in/CVE-2023-35078-Exploit-POC" target="_blank">CVE-2023-35078-Exploit-POC</a> - Remote Unauthenticated API Access vulnerability has been discovered in Ivanti Endpoint Manager Mobile (EPMM), formerly known as MobileIron Core. This vulnerability impacts all supported versions - Version 11.4 releases 11.10, 11.9 and 11.8.</li>
<li><a href="https://github.com/WKL-Sec/dcomhijack" target="_blank">dcomhijack</a> - Lateral Movement Using DCOM and DLL Hijacking.</li>
<li><a href="https://aadinternals.com/osint/" target="_blank">AADInternals OSINT</a>. This web based tool will extract openly available information for the given tenant.</li>
<li><a href="https://github.com/Cracked5pider/CodeCave/tree/main/LdrFunctionEx" target="_blank">LdrFunctionEx</a> - "should evade EAF and maybe (haven't tested it) EATGuard"</li>
<li><a href="https://github.com/reveng007/DarkWidow" target="_blank">DarkWidow</a> - Indirect Dynamic Syscall, SSN + Syscall address sorting via Modified TartarusGate approach + Remote Process Injection via APC Early Bird + Spawns a sacrificial Process as target process + (ACG+BlockDll) mitigation policy on spawned process + PPID spoofing + Api resolving from TIB + API hashing.</li>
<li><a href="https://github.com/lrh2000/StackRot" target="_blank">StackRot</a> - CVE-2023-3269: Linux kernel privilege escalation vulnerability. [First published in 2023-07-10 LWiS - Now includes an exploit]</li>
<li><a href="https://github.com/MzHmO/TGSThief" target="_blank">TGSThief</a> - My implementation of the GIUDA project (Ask a TGS on behalf of another user without password) in C++.</li>
<li><a href="https://github.com/mandiant/msi-search" target="_blank">msi-search</a> - This tool simplifies the task for red team operators and security teams to identify which MSI files correspond to which software and enables them to download the relevant file to investigate local privilege escalation vulnerabilities through MSI repairs. Read more about MSI repair vulnerabilities at <a href="https://www.mandiant.com/resources/blog/privileges-third-party-windows-installers" target="_blank">Escalating Privileges via Third-Party Windows Installers</a>.</li>
<li><a href="https://github.com/wh0amitz/S4UTomato" target="_blank">S4UTomato</a> - Escalate Service Account To LocalSystem via Kerberos.</li>
<li><a href="https://github.com/slemire/WSPCoerce" target="_blank">WSPCoerce</a> - PoC to coerce authentication from Windows hosts using MS-WSP.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/shipcod3/canTot" target="_blank">canTot</a> - quick and dirty canbus h4xing framework.</li>
<li><a href="https://github.com/allpaca/chrome-sbx-db" target="_blank">chrome-sbx-db</a> - A Collection of Chrome Sandbox Escape POCs/Exploits for learning.</li>
<li><a href="https://github.com/foxlox/GIUDA" target="_blank">GIUDA</a> - Ask a TGS on behalf of another user without password.</li>
<li><a href="https://github.com/sensepost/Frack" target="_blank">Frack</a> - Keep and Maintain your breach data.</li>
<li><a href="https://github.com/hasherezade/exe_to_dll" target="_blank">exe_to_dll</a> - Converts a EXE into DLL.</li>
<li><a href="https://github.com/zblurx/dploot" target="_blank">dploot</a> - DPAPI looting remotely in Python.</li>
<li><a href="https://github.com/x42en/sysplant" target="_blank">sysplant</a> - Your syscall factory.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 353 (+1)</p>
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
