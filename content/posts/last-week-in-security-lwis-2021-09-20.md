Title: Last Week in Security (LWiS) - 2021-09-20
Date: 2021-09-20 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-09-20
Author: Erik
Summary: OMI agent RCE in Azure (<a href="https://twitter.com/shirtamari" target="_blank">@shirtamari</a>), dynamic mac malware RE (<a href="https://twitter.com/philofishal" target="_blank">@philofishal</a>), Teams spoofing (<a href="https://twitter.com/mrd0x" target="_blank">@mrd0x</a>), AMD info disclosure (<a href="https://twitter.com/kyREcon" target="_blank">@kyREcon</a>), CABless Word RCE (<a href="https://twitter.com/Edu_Braun_0day" target="_blank">@Edu_Braun_0day</a>), dBase fuzzing for code exec (<a href="https://twitter.com/spaceraccoonsec" target="_blank">@spaceraccoonsec</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-09-14 to 2021-09-20.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://ostif.org/google-is-partnering-with-open-source-technology-improvement-fund-inc-to-sponsor-security-reviews-of-critical-open-source-software/" target="_blank">Google is partnering with Open Source Technology Improvement Fund, Inc to sponsor security reviews of critical open source software.</a>. Google is funding the review of eight libraries, frameworks, and apps including Git, lodash, and Laverel.</li>
<li><a href="https://www.kali.org/blog/kali-linux-2021-3-release/" target="_blank">Kali Linux 2021.3 Release</a>. The most popular offensive security Linux distribution gets its third release of the year, with minor tweaks to better support VMs, old TLS versions, new tools, and updates throughout the OS.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://www.mdsec.co.uk/2021/09/nsa-meeting-proposal-for-proxyshell/" target="_blank">NSA Meeting Proposal for ProxyShell</a>. By combining the "NSA Metting" and "ProxyShell" exploits for Exchange, a unique RCE chain can be created that may not otherwise be detected. Code <a href="https://github.com/mdsecresearch/NSAMeetingWithProxyShell" target="_blank">here</a>.</li>
<li><a href="https://www.sentinelone.com/labs/defeating-macos-malware-anti-analysis-tricks-with-radare2/" target="_blank">Defeating macOS Malware Anti-Analysis Tricks with Radare2</a>. Working around anti-debug measures is critical to dynamic analysis. This post shows how r2 can be used to manipulate execution and bypass checks.</li>
<li><a href="https://blog.thecybersecuritytutor.com/microsoft-teams-abuse/?no-cache=1" target="_blank">Microsoft Teams Spoofing Attacks</a>. This post contains a message request approval bypass, attachment spoofing, and link spoofing techniques. If you phish via Teams, this is a must read.</li>
<li><a href="https://zeroperil.co.uk/wp-content/uploads/2021/09/AMD_PSP_Vulnerability_Report.pdf" target="_blank">AMD Chipset Driver Information Disclosure Vulnerability</a>. Two vulnerabilities exist across modern AMD chipsets that allow for information disclosure via reading uninitialized physical memory pages.</li>
<li><a href="https://medium.com/csg-govtech/all-your-d-base-are-belong-to-us-part-1-code-execution-in-apache-openoffice-cve-2021-33035-767fc7d6daf7" target="_blank">All Your (d)Base Are Belong To Us, Part 1: Code Execution in Apache OpenOffice (CVE-2021–33035)</a>. Top tier exploit write up, from fuzzing to code execution.</li>
<li><a href="https://0xboku.com/2021/09/14/0dayappsecBeginnerGuide.html" target="_blank">Beginners Guide to 0day/CVE AppSec Research</a>. I'm not sure how this guy sleeps with the consistency of long form content and code he produces. This post has a walk through of how to setup and instrument a PHP app for testing.</li>
<li><a href="https://go.recordedfuture.com/hubfs/reports/mtp-2021-0914.pdf" target="_blank">Full-Spectrum Cobalt Strike Detection</a>. This report is a technical profile of the commercial post-exploitation framework Cobalt Strike. It contains details on the capabilities of the framework, observed threat actor use, host-based and network-based detections, and SOAR strategies for detection and response. This report is intended for security operations audiences who focus on detection engineering.</li>
<li><a href="https://twitter.com/the_bit_diddler/status/1439977311101673475" target="_blank">VSCode BOF Development Trick</a>. Set your compiler to mingw32-gcc and Intellisense will help you out!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><dl>
<dt>OMIGOD</dt>
<dd><ul>
<li><a href="https://www.wiz.io/blog/secret-agent-exposes-azure-customers-to-unauthorized-code-execution" target="_blank">“Secret” Agent Exposes Azure Customers To Unauthorized Code Execution</a>. This is the post the started it all. Another Azure find from Wiz. Simply removing the authorization header allowed for RCE as root. Amazing that is a thing in 2021.</li>
<li><a href="https://msrc-blog.microsoft.com/2021/09/16/additional-guidance-regarding-omi-vulnerabilities-within-azure-vm-management-extensions/" target="_blank">Additional Guidance Regarding OMI Vulnerabilities within Azure VM Management Extensions</a>. The official Microsoft response.</li>
<li><a href="https://github.com/microsoft/OMS-Agent-for-Linux/tree/master/tools/OMIcheck" target="_blank">OMIcheck</a> is a set of scripts from Microsoft to check and upgrade your omi agents.</li>
<li><a href="https://github.com/horizon3ai/CVE-2021-38647" target="_blank">CVE-2021-38647</a> is a nice wrapper for the PoC in the Wiz post.</li>
<li><a href="https://www.greynoise.io/viz/query/?gnql=tags%3A%22Azure%20OMI%20RCE%20Attempt%22" target="_blank">Azure OMI RCE Attempt</a> shows a small sample of "in the wild" exploitation.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/xiecat/goblin/blob/master/README_EN.md" target="_blank">goblin</a> is a phishing tool that can host sites and display notices if uses click call to action buttons. This won't replace <a href="https://getgophish.com/" target="_blank">GoPhish</a> any time soon.</li>
<li><a href="https://github.com/fofapro/fapro" target="_blank">fapro</a> is a multi-protocol honey pot with ELK logging support. Looks like no source code is available (yet?).</li>
<li><a href="https://github.com/iomoath/PowerShx" target="_blank">PowerShx</a> is a rewrite and expansion on the <a href="https://github.com/p3nt4/PowerShdll" target="_blank">PowerShdll</a> project. PowerShx provide functionalities for bypassing AMSI and running PS Cmdlets.</li>
<li><a href="https://github.com/Edubr2020/CVE-2021-40444--CABless/blob/main/MS_Windows_CVE-2021-40444%20-%20'Ext2Prot'%20Vulnerability%20'CABless'%20version.pdf" target="_blank">CVE-2021-40444--CABless</a>. Your favorite Word RCE, now with no CAB and a single line of javascript.</li>
<li><a href="https://github.com/uf0o/CFG_Allowed_Functions" target="_blank">CFG_Allowed_Functions</a> is a <a href="https://githomelab.ru/pykd/pykd" target="_blank">pykd</a> version-independent tool that finds and dump functions allowed by Control Flow Guard (CFG).</li>
<li><a href="https://pulsesecurity.co.nz/advisories/Zerotier-Private-Network-Access" target="_blank">Zerotier - Multiple Vulnerabilities</a>. An attacker may chain Zerotier root-server identity overwriting, insecure identity verification and various information leakage vulnerabilities to gain unauthorized access to private Zerotier networks. To exploit, see <a href="https://github.com/denandz/ZTCrack" target="_blank">ZTCrack</a>.</li>
<li><a href="https://github.com/h3xduck/Umbra" target="_blank">Umbra</a> is an experimental remotely controllable LKM rootkit for kernels 4.x and 5.x (up to 5.7) which opens a network backdoor that can spawn reverse shells to remote hosts, launch malware remotely and much more.</li>
<li><a href="https://github.com/rasta-mouse/Rosplant" target="_blank">Rosplant</a> Pis a proof of concept to leverage Roslyn for post-exploitation (Roslyn + Implant = Rosplant). It comes in two parts, the server and client. Raw C# is entered into the server's console by the attacker, which is sent to the client (via TCP for the PoC). The client uses Roslyn to evaluate the code and sends the results back to the attacker.</li>
<li><a href="https://github.com/Flangvik/SharpExfiltrate" target="_blank">SharpExfiltrate</a> is a tiny but modular C# framework to exfiltrate loot over secure and trusted channels. It supports both single-files and full-directory paths (recursively), file extension filtering, and file size filtering. Exfiltrated data will be compressed and encrypted before being uploaded. While exfiltrating a large amount of data will require the output stream to be cached on disk, smaller exfiltration operations can be done all in memory with the "memoryonly" option.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/CMEPW/Smersh" target="_blank">Smersh</a> is a pentest oriented collaborative tool used to track the progress of your company's missions and generate rapport.</li>
<li><a href="https://depthsecurity.com/blog/obfuscating-malicious-macro-enabled-word-docs" target="_blank">Obfuscating Malicious, Macro-Enabled Word Docs</a>. Missed this one last week, but some great tips on macro-obfuscation techniques for when that Word RCE stops being useful.</li>
<li><a href="https://github.com/s0md3v/be-a-hacker" target="_blank">be-a-hacker</a>. This is a road map to being a self-taught hacker.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
