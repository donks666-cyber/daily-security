Title: Last Week in Security (LWiS) - 2022-04-25
Date: 2022-04-26 12:00
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-04-25
Author: Erik
Summary: Acrobat extension issues (<a href="https://twitter.com/WPalant" target="_blank">@WPalant</a>), ECDSA signature in Java vuln (<a href="https://twitter.com/neilmaddog" target="_blank">@neilmaddog</a>), GPO LPE (<a href="https://twitter.com/decoder_it" target="_blank">@decoder_it</a>), SSN resolution from process structs (<a href="https://twitter.com/modexpblog" target="_blank">@modexpblog</a>), AWS container escape (<a href="https://twitter.com/yuvalavra" target="_blank">@yuvalavra</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-04-18 to 2022-04-25.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://googleprojectzero.blogspot.com/2022/04/the-more-you-know-more-you-know-you.html" target="_blank">The More You Know, The More You Know You Don't Know: A Year in Review of 0-days Used In-the-Wild in 2021</a>. "When we look over these 58 0-days used in 2021, what we see instead are 0-days that are similar to previous &amp; publicly known vulnerabilities." Keep looking for adjacent vulnerabilities!</li>
<li><a href="https://www.zerodayinitiative.com/blog/2022/4/14/pwn2own-miami-2022-results" target="_blank">Pwn2Own Miami 2022 Results</a>. 26 ICS focused 0days!</li>
<li><a href="https://www.cobaltstrike.com/blog/cobalt-strike-4-6-the-line-in-the-sand/" target="_blank">Cobalt Strike 4.6: The Line In The Sand</a>. Minor updates include a new user defined size limit for execute-assembly, and a unified "arsenal kit." The bigger updates are around the "security" (anti-piracy) features which may make it harder for criminals to use Cobalt Strike.</li>
<li><a href="https://www.hexacorn.com/blog/2022/04/21/infosec-salaries-the-myth-and-the-reality/" target="_blank">Infosec Salaries - the myth and the reality</a>. TLDR: Always take more base over options.</li>
<li><a href="https://techcommunity.microsoft.com/t5/storage-at-microsoft/smb1-now-disabled-by-default-for-windows-11-home-insiders-builds/ba-p/3289473" target="_blank">SMB1 now disabled by default for Windows 11 Home Insiders builds</a>. The unwillingness of Microsoft to break backward compatibility has caused many a vulnerability, perhaps the tide is turning? You can still enable SMBv1 but soon even the binaries will be gone and will be a separate unsupported install.</li>
<li><a href="https://www.youtube.com/playlist?list=PLYvhPWR_XYJnPvrhXE4RYvwZhV26nYTIp" target="_blank">OffensiveCon22 Youtube Playlist</a>. Which talks were your favorite?</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.grimm-co.com/2022/04/no-hardware-no-problem-emulation-and.html" target="_blank">No Hardware, No Problem: Emulation and Exploitation</a>. This is a good post for anyone interested in IoT devices as it contains some nice gotchas and workarounds.</li>
<li><a href="https://palant.info/2022/04/19/adobe-acrobat-hollowing-out-same-origin-policy/" target="_blank">Adobe Acrobat hollowing out same-origin policy</a>. Browser add-ons continue to be a silent killer. No one seems to be publicizing the power they have now that every app is a web app. Perhaps it will take a large add-on compromise for the industry to wake up?</li>
<li><a href="https://www.arashparsa.com/bypassing-pesieve-and-moneta-the-easiest-way-i-could-find/" target="_blank">Bypassing PESieve and Moneta (The "easy" way....?)</a>. Memory scanners can pose an problem to red team tooling, but there are clever (not not new) tricks to keep memory encrypted until it's needed.</li>
<li><a href="https://neilmadden.blog/2022/04/19/psychic-signatures-in-java/" target="_blank">CVE-2022-21449: Psychic Signatures in Java</a>. "If you are using ECDSA signatures for any of these security mechanisms, then an attacker can trivially and completely bypass them if your server is running any Java 15, 16, 17, or 18 version before the April 2022 Critical Patch Update (CPU)." A Java rewrite of a C++ cryptographic library introduced this flaw in Java 15. All those enterprise Java apps still on Java 8 are safe 😂. PoC to demonstrate the vulnerability <a href="https://github.com/khalednassar/CVE-2022-21449-TLS-PoC" target="_blank">here</a>.</li>
<li><a href="https://decoder.cloud/2022/04/25/a-not-so-common-and-stupid-privilege-escalation/" target="_blank">A not-so-common and stupid privilege escalation</a>. These kinds of hard-to-automatically-find vulnerabilities are what make red teams valuable. This is a cool find, and one to look out for on your next assessment or in your own environment. Lock down those shares!</li>
<li><a href="https://captmeelo.com//redteam/maldev/2022/04/21/kernelcallbacktable-injection.html" target="_blank">Adventures with KernelCallbackTable Injection</a>. This is a shellcode injection technique not often used. PoC here: <a href="https://github.com/capt-meelo/KernelCallbackTable-Injection" target="_blank">KernelCallbackTable-Injection</a>.</li>
<li><a href="https://xret2pwn.github.io/Access_Token_Part0x01/" target="_blank">Access Token Manipulation Part 0x01</a>. How do the token tricks for your favorite C2 work under the hood? It turns out the Windows APIs for tokens are pretty straight forward.</li>
<li><a href="https://www.mdsec.co.uk/2022/04/resolving-system-service-numbers-using-the-exception-directory/" target="_blank">Resolving System Service Numbers using the Exception Directory</a>. The use of a Control Flow Guard "feature" for malware dev is juicy. Classic hacking. The runtime function table method has a wider set of compatibility, and may be more useful.</li>
<li><a href="https://unit42.paloaltonetworks.com/aws-log4shell-hot-patch-vulnerabilities/" target="_blank">AWS's Log4Shell Hot Patch Vulnerable to Container Escape and Privilege Escalation</a>. Two weeks in a row with AWS issues, that's unusual. In this case a hotpatch was a bit too hot and ran any process named "java" in a container with elevated permission in order to patch them. This has been fixed, and AWS has an <a href="https://aws.amazon.com/security/security-bulletins/AWS-2022-006/" target="_blank">official announcement</a>.</li>
<li><a href="https://posts.specterops.io/abusing-azure-container-registry-tasks-1f407bfaa465" target="_blank">Abusing Azure Container Registry Tasks</a>. The cloud is just someone else's computer, and if you configure it poorly, there are shells to be had.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Dec0ne/KrbRelayUp" target="_blank">KrbRelayUp</a> is a universal no-fix local privilege escalation in windows domain environments where LDAP signing is not enforced (the default settings).</li>
<li><a href="https://github.com/bloomberg/memray" target="_blank">memray</a> is a memory profiler for Python. Not specifically security related, but very cool.</li>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2274" target="_blank">Issue 2274: Linux: watch_queue filter OOB write (and other bugs)</a>. Google Project Zero found another Linux LPE. This one affects kernel from 5.8 to 2022-03-11 (5.16.15, 5.15.29, 5.10.106). PoC exploit is included, but may be unstable.</li>
<li><a href="https://github.com/outflanknl/C2-Tool-Collection" target="_blank">C2-Tool-Collection</a> is a collection of tools which integrate with Cobalt Strike (and possibly other C2 frameworks) through BOF and reflective DLL loading techniques. This is from Outflank so you know its going to be good.</li>
<li><a href="https://github.com/j3ssie/cdnstrip" target="_blank">cdnstrip</a> is a tool for striping CDN IPs from a list of IP Addresses.</li>
<li><a href="https://github.com/dsnezhkov/elfpack" target="_blank">elfpack</a> does ELF Binary Section Docking for Stageless Payload Delivery.</li>
<li><a href="https://github.com/GetRektBoy724/HalosUnhooker" target="_blank">HalosUnhooker</a> is a Halos Gate-based NTAPI Unhooker.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/mgdm/htmlq" target="_blank">htmlq</a> is like jq, but for HTML. Uses CSS selectors to extract bits of content from HTML files.</li>
<li><a href="https://github.com/Octoberfest7/KDStab" target="_blank">KDStab</a> is a BOF combination of KillDefender and Backstab.</li>
<li><a href="https://github.com/AidenPearce369/ADReaper" target="_blank">ADReaper</a> is a fast enumeration tool for Windows Active Directory Pentesting written in Go.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 415 (+0)</p>
<p>Blogs monitored: 304 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
