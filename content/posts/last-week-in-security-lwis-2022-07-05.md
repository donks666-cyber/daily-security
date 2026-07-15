Title: Last Week in Security (LWiS) - 2022-07-05
Date: 2022-07-05 17:45
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-07-05
Author: Erik
Summary: In the wild 0days (<a href="https://twitter.com/maddiestone" target="_blank">@maddiestone</a>), new Win11 primitive (<a href="https://twitter.com/yarden_shafir" target="_blank">@yarden_shafir</a>), Cloudflare ZeroTrust for C2 (<a href="https://twitter.com/zux0x3a" target="_blank">@zux0x3a</a>), macOS LPEs (<a href="https://twitter.com/linushenze" target="_blank">@LinusHenze</a> + <a href="https://twitter.com/zhuowei" target="_blank">@zhuowei</a> + Jack Dates of <a href="https://twitter.com/ret2systems" target="_blank">@ret2systems</a>), SCCM abuse (<a href="https://twitter.com/subat0mik" target="_blank">@subat0mik</a> + <a href="https://twitter.com/_Mayyhem" target="_blank">@_Mayyhem</a>), Diamond Tickets (<a href="https://twitter.com/4ndr3w6S" target="_blank">@4ndr3w6S</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-06-27 to 2022-07-05.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://googleprojectzero.blogspot.com/2022/06/2022-0-day-in-wild-exploitationso-far.html" target="_blank">2022 0-day In-the-Wild Exploitation…so far</a>. Browsers and phones are were people do most of their work these days, and thats where most of the 0days are too, unsurprisingly.</li>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2268" target="_blank">Issue 2268: Windows: Windows Defender Remote Credential Guard Authentication Relay EoP</a>. The handling of Windows Defender Remote Credential Guard credentials is vulnerable to authentication relay attacks leading to elevation of privilege or authentication bypass. Fixed on 2022-06-15 as <a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30150" target="_blank">CVE-2022-30150</a>.</li>
<li><a href="https://about.gitlab.com/releases/2022/06/30/critical-security-release-gitlab-15-1-1-released/" target="_blank">GitLab Critical Security Release: 15.1.1, 15.0.4, and 14.10.5</a>. TLDR: authenticated RCE. "an authorised user could import a maliciously crafted project leading to remote code execution," plus other issues.</li>
<li><a href="https://www.vice.com/en/article/z34vpj/bug-bounty-platforms-employee-abused-internal-access-to-steal-bounties" target="_blank">Bug Bounty Platform's Employee Abused Internal Access to Steal Bounties</a>. As if bug bounty providers needed any more bad press...</li>
<li><a href="https://msrc-blog.microsoft.com/2022/06/28/azure-service-fabric-privilege-escalation-from-containerized-workloads-on-linux/" target="_blank">Service Fabric Privilege Escalation from Containerized Workloads on Linux</a>. A compromised container could escape the container and compromise the entire cluster. Yikes! More at <a href="https://unit42.paloaltonetworks.com/fabricscape-cve-2022-30137/" target="_blank">FabricScape: Escaping Service Fabric and Taking Over the Cluster</a>.</li>
<li><a href="https://youtu.be/ptCllQSm5KU" target="_blank">Malware Steel Mill</a>. "Some Malware causing a catastrophic failure of a bucket full of molten steel." Iran seems to be the testing ground for cyber-physical attacks.</li>
<li><a href="https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/" target="_blank">When Pentest Tools Go Brutal: Red-Teaming Tool Being Abused by Malicious Actors</a>. This will surely add fuel to the C2 twitter drama fire.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://rhinosecuritylabs.com/cloud-security/cloudgoat-detection_evasion-walkthrough/" target="_blank">CloudGoat detection_evasion Scenario: Avoiding AWS Security Detection and Response</a>. Step up your AWS exploitation game by not getting caught by automated defenses in this new scenario.</li>
<li><a href="https://www.elttam.com/blog/golang-codereview/" target="_blank">Golang code review notes</a>. This post is a good summary of some of the bug classes in Go.</li>
<li><a href="https://labs.withsecure.com/blog/spoofing-call-stacks-to-confuse-edrs/" target="_blank">Spoofing Call Stacks To Confuse EDRs</a>. Thread stack spoofing isn't new, but this post leverages it to actively trick EDRs with legitimate looking stacks while doing nasty things (like dumping lsass). <a href="https://github.com/countercept/CallStackSpoofer" target="_blank">CallStackSpoofer</a> is the GitHub project.</li>
<li><a href="https://windows-internals.com/one-i-o-ring-to-rule-them-all-a-full-read-write-exploit-primitive-on-windows-11/" target="_blank">One I/O Ring to Rule Them All: A Full Read/Write Exploit Primitive on Windows 11</a>. "This technique is a post exploitation primitive unique to Windows 11 22H2+ - there are no 0-days here. Instead, there's a method to turn an arbitrary write, or even arbitrary increment bug in the Windows kernel into a full read/write of kernel memory." Code is <a href="https://github.com/yardenshafir/IoRingReadWritePrimitive" target="_blank">IoRingReadWritePrimitive</a>.</li>
<li><a href="https://0xsp.com/offensive/red-ops-techniques/abuse-cloudflare-zerotrust-for-c2-channels/" target="_blank">Abuse Cloudflare Zerotrust for C2 channels</a>. Abuse is a strong word. "Repurpose" is perhaps a better term. Cool research, and as these kinds of services become more widespread, organizations are going to have to determine how to handle them. Want more cloudflare repurposing? Check out <a href="https://blog.christophetd.fr/abusing-cloudflare-workers/" target="_blank">MitM at the Edge: Abusing Cloudflare Workers</a>.</li>
<li><a href="https://www.archcloudlabs.com/projects/bulk-cs-analysis/" target="_blank">Bulk Analysis of Cobalt Strike's Beacon Configurations</a>. How unique are your post-ex and C2 profile choices?</li>
<li><a href="https://codewhitesec.blogspot.com/2022/06/bypassing-dotnet-serialization-binders.html" target="_blank">Bypassing .NET Serialization Binders</a>. "Serialization binders are often used to validate types specified in the serialized data to prevent the deserialization of dangerous types that can have malicious side effects with the runtime serializers such as the BinaryFormatter. This blog post looks into cases where this can fail and consequently may allow to bypass validation and walks though two real-world examples of insecure serialization binders in the DevExpress framework (CVE-2022-28684) and Microsoft Exchange (CVE-2022-23277), that both allow remote code execution."</li>
<li><a href="https://www.horizon3.ai/red-team-blog-cve-2022-28219/" target="_blank">CVE-2022-28219: Unauthenticated XXE to RCE and Domain Compromise in ManageEngine ADAudit Plus</a>. Java web applications and deserialization vulnerability, name a more iconic duo.</li>
<li><a href="https://blog.nviso.eu/2022/06/30/enforcing-a-sysmon-archive-quota/" target="_blank">Enforcing a Sysmon Archive Quota</a>. If you are using Sysmon's FileDelete archive hook to store deleted files, you likely already have a solution like this but if not, it should come in handy.</li>
<li><a href="https://worthdoingbadly.com/coretrust/" target="_blank">Get root on macOS 12.3.1: proof-of-concepts for Linus Henze's CoreTrust and DriverKit bugs (CVE-2022-26766, CVE-2022-26763)</a>. macOS local privilege escalation walk thorough with PoC code.</li>
<li><a href="https://blog.ret2.io/2022/06/29/pwn2own-2021-safari-sandbox-intel-graphics-exploit/" target="_blank">Exploiting Intel Graphics Kernel Extensions on macOS</a>. More macOS exploitation?! ret2systems posts are always excellent and this is no exception.</li>
<li><a href="https://posts.specterops.io/relaying-ntlm-authentication-from-sccm-clients-7dccb8f92867" target="_blank">Relaying NTLM Authentication from SCCM Clients</a>. What can't you relay authentication with in an active directory environment these days? But SCCM has even more fun in store: <a href="https://posts.specterops.io/the-phantom-credentials-of-sccm-why-the-naa-wont-die-332ac7aa1ab9" target="_blank">The Phantom Credentials of SCCM: Why the NAA Won't Die</a>.</li>
<li><a href="https://www.trustedsec.com/blog/a-diamond-in-the-ruff/" target="_blank">A Diamond in the Ruff</a>. You've heard of Golden Tickets but what about Diamond Tickets? They offer some OPSEC advantages, and you can use them in Rubeus with <a href="https://github.com/GhostPack/Rubeus/pull/136" target="_blank">this pull request</a>.</li>
<li><a href="https://blog.coffinsec.com//research/2022/07/02/orbi-nday-exploit-cve-2020-27861.html" target="_blank">nday exploit: netgear orbi unauthenticated command injection (cve-2020-27861)</a>. A detailed post on how the vulnerability was found and exploited.</li>
<li><a href="https://github.com/outflanknl/Presentations/blob/master/HackInParis2022_Bergman_Smeets_OffensiveHunting.pdf" target="_blank">Offensive Hunting</a>. The automation and "offensive hunts" in the presentation are awesome. <a href="https://github.com/outflanknl/RedELK" target="_blank">RedELK</a> is great and advanced teams should be using it already. Excited to see more development with it!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/winterknife/PINKPANTHER" target="_blank">PINKPANTHER</a> Windows x64 handcrafted token stealing kernel-mode shellcode. Be sure to check out the caveats.</li>
<li><a href="https://github.com/romainthomas/the-poor-mans-obfuscator" target="_blank">the-poor-mans-obfuscator</a> - Binary &amp; scripts associated with "The Poor Man's Obfuscator" presentation.</li>
<li><a href="https://github.com/h3xduck/TripleCross" target="_blank">TripleCross</a> - A Linux eBPF rootkit with a backdoor, C2, library injection, execution hijacking, persistence and stealth capabilities.</li>
<li><a href="https://github.com/j00sean/SecBugs/tree/main/CVEs/CVE-2019-7040" target="_blank">CVE-2019-7040 + CVE-2021-21042</a>. POCs and exploit code for Microsoft Internet Explorer &amp; Microsoft Word (in DOCX &amp; RTF formats).</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/bassammaged/awsEnum" target="_blank">awsEnum</a> - Enumerate AWS cloud resources based on provided credentials.</li>
<li><a href="https://github.com/zu1k/nali" target="_blank">nali</a> - An offline tool for querying IP geographic information and CDN provider.</li>
<li><a href="https://github.com/chvancooten/maldev-for-dummies" target="_blank">maldev-for-dummies</a> - A workshop about Malware Development.</li>
<li><a href="https://github.com/HackingLZ/ExtractedDefender" target="_blank">ExtractedDefender</a> - An attempt to group extracted data from Defender for research purposes.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 419 (+0)</p>
<p>Blogs monitored: 316 (+2)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
