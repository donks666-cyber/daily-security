Title: Last Week in Security (LWiS) - 2021-02-22
Date: 2021-02-22 23:58
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-02-22
Author: Erik
Summary: Ubuntu LPE (<a href="https://twitter.com/Gr33nh4t" target="_blank">@Gr33nh4t</a>), open source FIDO2 🔑 (<a href="https://twitter.com/SoloKeysSec" target="_blank">@SoloKeysSec</a>), new ways to copy shellcode in VBA (<a href="https://twitter.com/TheXC3LL" target="_blank">@TheXC3LL</a>), unconventional exploitation (<a href="https://twitter.com/itm4n" target="_blank">@itm4n</a>), harvesting hashes (<a href="https://twitter.com/domchell" target="_blank">@domchell</a>), M1 mac malware (<a href="https://twitter.com/ForensicITGuy" target="_blank">@ForensicITGuy</a>), BOFs outside of CS (<a href="https://twitter.com/trustedsec" target="_blank">@TrustedSec</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-02-15 to 2021-02-22.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.kickstarter.com/projects/conorpatrick/solo-v2-safety-net-against-phishing" target="_blank">Solo V2 — Safety Net Against Phishing</a>. Everyone knows FIDO2 keys are the best defense against credential phishing, but until now all the solutions have been closed source and expensive. Solokey's Solo V2 looks to change all that with an affordable, NFC capable, open source FIDO2 key. I have no affiliation with Solokey - just a fan of what they are doing. Note: the open source firmware <a href="https://doyensec.com/resources/Doyensec_SoloKeys_TestingReport_Q12020_v3.pdf" target="_blank">has been audited</a>.</li>
<li><a href="https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf" target="_blank">Sandworm intrusion set campaign targeting centreon systems</a>. In a three year long campaign, Sandworm used webshells and a Linux backdoor to access information technology providers, including web hosting providers. Based on Sandworm's history of targeting industrial control systems, ransomware, and highly public attacks (2018 winter olympics), perhaps this was just an effort to get free redirectors and payload hosting.</li>
<li><a href="https://ramble.pw/f/privacy/2387/brave-browser-leaks-your-tor-onion-service-requests-through" target="_blank">Brave Browser leaks your Tor / Onion service requests through DNS</a>. This isn't the first issue with Tor and Brave (<a href="https://github.com/sickcodes/security/blob/master/advisories/SICK-2020-013.md" target="_blank">CVE-2020-8276</a>), and likely won't be the last. Mixing Tor and a standard browser is a recipe for disaster.</li>
<li><a href="https://redcanary.com/blog/clipping-silver-sparrows-wings/" target="_blank">Clipping Silver Sparrow’s wings: Outing macOS malware before it takes flight</a>. MacOS specific malware, including an arm compiled variant, uses the old favorite malicious pkg installer to infect victims. MalwareBytes claims it has seen the malware on nearly 30,000 endpoints, while the Red Canary team says it has no evidence the malware has conducted any post-exploitation activities.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://alephsecurity.com/2021/02/16/apport-lpe/" target="_blank">Exploiting crash handlers: LPE on Ubuntu</a>. This was a great walkthrough of a complex bug chain that lead to a local privilege escalation. A few different tricks are used to fool the apport crash dump writer into writing a file to an arbitrary location, as root, with arbitrary data. This bug chain affects Ubuntu since the beginning of apport (12.04), so be sure to patch!</li>
<li><a href="https://www.xmcyber.com/introducing-machound-a-solution-to-macos-active-directory-based-attacks/" target="_blank">Introducing MacHound: A Solution to MacOS Active Directory-Based Attacks</a>. On an engagement with a large macOS user base and no good way to visualize them in BloodHound? Not anymore! Try <a href="https://github.com/XMCyber/MacHound" target="_blank">MacHound</a>, which uses a Python 3 script run on a macOS host to collect useful data that can be ingested into Bloodhound.</li>
<li><a href="https://adepts.of0x.cc/alternatives-copy-shellcode/" target="_blank">One thousand and one ways to copy your shellcode to memory (VBA Macros)</a>. Most VBA macros reused the same few ways to copy shellcode into memory before executing. This post explores a few "new" ways that are not commonly seen.</li>
<li><a href="https://itm4n.github.io/windows-registry-rpceptmapper-exploit/" target="_blank">An Unconventional Exploit for the RpcEptMapper Registry Key Vulnerability</a>. <a href="https://twitter.com/itm4n" target="_blank">@itm4n</a> takes you under the hood of <a href="https://github.com/itm4n/Perfusion" target="_blank">Perfusion</a> and the unconventional process to achieve an exploit exe without the need for compiling custom DLLs, etc.</li>
<li><a href="https://srcincite.io/blog/2021/02/18/smarty-template-engine-multiple-sandbox-escape-vulnerabilities.html" target="_blank">Smarty Template Engine Multiple Sandbox Escape PHP Code Injection Vulnerabilities</a>. Template engines are often a source of vulnerabilities. This post explores the smarty template engine for PHP and has practical unauthenticated remote code execution PoCs for popular web apps like TikiWiki.</li>
<li><a href="https://www.trustedsec.com/blog/coffloader-building-your-own-in-memory-loader-or-how-to-run-bofs/" target="_blank">COFFLoader: Building your own in memory loader or how to run BOFs</a>. As more and more techniques are written as Cobalt Strike BOFs, you may be wishing your C2 of choice could leverage them? This post explores how to load these COFFs in memory and run them. I am looking forward to a BOF runner library that will work across C2 frameworks so all the hard work put into BOFs can be used everywhere! The PoC is available <a href="https://github.com/trustedsec/COFFLoader" target="_blank">here</a></li>
<li><a href="https://www.mdsec.co.uk/2021/02/farming-for-red-teams-harvesting-netntlm/" target="_blank">Farming for Red Teams: Harvesting NetNTLM</a>. While this technique isn't new, the slick productization of it is. The <a href="https://github.com/mdsecactivebreach/Farmer" target="_blank">new tools</a> released should help any Red Team struggling with implementing NetNTLM captures after initial compromise.</li>
<li><a href="https://www.coresecurity.com/core-labs/articles/analysis-cisco-anyconnect-posture-hostscan-local-privilege-escalation-cve-2021" target="_blank">Analysis of Cisco AnyConnect Posture (HostScan) Local Privilege Escalation: CVE-2021-1366</a>. AnyConnect had an LPE early last year, but Core Security finds another with a nifty bug chain where the "host scan" feature of the VPN client is abused. A PoC is included - as an image of code for some reason.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/FortyNorthSecurity/CIMplant" target="_blank">CIMplant</a> is a C# port of WMImplant which uses either CIM or WMI to query remote systems. It allows you to gather data about a remote system, execute commands, exfil data, and more. The tool allows connections using Windows Management Instrumentation, WMI, or Common Interface Model, CIM. CIMplant requires local administrator permissions on the target system. More information in this <a href="https://fortynorthsecurity.com/blog/cimplant-part-1-detections/" target="_blank">post</a>.</li>
<li><a href="https://github.com/agnivesh/endgame" target="_blank">endgame</a> is an AWS Pentesting tool that lets you use one-liner commands to backdoor an AWS account's resources with a rogue AWS account - or share the resources with the entire internet. Compared to other AWS offensive tools, endgame have a much wider range of supported services (18 vs 11 for the official AWS Access Analyzer). Of note, the "original" repo (salesforce) and the author's repo (kmcquade) have both been taken down. Sadly, Salesforce has a <a href="https://arstechnica.com/gadgets/2017/08/salesforce-fires-two-security-team-members-for-presenting-at-defcon/" target="_blank">reputation for this kind of thing</a>.</li>
<li><a href="https://github.com/dennis-tra/pcp" target="_blank">pcp</a> is a command line peer-to-peer data transfer tool based on libp2p. It differs from others (like <a href="https://github.com/schollz/croc" target="_blank">croc</a>) because it uses <a href="https://ipfs.io/" target="_blank">IPFS</a> instead of a centralized sever.</li>
<li><a href="https://github.com/Flangvik/AzureC2Relay" target="_blank">AzureC2Relay</a> is an Azure Function that validates and relays Cobalt Strike beacon traffic by verifying the incoming requests based on a Cobalt Strike Malleable C2 profile. Any incoming requests that do not share the profiles user-agent, URI paths, headers, and query parameters, will be redirected to a configurable decoy website. More information in the <a href="https://www.trustedsec.com/blog/front-validate-and-redirect/" target="_blank">blog post</a>.</li>
<li><a href="https://github.com/Aetsu/OffensivePipeline" target="_blank">OffensivePipeline</a> allows you to download, compile (without Visual Studio), and obfuscate C# tools for Red Team exercises.</li>
<li><a href="https://github.com/cedowens/Swift-Attack" target="_blank">Swift-Attack</a> is the macOS equivalent of atomic red team. It contains unit tests for blue teams to aid with building detections for some common macOS post exploitation methods.</li>
<li><a href="https://github.com/swisskyrepo/SharpLAPS" target="_blank">SharpLAPS</a> is a C# executable that will retrieve the LAPS password from the Active Directory. It must be executed from either a Domain Administrator or an account with ExtendedRight or Generic All Rights.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/karttoon/trigen" target="_blank">trigen</a> is a Python script which uses different combinations of Win32 function calls in generated VBA to execute shellcode. More information <a href="http://ropgadget.com/posts/abusing_win_functions.html" target="_blank">here</a>.</li>
<li><a href="https://github.com/ZupIT/horusec" target="_blank">horusec</a> s an open source tool that performs static code analysis to identify security flaws during the development process. Currently, the languages for analysis are: C#, Java, Kotlin, Python, Ruby, Golang, Terraform, Javascript, Typescript, Kubernetes, PHP, C, HTML, JSON, and Dart. The tool has options to search for key leaks and security flaws in all files of your project, as well as in Git history.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
