Title: Last Week in Security (LWiS) - 2022-11-08
Date: 2022-11-08 23:58
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-11-08
Author: Erik
Summary: I'm a day late - sorry!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-10-31 to 2022-11-08.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.openssl.org/blog/blog/2022/11/01/email-address-overflows/" target="_blank">CVE-2022-3786 and CVE-2022-3602: X.509 Email Address Buffer Overflows</a>. Sometimes the hype is just hype. This looks extremely hard to exploit with modern mitigations and a limited userbase.</li>
<li><a href="https://arxiv.org/pdf/2210.08374.pdf" target="_blank">[PDF] How security professionals are being attacked: A study of malicious CVE proof of concept exploits in GitHub</a>. Over 10% of PoCs were malicious! There is a reason there is a disclaimer at the end of each of these posts.</li>
<li><a href="https://krebsonsecurity.com/2022/11/linkedin-adds-verified-emails-profile-creation-dates/" target="_blank">LinkedIn Adds Verified Emails, Profile Creation Dates</a>. Your favorite profile backstop just got a little harder to fake.</li>
<li><a href="https://www.mdsec.co.uk/2022/11/nighthawk-0-2-1-haunting-blue/" target="_blank">Nighthawk 0.2.1 - Haunting Blue</a>. Some cool features in the latest release of this commercial red team tool.</li>
<li><a href="https://www.fortra.com/" target="_blank">Meet Fortra™ The new face of HelpSystems</a>. HelpSystems (Cobalt Strike/Outflank's buyers) have rebranded - now with more generic corporate stock photos.</li>
<li><a href="https://simplex.chat/blog/20221108-simplex-chat-v4.2-security-audit-new-website.html" target="_blank">[SimpleX] Security assessment by Trail of Bits</a>. I've been playing with this new messenger app for a while and I think it has the potential to unseat Signal in a few versions. No shady CIA money, "open source" (but not really), blockchain silliness, etc. The pace of development is also impressive. They list their Monero address above their Bitcoin address - legit.</li>
<li><a href="https://positive.security/blog/urlscan-data-leaks" target="_blank">urlscan.io's SOAR spot: Chatty security tools leaking private data</a>. Careful what you auto-submit to external vendors.</li>
<li><a href="https://www.radare2.online/" target="_blank">radare2.online</a>. Your OS is just a bootloader for your browser. HTML/CSS/Javascript won the language war and will be the universal language of the future. Scary.</li>
<li><a href="https://papers.vx-underground.org/papers/Other/VXUG%20Zines/Black%20Mass%20Halloween%202022.pdf" target="_blank">[PDF] VX-Underground's Black Mass</a>. Tmp.out and vx-underground keep the zine scene alive.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.assetnote.io/2022/10/28/exploiting-static-site-generators/" target="_blank">Exploiting Static Site Generators: When Static Is Not Actually Static</a>. File this under "Serverless and other myths."</li>
<li><a href="https://googleprojectzero.blogspot.com/2022/11/a-very-powerful-clipboard-samsung-in-the-wild-exploit-chain.html" target="_blank">A Very Powerful Clipboard: Analysis of a Samsung in-the-wild exploit chain</a>. Mobile exploit chains are always a trip. This one look surprisingly easy to understand compared to most.</li>
<li><a href="https://captmeelo.com//redteam/maldev/2022/11/07/cloning-signing.html" target="_blank">Lessons Learned from Cloning Windows Binaries and Code Signing Implants</a>. Some good lessons here. Another option is to just used signed binaries for other purposes <a href="https://gitlab.com/badsectorlabs/iscariot-suite" target="_blank">...</a></li>
<li><a href="https://m365internals.com/2022/11/07/how-one-misconfiguration-in-adcs-can-lead-to-full-ad-forest-compromise/" target="_blank">How one misconfiguration in ADCS can lead to full AD Forest compromise</a>. ADCS is the gift that keeps on giving.</li>
<li><a href="https://srd.cx/cve-2022-26730/#h-poc-download" target="_blank">CVE-2022-26730 | ColorSync | Hoyt LLC</a>. macOS memory corruption in the processing of image ICC profiles can lead to RCE. Comes with the shorted PoC I have seen in a while (now patched).</li>
<li><a href="https://blog.zsec.uk/byodc-attack/" target="_blank">BYODC - Bring Your Own Domain Controller</a>. <a href="https://user-images.githubusercontent.com/2307945/35466403-d9a4f3f2-0303-11e8-9d94-a2e4b2df7a2c.jpg" target="_blank">This meme</a> makes a comeback. This is some great traitorware - why fake a DCSync, if you can just do an actual DCSync? <a href="https://www.dcshadow.com/" target="_blank">DCShadow</a> is a previously discovered/implemented version of this.</li>
<li><a href="https://blog.sonarsource.com/checkmk-rce-chain-1/" target="_blank">Checkmk: Remote Code Execution by Chaining Multiple Bugs (1/3)</a>. Quite a chain for unauth RCE across different tech/lanugages.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/CCob/Volumiser" target="_blank">Volumiser</a> is a command line tool and interactive console GUI for listing, browsing and extracting files from common virtual machine hard disk image formats.</li>
<li><a href="https://github.com/projectdiscovery/katana" target="_blank">katana</a> - A next-generation crawling and spidering framework from projectdiscovery.</li>
<li><a href="https://github.com/d3lb3/KeeFarceReborn" target="_blank">KeeFarceReborn</a> - A standalone DLL that exports databases in cleartext once injected in the KeePass process.</li>
<li><a href="https://github.com/Bdenneu/CVE-2022-33679" target="_blank">CVE-2022-33679</a> One day based on <a href="https://googleprojectzero.blogspot.com/2022/10/rc4-is-still-considered-harmful.html" target="_blank">RC4 is still considered harmfrul</a>.</li>
<li><a href="https://github.com/tothi/stager_libpeconv" target="_blank">stager_libpeconv</a> A basic meterpreter protocol stager using the libpeconv library by hasherezade for reflective loading.</li>
<li><a href="https://github.com/cckuailong/CVE-2022-40146_Exploit_Jar" target="_blank">CVE-2022-40146_Exploit_Jar</a>. Apache Batik SSRF to RCE Jar Exploit.</li>
<li><a href="https://github.com/hupe1980/awsrecon" target="_blank">awsrecon</a> - Tool for reconnaissance of AWS cloud environments.</li>
<li><a href="https://github.com/whokilleddb/exe_who" target="_blank">exe_who</a> - Executables on Disk? Bleh 🤮.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://offensivedefence.co.uk/posts/kardashev/" target="_blank">The Information Security Kardashev Scale</a>. Interesting way to tier out cybersecurity.</li>
<li><a href="https://github.com/NetSPI/PowerHuntShares" target="_blank">PowerHuntShares</a> is an audit script designed in inventory, analyze, and report excessive privileges configured on Active Directory domains.</li>
<li><a href="https://github.com/Ascotbe/Kernelhub" target="_blank">Kernelhub</a> 🌴Kernel privilege escalation vulnerability collection, with compilation environment, demo GIF map, vulnerability details, executable file (Windows only).</li>
<li><a href="https://github.com/liamg/grace" target="_blank">grace</a> It's strace, with colors.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 421 (+0)</p>
<p>Blogs monitored: 327 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
