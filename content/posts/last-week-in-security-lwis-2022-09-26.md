Title: Last Week in Security (LWiS) - 2022-09-26
Date: 2022-09-26 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-09-26
Author: Erik
Summary: AttachMe Oracle Cloud vuln (<a href="https://twitter.com/eladgabay_" target="_blank">@eladgabay_</a>), JuicyPotatoNG service to SYSTEM privesc (<a href="https://twitter.com/decoder_it" target="_blank">@decoder_it</a> + <a href="https://twitter.com/splinter_code" target="_blank">@splinter_code</a>), personal phishing (<a href="https://twitter.com/Direct_Defense" target="_blank">@Direct_Defense</a>), AD CS pwnage (<a href="https://twitter.com/theluemmel" target="_blank">@theluemmel</a>), Kerberos FAST protection (<a href="https://twitter.com/4ndr3w6S" target="_blank">@4ndr3w6S</a>), service exploitation via pipes (<a href="https://twitter.com/x86matthew" target="_blank">@x86matthew</a>), and more!

<aside class="m-note m-warning">
<h3>Bsides Augusta Talk</h3>
<p>I'll be giving the talk <a href="https://bsidesaugusta2022.busyconf.com/schedule#activity_6292462f6c06cd007f69eed1" target="_blank">Stop Writing Malware! The Blue team has done it for you</a> on 2022-10-01 in Augusta. Come say hi!</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-09-19 to 2022-09-26.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.cobaltstrike.com/blog/out-of-band-update-cobalt-strike-4-7-1/" target="_blank">Out Of Band Update: Cobalt Strike 4.7.1</a>. Cobalt Strike gets a rare out of band update after HTML injection in the victim controlled username was discovered. Other fixes for DoS prevention and a sleep mask bug were fixed as well.</li>
<li><a href="https://www.sophos.com/en-us/security-advisories/sophos-sa-20220923-sfos-rce" target="_blank">Resolved RCE in Sophos Firewall (CVE-2022-3236)</a>. RCE in your firewall has got to hurt.</li>
<li><a href="https://www.vice.com/en/article/y3pn9w/antivirus-used-by-millions-blocked-all-google-sites-by-mistake-sowing-chaos" target="_blank">Antivirus Used by Millions Blocked All Google Sites by Mistake, Sowing Chaos</a>. "Sowing Chaos" seems a bit much for an hour of outage. "For around an hour on Wednesday morning, some people who had Malwarebytes antivirus installed on their computers could not visit any Google site or use services like Gmail or the Google Play Store."</li>
<li><a href="https://www.sentinelone.com/labs/the-mystery-of-metador-an-unattributed-threat-hiding-in-telcos-isps-and-universities/" target="_blank">The Mystery of Metador | An Unattributed Threat Hiding in Telcos, ISPs, and Universities</a>. I skip most of these "APT" teardown blogs, because the "APTs" getting caught are using powershell and certutil, asking to be caught. This one however, shows a bit more sophistication.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.wiz.io/blog/attachme-oracle-cloud-vulnerability-allows-unauthorized-cross-tenant-volume-access" target="_blank">AttachMe: critical OCI vulnerability allows unauthorized access to customer cloud storage volumes</a>. This has to be one of the worst cloud vulnerabilities. Arbitrary access to any storage volume by just knowing the identifier. Its a classic IDOR vulnerability, except it gets you cloud storage volumes! Wiz again proves their dominance in the cloud security space.</li>
<li><a href="https://decoder.cloud/2022/09/21/giving-juicypotato-a-second-chance-juicypotatong/" target="_blank">Giving JuicyPotato a second chance: JuicyPotatoNG</a>. The potatoes are the Windows privesc class that seems to never die. This one will take you from a service account to SYSTEM. I have 16 unique potato tools in my collection, and the authors hint they have yet another on the way!</li>
<li><a href="https://www.directdefense.com/part-2-target-phishing-its-gotten-personal/" target="_blank">Part 2: Target Phishing — It's Gotten Personal</a>. This kind of drawn out phishing is extremely effective.</li>
<li><a href="https://research.nccgroup.com/2022/09/22/tool-release-project-kubescout-adding-kubernetes-support-to-scout-suite/" target="_blank">Tool Release - Project Kubescout: Adding Kubernetes Support to Scout Suite</a>. Now you can use the familiar Scout Suite with your k8s clusters too!</li>
<li><a href="https://luemmelsec.github.io/Skidaddle-Skideldi-I-just-pwnd-your-PKI/" target="_blank">Skidaddle Skideldi - I just pwnd your PKI</a>. This post is a one stop shop for AD CS pwnage walkthroughs.</li>
<li><a href="https://simonwillison.net/2022/Sep/16/prompt-injection-solutions/" target="_blank">I don't know how to solve prompt injection</a>. This is an interesting attack vector in "AI" powered bots. By feeding them input that looks like a back and forth, you can <a href="https://mobile.twitter.com/mkualquiera/status/1570546998104948736" target="_blank">leak the original prompt</a>. Who knew that natural language processing would lead to exploits in plain english.</li>
<li><a href="https://www.trustedsec.com/blog/i-wanna-go-fast-really-fast-like-kerberos-fast/" target="_blank">I Wanna Go Fast, Really Fast, like (Kerberos) FAST</a>. The new protections in Kerberos (<a href="https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831747(v=ws.11)#kerberos-armoring-flexible-authentication-secure-tunneling-fast" target="_blank">Flexible Authentication Secure Tunneling [FAST]</a>) provide good protection against "offline" kerberoasting attacks, but are ineffective against attacks that leverage lsass to generate requests (certain Rubeus commands) and are difficult to implement correctly. From the MS docs: "This policy setting is affected by another setting. When a domain does not support Kerberos armoring by enabling KDC support claims, compound authentication, and Kerberos armoring, all authentication attempts for all its users will fail from computers that have this policy enabled."</li>
<li><a href="https://www.x86matthew.com/view_post?id=windows_seagate_lpe" target="_blank">Exploiting a Seagate service to create a SYSTEM shell (CVE-2022-40286)</a>. From driver download to LPE. Excellent write up!</li>
<li><a href="https://www.matteomalvica.com/blog/2022/09/22/bypassing-intel-cet-counterfeit-objects/" target="_blank">Bypassing Intel CET with Counterfeit Objects</a>. Some great low level exploit dev content here. Control Enforcement Technology (CET) was supposed to stop ROP at the hardware level, until Counterfeit Object-Oriented Programming (COOP) showed up to take its place. This post shows COOP working on modern Windows with CET enabled.</li>
<li><a href="https://www.thehacker.recipes/ad/movement/kerberos/forged-tickets/sapphire" target="_blank">Sapphire tickets</a>. These might be the best precious-metal themed tickets yet. By not only requesting a ticket before modifying the PAC (Diamon Ticket), Sapphire tickets also request a ticket that contains a legitimate elevated privilege PAC to use with the previously requested ticket. This way, the information in the ticket matches exactly with whats in AD, making detection very difficult.</li>
<li><a href="https://mrd0x.com/spoofing-calendar-invites-using-ics-files/" target="_blank">Spoofing Calendar Invites Using .ics Files</a>. I'm a bit sad this was posted as this technique has been extremely effective.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/ZephrFish/AutoHoneyPoC" target="_blank">AutoHoneyPoC</a>. Automatically generate "HoneyPoC" scripts to catch people running things without understanding them.</li>
<li><a href="https://github.com/ZephrFish/SandboxSpy" target="_blank">SandboxSpy</a>. Code for profiling sandboxes - Initially an idea to profile sandboxes, the code is written to take enviromental variables and send them back in a Base32 string over HTTP to an endpoint.</li>
<li><a href="https://github.com/D1rkMtr/githubC2" target="_blank">githubC2</a> -  Abusing Github API to host our C2 traffic, useful for bypassing blocking firewall rules if github is in the target white list , and in case you don't have C2 infrastructure, now you have a free one.</li>
<li><a href="https://github.com/DavidBuchanan314/monomorph" target="_blank">monomorph</a>- MD5-Monomorphic Shellcode Packer - all payloads have the same MD5 hash.</li>
<li><a href="https://github.com/D1rkMtr/FilelessRemotePE" target="_blank">FilelessRemotePE</a> - Loading Fileless Remote PE from URI to memory with argument passing and ETW patching and NTDLL unhooking and No New Thread technique.</li>
<li><a href="https://github.com/memN0ps/mordor-rs" target="_blank">mordor-rs</a> - Rusty Hell's Gate / Halo's Gate / Tartarus' Gate and FreshyCalls / Syswhispers2 Library.</li>
<li><a href="https://github.com/ChoiSG/GwisinMsi" target="_blank">GwisinMsi</a> - PoC MSI payload based on ASEC/AhnLab's blog post.</li>
<li><a href="https://github.com/jazzpizazz/BloodHound.py-Kerberos" target="_blank">BloodHound.py-Kerberos</a> - A Python based ingestor for BloodHound, now with kerberos support on Linux.</li>
<li><a href="https://github.com/redteamsocietegenerale/DLLirant" target="_blank">DLLirant</a> is a tool to automatize the DLL Hijacking researches on a specified binary.</li>
<li><a href="https://github.com/Markakd/CVE-2022-2588" target="_blank">CVE-2022-2588</a> This linux LPE effects 3.17 to 5.19 (Ubuntu 17-22).</li>
<li><a href="https://github.com/Idov31/Cronos" target="_blank">Cronos</a> PoC for a new sleep obfuscation technique leveraging waitable timers to evade memory scanners.</li>
<li><a href="https://github.com/evilsocket/spycast" target="_blank">spycast</a> A crossplatform mDNS enumeration tool.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/blacklanternsecurity/bbot" target="_blank">bbot</a> - OSINT automation for hackers.</li>
<li><a href="https://github.com/chronoxor/NetCoreServer" target="_blank">NetCoreServer</a> - Ultra fast and low latency asynchronous socket server &amp; client C# .NET Core library with support TCP, SSL, UDP, HTTP, HTTPS, WebSocket protocols and 10K connections problem solution.</li>
<li><a href="https://pentesting.cloud/" target="_blank">A Free Pen Testing Learning Platform</a>. Spin up your own cloud scenarios using these free templates.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 420 (+0)</p>
<p>Blogs monitored: 324 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
